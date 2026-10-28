from __future__ import annotations
import csv, hashlib, json, shutil, zipfile
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw

SRC=Path(r'C:\Users\KK\VIDEO008_PRODUCTION\VIDEO008_SOURCE_ARCHIVE')
OUT=Path(r'C:\Users\KK\VIDEO008_PRODUCTION\VIDEO008_FINAL_VISUAL_PACK')
ROOT=Path(r'C:\Users\KK\VIDEO008_PRODUCTION')
REPO=Path(r'C:\Users\KK\Youtube-3-video005-voice\03_VIDEOS\VIDEO_008_CLAUDE_80_7_BILLION_LOSS_IPO_FILING')
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest().upper()
def sheet(paths,out,title,cols=4,cell=(480,270)):
 rows=(len(paths)+cols-1)//cols; im=Image.new('RGB',(cols*cell[0],60+rows*(cell[1]+38)),(8,8,8)); d=ImageDraw.Draw(im); d.text((20,18),title,fill='white')
 for i,p in enumerate(paths):
  x=i%cols*cell[0]; y=60+i//cols*(cell[1]+38); src=Image.open(p).convert('RGB'); src=ImageOps.fit(src,cell,Image.Resampling.LANCZOS); im.paste(src,(x,y)); d.text((x+8,y+cell[1]+8),p.stem[:55],fill=(220,220,220))
 im.save(out,quality=92)

# Remove browser-generated denial pages; they are not source evidence.
for base in [SRC/'03_ORIGINAL_DOCUMENTS',OUT/'DOCUMENTS/ORIGINALS']:
 for name in ['SRC016_Broadcom_63B_financing_official_release.pdf','SRC018_Broadcom_63B_financing_infographic.pdf']:
  p=base/name
  if p.exists(): p.unlink()

graphics=sorted((OUT/'GRAPHICS').glob('*.png')); crops=sorted((OUT/'DOCUMENTS/CROPS').glob('SC*.png'))
sheet(graphics,OUT/'REFERENCE_PREVIEWS/REMOTION_GRAPHICS_CONTACT_SHEET.jpg','VIDEO008 · 21 REMOTION GRAPHICS')
sheet(crops,OUT/'REFERENCE_PREVIEWS/DOCUMENT_CROPS_CONTACT_SHEET.jpg','VIDEO008 · AUTHENTIC DOCUMENT CROPS')

stock=list(csv.DictReader((SRC/'STOCK_ASSET_MANIFEST.csv').open(encoding='utf-8-sig')))
doc=list(csv.DictReader((OUT/'DOCUMENTS/CROPS/DOCUMENT_CROP_MANIFEST.csv').open(encoding='utf-8-sig')))
assets=[]
for r in stock:
 final=f"STOCK_VIDEO/{Path(r['local_path']).name}" if r['media']=='STOCK_VIDEO' else f"STOCK_PHOTOS/{r['scene_id']}_CROP_1920x1080.jpg"
 p=OUT/final
 assets.append({'scene_id':r['scene_id'],'asset_class':r['media'],'status':'TECH_PASS_RIGHTS_CONTEXT_REVIEW','final_path':final,'source_url':r['landing_page_url'],'license_or_basis':r['license'],'sha256':sha(p),'notes':r['brief']})
for r in doc:
 assets.append({'scene_id':r['scene_id'],'asset_class':'AUTHENTIC_EVIDENCE','status':r['status'],'final_path':r['crop_file'],'source_url':'See SOURCE_INDEX.csv and source_file','license_or_basis':'Primary-source documentary display; attribution and Stage16 rights review required','sha256':r['sha256'],'notes':r['notes']})
for p in graphics:
 assets.append({'scene_id':p.name[:5],'asset_class':'EDITOR_GRAPHIC','status':'REMOTION_RENDER_TECH_PASS','final_path':f'GRAPHICS/{p.name}','source_url':'','license_or_basis':'Original project graphic; source values traced in 12_DOCUMENT_GRAPHIC_TASKS.csv','sha256':sha(p),'notes':'1920x1080; key content above lower 20% caption-safe area.'})
assets.sort(key=lambda r:int(r['scene_id'][2:]))
cols=['scene_id','asset_class','status','final_path','source_url','license_or_basis','sha256','notes']
with (OUT/'ASSET_MANIFEST.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(assets)
with (OUT/'GRAPHICS/GRAPHICS_MANIFEST.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.writer(f);w.writerow(['scene_id','file','sha256','width','height','status'])
 for p in graphics:
  with Image.open(p) as im:w.writerow([p.name[:5],p.name,sha(p),im.width,im.height,'REMOTION_RENDER_TECH_PASS'])
shutil.copy2(SRC/'STOCK_ASSET_MANIFEST.csv',OUT/'QC/STOCK_ASSET_SOURCE_MANIFEST.csv')
shutil.copy2(SRC/'DOCUMENT_SOURCE_MANIFEST.csv',OUT/'QC/DOCUMENT_SOURCE_MANIFEST.csv')
shutil.copy2(SRC/'06_LICENSES/PEXELS_LICENSE_REFERENCE.txt',OUT/'QC/PEXELS_LICENSE_REFERENCE.txt')
summary={
 'planned_scenes':110,'asset_manifest_rows':len(assets),'stock_videos':sum(a['asset_class']=='STOCK_VIDEO' for a in assets),
 'stock_photos':sum(a['asset_class']=='STOCK_PHOTO' for a in assets),'document_tasks':sum(a['asset_class']=='AUTHENTIC_EVIDENCE' for a in assets),
 'document_full_pass':sum(a['asset_class']=='AUTHENTIC_EVIDENCE' and a['status']=='AUTHENTIC_SOURCE_CROP_TECH_PASS' for a in assets),
 'document_partial_hold':sum(a['asset_class']=='AUTHENTIC_EVIDENCE' and a['status']=='PARTIAL_PASS_SECOND_SOURCE_HOLD' for a in assets),
 'document_full_hold':sum(a['asset_class']=='AUTHENTIC_EVIDENCE' and a['status'].startswith('HOLD') for a in assets),
 'remotion_graphics':len(graphics),'optional_ai_stills_generated':0,'credits_spent':0,
 'formal_pipeline_stage':'08 (unchanged; narration/audio synchronization absent)'
}
(OUT/'QC/FINAL_QC_SUMMARY.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
(OUT/'README.md').write_text(f"""# VIDEO008 final visual pack

This is an unsynchronized visual asset package for the current 110-scene plan. It does not advance the formal pipeline beyond Stage 08 and is not a finished edit.

- 40 stock videos, full-decode checked
- 25 stock-photo 16:9 crops
- 24 authentic-evidence tasks: {summary['document_full_pass']} pass, {summary['document_partial_hold']} partial/HOLD, {summary['document_full_hold']} HOLD
- 21 Remotion graphics at 1920x1080
- 0 optional AI stills; 0 credits spent

Use `ASSET_MANIFEST.csv` as the package index. Rights/context approval remains a Stage16 gate.
""",encoding='utf-8')
print(json.dumps(summary,indent=2))
