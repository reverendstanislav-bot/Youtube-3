#!/usr/bin/env python3
import csv, io, json, os, re, subprocess, sys, time, urllib.request, zipfile
from pathlib import Path
from PIL import Image, ImageOps

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
UA = {"User-Agent": "Youtube-3 deterministic picture assembly"}
AUDIO_URL = "https://d2ol7oe51mr4n9.cloudfront.net/user_3J3zfwu7kpgllQvPySWoLtXHwdR/18843c9b-c63d-49a6-b967-6f6e134564d7.mp3"
RUNTIME = 940.617
OUT = HERE / "15_PICTURE_ASSEMBLY_BUILD"
FRAMES = OUT / "frames"
OUT.mkdir(exist_ok=True)
FRAMES.mkdir(exist_ok=True)

def get_url(url, tries=5):
    err = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as e:
            err = e
            time.sleep(1 + i)
    raise err

def read_csv(path):
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

manifest = read_csv(HERE / "ASSET_MANIFEST.csv")
timeline = read_csv(HERE / "11_VISUAL_TIMELINE.csv")
reqc = read_csv(HERE / "13_R10_QUEUE001_075_REQC.csv")

candidate = {r["frame_slot"]: r["attempt_id"] for r in reqc if r.get("canonical_selected","").upper() == "TRUE"}

latest = {}
for fn in ["13_R11_RETRY_RESULTS.csv", "13_R12_RETRY_RESULTS.csv", "13_R13_F059_FINAL_RESULT.csv"]:
    p = HERE / fn
    if not p.exists():
        continue
    for r in read_csv(p):
        if r.get("frame_slot") and r.get("result_url"):
            latest[r["frame_slot"]] = r["result_url"]

bundles = [(1,12),(13,24),(25,36),(37,48),(49,60),(61,72),(73,84),(85,96),(97,108),
           (109,120),(121,132),(133,144),(145,156),(157,168),(169,180),(181,184)]
zip_cache = {}
zip_index = {}

def norm(s):
    s = Path(s).stem
    s = re.sub(r"^A\d+__", "", s, flags=re.I)
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")

for a,b in bundles:
    rel = Path("TEMP_ASSEMBLY_RECOVERY_PREVIEWS") / f"ATTEMPTS_{a:03d}_{b:03d}.zip"
    z = zipfile.ZipFile(HERE / rel)
    zip_cache[str(rel)] = z
    for name in z.namelist():
        if name.lower().endswith((".jpg",".jpeg",".png",".webp")):
            zip_index.setdefault(norm(name), []).append((str(rel), name))

special = {
    "F082": ("TEMP_ASSEMBLY_RECOVERY_PREVIEWS/ATTEMPTS_169_180.zip", "previews/A178__wide_cinematic_still_life_editorial_graphic_scene_2_batch_1.jpg"),
    "F083": ("TEMP_ASSEMBLY_RECOVERY_PREVIEWS/ATTEMPTS_169_180.zip", "previews/A175__a_high_contrast_cinematic_documentary_style_still_3_batch_2.jpg"),
    "F087": ("TEMP_ASSEMBLY_RECOVERY_PREVIEWS/ATTEMPTS_181_184.zip", "previews/A181__wide_cinematic_moody_still_life_graphic_composit.jpg"),
    "F088": ("TEMP_ASSEMBLY_RECOVERY_PREVIEWS/ATTEMPTS_169_180.zip", "previews/A180__wide_cinematic_documentary_style_scene_on_a_dark_t.jpg"),
}

resolver, source_class = {}, {}
for row in manifest:
    slot = row.get("asset_id","")
    if not re.fullmatch(r"F\d{3}", slot):
        continue
    uri = row.get("storage_uri","") or ""
    if slot in latest:
        resolver[slot] = ("url", latest[slot])
        source_class[slot] = "latest-retry"
    elif (uri.startswith("conversation:") or uri.startswith("chatgpt-library:")) and slot in special:
        resolver[slot] = ("zip", special[slot])
        source_class[slot] = "chat-recovery-preview-960x540"
    elif uri.startswith("http"):
        resolver[slot] = ("url", uri)
        source_class[slot] = "http"
    elif uri:
        resolver[slot] = ("file", HERE / uri)
        source_class[slot] = "git-relative"
    else:
        c = candidate.get(slot)
        if not c:
            raise RuntimeError(f"No recovery candidate for {slot}")
        q = norm(c)
        hits = zip_index.get(q, [])
        if not hits:
            hits = [v for k, vals in zip_index.items() if q in k or k in q for v in vals]
        if not hits:
            raise RuntimeError(f"No recovery preview for {slot}: {c}")
        resolver[slot] = ("zip", hits[0])
        source_class[slot] = "recovery-preview-960x540"

