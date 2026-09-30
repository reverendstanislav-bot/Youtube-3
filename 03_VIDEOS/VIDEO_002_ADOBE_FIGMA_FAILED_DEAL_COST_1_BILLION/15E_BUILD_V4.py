#!/usr/bin/env python3
"""VIDEO 002 — Stage 15E (V4): continuous camera + premium number cards, built from V3.

Owner feedback on V3: motion graphics good but should be smoother / more premium; the zoom
in-out ruins it; the text punch-ins were great; still reads as a slideshow, not a film.
1. Camera: one constant-velocity push-in on every beat (never reverses, never eases to a stop
   at a cut). Punch-ins on narrated numbers blend in with smootherstep over 1.2 s and keep drifting.
2. Cut rhythm (unchanged from V3): hard cuts in running speech, 0.5 s dissolves on pauses
   >= 0.95 s, 0.9 s dip-to-black at chapter changes.
3. Number cards: every frame is its own eased ASS event — plate fades in, figure resolves from
   blur and 110 % scale while counting up, red rule grows from the centre, label rises in late.
Captions (15B) stay on top; voice-only audio. V2 / V3 untouched.
Output (outside Git): <media>/15E_V4/VIDEO_002_STAGE15E_REVIEW_V4_1080P25.mp4
"""
import csv, hashlib, json, math, os, shutil, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent
MEDIA = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("C:/Users/KK/Documents/WhatItCost_media/002-adobe-figma")
FRAMES = HERE / "15_FINAL_FRAMES_1080P"
AUDIO = MEDIA / "15_ASSEMBLY_V2" / "HARRISON_AUDIO_MASTER.mp3"
CAPTIONS = MEDIA / "15B_CAPTIONS" / "VIDEO_002_STAGE15B_CAPTIONS.ass"
FONT_SRC = [MEDIA.parent / "_fonts" / "Montserrat-ExtraBold.ttf",
            MEDIA.parent / "_fonts" / "ttf" / "BebasNeue-Regular.ttf"]
OUT = MEDIA / "15E_V4"
CLIPS = OUT / "clips"
FONTS = OUT / "fonts"
REVIEW = OUT / "VIDEO_002_STAGE15E_REVIEW_V4_1080P25.mp4"
RUNTIME = 940.617
FPS = 25
W, H = 1920, 1080
T_HARD, T_SOFT, T_CHAPTER = 0.04, 0.5, 0.9
SOFT_PAUSE = 0.95
ZPUNCH = 1.35

rows = sorted(csv.DictReader(open(HERE / "11_VISUAL_TIMELINE.csv", encoding="utf-8-sig")),
              key=lambda r: int(r["generation_slot"][1:]))
assert len(rows) == 110
words = [(float(w["start"]), float(w["end"])) for w in
         csv.DictReader(open(HERE / "11_WORD_TRANSCRIPT.csv", encoding="utf-8-sig"))]
starts = [float(r["start"]) for r in rows] + [RUNTIME]
starts[0] = 0.0

# frame -> [(word start, box x0 y0 x1 y1 in 1920x1080)] — where the narrated number sits in the frame
PUNCH = {
    "F002": [(9.60, (810, 555, 1860, 705))],      # "billion dollars" -> fee clause
    "F025": [(210.06, (30, 75, 645, 810)),        # "June nineteenth: twenty billion" -> June 19 card
             (212.82, (645, 75, 1290, 810))],     # "July fifth" -> July 5 card
    "F030": [(249.66, (720, 230, 1560, 330))],    # "one billion dollars" -> $1,000,000,000 line
    "F079": [(672.60, (900, 200, 1880, 340))],    # "one billion dollars" -> 8-K line
    "F086": [(735.78, (90, 60, 630, 540))],       # "about twenty billion" -> ~$20B
    "F091": [(782.24, (30, 90, 750, 330))],       # "twenty-one billion" -> NOT $21B
    "F096": [(828.48, (600, 450, 1850, 620))],    # "twelve-point-five million" -> share count
}
# (word start, value, label, format) — figures exactly as narrated
CARDS = [
    (7.82, 1_000_000_000, "PAID TO FIGMA", "int"),
    (104.54, 20_000_000_000, "APPROXIMATE DEAL VALUE", "int"),
    (129.82, 1_000_000_000, "TERMINATION FEE", "int"),
    (747.58, 20_000_000_000, "NOT PAID", "int"),
    (750.34, 1_000_000_000, "ACTUALLY PAID", "int"),
    (836.62, 393.1, "APPROX. NET PROCEEDS", "m1"),
    (922.14, 1_000_000_000, "PAID TO FIGMA", "int"),
]

