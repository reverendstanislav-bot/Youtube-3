#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import math
import random
import struct
import subprocess
import wave
from pathlib import Path

BASE = Path(__file__).resolve().parent
SRC = BASE / "15B_OUTPUT" / "VIDEO_001_STAGE15B_REVIEW_V1_1080P.mp4"
ROOT = BASE / "15C_SFX_MICROTEST"
SFX = ROOT / "sfx"
OUT = ROOT / "out"
TMP = ROOT / "tmp"
for p in (SFX, OUT, TMP):
    p.mkdir(parents=True, exist_ok=True)

SR = 44100
random.seed(15003)

EXCERPT_START = 0.0
EXCERPT_DUR = 34.0

EVENTS = [
    {"id": "E01", "time": 6.340, "name": "paper_tick", "file": "01_paper_tick.wav", "kind": "transient"},
    {"id": "E02", "time": 7.760, "name": "page_rustle", "file": "02_page_rustle.wav", "kind": "texture"},
    {"id": "E03", "time": 21.900, "name": "soft_whoosh", "file": "03_soft_whoosh.wav", "kind": "texture"},
    {"id": "E04", "time": 30.120, "name": "dry_click", "file": "04_dry_click.wav", "kind": "transient"},
]

def sh(cmd, capture=False):
    print("RUN", " ".join(map(str, cmd)))
    if capture:
        return subprocess.run(cmd, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run(cmd, check=True)

def wav_write(path: Path, samples):
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        frames = b"".join(
            struct.pack("<h", max(-32768, min(32767, int(round(x)))))
            for x in samples
        )
        w.writeframes(frames)

def measure_wav(path: Path):
    with wave.open(str(path), "rb") as w:
        n = w.getnframes()
        raw = w.readframes(n)
        ch = w.getnchannels()
        sw = w.getsampwidth()
        if sw != 2:
            raise RuntimeError(f"Expected 16-bit WAV: {path}")
        vals = struct.unpack("<" + "h" * (len(raw) // 2), raw)
        if ch > 1:
            vals = vals[::ch]
    if not vals:
        return {"peak_dbfs": -120.0, "rms_dbfs": -120.0}
    peak = max(abs(x) for x in vals) / 32768.0
    rms = math.sqrt(sum(float(x) * float(x) for x in vals) / len(vals)) / 32768.0
    peak_db = 20.0 * math.log10(max(peak, 1e-12))
    rms_db = 20.0 * math.log10(max(rms, 1e-12))
    return {"peak_dbfs": peak_db, "rms_dbfs": rms_db}

def normalize_peak(samples, target_dbfs):
    peak = max(max(abs(x) for x in samples), 1e-9)
    target = 32767.0 * (10.0 ** (target_dbfs / 20.0))
    g = target / peak
    return [x * g for x in samples]

def noise_lp(n, amp=1.0, smooth=.75):
    out = []
    y = 0.0
    for _ in range(n):
        x = (random.random() * 2.0 - 1.0) * amp
        y = smooth * y + (1.0 - smooth) * x
        out.append(y)
    return out

# E01 paper tick: short, papery transient; normalized strong enough to be unmistakable.
n = int(.19 * SR)
raw = noise_lp(n, 1.0, .66)
paper = []
for i, x in enumerate(raw):
    d = i / max(n - 1, 1)
    env = (1.0 - d) ** 2.3
    grain = (random.random() * 2.0 - 1.0) * .22 * env
    paper.append((x + grain) * env)
paper = normalize_peak(paper, -4.5)
wav_write(SFX / "01_paper_tick.wav", paper)

# E02 page rustle: brighter mid/high texture, not a literal page-turn performance.
n = int(.58 * SR)
page = []
lp = 0.0
for i in range(n):
    x = random.random() * 2.0 - 1.0
    lp = .82 * lp + .18 * x
    high = x - lp
    t = i / SR
    env = min(1.0, t / .055) * min(1.0, max(0.0, (.58 - t) / .16))
    mod = .72 + .28 * math.sin(2 * math.pi * 3.1 * t + .7)
    page.append((.78 * high + .22 * lp) * env * mod)
page = normalize_peak(page, -5.0)
wav_write(SFX / "02_page_rustle.wav", page)

# E03 soft whoosh: editorial air transition, no impact/boom.
n = int(.62 * SR)
whoosh_raw = noise_lp(n, 1.0, .58)
whoosh = []
for i, x in enumerate(whoosh_raw):
    d = i / max(n - 1, 1)
    env = max(0.0, math.sin(math.pi * d)) ** 1.45
    whoosh.append(x * env)
whoosh = normalize_peak(whoosh, -7.0)
wav_write(SFX / "03_soft_whoosh.wav", whoosh)

# E04 dry editorial click: short punctuation, no UI/cash-register character.
n = int(.085 * SR)
click = []
for i in range(n):
    t = i / SR
    env = math.exp(-t / .012)
    x = math.sin(2 * math.pi * 1120 * t) + .22 * math.sin(2 * math.pi * 2240 * t)
    x += (random.random() * 2.0 - 1.0) * .12
    click.append(x * env)
click = normalize_peak(click, -4.0)
wav_write(SFX / "04_dry_click.wav", click)

def extract_vo_window(event_time: float, out_path: Path, half=.45):
    start = max(EXCERPT_START, event_time - half)
    end = min(EXCERPT_START + EXCERPT_DUR, event_time + half)
    dur = max(.2, end - start)
    sh([
        "ffmpeg", "-y", "-loglevel", "error",
        "-ss", f"{start:.3f}", "-t", f"{dur:.3f}", "-i", str(SRC),
        "-vn", "-ac", "1", "-ar", str(SR), "-c:a", "pcm_s16le",
        str(out_path),
    ])
    return start, dur

rows = []
for event in EVENTS:
    sfx_path = SFX / event["file"]
    sfx_m = measure_wav(sfx_path)
    vo_wav = TMP / f'{event["id"]}_harrison.wav'
    vo_start, vo_dur = extract_vo_window(event["time"], vo_wav)
    vo_m = measure_wav(vo_wav)
    peak_delta = sfx_m["peak_dbfs"] - vo_m["peak_dbfs"]
    rms_delta = sfx_m["rms_dbfs"] - vo_m["rms_dbfs"]
    if event["kind"] == "transient":
        audible = peak_delta >= -5.0
        criterion = "SFX peak >= Harrison local peak - 5 dB"
    else:
        audible = (peak_delta >= -7.0) and (rms_delta >= -10.0)
        criterion = "SFX peak >= Harrison - 7 dB AND SFX RMS >= Harrison - 10 dB"
    rows.append({
        **event,
        "vo_window_start": vo_start,
        "vo_window_dur": vo_dur,
        "sfx_peak_dbfs": sfx_m["peak_dbfs"],
        "sfx_rms_dbfs": sfx_m["rms_dbfs"],
        "harrison_peak_dbfs": vo_m["peak_dbfs"],
        "harrison_rms_dbfs": vo_m["rms_dbfs"],
        "peak_delta_db": peak_delta,
        "rms_delta_db": rms_delta,
        "audibility_preflight": "PASS" if audible else "FAIL",
        "criterion": criterion,
    })

failed = [r for r in rows if r["audibility_preflight"] != "PASS"]
if failed:
    raise RuntimeError("Audibility preflight failed: " + ", ".join(r["id"] for r in failed))

# SOLO REFERENCE: same exact WAV assets, widely spaced, no narration/music.
solo = OUT / "VIDEO_001_STAGE15C_SFX_SOLO_REFERENCE_V1.mp4"
solo_inputs = []
solo_filters = []
solo_labels = []
solo_times = [2.0, 6.0, 10.0, 14.0]
for idx, (event, t) in enumerate(zip(EVENTS, solo_times), start=1):
    solo_inputs += ["-i", str(SFX / event["file"])]
    ms = int(round(t * 1000))
    lab = f"s{idx}"
    solo_filters.append(f"[{idx}:a]adelay={ms}|{ms}[{lab}]")
    solo_labels.append(f"[{lab}]")
solo_filters.append("".join(solo_labels) + f"amix=inputs={len(solo_labels)}:duration=longest:normalize=0,alimiter=limit=0.95[a]")
solo_text = "SFX SOLO REFERENCE  |  00-02 PAPER TICK  |  00-06 PAGE RUSTLE  |  00-10 SOFT WHOOSH  |  00-14 DRY CLICK"
solo_vf = (
    "drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:"
    f"text='{solo_text}':x=(w-text_w)/2:y=470:fontsize=34:fontcolor=white@0.92"
)
sh([
    "ffmpeg", "-y", "-loglevel", "error",
    "-f", "lavfi", "-i", "color=c=0x0B0B0B:s=1920x1080:r=25:d=18",
    *solo_inputs,
    "-filter_complex", ";".join(solo_filters),
    "-map", "0:v:0", "-map", "[a]", "-vf", solo_vf,
    "-c:v", "libx264", "-preset", "veryfast", "-crf", "24", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-ac", "2",
    "-t", "18", "-movflags", "+faststart", str(solo),
])

# IN-CONTEXT PROOF: one 34s approved Stage15B excerpt, same exact SFX assets.
ctx = OUT / "VIDEO_001_STAGE15C_SFX_IN_CONTEXT_PROOF_V1.mp4"
ctx_inputs = ["-ss", f"{EXCERPT_START:.3f}", "-t", f"{EXCERPT_DUR:.3f}", "-i", str(SRC)]
ctx_filters = []
ctx_labels = []
for idx, event in enumerate(EVENTS, start=1):
    ctx_inputs += ["-i", str(SFX / event["file"])]
    rel = event["time"] - EXCERPT_START
    ms = int(round(rel * 1000))
    lab = f"e{idx}"
    ctx_filters.append(f"[{idx}:a]adelay={ms}|{ms}[{lab}]")
    ctx_labels.append(f"[{lab}]")
ctx_filters.append("".join(ctx_labels) + f"amix=inputs={len(ctx_labels)}:duration=longest:normalize=0[sfx]")
ctx_filters.append("[0:a]volume=1.0[vo]")
ctx_filters.append("[vo][sfx]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[a]")
ctx_vf = (
    "drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:"
    "text='STAGE 15C SFX MICROTEST - IN CONTEXT':x=55:y=45:fontsize=28:"
    "fontcolor=white@0.82:box=1:boxcolor=black@0.38:boxborderw=12"
)
sh([
    "ffmpeg", "-y", "-loglevel", "error",
    *ctx_inputs,
    "-filter_complex", ";".join(ctx_filters),
    "-map", "0:v:0", "-map", "[a]", "-vf", ctx_vf,
    "-c:v", "libx264", "-preset", "veryfast", "-crf", "25", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-ac", "2",
    "-t", f"{EXCERPT_DUR:.3f}", "-movflags", "+faststart", str(ctx),
])

def sha256(path: Path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

measure_csv = OUT / "VIDEO_001_STAGE15C_SFX_MICROTEST_MEASUREMENTS_V1.csv"
fields = [
    "id", "time", "name", "kind",
    "sfx_peak_dbfs", "sfx_rms_dbfs",
    "harrison_peak_dbfs", "harrison_rms_dbfs",
    "peak_delta_db", "rms_delta_db",
    "audibility_preflight", "criterion",
]
with measure_csv.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    for r in rows:
        rr = dict(r)
        for k in ["sfx_peak_dbfs", "sfx_rms_dbfs", "harrison_peak_dbfs", "harrison_rms_dbfs", "peak_delta_db", "rms_delta_db"]:
            rr[k] = f"{rr[k]:.2f}"
        w.writerow(rr)

report = OUT / "VIDEO_001_STAGE15C_SFX_MICROTEST_REPORT_V1.txt"
lines = [
    "VIDEO_001 — STAGE 15C SFX AUDIBILITY MICROTEST V1",
    "",
    "Scope: 34.000 sec of the approved Stage15B opening (film 00:00.000–00:34.000).",
    "Music: NONE",
    "Room tone: NONE",
    "Third-party SFX: NONE",
    "Model/paid generation: NONE / 0 credits",
    "",
    "Outputs:",
    f"- SOLO: {solo.name}",
    f"- CONTEXT: {ctx.name}",
    "",
    "Exact in-context checkpoints:",
]
for r in rows:
    lines += [
        f'- {r["time"]:06.3f}s — {r["name"]}: '
        f'SFX peak {r["sfx_peak_dbfs"]:.2f} dBFS / RMS {r["sfx_rms_dbfs"]:.2f} dBFS; '
        f'Harrison local peak {r["harrison_peak_dbfs"]:.2f} / RMS {r["harrison_rms_dbfs"]:.2f}; '
        f'Δpeak {r["peak_delta_db"]:+.2f} dB / ΔRMS {r["rms_delta_db"]:+.2f} dB; '
        f'preflight {r["audibility_preflight"]}.'
    ]
lines += [
    "",
    "SOLO reference checkpoints:",
    "- 00:02.000 paper tick",
    "- 00:06.000 page rustle",
    "- 00:10.000 soft whoosh",
    "- 00:14.000 dry click",
    "",
    "Audibility verification rule:",
    "- transients: SFX peak must be no more than 5 dB below local Harrison peak;",
    "- textures: SFX peak must be no more than 7 dB below local Harrison peak AND RMS no more than 10 dB below local Harrison RMS;",
    "- all four events passed this preflight before encoding.",
    "",
    "Editorial guardrails:",
    "- Harrison remains primary; no VO ducking used in this test.",
    "- No gavel, siren, cash register, horror, trailer boom, animal/insect foley, or fake event-implying sound.",
    "- This is an audibility/style gate only. It does NOT approve Stage 15C and does NOT authorize scaling to the full film.",
    "",
    f"SOLO SHA256: {sha256(solo)}",
    f"CONTEXT SHA256: {sha256(ctx)}",
]
report.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(report.read_text())
