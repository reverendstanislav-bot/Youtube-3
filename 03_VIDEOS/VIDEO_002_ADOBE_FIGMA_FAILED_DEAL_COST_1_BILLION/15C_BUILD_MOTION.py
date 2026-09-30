#!/usr/bin/env python3
"""VIDEO 002 — Stage 15C: motion edit (owner feedback: "looks like a slideshow").

Per beat: slow push-in / pull-out / lateral drift on the locked 1080p frame.
Between beats: 0.5 s cross-dissolve; at chapter (section) changes: 0.9 s dip to black.
Every transition is centred on the original cut, so picture stays in sync with the
locked Harrison narration. Stage 15B captions are burned on top; voice-only audio.

Output (outside Git): <media>/15C_MOTION/VIDEO_002_STAGE15C_REVIEW_V1_1080P25.mp4
"""
import csv, hashlib, json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
MEDIA = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("C:/Users/KK/Documents/WhatItCost_media/002-adobe-figma")
FRAMES = HERE / "15_FINAL_FRAMES_1080P"
AUDIO = MEDIA / "15_ASSEMBLY_V2" / "HARRISON_AUDIO_MASTER.mp3"
ASS = MEDIA / "15B_CAPTIONS" / "VIDEO_002_STAGE15B_CAPTIONS.ass"
FONTS = MEDIA.parent / "_fonts"
OUT = MEDIA / "15C_MOTION"
CLIPS = OUT / "clips"
CLIPS.mkdir(parents=True, exist_ok=True)
REVIEW = OUT / "VIDEO_002_STAGE15C_REVIEW_V1_1080P25.mp4"
RUNTIME = 940.617
FPS = 25
T_CUT, T_CHAPTER = 0.5, 0.9

rows = list(csv.DictReader(open(HERE / "11_VISUAL_TIMELINE.csv", encoding="utf-8-sig")))
rows.sort(key=lambda r: int(r["generation_slot"][1:]))
assert len(rows) == 110
starts = [float(r["start"]) for r in rows] + [RUNTIME]
starts[0] = 0.0
chapter_change = [False] + [rows[i]["section"] != rows[i - 1]["section"] for i in range(1, 110)]
trans = [T_CHAPTER if chapter_change[i] else T_CUT for i in range(110)]  # transition INTO beat i

# Motion recipes cycle so consecutive beats never repeat; zoom stays within 1.00-1.10.
MOVES = ["in", "left", "out", "right", "in", "up", "out"]

def zp(move, n):
    on = f"(on/{max(n - 1, 1)})"
    ease = f"(0.5-0.5*cos(PI*{on}))"
    z0, z1 = {"in": (1.0, 1.10), "out": (1.10, 1.0)}.get(move, (1.06, 1.06))
    z = f"{z0}+({z1}-{z0})*{ease}"
    cx, cy = "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"
    span = "(iw-iw/zoom)"
    x = {"left": f"{span}*(1-{ease})", "right": f"{span}*{ease}"}.get(move, cx)
    y = {"up": f"(ih-ih/zoom)*(1-{ease})*0.6+(ih-ih/zoom)*0.2"}.get(move, cy)
    return f"zoompan=z='{z}':x='{x}':y='{y}':d={n}:s=1920x1080:fps={FPS}"

def clip(i):
    if os.environ.get("REUSE_CLIPS") and (CLIPS / f"C{i + 1:03d}.mp4").exists():
        return i, 0.0
    lead = trans[i] / 2 if i > 0 else 0.0
    tail = trans[i + 1] / 2 if i < 109 else 0.0
    dur = (starts[i + 1] - starts[i]) + lead + tail
    n = max(2, round(dur * FPS))
    out = CLIPS / f"C{i + 1:03d}.mp4"
    vf = (f"scale=3840:2160:flags=lanczos,{zp(MOVES[i % len(MOVES)], n)},"
          f"format=yuv420p,setsar=1")
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-loop", "1",
                    "-framerate", str(FPS), "-i", str(FRAMES / f"F{i + 1:03d}.jpg"),
                    "-vf", vf, "-frames:v", str(n), "-c:v", "libx264", "-preset", "fast",
                    "-crf", "14", "-r", str(FPS), str(out)], check=True)
    return i, n / FPS

with ThreadPoolExecutor(max_workers=max(2, (os.cpu_count() or 4) // 2)) as ex:
    lengths = dict(ex.map(clip, range(110)))

# xfade chain: transition into beat i starts at (cut_i - trans_i/2) on the output timeline.
inputs, parts = [], []
for i in range(110):
    inputs += ["-i", str(CLIPS / f"C{i + 1:03d}.mp4")]
prev = "[0:v]"
for i in range(1, 110):
    t = trans[i]
    offset = starts[i] - t / 2
    kind = "fadeblack" if chapter_change[i] else "fade"
    lab = f"[v{i}]"
    parts.append(f"{prev}[{i}:v]xfade=transition={kind}:duration={t}:offset={offset:.3f}{lab}")
    prev = lab
fonts_rel = Path(os.path.relpath(FONTS, OUT)).as_posix()
ass_rel = Path(os.path.relpath(ASS, OUT)).as_posix()
parts.append(f"{prev}fps={FPS},ass={ass_rel}:fontsdir={fonts_rel},format=yuv420p[vout]")
graph = OUT / "xfade.txt"
graph.write_text(";\n".join(parts), encoding="utf-8")

subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", *inputs, "-i", str(AUDIO),
                "-/filter_complex", graph.name, "-map", "[vout]", "-map", "110:a:0",
                "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-profile:v", "high",
                "-level", "4.1", "-color_primaries", "bt709", "-color_trc", "bt709",
                "-colorspace", "bt709", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2",
                "-t", f"{RUNTIME:.3f}", "-movflags", "+faststart", str(REVIEW)], check=True, cwd=OUT)

probe = json.loads(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries",
    "format=duration,size", "-of", "json", str(REVIEW)]))
print(json.dumps({"beats": 110, "chapter_dips": sum(chapter_change),
                  "duration": probe["format"]["duration"], "size": probe["format"]["size"],
                  "sha256": hashlib.sha256(REVIEW.read_bytes()).hexdigest()}, indent=2))
