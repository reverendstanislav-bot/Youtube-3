#!/usr/bin/env python3
import csv, io, hashlib, re, time, urllib.request, zipfile
from pathlib import Path
from PIL import Image, ImageOps

HERE = Path(__file__).resolve().parent
UA = {"User-Agent": "Youtube-3 final-frame exporter"}
OUT = HERE / "15_FINAL_FRAMES_1080P"
OUT.mkdir(exist_ok=True)

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
zip_cache, zip_index = {}, {}

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
        resolver[slot] = ("url", latest[slot]); source_class[slot] = "latest-retry"
    elif (uri.startswith("conversation:") or uri.startswith("chatgpt-library:")) and slot in special:
        resolver[slot] = ("zip", special[slot]); source_class[slot] = "chat-recovery-preview"
    elif uri.startswith("http"):
        resolver[slot] = ("url", uri); source_class[slot] = "http"
    elif uri:
        resolver[slot] = ("file", HERE / uri); source_class[slot] = "git-relative"
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
        resolver[slot] = ("zip", hits[0]); source_class[slot] = "recovery-preview"

missing = [f"F{i:03d}" for i in range(1,111) if f"F{i:03d}" not in resolver]
if missing:
    raise RuntimeError(f"Unresolved slots: {missing}")

rows=[]
for i in range(1,111):
    slot=f"F{i:03d}"
    kind,loc=resolver[slot]
    if kind=="url":
        data=get_url(loc); locator=loc
    elif kind=="file":
        data=Path(loc).read_bytes(); locator=str(Path(loc).relative_to(HERE))
    else:
        zrel,name=loc; data=zip_cache[zrel].read(name); locator=f"{zrel}::{name}"

    im=Image.open(io.BytesIO(data)).convert("RGB")
    sw,sh=im.size
    normalized=ImageOps.fit(
        im,(1920,1080),
        method=Image.Resampling.LANCZOS,
        centering=(0.5,0.5),
    )
    out=OUT/f"{slot}.jpg"
    normalized.save(out,"JPEG",quality=95,subsampling=0,optimize=True)
    sha=hashlib.sha256(out.read_bytes()).hexdigest()
    rows.append([
        slot,source_class[slot],sw,sh,"1920","1080",
        "YES" if sw<1920 or sh<1080 else "NO",
        locator,sha,out.stat().st_size
    ])

with open(OUT/"FRAME_EXPORT_MANIFEST.csv","w",newline="",encoding="utf-8") as f:
    w=csv.writer(f)
    w.writerow([
        "frame_slot","source_class","source_width","source_height",
        "output_width","output_height","upscaled",
        "source_locator","sha256","file_size_bytes"
    ])
    w.writerows(rows)

with open(OUT/"README.md","w",encoding="utf-8") as f:
    f.write("""# VIDEO 002 — Final Frames 1080p

This folder contains the canonical locked F001–F110 frame set normalized to **1920×1080** with no black inset borders.

- exactly 110 JPEG frames;
- exact output size: 1920×1080;
- JPEG quality 95, 4:4:4;
- latest approved R11/R12/R13 retries are used where applicable;
- no new AI generation is performed by this exporter.

Important: some older locked frames are only recoverable from 960×540 preview archives. Those files are upscaled to 1920×1080 here and are explicitly marked `upscaled=YES` in `FRAME_EXPORT_MANIFEST.csv`. This folder fixes the black-border/inset bug; it does not pretend those preview-backed frames are native-resolution originals.
""")

print(f"Exported {len(rows)} frames to {OUT}")
