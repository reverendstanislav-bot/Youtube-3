#!/usr/bin/env python3
"""VIDEO 002 — Stage 15G (V6): sound design trial over the locked V5 picture.

Owner fixed V5 as the main cut and asked to try sound (exception to the voice-only channel rule,
for this experiment). Everything is synthesised here (numpy only, no downloads, no credits) and
placed on the exact V5 edit events:
- ambience bed: low drone (55/82/110/165 Hz, slow LFOs) + soft room air, swells into chapter dips
- dissolves (24): short air whoosh, panned L -> R
- chapter dips (12): reverse swell into the black + sub drop on the cut
- punch-ins: quiet rising air under the camera move
- number cards (7): low impact on reveal, counter ticks slowing with the count-up, soft exit air
Picture stream is copied from V5 untouched; only the audio is new.
Output (outside Git): <media>/15G_V6/VIDEO_002_STAGE15G_REVIEW_V6_1080P25.mp4
"""
import hashlib, importlib.util, json, subprocess, sys, wave
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("v5", HERE / "15F_BUILD_V5.py")
v5 = importlib.util.module_from_spec(spec)
sys_argv = sys.argv
sys.argv = sys.argv[:2]
spec.loader.exec_module(v5)
sys.argv = sys_argv

OUT = v5.MEDIA / "15G_V6"
OUT.mkdir(exist_ok=True)
PICTURE = v5.REVIEW
SFX_WAV = OUT / "VIDEO_002_V6_SOUND_LAYER.wav"
REVIEW = OUT / "VIDEO_002_STAGE15G_REVIEW_V6_1080P25.mp4"
SR = 48000
N = int(v5.RUNTIME * SR) + SR
rng = np.random.default_rng(2002)

def db(x):
    return 10 ** (x / 20)

def band_noise(n, lo, hi, tilt=0.0):
    """White noise shaped to a soft band [lo, hi] Hz in the frequency domain."""
    spec = np.fft.rfft(rng.standard_normal(n))
    f = np.fft.rfftfreq(n, 1 / SR) + 1e-3
    lf = np.log(f)
    m = 1 / (1 + np.exp(-(lf - np.log(lo)) * 6)) * 1 / (1 + np.exp((lf - np.log(hi)) * 6))
    if tilt:
        m *= (f / lo) ** tilt
    y = np.fft.irfft(spec * m, n)
    return y / (np.abs(y).max() + 1e-9)

def env(n, attack, release, peak_at=None):
    t = np.linspace(0, 1, n)
    if peak_at is None:
        a = np.clip(t / max(attack, 1e-4), 0, 1)
        r = np.clip((1 - t) / max(release, 1e-4), 0, 1)
        return np.minimum(a, r) ** 2
    up = np.clip(t / peak_at, 0, 1) ** 2.2
    down = np.clip((1 - t) / (1 - peak_at), 0, 1) ** 1.6
    return np.where(t < peak_at, up, down)

IR = None
def reverb(x, wet=0.28):
    """Stereo convolution with a 1.8 s dark decaying-noise IR (shared space for all effects)."""
    global IR
    if IR is None:
        n = int(1.8 * SR)
        decay = np.exp(-np.linspace(0, 7, n))
        IR = np.stack([band_noise(n, 80, 5000, -0.4) * decay for _ in range(2)])
        IR /= np.sqrt((IR ** 2).sum(axis=1, keepdims=True))
    out = []
    for ch in range(2):
        m = len(x[ch]) + IR.shape[1]
        y = np.fft.irfft(np.fft.rfft(x[ch], m) * np.fft.rfft(IR[ch], m), m)
        dry = np.pad(x[ch], (0, IR.shape[1]))
        out.append(dry * (1 - wet) + y * wet)
    return np.stack(out)

def pan(mono, p0, p1):
    p = np.linspace(p0, p1, len(mono))
    return np.stack([mono * np.cos((p + 1) * np.pi / 4), mono * np.sin((p + 1) * np.pi / 4)])

mix = np.zeros((2, N), dtype=np.float32)
def place(st, t, gain_db):
    i = int(t * SR)
    if i < 0:
        st, i = st[:, -i:], 0
    j = min(N, i + st.shape[1])
    mix[:, i:j] += st[:, :j - i] * db(gain_db)

# ---- effects --------------------------------------------------------------------------------
def whoosh(dur=1.0):
    n = int(dur * SR)
    y = sum(band_noise(n, lo, hi) * env(n, 0, 0, pk) * g
            for (lo, hi, pk, g) in [(250, 900, 0.42, 1.0), (900, 2800, 0.5, 0.8), (2800, 8000, 0.58, 0.45)])
    return reverb(pan(y / np.abs(y).max(), -0.6, 0.6), 0.32)

def sub_drop(dur=2.2):
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = 38 + 22 * np.exp(-t * 2.2)
    body = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 1.9) * np.clip(t / 0.006, 0, 1)
    thump = band_noise(n, 40, 400) * np.exp(-t * 14)
    y = body + 0.35 * thump
    return reverb(pan(y / np.abs(y).max(), 0, 0), 0.22)

def reverse_swell(dur=0.8):
    n = int(dur * SR)
    y = band_noise(n, 200, 4500, -0.3) * np.linspace(0, 1, n) ** 3
    return reverb(pan(y, 0.3, -0.3), 0.4)[:, :n + int(0.3 * SR)]

