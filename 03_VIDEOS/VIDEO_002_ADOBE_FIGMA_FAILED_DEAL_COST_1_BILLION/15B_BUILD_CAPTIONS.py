#!/usr/bin/env python3
"""VIDEO 002 — Stage 15B: word-highlight captions over Picture Assembly V2.

Mirrors VIDEO_001 15B_BUILD.py caption rules (Montserrat ExtraBold 46, #EDEDED base,
current word #D32222, charcoal outline, bottom-centre, voice-only audio).
VIDEO_002 frames already carry baked headlines/sources, so no metadata overlay layer.

Inputs : 11_WORD_TRANSCRIPT.csv (2,185 timed words), Picture Assembly V2 MP4.
Outputs: 11_CAPTIONS.srt, 18_YOUTUBE_ENGLISH_CC_POSITIONED.vtt (in Git),
         captions .ass + review MP4 (in OUT, outside Git).
"""
import csv, hashlib, json, os, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MEDIA = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("C:/Users/KK/Documents/WhatItCost_media/002-adobe-figma")
SRC = MEDIA / "15_ASSEMBLY_V2" / "VIDEO_002_ADOBE_FIGMA_PICTURE_ASSEMBLY_V2_1080P25.mp4"
FONTS = MEDIA.parent / "_fonts"
OUT = MEDIA / "15B_CAPTIONS"
OUT.mkdir(exist_ok=True)
ASS = OUT / "VIDEO_002_STAGE15B_CAPTIONS.ass"
REVIEW = OUT / "VIDEO_002_STAGE15B_REVIEW_V1_1080P25.mp4"
RUNTIME = 940.617

WHITE = "&H00EDEDED"
RED = "&H002222D3"  # RGB D32222
MAX_CUE_CHARS = 64   # one cue = what is on screen at once (max two lines)
LINE_CHARS = 42      # split into two lines above this
MAX_GAP = 0.7        # a pause this long starts a new cue

words = [{"i": int(r["word_index"]), "w": r["word"], "a": float(r["start"]), "b": float(r["end"])}
         for r in csv.DictReader(open(HERE / "11_WORD_TRANSCRIPT.csv", encoding="utf-8-sig"))]
assert len(words) == 2185

# Group words into cues: break on sentence end, long pause, or length.
cues, cur = [], []
for k, t in enumerate(words):
    if cur:
        text = " ".join(x["w"] for x in cur + [t])
        if len(text) > MAX_CUE_CHARS or t["a"] - cur[-1]["b"] > MAX_GAP:
            cues.append(cur); cur = []
    cur.append(t)
    if t["w"][-1] in ".?!" and len(" ".join(x["w"] for x in cur)) >= 12:
        cues.append(cur); cur = []
if cur:
    cues.append(cur)

def split_lines(tokens):
    total = sum(len(t["w"]) + 1 for t in tokens)
    if total <= LINE_CHARS or len(tokens) <= 1:
        return [tokens]
    best, best_diff, acc = 1, 10**9, 0
    for j, t in enumerate(tokens[:-1], 1):
        acc += len(t["w"]) + 1
        if abs(acc - total / 2) < best_diff:
            best, best_diff = j, abs(acc - total / 2)
    return [tokens[:best], tokens[best:]]

def safe(s): return s.replace("{", "(").replace("}", ")")
def ass_t(s):
    cs = int(round(s * 100)); h, cs = divmod(cs, 360000); m, cs = divmod(cs, 6000); sec, cs = divmod(cs, 100)
    return f"{h}:{m:02d}:{sec:02d}.{cs:02d}"
def srt_t(s):
    ms = int(round(s * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); sec, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{sec:02d},{ms:03d}"
def vtt_t(s): return srt_t(s).replace(",", ".")

# Cue display windows: from first word start to next cue start (capped), never overlapping.
spans = []
for n, c in enumerate(cues):
    a = c[0]["a"]
    nxt = cues[n + 1][0]["a"] if n + 1 < len(cues) else RUNTIME
    b = min(nxt, c[-1]["b"] + 0.6)
    spans.append((a, max(b, c[-1]["b"])))

events = []
for c, (ca, cb) in zip(cues, spans):
    lines = split_lines(c)
    flat = [x for l in lines for x in l]
    for k, tok in enumerate(flat):
        s = ca if k == 0 else tok["a"]
        e = cb if k == len(flat) - 1 else flat[k + 1]["a"]
        if e <= s: e = s + 0.04
        out, idx = [], 0
        for l in lines:
            parts = []
            for item in l:
                txt = safe(item["w"])
                parts.append("{\\c" + RED + "}" + txt + "{\\c" + WHITE + "}" if idx == k else txt)
                idx += 1
            out.append(" ".join(parts))
        events.append((s, e, "\\N".join(out)))

header = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: Caption,Montserrat ExtraBold,46,&H00EDEDED,&H00EDEDED,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,3.2,0,2,120,120,46,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
ASS.write_text(header + "\n".join(f"Dialogue: 2,{ass_t(a)},{ass_t(b)},Caption,,0,0,0,,{t}" for a, b, t in events) + "\n", encoding="utf-8")

srt, vtt = [], ["WEBVTT", ""]
for n, (c, (a, b)) in enumerate(zip(cues, spans), 1):
    text = "\n".join(" ".join(x["w"] for x in l) for l in split_lines(c))
    srt += [str(n), f"{srt_t(a)} --> {srt_t(b)}", text, ""]
    vtt += [f"{vtt_t(a)} --> {vtt_t(b)} line:78% position:50% align:center size:88%", text, ""]
(HERE / "11_CAPTIONS.srt").write_text("\n".join(srt), encoding="utf-8")
(HERE / "18_YOUTUBE_ENGLISH_CC_POSITIONED.vtt").write_text("\n".join(vtt), encoding="utf-8")

used = sum(len(c) for c in cues)
assert used == 2185, used
assert all(b > a for a, b in spans)
assert all(spans[i][1] <= spans[i + 1][0] + 1e-6 for i in range(len(spans) - 1))

subprocess.run([
    "ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(SRC),
    # relative fontsdir: avoids drive-letter colons inside the filtergraph (cwd=OUT)
    "-vf", f"ass={ASS.name}:fontsdir={Path(os.path.relpath(FONTS, OUT)).as_posix()}",
    "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-profile:v", "high", "-level", "4.1",
    "-pix_fmt", "yuv420p", "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709",
    "-c:a", "copy", "-movflags", "+faststart", str(REVIEW)], check=True, cwd=OUT)

probe = json.loads(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries",
    "format=duration,size:stream=codec_name,width,height,r_frame_rate,sample_rate,channels",
    "-of", "json", str(REVIEW)]))
sha = hashlib.sha256(REVIEW.read_bytes()).hexdigest()
print(json.dumps({"cues": len(cues), "highlight_events": len(events), "words": used,
                  "duration": probe["format"]["duration"], "size": probe["format"]["size"],
                  "sha256": sha}, indent=2))
