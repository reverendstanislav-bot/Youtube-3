from __future__ import annotations
import csv, hashlib, json, os, shutil, subprocess
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw, ImageFont

SRC=Path(r'C:\Users\KK\VIDEO008_PRODUCTION\VIDEO008_SOURCE_ARCHIVE')
OUT=Path(r'C:\Users\KK\VIDEO008_PRODUCTION\VIDEO008_FINAL_VISUAL_PACK')
REPO=Path(r'C:\Users\KK\Youtube-3-video005-voice\03_VIDEOS\VIDEO_008_CLAUDE_80_7_BILLION_LOSS_IPO_FILING')
for d in ['STOCK_VIDEO','STOCK_PHOTOS','DOCUMENTS/ORIGINALS','DOCUMENTS/CROPS','GRAPHICS','GENERATED_STILLS','REMOTION_SOURCES','REFERENCE_PREVIEWS','QC']:(OUT/d).mkdir(parents=True,exist_ok=True)

def sha(p:Path):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest().upper()
def link_or_copy(src:Path,dst:Path):
 if dst.exists(): return
 try: os.link(src,dst)
 except OSError: shutil.copy2(src,dst)
def sheet(images:list[Path],out:Path,title:str,cell=(384,216),cols=5):
 rows=(len(images)+cols-1)//cols; canvas=Image.new('RGB',(cols*cell[0],60+rows*(cell[1]+42)),(10,10,10)); dr=ImageDraw.Draw(canvas); dr.text((20,18),title,fill='white')
 for i,p in enumerate(images):
  im=Image.open(p).convert('RGB'); im=ImageOps.fit(im,cell,method=Image.Resampling.LANCZOS); x=(i%cols)*cell[0]; y=60+(i//cols)*(cell[1]+42); canvas.paste(im,(x,y)); dr.text((x+10,y+cell[1]+10),p.stem[:48],fill=(220,220,220))
 canvas.save(out,quality=92)

rows=list(csv.DictReader((SRC/'STOCK_ASSET_MANIFEST.csv').open(encoding='utf-8-sig')))
photo_previews=[]; video_previews=[]; video_qc=[]
for r in rows:
 p=Path(r['local_path'].replace('VIDEO008_SOURCE_ARCHIVE',str(SRC)))
 if r['media']=='STOCK_VIDEO':
  dst=OUT/'STOCK_VIDEO'/p.name; link_or_copy(p,dst)
  prev=OUT/'REFERENCE_PREVIEWS'/f"{r['scene_id']}_MIDPOINT.jpg"
  subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-ss',str(max(0.1,float(r['duration_sec'])/2)),'-i',str(p),'-frames:v','1','-vf','scale=640:-2','-y',str(prev)],check=True)
  decode=subprocess.run(['ffmpeg','-v','error','-xerror','-i',str(p),'-f','null','NUL'],capture_output=True,text=True)
  video_qc.append({'scene_id':r['scene_id'],'file':p.name,'sha256':sha(p),'decode_status':'PASS' if decode.returncode==0 else 'FAIL','stderr':decode.stderr.strip()})
  video_previews.append(prev)
 else:
  dst=OUT/'STOCK_PHOTOS'/f"{r['scene_id']}_CROP_1920x1080.jpg"
  im=Image.open(p).convert('RGB'); crop=ImageOps.fit(im,(1920,1080),method=Image.Resampling.LANCZOS,centering=(0.5,0.5)); crop.save(dst,quality=95,subsampling=0); photo_previews.append(dst)
for p in (SRC/'03_ORIGINAL_DOCUMENTS').glob('*'):
 if p.is_file() and 'Access_Denied' not in p.name: link_or_copy(p,OUT/'DOCUMENTS/ORIGINALS'/p.name)
sheet(photo_previews,OUT/'REFERENCE_PREVIEWS/STOCK_PHOTOS_CONTACT_SHEET.jpg','VIDEO008 · 25 STOCK PHOTO CROPS')
sheet(video_previews,OUT/'REFERENCE_PREVIEWS/STOCK_VIDEO_CONTACT_SHEET.jpg','VIDEO008 · 40 STOCK VIDEO MIDPOINTS')
with (OUT/'QC/STOCK_VIDEO_DECODE_QC.csv').open('w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=['scene_id','file','sha256','decode_status','stderr']); w.writeheader(); w.writerows(video_qc)
(OUT/'GENERATED_STILLS/README_HOLD.txt').write_text('Five optional replacement stills were NOT generated. GPT Image 2 per-image credit cost could not be confirmed at or below 0.5 credit; spend: 0 credits. Existing 110-scene assignments remain in force.\n',encoding='utf-8')
rem=REPO/'13_VISUAL_PRODUCTION/remotion'; dst=OUT/'REMOTION_SOURCES'
for p in rem.rglob('*'):
 if 'node_modules' in p.parts or p.name=='rendered': continue
 if p.is_file():
  rel=p.relative_to(rem); (dst/rel).parent.mkdir(parents=True,exist_ok=True); shutil.copy2(p,dst/rel)
summary={'stock_video':sum(r['media']=='STOCK_VIDEO' for r in rows),'stock_photos':sum(r['media']=='STOCK_PHOTO' for r in rows),'video_decode_pass':sum(q['decode_status']=='PASS' for q in video_qc),'generated_stills':0,'generated_credits':0}
(OUT/'QC/PREP_SUMMARY.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary,indent=2))