# ---- cut rhythm -------------------------------------------------------------------------
def pause_at(c):
    before = max([e for s, e in words if e <= c + 0.05] or [0.0])
    after = min([s for s, e in words if s >= c - 0.05] or [c])
    return after - before

kind, trans = ["-"], [0.0]
for i in range(1, 110):
    if rows[i]["section"] != rows[i - 1]["section"]:
        k = "fadeblack"
    elif rows[i - 1]["generation_slot"] in PUNCH or pause_at(starts[i]) < SOFT_PAUSE:
        k = "hard"
    else:
        k = "fade"
    kind.append(k)
    trans.append({"fadeblack": T_CHAPTER, "fade": T_SOFT, "hard": T_HARD}[k])
trans.append(0.0)

# ---- camera -----------------------------------------------------------------------------
# V4: one continuous camera. Constant-velocity push-in (never reverses, never stops at a cut),
# so the film reads as a camera move, not a slideshow. Punch-ins blend in with smootherstep
# and keep the same forward drift after they land.
RATE = 0.0035        # zoom per second of the base push (<= ~4 % on the longest beat)
MOVE = 1.2           # punch-in travel, s

def smooth(x):
    x = min(max(x, 0.0), 1.0)
    return x * x * x * (x * (6 * x - 15) + 10)

def target(box):
    x0, y0, x1, y1 = box
    z = min(ZPUNCH, 0.85 * W / (x1 - x0), 0.85 * H / (y1 - y0))
    return z, (x0 + x1) / 2, (y0 + y1) / 2

def clamp(z, cx, cy):
    hw, hh = W / 2 / z, H / 2 / z
    return z, min(max(cx, hw), W - hw), min(max(cy, hh), H - hh)

def camera(i, n, t0):
    """Per-frame (zoom, cx, cy); t0 = clip start on the film timeline."""
    keys = [(t - 0.6 - t0, target(b)) for t, b in PUNCH.get(rows[i]["generation_slot"], [])]
    out = []
    for f in range(n):
        t = f / FPS
        state = (1 + RATE * t, W / 2, H / 2)
        for kt, (tz, tx, ty) in keys:
            if t < kt:
                break
            a = smooth((t - kt) / MOVE)
            goal = (tz * (1 + RATE * (t - kt)), tx, ty)
            state = tuple(s + (g - s) * a for s, g in zip(state, goal))
        out.append(clamp(*state))
    return out

def clip(i):
    out = CLIPS / f"C{i + 1:03d}.mp4"
    if os.environ.get("REUSE_CLIPS") and out.exists():
        return i
    lead = trans[i] / 2
    t0 = starts[i] - lead
    n = math.ceil((starts[i + 1] + trans[i + 1] / 2 - t0) * FPS) + 1
    img = Image.open(FRAMES / f"F{i + 1:03d}.jpg").convert("RGB")
    enc = subprocess.Popen(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-f", "rawvideo",
                            "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                            "-c:v", "libx264", "-preset", "fast", "-crf", "14", "-pix_fmt", "yuv420p",
                            str(out)], stdin=subprocess.PIPE)
    for z, cx, cy in camera(i, n, t0):
        a = 1 / z
        f = img.transform((W, H), Image.AFFINE, (a, 0, cx - W / 2 * a, 0, a, cy - H / 2 * a),
                          resample=Image.BICUBIC)
        enc.stdin.write(f.tobytes())
    enc.stdin.close()
    if enc.wait():
        raise RuntimeError(out)
    return i

# ---- number cards (ASS layers 0-1, captions stay on layer 2) ------------------------------
# ---- number cards (ASS layers 0-1, captions stay on layer 2) ------------------------------
def ass_t(s):
    cs = int(round(s * 100)); h, cs = divmod(cs, 360000); m, cs = divmod(cs, 6000); sec, cs = divmod(cs, 100)
    return f"{h}:{m:02d}:{sec:02d}.{cs:02d}"

def fmt(v, k):
    return f"${v:.1f}M" if k == "m1" else f"${int(round(v)):,}"

FULL = "m 0 0 l 1920 0 1920 1080 0 1080"

# V4 cards: every frame of the animation is its own event with eased values (no stepped fades).
HOLD, T_IN, T_OUT = 2.6, 1.0, 0.55
BAR_W = 170

def eo(x):  # ease-out cubic
    x = min(max(x, 0.0), 1.0)
    return 1 - (1 - x) ** 3

def eo_expo(x):
    x = min(max(x, 0.0), 1.0)
    return 1.0 if x >= 1 else 1 - 2 ** (-10 * x)

def alpha(op):
    return f"&H{int(round(255 * (1 - min(max(op, 0.0), 1.0)))):02X}&"

