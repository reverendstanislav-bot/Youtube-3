#!/usr/bin/env python3
"""Encode VIDEO008 still assets as exact-duration 25 fps Resolve plates."""

from __future__ import annotations

import csv
import json
import subprocess
from pathlib import Path


FPS = 25
PACK = Path(r"C:\Users\KK\VIDEO008_PRODUCTION\VIDEO008_FINAL_VISUAL_PACK")
HERE = Path(__file__).resolve().parent
OUT = PACK / "RESOLVE_PLATES"


def run(cmd: list[str]) -> str:
    return subprocess.run(cmd, check=True, capture_output=True, text=True).stdout.strip()


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = {r["scene_id"]: r for r in csv.DictReader((PACK / "ASSET_MANIFEST.csv").open(encoding="utf-8-sig", newline=""))}
    scenes = list(csv.DictReader((HERE / "11_SCENE_TIMELINE.csv").open(encoding="utf-8-sig", newline="")))
    fallback = PACK / manifest["SC040"]["final_path"]
    rows = []
    for idx, scene in enumerate(scenes, 1):
        sid = scene["scene_id"]
        item = manifest[sid]
        if item["asset_class"] == "STOCK_VIDEO":
            continue
        source = PACK / item["final_path"] if item["final_path"] else fallback
        frames = int(scene["duration_frames"])
        target = OUT / f"{sid}_PLATE_25FPS.mp4"
        subprocess.run([
            "ffmpeg", "-v", "error", "-y", "-loop", "1", "-i", str(source),
            "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease,"
                   "pad=1920:1080:(ow-iw)/2:(oh-ih)/2:black,fps=25,format=yuv420p",
            "-frames:v", str(frames), "-c:v", "libx264", "-preset", "veryfast", "-crf", "16", "-an", str(target),
        ], check=True)
        probe = json.loads(run([
            "ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0",
            "-show_entries", "stream=avg_frame_rate,nb_read_frames,width,height", "-of", "json", str(target),
        ]))["streams"][0]
        actual = int(probe["nb_read_frames"])
        if actual != frames or probe["avg_frame_rate"] != "25/1" or probe["width"] != 1920 or probe["height"] != 1080:
            raise RuntimeError(f"Plate QC failed for {sid}: {probe}, expected {frames} frames")
        rows.append({
            "scene_id": sid, "source_path": str(source), "plate_path": str(target),
            "frames": frames, "duration_sec": f"{frames/FPS:.3f}",
            "fallback_note": "SC040_CONTEXT_GRAPHIC_NOT_AUTHENTIC_EVIDENCE" if sid == "SC043" else "",
            "qc": "PASS_1920X1080_25FPS_EXACT_FRAMES",
        })
        print(f"[{len(rows):02d}] {sid}: {frames}f", flush=True)
    with (HERE / "11_RESOLVE_PLATE_MANIFEST.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps({"plates": len(rows), "qc": "PASS", "output": str(OUT)}))


if __name__ == "__main__":
    main()
