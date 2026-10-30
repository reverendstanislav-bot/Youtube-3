from pathlib import Path
import csv,hashlib,json,re,shutil
ROOT=Path(r'C:\Users\KK\VIDEO009_VISUAL_PRODUCTION')
EP=Path(r'C:\Users\KK\Youtube-3-video009-visual-v2\03_VIDEOS\VIDEO_009_FYRE_FESTIVAL_FAKE_MILLIONS')
OUT=EP/'12_VISUAL_V2'; DOC=OUT/'DOCUMENTS'; REF=OUT/'REFERENCES';REF.mkdir(exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read_csv(p):return list(csv.DictReader(p.open(encoding='utf-8-sig',newline='')))
def write_csv(p,rows):
    with p.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
facts={x['fact_id']:x for x in read_csv(DOC/'DOCUMENT_FACT_REFERENCES.csv')}
sources={x['source_id']:x for x in json.loads((DOC/'VERIFIED_SOURCES.json').read_text(encoding='utf-8'))}
groups={
 'BOOKINGS':[1,2,3,4,5,8,9,10,11,12,13,14,15,16,17,18,35,36,50,51,52],
 'REVENUE':[6,19,20,21,22,29,50,51], 'MAGNISES':[23,24,25],
 'BROKERAGE':[7,26,27,28,29,51], 'INSURANCE':[30,31,32,33,51],
 'INVESTOR_LOSSES':[34,46,49], 'VENDOR_LOSSES':[34,46,49],
 'JUNE_CHARGES':[37], 'MARCH_PLEA':[38,44], 'JULY_PLEA':[39,40,41,42,43,44],
 'SENTENCE':[45], 'FORFEITURE':[46,48], 'SEC_RAISED':[46,47],
 'SEC_OTHER_RESPONDENTS_NONADMISSION':[44,46,47]}
reviews=read_csv(OUT/'GENERATION_REVIEW_V2.csv');references=[];summary=[]
for row in reviews:
    n=int(row['asset_id'][2:]);ids=[key for key,ns in groups.items() if n in ns]
    assert ids,row['asset_id']
    links=[];support=[]
    for fid in ids:
        fact=facts[fid]
        if not fact['reference_page']:
            references.append({'asset_id':row['asset_id'],'reference_role':'ADDITIONAL_LEGAL_CAVEAT_PRIMARY_WEB_ONLY','fact_id':fid,'source_id':fact['source_id'],'official_url':fact['official_url'],'actual_download_url':'','source_file_repo':'','source_sha256':'','reference_file_repo':'','reference_sha256':'','page_1_based':fact['page_1_based'],'verified_passage':fact['verified_passage'],'guardrail':fact['guardrail'],'status':'HOLD_LOCAL_ARCHIVAL_COPY_NOT_AVAILABLE; PRIMARY_WEB_READ_VERIFIED'})
            links.append(f"Additional legal caveat: {fact['official_url']} — primary reader verified; genuine local release response remains HOLD.")
            continue
        origin=sources[fact['source_id']]
        source_repo=DOC/'ORIGINALS'/Path(origin['original_file']).name
        image_repo=DOC/'REFERENCE_PAGES'/Path(fact['reference_page']).name
        assert source_repo.is_file() and image_repo.is_file()
        assert sha(source_repo)==origin['original_sha256']
        entry={'asset_id':row['asset_id'],'reference_role':'FACT_SUPPORT_AND_GENUINE_SOURCE_PIXEL_REFERENCE','fact_id':fid,'source_id':fact['source_id'],'official_url':fact['official_url'],'actual_download_url':fact['actual_download_url'],'source_file_repo':source_repo.relative_to(EP).as_posix(),'source_sha256':sha(source_repo),'reference_file_repo':image_repo.relative_to(EP).as_posix(),'reference_sha256':sha(image_repo),'page_1_based':fact['page_1_based'],'verified_passage':fact['verified_passage'],'guardrail':fact['guardrail'],'status':'PASS_ACTUAL_LOCAL_FILE_HASH_AND_PASSAGE_CHECK; SEC_MIRROR_LIMITS_RETAINED' if fact['source_id']=='SEC_COMPLAINT_MIRROR' else 'PASS_ACTUAL_LOCAL_FILE_HASH_AND_PASSAGE_CHECK'}
        references.append(entry);support.append(entry)
        links.append(f"{fid}: `{entry['reference_file_repo']}`, page {fact['page_1_based']}; PNG SHA256 `{entry['reference_sha256']}`; source `{entry['source_file_repo']}`, SHA256 `{entry['source_sha256']}`. OfficialURL {fact['official_url']}; actualdownload {fact['actual_download_url']}. Scope: {fact['guardrail']}")
    assert support
    row['fact_source_id']=' | '.join(dict.fromkeys(x['source_id'] for x in support))
    row['fact_source_url']=' | '.join(dict.fromkeys(x['official_url'] for x in support))
    row['fact_ids']=' | '.join(ids)
    # A generic context crop must not be misrepresented as containing a specific fact.
    verified_crops={'BOOKINGS':'DOC004','REVENUE':'DOC005','BROKERAGE':'DOC006','INSURANCE':'DOC008','INVESTOR_LOSSES':'DOC003','JUNE_CHARGES':'DOC010','MARCH_PLEA':'DOC009','JULY_PLEA':'DOC011','SENTENCE':'DOC013','SEC_RAISED':'DOC014'}
    row['document_reference_id']=' | '.join(dict.fromkeys(verified_crops[fid] for fid in ids if fid in verified_crops)) or 'GENUINE_FULL_SOURCE_REFERENCE_PAGE_NOT_A_SELECTED_CROP'
    row['reference_paths_or_urls']=' | '.join(x['reference_file_repo']+'#sha256='+x['reference_sha256'] for x in support)
    row['fact_qc']='PASS_LOCAL_PRIMARY_PASSAGES; MIRROR_PROVENANCE_EXPLICIT'
    row['additional_caveat_archival_hold']='SEC_RELEASE_LOCAL_ARCHIVE' if 'SEC_OTHER_RESPONDENTS_NONADMISSION' in ids else ''
    # Canonical style references are actual repository files, not invented image URLs.
    canonical_refs=[]
    for name in ['00_FOUNDATION/VISUAL_LOCK.md','00_FOUNDATION/EDITING_CANON.md','01_CHANNEL/VISUAL_BIBLE.md']:
        path=EP.parent.parent/name
        assert path.is_file();canonical_refs.append({'path':name,'sha256':sha(path),'role':'CHANNEL_STYLE_REFERENCE'})
    sidecar={'asset_id':row['asset_id'],'paragraph_id':row['paragraph_id'],'production_route':'LOCAL_EDITOR_NATIVE_SVG_PNG','source_fact_references':support,'legal_archival_hold':row['additional_caveat_archival_hold'],'canonical_style_references':canonical_refs,'layout':row['layout_fingerprint'],'frame':[1920,1080],'clean_lower_zone':[0,864,1920,1080],'separate_layers':['background','editorial_geometry','factual_type','semantic_emphasis','reveal_masks'],'images_generated':0,'api_cost_usd':0,'official_documents_must_never_be_generated':True}
    (REF/(row['asset_id']+'.json')).write_text(json.dumps(sidecar,ensure_ascii=False,indent=2),encoding='utf-8')
    summary.append((row['asset_id'],links))
write_csv(OUT/'GENERATION_REVIEW_V2.csv',reviews)
write_csv(OUT/'GENERATION_REFERENCE_REGISTRY.csv',references)
text=(OUT/'GENERATION_PROMPTS_REVIEWED_V2.md').read_text(encoding='utf-8')
parts=re.split(r'(?m)(?=^## GF\d+)',text);new=[parts[0]]
for part,(aid,links) in zip(parts[1:],summary):
    assert part.startswith('## '+aid)
    begin=part.index('**References:**');end=part.index('**Motion handoff:**')
    part=part[:begin]+'**Concrete source and style references:**\n- Canonical actual repository files: `00_FOUNDATION/VISUAL_LOCK.md`, `00_FOUNDATION/EDITING_CANON.md`, `01_CHANNEL/VISUAL_BIBLE.md`.\n'+''.join('- '+link+'\n' for link in links)+'\n'+part[end:]
    new.append(part)
assert len(new)==53
(OUT/'GENERATION_PROMPTS_REVIEWED_V2.md').write_text(''.join(new),encoding='utf-8')
first=read_csv(OUT/'FIRST_BATCH_10_QUEUE.csv')
for r in first:
    matched=next(x for x in reviews if x['asset_id']==r['asset_id']);r['references']=matched['reference_paths_or_urls'];r['source_review']='PASS_LOCAL_FILES_HASH_VERIFIED'
write_csv(OUT/'FIRST_BATCH_10_QUEUE.csv',first)
print(json.dumps({'briefs_with_local_fact_and_pixel_references':len(reviews),'reference_records':len(references),'individual_reference_sidecars':len(list(REF.glob('GF*.json'))),'first_batch':len(first),'paid_generation_submitted':0}))
