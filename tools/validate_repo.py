#!/usr/bin/env python3
"""Validate the YouTube 3 business/legal documentary repository contract."""
from __future__ import annotations
import csv, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VIDEOS = ROOT / "03_VIDEOS"
INDEX = ROOT / "02_PIPELINE" / "VIDEO_INDEX.csv"
BACKLOG = ROOT / "02_PIPELINE" / "TOPIC_BACKLOG.csv"

ALLOWED_TOP = {".github","00_FOUNDATION","00_CORE","01_CHANNEL","02_PIPELINE","03_VIDEOS","04_SHARED","tools"}
ROOT_REQUIRED = {"README.md","AGENTS.md",".gitignore"}
FOUNDATION_REQUIRED = {
    "README.md","CHANNEL_LOCKS.md","POSITIONING.md","CONTENT_PILLARS.md",
    "TOPIC_QUALIFICATION_LOCK.md","LAUNCH_BATCH.csv","SOURCE_HIERARCHY.md",
    "LEGAL_LANGUAGE_LOCKS.md","REVIEW_METRICS.md","BRAND_LOCK.md","VOICE_LOCK.md"
}
CORE_REQUIRED = {
    "AGENT_PROTOCOL.md","AGENT_PLAYBOOK.md","REPOSITORY_CONTRACT.md","NAMING.md",
    "STATUS_SCHEMA.md","VIDEO_SCHEMA.md","LEGAL_STATUS_SCHEMA.md","SOURCE_SCHEMA.md",
    "TOPIC_QUALIFICATION_SCHEMA.md","CHANNEL_OPERATING_MAP.md","QUALITY_GATES.md",
    "PRODUCTION_PIPELINE.md","TASK_RECIPES.md","STORAGE_POLICY.md",
    "YOUTUBE_LAUNCH_SYSTEM.md","PUBLISH_ANALYTICS_SCHEMA.md"
}
CHANNEL_REQUIRED = {
    "CHANNEL_BIBLE.md","STORYTELLING_BIBLE.md","FACT_CHECK_POLICY.md",
    "LEGAL_EDITORIAL_POLICY.md","COMPETITOR_RESEARCH_POLICY.md",
    "SOURCE_CAPTURE_GUIDE.md","CLAIMS_WORDING_GUIDE.md","CHANNEL_LAUNCH_STRATEGY.md",
    "VISUAL_BIBLE.md","VOICE_BIBLE.md","TITLE_SYSTEM.md","THUMBNAIL_SYSTEM.md",
    "REFERENCE_CHANNELS.csv"
}
PIPELINE_ALLOWED = {"README.md","TOPIC_BACKLOG.csv","VIDEO_INDEX.csv"}
SHARED_REQUIRED = {"README.md","ASSET_REGISTRY.csv","PROMPT_COMPONENTS.md","DOCUMENT_VISUAL_POLICY.md","GRAPHICS_COMPONENTS.md"}
TEMPLATE_REQUIRED = {
"00_BRIEF.md","00_TOPIC_QUALIFICATION.md","01_DEEP_RESEARCH.md","01_COMPETITOR_RESEARCH.csv","SOURCE_INDEX.csv","CLAIMS_LEDGER.csv","CASE_EVENT_LEDGER.csv","FACT_CHECK.md",
"02_STORY_MAP.md","02_TIMELINE.csv","03_SCRIPT_V1.md","04_FACT_LEGAL_REVIEW.md","05_SCRIPT_V2.md","06_PERFORMANCE_REVIEW.md","07_SCRIPT_FINAL.md",
"08_VOICE_SCRIPT.md","09_VOICE_REVIEW.md","10_AUDIO_MASTER.md","11_WORD_LEVEL_TRANSCRIPT.json","11_VISUAL_TIMELINE.md","SCENE_TIMELINE.csv",
"12_VISUAL_SOURCE_PLAN.md","12_IMAGE_PROMPTS.md","12_RECONSTRUCTION_PROMPTS.md","13_GENERATION_QC.csv","13_SOURCE_VISUAL_QC.csv",
"14_GRAPHICS_PLAN.md","14_DOCUMENT_PLAN.md","14_MUSIC_SFX_PLAN.md","14_OVERLAYS.md","15_ASSEMBLY_PLAN.md","15_EDIT_QC.md",
"16_FINAL_FACT_LEGAL_REFRESH.md","16_COPYRIGHT_PROVENANCE_AUDIT.md","17_PACKAGING.md","17_TITLE_CANDIDATES.csv","17_THUMBNAIL_CONCEPTS.md","17_PACKAGING_QC.md",
"18_UPLOAD_PACKAGE.md","18_PREPUBLICATION_QC.md","19_ANALYTICS.md","19_ANALYTICS_SNAPSHOTS.csv","19_EXPERIMENT_LOG.csv",
"STATE.md","manifest.yaml","VERSION_LOG.md","QA_LEDGER.csv","ASSET_MANIFEST.csv","QC_CHECKLIST.md"
}
VIDEO_LOCAL = {"SOURCE_INDEX.csv","CLAIMS_LEDGER.csv","CASE_EVENT_LEDGER.csv","QA_LEDGER.csv","ASSET_MANIFEST.csv","SCENE_TIMELINE.csv","13_GENERATION_QC.csv","13_SOURCE_VISUAL_QC.csv"}
BACKLOG_REQUIRED_FIELDS = {
    "topic_id","pillar","company_or_creator","working_title","recognizability",
    "money_stakes","conflict","legal_mechanism","hidden_problem","consequence",
    "primary_source_availability","timeliness","competition","visual_potential",
    "story_potential","risk_level","qualification_score","hard_gate_status",
    "qualification_decision","last_checked","video_id","status","notes"
}

