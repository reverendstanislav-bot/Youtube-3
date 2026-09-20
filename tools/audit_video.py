#!/usr/bin/env python3
"""Stage-aware audit with legal-status and claim/source integrity checks."""
from __future__ import annotations
import argparse, csv, json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
VIDEOS=ROOT/"03_VIDEOS"
ALLOWED_LEGAL={"ALLEGATION","COMPLAINT","CLAIM","CHARGE","RULING","VERDICT","SETTLEMENT","DISMISSAL","CONVICTION","ADMISSION","DENIAL","UNDISPUTED_FACT","REPORTED_FACT","OPINION","ANALYSIS","UNKNOWN_REQUIRES_REVIEW"}
LEGAL_PRIMARY={"COMPLAINT","CHARGE","RULING","VERDICT","SETTLEMENT","DISMISSAL","CONVICTION","ADMISSION"}
BASE={"STATE.md","manifest.yaml","VERSION_LOG.md","QA_LEDGER.csv","ASSET_MANIFEST.csv"}
STAGE_REQUIRED={
"BRIEF":BASE|{"00_BRIEF.md","00_TOPIC_QUALIFICATION.md"},
"00_TOPIC_QUALIFICATION":BASE|{"00_BRIEF.md","00_TOPIC_QUALIFICATION.md"},
"01_EVIDENCE_RESEARCH":BASE|{"01_DEEP_RESEARCH.md","SOURCE_INDEX.csv","CLAIMS_LEDGER.csv","CASE_EVENT_LEDGER.csv","FACT_CHECK.md"},
"02_CASE_STORY_MAP":BASE|{"01_DEEP_RESEARCH.md","SOURCE_INDEX.csv","CLAIMS_LEDGER.csv","CASE_EVENT_LEDGER.csv","02_STORY_MAP.md","02_TIMELINE.csv"},
"03_SCRIPT_V1":BASE|{"03_SCRIPT_V1.md","SOURCE_INDEX.csv","CLAIMS_LEDGER.csv","CASE_EVENT_LEDGER.csv"},
"04_FACT_LEGAL_REVIEW":BASE|{"03_SCRIPT_V1.md","04_FACT_LEGAL_REVIEW.md","SOURCE_INDEX.csv","CLAIMS_LEDGER.csv","CASE_EVENT_LEDGER.csv"},
"05_SCRIPT_REVISION":BASE|{"04_FACT_LEGAL_REVIEW.md","05_SCRIPT_V2.md","CLAIMS_LEDGER.csv"},
"06_PERFORMANCE_REVIEW":BASE|{"05_SCRIPT_V2.md","06_PERFORMANCE_REVIEW.md","CLAIMS_LEDGER.csv"},
"07_SCRIPT_LOCK":BASE|{"07_SCRIPT_FINAL.md","SOURCE_INDEX.csv","CLAIMS_LEDGER.csv","CASE_EVENT_LEDGER.csv"},
"08_VOICE_SCRIPT":BASE|{"07_SCRIPT_FINAL.md","08_VOICE_SCRIPT.md"},
"09_VOICE_QA_LOCK":BASE|{"07_SCRIPT_FINAL.md","08_VOICE_SCRIPT.md","09_VOICE_REVIEW.md"},
"10_AUDIO_MASTER":BASE|{"07_SCRIPT_FINAL.md","10_AUDIO_MASTER.md"},
"11_TRANSCRIPT_VISUAL_TIMELINE":BASE|{"10_AUDIO_MASTER.md","11_WORD_LEVEL_TRANSCRIPT.json","11_VISUAL_TIMELINE.md","SCENE_TIMELINE.csv"},
"12_VISUAL_SOURCE_GENERATION_PLAN":BASE|{"11_VISUAL_TIMELINE.md","12_VISUAL_SOURCE_PLAN.md","12_IMAGE_PROMPTS.md","12_RECONSTRUCTION_PROMPTS.md"},
"13_VISUAL_ASSET_QC":BASE|{"13_GENERATION_QC.csv","13_SOURCE_VISUAL_QC.csv","ASSET_MANIFEST.csv"},
"14_GRAPHICS_DOCUMENTS_MUSIC_SFX":BASE|{"14_GRAPHICS_PLAN.md","14_DOCUMENT_PLAN.md","14_MUSIC_SFX_PLAN.md","14_OVERLAYS.md"},
"15_ASSEMBLY_EDIT":BASE|{"15_ASSEMBLY_PLAN.md","15_EDIT_QC.md"},
"16_FINAL_FACT_LEGAL_REFRESH":BASE|{"16_FINAL_FACT_LEGAL_REFRESH.md","16_COPYRIGHT_PROVENANCE_AUDIT.md","SOURCE_INDEX.csv","CLAIMS_LEDGER.csv","CASE_EVENT_LEDGER.csv"},
"17_PACKAGING":BASE|{"16_FINAL_FACT_LEGAL_REFRESH.md","17_PACKAGING.md","17_TITLE_CANDIDATES.csv","17_THUMBNAIL_CONCEPTS.md","17_PACKAGING_QC.md"},
"18_UPLOAD_PREPUBLICATION":BASE|{"18_UPLOAD_PACKAGE.md","18_PREPUBLICATION_QC.md","17_PACKAGING_QC.md","16_FINAL_FACT_LEGAL_REFRESH.md"},
"19_POST_PUBLISH_ANALYTICS":BASE|{"19_ANALYTICS.md","19_ANALYTICS_SNAPSHOTS.csv","19_EXPERIMENT_LOG.csv"},
}
UNRESOLVED=re.compile(r"\{\{[^}]+\}\}|\bTODO\b",re.I)

