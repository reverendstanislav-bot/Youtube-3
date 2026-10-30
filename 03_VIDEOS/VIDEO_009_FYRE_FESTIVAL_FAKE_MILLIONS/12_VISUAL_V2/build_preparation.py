from pathlib import Path
import csv, hashlib, json, re, shutil

ROOT=Path(r'C:\Users\KK\VIDEO009_VISUAL_PRODUCTION')
REPO=Path(r'C:\Users\KK\Youtube-3-video009-visual-v2')
EP=REPO/'03_VIDEOS/VIDEO_009_FYRE_FESTIVAL_FAKE_MILLIONS'
IN=ROOT/'INPUT_PACKAGE/VIDEO009_CODEX_VISUAL_PACKAGE'
OUT=EP/'12_VISUAL_V2'; OUT.mkdir(exist_ok=True)
def write_csv(path,rows):
    assert rows
    with path.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
def read_csv(path):return list(csv.DictReader(path.open(encoding='utf-8-sig',newline='')))
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
package=[]
for line in (IN/'PACKAGE_SHA256_V2.txt').read_text(encoding='utf-8-sig').splitlines():
    sha,name=line.split(None,1);name=name.strip();p=IN/name
    assert digest(p)==sha,name
    package.append({'file':name,'sha256':sha,'verification':'PASS_BYTES_MATCH_ATTACHED_MANIFEST'})
source=EP/'05R_SCRIPT_V3_EN.md'
canonical=source.read_bytes().replace(b'\r\n',b'\n')
blob=hashlib.sha1(b'blob '+str(len(canonical)).encode()+b'\0'+canonical).hexdigest()
assert blob=='8edd63b3734e12c49a679e53c7719c0730299438'
voice=(EP/'08_VOICE_SCRIPT.md').read_text(encoding='utf-8-sig')
vp=[x.strip() for x in re.split(r'\n\s*\n',voice) if x.strip() and not x.strip().startswith('#')]
paras=[];act=None;words=0
for block in re.split(r'\n\s*\n',canonical.decode('utf-8')):
    block=block.strip()
    if not block:continue
    if block.startswith('### ACT '):act=int(re.search(r'ACT (\d+)',block).group(1));continue
    if block.startswith('#'):continue
    assert act
    tokens=list(re.finditer(r'\S+',block));count=len(tokens)
    paras.append({'paragraph_id':f'P{len(paras)+1:03}','act':act,'word_count':count,'global_word_start':words,'global_word_end':words+count,'estimated_start_s':round(words*60/145,3),'estimated_end_s':round((words+count)*60/145,3),'timing_status':'ESTIMATED_145WPM_NO_AUDIO_NO_ADDED_PAUSE_MODEL','locked_text':block})
    words+=count
assert vp==[p['locked_text'] for p in paras]
assert len(paras)==37 and words==1804
shots=read_csv(IN/'SHOT_PLAN_V2.csv');stocks=read_csv(IN/'STOCK_SEARCH_QUEUE_V2.csv');docs=read_csv(IN/'DOCUMENT_CROP_PLAN_V2.csv')
sections=re.split(r'(?m)^## ',(IN/'GENERATION_PROMPTS_V2.md').read_text(encoding='utf-8-sig'))[1:]
briefs=[]
for section in sections:
    lines=section.splitlines();h=re.match(r'(GF\d+) — Act (\d+) — (.+)',lines[0]);assert h
    fields={line.split(':',1)[0]:line.split(':',1)[1].strip() for line in lines[1:] if ':' in line}
    briefs.append({'asset_id':h[1],'act':int(h[2]),'title':h[3],'original_type':fields['TYPE'],'original_role':fields['NARRATIVE ROLE']})
assert len(shots)==142 and len(stocks)==76 and len(docs)==14 and len(briefs)==52
assert len({s['shot_id'] for s in shots})==142
assert {s['asset_id'] for s in shots}=={b['asset_id'] for b in briefs}|{d['asset_id'] for d in docs}|{s['asset_id'] for s in stocks}

