"""Validate the unique still plan; emit reproducible derived-file apply_patch with --patch.

No network, generation, media editing or automatic file writes. Frame end is exclusive.
"""
from __future__ import annotations

import argparse
import csv
import difflib
import hashlib
import io
import json
import re
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent
PLAN = BASE / "12_GENERATION_PLAN_V4.json"


def csv_text(rows: list[dict]) -> str:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue()


def build() -> dict[str, str]:
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    with (BASE / plan["timing_source"]).open(encoding="utf-8-sig", newline="") as stream:
        cues = {row["scene_id"]: row for row in csv.DictReader(stream)}
    with (BASE / "SOURCE_INDEX.csv").open(encoding="utf-8-sig", newline="") as stream:
        sources = {row["source_id"] for row in csv.DictReader(stream)}
    with (BASE / "CLAIMS_LEDGER.csv").open(encoding="utf-8-sig", newline="") as stream:
        claims = {row["claim_id"] for row in csv.DictReader(stream)}
    assets = plan["assets"]
    assert len({a["id"] for a in assets}) == len(assets), "Duplicate asset ID"
    assert [a["id"] for a in assets] == [f"GF{i:03}" for i in range(1, len(assets)+1)]
    assert len(cues) == 124 and "SC124" in cues
    assert plan["paid_jobs_authorized_this_task"] == plan["paid_jobs_submitted_this_task"] == 0
    mapped: list[dict] = []
    manifest: list[dict] = []
    for asset in assets:
        assert all(asset[k] for k in ("type", "uses", "visible_text", "direction", "new_frame_reason", "reuse_reason"))
        assert all(not re.search(r"[\u0400-\u04ff]", text) for text in asset["visible_text"])
        linked_sources: set[str] = set()
        linked_claims: set[str] = set()
        linked_beats: set[str] = set()
        linked_scenes: set[str] = set()
        for use in asset["uses"]:
            match = re.fullmatch(r"(SC\d{3})(?:-(SC\d{3}))?(?:@(START|\d+):(END|\d+))?", use)
            assert match, f"Invalid use {use}"
            first, last, local_start, local_end = match.groups()
            assert not (last and local_start), "Partial range not supported"
            names = [f"SC{i:03}" for i in range(int(first[2:]), int((last or first)[2:])+1)]
            for name in names:
                cue = cues[name]
                start, end = int(cue["start_frame"]), int(cue["end_frame"])
                if local_start and local_start != "START":
                    start = int(local_start)
                if local_end and local_end != "END":
                    end = int(local_end)
                assert int(cue["start_frame"]) <= start < end <= int(cue["end_frame"]), use
                src = set(filter(None, cue["source_ids"].split(";")))
                clm = set(filter(None, cue["claim_ids"].split(";")))
                assert src <= sources and clm <= claims, name
                linked_sources |= src
                linked_claims |= clm
                linked_beats.add(cue["beat_id"])
                linked_scenes.add(name)
                mapped.append({"scene_id":name,"script_ref":cue["script_ref"],"asset_id":asset["id"],"start_frame":start,"end_frame":end,"start_sec":f"{start/25:.2f}","end_sec":f"{end/25:.2f}","beat_id":cue["beat_id"],"claim_ids":cue["claim_ids"],"source_ids":cue["source_ids"],"short_ids":cue["short_ids"],"use_status":"","edit_rule":"SAME_COMPLETE_IMAGE;NO_TEXT_SWAP;NO_SHAKE;PROVISIONAL_TIMING"})
        assert linked_sources or asset["type"] == "ENDSCREEN", asset["id"]
        label = "RECREATION / NOT AN ORIGINAL DOCUMENT" if asset["type"] == "RECREATED_DOCUMENT" else ("" if asset["type"] == "ENDSCREEN" else "ILLUSTRATION")
        manifest.append({"asset_id":asset["id"],"asset_type":asset["type"],"scene_ids":";".join(sorted(linked_scenes)),"beat_ids":";".join(sorted(linked_beats)),"claim_ids":";".join(sorted(linked_claims)),"source_ids":";".join(sorted(linked_sources)),"visible_text":" | ".join(asset["visible_text"]),"mandatory_label":label,"direction":asset["direction"],"new_frame_reason":asset["new_frame_reason"],"reuse_reason":asset["reuse_reason"],"generation_status":"NOT_SUBMITTED","generation_job_id":"","approved_asset_path":"","provider":"Higgsfield_REQUESTED","model":"NOT_SELECTED","cost":"NOT_QUOTED","frame_format":"16:9_FULL_FRAME","safe_bottom_percent":20})
    mapped.sort(key=lambda row:row["start_frame"])
    cursor = 0
    seen: set[str] = set()
    placements: list[dict] = []
    for row in mapped:
        assert row["start_frame"] == cursor, f"Gap/overlap at {cursor}: {row}"
        cursor = row["end_frame"]
        row["use_status"] = "REUSE" if row["asset_id"] in seen else "FIRST_USE"
        seen.add(row["asset_id"])
        if placements and placements[-1]["asset_id"] == row["asset_id"] and placements[-1]["end_frame"] == row["start_frame"]:
            placements[-1]["end_frame"] = row["end_frame"]
            placements[-1]["scene_ids"].append(row["scene_id"])
        else:
            placements.append({"asset_id":row["asset_id"],"start_frame":row["start_frame"],"end_frame":row["end_frame"],"scene_ids":[row["scene_id"]]})
    assert cursor == 20700 and mapped[-1]["scene_id"] == "SC124"
    assert set(row["scene_id"] for row in mapped) == set(cues)
    assert set(row["beat_id"] for row in mapped) == set(c["beat_id"] for c in cues.values())
    assert mapped[-1]["start_frame"] == 20200 and assets[-1]["type"] == "ENDSCREEN"
    assert sum(a["type"] == "ENDSCREEN" for a in assets) == 1
    # Preserve story answers until their actual cue; no early baked-in text reveal.
    for asset_id, first_scene in {"GF012":"SC021", "GF017":"SC037", "GF024":"SC050", "GF031":"SC070", "GF047":"SC100"}.items():
        assert next(row for row in mapped if row["asset_id"] == asset_id)["scene_id"] == first_scene
    narration = [p for p in placements if p["asset_id"] != assets[-1]["id"]]
    report = {
        "status":"STRUCTURAL_PLAN_PASS_NOT_MEDIA_QC",
        "unique_generated_frame_slots":len(assets),
        "narrative_frame_slots":len(assets)-1,
        "silent_endscreen_frame_slots":1,
        "category_counts":dict(sorted(Counter(a["type"] for a in assets).items())),
        "timeline_cues_covered":len(cues),
        "cue_segments":len(mapped),
        "narrative_macro_beats_covered":len({row["beat_id"] for row in mapped if row["scene_id"] != "SC124"}),
        "endscreen_beats_covered":1,
        "continuous_image_placements_including_reuses":len(placements),
        "repeat_placements_without_new_generation":len(placements)-len(assets),
        "narration_placements":len(narration),
        "max_narration_image_hold_sec":max((p["end_frame"]-p["start_frame"])/25 for p in narration),
        "average_narration_image_hold_sec":round(808/len(narration),3),
        "fps":25,"covered_frames":cursor,"planned_video_sec":cursor/25,
        "paid_jobs_submitted_this_task":0,
        "accepted_generated_files":"NOT_ESTABLISHED_BY_THIS_PLANNING_TASK",
        "shorts":{sid:sorted({r["asset_id"] for r in mapped if sid in r["short_ids"].split(";")}) for sid in ("SH01","SH02","SH04","SH08")},
        "excluded":"Shorts vertical variants/CTA, thumbnails, optional alternatives, retries and rejected Fusion states are not mandatory long-form frame slots.",
        "locks":"Audio auditory QC, timeline final lock, generated-image QC, edit and release remain open. Count is exact for this V11 plan, not a guarantee of successful job attempts or future revisions.",
        "input_sha256_scheme":"UTF8_TEXT_LF_NORMALIZED_FOR_CROSS_PLATFORM_REPRODUCIBILITY",
        "input_sha256":{name:hashlib.sha256((BASE/name).read_text(encoding="utf-8").encode("utf-8")).hexdigest() for name in (PLAN.name,"07_SCRIPT_FINAL.md","SCENE_TIMELINE.csv","11_SHORTS_CUT_MAP.csv")}
    }
    return {"12_GENERATION_ASSET_MANIFEST_V4.csv":csv_text(manifest),"12_GENERATION_CUE_MAP_V4.csv":csv_text(mapped),"12_GENERATION_COUNT_V4.json":json.dumps(report,ensure_ascii=False,indent=2)+"\n"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--patch",action="store_true")
    args = parser.parse_args()
    outputs = build()
    if args.patch:
        print("*** Begin Patch")
        for name, content in outputs.items():
            if (BASE/name).exists():
                old = (BASE/name).read_text(encoding="utf-8")
                if old == content:
                    continue
                print(f"*** Update File: {(BASE/name).as_posix()}")
                for line in list(difflib.unified_diff(old.splitlines(), content.splitlines(), lineterm=""))[2:]:
                    print("@@" if line.startswith("@@") else line)
            else:
                print(f"*** Add File: {(BASE/name).as_posix()}")
                for line in content.splitlines():
                    print("+"+line)
        print("*** End Patch")
    else:
        for name, content in outputs.items():
            assert (BASE/name).read_text(encoding="utf-8") == content, f"Stale derived output: {name}"
        print(outputs["12_GENERATION_COUNT_V4.json"])


if __name__ == "__main__":
    main()
