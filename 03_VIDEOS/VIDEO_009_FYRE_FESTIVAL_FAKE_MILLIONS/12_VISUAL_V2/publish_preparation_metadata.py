from pathlib import Path
import csv,hashlib,json,re,shutil,io
R=Path(r'C:\Users\KK\VIDEO009_VISUAL_PRODUCTION')
REPO=Path(r'C:\Users\KK\Youtube-3-video009-visual-v2')
EP=REPO/'03_VIDEOS/VIDEO_009_FYRE_FESTIVAL_FAKE_MILLIONS';O=EP/'12_VISUAL_V2'
DATE='2026-10-30'
def read(p):return list(csv.DictReader(p.open(encoding='utf-8-sig',newline='')))
def write(p,items):
    with p.open('w',encoding='utf-8',newline='') as f:w=csv.DictWriter(f,list(items[0]),lineterminator='\n');w.writeheader();w.writerows(items)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
stock=read(O/'STOCK/STOCK_REGISTRY_V2.csv');stock_by={x['asset_id']:x for x in stock}
docs=read(O/'DOCUMENTS/DOCUMENT_CROP_REGISTRY.csv');doc_by={x['asset_id']:x for x in docs}
gfs=read(O/'GENERATION_REVIEW_V2.csv');gf_by={x['asset_id']:x for x in gfs}
timeline=read(O/'VISUAL_TIMELINE_V2.csv');paras={x['paragraph_id']:x for x in read(O/'VOICE_PARAGRAPH_MAP.csv')}
ss=json.loads((O/'STOCK/STOCK_QC_SUMMARY.json').read_text());ds=json.loads((O/'DOCUMENTS/DOCUMENT_QC_SUMMARY.json').read_text())
for t in timeline:
    aid=t['asset_id']
    if aid in stock_by:t['asset_status']=stock_by[aid]['qc']+'_'+stock_by[aid]['technical_qc']
    elif aid in doc_by:t['asset_status']='PASS_AUTHENTIC_CROP_VERIFIED; FINAL_FRAME_COMPOSITING_NOT_STARTED'
    else:t['asset_status']='SPEC_AND_REFERENCES_CHECKED_IMAGE_NOT_RENDERED'
    assert paras[t['paragraph_id']]['locked_text'][int(t['paragraph_char_start']):int(t['paragraph_char_end'])]==t['script_anchor_verbatim']
write(O/'VISUAL_TIMELINE_V2.csv',timeline)
qc=[];assets=[]
for t in timeline:
    aid=t['asset_id'];status='HOLD';file='';digest='';kind='';source_url='';license_status='';download_status='';note='';hash_kind='ACTUAL_FILE'
    if aid in doc_by:
        d=doc_by[aid];status='PASS';file=(O/'DOCUMENTS/CROPS'/Path(d['file']).name).relative_to(EP).as_posix();digest=d['sha256'];kind='AUTHENTIC_DOCUMENT_CROP';source_url=d['actual_download_url'];license_status='US_GOVERNMENT_TEXT_SCOPE';download_status='FILE_VERIFIED';note=d['source_provenance']+'; '+d['source_substitution_or_limits']
        assert sha(EP/file)==digest
    elif aid in stock_by:
        d=stock_by[aid];status=d['qc'];file=d['local_original'];digest=d['sha256'];kind='LICENSED_STOCK_'+d['type'].upper();source_url=d['source_page'];license_status=d['commercial_youtube'];download_status=d['technical_qc'];note=d['thematic_usage_and_limits']
        if file and Path(file).is_file():assert sha(Path(file))==digest
    else:
        d=gf_by[aid];file=f'12_VISUAL_V2/REFERENCES/{aid}.json';digest=sha(EP/file);kind='EDITOR_NATIVE_BRIEF_NOT_RENDERED_IMAGE';hash_kind='REFERENCE_SPEC_NOT_RENDERED_IMAGE';source_url=d['fact_source_url'];license_status='ORIGINAL_EDITOR_GRAPHIC_DESIGN';download_status='NOT_RENDERED';note='Distinct exact-text brief and hashed genuine references checked; renderer not run. No image-generation credit spent.'
    assets.append({'asset_id':aid,'type':kind,'source_url':source_url,'license_status':license_status,'download_status':download_status,'usage_note':note,'act':t['act'],'paragraph_id':t['paragraph_id'],'local_asset_path':file,'sha256':digest,'hash_kind':hash_kind,'qc':status})
    qc.append({'asset_id':aid,'act':t['act'],'paragraph_id':t['paragraph_id'],'qc':status,'scope':'SOURCE_PREPARATION_ONLY_NOT_FINAL_RENDER','actual_file':file,'sha256':digest,'issue_or_limit':note if status!='PASS' else 'Final edit legibility/context and release remain separate gates'})
