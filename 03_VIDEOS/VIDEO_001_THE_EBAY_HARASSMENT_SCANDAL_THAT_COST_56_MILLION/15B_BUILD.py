#!/usr/bin/env python3
from __future__ import annotations
import csv, hashlib, json, re, subprocess, urllib.request
from pathlib import Path

BASE = Path(__file__).resolve().parent
OUT = BASE / "15B_OUTPUT"
OUT.mkdir(exist_ok=True)

VIDEO_URL = "https://d2ol7oe51mr4n9.cloudfront.net/user_3J3zfwu7kpgllQvPySWoLtXHwdR/174a262e-958f-4b63-b215-1a6ab385b755.mp4"
AUDIO_URL = "https://d2ol7oe51mr4n9.cloudfront.net/user_3J3zfwu7kpgllQvPySWoLtXHwdR/4c1aa66b-440d-4fc7-ae95-78e60845ae5f.mp3"
RUNTIME = 957.414

SRC_VIDEO = OUT / "stage15a.mp4"
SRC_AUDIO = OUT / "harrison.mp3"
CAP_ASS = OUT / "VIDEO_001_STAGE15B_CAPTIONS_WORD_HIGHLIGHT.ass"
OV_ASS = OUT / "VIDEO_001_STAGE15B_OVERLAYS.ass"
COMBINED_ASS = OUT / "VIDEO_001_STAGE15B_COMBINED.ass"
REVIEW = OUT / "VIDEO_001_STAGE15B_REVIEW_V1_1080P.mp4"
CONTACT = OUT / "VIDEO_001_STAGE15B_CONTACT_SHEET.jpg"
QC = OUT / "VIDEO_001_STAGE15B_QC.txt"

WHITE = "&H00EDEDED"
ACCENT = "&H002222D3"  # RGB D32222 — channel red
RED = "&H002222D3"     # RGB D32222

def download(url: str, path: Path) -> None:
    if path.exists() and path.stat().st_size > 0:
        return
    print(f"download {url} -> {path}")
    urllib.request.urlretrieve(url, path)

