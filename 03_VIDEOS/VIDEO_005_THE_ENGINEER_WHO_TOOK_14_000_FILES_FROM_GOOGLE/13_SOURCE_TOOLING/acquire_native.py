#!/usr/bin/env python3
"""VIDEO005: source-native acquisition/crop only, no AI and no fake legal copy."""
from pathlib import Path
import csv,json,hashlib,re,time,sys,io,datetime
import requests,fitz
from PIL import Image,ImageDraw,ImageFont
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'13_SOURCE_REAL_ACQUISITION'; SRC=OUT/'original_sources'; CROPS=OUT/'native_crops'; FRAMES=OUT/'control_frames'
for p in [SRC,CROPS,FRAMES]:p.mkdir(parents=True,exist_ok=True)
CSV=ROOT/'13_SOURCE_CROP_ACQUISITION_LEDGER.csv'
LIST=list(csv.DictReader(CSV.open(encoding='utf8')))
assert len(LIST)==37 and len({x['asset_id'] for x in LIST})==37
DIRECT={
'S001':'https://cases.justia.com/federal/district-courts/california/candce/3:2017cv00939/308136/1/0.pdf',
'S003':'https://cases.justia.com/federal/district-courts/california/candce/3:2017cv00939/308136/433/0.pdf',
'S004':'https://cases.justia.com/federal/district-courts/california/candce/3:2017cv00939/308136/566/0.pdf',
'S005':'https://business.cch.com/ipld/WaymoUberTechnologiesDiismissal20180209.pdf',
'S007':'https://cases.justia.com/delaware/court-of-chancery/2019-ca-2017-0888-sg.pdf',
'S008':'https://cases.justia.com/delaware/supreme-court/2020-181-2019.pdf',
'S009':'https://www.uber.com/en-IE/newsroom/uber-waymo-settlement/',
'S010':'https://www.justice.gov/usao-ndca/pr/former-uber-self-driving-car-executive-signs-agreement-plead-guilty-theft-trade-secrets',
'S011':'https://www.justice.gov/usao-ndca/pr/former-uber-executive-sentenced-18-months-jail-trade-secret-theft-google',
'S012':'https://www.justice.gov/pardon/pardons-granted-president-donald-j-trump-2017-2021',
'S031':'https://cases.justia.com/federal/district-courts/california/candce/3:2017cv00939/308136/2585/0.pdf',
'S032':'https://www.govinfo.gov/content/pkg/USCOURTS-canb-3_20-bk-30242/pdf/USCOURTS-canb-3_20-bk-30242-0.pdf',
'S033':'https://www.govinfo.gov/content/pkg/USCOURTS-cand-4_22-cv-02781/pdf/USCOURTS-cand-4_22-cv-02781-0.pdf',
}
FALLBACK={'S007':'https://law.justia.com/cases/delaware/court-of-chancery/2019/ca-2017-0888-sg.html',
'S008':'https://law.justia.com/cases/delaware/supreme-court/2020/181-2019.html',
'S031':'https://docs.justia.com/cases/federal/district-courts/california/candce/3:2017cv00939/308136/2585'}
PREFERRED={
'S007':['$100,000','up-front cash','milestones','680 million'],
'S008':['$100,000','Stroz','Otto'],
'S010':['December 11, 2015','14,000','weekly','33'],
'S011':['one count','33 counts','18 months','pleaded guilty'],
'S012':['Anthony Scott Levandowski'],
'S009':['regret','trade secrets'],
'S031':['may, but need not','discs','misconduct']
}
SECONDARY={
'V005-VP016':[('S010','December 11, 2015')],
'V005-VP026':[('S008','$100,000')],
'V005-VP039':[('S008','Stroz')],
'V005-VP081':[('S010','33')],
'V005-VP083':[('S012','Anthony Scott Levandowski')],
'V005-VP091':[('S032','Settlement Agreement')],
'V005-VP094':[('S032','Settlement Agreement')],
'V005-VP109':[('S032','179,047,998.64'),('S033','May 20, 2022')],
}
def digest(data):return hashlib.sha256(data).hexdigest()
def sha_file(p):return digest(p.read_bytes())
def save_json(p,ob):p.write_text(json.dumps(ob,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
def download(session,sid):
 urls=[DIRECT[sid]]+([FALLBACK[sid]] if sid in FALLBACK else [])
 attempts=[]
 for u in urls:
  try:
   resp=session.get(u,timeout=40,allow_redirects=True)
   data=resp.content
   typ='pdf' if data[:5]==b'%PDF-' else 'html' if b'<html' in data[:200000].lower() or b'<!doctype html' in data[:200000].lower() else 'other'
   attempts.append(dict(url=u,status=resp.status_code,size=len(data),type=typ))
   if resp.status_code!=200 or len(data)<500 or typ=='other':continue
   name=SRC/(sid+'.'+typ)
   name.write_bytes(data)
   return dict(source_id=sid,status='SAVED_ORIGINAL_BINARY_REQUIRES_RIGHTS_QC',type=typ,url=u,resolved_url=resp.url,
               path=str(name.relative_to(ROOT)),sha256=digest(data),byte_size=len(data),attempts=attempts)
  except Exception as e:attempts.append(dict(url=u,error=str(e)[:180]))
 return dict(source_id=sid,status='HOLD_DOWNLOAD_FAILED',attempts=attempts)
def save_pdf_crop(sid,original,asset,phrase,hint):
 p=ROOT/original['path'];doc=fitz.open(p);n=len(doc)
 indexes=([hint-1] if hint and 1<=hint<=n else [])+[i for i in range(n) if i!=hint-1]
 candidates=[phrase]+[z for z in PREFERRED.get(sid,[]) if z.lower()!=phrase.lower()]
 for anchor in candidates:
  for idx in indexes:
   page=doc[idx];rects=page.search_for(anchor)
   if not rects:continue
   # Expand to near-full paragraph width and evidence adjacency; exact native pt rect is retained.
   r=rects[0]; full=page.rect
   maxWidth=min(full.width-24, min(470,full.width*.87))
   mid=(r.x0+r.x1)/2
   x0=max(full.x0+12,mid-maxWidth/2)
   x1=min(full.x1-12,x0+maxWidth)
   x0=max(full.x0+12,x1-maxWidth)
   y0=max(full.y0+20,r.y0-75)
   y1=min(full.y1-20,r.y1+110)
   clip=fitz.Rect(x0,y0,x1,y1)
   data=page.get_pixmap(matrix=fitz.Matrix(3,3),clip=clip,alpha=False).tobytes('png')
   fp=CROPS/(asset+'__'+sid+'.png');fp.write_bytes(data)
   native_text=page.get_text('text',clip=clip)
   # proof full original native page, useful human context; not proposed as final crop
   context=CROPS/(asset+'__'+sid+'__fullpage_QC.png')
   context.write_bytes(page.get_pixmap(matrix=fitz.Matrix(1.2,1.2),alpha=False).tobytes('png'))
   return dict(status='NATIVE_PDF_CROP_EXTRACTED_PENDING_LEGAL_VISUAL_RIGHTS_QC',
      asset_id=asset,source_id=sid,original_sha256=original['sha256'],source_url=original['url'],
      source_type='pdf',crop_file=str(fp.relative_to(ROOT)),crop_sha256=digest(data),
      page_1based=idx+1,total_pages=n,page_bounds_pt=[round(full.x0,2),round(full.y0,2),round(full.x1,2),round(full.y1,2)],
      crop_rect_pt=[round(x0,2),round(y0,2),round(x1,2),round(y1,2)],target_native_phrase=phrase,
      matched_native_phrase=anchor,substitution_used=anchor!=phrase,extracted_text=native_text[:1600],
      qc_fullpage_file=str(context.relative_to(ROOT)),font_preserved_as_source_pixels=True,rights_status='HOLD')
 return dict(status='HOLD_NO_MATCHING_PDF_PHRASE',source_id=sid,asset_id=asset,target_native_phrase=phrase,page_hint=hint,
             doc_pages=n,original_sha256=original['sha256'],rights_status='HOLD')
def save_html_crop(page,sid,original,asset,phrase):
 u=original['url']
 try:
  page.goto(u,wait_until='domcontentloaded',timeout=40000)
  page.wait_for_timeout(1300)
  phrases=[phrase]+[z for z in PREFERRED.get(sid,[]) if z.lower()!=phrase.lower()]
  box=None;anchor=None
  for candidate in phrases:
   # select ORIGINAL publisher-rendered DOM text and take a browser screenshot of the element.
   for selector in ['article p','main p','p','article','main']:
    nodes=page.locator(selector).filter(has_text=re.compile(re.escape(candidate),re.I))
    try:ct=nodes.count()
    except Exception:ct=0
    if ct:
     loc=nodes.first
     b=loc.bounding_box()
     if b and b['width']>70 and b['height']>14:
      box=b;anchor=candidate;break
   if box:break
  if not box:
   return dict(status='HOLD_ANCHOR_NOT_VISIBLE_ON_ORIGINAL_PAGE',source_id=sid,asset_id=asset,phrase=phrase,url=u,rights_status='HOLD')
  # screenshot actual rendering; adjust scroll then capture an exact screenshot clipping to source DOM.
  page.evaluate('window.scrollTo(0,0)')
  target=page.locator('p').filter(has_text=re.compile(re.escape(anchor),re.I)).first
  if target.count()==0:target=page.locator('article').first
  target.scroll_into_view_if_needed(timeout=10000)
  dest=CROPS/(asset+'__'+sid+'.png')
  target.screenshot(path=str(dest),timeout=15000)
  if dest.stat().st_size<1000:raise RuntimeError('screenshot unusually small')
  pgtitle=page.title()
  return dict(status='NATIVE_HTML_SCREENSHOT_EXTRACTED_PENDING_LEGAL_VISUAL_RIGHTS_QC',
     asset_id=asset,source_id=sid,original_sha256=original['sha256'],source_url=u,captured_url=page.url,
     source_type='html',crop_file=str(dest.relative_to(ROOT)),crop_sha256=sha_file(dest),
     dom_locator='p filtered by case-insensitive native source text',
     target_native_phrase=phrase,matched_native_phrase=anchor,substitution_used=anchor!=phrase,
     capture_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
     html_dom_bounds_css_px={k:round(v,2) for k,v in box.items()},publisher_title=pgtitle,rights_status='HOLD')
 except Exception as e:
  return dict(status='HOLD_HTML_BROWSER_SCREENSHOT_ERROR',source_id=sid,asset_id=asset,error=str(e)[:300],rights_status='HOLD')
def font(sz,bold=False):
 p='/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-'+('Bold' if bold else '')+'.ttf'
 try:return ImageFont.truetype(p,sz)
 except:return ImageFont.load_default()
def make_controls(extracted):
 by={v['asset_id']+'__'+v['source_id']:v for v in extracted if v['status'].startswith('NATIVE_')}
 controls=[]
 for canon,asset,refs in [('AUTH-01','V005-VP101',['S032']),('AUTH-02','V005-VP026',['S007']),('AUTH-03','V005-VP109',['S005','S032','S033'])]:
  if not all(asset+'__'+s in by for s in refs):
   controls.append(dict(canon=canon,asset_id=asset,status='HOLD_MISSING_REQUIRED_SOURCE_CROP',missing=[s for s in refs if asset+'__'+s not in by]))
   continue
  image=Image.new('RGB',(1920,1080),(14,17,19));d=ImageDraw.Draw(image)
  # physical editorial background only; ALL legal evidence pixels are composited directly from original PDF/HTML crop.
  d.rectangle((0,0,1919,1080),outline=(40,45,47),width=7)
  if canon=='AUTH-01':
   d.text((110,130),'NOT A FINAL',font=font(92,True),fill=(240,233,222))
   d.text((110,230),'TAX BILL',font=font(92,True),fill=(240,233,222))
   placements=[(refs[0],980,140,820,665)]
  elif canon=='AUTH-02':
   d.text((108,112),'VALUE  /  CASH',font=font(91,True),fill=(240,233,222))
   d.text((115,270),'UP TO $680M',font=font(76,True),fill=(215,209,196))
   d.text((115,395),'$100K INITIAL',font=font(61,True),fill=(230,226,212))
   placements=[(refs[0],1050,200,760,580)]
  else:
   d.text((100,100),'FOUR SEPARATE EVENTS',font=font(76,True),fill=(240,233,222))
   for xx,yr in zip([105,545,995,1440],['2018','2020','2022','2025']):
    d.text((xx,300),yr,font=font(60,True),fill=(226,220,208))
   placements=list(zip(refs,[112,675,1240],[440]*3,[520]*3,[340]*3))
  for sid,x,y,w,h in placements:
   p=ROOT/by[asset+'__'+sid]['crop_file']
   orig=Image.open(p).convert('RGB');orig.thumbnail((w,h),Image.Resampling.LANCZOS)
   xx=x+(w-orig.width)//2; yy=y+(h-orig.height)//2
   d.rectangle((xx-8,yy-8,xx+orig.width+8,yy+orig.height+8),fill=(59,59,56))
   image.paste(orig,(xx,yy))
   d.text((xx,yy+orig.height+18),sid+' | ORIGINAL COURT SOURCE',font=font(19),fill=(205,202,193))
  # 20% lower subtitle safe, no important content below y=864
  p=FRAMES/(canon+'__CONTROL_SOURCE_NATIVE_QC_PENDING.png');image.save(p,optimize=True)
  controls.append(dict(canon=canon,asset_id=asset,status='COMPOSITED_FROM_ORIGINAL_PIXELS_VISUAL_LEGAL_RIGHTS_QC_PENDING',
                       path=str(p.relative_to(ROOT)),sha256=sha_file(p),sources=refs))
 return controls
def run():
 ss=requests.Session();ss.headers.update({'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/130.0.0.0 Safari/537.36','Accept':'application/pdf,text/html,*/*'})
 needed=sorted({s for a in LIST for s in a['working_source_ids'].split(';')})
 source={sid:download(ss,sid) for sid in needed}
 save_json(OUT/'SOURCE_DOWNLOAD_LEDGER.json',list(source.values()))
 extracted=[]
 try:
  with sync_playwright() as pw:
   browser=pw.chromium.launch(headless=True,args=['--no-sandbox'])
   page=browser.new_page(viewport={'width':1920,'height':1080},device_scale_factor=1)
   for a in LIST:
    asset=a['asset_id']; primary=a['working_source_ids'].split(';')[0]
    plans=[(primary,a['exact_anchor_to_verify'])]+SECONDARY.get(asset,[])
    for sid,phrase in plans:
     s=source.get(sid)
     if not s or s['status'].startswith('HOLD'):
      extracted.append(dict(asset_id=asset,source_id=sid,status='HOLD_SOURCE_BINARY_UNAVAILABLE',rights_status='HOLD'))
      continue
     try:
      if s['type']=='pdf':
       hint=int(a['source_document_page_hint_1based']) if sid==primary and a['source_document_page_hint_1based'].isdigit() else 0
       r=save_pdf_crop(sid,s,asset,phrase,hint)
      else:r=save_html_crop(page,sid,s,asset,phrase)
      extracted.append(r)
     except Exception as e:
      extracted.append(dict(asset_id=asset,source_id=sid,status='HOLD_EXTRACTION_EXCEPTION',error=str(e)[:300],rights_status='HOLD'))
   browser.close()
 except Exception as e:
  save_json(OUT/'BROWSER_BOOT_ERROR.json',{'error':str(e)})
  # Try pdf crops even when Chromium fails.
  for a in LIST:
   asset=a['asset_id'];sid=a['working_source_ids'].split(';')[0];s=source.get(sid)
   if s and s.get('type')=='pdf' and not any(x['asset_id']==asset for x in extracted):
    hint=int(a['source_document_page_hint_1based']) if a['source_document_page_hint_1based'].isdigit() else 0
    extracted.append(save_pdf_crop(sid,s,asset,a['exact_anchor_to_verify'],hint))
 save_json(OUT/'REAL_CROP_QC_LEDGER.json',extracted)
 controls=make_controls(extracted)
 save_json(OUT/'THREE_CONTROL_FRAMES_QC.json',controls)
 summary={'date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'source_total':len(needed),'original_sources_acquired':sum(x['status'].startswith('SAVED_') for x in source.values()),
 'main_crop_total':37,'main_crops_extracted':sum(any(x['asset_id']==a['asset_id'] and x['source_id']==a['working_source_ids'].split(';')[0] and x['status'].startswith('NATIVE_') for x in extracted) for a in LIST),
 'all_crop_files':sum(x['status'].startswith('NATIVE_') for x in extracted),
 'control_frames_created':sum(x['status'].startswith('COMPOSITED_') for x in controls),
 'render_or_rights_auto_pass':0,
 'stage13_status':'HOLD_UNTIL_VISUAL_LEGAL_RIGHTS_QC' }
 save_json(OUT/'SUMMARY.json',summary)
 print(json.dumps(summary,indent=2))
if __name__=='__main__':run()
