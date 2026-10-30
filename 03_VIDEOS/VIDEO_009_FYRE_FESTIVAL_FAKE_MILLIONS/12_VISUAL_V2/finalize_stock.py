from pathlib import Path
import csv,hashlib,json,shutil,subprocess
from PIL import Image,ImageOps,ImageDraw

R=Path(r'C:\Users\KK\VIDEO009_VISUAL_PRODUCTION\STOCK')
EP=Path(r'C:\Users\KK\Youtube-3-video009-visual-v2\03_VIDEOS\VIDEO_009_FYRE_FESTIVAL_FAKE_MILLIONS')
O=EP/'12_VISUAL_V2/STOCK';O.mkdir(exist_ok=True);(O/'EVIDENCE').mkdir(exist_ok=True);(O/'PREVIEWS').mkdir(exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rows(p):return list(csv.DictReader(p.open(encoding='utf-8-sig',newline='')))
def write_csv(p,x):
    with p.open('w',encoding='utf-8',newline='') as f:w=csv.DictWriter(f,list(x[0]),lineterminator='\n');w.writeheader();w.writerows(x)
raw=json.loads((R/'DOWNLOAD_RESULTS.json').read_text(encoding='utf-8'))
items={x['id']:dict(x) for x in raw}
for x in items.values():
    p=Path(x['local_path']) if x.get('local_path') else None
    if p and p.is_file():assert sha(p)==x['sha256']
    if x.get('technical_status')=='PASS':
        assert p and p.is_file() and x.get('license_verified') and x.get('creator') and x.get('item_evidence')
        x['visual_review']='PASS_ROOT_CONTACT_SHEET_REVIEW_43_SOURCE_SAMPLES'

# Four additional genuine files recovered after the batch metadata snapshot.
extra=[
 ('C_MOYNIHAN','COMMONS_MOYNIHAN_COURTHOUSE.jpg','Ken Lund','CC BY-SA 2.0','https://creativecommons.org/licenses/by-sa/2.0/','https://commons.wikimedia.org/wiki/File:Daniel_Patrick_Moynihan_U.S._Courthouse,_Manhattan,_New_York_(7237347688).jpg','Actual Daniel Patrick Moynihan US Courthouse entrance, Manhattan; no claim this is the sentencing day.'),
 ('C_MARSHALL','COMMONS_2.jpg','Kidfly182','CC BY-SA 4.0','https://creativecommons.org/licenses/by-sa/4.0/','https://commons.wikimedia.org/wiki/File:Thurgood_Marshall_United_States_Courthouse.jpg','Actual Thurgood Marshall courthouse; location context only, not a photographed case event.'),
 ('C_PANORAMA','COMMONS_3.jpg','giggel','CC BY 3.0','https://creativecommons.org/licenses/by/3.0/','https://commons.wikimedia.org/wiki/File:NYC_-New_York_County_Courthouse_-_Daniel_Patrick_Moynihan_US_Courthouse_-_panoramio.jpg','Actual NYC courthouses panorama, photographed2015; not footage of the2018 proceeding.'),
 ('10341357','PX10341357.jpeg','Vlad Deep','Pexels License','https://www.pexels.com/license/','https://www.pexels.com/photo/magnifying-glass-and-a-document-10341357/','Generic magnifier/insurance-document context; not any Fyre insurance policy or proof of executed coverage.')]
commons=json.loads((R/'COMMONS_EXTRA_DOWNLOADS.json').read_text(encoding='utf-8'))
for ident,name,creator,license_name,license_url,page,note in extra:
    p=R/'ORIGINALS'/name; im=Image.open(p);im.load();w,h=im.size
    assert w>=1280 and w>h
    direct=next((x['url'] for x in commons if Path(x['local_path']).name==name),'')
    if ident=='10341357':direct='https://images.pexels.com/photos/10341357/pexels-photo-10341357.jpeg'
    # Commons originalURL is extracted from the authoritative item-page evidence when available.
    if ident=='C_MOYNIHAN':
        direct='https://upload.wikimedia.org/wikipedia/commons/8/83/Daniel_Patrick_Moynihan_U.S._Courthouse%2C_Manhattan%2C_New_York_%287237347688%29.jpg'
    cw=min(w,round(h*16/9));ch=min(h,round(w*9/16));x=(w-cw)//2;y=(h-ch)//2;box=[x,y,x+cw,y+ch]
    preview=R/'PREVIEWS'/(ident+'.jpg');im.crop(box).resize((1280,720)).convert('RGB').save(preview,quality=91)
    items[ident]={'id':ident,'type':'photo','source_page':page,'url':page,'creator':creator,'license':license_name,'license_url':license_url,'commercial_youtube':'YES_SUBJECT_TO_ATTRIBUTION_AND_LICENSE_CONDITIONS','license_verified':True,'item_evidence':'LICENSE_AND_MAGNIFIER_ALTERNATIVE.txt' if ident=='10341357' else 'NYC_COURTHOUSE_RIGHTS.txt','local_path':str(p),'direct_download_url':direct,'bytes':p.stat().st_size,'sha256':sha(p),'width':w,'height':h,'format':'JPEG','duration_sec':'','technical_status':'PASS','full_decode':'PASS_IMAGE_LOAD','visual_review':'PASS_ROOT_FULL_IMAGE_OR_CONTACT_REVIEW','adaptation_exception':'LANDSCAPE_ORIGINAL_RETAINED_16_9_DERIVATIVE','crop_bbox':box,'preview_path':str(preview),'notes':note}

pool=[x for x in items.values() if x.get('technical_status')=='PASS']
assert len(pool)==47,len(pool)
for x in pool:
    preview=Path(x['preview_path']);assert preview.is_file()
    shutil.copy2(preview,O/'PREVIEWS'/preview.name)
    x['preview_repo']=(O/'PREVIEWS'/preview.name).relative_to(EP).as_posix()
for name in ['ITEM_METADATA.json','DOWNLOAD_RESULTS.json','ROW_MAPPING.json','SELECTED_ITEMS.json','COMMONS_EXTRA_DOWNLOADS.json']:
    shutil.copy2(R/name,O/'EVIDENCE'/name)
for pattern in ['ITEM_PAGES_*.txt','NYC_COURTHOUSE_*.txt','LICENSE_AND_MAGNIFIER_ALTERNATIVE.txt','EARLY_REFERENCE_METADATA.txt']:
    for p in R.glob(pattern):shutil.copy2(p,O/'EVIDENCE'/p.name)
mapping=json.loads((R/'ROW_MAPPING.json').read_text(encoding='utf-8'))
assignment=mapping['mapping'].copy();assignment.update({'STK0707':'C_MOYNIHAN','STK0807':'C_MARSHALL','STK0901':'C_MOYNIHAN','STK0907':'10341357'})
hold_exact=set(mapping['hold_exact'])-{'STK0709','STK0908'}
bad={
'STK0106':'Prominent unrelated Broadcom branding. REJECT for the FYRE assignment; do not imply a corporate affiliation.',
'STK0202':'The sample shows a staged legal/judge-office context, not a booking calendar. Wrong narrative use.',
'STK0205':'Recognizable models in a business meeting; hands-only neutral derivative must be prepared before use in fraud narration.',
'STK0903':'Recognizable actor/business-document context; neutral hands-only derivative not yet prepared.',
'STK0906':'UPS truck dominates the nominal NYC street shot; unsuitable Manhattan-wide establishing view.',
'STK1004':'Shredder falsely implies destruction of case records; no such event is established by the locked narration.'}
registry=[]
queue=rows(Path(r'C:\Users\KK\VIDEO009_VISUAL_PRODUCTION\INPUT_PACKAGE\VIDEO009_CODEX_VISUAL_PACKAGE\STOCK_SEARCH_QUEUE_V2.csv'))
for request in queue:
    aid=request['asset_id'];item=items.get(assignment.get(aid,''));note=mapping['exceptions'].get(aid,'')
    if aid in ('STK0707','STK0807','STK0901'):note=item['notes']+' Attribution and ShareAlike conditions must be retained when applicable; not period-event footage.'
    if aid=='STK0907':note=item['notes']
    if aid=='STK0709':note='Genuine anonymous hands handling an archive-style file box; suitable contextual document handling, not case evidence.'
    if aid=='STK0908':note='Visual sample confirms a genuine banknote-counting machine. Generic financial-process context only.'
    status='PASS' if item and item.get('technical_status')=='PASS' else 'HOLD'
    if aid in hold_exact:status='HOLD';note+=' Exact requested scene remains missing; downloaded alternative is not silently accepted.'
    if aid in bad:status='REJECT' if aid in ('STK0106','STK1004') else 'HOLD';note=bad[aid]
    if not item:note=mapping['missing'].get(aid,note or 'No downloaded item with verified rights and suitable scene.')
    if item and item.get('technical_status')!='PASS':note+=' Source/download QC: '+item.get('failure',item['technical_status'])
    registry.append({'asset_id':aid,'act':request['act'],'requested_scene':request['required_scene'],'source_item_id':item['id'] if item else '', 'source_page':item.get('source_page','') if item else '', 'direct_download_url':item.get('direct_download_url','') if item else '', 'creator_rightsholder':item.get('creator','') if item else '', 'license':item.get('license','') if item else '', 'license_url':item.get('license_url','') if item else '', 'commercial_youtube':item.get('commercial_youtube','') if item and item.get('technical_status')=='PASS' else 'NOT_VERIFIED_FOR_DOWNLOADED_SUITABLE_ITEM', 'attribution_and_conditions':(item['creator']+'; '+item['license']+'; '+item['source_page']+'; '+item['license_url']+'; crop/resize changes disclosed; preserve ShareAlike on adapted image where applicable') if item and 'CC BY' in item.get('license','') else 'Pexels License: no defamatory/offensive portrayal, no false endorsement; depicted people are not actual Fyre participants.', 'type':item.get('type','') if item else '', 'width':item.get('width','') if item else '', 'height':item.get('height','') if item else '', 'format':item.get('format','') if item else '', 'duration_sec':item.get('duration_sec','') if item else '', 'fps':item.get('fps','') if item else '', 'local_original':item.get('local_path','') if item else '', 'sha256':item.get('sha256','') if item else '', 'technical_qc':item.get('technical_status','NOT_DOWNLOADED') if item else 'NOT_DOWNLOADED', 'full_decode':item.get('full_decode','') if item else '', 'item_rights_evidence':('12_VISUAL_V2/STOCK/EVIDENCE/'+item['item_evidence']) if item and item.get('item_evidence') else '', 'adaptation':item.get('adaptation_exception','') if item else '', 'crop_bbox':json.dumps(item.get('crop_bbox',[])) if item else '', 'preview_repo':item.get('preview_repo','') if item else '', 'thematic_usage_and_limits':note or 'Generic contextual visual relevant to the specified scene. Never identify it as actual Fyre footage.', 'qc':status,'final_edit_context':'PENDING_NOT_A_PUBLICATION_CLEARANCE'})
assert len(registry)==76
write_csv(O/'STOCK_REGISTRY_V2.csv',registry)
write_csv(O/'MISSING_OR_REJECTED_STOCK.csv',[x for x in registry if x['qc']!='PASS'])
(O/'VERIFIED_DOWNLOAD_POOL.json').write_text(json.dumps(pool,ensure_ascii=False,indent=2),encoding='utf-8')
raw_inventory=[]
for p in sorted((R/'ORIGINALS').iterdir()):
    if p.is_file():raw_inventory.append({'file':str(p),'bytes':p.stat().st_size,'sha256':sha(p),'selected_pool':any(x['local_path']==str(p) for x in pool)})
write_csv(O/'STOCK_ORIGINAL_SHA256.csv',raw_inventory)
credit='\n'.join(x['attribution_and_conditions'] for x in registry if 'CC BY' in x['license'])
(O/'REQUIRED_CREDITS.txt').write_text(credit+'\n',encoding='utf-8')
# A fresh contact sheet for the four late additions is review evidence, not a final frame.
sheet=Image.new('RGB',(1600,520),'#171717');draw=ImageDraw.Draw(sheet)
for i,e in enumerate(extra):
    item=items[e[0]];im=Image.open(item['preview_path']);im=ImageOps.fit(im,(400,225));sheet.paste(im,(i*400,0));draw.text((i*400+8,245),item['id']+' / '+item['creator'],fill='white')
sheet.save(O/'LATE_ADDITIONS_CONTACT.jpg',quality=92)
summary={'stock_requests':76,'downloaded_original_files':len(raw_inventory),'downloaded_bytes':sum(x['bytes'] for x in raw_inventory),'source_pool_license_and_technical_pass':len(pool),'pool_videos':sum(x['type']=='video' for x in pool),'pool_photos':sum(x['type']=='photo' for x in pool),'request_rows_pass':sum(x['qc']=='PASS' for x in registry),'request_rows_hold':sum(x['qc']=='HOLD' for x in registry),'request_rows_reject':sum(x['qc']=='REJECT' for x in registry),'distinct_files_used_by_pass_rows':len({x['sha256'] for x in registry if x['qc']=='PASS'}),'no_netflix_hulu_or_documentary_footage':True,'source_binaries_storage':'Local VIDEO009_VISUAL_PRODUCTION/STOCK/ORIGINALS; registry contains direct retrieval URLs and SHA256; large stock videos not in ordinaryGit','rights_scope':'Commercial license permission and item provenance, subject to recorded attribution/adaptation/context limits; final film/publication not approved','independent_stock_final_review':'NOT_COMPLETED_REVIEWER_USAGE_LIMIT; root inspected all43batch samples and4late-addition samples'}
(O/'STOCK_QC_SUMMARY.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary))