assert len(assets)==142
write(EP/'ASSET_MANIFEST.csv',assets);write(O/'QC_REGISTRY_V2.csv',qc)
missing=[{'item_id':x['asset_id'],'kind':x['type'],'status':x['qc'],'missing_or_action':x['usage_note']} for x in assets if x['qc']!='PASS']
missing.extend([{'item_id':'SEC_OFFICIAL_PDF','kind':'ARCHIVAL_SOURCE','status':'HOLD','missing_or_action':'OfficialSECdomain download403; genuine court-complaint mirror available, no official-byteidentity claimed.'},{'item_id':'SEC_RELEASE_LOCAL','kind':'ARCHIVAL_SOURCE','status':'HOLD','missing_or_action':'Officialrelease primarywebtext checked; exact localHTML response and settlementparagraph sourcepixels unavailable.'},{'item_id':'AUDIO_TIMINGS','kind':'VOICE_ALIGNMENT','status':'HOLD','missing_or_action':'No VIDEO009 accepted narration or measuredwordtimings yet; all142ranges are explicitlyESTIMATED.'},{'item_id':'FINAL_INDEPENDENT_STOCK_TEXT_RECHECK','kind':'QC','status':'HOLD','missing_or_action':'Independent critic inspected14crops and drafttext; final stock/text rereview interrupted by usage limit. Root checks are recorded separately, not substituted as independent approval.'}])
write(O/'MISSING_MATERIALS_V2.csv',missing)
for p in (R/'PREP').glob('*.py'):shutil.copy2(p,O/p.name)
doc_summary=f"6 genuine case-sourcefiles:4DOJ rawHTML responses,1officialDOJnativePDF and1SECcourtcomplaintPDFfromexplicitCCHmirror.14authenticcrops independently matchedpixel-for-pixel; officialSECdownload403HOLD remains. SourceZIP: `DOCUMENTS/VIDEO009_ORIGINAL_DOCUMENT_SOURCES.zip`, SHA256 `{ds['source_archive_sha256']}`."
report=f'''# VIDEO009 — actual visual preparation V2 — {DATE}

## Result and boundaries

Preparation executed from main `cc63aa6321e6f509dbc0f9706434aec9b410938a`. Locked V3 EN Gitblob `8edd63b3734e12c49a679e53c7719c0730299438` verified; script/voice files untouched. WindowsCRLF workingbytes and canonical GitLF identity are recorded separately.

{doc_summary}

All76 stock requests processed: {ss['downloaded_original_files']} original files physically downloaded ({ss['downloaded_bytes']}bytes). {ss['source_pool_license_and_technical_pass']} unique sources have item-level commercial-license evidence and technical checks ({ss['pool_videos']}videos/{ss['pool_photos']}photos). Request-level selection: {ss['request_rows_pass']}PASS / {ss['request_rows_hold']}HOLD / {ss['request_rows_reject']}REJECT. PASS assignments currently use {ss['distinct_files_used_by_pass_rows']}distinct originals; reuse is explicit, not presented as76unique cleared clips. Originalstockbinaries remain local under `C:/Users/KK/VIDEO009_VISUAL_PRODUCTION/STOCK/ORIGINALS`; direct source/downloadURLs andSHA256 are in the committed registry. Do not upload800MB of video into ordinaryGit.

Landscape originals with explicit16:9 editorial crops are permitted under the owner's thematic-material priority, rather than silently substituting unrelatednative16:9stock. Originals and cropbboxes are retained. Portraits were rejected. TrueNYCfederalcourthouse photographs replace unrelatedLA courtcontext where relevant. Broadercourthouses panorama is not treated as the actualsentencing venue. Broadcombranding and unsupportedshredder imagery are rejected. Identifiablemodels and inaccurate exactscene substitutes remainHOLD.

All52 GF briefs have distinct reviewed compositions and genuine hashed referencefiles: `GENERATION_PROMPTS_REVIEWED_V2.md`, `GENERATION_REVIEW_V2.csv`, `GENERATION_REFERENCE_REGISTRY.csv` and52`REFERENCES/GFxxx.json` sidecars. Native editableSVG/PNG is the correct route for precise labels/tables/diagrams. No officialsource pages are recreated orsent toimagegeneration. No yellow/redoutlines are bakedinto assets; emphasisbelongsinseparateFusionlayers.

First10imagequeue: `FIRST_BATCH_10_QUEUE.csv`, GF001–GF010. Each is one1920x1080editor-native frame with separate layers. **10native renders /0paidmodeljobs /$0API and0credits**. This is not anImageGentariff. PhotographicImageGenwork is not part of this zero-costroute and would need its own scopedquote/approval. NoGFimages have been rendered in this preparation snapshot.

All142positions mapped to37lockedparagraphs/1804words, with exact source-verbatim sentence/phrase offsets and source hashes. All intervals are **ESTIMATED**, basedon145wpm without measuredpauses; total746.483s is a planningmodel, not an audio runtime. Inventory entries are selectable base/insert/alternative/reveal positions, not142forcedhardcuts. `VISUAL_DENSITY_QC.csv` gives named staged progression for longparagraphs andwarns about denseopeners. Finalpacing cannotPASS withoutactualaudio andpicture.

## Files to open

- `DOCUMENTS/VIDEO009_ORIGINAL_DOCUMENT_SOURCES.zip`, `DOCUMENTS/ORIGINAL_SOURCE_SHA256.csv`, `DOCUMENTS/DOCUMENT_CROP_REGISTRY.csv`,14PNGcrops andnative referencepages.
- `STOCK/STOCK_REGISTRY_V2.csv`, `STOCK/STOCK_ORIGINAL_SHA256.csv`, `STOCK/REQUIRED_CREDITS.txt`, item/license evidence and47real previews.
- `VISUAL_TIMELINE_V2.csv`, `VOICE_PARAGRAPH_MAP.csv`, `VISUAL_DENSITY_QC.csv`.
- `GENERATION_PROMPTS_REVIEWED_V2.md`, `GENERATION_REFERENCE_REGISTRY.csv`, `FIRST_BATCH_10_QUEUE.csv`.
- `QC_REGISTRY_V2.csv`, `MISSING_MATERIALS_V2.csv`, `INDEPENDENT_QC.md` and `LEAD_QC_RECONCILIATION.md`.

Overall visual-asset completion is **HOLD**, notPASS. Missingstock/exactscene slots, directSECarchive, paid/nativegenerationoutputQC, actualaudio timing and finalindependentstock/textreview remain explicit. Netflix/Hulu/documentaryfootage was not used. NoTTS, timelineassembly, video/imagegeneration or paidcredits were executed during this preparation snapshot. Theowner's later instruction authorizes the subsequent Voiceboxqueue and frameproduction; their actual execution belongs in separate state artifacts.
'''
(O/'PREPARATION_REPORT.md').write_text(report,encoding='utf-8')
(O/'LEAD_QC_RECONCILIATION.md').write_text('''# Lead resolution — preparation only

Independent review evidence is preserved verbatim in INDEPENDENT_QC.md. It independently confirms14/14real sourcepixelcrops andsource/crophashes. Draft issues were addressed by the maker:142exact sentence/phrase offsets; base/insert/alternative roles; named progression forP007/P017/P020/P021/P023/P025/P029; preciseGF033/041/044/046/030/051anchors; genuine Junecharging source; March/July sourcepair; SECplusDOJmoneycategories; actualMagnises sourcepage;66real reference records and52hashed sidecars.

Root checks: all142anchor substrings match the lockedparagraphs; all52sidecars contain existing source/page files with matchingSHA256;47stocksourcepreviews reviewed plus technical/rights metadata;76stockrequests explicitly reconciled. These checks do not become an independent finalreview. Thecritic reached a usage limit before the repaired text and finalstockregistry couldbe independentlyapproved. OverallstatusHOLD. No newagent was started to bypass thatlimit.
''',encoding='utf-8')

