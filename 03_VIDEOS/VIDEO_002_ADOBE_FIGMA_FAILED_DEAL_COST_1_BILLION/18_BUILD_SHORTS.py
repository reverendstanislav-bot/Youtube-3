#!/usr/bin/env python3
"""VIDEO 002 — Stage 18: eight vertical Shorts cut from the locked V6 edit (07_SHORTS_LOCK.csv).

Each Short = one whole locked section (contiguous, no rewrite / reorder), 9:16 reframe only:
- background: the same picture, scaled to fill, blurred and darkened
- foreground: the full 16:9 frame (camera moves, punch-ins, number cards, film look) at 1080 wide
- top: short hook line (Bebas Neue) over a red rule
- below the picture: word-highlight captions re-set for vertical (Montserrat ExtraBold 64)
- audio: the V6 mix (voice + sound design) for the same window, short fades
Picture comes from a caption-free V5 render (cards + film look, no burned captions), built once.
Outputs (outside Git): <media>/18_UPLOAD_PACK/SHORTS/VIDEO_002_SH01.mp4 … SH08.mp4
"""
import csv, hashlib, importlib.util, json, os, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("v5", HERE / "15F_BUILD_V5.py")
v5 = importlib.util.module_from_spec(spec)
argv, sys.argv = sys.argv, sys.argv[:2]
spec.loader.exec_module(v5)
sys.argv = argv

MEDIA = v5.MEDIA
CLEAN = MEDIA / "18_UPLOAD_PACK" / "_work" / "VIDEO_002_V5_NO_CAPTIONS_1080P25.mp4"
V6 = MEDIA / "15G_V6" / "VIDEO_002_STAGE15G_REVIEW_V6_1080P25.mp4"
OUT = MEDIA / "18_UPLOAD_PACK" / "SHORTS"
WORK = CLEAN.parent
FONTS = v5.FONTS

SHORTS = {
    "SH01": "$1B FOR A DEAL\\NTHAT NEVER CLOSED",
    "SH02": "THE CLAUSE CAME\\NBEFORE THE DEAL",
    "SH03": "NOT A PENALTY",
    "SH04": "NO FINAL \"NO\" YET",
    "SH05": "HOW THE DEAL\\NACTUALLY ENDED",
    "SH06": "3 DAYS LATER:\\N$1,000,000,000",
    "SH07": "$20B IS NOT $1B",
    "SH08": "FIGMA AFTER ADOBE",
}

WHITE, RED = "&H00EDEDED", "&H002222D3"

def ass_t(s):
    cs = int(round(max(s, 0) * 100)); h, cs = divmod(cs, 360000); m, cs = divmod(cs, 6000); sec, cs = divmod(cs, 100)
    return f"{h}:{m:02d}:{sec:02d}.{cs:02d}"

def render_clean():
    """V5 picture without burned captions (cards + film look kept)."""
    if CLEAN.exists():
        return
    WORK.mkdir(parents=True, exist_ok=True)
    inputs, parts, prev = [], [], "[0:v]"
    for i in range(110):
        inputs += ["-i", str(v5.CLIPS / f"C{i + 1:03d}.mp4")]
    for i in range(1, 110):
        t = v5.trans[i]
        xk = "fadeblack" if v5.kind[i] == "fadeblack" else "fade"
        parts.append(f"{prev}[{i}:v]xfade=transition={xk}:duration={t}:offset={v5.starts[i] - t / 2:.3f}[v{i}]")
        prev = f"[v{i}]"
    cards = v5.OUT / "VIDEO_002_STAGE15F_CARDS.ass"
    fonts = os.path.relpath(FONTS, WORK).replace("\\", "/")
    cards_rel = os.path.relpath(cards, WORK).replace("\\", "/")
    parts.append(f"{prev}fps={v5.FPS},ass={cards_rel}:fontsdir={fonts},{v5.LOOK},format=yuv420p[vout]")
    graph = WORK / "clean_graph.txt"
    graph.write_text(";\n".join(parts), encoding="utf-8")
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", *inputs,
                    "-/filter_complex", graph.name, "-map", "[vout]", "-an",
                    "-c:v", "libx264", "-preset", "fast", "-crf", "16", "-t", f"{v5.RUNTIME:.3f}",
                    str(CLEAN)], check=True, cwd=WORK)

def section_window(sec):
    w = [x for x in csv.DictReader(open(HERE / "11_WORD_TRANSCRIPT.csv", encoding="utf-8-sig")) if x["section"] == sec]
    words = [(x["word"], float(x["start"]), float(x["end"])) for x in w]
    return words, words[0][1] - 0.15, min(words[-1][2] + 0.6, v5.RUNTIME)