# Explicit semantic assignment, not a simple distribution by row number.
gp=[1,1,2,2,2,3,4,4,5,5,5,6,6,8,8,9,9,10,12,11,11,12,13,14,14,15,15,16,17,18,19,19,20,21,22,23,24,24,25,26,26,26,27,29,30,34,33,32,31,35,36,37]
dp=[1,2,5,9,11,15,15,19,24,24,27,27,30,33]
sp={1:[1,1,4,3,1,4],2:[5,5,5,5,6,5,7],3:[9,8,8,8,9,10,10],4:[11,11,12,11,12,12,13],5:[14,14,15,16,15,16,14],6:[18,18,19,18,18,19,18,21],7:[22,22,22,22,22,24,24,22,25],8:[26,26,26,26,27,28,27,28,26],9:[30,31,31,32,32,33,33,34,34],10:[35,35,36,36,37,37,37]}
mapping={f'GF{i+1:03}':p for i,p in enumerate(gp)}|{f'DOC{i+1:03}':p for i,p in enumerate(dp)}
for s in stocks:
    a=int(s['act']);index=int(s['asset_id'][-2:])-1;mapping[s['asset_id']]=sp[a][index]
assert len(mapping)==142

designs=[
'One continuous tropical-light to ledger-line transition; single full-frame state, not a split screen. Keep a clean horizon and a separate native ledger motif; no depicted real Fyre invitation.',
'Large open question integrated into charcoal negative space: WHAT DID THE RECORDS SHOW? Typography is the object; no empty index-card or boxed dashboard.',
'One giant 2,500+ counter with ONE MONTH and CLAIMED, explicitly Fyre Media platform bookings. Animate the counter only after the qualifying label is visible.',
'A restrained matrix of60 small native marks resolving into the number60, with CONFIRMED / ONE YEAR. Keep the year visible throughout; never compare on a shared rate axis.',
'Two unequal calendar-duration strips: one month and one year. Separate units, no common bar scale or conversion into an unsupported ratio.',
'Single precise revenue amount $57,443 with May2016–April2017 and PLATFORM BOOKINGS; visually separate it from the festival ticket motif.',
'Two typographic bounds >$2.5M and <$1,500 on an open field; CLAIMED/ACTUAL and SEC attribution. No scale implying exact balances or stolen shares.',
'A confidence question emerges from three fading verified-metric anchors. End with HOW DID ANYONE TRUST THIS BUSINESS? rather than another empty title card.',
'A sparse three-node booking workflow: customer, marketplace, performer. Independent shapes and connecting line; no invented completed booking or fake product UI.',
'Two independent vertical paths: Fyre Media marketplace and Fyre Festival publicity. Distinct purposes, no identical-operations claim and no sum connecting them.',
'One native spotlight fades off PUBLICITY while a transaction-verification question remains in focus. Editorial metaphor, not an invented investor meeting.',
'Three unfilled verification gates for transaction, customer and repeatability, phrased as questions. No checkmarks claiming that this company passed them.',
'A factual completed-transaction marker opposite a dashed forecast outline. Use words rather than invented chart values; keep hypothetical analysis explicit.',
'A funnel of questions from completed transaction to evidence of demand to confidence. Read as an analytical inference, not a witnessed investor decision.',
'A broken proof path from reported bookings to apparent marketplace success. DOJ plea context; avoid the original weaker allegation-only phrasing for McFarland admitted conduct.',
'One festival-stage outline separated from a platform booking mark by the explicit qualifier NOT FESTIVAL LINEUP. No actual artist likeness or invented event programme.',
'Use the authentic DOC004 crop as the only source pixels. Native callout anchors remain outside the source crop; never generate or typeset the DOJ passage.',
'A narrow reconciliation path connecting booking claim, transaction check and missing corroboration. This is an editorial checklist, not an authentic record.',
'Two unsupported assertions form a reinforcing loop: apparent booking volume and apparent revenue. Use a two-arc arrangement, not another three-node flow.',
'A neutral platform-service and revenue-recognition explainer, clearly analytical. No assertion that all booking value is platform revenue and no made-up amounts.',
'Only the sourced actual $57,443 is numeric. The inflated claim stays words, without an invented bar height, total or magnitude ratio.',
'A single scrutiny lens separates claim from investment decision. Abstract editorial diagram; no fictional private investor, signature or scene.',
'A quiet plain-text MAGNISES pivot with a track-record question, visually distinct from FYRE MEDIA; no fabricated historic logo or sale certificate.',
'Approximately $40M is labelled FALSE SALE CLAIM / DOJ. No transfer illustration suggesting the sale happened; separate claim from established non-sale.',
'An analytical founder-credential question, typography over a subtle timeline motif. Never fabricate a pitch-deck page, signature, acquirer or due-diligence certificate.',
'SEC balance bounds appear as two neutral measurement brackets, visually different from opening GF007; labels remain attached to their amounts. Not a recreated brokerage statement.',
'Abstract account-statement anatomy reduced to labelled regions only. Make EDITORIAL SCHEMATIC explicit; no account number, logo, signature, fake balance or source-page facsimile.',
'A two-lane verification diagram distinguishes company operating results from personal holdings. No connecting arrow implying they are the same asset pool.',
'Three sequential credibility layers, vertically offset rather than stacked opaque cards: bookings, revenue and claimed wealth. Each settles before the next arrives.',
'A simple risk wheel for weather, performers and logistics. Generic risk examples only; no claim these caused the historical festival failure.',
'A promised protection line sits outside an investor-risk path. DOJ attribution visible; no generated insurance policy, insurer logo, actual payout or signature.',
'A single documentary verdict about execution: POLICY NOT EXECUTED, with DOJ plea attribution. Plain editorial type, no forged CANCELLED stamp.',
'A ghosted protection contour is explicitly labelled REPRESENTATION, NOT COVERAGE. Separate the promised downside protection from an actual executed policy.',
'Two non-stacked criminal-loss measures: >$24M investor losses and $2M ticket-vendor losses. No festival budget heading and no all-attendee-loss claim.',
'An abstract empty-event site diagram with no real geolocation, tents count or asserted on-site detail. Clearly schematic; use rights-cleared Bahamas context separately.',
'A branching distinction: failed logistics and proven financial deception. A festival failure alone does not establish fraud; keep the legal premise written.',
'One dated timeline marker: June2017 criminal charges. The historic status is CHARGES at this point; do not label this marker a conviction.',
'A March6 2018 guilty-plea marker with the two initial wire-fraud categories. Distinct visual structure from the charge marker.',
'A restrained second-chapter question revealed only at P025. Do not name NYC VIP Access before P026 or imply an unknown private motive.',
'NYC VIP ACCESS appears as plain editorial text with SEPARATE LATER OPERATION. No invented corporate wordmark or real-ticket claim.',
'Separate Fyre and NYC VIP Access timelines with their own labels and dates. A temporal sequence is not by itself a causal arrow.',
'One group of generic ticket silhouettes for event categories. No real ticket facsimile, scannable barcode, specific venue, seat, signature or event-logo permission implied.',
'July26 2018 plea marker lists wire fraud, bank fraud and false statements. No upgraded charge-only claim and no assignment to other respondents.',
'March and July guilty pleas are shown as separate dated milestones on an unscaled strip. No invented proportional duration or conflated operation.',
'October11 2018: six-year historical sentence. Keep HISTORICAL SENTENCE visible; no current-custody statement or invented prison image.',
'Three separate non-additive rows for raised funds, criminal losses and forfeiture. Preserve >=, > and category labels; no total or stacked chart.',
'At least $27.4M with three entity names below a single bracket. Do not allocate amounts to entities or present raised funds as a criminal-loss subtotal.',
'Exact $26,191,306.28, with cents retained, labelled CRIMINAL FORFEITURE. No recovered-money animation or implied victim-recovery total.',
'LOSS IS NOT PRODUCTION BUDGET is the main distinction; the sourced investor/vendor figures stay secondary. Different thesis from the first loss reveal.',
'Closing distinction between claims and verified evidence, expressed as one continuous editorial line. No new source document or final total introduced.',
'Four successive scrutiny questions attached to bookings, revenue, holdings and insurance. Use an open path, not a repetitive card grid or dashboard.',
'One restrained closing file-edge or paper-line motif against charcoal, then negative space for the final thesis. No fabricated government page or decorative legal seal.'
]
assert len(designs)==52 and len(set(designs))==52
sources={r['source_id']:r['url'] for r in read_csv(IN/'SOURCE_URLS.csv')}
sources['DOJ_INITIAL_CHARGES']='https://www.justice.gov/usao-sdny/pr/manhattan-us-attorney-announces-charges-against-individual-defrauding-investors-digital'
facts=[];prompt_md=['# VIDEO009 — reviewed GF001–GF052 production briefs\n','No images are generated by this file. All52 are routed to editor-native SVG/PNG because their labels, diagrams and evidence require exact typography. An optional photographic background would need separate ImageGen approval; do not send official source pages to image generation.\n','Canonical palette: #0B0B0B / #1F1F1F / #EDEDED with restrained #D32222; warm natural paper may be ivory. Content bounds y90–800; y864–1080 remains empty. No collage, fake source page, baked outline or default box-grid.\n']
first=[]
for i,b in enumerate(briefs):
    aid=b['asset_id'];p=paras[mapping[aid]-1];n=i+1
    fact_id='SEC_RELEASE' if n in (7,26,27,28,47) else 'DOJ_VIP' if 40<=n<=44 else 'DOJ_SENTENCE' if n in (45,46,48,49) else 'DOJ_PLEA'
    if n==37:fact_id='DOJ_INITIAL_CHARGES'
    doc_id='DOC006' if fact_id=='SEC_RELEASE' and n!=47 else 'DOC014' if n==47 else 'DOC011' if fact_id=='DOJ_VIP' else 'DOC013' if fact_id=='DOJ_SENTENCE' else 'DOC004' if n in (3,4,5,14,15,16,17,18) else 'DOC005' if n in (6,19,20,21) else 'DOC008' if n in (30,31,32,33) else 'DOC003'
    legal='Analytical/editorial model; no new event or private decision claimed.' if b['original_type']=='diagram' else 'DOJ historical guilty-plea/sentencing scope; SEC findings/admissions specific to McFarland; no guilt assigned to other people.'
    refs=[f'00_FOUNDATION/VISUAL_LOCK.md',f'00_FOUNDATION/EDITING_CANON.md',f'08_VOICE_SCRIPT.md#{p["paragraph_id"]}',sources[fact_id],f'DOCUMENTS/CROPS/{doc_id} (resolve exact file from crop registry)']
    if n==37:
        doc_id='DOC010';refs[-1]='DOCUMENTS/CROPS/DOC010 (resolve exact file from crop registry)'
    if n==44:refs.extend([sources['DOJ_PLEA'],sources['DOJ_SENTENCE']])
    if n==46:refs.extend([sources['SEC_RELEASE'],sources['DOJ_PLEA']])
    if n in (1,35,52):refs+=['STOCK/PREVIEWS/PX9400986_NASSAU_BAHA_MAR.jpg — authentic Nassau context, not actual Fyre site']
    if n in (9,10,11,16,30,42):refs+=['STOCK/PREVIEWS/PX7722744_BAND_CONCERT.jpg — generic performance context only']
    fact={'asset_id':aid,'act':b['act'],'paragraph_id':p['paragraph_id'],'title':b['title'],'original_type':b['original_type'],'production_route':'LOCAL_EDITOR_NATIVE_SVG_PNG','model':'NONE','fact_source_id':fact_id,'fact_source_url':sources[fact_id],'document_reference_id':doc_id,'legal_scope':legal,'layout_fingerprint':designs[i],'prompt_review':'PASS_DISTINCT_BRIEF_SCRIPT_SCOPE','asset_qc':'HOLD_NOT_RENDERED','paid_jobs_authorized':False,'estimated_api_cost_usd':'0.00','reference_paths_or_urls':' | '.join(refs)}
    facts.append(fact)
    prompt_md.append(f'\n## {aid} — Act{b["act"]} — {b["title"]}\n\nScript: **{p["paragraph_id"]}**, unchanged locked paragraph.\nPurpose: {b["original_role"]}\n\n**Reviewed composition:** {designs[i]}\n\n**Legal/factual scope:** {legal}\n\n**References:**\n'+''.join('- '+r+'\n' for r in refs)+'\n**Motion handoff:** separate labelled foreground, background, factual text, semantic emphasis and mask layers. Specify clean entry/settle/read/exit states; do not create or edit a Resolve timeline. Keep highlights outside authentic source pixels.\n\n**Output after owner approval:** '+aid+'.svg + '+aid+'.png at1920x1080, plus source/rights/geometry JSON. No image model is needed for this exact-text native composition.\n\n**QC:** brief PASS; rendered asset HOLD until actual file and visible geometry are inspected.\n')
    if i<10:first.append({'batch_order':i+1,'asset_id':aid,'paragraph_id':p['paragraph_id'],'purpose':b['title'],'references':' | '.join(refs),'tool':'LOCAL_EDITOR_NATIVE_SVG_PNG','model':'NONE','output_images':1,'estimated_api_cost_usd':'0.00','credits':0,'status':'QUEUE_ONLY_NOT_RENDERED','optional_imagegen_model':'NOT_PROPOSED_FOR_EXACT_TEXT_GFX','optional_imagegen_cost':'NOT_APPLICABLE; if separately requested built-in tool exposes no numeric price'})