# Make authoritative stage state agree with the owner's explicitly authorized parallel visual-prep task.
p=EP/'manifest.yaml';t=p.read_text(encoding='utf-8')
updates={'last_updated':DATE,'current_stage':'12_VISUAL_SOURCE_PREPARATION','next_action':'Owner authorized subsequent local Harrison five-part queue, then native frame production. Complete unresolvedstock/context and independentreview before final visualPASS; no montage authorized.','stage_12_visual_source_generation_plan':'PREPARATION_COMPLETED_142_MAPPED_52_REVIEWED_14_REAL_CROPS_STOCK_HOLDS','stage_13_visual_asset_qc':'PARTIAL_DOC14_INDEPENDENT_PIXEL_PASS_STOCK38PASS_36HOLD_2REJECT','visual':'PREPARATION_DONE_WITH_DECLARED_HOLDS_NO_FINAL_ASSET_PASS'}
for key,value in updates.items():
    t,n=re.subn(r'(?m)^(\s*'+re.escape(key)+r':) "[^"]*"$',lambda m:m[1]+' '+json.dumps(value),t,count=1);assert n==1,key
t+='\nvisual_preparation_v2:\n'
values={'date':DATE,'report':'12_VISUAL_V2/PREPARATION_REPORT.md','input_zip_sha256':'855e6f6c66873c1af5879be498879a749e92a50b101a34b858692012bc93e6ce','positions':142,'voice_paragraphs':37,'prompts_reviewed':52,'document_originals':6,'authentic_crops':14,'downloaded_stock_originals':50,'licensed_technical_stock_pool':47,'stock_request_pass':38,'stock_request_hold':36,'stock_request_reject':2,'timing':'ESTIMATED_NO_AUDIO','native_first_batch_images':10,'native_first_batch_api_cost_usd':0,'paid_generation_submitted':0,'overall_asset_qc':'HOLD','script_audio_modified':False}
for key,val in values.items():t+='  '+key+': '+json.dumps(val)+'\n'
p.write_text(t,encoding='utf-8')
p=EP/'STATE.md';old=p.read_text(encoding='utf-8');p.write_text(f'''# VIDEO009 — Fyre Festival — visual preparation V2 — {DATE}

Current stage: **12_VISUAL_SOURCE_PREPARATION**. Preparation executed; overallvisualassetcompletion **HOLD**.

37lockedparagraphs/1804words unchanged;142visualpositions mapped to exactscriptanchors, alltimeintervalsESTIMATED.52distinctGFbriefs withconcrete hashedsource/style references.14authenticdocumentcrops independentlypixelverified.6case-sourceoriginals saved, directSECarchive403HOLD withgenuineCCHcourtcomplaintmirrorexplicit.50stockoriginals downloaded;47licensed/technicallychecked;76requestrows:38PASS/36HOLD/2REJECT. Finalindependentstock/repairedtextreview incomplete aftercriticusage limit.

Open `12_VISUAL_V2/PREPARATION_REPORT.md`, `QC_REGISTRY_V2.csv` and `MISSING_MATERIALS_V2.csv`. First10nativeimagequeue prepared($0API,0paidjobs), notrendered in this snapshot. No paidgeneration/TTS/montage run during preparation. Owner subsequently authorized a five-partlocalVoiceboxqueue thenframeproduction; executionandIDs mustbe recordedbeforeclaimingstarted. NoStage15montageorpublicationauthorization.

## Historical handoff snapshots below

'''+old,encoding='utf-8')
p=EP/'VERSION_LOG.md';t=p.read_text(encoding='utf-8');marker='|---|---|---|---|\n';t=t.replace(marker,marker+f'| {DATE} | Visual preparation V2 | Actual6case sources,14independentpixelcrops,50stockoriginals/47licensedtechnicalpool;76requestQC;142exactanchors/ESTIMATEDintervals;52distinctbriefs+hashedrefs; first10nativezeroAPIcostqueue | PREPARED_WITH_EXPLICIT_STOCK_SEC_TIMING_AND_REVIEW_HOLDS |\n',1);p.write_text(t,encoding='utf-8')
p=EP/'QA_LEDGER.csv';t=p.read_text(encoding='utf-8-sig');s=io.StringIO();csv.writer(s,lineterminator='\n').writerow(['QA_VISUAL_V2_20261030','12_VISUAL_SOURCE_PREPARATION','MAKER_PLUS_INDEPENDENT_DOCUMENT_CRITIC','SOURCE_RIGHTS_PIXEL_SCRIPT_ALIGNMENT','MEDIUM','142POSITIONS_52GF_14DOC_76STK','No finalassetPASS with source rights timing or review gaps','ActualbytesSHA and14independentpixelmatches;76requestregistry','KeepHOLDwhereexactscene sourcearchival audio orindependentreviewmissing','SCOPED_PREPARATION_DELIVERED','OPEN_EXPLICIT_HOLDS','No paidgeneration voiceor montage in preparationsnapshot; owner laterauthorizedqueueandframes separately']);p.write_text(t.rstrip()+'\n'+s.getvalue(),encoding='utf-8')

