#!/usr/bin/env python3
"""Read-only audit of VIDEO005 Stage13 originals and crops. NO IMAGE GENERATION."""
from pathlib import Path
import csv,json,hashlib,re,collections
import fitz
from PIL import Image
R=Path(__file__).resolve().parents[1]
origin=R/"13_SOURCE_REAL_ACQUISITION"
records=json.loads((origin/"REAL_CROP_QC_LEDGER_FINAL.json").read_text())
sources=json.loads((origin/"SOURCE_DOWNLOAD_LEDGER_FINAL.json").read_text())
asset_rows=list(csv.DictReader((R/"13_SOURCE_CROP_ACQUISITION_LEDGER.csv").open(encoding="utf-8")))
assert len(sources)==13 and len(asset_rows)==37 and len({r["asset_id"] for r in asset_rows})==37
def sha(path):
 h=hashlib.sha256()
 with open(path,"rb") as f:
  for b in iter(lambda:f.read(1024*1024),b""):h.update(b)
 return h.hexdigest()
by_source={s["source_id"]:s for s in sources}
existing=set()
checks=[]
for rec in records:
 asset=rec["asset_id"];sid=rec["source_id"]
 if (asset,sid) in existing:raise ValueError("duplicate "+asset+":"+sid)
 existing.add((asset,sid))
 src=by_source[sid]
 ext=src["type"]
 orig=origin/"original_sources"/(sid+"."+ext)
 png=origin/"native_crops"/(asset+"__"+sid+".png")
 ok_ori=orig.exists() and sha(orig)==src["source_sha256_verified_final"]
 ok_crop=png.exists() and sha(png)==rec.get("crop_sha256")
 if png.exists():
  with Image.open(png) as im:size=list(im.size)
 else:size=None
 item={
  "asset_id":asset,"source_id":sid,"original_sha256_verified":ok_ori,"crop_sha256_verified":ok_crop,
  "crop_size_px":size,"native_reference_document_type":ext,"rights_gate":"HOLD",
  "source_media_status":"FAIL" if not (ok_ori and ok_crop) else "PASS_FILE_HASH",
  "visual_aesthetic_status":"NOT_RUN_OWNER_QC_REQUIRED","no_pixels_generated":True
 }
 if ext=="pdf" and rec.get("crop_rect_pt"):
  doc=fitz.open(orig)
  idx=int(rec["page_1based"])-1
  if idx<0 or idx>=len(doc):raise ValueError((asset,sid,"invalid pdf page"))
  page=doc[idx]
  rect=fitz.Rect(rec["crop_rect_pt"])
  pagewords=page.get_text("words")
  boundary=[]
  possible_dropped=[]
  for w in pagewords:
   x0,y0,x1,y1,txt,*_=w
   if y1>=rect.y0 and y0<=rect.y1:
    if x0<rect.x0<x1 or x0<rect.x1<x1:
     boundary.append(txt)
    if x1<=rect.x0 and rect.x0-x1<42 and len(txt)>2:
     possible_dropped.append(txt)
  text=page.get_text("text",clip=rect)
  anchor=rec.get("matched_native_phrase") or rec.get("target_native_phrase") or ""
  anchor_in_cropped=bool(anchor and anchor.casefold() in text.casefold())
  normalized=lambda x:" ".join((x or "").split())
  stale=normalized(rec.get("extracted_text"))!=normalized(text[:len(rec.get("extracted_text") or "")])
  item.update(page_1based=idx+1,rect_pdf_points=list(map(lambda x:round(x,2),rect)),
     matched_anchor_in_current_crop_text=anchor_in_cropped,old_extracted_text_metadata_stale=stale,
     truncated_word_intersections=boundary[:20],potential_left_side_omissions=possible_dropped[:12],
     crop_continuity_status="REVIEW_CLIPPED_TEXT" if boundary or possible_dropped else "NO_BOUNDARY_WORD_CROSSES",
     source_native_crop_text_snippet=text[:350])
 elif ext=="html":
  item.update(native_css_crop=rec.get("html_dom_crop_absolute_rect_css_px",rec.get("html_dom_bounds_css_px")),
              publisher_html_original_capture=orig.name,html_text_visible_claim="SOURCE_DOM_ARCHIVED_PNG_HASH_VERIFIED")
 checks.append(item)
all_assets={a["asset_id"] for a in asset_rows}
present={c["asset_id"] for c in checks if c["source_media_status"]=="PASS_FILE_HASH"}
primary_ok=sum(
  (r["asset_id"],r["working_source_ids"].split(";")[0]) in existing
  for r in asset_rows
)
clip=[c for c in checks if c.get("crop_continuity_status")=="REVIEW_CLIPPED_TEXT"]
stale=[c for c in checks if c.get("old_extracted_text_metadata_stale")]
report={
 "audit":"VIDEO005_STAGE13_NONRENDER_QC_20261015",
 "no_media_generated":True,"no_image_generation":True,"source_origins":len(sources),
 "authentic_asset_count":len(all_assets),"asset_source_pairs":len(checks),
 "primary_source_pairs_resolved":primary_ok,
 "all_source_and_png_hashes_valid":all(c["source_media_status"]=="PASS_FILE_HASH" for c in checks),
 "pdf_crop_text_boundary_review":len(clip),
 "pdf_crop_stale_metadata_count":len(stale),
 "copyright_rights_release":"HOLD_CASE_BY_CASE",
 "final_frame_visual_qc":"NOT_RUN_PER_USER_NO_GENERATION",
 "motion_render_qc":"NOT_RUN_PER_USER_NO_GENERATION",
 "stage13_source_provenance":"COMPLETE",
 "stage13_full_final_frame_release":"HOLD",
 "flagged_source_pairs":[{"asset_id":x["asset_id"],"source_id":x["source_id"],"boundary":x.get("truncated_word_intersections"),"left_near":x.get("potential_left_side_omissions")} for x in clip],
}
(R/"13_SOURCE_TEXT_ONLY_AUDIT.json").write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
(R/"13_SOURCE_CROP_READ_ONLY_QC.json").write_text(json.dumps(checks,indent=2,ensure_ascii=False)+"\n")
assert report["all_source_and_png_hashes_valid"] and primary_ok==37,report
print(json.dumps(report,ensure_ascii=False,indent=2)[:12000])