write_csv(OUT/'GENERATION_REVIEW_V2.csv',facts)
(OUT/'GENERATION_PROMPTS_REVIEWED_V2.md').write_text(''.join(prompt_md),encoding='utf-8')
write_csv(OUT/'FIRST_BATCH_10_QUEUE.csv',first)
write_csv(OUT/'VOICE_PARAGRAPH_MAP.csv',paras)
write_csv(OUT/'ATTACHED_PACKAGE_SHA256_CHECK.csv',package)

timeline=[]
sentence_indices=[0,2,0,1,3,1,0,2,0,1,2,1,0,0,3,0,2,2,0,1,2,1,2,0,1,0,2,0,1,1,0,1,1,0,0,1,0,1,3,0,1,1,1,0,2,0,0,0,0,1,0,1]
doc_sentence_indices=[2,0,0,0,1,0,0,0,1,0,1,1,2,0]
stop={'the','of','a','an','for','and','in','from','to','with','at','on','as','is','it','that','was','not','no','generic','unbranded','neutral','empty','closeup','macro','wide','real','video','photo'}
def sentence_spans(text):
    return [(m.start()+len(m.group(0))-len(m.group(0).lstrip()),m.end(),m.group(0).strip()) for m in re.finditer(r'[^.!?]+[.!?]?',text) if m.group(0).strip()]