def scalar(text,key):
    m=re.search(rf'^{re.escape(key)}:\s*["\']?([^"\'\n]+)["\']?\s*$',text,re.M)
    return m.group(1).strip() if m else ""

def rows(path):
    if not path.exists(): return []
    with path.open(newline="",encoding="utf-8") as f: return list(csv.DictReader(f))

def audit(folder:Path, force_strict=False):
    errors=[]; warns=[]
    mp=folder/"manifest.yaml"
    if not mp.exists(): return ["missing manifest.yaml"],[]
    text=mp.read_text(encoding="utf-8")
    vid=scalar(text,"video_id"); stage=scalar(text,"current_stage"); status=scalar(text,"status")
    m=re.fullmatch(r"VIDEO_(\d{3})_[A-Z0-9_]+",folder.name)
    if not m: errors.append("invalid folder name")
    elif vid!=m.group(1): errors.append(f"manifest video_id {vid!r} != folder ID {m.group(1)}")

    required=STAGE_REQUIRED.get(stage,BASE)
    missing=sorted(x for x in required if not (folder/x).is_file())
    if missing: errors.append("missing required files for stage "+stage+": "+", ".join(missing))

    strict=force_strict or status in {"RELEASE_READY","SCHEDULED","PUBLISHED"} or stage in {"17_PACKAGING","18_UPLOAD_PREPUBLICATION","19_POST_PUBLISH_ANALYTICS"}

    sources=rows(folder/"SOURCE_INDEX.csv")
    source_ids={(r.get("source_id") or "").strip() for r in sources if (r.get("source_id") or "").strip()}
    claims=rows(folder/"CLAIMS_LEDGER.csv")
    for i,r in enumerate(claims,1):
        cid=(r.get("claim_id") or f"row{i}").strip()
        if not (r.get("claim_text") or "").strip(): continue
        ls=(r.get("legal_status") or "").strip().upper()
        if ls not in ALLOWED_LEGAL: errors.append(f"{cid}: invalid legal_status {ls!r}")
        if ls=="UNKNOWN_REQUIRES_REVIEW": errors.append(f"{cid}: material legal status unresolved")
        sids=[x.strip() for x in re.split(r"[;|]",r.get("source_ids") or "") if x.strip()]
        if ls not in {"OPINION","ANALYSIS"} and not sids:
            errors.append(f"{cid}: missing source_ids")
        missing_s=[x for x in sids if x not in source_ids]
        if missing_s: errors.append(f"{cid}: unresolved source IDs {', '.join(missing_s)}")
        ver=(r.get("verification_status") or "").strip().upper()
        if strict and ver not in {"VERIFIED","SUPPORTED","ATTRIBUTED","ANALYSIS","N/A"}:
            errors.append(f"{cid}: verification_status not release-ready: {ver!r}")
        primary=(r.get("primary_source_present") or "").strip().lower()
        if strict and ls in LEGAL_PRIMARY and primary not in {"yes","true","1"}:
            errors.append(f"{cid}: {ls} requires primary-source confirmation before release")

    qa=rows(folder/"QA_LEDGER.csv")
    if strict:
        open_critical=[r.get("issue_id","?") for r in qa if (r.get("severity") or "").upper() in {"BLOCKER","HIGH"} and (r.get("resolution_status") or "").upper() not in {"RESOLVED","ACCEPTED_WITH_RATIONALE","REJECTED_WITH_REASON"}]
        if open_critical: errors.append("unresolved BLOCKER/HIGH QA: "+", ".join(open_critical[:20]))
        refresh=scalar(text,"last_case_status_refresh")
        if not refresh: errors.append("release-stage manifest requires last_case_status_refresh")

    st=folder/"STATE.md"
    if st.exists() and status and status not in st.read_text(encoding="utf-8"):
        warns.append("STATE.md may not mirror manifest status")

    transcript=folder/"11_WORD_LEVEL_TRANSCRIPT.json"
    if transcript.exists():
        try: json.loads(transcript.read_text(encoding="utf-8"))
        except Exception as e: errors.append(f"11_WORD_LEVEL_TRANSCRIPT.json invalid JSON: {e}")

    if strict:
        for p in folder.iterdir():
            if p.is_file() and p.suffix.lower() in {".md",".yaml",".yml",".json",".csv",".txt"}:
                try: t=p.read_text(encoding="utf-8")
                except UnicodeDecodeError: continue
                if UNRESOLVED.search(t): errors.append(f"unresolved template token/TODO in {p.name}")

    return errors,warns

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("folder",nargs="?"); ap.add_argument("--strict",action="store_true"); ap.add_argument("--all",action="store_true"); a=ap.parse_args()
    if a.all: targets=[p for p in sorted(VIDEOS.iterdir()) if p.is_dir() and p.name!="_VIDEO_TEMPLATE"]
    elif a.folder:
        p=Path(a.folder); targets=[p if p.is_absolute() else ROOT/p]
    else: ap.error("provide VIDEO folder or --all")
    errors=[]; warns=[]
    for p in targets:
        e,w=audit(p,a.strict); errors += [f"{p.name}: {x}" for x in e]; warns += [f"{p.name}: {x}" for x in w]
    for w in warns: print("WARN:",w)
    for e in errors: print("FAIL:",e)
    if errors:
        print(f"AUDIT FAILED: {len(errors)} fail(s), {len(warns)} warning(s)"); return 1
    print(f"AUDIT PASSED: {len(targets)} video package(s), {len(warns)} warning(s)"); return 0

if __name__=="__main__":
    raise SystemExit(main())