def riser(dur=1.4):
    n = int(dur * SR)
    y = band_noise(n, 1200, 9000) * env(n, 0, 0, 0.75)
    return reverb(pan(y, -0.2, 0.2), 0.45)

def impact(dur=1.6):
    n = int(dur * SR)
    t = np.arange(n) / SR
    low = np.sin(2 * np.pi * (62 + 30 * np.exp(-t * 30)) * t) * np.exp(-t * 5.5)
    mid = band_noise(n, 140, 900) * np.exp(-t * 18)
    click = band_noise(n, 2500, 12000) * np.exp(-t * 400)
    y = low + 0.45 * mid + 0.35 * click
    return reverb(pan(y / np.abs(y).max(), 0, 0), 0.3)

def tick():
    n = int(0.012 * SR)
    t = np.arange(n) / SR
    y = band_noise(n, 2500, 9000) * np.exp(-t * 900) * rng.uniform(0.6, 1.0)
    return pan(y, rng.uniform(-0.2, 0.2), 0)

# ---- ambience bed ---------------------------------------------------------------------------
DRONE = [(55.0, 1.0, 0.031), (82.41, 0.55, 0.047), (110.0, 0.4, 0.023), (164.81, 0.18, 0.061)]
PHASES = [(rng.uniform(0, 6.28), rng.uniform(0, 6.28)) for _ in DRONE]
DIPS = [v5.starts[i] for i in range(1, 110) if v5.kind[i] == "fadeblack"]

def add_bed(gain_db):
    """Drone + room air, written into the mix in 20 s blocks (air blocks overlap-crossfaded)."""
    blk, fade = 20 * SR, SR
    w = np.hanning(2 * fade)
    for s in range(0, N, blk):
        n = min(blk + fade, N - s)
        t = (s + np.arange(n)) / SR
        drone = sum(g * np.sin(2 * np.pi * f * t + p) * (0.65 + 0.35 * np.sin(2 * np.pi * lfo * t + q))
                    for (f, g, lfo), (p, q) in zip(DRONE, PHASES)) / 2.13
        air = np.stack([band_noise(n, 60, 2200, -0.8) for _ in range(2)]) * 0.5
        st = np.stack([drone, drone * 0.97]) * db(-6) + air * db(-14)
        shape = 1 + sum((db(4) - 1) * np.exp(-((t - c) / 1.4) ** 2) for c in DIPS)
        io = np.clip(t / 3, 0, 1) * np.clip((v5.RUNTIME - t) / 4, 0, 1)
        xf = np.ones(n)
        if s:
            xf[:fade] = w[:fade]
        if s + n < N:
            xf[-fade:] = w[fade:]
        mix[:, s:s + n] += (st * shape * io * xf * db(gain_db)).astype(np.float32)

if __name__ == "__main__":
    add_bed(-24)
    for i in range(1, 110):
        c = v5.starts[i]
        if v5.kind[i] == "fade":
            place(whoosh(), c - 0.5, -27)
        elif v5.kind[i] == "fadeblack":
            place(reverse_swell(), c - 0.8, -26)
            place(sub_drop(), c, -15)
    for slot, keys in v5.PUNCH.items():
        for t, _ in keys:
            place(riser(), t - 0.6, -31)
    for n, (t, val, label, k) in enumerate(v5.CARDS):
        a = round((t - 0.25) * v5.FPS) / v5.FPS
        b = a + v5.HOLD if n + 1 == len(v5.CARDS) else min(a + v5.HOLD, v5.CARDS[n + 1][0] - 0.3)
        place(impact(), a, -14)
        tt, gap = a + 0.05, 0.028
        while tt < a + 1.25:
            place(tick(), tt, -29)
            tt += gap
            gap *= 1.13
        place(whoosh(0.6), b - 0.55, -33)

    peak = np.abs(mix).max()
    pcm = (np.clip(mix, -1, 1).T * 32767).astype("<i2")
    with wave.open(str(SFX_WAV), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())

    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(PICTURE),
                    "-i", str(v5.AUDIO), "-i", str(SFX_WAV), "-filter_complex",
                    "[1:a]aresample=48000,aformat=channel_layouts=stereo[v];"
                    "[v][2:a]amix=inputs=2:normalize=0:duration=first,"
                    "alimiter=limit=0.89:level=false[a]",
                    "-map", "0:v:0", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                    "-ar", "48000", "-t", f"{v5.RUNTIME:.3f}", "-movflags", "+faststart", str(REVIEW)],
                   check=True)
    loud = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(REVIEW), "-map", "0:a", "-af",
                           "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    summary = loud[loud.rfind("Summary:"):]
    probe = json.loads(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries",
        "format=duration,size", "-of", "json", str(REVIEW)]))
    print(json.dumps({"sfx_peak_dbfs": round(float(20 * np.log10(peak + 1e-9)), 1),
                      "dissolve_whooshes": v5.kind.count("fade"), "chapter_drops": v5.kind.count("fadeblack"),
                      "punch_risers": sum(len(k) for k in v5.PUNCH.values()), "cards": len(v5.CARDS),
                      "duration": probe["format"]["duration"], "size": probe["format"]["size"],
                      "sha256": hashlib.sha256(REVIEW.read_bytes()).hexdigest()}, indent=2))
    print(" ".join(summary.split()))
