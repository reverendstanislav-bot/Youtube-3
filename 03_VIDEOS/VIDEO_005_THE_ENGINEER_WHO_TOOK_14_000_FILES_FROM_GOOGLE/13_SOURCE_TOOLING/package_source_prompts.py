#!/usr/bin/env python3
"""VIDEO005 original source + 110 prompt asset package, NO generation or fabrication."""
from pathlib import Path
import csv,zipfile,json,re,hashlib,datetime
P=Path(__file__).resolve().parents[1]
OUT=P/'13_PRODUCTION_HANDOFF_ASSET_PACKAGE'
OUT.mkdir(exist_ok=True)
def csvfile(path):
 with path.open(newline='',encoding='utf8') as f:return list(csv.DictReader(f))
def jsonfile(path):return json.loads(path.read_text(encoding='utf8'))
plans=csvfile(P/'12_VISUAL_ASSET_PLAN.csv')
assert len(plans)==110 and len({x['asset_id'] for x in plans})==110
cat={}
for a in plans:cat.setdefault(a['primary_class'],set()).add(a['asset_id'])
assert {k:len(v) for k,v in cat.items()}=={'EDITOR_GRAPHIC':60,'AUTHENTIC_SOURCE':37,'LICENSED_OR_USABLE_CONTEXT':3,'GENERATED_ILLUSTRATION':10}
gfile=P/'13_EDITOR_GFX_TASKS.jsonl'
gfx=[json.loads(line) for line in gfile.read_text(encoding='utf8').splitlines() if line.strip()]
assert len(gfx)==60 and {x['asset_id'] for x in gfx}==cat['EDITOR_GRAPHIC']
auth_ids=set()
for fn in ['13_AUTHENTIC_PROMPTS_AUTH01.md','13_AUTHENTIC_PROMPTS_AUTH02.md','13_AUTHENTIC_PROMPTS_AUTH03.md']:
 content=(P/fn).read_text(encoding='utf8')
 auth_ids|={'V005-'+x for x in re.findall(r'^## (VP\d{3})\b',content,re.M)}
assert len(auth_ids)==37 and auth_ids==cat['AUTHENTIC_SOURCE'],len(auth_ids)
genc=set(re.findall(r'^### (V005-VP\d{3})\b',(P/'12_IMAGE_PROMPTS.md').read_text(encoding='utf8'),re.M))
assert len(genc)==10 and genc==cat['GENERATED_ILLUSTRATION'],genc
ctx=set(re.findall(r'^## (V005-VP\d{3})\b',(P/'13_CONTEXT_PRODUCTION_PROMPTS.md').read_text(encoding='utf8'),re.M))
assert len(ctx)==3 and ctx==cat['LICENSED_OR_USABLE_CONTEXT'],ctx
sourceids=set()
for a in plans:sourceids.update(x for x in a['source_ids'].split(';') if x)
assert len(sourceids)==13
orig=P/'13_SOURCE_REAL_ACQUISITION/original_sources'
assert len(list(orig.iterdir()))==13
originals=jsonfile(P/'13_SOURCE_REAL_ACQUISITION/SOURCE_DOWNLOAD_LEDGER_FINAL.json')
orgmap={x['source_id']:x for x in originals}
for x in sourceids:
 assert x in orgmap
 src=orig/(x+'.'+orgmap[x]['type'])
 assert src.is_file() and hashlib.sha256(src.read_bytes()).hexdigest()==orgmap[x]['source_sha256_verified_final'],x
crops=P/'13_SOURCE_REAL_ACQUISITION/native_crops'
pngs=sorted(x for x in crops.glob('V005-VP*.png') if '__fullpage_QC' not in x.name)
assert len(pngs)==47,len(pngs)
context=P/'13_CONTEXT_ORIGINALS'
cj=jsonfile(context/'13_CONTEXT_ACQUISITION_QC.json')
assert len(cj)==3
for x in cj:
 f=context/x['file']
 assert f.exists() and hashlib.sha256(f.read_bytes()).hexdigest()==x['sha256']
 assert x['asset_id'] in cat['LICENSED_OR_USABLE_CONTEXT']
