#!/usr/bin/env python3
"""NO GENERATION. Refresh historical crop-text metadata against archived genuine PDFs.
Only JSON/CSV metadata changes: never touch, render or edit a single PNG/PDF/HTML."""
from pathlib import Path
import csv,hashlib,json,fitz,datetime
root=Path(__file__).resolve().parents[1]
src=root/'13_SOURCE_REAL_ACQUISITION'
cropfile=src/'REAL_CROP_QC_LEDGER_FINAL.json'
sourcefile=src/'SOURCE_DOWNLOAD_LEDGER_FINAL.json'
sourceindex=root/'SOURCE_INDEX.csv'
rows=json.loads(cropfile.read_text(encoding='utf-8'))
originals=json.loads(sourcefile.read_text(encoding='utf-8'))
def sha_file(path):
 h=hashlib.sha256()
 with open(path,'rb') as f:
  for block in iter(lambda:f.read(2**20),b''):h.update(block)
 return h.hexdigest()
assert len(originals)==13 and len(rows)==46
origin={r['source_id']:r for r in originals}
checked=[]
left_flags={'V005-VP008','V005-VP031','V005-VP045','V005-VP048','V005-VP053','V005-VP058','V005-VP061','V005-VP064'}
stale_repaired=0
for r in rows:
 sid=r['source_id'];asset=r['asset_id'];o=origin[sid]
 p=src/'original_sources'/(sid+'.'+o['type'])
 cp=src/'native_crops'/(asset+'__'+sid+'.png')
 assert p.is_file() and cp.is_file(),(asset,sid,'missing original/crop')
 assert sha_file(p)==o['source_sha256_verified_final'],(sid,'original sha mismatch')
 assert sha_file(cp)==r['crop_sha256'],(asset,sid,'crop sha mismatch')
 r['original_media_sha256_verified_from_archived_bytes']=True
 r['crop_sha256_verified_from_archived_bytes']=True
 if o['type']=='pdf':
  pageidx=r.get('page_1based',0)-1
  doc=fitz.open(p);assert 0<=pageidx<len(doc),(asset,sid)
  page=doc[pageidx]
  rect=fitz.Rect(r['crop_rect_pt'])
  assert page.rect.contains(rect),(asset,sid,'bad PDF point rect')
  s=page.get_text('text',clip=rect)
  if 'extracted_text' in r:
   r['historical_extracted_text_is_pre_recrop']=(r['extracted_text']!=s[:len(r['extracted_text'])])
   if r['historical_extracted_text_is_pre_recrop']:stale_repaired+=1
  # Replace the obsolete text with a complete re-extraction based on the CURRENT original rectangle.
  r['extracted_text']=s
  r['text_extraction_basis']='CURRENT_ARCHIVED_ORIGINAL_PDF_NATIVE_RECT'
  r['extracted_text_utf8_sha256']=hashlib.sha256(s.encode('utf-8')).hexdigest()
  intersects=[]
  outside_margin=[]
  for a in page.get_text('words'):
   x0,y0,x1,y1,word=a[:5]
   if y1<rect.y0 or y0>rect.y1:continue
   if x0<rect.x0<x1 or x0<rect.x1<x1:intersects.append(word)
   if x1<=rect.x0 and rect.x0-x1<45 and len(word)>2:outside_margin.append(word)
  r['word_crosses_crop_x_edge']=intersects
  r['left_margin_adjacent_original_words']=outside_margin[:20]
  r['source_crop_text_context']='HOLD_EDITOR_VERIFY_LEFT_MARGINAL_COURT_METADATA' if asset in left_flags else ('WORD_BOUNDARY_CROSSED_REVIEW' if intersects else 'NO_WORD_BOUNDARY_CROSSED')
  checked.append({'asset_id':asset,'source_id':sid,'page_1based':pageidx+1,'text_utf8_sha256':r['extracted_text_utf8_sha256'],
                  'source_crop_text_context':r['source_crop_text_context'],'words_intersecting_crop_x_edge':len(intersects),
                  'old_text_stale':r.get('historical_extracted_text_is_pre_recrop',False)})
 else:
  r['text_extraction_basis']='PUBLISHER_NATIVE_HTML_OR_SCREENSHOT_DO_NOT_SYNTHESIZE_TEXT'
  r['source_crop_text_context']='HOLD_EDITOR_VERIFY_NATIVE_HTML_TEXT_AND_RIGHTS'
  checked.append({'asset_id':asset,'source_id':sid,'text_utf8_sha256':None,'source_crop_text_context':r['source_crop_text_context']})
assert len({r['asset_id'] for r in rows})==37
cropfile.write_text(json.dumps(rows,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
# Keep the SOURCE_INDEX provenance contract accurate: 13 originals HAVE now been archived.
with sourceindex.open(newline='',encoding='utf-8') as f:
 reader=csv.DictReader(f);fieldnames=reader.fieldnames;registry=list(reader)
assert len(registry)==36
n=0
for r in registry:
 sid=r['source_id']
 if sid not in origin:continue
 typ=origin[sid]['type']
 r['archived_copy']='13_SOURCE_REAL_ACQUISITION/original_sources/'+sid+'.'+typ
 # Preserve verified research and old authorship/filing dates, do not imply rights were cleared.
 n+=1
assert n==13
with sourceindex.open('w',newline='',encoding='utf-8') as f:
 wr=csv.DictWriter(f,fieldnames=fieldnames);wr.writeheader();wr.writerows(registry)
s={
 'date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'method':'read_only_original_media / updated_metadata_only',
 'no_media_created_or_modified':True,'original_sources_hash_verified':13,
 'crop_hash_verified_records':len(rows),'individual_authentic_assets':len({r['asset_id'] for r in rows}),
 'pdf_source_text_refreshed':sum('extracted_text_utf8_sha256' in r for r in rows),
 'historical_pdf_text_fields_repaired':stale_repaired,
 'eight_margin_context_flags_still_require_visual_review':sorted(left_flags),
 'native_pdf_words_crossing_x_edge':sum(x.get('words_intersecting_crop_x_edge',0) for x in checked),
 'source_index_archive_paths_updated':n,
 'rights_status':'HOLD_FINAL_USE_ASSESSMENT',
 'composited_final_authentic_frames':'NOT_GENERATED_AS_ORDERED',
 'final_stage13_status':'SOURCE_PROVENANCE_AND_TEXT_METADATA_COMPLETE / IMAGE_ASSEMBLY_OWNER_HOLD'
}
(root/'13_METADATA_REPAIR_QC.json').write_text(json.dumps(s,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(s,ensure_ascii=False,indent=2))