# Add local archival locators without rewriting source/claim/legal prose.
p=EP/'SOURCE_INDEX.csv';src=read(p)
locators={'SRC001':'DOJ_PLEA_BROWSER_RESPONSE.html','SRC004':'SEC_COMPLAINT_CCH_MIRROR.pdf','SRC006':'DOJ_VIP_BROWSER_RESPONSE.html','SRC007':'DOJ_SENTENCE_BROWSER_RESPONSE.html','SRC008':'DOJ_INITIAL_CHARGES_BROWSER_RESPONSE.html'}
for row in src:
    if row['source_id'] in locators:
        row['archived_copy']='12_VISUAL_V2/DOCUMENTS/ORIGINALS/'+locators[row['source_id']]
        row['status']='ARCHIVED_PRIMARY_MIRROR_COPY_IDENTITY_CHECKED_OFFICIAL_BYTES_HOLD' if row['source_id']=='SRC004' else 'ARCHIVED_OFFICIAL_HTML_RESPONSE_AND_SOURCE_PIXEL_CHECKED'
write(p,src)
p=REPO/'02_PIPELINE/VIDEO_INDEX.csv';t=p.read_text(encoding='utf-8-sig');lines=t.splitlines(keepends=True)
for i,line in enumerate(lines):
    if line.startswith('009,'):lines[i]=line.replace(',02_CASE_STORY_MAP,',',12_VISUAL_SOURCE_PREPARATION,')