assert {x['asset_id'] for x in cj}==cat['LICENSED_OR_USABLE_CONTEXT']
ref_inventory=(P/'13_VISUAL_REFERENCE_BINARY_INVENTORY.md').read_text(encoding='utf8')
assert all(x in ref_inventory for x in ['how_the_files_moved.png','two_separate_costs_investigative_evidence_board.png','four_events_a_legal_tech_timeline.png'])
coverage={
 'video_id':'005','total_placements':110,
 'prompt_counts':{'AUTHENTIC_SOURCE':37,'EDITOR_GRAPHIC':60,'LICENSED_OR_USABLE_CONTEXT':3,'GENERATED_ILLUSTRATION':10},
 'prompt_assigned_110_of_110':True,
 'original_document_families_archived':13,
 'source_crops_archived':47,
 'context_original_photos_archived':3,
 'context_licenses':[{'asset_id':x['asset_id'],'license':x['license_id'],'sha256':x['sha256']} for x in cj],
 'style_references_AUTH':'3 PNG PRESENT_IN_COMPANION_CHAT_ZIP_SHA256_VERIFIED',
 'style_references_EDITOR_GFX':'3 PNG NOT_AVAILABLE_BINARY_OWNER_REATTACH_REQUIRED',
 'status':'PRODUCTION_SOURCE_AND_PROMPTS_COMPLETE_WITH_3_GFX_STYLE_REFERENCE_BINARY_HOLD',
 'images_generated':0,'credits_spent':0,
 'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(OUT/'PROMPTS_110_COVERAGE_QC.json').write_text(json.dumps(coverage,indent=2,ensure_ascii=False)+'\n')
columns=['asset_id','primary_class','scene_id','start_frame','end_frame_exclusive','start_sec','end_sec','instruction_source']
sourcefiles={'EDITOR_GRAPHIC':'13_EDITOR_GFX_TASKS.jsonl','AUTHENTIC_SOURCE':'13_AUTHENTIC_PROMPTS_AUTH01-02-03.md',
'LICENSED_OR_USABLE_CONTEXT':'13_CONTEXT_PRODUCTION_PROMPTS.md','GENERATED_ILLUSTRATION':'12_IMAGE_PROMPTS.md'}
with (OUT/'PROMPT_INDEX_110.csv').open('w',newline='',encoding='utf8') as f:
 w=csv.DictWriter(f,fieldnames=columns);w.writeheader()
 for x in plans:w.writerow({**{k:x.get(k,'') for k in columns},'instruction_source':sourcefiles[x['primary_class']]})
files={}
for doc in orig.iterdir():
 if doc.is_file():files['01_EVIDENCE/13_ORIGINAL_DOCUMENTS/'+doc.name]=doc
for img in pngs:files['01_EVIDENCE/47_NATIVE_SOURCE_CROPS/'+img.name]=img
for f in context.iterdir():
 if f.is_file():files['02_REAL_LICENSED_CONTEXT/'+f.name]=f
for name in [
 '13_AUTHENTIC_PROMPTS_AUTH01.md','13_AUTHENTIC_PROMPTS_AUTH02.md','13_AUTHENTIC_PROMPTS_AUTH03.md',
 '13_EDITOR_GFX_TASKS.jsonl','13_EDITOR_GFX_CANON_LOCK.md','13_EDITOR_GFX_CODEX_RUNBOOK.md',
 '13_CONTEXT_PRODUCTION_PROMPTS.md','12_IMAGE_PROMPTS.md','12_VISUAL_ASSET_PLAN.csv',
 '13_AUTHENTIC_37_NON_GENERATIVE_HANDOFF.csv','13_VISUAL_REFERENCE_BINARY_INVENTORY.md',
 '13_SOURCE_EDITORIAL_RIGHTS_PREFLIGHT.md','13_SOURCE_CROP_ACQUISITION_LEDGER.csv',
 '13_SOURCE_REAL_ACQUISITION/REAL_CROP_QC_LEDGER_FINAL.json',
 '13_SOURCE_REAL_ACQUISITION/SOURCE_DOWNLOAD_LEDGER_FINAL.json',
 'SOURCE_INDEX.csv','13_NO_GENERATION_PREPRODUCTION_CLOSURE.md',
 'manifest.yaml'
]:
 p=P/name;assert p.is_file(),name
 files['03_ALL_PROMPTS_SOURCES_QC/'+name.replace('/','__')]=p
files['00_COVERAGE/PROMPT_INDEX_110.csv']=OUT/'PROMPT_INDEX_110.csv'
files['00_COVERAGE/PROMPTS_110_COVERAGE_QC.json']=OUT/'PROMPTS_110_COVERAGE_QC.json'
readme=OUT/'README_RU.txt'
readme.write_text('VIDEO005: 110/110 production briefs; 13 court/official original sources; 47 authentic source crops; 3 license-audited context JPGs.\n'
'NO generated stills. Three AUTH canons must be added from accompanying previously approved CHAT ZIP (verified SHA256).\n'
'Three approved EDITOR GFX reference PNGs are NOT available in GitHub/archive; exact hashes/names provided in 13_VISUAL_REFERENCE_BINARY_INVENTORY.md; owner must provide their historical ZIP.\n'
'CC BY 2.0 context requires attribution, 2018 truck is NOT 2016 Otto, Ford 2015 is NOT Uber. No final-frame or rights blanket PASS.\n',encoding='utf8')
files['00_COVERAGE/README_RU.txt']=readme
dest=OUT/'VIDEO005_PRODUCTION_SOURCES_AND_PROMPTS.zip'
with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=5,allowZip64=True) as z:
 for name,fp in sorted(files.items()):z.write(fp,arcname=name)
print(json.dumps({'zip_file':str(dest),'files':len(files),'bytes':dest.stat().st_size,'coverage':coverage},indent=2))
