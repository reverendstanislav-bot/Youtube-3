#!/usr/bin/env python3
"""Produce unbaked authentic documentary source and marker masks for VIDEO004.
No generated imagery, no fabricated documents, no automatic edit approval.
"""
import csv, hashlib, json, pathlib
import fitz
from PIL import Image, ImageDraw

D=pathlib.Path(__file__).resolve().parent
OUT=D/"12_VERIFIED_SOURCE_LAYERS"
OUT.mkdir(exist_ok=True)
geo=json.loads((D/"12_SOURCE_DOCUMENT_GEOMETRY.json").read_text("utf8"))
rows=list(csv.DictReader((D/"12_RESOLVE_PDF_CROPS_V3.csv").open(newline="",encoding="utf8")))
blue={r["shot_id"]:r for r in csv.DictReader((D/"12_RESOLVE_COMPOSITIONS_V3.csv").open(newline="",encoding="utf8"))}
sync={r["shot_id"]:r for r in csv.DictReader((D/"12_RESOLVE_MARKER_WORD_SYNC_V3.csv").open(newline="",encoding="utf8"))}
index={"status":"DOCUMENT_LAYERS_BUILT_PENDING_VISUAL_QC","canvas":[1920,1080],"fps":25,"source_crops":{},"shots":{},"notes":"Authentic original PDF crop + independent transparent rectangle mask. Match original and source ID; mask uses Fusion multiply as separate layer. Not a final rendered frame."}
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
for r in rows:
    sid=r["source"].replace(".pdf","")
    src=D/"12_SOURCE_PDF_DOWNLOADS"/r["source"]
    if not src.exists():raise FileNotFoundError(src)
    if sha(src)!=r["sha256"]:raise ValueError("Original source SHA mismatch: "+sid)
    page=int(r["page0"])
    rect=[float(v) for v in (r["crop_x0_pt"]+"|"+r["crop_y0_pt"]+"|"+r["crop_x1_pt"]+"|"+r["crop_y1_pt"]).split("|")] if "crop_x0_pt" in r else None
    # Current CSV stores crop as pipe-separated vector.
    if rect is None:rect=[float(x) for x in r["crop_rect_pdf_pt"].split("|")]
    target=[float(x) for x in r["marker_rect_px"].split("|")]
    x,y,w,h=[int(float(z)) for z in r["destination_rect_px"].split("|")]
    doc=fitz.open(src)
    pg=doc[page]
    crop=fitz.Rect(*rect)
    crop_key=hashlib.sha256((sid+str(page)+str(rect)).encode()).hexdigest()[:12]
    name=f"{sid}_p{page+1:02d}_{crop_key}"
    dest=OUT/(name+"_DOCUMENT.png")
    if not dest.exists():
        pix=pg.get_pixmap(matrix=fitz.Matrix(w/crop.width,h/crop.height),clip=crop,alpha=False)
        layer=Image.new("RGBA",(1920,1080),(0,0,0,0))
        im=Image.frombytes("RGB",(pix.width,pix.height),pix.samples).convert("RGBA")
        if im.size!=(w,h):im=im.resize((w,h),Image.Resampling.LANCZOS)
        layer.paste(im,(x,y))
        layer.save(dest,optimize=True)
        index["source_crops"][name]={"source_sha256":sha(src),"original_pdf":r["source"],"page0":page,"crop_pdf_pt":rect,"image_sha256":sha(dest),"file":dest.name,"dest_rect_px":[x,y,w,h]}
    ms=OUT/(name+"_MARKER_ALPHA.png")
    if not ms.exists():
        mask=Image.new("RGBA",(1920,1080),(0,0,0,0))
        draw=ImageDraw.Draw(mask)
        mx,my,mw,mh=target
        draw.rectangle((round(mx),round(my),round(mx+mw),round(my+mh)),fill=(214,180,74,110))
        mask.save(ms,optimize=True)
    plan=blue[r["shot"]]
    mark_allowed=sync.get(r["shot"],{}).get("status","").startswith("ASR_WORD_ANCHORED")
    index["shots"][r["shot"]]={"source_key":name,"document_layer":dest.name,"marker_layer":ms.name if mark_allowed else None,
      "marker_allowed":mark_allowed,"marker_keyframes_local":("F"+sync[r["shot"]]["marker_start_local_frame"]+"..F"+sync[r["shot"]]["marker_end_local_frame"]+" ASR word provisional; needs human audition") if mark_allowed else "NONE",
      "source_line_pt":r["native_rect_pdf_pt"],"marker_rect_px":target,"status":"SOURCE_DERIVED__NOT_HUMAN_VISUAL_QC"}
with (OUT/"12_LAYER_ASSET_MANIFEST.json").open("w",encoding="utf8") as f:json.dump(index,f,indent=2,ensure_ascii=False)
print(json.dumps({"mapped_shots":len(index["shots"]),"unique_documents":len(index["source_crops"]),"marker_enabled":sum(x["marker_allowed"] for x in index["shots"].values())}))