missing = [f"F{i:03d}" for i in range(1,111) if f"F{i:03d}" not in resolver]
if missing:
    raise RuntimeError(f"Unresolved slots: {missing}")

resolver_rows = []
for i in range(1,111):
    slot = f"F{i:03d}"
    kind, loc = resolver[slot]
    if kind == "url":
        data = get_url(loc)
        locator = loc
    elif kind == "file":
        data = Path(loc).read_bytes()
        locator = str(Path(loc).relative_to(HERE))
    else:
        zrel, name = loc
        data = zip_cache[zrel].read(name)
        locator = f"{zrel}::{name}"
    im = Image.open(io.BytesIO(data)).convert("RGB")
    sw, sh = im.size
    # Normalize every locked frame to a true full-frame 1920x1080 image.
    # ImageOps.fit scales both up and down and center-crops only when aspect ratios differ.
    # This fixes the previous thumbnail()+black-canvas bug that produced inset 960x540 frames.
    canvas = ImageOps.fit(
        im, (1920,1080),
        method=Image.Resampling.LANCZOS,
        centering=(0.5,0.5),
    )
    out_frame = FRAMES / f"{slot}.jpg"
    canvas.save(out_frame, "JPEG", quality=95, subsampling=0, optimize=True)
    resolver_rows.append([slot, source_class[slot], sw, sh, locator])

audio = OUT / "HARRISON_AUDIO_MASTER.mp3"
audio.write_bytes(get_url(AUDIO_URL))

by_slot = {r["generation_slot"]: r for r in timeline}
starts = [float(by_slot[f"F{i:03d}"]["start"]) for i in range(1,111)]
concat = OUT / "picture.ffconcat"
with open(concat, "w", encoding="utf-8") as f:
    f.write("ffconcat version 1.0\n")
    for i in range(110):
        slot = f"F{i+1:03d}"
        dur = starts[i+1]-starts[i] if i < 109 else RUNTIME-starts[i]
        f.write(f"file '{(FRAMES / (slot+'.jpg')).as_posix()}'\n")
        f.write(f"duration {dur:.6f}\n")
    f.write(f"file '{(FRAMES / 'F110.jpg').as_posix()}'\n")

resolver_csv = OUT / "FINAL_ASSEMBLY_ASSET_RESOLVER.csv"
with open(resolver_csv, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["frame_slot","source_class","source_width","source_height","source_locator"])
    w.writerows(resolver_rows)

video = OUT / "VIDEO_002_ADOBE_FIGMA_PICTURE_ASSEMBLY_V1_1080P25.mp4"
cmd = [
    "ffmpeg","-y","-hide_banner","-loglevel","warning",
    "-f","concat","-safe","0","-i",str(concat),"-i",str(audio),
    "-map","0:v:0","-map","1:a:0",
    "-vf","fps=25,format=yuv420p",
    "-c:v","libx264","-preset","veryfast","-crf","18","-profile:v","high","-level","4.1",
    "-color_primaries","bt709","-color_trc","bt709","-colorspace","bt709",
    "-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
    "-t",f"{RUNTIME:.3f}","-movflags","+faststart",str(video)
]
subprocess.run(cmd, check=True)

probe = subprocess.check_output([
    "ffprobe","-v","error","-show_entries",
    "format=duration,size:stream=index,codec_name,codec_type,width,height,r_frame_rate,sample_rate,channels",
    "-of","json",str(video)
], text=True)
(OUT / "FFPROBE.json").write_text(probe, encoding="utf-8")
sha = subprocess.check_output(["sha256sum", str(video)], text=True).strip()
(OUT / "SHA256.txt").write_text(sha+"\n", encoding="utf-8")

classes = {k: list(source_class.values()).count(k) for k in sorted(set(source_class.values()))}
report = {
    "runtime_sec": RUNTIME,
    "frames": 110,
    "resolution": "1920x1080",
    "fps": 25,
    "audio_master_media_id": "18843c9b-c63d-49a6-b967-6f6e134564d7",
    "source_classes": classes,
    "quality_hold": "40 slots use 960x540 recovery-preview images upscaled to 1920x1080; picture assembly is valid for edit/QC but is not a release-resolution master until full-resolution originals replace those preview sources."
}
(OUT / "BUILD_REPORT.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
print(json.dumps(report, indent=2))
