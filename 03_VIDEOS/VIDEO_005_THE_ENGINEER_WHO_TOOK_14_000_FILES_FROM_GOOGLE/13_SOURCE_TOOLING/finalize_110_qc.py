from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import csv, hashlib, json, collections

ROOT=Path(r"C:\Users\KK\Desktop\Youtube\Youtube-3-video005-gfx\03_VIDEOS\VIDEO_005_THE_ENGINEER_WHO_TOOK_14_000_FILES_FROM_GOOGLE")
INDEX=ROOT/"13_FINAL_ASSET_INDEX.csv"
QC=ROOT/"13_ALL_110_ASSET_QC.csv"
MAN=ROOT/"ASSET_MANIFEST.csv"

def sha256(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()

with INDEX.open(encoding="utf-8-sig",newline="") as f:
    rows=list(csv.DictReader(f))
assert len(rows)==110, len(rows)
counts=collections.Counter(r["primary_class"] for r in rows)
assert counts=={"EDITOR_GRAPHIC":60,"AUTHENTIC_SOURCE":37,"LICENSED_OR_USABLE_CONTEXT":3,"GENERATED_ILLUSTRATION":10}, counts
prev=0
for r in rows:
    assert int(r["start_frame"])==prev,(r["asset_id"],prev,r["start_frame"])
    prev=int(r["end_frame_exclusive"])
    p=ROOT/r["master_path"]
    assert p.is_file(),p
    with Image.open(p) as im:
        im.load()
        assert im.size==(1920,1080),(r["asset_id"],im.size)
    r["sha256"]=sha256(p)
assert prev==24876,prev
with INDEX.open("w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys(),lineterminator="\n"); w.writeheader(); w.writerows(rows)
idx={r["asset_id"]:r for r in rows}

with QC.open(encoding="utf-8-sig",newline="") as f:
    qrows=list(csv.DictReader(f))
assert len(qrows)==110
for r in qrows:
    i=idx[r["asset_id"]]
    r["sha256"]=i["sha256"]; r["dimensions"]="1920x1080"; r["decode"]="PASS"; r["edit_readiness"]="PASS"
with QC.open("w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,fieldnames=qrows[0].keys(),lineterminator="\n"); w.writeheader(); w.writerows(qrows)

with MAN.open(encoding="utf-8-sig",newline="") as f:
    mrows=list(csv.DictReader(f))
for r in mrows:
    if r["asset_id"] in idx:
        i=idx[r["asset_id"]]
        r["storage_uri"]=i["master_path"]; r["sha256"]=i["sha256"]
        if r["asset_id"] in {"V005-VP033","V005-VP039","V005-VP109"}:
            r["version"]="20261015_R3_SEMANTIC_SOURCE_FIX"
with MAN.open("w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,fieldnames=mrows[0].keys(),quoting=csv.QUOTE_ALL,lineterminator="\n"); w.writeheader(); w.writerows(mrows)

font=ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf",22)
small=ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf",16)
def sheets(items,outdir,prefix):
    outdir.mkdir(parents=True,exist_ok=True)
    for old in outdir.glob(f"{prefix}_*.jpg"): old.unlink()
    made=[]
    for page in range((len(items)+11)//12):
        c=Image.new("RGB",(1920,1080),(18,18,18)); d=ImageDraw.Draw(c)
        for j,r in enumerate(items[page*12:(page+1)*12]):
            col=j%4; row=j//4; x=col*480; y=row*360
            im=Image.open(ROOT/r["master_path"]).convert("RGB")
            im.thumbnail((464,261),Image.Resampling.LANCZOS)
            c.paste(im,(x+8,y+38))
            d.text((x+10,y+8),f'{r["asset_id"]}  {r["primary_class"]}',font=font,fill=(245,240,230))
            d.text((x+10,y+306),f'{r["start_sec"]}s–{r["end_sec"]}s',font=small,fill=(190,190,190))
        p=outdir/f"{prefix}_{page+1:02}.jpg"; c.save(p,quality=90); made.append(p)
    return made
sheets([r for r in rows if r["primary_class"]=="AUTHENTIC_SOURCE"],ROOT/"13_AUTHENTIC_OUTPUT","CONTACT_SHEET")
made=sheets(rows,ROOT/"13_ALL_110_CONTACT_SHEETS","CONTACT_SHEET")
thumbs=[]
for p in made:
    im=Image.open(p).convert("RGB"); im.thumbnail((960,540),Image.Resampling.LANCZOS); thumbs.append(im.copy())
combined=Image.new("RGB",(1920,((len(thumbs)+1)//2)*540),(12,12,12))
for n,im in enumerate(thumbs): combined.paste(im,((n%2)*960,(n//2)*540))
combined.save(ROOT/"13_ALL_110_CONTACT_SHEETS"/"ALL_10_SHEETS.jpg",quality=88)

report={
  "status":"PASS_FOR_EDIT",
  "asset_count":len(rows),
  "class_counts":dict(counts),
  "dimensions":"110/110 1920x1080",
  "decode":"110/110 PASS",
  "hashes":"110/110 INDEX MATCH",
  "timeline_continuity":"0-24876 continuous at 25fps",
  "duration_seconds":24876/25,
  "release_rights":"37 AUTHENTIC_SOURCE remain HOLD_CASE_BY_CASE",
  "motion_qc":"PENDING_DAVINCI"
}
(ROOT/"13_LIGHT_QC_FINAL.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
print(json.dumps(report,indent=2))