p.write_text(''.join(lines),encoding='utf-8')

checks=json.loads((O/'PREPARATION_CHECKS.json').read_text());checks.update(actual_doc_crops=14,doc_independent_pixel_qc='PASS14OF14',stock_downloaded_originals=50,stock_licensed_technical_pool=47,stock_requests={'PASS':38,'HOLD':36,'REJECT':2},visual_output_qc='HOLD_EXPLICIT_MISSING_SOURCES_STOCK_TIMING_RENDER_AND_FINAL_INDEPENDENT_REVIEW')
(O/'PREPARATION_CHECKS.json').write_text(json.dumps(checks,indent=2),encoding='utf-8')
# Verify preserved input bytes and all GF source/page reference hashes.
for row in read(O/'LOCKED_INPUT_SHA256.csv'):assert sha(EP/row['file'])==row['working_tree_sha256'],row['file']
for row in read(O/'GENERATION_REFERENCE_REGISTRY.csv'):
    for a,b in [('source_file_repo','source_sha256'),('reference_file_repo','reference_sha256')]:
        if row[a]:assert sha(EP/row[a])==row[b]
assert len(assets)==142 and len(docs)==14 and len(stock)==76 and len(gfs)==52
print(json.dumps({'report':str(O/'PREPARATION_REPORT.md'),'rows':len(assets),'docs':14,'stock_downloaded':50,'rights_technical_pool':47,'locked_inputs_unchanged':True,'overall':'HOLD_EXPLICIT'}))