for s in shots:
    p=paras[mapping[s['asset_id']]-1]
    assert int(s['act'])==p['act'],s['asset_id']
    spans=sentence_spans(p['locked_text']);aid=s['asset_id']
    if aid.startswith('GF'):index=min(sentence_indices[int(aid[2:])-1],len(spans)-1)
    elif aid.startswith('DOC'):index=min(doc_sentence_indices[int(aid[3:])-1],len(spans)-1)
    else:
        terms=set(re.findall(r'[a-z]+',s['editorial_cue'].lower()))-stop
        scores=[len(terms & set(re.findall(r'[a-z]+',x[2].lower()))) for x in spans]
        index=max(range(len(spans)),key=lambda k:scores[k])
    a,b,anchor=spans[index]
    exact_overrides={
        'GF033':'The insurance story seems to limit the downside.',
        'GF041':'This was separate from the failed Bahamas festival.',
        'GF044':"The criminal admissions are McFarland's.",
        'GF046':'Money raised, money lost, money ordered forfeited, and money spent on the event are not interchangeable.'}
    if aid in exact_overrides:
        anchor=exact_overrides[aid];a=p['locked_text'].index(anchor);b=a+len(anchor)
    if aid=='GF030':a=spans[1][0];b=spans[3][1];anchor=p['locked_text'][a:b]
    if aid=='GF051':a=0;b=len(p['locked_text']);anchor=p['locked_text']
    before=len(p['locked_text'][:a].split());inside=len(anchor.split())
    begin=round((p['global_word_start']+before)*60/145,3);end=round((p['global_word_start']+before+inside)*60/145,3)
    role='ALTERNATIVE_BROLL_CONTEXT' if s['category']=='STOCK' else 'AUTHENTIC_SOURCE_INSERT' if s['category']=='DOC' else 'FULL_FRAME_EDITOR_NATIVE_REVEAL'
    if aid=='GF029':a=0;b=len(p['locked_text']);anchor=p['locked_text'];begin=p['estimated_start_s'];end=p['estimated_end_s']
    timeline.append({'shot_id':s['shot_id'],'original_inventory_order':int(s['shot_id'][1:]),'editorial_order':0,'act':p['act'],'asset_id':aid,'category':s['category'],'paragraph_id':p['paragraph_id'],'script_anchor_verbatim':anchor,'paragraph_char_start':a,'paragraph_char_end':b,'estimated_start_s':begin,'estimated_end_s':end,'paragraph_estimated_start_s':p['estimated_start_s'],'paragraph_estimated_end_s':p['estimated_end_s'],'timing_status':'ESTIMATED_VERBATIM_SENTENCE_WORD_OFFSET_NOT_MEASURED_AUDIO','estimate_method':'145WPM_WORD_COUNT_NO_AUDIO_PAUSES_UNKNOWN','editorial_purpose':s['editorial_cue'],'layer_or_usage':role,'pacing_instruction':'Use exact anchor order; composited source/graphic reveals and alternative B-roll are not142 forced hard cuts. No factual material may be hidden by overlap.','asset_status':'PENDING_REGISTRY_RECONCILIATION','assembly':'NOT_STARTED'})
