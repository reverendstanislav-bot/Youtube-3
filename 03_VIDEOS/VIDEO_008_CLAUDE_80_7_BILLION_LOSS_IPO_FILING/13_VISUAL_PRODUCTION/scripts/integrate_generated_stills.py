from pathlib import Path
import csv, hashlib, json, shutil
from PIL import Image, ImageOps, ImageDraw

gen=Path(r'C:\Users\KK\.codex\generated_images\01a13a62-cc01-7a63-b515-ad6b5879f6e8')
pack=Path(r'C:\Users\KK\VIDEO008_PRODUCTION\VIDEO008_FINAL_VISUAL_PACK')
repo=Path(r'C:\Users\KK\Youtube-3-video005-voice\03_VIDEOS\VIDEO_008_CLAUDE_80_7_BILLION_LOSS_IPO_FILING')
out=pack/'GENERATED_STILLS'; out.mkdir(parents=True,exist_ok=True)
mapping={
 'SC023':gen/'exec-71f4d0d2-8969-4fea-96df-fd36acfb27ed.png',
 'SC047':gen/'exec-c3bfdfd9-8953-476f-a0a5-37d75722e26a.png',
 'SC079':gen/'exec-5c617287-718e-43c7-b2a5-db3d85cad1ac.png',
 'SC096':gen/'exec-aafa9329-cf0d-4f42-9ca4-bfa4d6c25bb6.png',
 'SC110':gen/'exec-c4e01573-a24c-46b8-afed-09924b2a70ce.png'}
labels={'SC023':'unused server capacity concept','SC047':'equipment and folders still life','SC079':'empty conditional-governance boardroom','SC096':'generic power and data-center infrastructure','SC110':'capacity-ahead-of-demand concluding server aisle'}
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest().upper()
rows=[]; previews=[]
for scene,src in mapping.items():
 if not src.exists(): raise FileNotFoundError(src)
 dst=out/f'{scene}_GENERATED_REPLACEMENT_1920x1080.png'
 with Image.open(src) as im:
  final=ImageOps.fit(im.convert('RGB'),(1920,1080),method=Image.Resampling.LANCZOS,centering=(0.5,0.5)); final.save(dst,optimize=True)
 previews.append(dst); rows.append({'scene_id':scene,'file':f'GENERATED_STILLS/{dst.name}','sha256':sha(dst),'width':1920,'height':1080,'status':'GENERATED_STILL_VISUAL_QC_PASS','role':labels[scene],'provenance':'OpenAI built-in image generation; conceptual illustration; not evidence','cost_reporting':'Built-in tool did not expose per-image credits'})
cols=list(rows[0]);
with (out/'GENERATED_STILLS_MANIFEST.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(rows)

sheet=Image.new('RGB',(1920,60+2*580),(8,8,8)); d=ImageDraw.Draw(sheet); d.text((20,18),'VIDEO008 · 5 GENERATED REPLACEMENT STILLS',fill='white')
for i,p in enumerate(previews):
 with Image.open(p) as im: thumb=ImageOps.fit(im.convert('RGB'),(640,360),Image.Resampling.LANCZOS)
 x=(i%3)*640; y=60+(i//3)*580; sheet.paste(thumb,(x,y)); d.text((x+12,y+372),p.stem,fill=(230,230,230))
sheet.save(pack/'REFERENCE_PREVIEWS/GENERATED_STILLS_CONTACT_SHEET.jpg',quality=92)

def update_manifest(path,pack_schema=False):
 data=list(csv.DictReader(path.open(encoding='utf-8-sig'))); by={r['scene_id']:r for r in rows}
 for r in data:
  if r['scene_id'] not in by: continue
  g=by[r['scene_id']]
  if pack_schema:
   r.update(asset_class='GENERATED_STILL',status=g['status'],final_path=g['file'],source_url='',license_or_basis=g['provenance'],sha256=g['sha256'],notes=g['role'])
  else:
   r.update(asset_type='GENERATED_STILL',provenance_class='OPENAI_GENERATED_CONCEPTUAL_ILLUSTRATION',source_id='',generator_or_origin='OpenAI built-in image generation',version='GENERATED_REPLACEMENT_2026-10-28',status=g['status'],storage_uri=f"https://github.com/reverendstanislav-bot/Youtube-3/releases/download/video008-visual-assets-20261027/VIDEO008_FINAL_VISUAL_PACK.zip#/{g['file']}",sha256=g['sha256'],rights_or_usage_note='Conceptual illustration only; not evidence or reconstruction; final visual/context review required.',notes=g['role'])
 with path.open('w',newline='',encoding='utf-8-sig') as f:
  w=csv.DictWriter(f,fieldnames=data[0].keys());w.writeheader();w.writerows(data)
update_manifest(pack/'ASSET_MANIFEST.csv',True)
update_manifest(repo/'ASSET_MANIFEST.csv',False)

req=list(csv.DictReader((repo/'12_STOCK_SHOT_REQUIREMENTS.csv').open(encoding='utf-8-sig')))
for r in req:
 if r['scene_id'] in mapping:
  r['rights_status']='GENERATED_CONCEPTUAL_ILLUSTRATION_FINAL_REVIEW_PENDING'; r['asset_status']='REPLACED_BY_GENERATED_STILL_STOCK_FALLBACK_RETAINED'
with (repo/'12_STOCK_SHOT_REQUIREMENTS.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=req[0].keys());w.writeheader();w.writerows(req)

shutil.copy2(out/'GENERATED_STILLS_MANIFEST.csv',repo/'13_VISUAL_PRODUCTION/manifests/13_GENERATED_STILLS_MANIFEST.csv')
shutil.copy2(pack/'REFERENCE_PREVIEWS/GENERATED_STILLS_CONTACT_SHEET.jpg',repo/'13_VISUAL_PRODUCTION/previews/GENERATED_STILLS_CONTACT_SHEET.jpg')
shutil.copy2(pack/'ASSET_MANIFEST.csv',repo/'13_VISUAL_PRODUCTION/manifests/13_FINAL_PACK_ASSET_MANIFEST.csv')

summary_path=pack/'QC/FINAL_QC_SUMMARY.json'; summary=json.loads(summary_path.read_text(encoding='utf-8'))
summary.update(optional_ai_stills_generated=5,active_stock_photos=20,stock_photo_fallbacks_retained=25,generation_cost_reporting='Built-in tool did not expose per-image credits')
summary_path.write_text(json.dumps(summary,indent=2),encoding='utf-8')
shutil.copy2(summary_path,repo/'13_VISUAL_PRODUCTION/qc/13_FINAL_QC_SUMMARY.json')
print(json.dumps({'generated':len(rows),'files':[r['file'] for r in rows]},indent=2))