def card_events():
    ev = []
    for n, (t, val, label, k) in enumerate(CARDS):
        a = round((t - 0.25) * FPS) / FPS
        b = a + HOLD if n + 1 == len(CARDS) else min(a + HOLD, CARDS[n + 1][0] - 0.3)
        frames = int(round((b - a) * FPS))
        for f in range(frames):
            p = f / FPS
            tt = a + p
            span = f"{ass_t(tt)},{ass_t(tt + 1 / FPS)}"
            out = eo((p - (b - a - T_OUT)) / T_OUT)          # 0 -> 1 during the exit
            keep = 1 - out
            # plate
            plate = 0.88 * smooth(p / 0.5) * keep
            ev.append(f"Dialogue: 0,{span},Plate,,0,0,0,,{{\\1a{alpha(plate)}\\p1}}{FULL}")
            # number: blur-to-sharp, settles from 110 %, tracking closes, value counts up
            e = eo(p / T_IN)
            sc = (110 - 10 * e) * (1 - 0.03 * out)
            ev.append(f"Dialogue: 1,{span},Num,,0,0,0,,{{\\an5\\pos(960,{520 - 8 * out:.1f})"
                      f"\\alpha{alpha(eo(p / 0.55) * keep)}\\blur{9 * (1 - eo(p / 0.75)) + 5 * out:.2f}"
                      f"\\fscx{sc:.2f}\\fscy{sc:.2f}\\fsp{2 + 16 * (1 - e):.2f}}}"
                      f"{fmt(val * eo_expo(p / 1.3), k)}")
            # red bar grows from the centre
            w = BAR_W * eo((p - 0.3) / 0.6) * keep
            if w > 0.5:
                x0, x1 = 960 - w / 2, 960 + w / 2
                ev.append(f"Dialogue: 1,{span},Plate,,0,0,0,,{{\\1c&H2222D3&\\1a{alpha(keep)}\\p1}}"
                          f"m {x0:.1f} 610 l {x1:.1f} 610 {x1:.1f} 618 {x0:.1f} 618")
            # label rises in after the bar
            le = eo((p - 0.5) / 0.6)
            if le > 0:
                ev.append(f"Dialogue: 1,{span},Label,,0,0,0,,{{\\an8\\pos(960,{640 + 14 * (1 - le) - 8 * out:.1f})"
                          f"\\alpha{alpha(le * keep)}\\fsp{3 + 10 * (1 - le):.2f}}}{label}")
    return ev

STYLES = ("Style: Plate,Arial,20,&H00000000,&H00000000,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1\n"
          "Style: Num,Bebas Neue,190,&H00EDEDED,&H00EDEDED,&H00000000,&H00000000,0,0,0,0,100,100,2,0,1,0,0,2,0,0,0,1\n"
          "Style: Label,Montserrat ExtraBold,46,&H002222D3,&H002222D3,&H00000000,&H00000000,-1,0,0,0,100,100,3,0,1,0,0,8,0,0,0,1\n")


# ---- render -------------------------------------------------------------------------------
if __name__ == "__main__":
    for d in (CLIPS, FONTS):
        d.mkdir(parents=True, exist_ok=True)
    for f in FONT_SRC:
        shutil.copy2(f, FONTS / f.name)
    ass = OUT / "VIDEO_002_STAGE15E_CAPTIONS_CARDS.ass"
    cap = CAPTIONS.read_text(encoding="utf-8").replace("\n[Events]", STYLES + "\n[Events]")
    ass.write_text(cap.rstrip("\n") + "\n" + "\n".join(card_events()) + "\n", encoding="utf-8")

    with ThreadPoolExecutor(max_workers=max(2, (os.cpu_count() or 4) // 2)) as ex:
        list(ex.map(clip, range(110)))
    inputs, parts, prev = [], [], "[0:v]"
    for i in range(110):
        inputs += ["-i", str(CLIPS / f"C{i + 1:03d}.mp4")]
    for i in range(1, 110):
        t = trans[i]
        xk = "fadeblack" if kind[i] == "fadeblack" else "fade"
        parts.append(f"{prev}[{i}:v]xfade=transition={xk}:duration={t}:offset={starts[i] - t / 2:.3f}[v{i}]")
        prev = f"[v{i}]"
    parts.append(f"{prev}fps={FPS},ass={ass.name}:fontsdir={FONTS.name},format=yuv420p[vout]")
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
    print(json.dumps({"cuts": {k: kind.count(k) for k in ("hard", "fade", "fadeblack")},
                      "punch_beats": len(PUNCH), "cards": len(CARDS),
                      "duration": probe["format"]["duration"], "size": probe["format"]["size"],
                      "sha256": hashlib.sha256(REVIEW.read_bytes()).hexdigest()}, indent=2))