timeline.sort(key=lambda r:(int(r['paragraph_id'][1:]),r['paragraph_char_start'],r['original_inventory_order']))
for i,row in enumerate(timeline):row['editorial_order']=i+1
for p in paras:
    choices=[r for r in timeline if r['paragraph_id']==p['paragraph_id'] and r['category']=='STOCK']
    if choices:choices[0]['layer_or_usage']='BASE_BROLL_CONTEXT_CANDIDATE'
for row in timeline:
    p=paras[int(row['paragraph_id'][1:])-1]
    assert p['locked_text'][row['paragraph_char_start']:row['paragraph_char_end']]==row['script_anchor_verbatim']
covered={r['paragraph_id'] for r in timeline}
assert covered=={p['paragraph_id'] for p in paras}
write_csv(OUT/'VISUAL_TIMELINE_V2.csv',timeline)
density=[]
staged={
'P007':('STK0207;GF013','Question about audience; then existing historical-versus-forecast graphic highlights completed-business evidence. Change attention once during the11.6s estimate.'),
'P017':('GF029;GF003;GF021;GF026;GF033','Four named sequential reveals: booking counts, apparent revenue, claimed founder wealth, then protection question. Existing exact-text assets reused after their first introduction, never four simultaneous unreadable cards.'),
'P020':('GF033;GF031;GF032','Upside premise, represented downside protection, then contrast against unexecuted coverage. Three clean settle/read states across the paragraph; no unrelated rain footage.'),
'P021':('GF034;DOC001;STK0608','First investor loss and >80victims; second ticket-vendor loss and not-budget caveat; then short approach-to-event context at the final sentence. Do not hold backstage footage over the financial explanation.'),
'P023':('GF036;DOC009','Logistical failures as generic examples; legal distinction that event failure alone is not fraud; genuine source support for specific financial misrepresentation. No generic newsroom as evidence.'),
'P025':('STK0709;GF038;DOC009;GF039','Short legal-record handling context; recap initial admission; question turns at the final sentence. Do not reveal NYC VIP Access before P026.'),
'P029':('GF044;DOC012;GF041','State that criminal admissions are McFarland\'s only; keep other participants unaccused; separate the two ventures; end on sentencing handoff. Ticketqueue is only an alternative at P026, never the primary fairness-caveat visual.')}
for p in paras:
    rows=[r for r in timeline if r['paragraph_id']==p['paragraph_id']]
    seconds=p['estimated_end_s']-p['estimated_start_s'];seconds_per=seconds/len(rows)
    reuse,decision=staged.get(p['paragraph_id'],('','Use mapped sentence order; select relevant B-roll, give factual qualifiers a readable hold, and interleave authentic proof with native explanation.'))
    density.append({'paragraph_id':p['paragraph_id'],'act':p['act'],'estimated_seconds':round(seconds,3),'positions':len(rows),'if_all_positions_forced_sequential_seconds_each':round(seconds_per,3),'base_candidates':sum(r['category']=='STOCK' for r in rows),'graphic_or_doc_positions':sum(r['category']!='STOCK' for r in rows),'coverage':'PASS_HAS_MAPPED_VISUAL_OPTIONS','pacing_qc':'HOLD_NO_AUDIO_OR_RENDERED_PACING_CHECK','named_existing_reuse_assets':reuse,'decision':decision})
