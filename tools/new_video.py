#!/usr/bin/env python3
"""Create an immutable VIDEO_0XX package from _VIDEO_TEMPLATE and register it."""
from __future__ import annotations
import csv, re, shutil, sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "03_VIDEOS" / "_VIDEO_TEMPLATE"
INDEX = ROOT / "02_PIPELINE" / "VIDEO_INDEX.csv"
VIDEOS = ROOT / "03_VIDEOS"

FIELDS = ["video_id","status","working_title","pillar","current_stage","folder","priority","publish_date","youtube_url"]

def slugify(title: str) -> str:
    return (re.sub(r"[^A-Za-z0-9]+", "_", title.upper()).strip("_")[:56] or "UNTITLED")

def replace_tokens(folder: Path, tokens: dict[str, str]) -> None:
    for path in folder.rglob("*"):
        if not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for key, value in tokens.items():
            text = text.replace("{{" + key + "}}", value)
        path.write_text(text, encoding="utf-8")

def main() -> int:
    if len(sys.argv) < 3:
        print('Usage: python tools/new_video.py <1-999> "Working title" [PILLAR]', file=sys.stderr)
        return 2
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("Video ID must be an integer 1-999.", file=sys.stderr); return 2
    if not 1 <= number <= 999:
        print("Video ID must be between 1 and 999.", file=sys.stderr); return 2
    title = sys.argv[2].strip()
    pillar = sys.argv[3].strip() if len(sys.argv) >= 4 else ""
    if not title:
        print("Working title cannot be empty.", file=sys.stderr); return 2

    video_id = f"{number:03d}"
    existing_dirs = [p for p in VIDEOS.glob(f"VIDEO_{video_id}_*") if p.is_dir()]
    if existing_dirs:
        print(f"Refusing to reuse immutable VIDEO_{video_id}: {existing_dirs[0].name}", file=sys.stderr)
        return 1
    if not TEMPLATE.is_dir() or not INDEX.is_file():
        print("Template or VIDEO_INDEX.csv missing.", file=sys.stderr); return 1

    with INDEX.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    if any((r.get("video_id") or "") == video_id for r in rows):
        print(f"VIDEO_{video_id} is already registered.", file=sys.stderr); return 1

    slug = slugify(title)
    dest = VIDEOS / f"VIDEO_{video_id}_{slug}"
    shutil.copytree(TEMPLATE, dest)
    today = date.today().isoformat()
    replace_tokens(dest, {"VIDEO_ID":video_id,"TITLE":title,"SLUG":slug,"CREATED_AT":today})

    manifest = dest / "manifest.yaml"
    if pillar:
        text = manifest.read_text(encoding="utf-8")
        text = re.sub(r'^pillar:\s*""$', f'pillar: "{pillar}"', text, flags=re.M)
        manifest.write_text(text, encoding="utf-8")

    rows.append({
        "video_id":video_id,"status":"CANDIDATE","working_title":title,"pillar":pillar,
        "current_stage":"BRIEF","folder":str(dest.relative_to(ROOT)).replace("\\","/"),
        "priority":"","publish_date":"","youtube_url":""
    })
    rows.sort(key=lambda r: int(r["video_id"]))
    with INDEX.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS, lineterminator="\n")
        w.writeheader(); w.writerows(rows)
    print(f"Created {dest.relative_to(ROOT)} and registered immutable VIDEO_{video_id}.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