def scalar(text: str, key: str) -> str:
    m = re.search(rf'^{re.escape(key)}:\s*["\']?([^"\'\n]+)["\']?\s*$', text, re.M)
    return m.group(1).strip() if m else ""

def manifest_data(path: Path) -> dict[str,str]:
    if not path.exists(): return {}
    t = path.read_text(encoding="utf-8")
    return {k:scalar(t,k) for k in ("video_id","status","current_stage","title","pillar")}

def main() -> int:
    errors=[]
    top={p.name for p in ROOT.iterdir() if p.is_dir() and p.name != ".git"}
    extra=sorted(top-ALLOWED_TOP)
    if extra: errors.append("Unknown top-level directories: "+", ".join(extra))
    for n in ROOT_REQUIRED:
        if not (ROOT/n).is_file(): errors.append("Missing root file: "+n)

    for label,base,required in [
        ("00_FOUNDATION",ROOT/"00_FOUNDATION",FOUNDATION_REQUIRED),
        ("00_CORE",ROOT/"00_CORE",CORE_REQUIRED),
        ("01_CHANNEL",ROOT/"01_CHANNEL",CHANNEL_REQUIRED),
        ("04_SHARED",ROOT/"04_SHARED",SHARED_REQUIRED),
    ]:
        miss=sorted(n for n in required if not (base/n).is_file())
        if miss: errors.append(label+" missing: "+", ".join(miss))

    pipe=ROOT/"02_PIPELINE"
    if not pipe.is_dir(): errors.append("Missing 02_PIPELINE")
    else:
        extras=sorted(p.name for p in pipe.iterdir() if p.name not in PIPELINE_ALLOWED)
        if extras: errors.append("02_PIPELINE contains workspace files: "+", ".join(extras))

    if not BACKLOG.is_file():
        errors.append("Missing TOPIC_BACKLOG.csv")
    else:
        with BACKLOG.open(newline="",encoding="utf-8") as f:
            reader=csv.DictReader(f)
            fields=set(reader.fieldnames or [])
            missing_fields=sorted(BACKLOG_REQUIRED_FIELDS-fields)
            if missing_fields: errors.append("TOPIC_BACKLOG missing fields: "+", ".join(missing_fields))
            backlog_rows=list(reader)
        topic_ids=[(r.get("topic_id") or "").strip() for r in backlog_rows]
        if len(topic_ids)!=len(set(topic_ids)):
            errors.append("Duplicate topic_id in TOPIC_BACKLOG")

    template=VIDEOS/"_VIDEO_TEMPLATE"
    if not template.is_dir(): errors.append("Missing _VIDEO_TEMPLATE")
    else:
        miss=sorted(n for n in TEMPLATE_REQUIRED if not (template/n).is_file())
        if miss: errors.append("Template missing: "+", ".join(miss))

    rows=[]
    if not INDEX.is_file(): errors.append("Missing VIDEO_INDEX.csv")
    else:
        with INDEX.open(newline="",encoding="utf-8") as f: rows=list(csv.DictReader(f))
    ids=[(r.get("video_id") or "").strip() for r in rows]
    if len(ids)!=len(set(ids)): errors.append("Duplicate video_id in VIDEO_INDEX")
    if ids and ids != sorted(ids, key=int): errors.append("VIDEO_INDEX must be numerically sorted")

    indexed={}
    for r in rows:
        vid=(r.get("video_id") or "").strip()
        if not re.fullmatch(r"\d{3}",vid): errors.append(f"Invalid video_id {vid!r}"); continue
        folder=(r.get("folder") or "").strip()
        if not folder: errors.append(f"VIDEO_{vid}: folder required"); continue
        if vid in indexed: errors.append(f"VIDEO_{vid}: duplicate index registration")
        indexed[vid]=folder
        p=ROOT/folder
        if not p.is_dir(): errors.append(f"VIDEO_{vid}: missing folder {folder}"); continue
        md=manifest_data(p/"manifest.yaml")
        for key,col in (("video_id","video_id"),("status","status"),("current_stage","current_stage"),("title","working_title"),("pillar","pillar")):
            if md.get(key,"") != (r.get(col) or "").strip():
                errors.append(f"VIDEO_{vid}: index {col} != manifest {key}")

    seen_dirs={}
    if VIDEOS.is_dir():
        for p in VIDEOS.iterdir():
            if not p.is_dir() or p.name=="_VIDEO_TEMPLATE": continue
            m=re.fullmatch(r"VIDEO_(\d{3})_[A-Z0-9_]+",p.name)
            if not m: errors.append("Invalid video folder: "+p.name); continue
            vid=m.group(1)
            if vid in seen_dirs: errors.append(f"Duplicate immutable video ID {vid}: {seen_dirs[vid]} and {p.name}")
            seen_dirs[vid]=p.name
            if vid not in indexed: errors.append(f"Unregistered video folder: {p.relative_to(ROOT)}")
            elif indexed[vid] != str(p.relative_to(ROOT)).replace("\\","/"):
                errors.append(f"VIDEO_{vid}: index folder points elsewhere")

    for p in ROOT.rglob("*"):
        if not p.is_file(): continue
        rel=p.relative_to(ROOT)
        if rel.parts and rel.parts[0]=="03_VIDEOS": continue
        if p.name in VIDEO_LOCAL:
            errors.append(f"Video-local ledger outside 03_VIDEOS: {rel}")

    if errors:
        print("REPOSITORY CONTRACT FAILED")
        for e in errors: print("- "+e)
        return 1
    print(f"REPOSITORY CONTRACT PASSED: {len(rows)} registered video package(s).")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