write_csv(OUT/'VISUAL_DENSITY_QC.csv',density)
all_inputs=['05R_SCRIPT_V3_EN.md','05R_SCRIPT_V3_RU.md','07_SCRIPT_LOCK.md','08_VOICE_SCRIPT.md']+[f'08_HARRISON_PART_{i:02}.txt' for i in range(1,6)]
hashes=[{'file':name,'working_tree_sha256':digest(EP/name),'policy':'PRESERVE_UNCHANGED'} for name in all_inputs]
write_csv(OUT/'LOCKED_INPUT_SHA256.csv',hashes)
shutil.copy2(ROOT/'../Downloads/VIDEO009_CODEX_VISUAL_PACKAGE_EXPANDED.zip',OUT/'VIDEO009_CODEX_VISUAL_PACKAGE_EXPANDED.zip')
summary={'source_main_commit':'cc63aa6321e6f509dbc0f9706434aec9b410938a','locked_script_git_blob':blob,'working_tree_crlf_note':'Git canonical LF blob verified; raw Windows working-treeSHA256 separately retained','voice_paragraphs':37,'voice_words':1804,'inventory_positions':142,'gf_prompts_reviewed':52,'doc_positions':14,'stock_positions':76,'all_paragraphs_mapped':True,'estimated_runtime_no_pauses_seconds':round(words*60/145,3),'timestamps':'ALL_ESTIMATED_NO_AUDIO_GENERATED','first_batch_images':10,'first_batch_route':'LOCAL_EDITOR_NATIVE_NO_PAID_IMAGE_MODEL','first_batch_estimated_api_usd':0,'paid_generations_submitted':0,'uncovered_paragraphs':0,'visual_output_qc':'HOLD_PENDING_REAL_FILES_REGISTRIES_AND_INDEPENDENT_REVIEW'}
(OUT/'PREPARATION_CHECKS.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps(summary))
