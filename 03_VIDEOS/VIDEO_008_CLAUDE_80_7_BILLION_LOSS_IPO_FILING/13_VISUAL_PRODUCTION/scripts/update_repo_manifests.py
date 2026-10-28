from pathlib import Path
import csv, shutil

repo=Path(r'C:\Users\KK\Youtube-3-video005-voice\03_VIDEOS\VIDEO_008_CLAUDE_80_7_BILLION_LOSS_IPO_FILING')
src=Path(r'C:\Users\KK\VIDEO008_PRODUCTION\VIDEO008_SOURCE_ARCHIVE')
pack=Path(r'C:\Users\KK\VIDEO008_PRODUCTION\VIDEO008_FINAL_VISUAL_PACK')
prod=repo/'13_VISUAL_PRODUCTION'; details=prod/'manifests'; previews=prod/'previews'; qc=prod/'qc'
for d in [details,previews,qc]:d.mkdir(parents=True,exist_ok=True)
release='https://github.com/reverendstanislav-bot/Youtube-3/releases/download/video008-visual-assets-20261027/VIDEO008_FINAL_VISUAL_PACK.zip'

stock=list(csv.DictReader((src/'STOCK_ASSET_MANIFEST.csv').open(encoding='utf-8-sig')))
stock_by={r['scene_id']:r for r in stock}
docs=list(csv.DictReader((pack/'DOCUMENTS/CROPS/DOCUMENT_CROP_MANIFEST.csv').open(encoding='utf-8-sig')))
doc_by={r['scene_id']:r for r in docs}
gfx=list(csv.DictReader((pack/'GRAPHICS/GRAPHICS_MANIFEST.csv').open(encoding='utf-8-sig')))
gfx_by={r['scene_id']:r for r in gfx}

rows=list(csv.DictReader((repo/'ASSET_MANIFEST.csv').open(encoding='utf-8-sig')))
for r in rows:
 sid=r['scene_id']
 if sid in stock_by:
  s=stock_by[sid]; r.update(provenance_class='PEXELS_LICENSED_STOCK_ORIGINAL',generator_or_origin=s['landing_page_url'],version='MATERIALIZED_2026-10-27',status='TECH_PASS_RIGHTS_CONTEXT_REVIEW',storage_uri=f"{release}#/{'STOCK_VIDEO' if s['media']=='STOCK_VIDEO' else 'STOCK_PHOTOS'}",sha256=s['sha256'],rights_or_usage_note='Pexels License verified; attribution not required; no endorsement; third-party/context rights and Stage16 review remain.',notes=s['brief'])
 elif sid in doc_by:
  d=doc_by[sid]; r.update(provenance_class='AUTHENTIC_PRIMARY_SOURCE_CROP',generator_or_origin=d['source_file'],version='MATERIALIZED_2026-10-27',status=d['status'],storage_uri=f"{release}#/{d['crop_file']}" if d['crop_file'] else '',sha256=d['sha256'],rights_or_usage_note='Primary-source documentary display; context and attribution required; final Stage16 review remains.',notes=d['notes'])
 elif sid in gfx_by:
  g=gfx_by[sid]; r.update(provenance_class='ORIGINAL_REMOTION_EDITOR_GRAPHIC',generator_or_origin='13_VISUAL_PRODUCTION/remotion',version='MATERIALIZED_2026-10-27',status=g['status'],storage_uri=f"{release}#/GRAPHICS/{g['file']}",sha256=g['sha256'],rights_or_usage_note='Original editable graphic; factual values traced to 12_DOCUMENT_GRAPHIC_TASKS.csv.',notes='1920x1080; bottom 20 percent kept caption-safe.')
with (repo/'ASSET_MANIFEST.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)

req=list(csv.DictReader((repo/'12_STOCK_SHOT_REQUIREMENTS.csv').open(encoding='utf-8-sig')))
for r in req:
 s=stock_by[r['scene_id']]; r['candidate_id']=s['candidate_id'];r['landing_page_or_search']=s['landing_page_url'];r['rights_status']='PEXELS_LICENSE_VERIFIED_CONTEXT_REVIEW_PENDING';r['asset_status']='DOWNLOADED_FULL_TECH_PASS'
with (repo/'12_STOCK_SHOT_REQUIREMENTS.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=req[0].keys());w.writeheader();w.writerows(req)

tasks=list(csv.DictReader((repo/'12_DOCUMENT_GRAPHIC_TASKS.csv').open(encoding='utf-8-sig')))
for r in tasks:
 sid=r['scene_id']; r['status']=doc_by[sid]['status'] if sid in doc_by else gfx_by[sid]['status']
with (repo/'12_DOCUMENT_GRAPHIC_TASKS.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=tasks[0].keys());w.writeheader();w.writerows(tasks)

copies=[
 (src/'STOCK_ASSET_MANIFEST.csv',details/'13_ACQUIRED_STOCK_MANIFEST.csv'),
 (src/'DOCUMENT_SOURCE_MANIFEST.csv',details/'13_DOCUMENT_SOURCE_MANIFEST.csv'),
 (pack/'DOCUMENTS/CROPS/DOCUMENT_CROP_MANIFEST.csv',details/'13_DOCUMENT_CROP_MANIFEST.csv'),
 (pack/'GRAPHICS/GRAPHICS_MANIFEST.csv',details/'13_GRAPHICS_MANIFEST.csv'),
 (pack/'ASSET_MANIFEST.csv',details/'13_FINAL_PACK_ASSET_MANIFEST.csv'),
 (pack/'QC/STOCK_VIDEO_DECODE_QC.csv',qc/'13_STOCK_VIDEO_DECODE_QC.csv'),
 (pack/'QC/FINAL_QC_SUMMARY.json',qc/'13_FINAL_QC_SUMMARY.json')]
for a,b in copies:shutil.copy2(a,b)
for p in (pack/'REFERENCE_PREVIEWS').glob('*CONTACT_SHEET.jpg'):shutil.copy2(p,previews/p.name)
print(f'updated {len(rows)} scene rows, {len(req)} stock requirements, {len(tasks)} proof/graphic tasks')
