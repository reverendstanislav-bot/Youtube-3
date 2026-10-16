#!/usr/bin/env python3
"""Acquire 3 unaltered licensed Commons source photos. NO GENERATED MEDIA."""
from pathlib import Path
import requests,hashlib,json,csv,datetime,io,re,time
from PIL import Image
root=Path(__file__).resolve().parents[1]
dest=root/'13_CONTEXT_ORIGINALS'
dest.mkdir(exist_ok=True)
entries=[
{'id':'V005-VP009','title':'File:Mapping van tomtom with five lidars.jpg','license':'Public domain','creator':'Mike1024','date':'2012-06-06','shot':'ARCHIVAL SENSOR TESTING CONTEXT — TomTom mapping van, 2012, NOT GOOGLE / WAYMO'},
{'id':'V005-VP018','title':'File:Autonomous truck cab on display (44825419221).jpg','license':'CC BY 2.0','creator':'Oregon Department of Transportation','date':'2018-08-14','shot':'ARCHIVAL TRUCK-TECHNOLOGY CONTEXT — 2018 publicly displayed cab, NOT OTTO 2016'},
{'id':'V005-VP042','title':'File:Ford Autonomous Test Vehicle.jpg','license':'CC BY 2.0','creator':'Steve Jurvetson','date':'2015-11-08','shot':'ARCHIVAL AUTONOMOUS TEST VEHICLE — Ford 2015, NOT UBER 2016'},
]
session=requests.Session()
session.headers.update({'User-Agent':'Youtube3-DocumentarySourceArchiver/1.0 (attribution+provenance; noncommercial sourcing) Python requests','Accept':'application/json,text/plain,*/*'})
report=[]
def get(url,params=None,timeout=55):
 for n in range(4):
  try:
   r=session.get(url,params=params,timeout=timeout)
   r.raise_for_status();return r
  except Exception:
   if n==3:raise
   time.sleep(2*(n+1))
for a in entries:
 try:
  api=get('https://commons.wikimedia.org/w/api.php',params={'action':'query','format':'json','prop':'imageinfo','iiprop':'url|size|sha1|extmetadata','titles':a['title']},timeout=40).json()
  p=next(iter(api['query']['pages'].values()))
  assert p.get('imageinfo'),('no metadata',a)
  m=p['imageinfo'][0]
  ex=m.get('extmetadata',{})
  observed=(ex.get('LicenseShortName',{}).get('value') or '')
  licenseurl=(ex.get('LicenseUrl',{}).get('value') or '')
  assert observed.lower().replace('-',' ') == a['license'].lower().replace('-',' ') or (a['license']=='Public domain' and re.search(r'public domain|pd-self',observed,re.I)),(a['id'],observed)
  assert m['width']>=1800 and m['height']>=1200,(a['id'],m['width'],m['height'])
  url=m['url']
  assert url.startswith('https://upload.wikimedia.org/'),url
  pic=get(url,timeout=120).content
  assert len(pic)>100_000 and pic[:2]==b'\xff\xd8',(a['id'],len(pic))
  image=Image.open(io.BytesIO(pic));image.verify()
  name=a['id']+'__CONTEXT_ARCHIVE_ORIGINAL.jpg'
  fp=dest/name;fp.write_bytes(pic)
  sha256=hashlib.sha256(pic).hexdigest()
  commons_sha1=hashlib.sha1(pic).hexdigest()
  assert commons_sha1.lower()==m['sha1'].lower(),(a['id'],commons_sha1,m['sha1'])
  s={'asset_id':a['id'],'file':name,'sha256':sha256,'commons_sha1':commons_sha1,
      'file_bytes':len(pic),'source_width':m['width'],'source_height':m['height'],
      'commons_file_title':a['title'],'commons_url':'https://commons.wikimedia.org/wiki/'+a['title'].replace('File:','File:').replace(' ','_'),
      'original_file_url':url,'license_id':observed,'license_url':licenseurl,
      'creator':a['creator'],'photograph_date':a['date'],'displayed_narrative_status':'NON-EVENT GENERIC CONTEXT ONLY',
      'factual_label_required':a['shot'],
      'license_verified_in_commons_metadata':True,
      'rights_requirement':'ATTRIBUTION_REQUIRED' if 'BY' in observed.upper() else 'PD_DESIGNATION_PRESERVED',
      'license_release':'SOURCE_RIGHTS_PRECHECK_PASS_WITH_CONDITIONS',
      'factual_release':'CONTEXT_ONLY_MUST_NOT_PASS_AS_REAL_2016_UBER_OTTO_TEST'}
  report.append(s)
 except Exception as e:
  report.append({'asset_id':a['id'],'status':'HOLD_FAILED_TO_ACQUIRE_OR_VERIFY','error':str(e)[:400]})
(dest/'13_CONTEXT_ACQUISITION_QC.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
lines=['VIDEO005 3 real archival CONTEXT photos (not the actual reported event).','Attribution / photography:',
       'VP009 Mike1024, Mapping van tomtom with five lidars, public domain, https://commons.wikimedia.org/wiki/File:Mapping_van_tomtom_with_five_lidars.jpg',
       'VP018 Oregon Department of Transportation, Autonomous truck cab on display, CC BY 2.0, https://commons.wikimedia.org/wiki/File:Autonomous_truck_cab_on_display_(44825419221).jpg, license https://creativecommons.org/licenses/by/2.0/',
       'VP042 Steve Jurvetson, Ford Autonomous Test Vehicle, CC BY 2.0, https://commons.wikimedia.org/wiki/File:Ford_Autonomous_Test_Vehicle.jpg, license https://creativecommons.org/licenses/by/2.0/',
       'NO CLAIM: these are not photos of 2016 Google files, Otto acquisition, or August 2016 Uber testing. Dates differ.',
       'Crop/retouch attribution: add if altered in later edit. Media here are unchanged original files.']
(dest/'CONTEXT_ATTRIBUTION_EN.txt').write_text('\n'.join(lines)+'\n')
with (dest/'CONTEXT_3_ORIGINALS.csv').open('w',newline='',encoding='utf8') as f:
  keys=['asset_id','file','sha256','commons_sha1','source_width','source_height','file_bytes','commons_url','original_file_url','license_id','license_url','creator','photograph_date','factual_label_required','license_release','factual_release']
  w=csv.DictWriter(f,fieldnames=keys);w.writeheader()
  for s in report:
    if 'sha256' in s:w.writerow({k:s.get(k,'') for k in keys})
print(json.dumps({'received':sum('sha256' in s for s in report),'expected':3,'sources':report},indent=2,ensure_ascii=False)[:7000])
assert len(report)==3 and all('sha256' in s for s in report),report
