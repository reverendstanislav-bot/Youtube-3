#!/usr/bin/env python3
"""VIDEO005 Stage11 deterministic alignment from stage08 text & observed release ASR words.
ASR word times are PROVISIONAL, not manually auditioned or certified subtitles.
Source-only editorial visuals; does not create or license any media.
"""
import csv, difflib, json, math, re, hashlib, pathlib
from collections import defaultdict, Counter
ROOT=pathlib.Path('/home/user/video005_release')
OUT=ROOT/'stage11'
OUT.mkdir(exist_ok=True)
SRC='https://raw.githubusercontent.com/reverendstanislav-bot/Youtube-3/main/03_VIDEOS/VIDEO_005_THE_ENGINEER_WHO_TOOK_14_000_FILES_FROM_GOOGLE/'
def load(n):
    f=ROOT/n
    assert f.exists(),n
    return f.read_text(encoding='utf-8-sig')
def save(n,s):
    (OUT/n).write_text(s,encoding='utf8')
def jsonsave(n,o):save(n,json.dumps(o,ensure_ascii=False,indent=2)+'\n')
def csvsave(n,rs,keys=None):
    assert rs, n
    keys=keys or list(rs[0])
    with (OUT/n).open('w',encoding='utf8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(rs)
def timefmt(t):
    m,s=divmod(max(0,t),60)
    return f'{int(m):02d}:{s:06.3f}'
def srtfmt(t):
    s=max(0,t);h=int(s//3600);m=int((s-h*3600)//60);return f'{h:02d}:{m:02d}:{int(s%60):02d},{int(round((s%1)*1000)):03d}'.replace(',1000',',999')
def toks(t):
    return re.findall(r"[a-z]+|\d+",t.lower().replace("’","'"))
with open(ROOT/'stage10_build_manifest.json') as f:build=json.load(f)
assert abs(build["output_duration_seconds"]-995.03)<.001
parts=load('expected_master.txt').strip().split('\n\n')
expectedIds=[]
script=load('stage11_locked_script.md')
matches=list(re.finditer(r'\*\*(A\d\d-P\d\d)\*\*\s*\n+([\s\S]*?)(?=\n\*\*A\d\d-P\d\d\*\*|\n## A\d\d |\n---|$)',script))
assert len(matches)==len(parts)==55,('script paragraphs',len(matches),'voice paragraphs',len(parts))
paras=[{'id':m[1],'locked_text':' '.join(m[2].split()),'tts_text':t,'act':m[1][:3],'words_original':len(m[2].split()),'words_tts':len(t.split())} for m,t in zip(matches,parts)]
assert sum(p['words_original'] for p in paras)==2551
assert sum(p['words_tts'] for p in paras)==2627
expectedByChunk=[10,12,11,11,11];assert sum(expectedByChunk)==55
assert [len([p for p in paras if p['act'] in (f'A{i:02d}',f'A{i+1:02d}')]) for i in range(0,10,2)]==expectedByChunk

visuals=[
# A00 five
("HOOK / 14K & PERSONAL JUDGMENT","Editorial identity/title beside attributed federal case figure; contrast Google file count with PERSONALLY OWED, no false conviction image","EDITOR_GRAPHIC"),
("TWO CORPORATE PAYMENTS","Split 2018 Uber shares settlement and 2022 sealed Google transfer as two legally separate events","EDITOR_GRAPHIC"),
("DECISION ROADMAP","Three grounded case milestones: predeal forensic report, disputed risk-sharing clause, wrongly sent drawing","EDITOR_GRAPHIC"),
("BURDEN OF PROOF","Evidence-versus-allegation typography: copied files are not a verdict of Uber product use","EDITOR_GRAPHIC"),
("PRE-DOWNLOAD ORIGIN","December 2015 Google autonomous-driving lab context; no fabricated room or witness footage","REAL_CONTEXT"),
# A01 five
("LIDAR FUNCTION","Neutral LiDAR range-sensing explanatory wireframe, without copying protected design","EDITOR_GRAPHIC"),
("INTERNAL DOWNLOAD DATE","Verified court/DOJ document callout: December 11, 2015 and internal repository; never forge a Google login screenshot","AUTHENTIC_DOCUMENT"),
("COPY IS NOT USE","Count 14,000 copied project files vs separate unproved Uber use; two-column evidentiary comparison","EDITOR_GRAPHIC"),
("OTTO FOUNDING","January 2016 Otto founding then Levandowski leaves Google Jan 27; historically grounded dates on simple timeline","EDITOR_GRAPHIC"),
("ACQUISITION PRICE OPEN LOOP","Up to $680M conditional headline in acquisition context; defer $100K contrast to next section","EDITOR_GRAPHIC"),
# A02 six
("EARLY DEAL TERMS","February 2016 agreement timeline alongside authenticated transaction summary source","AUTHENTIC_DOCUMENT"),
("POSSIBLE VALUE QUALIFIER","Up to $680M, conditional, not payout card; restraint before reveal","EDITOR_GRAPHIC"),
("100K CASH REVEAL","$100,000 initial cash against up-to-$680M contingent acquisition maximum; Delaware record evidence label","EDITOR_GRAPHIC"),
("FUTURE VALUE VS PAST RISK","Business purchase forward-looking opportunity versus preexisting employee obligations in separate lanes","EDITOR_GRAPHIC"),
("INDEMNITY AGREEMENT","Authentic 2016 indemnification references, conditional terms circled only when verified","AUTHENTIC_DOCUMENT"),
("PRE-CLOSE FORENSIC MANDATE","Stroz Friedberg inquiry anchored to dated court-source description; no fabricated investigator workstation","AUTHENTIC_DOCUMENT"),
# A03 six
("STROZ EXAMINATION","Qualified source text: device investigation and potential Google material, no unverifiable screen recreation","AUTHENTIC_DOCUMENT"),
("SHAREHOLDER ALLEGATION","Clearly labeled lawsuit allegation vs proven finding, with original pleadings quotation only","AUTHENTIC_DOCUMENT"),
("BOARD RISK DECISION","Buyer benefit/risk ledger with no imagined private board minutes","EDITOR_GRAPHIC"),
("LIMITED FORENSIC FINDING","Quote real Stroz finding narrowed to Levandowski-held information, not universal exoneration","AUTHENTIC_DOCUMENT"),
("ACQUISITION CLOSE","August 2016 chronology card for Otto/Uber transaction, source-backed","EDITOR_GRAPHIC"),
("MISDELIVERED MATERIAL TEASE","Abstract technical envelope addressed to wrong recipient; do not depict invented drawing or claim proof","EDITOR_GRAPHIC"),
# A04 five
("SUPPLIER EMAIL REVEAL","Gorilla Circuits misaddressed PCB drawings December 2016, use authentic source not generated screenshot","AUTHENTIC_DOCUMENT"),
("TWO EVIDENCE STREAMS","Separate recovered download record and delivered circuit drawings as unrelated evidentiary pieces","EDITOR_GRAPHIC"),
("LAWSUIT TRIGGER","December 2016 mistaken email -> February 2017 lawsuit, allegedly similar drawings clearly attributed","EDITOR_GRAPHIC"),
("WAYMO V UBER COMPLAINT","Court complaint crop with ALLEGED label and opponent's denial; no invented allegation as judicial fact","AUTHENTIC_DOCUMENT"),
("MAY 2017 PRELIMINARY ORDER","Narrow preliminary injunction language from Judge Alsup with provisional tag","AUTHENTIC_DOCUMENT"),
# A05 six
("FIVE DISKS ACCOUNT","Five alleged disks in court record with SOURCE ATTRIBUTION, contents UNKNOWN; no fictional disk photo labeled real","EDITOR_GRAPHIC"),
("DISCLOSURE DELAY","When Uber knew versus when disclosed, marked as timeline interval not theft proof","EDITOR_GRAPHIC"),
("JUROR INFERENCE QUESTION","Decision tree judge could allow juror inference, not predetermined conclusion","EDITOR_GRAPHIC"),
("PERMISSIVE COURT ORDER","Original January 2018 judicial language MAY NOT MUST; source crop when available","AUTHENTIC_DOCUMENT"),
("NO AUTOMATIC VERDICT","Credibility matter separated from proof, restrained text editorial graphic","EDITOR_GRAPHIC"),
("TRIAL BEFORE SETTLEMENT","February 2018 start-and-stop trial marker, no invented jury verdict images","EDITOR_GRAPHIC"),
# A06 five
("WAYMO UBER DISMISSAL","February 9 2018 dismissal with prejudice, authentic signed case record","AUTHENTIC_DOCUMENT"),
("245M IN SHARES","~$245M 2018 Uber stock deal, NOT cash fine/jury damages; distinct from Google civil judgment","EDITOR_GRAPHIC"),
("UBER RESPONSE","Reported Uber leadership statement only as attributed, not court fact","AUTHENTIC_DOCUMENT"),
("GOOGLE EMPLOYMENT CASE","Two case files side by side: separate Google v Levandowski employment arbitration vs Waymo v Uber","EDITOR_GRAPHIC"),
("INDEMNITY RISK QUESTION","2016 contractual risk allocation reappears for Levandowski's own dispute","EDITOR_GRAPHIC"),
# A07 six
("ARBITRATION AWARD","Google/Levandowski employment arbitration confirmed by court; focus on separate litigant","AUTHENTIC_DOCUMENT"),
("179047998 PERSONAL JUDGMENT","Exact $179,047,998.64 personal civil judgment and Chapter 11 hours later; original order","AUTHENTIC_DOCUMENT"),
("CRIMINAL TRACK SEPARATION","33 federal charges vs single guilty plea, separate federal case documents not combined with civil order","EDITOR_GRAPHIC"),
("2020 SENTENCE 2021 PARDON","Documented criminal sentence then presidential pardon; show no civil-debt forgiveness","AUTHENTIC_DOCUMENT"),
("CONTESTED INDEMNITY","Levandowski claim versus Uber contested coverage, attributed legal positions","EDITOR_GRAPHIC"),
("WHO BEARS THE COST","Unresolved pre-2022 cost question, with 2018 Waymo settlement clearly closed","EDITOR_GRAPHIC"),
# A08 six
("2016 AGREEMENT DISPUTE","Personal liability and disputed indemnity, NO judgment compelling Uber payment","EDITOR_GRAPHIC"),
("NEW 2022 SETTLEMENT","New multi-party Global Settlement, distinct from 2016 contract, real court filing as source","AUTHENTIC_DOCUMENT"),
("NEGOTIATED PAYMENT BASIS","Flow Uber to Google labelled separate 2022 obligations, not second Waymo verdict","EDITOR_GRAPHIC"),
("SEALED SECOND PAYMENT","SEALED main sum shown as undisclosed; separate $2m plan support, NEVER invent dollar value","EDITOR_GRAPHIC"),
("BANKRUPTCY OPINION PROOF","Jan 2025 court source: paid under 2022 Global Settlement NOT old indemnification","AUTHENTIC_DOCUMENT"),
("TAX TREATMENT OPEN LOOP","Money-transfer mechanism to tax treatment question, avoid alleged final tax amount","EDITOR_GRAPHIC"),
# A09 five
("2025 GROSS INCOME RULING","Jan 2025 court holding of gross income to Levandowski, no final tax bill","AUTHENTIC_DOCUMENT"),
("AFTERLIFE","2022 settlement then 2025 tax interpretation, separate from settled 2018 suit","EDITOR_GRAPHIC"),
("SETTLEMENT VALIDITY","Court's explicit scope: tax treatment does not invalidate settlement; principal still sealed","AUTHENTIC_DOCUMENT"),
("EVIDENCE CHAIN","Decision logic: downloaded files -> vetted acquisition -> personal award -> new settlement, not one case verdict","EDITOR_GRAPHIC"),
("FINAL CONCRETE COST","Documented two separate settlements and unresolved sealed amount, then clean ending without new claims","EDITOR_GRAPHIC")
]
assert len(visuals)==55,len(visuals)

sourceRows=list(csv.DictReader(load('stage11_source_trace.csv').splitlines()))
sources={r['paragraph_id']:r for r in sourceRows}
assert len(sourceRows)==55 and all(p['id'] in sources for p in paras)

all_words=[];align_reports=[];visual_qc=[]
master_offsets=build['per_chunk_start_seconds']
exact_all=0;recog_count=0;flagged_paras=[]
k=0
for chunk_i,chunk_len in enumerate(expectedByChunk,1):
    local=paras[k:k+chunk_len];k+=chunk_len
    observations=json.loads(load(f'chunk_{chunk_i:02d}_timestamped.json'))
    observed=[];obs_t=[]
    for segment in observations:
        for ow in segment.get('words',[]):
            tt=toks(ow['w'])
            for t in tt:
                observed.append(t)
                obs_t.append((float(ow['s']),float(ow['e']),ow['w']))
    expected=[];ids=[];wordlist=[]
    for p in local:
        for j,w in enumerate(p['tts_text'].split()):
            token_indexes=toks(w)
            if not token_indexes: continue
            wi=len(wordlist)
            wordlist.append({'pid':p['id'],'local_idx':j,'spoken_token':w,'expected_tokens':token_indexes})
            for t in token_indexes:
                expected.append(t);ids.append(wi)
    match=difflib.SequenceMatcher(None,expected,observed,autojunk=False)
    mapped={}
    for op,a1,a2,b1,b2 in match.get_opcodes():
        if op=='equal':
            for i in range(a2-a1):mapped[a1+i]=b1+i
    exact_all+=len(mapped);recog_count+=len(expected)
    wmatch=defaultdict(list)
    for i,obs_i in mapped.items():wmatch[ids[i]].append(obs_i)
    known={}
    for idx,items in wmatch.items():
        known[idx]=(min(obs_t[i][0] for i in items),max(obs_t[i][1] for i in items))
    approx_s, approx_e=build['per_chunk_start_seconds'][chunk_i-1], None
    end_bound=(build['per_chunk_start_seconds'][chunk_i]-.120) if chunk_i<5 else build['output_duration_seconds']
    chunk_duration=end_bound-approx_s
    indices=sorted(known)
    unknown_runs=[]
    for wi,w in enumerate(wordlist):
        if wi in known: s,e=known[wi];status='ASR_EXACT_TOKEN_ANCHOR'
        else:
            left=max((v for v in indices if v<wi),default=None)
            right=min((v for v in indices if v>wi),default=None)
            if left is None and right is None:raise RuntimeError('unanchored entire chunk')
            if left is None:
                available=max(0,known[right][0]);start=0
                s=available*wi/right;e=available*(wi+1)/right
            elif right is None:
                avail=max(0,chunk_duration-known[left][1]);n=len(wordlist)-left-1
                s=known[left][1]+avail*(wi-left-1)/n;e=known[left][1]+avail*(wi-left)/n
            else:
                a=known[left][1];b=known[right][0]
                span=max(0,b-a);n=right-left-1
                s=a+span*(wi-left-1)/n;e=a+span*(wi-left)/n
            status='ASR_INTERPOLATED_UNMATCHED_TOKEN'
        s=max(0,s);e=max(s,e)
        p_off=master_offsets[chunk_i-1]
        all_words.append({'word_id':len(all_words)+1,'paragraph_id':w['pid'],'act':w['pid'][:3],
              'word_index_in_paragraph':w['local_idx']+1,'spoken_token':w['spoken_token'],
              'start_sec':round(s+p_off,3),'end_sec':round(e+p_off,3),
              'duration_sec':round(e-s,3),'source_chunk':chunk_i,
              'timestamp_status':status,'observed_token_match_count':len(wmatch.get(wi,[]))})
    matched_count=len(mapped);alignment_ratio=round(matched_count/len(expected),4)
    align_reports.append({'chunk':chunk_i,'paragraphs':len(local),'spoken_words':len(wordlist),
                          'script_lexical_tokens':len(expected),'recognized_lexical_tokens':len(observed),
                          'exact_token_matches':matched_count,'script_exact_match_fraction':alignment_ratio,
                          'nonexact_tokens':len(expected)-matched_count,'source_start_sec':round(approx_s,3),
                          'source_end_sec':round(end_bound,3),
                          'note':'ASR forced-word timestamps; unmatched script words interpolated and explicitly flagged'})

assert len(all_words)==2627,(len(all_words),2627)
byPara=defaultdict(list)
for w in all_words:byPara[w['paragraph_id']].append(w)
assert len(byPara)==55
masters=[]
for i,p in enumerate(paras):
    ww=byPara[p['id']]
    anchor=[w for w in ww if w['timestamp_status']=='ASR_EXACT_TOKEN_ANCHOR']
    if not anchor:raise RuntimeError('No exact matching tokens for paragraph '+p['id'])
    raw_start=anchor[0]['start_sec'];raw_end=anchor[-1]['end_sec']
    matched=len(anchor);ratio=round(matched/len(ww),3)
    first=ww[0]['timestamp_status']=='ASR_EXACT_TOKEN_ANCHOR'
    last=ww[-1]['timestamp_status']=='ASR_EXACT_TOKEN_ANCHOR'
    status='ASR_ANCHORED_PROVISIONAL' if ratio>=.75 and first and last else 'ASR_REVIEW_BOUNDARIES'
    p.update({'paragraph_index':i+1,'tts_word_count':len(ww),'first_word_est_sec':raw_start,
      'last_word_est_sec':raw_end,'anchored_words':matched,'anchored_ratio':ratio,
      'first_word_anchored':first,'last_word_anchored':last,
      'alignment_status':status,'visual_title':visuals[i][0],
      'visual_plan':visuals[i][1],'visual_evidence_class_proposal':visuals[i][2],
      'source_ids':sources[p['id']]['source_family_from_G04'],
      'claim_ids':sources[p['id']]['claim_ids'],
      'short_id':sources[p['id']]['short_id'] or ''})
    if status!='ASR_ANCHORED_PROVISIONAL':flagged_paras.append(p['id'])
    
# Frame-exact contiguous scene coverage from center of inter-paragraph gaps.
fps=25;frames=int(math.ceil(build['output_duration_seconds']*fps))
bounds=[0]
for i in range(len(paras)-1):
    left=paras[i]['last_word_est_sec'];right=paras[i+1]['first_word_est_sec']
    if right<left:
        # unexpected but still produce contiguous boundaries, flagged
        cut=left
    else:cut=(left+right)/2
    bounds.append(round(cut*fps))
bounds.append(frames)
assert len(bounds)==56 and all(x<y for x,y in zip(bounds,bounds[1:])),bounds
timelines=[];srt=[]
for i,p in enumerate(paras):
    p['scene_id']=f'SC{i+1:03d}'
    p['start_frame']=bounds[i];p['end_frame_exclusive']=bounds[i+1]
    p['scene_start_sec']=round(bounds[i]/fps,3);p['scene_end_sec']=round(bounds[i+1]/fps,3)
    p['scene_duration_sec']=round((bounds[i+1]-bounds[i])/fps,3)
    p['semantic_scene']={'narration':p['id'],'not_a_mandatory_picture_cut':True}
    timelines.append({'scene_id':p['scene_id'],'start_frame':bounds[i],'end_frame_exclusive':bounds[i+1],
      'start_sec':p['scene_start_sec'],'end_sec':p['scene_end_sec'],'duration_sec':p['scene_duration_sec'],
      'act':p['act'],'paragraph_id':p['id'],'short_id':p['short_id'],
      'editorial_role':p['visual_title'],'narration_locked_text':p['locked_text'],
      'visual_intent':p['visual_plan'],'proposed_source_class':p['visual_evidence_class_proposal'],
      'evidence_source_ids':p['source_ids'],'claim_ids':p['claim_ids'],
      'speech_start_anchor':p['first_word_est_sec'],'speech_end_anchor':p['last_word_est_sec'],
      'spoken_words':p['tts_word_count'],'asr_match_fraction':p['anchored_ratio'],
      'alignment_status':p['alignment_status'],
      'editor_notes':'Semantic cue span; split/hold at Stage12/15 as appropriate; no asset existence/rights implied'})
    srt.extend([str(i+1),f"{srtfmt(p['scene_start_sec'])} --> {srtfmt(min(p['scene_end_sec'],995.03))}",p['locked_text'],''])
assert timelines[0]['start_frame']==0 and timelines[-1]['end_frame_exclusive']==24876
assert sum(x['end_frame_exclusive']-x['start_frame'] for x in timelines)==24876
assert all(timelines[i]['end_frame_exclusive']==timelines[i+1]['start_frame'] for i in range(54))
shorts=[]
short_ids={'S01':'A00-P01','S03':'A02-P03','S05':'A04-P03','S08':'A08-P04'}
shortTitles={'S01':'THE ENGINEER OWED $179M','S03':'$680M? ONLY $100K CASH','S05':'ONE WRONG EMAIL','S08':'UBER PAID AGAIN — AMOUNT SEALED'}
shortsMatch=[]
for name,pid in short_ids.items():
    p=next(x for x in paras if x['id']==pid)
    w=byPara[pid]
    # use first/last word anchors, conservatively add <=0.08s before and 0.12s after; avoid adjacent paragraph.
    ix=paras.index(p)
    prevlast=paras[ix-1]['last_word_est_sec'] if ix>0 else 0
    nxtfirst=paras[ix+1]['first_word_est_sec'] if ix<54 else 995.03
    in_s=max(prevlast+0.005 if ix>0 else 0,p['first_word_est_sec']-.06)
    out_s=min(nxtfirst-.005 if ix<54 else 995.03,p['last_word_est_sec']+.12)
    # round to in 25fps frames with outward slight margin, but no adjacent words
    in_frame=max(0,math.floor(in_s*fps))
    out_frame=min(frames,math.ceil(out_s*fps))
    cut_len=(out_frame-in_frame)/fps
    needs_review=('ASR_REVIEW_BOUNDARIES'==p['alignment_status']) or (not p['first_word_anchored']) or (not p['last_word_anchored'])
    shorts.append({
      'short_id':name,'status':'PROVISIONAL_ASR_CUT_NOT_EXPORTED','working_title':shortTitles[name],
      'start_timecode':timefmt(in_frame/fps),'end_timecode':timefmt(out_frame/fps),
      'duration_sec':round(cut_len,3),'section_range':p['act'],
      'beat_ids':p['scene_id'],'gfx_ids':'','claim_ids':p['claim_ids'],
      'hook':shortTitles[name],'payoff':p['locked_text'].split('.')[-2].strip() if '.' in p['locked_text'] else '',
      'first_line':p['locked_text'].split('.')[0]+'.','last_line':p['locked_text'].split('.')[-2].strip()+'.',
      'extraction_rule':'ONE_CONTIGUOUS_ORIGINAL_LONGFORM_PARAGRAPH_NO_ALT_TTS',
      'audio_source':'VIDEO005_HARRISON_QWEN06_STAGE10_AUDIO_MASTER_48K_MONO.wav',
      'vertical_rule':'SAME_AUDIO_SOURCE_9X16_REFRAME_OR_EDITOR_ALT_LAYOUT_NO_BURNED_CAPTIONS',
      'legal_review':'G04_V4_4_ISOLATED_TEXT_PASS',
      'start_sec':round(in_frame/fps,3),'end_sec':round(out_frame/fps,3),
      'speech_start_sec':p['first_word_est_sec'],'speech_end_sec':p['last_word_est_sec'],
      'cta_sec':3,'planned_total_sec':round(cut_len+3,3),
      'scene_ids':p['scene_id'],'export_measured':'NO',
      'match_fraction':p['anchored_ratio'],
      'boundary_qc':'REQUIRES_MANUAL_AUDITION' if needs_review else 'ASR_PROVISIONAL_BOUNDARIES_REQUIRE_LISTEN',
      'source_paragraph_id':pid})
    shortsMatch.append((name,p['anchored_ratio'],in_s,out_s,cut_len))
assert len(shorts)==4
assert all(s['planned_total_sec']<=30.0 for s in shorts)

act_timeline=[]
for i in range(10):
    pp=[x for x in paras if x['act']==f'A{i:02d}']
    act_timeline.append({'act':f'A{i:02d}','start_sec':pp[0]['scene_start_sec'],
       'end_sec':pp[-1]['scene_end_sec'],'paragraphs':len(pp),
       'narration_words':sum(x['tts_word_count'] for x in pp),
       'story_function':pp[0]['visual_title']+' → '+pp[-1]['visual_title']})
qc={'source_master_sha256':'0db92584d7eddd70914b800cb981250463d222cc4db1245444a8153c782847a0',
    'actual_master_duration_sec':995.03,'video_timeline_fps':25,'end_frame_exclusive':24876,
    'render_video_runtime_sec':24876/25,'audio_tail_padding_on_video_sec':round(24876/25-995.03,3),
    'script_paragraphs':len(paras),'scene_rows':len(timelines),'act_rows':len(act_timeline),
    'word_rows':len(all_words),'word_exact_asr_anchors':sum(w['timestamp_status']=='ASR_EXACT_TOKEN_ANCHOR' for w in all_words),
    'word_interpolated_unmatched':sum(w['timestamp_status']!='ASR_EXACT_TOKEN_ANCHOR' for w in all_words),
    'paragraphs_requiring_boundary_review':flagged_paras,
    'contiguous_timeline_0_995_04sec':True,
    'no_overlapping_scene_frames':True,'four_owner_shorts_only':list(short_ids),
    'shorts_provisional':shortsMatch,
    'timings_are_not_hand_listened':True,
    'captions_status':'DRAFT_PARAGRAPH_SRT_NOT_WORD_ACCURATE',
    'stage12_source_permissions':'NOT_REVIEWED',
    'stage15_final_short_under_30s':'NOT_YET_EXPORTED_OR_MEASURED',
    'chunk_alignment':align_reports,
    'generation_spend':'NONE'}

csvsave('11_WORD_TRANSCRIPT.csv',all_words)
jsonsave('11_WORD_LEVEL_TRANSCRIPT.json',all_words)
jsonsave('11_PARAGRAPH_ALIGNMENT.json',paras)
csvsave('11_VISUAL_TIMELINE.csv',timelines)
csvsave('11_SHORTS_CUT_MAP.csv',shorts)
csvsave('11_ACT_TIMELINE.csv',act_timeline)
jsonsave('11_ALIGNMENT_QC.json',qc)
save('11_CAPTIONS_DRAFT.srt','\n'.join(srt))
print('QC',json.dumps({k:v for k,v in qc.items() if k!='chunk_alignment'},indent=2))
print('FILES',[(p.name,p.stat().st_size) for p in OUT.iterdir()])


# Picture placement planning only, never falsely claiming downloaded/document-cleared images.
visual_placements=[]
for i,p in enumerate(paras):
    t0,t1=p['scene_start_sec'],p['scene_end_sec']
    sframe,eframe=p['start_frame'],p['end_frame_exclusive']
    words=byPara[p['id']]
    # Two distinct ideas per ~18s source paragraph; use nearest sentence ending to midpoint.
    sentence_ends=[m.end() for m in re.finditer(r'(?<=[.!?])\s+',p['locked_text'])]
    cand=[]
    if sentence_ends:
        for endchr in sentence_ends:
            proportion=endchr/max(1,len(p['locked_text']))
            if .28<proportion<.72:
                cand.append(proportion)
    ratio=min(cand,key=lambda x:abs(x-.5)) if cand else .5
    midframe=round(sframe+(eframe-sframe)*ratio)
    midframe=max(sframe+round(3*fps),min(eframe-round(3*fps),midframe))
    if not(sframe<midframe<eframe):raise RuntimeError('Not enough scene length for visual placements '+p['id'])
    typ=p['visual_evidence_class_proposal']
    alternatives={
      'AUTHENTIC_DOCUMENT':(
          'Verified authentic original document/court page showing date/party/docket; no synthesized source text',
          'Different relevant authentic paragraph/crop, carefully underlined to reveal legal qualification; verify exact crop in Stage12'),
      'EDITOR_GRAPHIC':(
          'Editorial original full-frame evidence-first number or case setup, qualified and source-backed',
          'Distinct counterpoint/outcome graphic with attribution and caveat; not repeated numerical title card'),
      'REAL_CONTEXT':(
          'Historically relevant documented CC0/PD context image, source and license verification required',
          'Independent diagram/graphic to clarify the story, not an invented witness-scene reconstruction')}
    ap=alternatives[typ]
    for slot,(a,b,desc,role) in enumerate([(sframe,midframe,ap[0],'ESTABLISH'),
                                             (midframe,eframe,ap[1],'PAYOFF_OR_QUALIFICATION')],1):
        visual_placements.append({
          'placement_id':f'VP{len(visual_placements)+1:03d}',
          'scene_id':p['scene_id'],'paragraph_id':p['id'],'act':p['act'],'short_id':p['short_id'],
          'start_frame':a,'end_frame_exclusive':b,'start_sec':round(a/fps,3),
          'end_sec':round(b/fps,3),'duration_sec':round((b-a)/fps,3),
          'slot_role':role,'paragraph_editorial_role':p['visual_title'],
          'picture_direction':p['visual_plan']+' | '+desc,
          'suggested_source_class':typ,
          'source_ids_to_verify':p['source_ids'],'claim_ids':p['claim_ids'],
          'asset_locked_or_existing':'NO_STAGE12_MUST_VERIFY',
          'motion_note':'STATIC_OR_SUBTLE_EDITORIAL_DETAIL_ONLY_NO_SHAKE_NO_JUMPY_CROP; NO_BURNED_SPEECH_CAPTIONS'})
assert len(visual_placements)==110
assert visual_placements[0]['start_frame']==0 and visual_placements[-1]['end_frame_exclusive']==24876
assert all(x['end_frame_exclusive']==y['start_frame'] for x,y in zip(visual_placements,visual_placements[1:]))
csvsave('11_VISUAL_PLACEMENTS_DRAFT.csv',visual_placements)
qc['editorial_visual_placements_planned']=110
qc['picture_placements_full_coverage_25fps']=True
jsonsave('11_ALIGNMENT_QC.json',qc)
print('ADDITIONAL_PLACEMENTS',len(visual_placements),'ALL_55_X_2','FULL_TIMELINE_FRAMES',sum(p['end_frame_exclusive']-p['start_frame'] for p in visual_placements))