def captions(words, t0, path, hook):
    """Vertical word-highlight captions, timed relative to the Short start t0."""
    cues, cur = [], []
    for wd in words:
        if cur and (len(" ".join(x[0] for x in cur + [wd])) > 34 or wd[1] - cur[-1][2] > 0.7):
            cues.append(cur); cur = []
        cur.append(wd)
        if wd[0][-1] in ".?!" and len(" ".join(x[0] for x in cur)) >= 10:
            cues.append(cur); cur = []
    if cur:
        cues.append(cur)
    ev = []
    for n, c in enumerate(cues):
        end = min(cues[n + 1][0][1] if n + 1 < len(cues) else c[-1][2] + 0.6, c[-1][2] + 0.6)
        for k in range(len(c)):
            s = c[0][1] if k == 0 else c[k][1]
            e = end if k == len(c) - 1 else c[k + 1][1]
            toks = [("{\\c" + RED + "}" + x[0] + "{\\c" + WHITE + "}") if j == k else x[0] for j, x in enumerate(c)]
            half = len(c) // 2 if len(" ".join(x[0] for x in c)) > 18 else len(c)
            text = " ".join(toks[:half]) + ("\\N" + " ".join(toks[half:]) if half < len(c) else "")
            ev.append(f"Dialogue: 2,{ass_t(s - t0)},{ass_t(max(e, s + 0.04) - t0)},Cap,,0,0,0,,{text}")
    dur = words[-1][2] + 0.6 - t0
    ev.append(f"Dialogue: 1,{ass_t(0)},{ass_t(dur)},Hook,,0,0,0,,{{\\fad(250,0)}}{hook}")
    ev.append(f"Dialogue: 1,{ass_t(0)},{ass_t(dur)},Rule,,0,0,0,,{{\\fad(250,0)\\p1}}m 465 452 l 615 452 615 460 465 460")
    path.write_text("""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: Cap,Montserrat ExtraBold,64,&H00EDEDED,&H00EDEDED,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,4,0,8,70,70,1290,1
Style: Hook,Bebas Neue,118,&H00EDEDED,&H00EDEDED,&H00000000,&H00000000,0,0,0,0,100,100,2,0,1,0,0,2,60,60,1490,1
Style: Rule,Arial,20,&H002222D3,&H002222D3,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""" + "\n".join(ev) + "\n", encoding="utf-8")

def build(sid, sec):
    words, a, b = section_window(sec)
    ass = WORK / f"{sid}.ass"
    captions(words, a, ass, SHORTS[sid])
    out = OUT / f"VIDEO_002_{sid}.mp4"
    dur = b - a
    fonts = os.path.relpath(FONTS, WORK).replace("\\", "/")
    vf = ("[0:v]split[bg][fg];"
          "[bg]scale=-2:1920,crop=1080:1920,gblur=sigma=40,eq=brightness=-0.30:saturation=0.7[bgb];"
          "[fg]scale=1080:-2[fgs];"
          "[bgb][fgs]overlay=0:620,"
          f"ass={ass.name}:fontsdir={fonts},format=yuv420p[v];"
          f"[1:a]afade=t=in:d=0.12,afade=t=out:st={dur - 0.45:.2f}:d=0.45[a]")
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
                    "-ss", f"{a:.3f}", "-t", f"{dur:.3f}", "-i", str(CLEAN),
                    "-ss", f"{a:.3f}", "-t", f"{dur:.3f}", "-i", str(V6),
                    "-filter_complex", vf, "-map", "[v]", "-map", "[a]",
                    "-c:v", "libx264", "-preset", "slow", "-tune", "grain", "-crf", "19", "-r", "25",
                    "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", str(out)],
                   check=True, cwd=WORK)
    return {"short": sid, "section": sec, "start": round(a, 3), "end": round(b, 3), "duration": round(dur, 2),
            "file": out.name, "sha256": hashlib.sha256(out.read_bytes()).hexdigest()}

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    render_clean()
    lock = list(csv.DictReader(open(HERE / "07_SHORTS_LOCK.csv", encoding="utf-8-sig")))
    res = [build(r["short_id"], r["section_start"]) for r in lock]
    (OUT / "SHORTS_MANIFEST.json").write_text(json.dumps(res, indent=2), encoding="utf-8")
    print(json.dumps(res, indent=2))