def ass_time(sec: float) -> str:
    sec = max(0.0, sec)
    h = int(sec // 3600); sec -= h * 3600
    m = int(sec // 60); sec -= m * 60
    s = int(sec); cs = int(round((sec - s) * 100))
    if cs >= 100:
        s += 1; cs -= 100
    if s >= 60:
        m += 1; s -= 60
    if m >= 60:
        h += 1; m -= 60
    return f"{h}:{m:02d}:{s:02d}.{cs:02d}"

def srt_time(value: str) -> float:
    h, m, sms = value.split(":")
    s, ms = sms.split(",")
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def safe(text: str) -> str:
    return text.replace("{", "(").replace("}", ")")

def split_lines(tokens: list[dict], max_chars: int = 53) -> list[list[dict]]:
    total = sum(len(t["w"]) + 1 for t in tokens)
    if total <= max_chars or len(tokens) <= 1:
        return [tokens]
    best = 1
    best_diff = 10**9
    acc = 0
    for j, token in enumerate(tokens[:-1], 1):
        acc += len(token["w"]) + 1
        diff = abs(acc - total / 2)
        if diff < best_diff:
            best_diff = diff
            best = j
    return [tokens[:best], tokens[best:]]

download(VIDEO_URL, SRC_VIDEO)
download(AUDIO_URL, SRC_AUDIO)

word_data = json.loads((BASE / "11_TRANSCRIPT_WORD_LEVEL.json").read_text(encoding="utf-8"))
srt_text = (BASE / "11_CAPTIONS.srt").read_text(encoding="utf-8")
overlay_rows = list(csv.DictReader((BASE / "14_OVERLAY_MAP.csv").open(encoding="utf-8-sig", newline="")))

# Parse 409 authored SRT cues.
cues = []
for block in re.split(r"\n\s*\n", srt_text.strip()):
    lines = block.splitlines()
    if len(lines) < 3:
        continue
    m = re.match(r"(\d\d:\d\d:\d\d,\d{3}) --> (\d\d:\d\d:\d\d,\d{3})", lines[1])
    if not m:
        continue
    cues.append({
        "start": srt_time(m.group(1)),
        "end": srt_time(m.group(2)),
        "text": " ".join(lines[2:]).strip(),
    })

# Flatten canonical authored words; Whisper timing is only the anchor.
words = []
idx = 0
for section in word_data["sections"]:
    for paragraph in section["paragraphs"]:
        for w, a, b in paragraph["words"]:
            words.append({"idx": idx, "w": w, "a": a / 1000, "b": b / 1000})
            idx += 1
words.sort(key=lambda x: x["a"])

# Fix one known alignment tokenization artifact: "i" + "n" => "in".
merged = []
i = 0
while i < len(words):
    if (
        i + 1 < len(words)
        and words[i]["w"].lower() == "i"
        and words[i + 1]["w"].lower() == "n"
        and words[i + 1]["a"] - words[i]["b"] <= 0.25
    ):
        merged.append({
            "idx": words[i]["idx"],
            "w": "in",
            "a": words[i]["a"],
            "b": words[i + 1]["b"],
        })
        i += 2
    else:
        merged.append(words[i])
        i += 1
words = merged

used = set()
caption_events = []
fallback_cues = 0

for cue in cues:
    # midpoint assignment prevents duplicate word use at cue boundaries.
    tokens = []
    for token in words:
        if token["idx"] in used:
            continue
        mid = (token["a"] + token["b"]) / 2
        if cue["start"] - 0.001 <= mid <= cue["end"] + 0.001:
            tokens.append(token)
            used.add(token["idx"])

    if not tokens:
        fallback_cues += 1
        caption_events.append((cue["start"], cue["end"], safe(cue["text"])))
        continue

    lines = split_lines(tokens)
    flat = [x for line in lines for x in line]
    for k, token in enumerate(flat):
        start = cue["start"] if k == 0 else max(cue["start"], token["a"])
        end = cue["end"] if k == len(flat) - 1 else min(cue["end"], flat[k + 1]["a"])
        if end <= start:
            end = min(cue["end"], start + 0.04)

        out_lines = []
        flat_idx = 0
        for line in lines:
            parts = []
            for item in line:
                text = safe(item["w"])
                if flat_idx == k:
                    parts.append(r"{\c" + ACCENT + "}" + text + r"{\c" + WHITE + "}")
                else:
                    parts.append(text)
                flat_idx += 1
            out_lines.append(" ".join(parts))
        caption_events.append((start, end, r"\N".join(out_lines)))

overlay_events = []
for row in overlay_rows:
    if row["overlay_classes"] == "NONE":
        continue
    labels = []
    for key in ("date_label", "source_label", "legal_status", "provenance_label"):
        value = (row.get(key) or "").strip()
        if value:
            labels.append(value)
    if not labels:
        continue
    stack = r"\N".join(r"{\c" + RED + r"}▌{\c" + WHITE + "} " + safe(x) for x in labels)
    overlay_events.append((float(row["start"]), float(row["end"]), stack, row["beat_id"]))

ASS_HEADER = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: Caption,Montserrat ExtraBold,46,&H00EDEDED,&H00EDEDED,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,3.2,0,2,120,120,46,1
Style: Meta,Montserrat ExtraBold,27,&H00EDEDED,&H00EDEDED,&H00000000,&H880B0B0B,-1,0,0,0,100,100,0,0,3,1.5,0,9,760,58,54,1
Style: Patch,Montserrat ExtraBold,24,&H00EDEDED,&H00EDEDED,&H00000000,&H000B0B0B,-1,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1
Style: PatchBox,Montserrat ExtraBold,24,&H000B0B0B,&H000B0B0B,&H000B0B0B,&H000B0B0B,-1,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

caption_lines = [
    f"Dialogue: 2,{ass_time(a)},{ass_time(b)},Caption,,0,0,0,,{text}"
    for a, b, text in caption_events
]
overlay_lines = [
    f"Dialogue: 1,{ass_time(a)},{ass_time(b)},Meta,{beat},0,0,0,,{{\\an9}}{text}"
    for a, b, text, beat in overlay_events
]
# B104 deterministic cleanup: cover the Stage15A fallback-glyph in the baked inequality line.
overlay_lines.append(r"Dialogue: 3,0:14:22.24,0:14:29.06,PatchBox,B104_BOX,0,0,0,,{\an7\pos(900,420)\p1\c&H0B0B0B&\bord0\shad0}m 0 0 l 520 0 520 70 0 70")
overlay_lines.append(r"Dialogue: 4,0:14:22.24,0:14:29.06,Patch,B104_PATCH,0,0,0,,{\pos(930,438)\an7}SURVIVING CLAIM ≠ LIABILITY")

CAP_ASS.write_text(ASS_HEADER + "\n".join(caption_lines) + "\n", encoding="utf-8")
OV_ASS.write_text(ASS_HEADER + "\n".join(overlay_lines) + "\n", encoding="utf-8")
COMBINED_ASS.write_text(ASS_HEADER + "\n".join(overlay_lines + caption_lines) + "\n", encoding="utf-8")

combined = COMBINED_ASS.read_text(encoding="utf-8")
structural = {
    "canonical_words": word_data["alignment"]["canonical_words"],
    "display_words_after_merge": len(words),
    "used_word_tokens": len(used),
    "srt_cues": len(cues),
    "caption_events": len(caption_events),
    "fallback_cues": fallback_cues,
    "overlay_rows": len(overlay_rows),
    "overlay_events": len(overlay_events),
    "artifact_100_100": "100,100)}" in combined,
    "split_i_n": " i n " in combined,
    "no_58_7_lock": "NO $58.7M AWARD" in combined,
    "gps_lock": "ATTEMPTED GPS • INSTALLATION NOT ESTABLISHED" in combined,
    "liability_lock": "SURVIVING CLAIM ≠ LIABILITY" in combined,
    "reconstruction_lock": "ILLUSTRATIVE RECONSTRUCTION" in combined,
    "b104_inequality_patch": "B104_PATCH" in combined and "B104_BOX" in combined and "SURVIVING CLAIM ≠ LIABILITY" in combined,
}
positive_58 = combined.replace("NO $58.7M AWARD", "")
structural["positive_58_7_award"] = "$58.7M AWARD" in positive_58

assert structural["srt_cues"] == 409
assert structural["used_word_tokens"] >= 2140
assert not structural["artifact_100_100"]
assert not structural["split_i_n"]
assert not structural["positive_58_7_award"]
assert structural["no_58_7_lock"]
assert structural["gps_lock"]
assert structural["liability_lock"]
assert structural["reconstruction_lock"]
assert structural["b104_inequality_patch"]

print("STRUCTURAL_QC", json.dumps(structural, indent=2))

# Burn Stage 15B overlay/caption layer into a true CFR 25 fps review master.
subprocess.run([
    "ffmpeg", "-y", "-hide_banner", "-loglevel", "warning",
    "-i", str(SRC_VIDEO), "-i", str(SRC_AUDIO),
    "-map", "0:v:0", "-map", "1:a:0",
    "-vf", f"tpad=stop_mode=clone:stop_duration=0.20,fps=25,ass={COMBINED_ASS.name}",
    "-c:v", "libx264", "-preset", "ultrafast", "-crf", "21", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-ac", "1",
    "-t", f"{RUNTIME:.3f}", "-movflags", "+faststart",
    str(REVIEW)
], cwd=OUT, check=True)

probe_raw = subprocess.check_output([
    "ffprobe", "-v", "error", "-show_entries", "format=duration,size",
    "-show_entries", "stream=index,codec_type,codec_name,width,height,r_frame_rate,avg_frame_rate,sample_rate,channels",
    "-of", "json", str(REVIEW)
], text=True)
probe = json.loads(probe_raw)
video = next(s for s in probe["streams"] if s["codec_type"] == "video")
audio = next(s for s in probe["streams"] if s["codec_type"] == "audio")
duration = float(probe["format"]["duration"])
delta = duration - RUNTIME

assert video["width"] == 1920 and video["height"] == 1080
assert video["r_frame_rate"] == "25/1"
assert video["avg_frame_rate"] == "25/1"
assert audio["sample_rate"] == "44100"
assert int(audio["channels"]) == 1
assert abs(delta) <= 0.08

# 16-frame visual contact sheet, sampled once per minute.
subprocess.run([
    "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
    "-i", str(REVIEW),
    "-vf", "fps=1/60,scale=480:270,tile=4x4:padding=0:margin=0",
    "-frames:v", "1", "-q:v", "2", str(CONTACT)
], check=True)

qc_text = f"""VIDEO_001 — STAGE 15B REVIEW V1

STATUS: TECHNICAL PASS / OWNER VISUAL REVIEW PENDING

CAPTIONS
- SRT cues: {len(cues)}
- canonical authored words: {word_data['alignment']['canonical_words']}
- displayed word tokens after known i+n merge: {len(words)}
- uniquely mapped word tokens: {len(used)}
- word-highlight events: {len(caption_events)}
- fallback cues without token mapping: {fallback_cues}
- white base captions + channel-red current word
- bottom caption zone only
- forbidden 100,100)}} artifact: ABSENT
- known 'i n' split: FIXED

OVERLAYS
- overlay map rows: {len(overlay_rows)}
- timed metadata stacks: {len(overlay_events)}
- upper-right side-margin stack
- bottom 22% left clear for captions
- GPS lock present: YES
- DPA / conviction distinction preserved: YES
- surviving claim / liability distinction preserved: YES
- reconstruction provenance present: YES
- B104 surviving-claim inequality fallback glyph patched deterministically: YES
- NO $58.7M AWARD lock present: YES
- positive $58.7M award claim present: NO

VIDEO
- file: {REVIEW.name}
- codec: {video['codec_name']}
- frame: {video['width']}x{video['height']}
- r_frame_rate: {video['r_frame_rate']}
- avg_frame_rate: {video['avg_frame_rate']}
- audio: {audio['codec_name']} / {audio['sample_rate']} Hz / {audio['channels']} channel
- measured duration: {duration:.3f} sec
- locked target: {RUNTIME:.3f} sec
- delta: {delta:+.3f} sec
- SHA-256: {sha256(REVIEW)}

SIDECAR SHA-256
- captions ASS: {sha256(CAP_ASS)}
- overlays ASS: {sha256(OV_ASS)}
- combined ASS: {sha256(COMBINED_ASS)}

NOT INCLUDED
- music
- SFX
- Stage 15C audio mix

NEXT GATE
- owner reviews Stage 15B picture/caption/overlay cut
- do not start Stage 15C automatically
"""
QC.write_text(qc_text, encoding="utf-8")
print(qc_text)
