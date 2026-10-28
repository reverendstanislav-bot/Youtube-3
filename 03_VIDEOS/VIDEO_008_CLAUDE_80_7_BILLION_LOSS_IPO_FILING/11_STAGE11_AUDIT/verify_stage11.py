from pathlib import Path
import csv,json,hashlib,wave,re,io
ROOT=Path(__file__).resolve().parent;EP=ROOT.parent;OUT=ROOT/'VERIFIED';OUT.mkdir(exist_ok=True)
MASTER=EP/'10_AUDIO_MASTER/VIDEO008_HARRISON_V5_MASTER_24K_MONO_S16.wav'
with MASTER.open('rb') as f:sha=hashlib.file_digest(f,'sha256').hexdigest()
assert sha=='5cf8cf37bb728e8a50456b08240824eca4a8d03583626519396eca0258a7ad72'
with wave.open(str(MASTER),'rb') as w:assert (w.getnframes(),w.getframerate(),w.getnchannels(),w.getsampwidth())==(23707200,24000,1,2)
def source(name):return ROOT/name if (ROOT/name).is_file() else EP/name
def rows(name):return list(csv.DictReader(source(name).open(encoding='utf-8-sig',newline='')))
def writecsv(name,data):
 with (OUT/name).open('w',encoding='utf-8',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows(data)
def tc(frame):
 s,f=divmod(frame,25);m,s=divmod(s,60);h,m=divmod(m,60);return f'{h:02}:{m:02}:{s:02}:{f:02}'
data=json.loads(source('11_WORD_LEVEL_TRANSCRIPT.json').read_text());words=data['words'];pars=data['paragraphs']
assert data['runtime_sec']==987.8 and data['total_frames']==24695 and len(pars)==50
assert all(0<=w['start']<=w['end']<=987.8 for w in words)
assert all(a['end']<=b['start']+.0001 for a,b in zip(words,words[1:]))
assert [p['paragraph_id'] for p in pars]==[f'P{i:03}' for i in range(1,51)]
assert pars[0]['start_frame']==0 and pars[-1]['end_frame']==24695
assert all(a['end_frame']==b['start_frame'] for a,b in zip(pars,pars[1:]))
text=source('08_VOICE_SCRIPT_MASTER.txt').read_text();canonical=text.strip().split('\n\n');assert len(canonical)==50 and len(text.split())==2548
mapping=rows('08_VOICE_PARAGRAPH_MAP.csv');assert len(mapping)==50
scenes=rows('11_SCENE_TIMELINE.csv');assert len(scenes)==110
assert [s['scene_id'] for s in scenes]==[f'SC{i:03}' for i in range(1,111)]
assert int(scenes[0]['start_frame_25fps'])==0 and int(scenes[-1]['end_frame_25fps_exclusive'])==24695
assert all(int(a['end_frame_25fps_exclusive'])==int(b['start_frame_25fps']) for a,b in zip(scenes,scenes[1:]))
assert all(int(s['start_frame_25fps'])<int(s['end_frame_25fps_exclusive']) for s in scenes)
for p in pars:
 group=[s for s in scenes if s['paragraph_id']==p['paragraph_id']]
 assert len(group) in [2,3]
 assert int(group[0]['start_frame_25fps'])==p['start_frame'] and int(group[-1]['end_frame_25fps_exclusive'])==p['end_frame']
asrrows=[]
for i,w in enumerate(words):
 center=(w['start']+w['end'])/2
 p=next((p for p in pars if p['start_frame']/25<=center<p['end_frame']/25),pars[-1])
 asrrows.append(dict(word_index=i+1,asr_word=w['word'],start_sec=w['start'],end_sec=w['end'],probability=w.get('probability',''),paragraph_id=p['paragraph_id'],timing_status='ZERO_DURATION_ASR_POINT_REVIEW' if w['start']==w['end'] else 'ASR_TIMING_EVIDENCE',audio_sha256=sha))
writecsv('11_ASR_WORD_TIMINGS.csv',asrrows)
paragraphs=[]
verified_onsets={'P008':133.66,'P032':632.80}
for p,c,m in zip(pars,canonical,mapping):
 assert p['paragraph_id']==m['paragraph_id'] and len(c.split())==int(m['spoken_words'])
 speech_start=verified_onsets.get(p['paragraph_id'],p['start_sec_raw'])
 p['speech_start_sec_verified']=speech_start
 paragraphs.append(dict(paragraph_id=p['paragraph_id'],beat_id=m['beat_id'],segment_id=m['segment_id'],short_id=m['short_id'],locked_narration=c,spoken_whitespace_words=len(c.split()),speech_start_sec=speech_start,speech_end_sec=p['end_sec_raw'],start_frame_25fps=p['start_frame'],end_frame_exclusive_25fps=p['end_frame'],start_timecode=tc(p['start_frame']),end_timecode=tc(p['end_frame']),exact_asr_token_match_ratio=p['match_ratio'],timing_status='ASR_PARAGRAPH_ANCHORED_VISUAL_RANGES_PRESERVED',boundary_note='Visual range is an edit allocation, not a phoneme boundary; use speech_start_sec and Shorts map for audio extraction',semantic_authority='OWNER_ACCEPTED_AUDIO_AND_LOCKED_V5_NOT_ASR'))
writecsv('11_TRANSCRIPT_ASR_ALIGNED.csv',paragraphs)
anchors=[]
for s in scenes:
 start=int(s['start_frame_25fps']);end=int(s['end_frame_25fps_exclusive'])
 w=[x for x in asrrows if x['end_sec']>start/25 and x['start_sec']<end/25]
 anchors.append(dict(scene_id=s['scene_id'],paragraph_id=s['paragraph_id'],start_frame_25fps=start,end_frame_exclusive_25fps=end,start_sec=start/25,end_sec=end/25,first_overlapping_word_index=w[0]['word_index'] if w else '',last_overlapping_word_index=w[-1]['word_index'] if w else '',first_overlapping_asr_word=w[0]['asr_word'] if w else '',last_overlapping_asr_word=w[-1]['asr_word'] if w else '',timing_basis='ASR_PARAGRAPH_ANCHORED_WEIGHTED_SCENE_SPLIT',boundary_precision_note='Scene boundaries preserved; proportional visual planning subdivisions, not independently phoneme-aligned cuts'))
writecsv('11_SCENE_WORD_ANCHORS.csv',anchors)
locks=rows('07_SHORTS_LOCK.csv');cuts=rows('11_SHORTS_CUT_MAP.csv');assert len(locks)==len(cuts)==4
assert [r['paragraph_start'] for r in locks]==['P008','P013','P029','P032']
for lock,cut in zip(locks,cuts):
 assert lock['short_id']==cut['short_id'] and lock['paragraph_start']==cut['paragraph_id']==lock['paragraph_end']
 p=next(p for p in pars if p['paragraph_id']==cut['paragraph_id']);c=canonical[int(p['paragraph_id'][1:])-1]
 assert c==lock['exact_locked_narration']
 original_start=int(cut['start_frame_25fps']);start={'SH01':3334,'SH04':15812}.get(cut['short_id'],original_start);end=int(cut['end_frame_25fps_exclusive']);duration=(end-start)/25
 assert end==p['end_frame'] and start/25<=p['speech_start_sec_verified'] and end/25>=p['end_sec_raw']
 cut.update(start_frame_25fps=str(start),start_timecode=tc(start),duration_sec=f'{duration:.3f}',status='AUDIO_CUT_VERIFIED_CTA_BUDGETED_NOT_RENDERED',duration_verdict='AUDIO_PLUS_PLANNED_CTA_WITHIN_CAP_NOT_A_RENDER_QC',speech_start_sec=str(p['speech_start_sec_verified']),speech_end_sec=str(p['end_sec_raw']),planned_canonical_cta_sec='3.000',planned_complete_export_sec=f'{duration+3:.3f}',remaining_headroom_sec=f'{30-duration-3:.3f}',master_start_sample=str(start*960),master_end_sample_exclusive=str(end*960),source_audio_sha256=sha,rendered_short_duration_sec='',final_9x16_export_qc='NOT_RENDERED_STAGE11_PLANNING_ONLY',cut_start_note='Corrected onset: ASR digit 4 begins133.66s; include complete Four' if cut['short_id']=='SH01' else 'Lead-in before Anthropic onset632.80s' if cut['short_id']=='SH04' else 'Existing cut preserved')
 assert duration+3<=30
writecsv('11_SHORTS_CUT_MAP.csv',cuts)
warnings=[dict(paragraph_id=p['paragraph_id'],exact_token_match_ratio=p['match_ratio'],speech_start_sec=p['start_sec_raw'],speech_end_sec=p['end_sec_raw'],status='ASR_LEXICAL_MISMATCH_REVIEW_NOT_PROVEN_AUDIO_ERROR',note='Owner accepted audio; exact-match score is affected by hyphenation and recognized numeric forms. Do not rewrite narration from ASR.') for p in pars if p['match_ratio']<.85]
writecsv('11_ASR_ALIGNMENT_WARNINGS.csv',warnings)
zero=[r for r in asrrows if r['start_sec']==r['end_sec']]
data.update(audio_sha256=sha,master_sample_rate=24000,master_pcm_samples=23707200,source_github_ref=(ROOT/'SOURCE_REF.txt').read_text().strip() if (ROOT/'SOURCE_REF.txt').exists() else data.get('source_github_ref','REPOSITORY_STAGE11_INPUTS'),stage11_verification='PASS_STRUCTURAL_TIMING_WITH_EXPLICIT_ASR_WARNINGS',word_timing_qualification='Raw ASR timings retained including zero-duration points; no invented word-level acoustic precision or semantic rewrite',zero_duration_asr_word_indices=[r['word_index'] for r in zero])
(OUT/'11_WORD_LEVEL_TRANSCRIPT.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report=dict(status='PASS_STAGE11_TIMING_AUDIT_WITH_ASR_WARNINGS',source_github_ref=data['source_github_ref'],master_sha256=sha,audio_duration_sec=987.8,total_frames_25fps=24695,word_timestamp_count=len(words),word_range_errors=0,word_overlaps=0,zero_duration_asr_points=zero,paragraphs=50,canonical_spoken_whitespace_words=2548,asr_normalized_canonical_tokens=data['canonical_token_count'],exact_asr_match_ratio=data['global_match_ratio'],paragraphs_below_85pct_exact_lexical_match=len(warnings),scenes=110,scene_gaps=0,scene_overlaps=0,scene_and_paragraph_boundaries_changed=False,visual_edit_boundary_caveats=['P008 visual boundary133.76 crosses word4 at133.66-133.96; speech onset and Short cut corrected separately','P049 visual boundary963.60 crosses last20ms of earn ending963.62; visual allocation retained, not an audio trim'],corrected_short_starts={'SH01':dict(original_frame=3344,corrected_frame=3334,reason='Preserve complete first word Four'), 'SH04':dict(original_frame=15820,corrected_frame=15812,reason='Add lead-in before first word Anthropic')},shorts=[dict(short_id=c['short_id'],paragraph_id=c['paragraph_id'],audio_cut_sec=float(c['duration_sec']),planned_cta_sec=3,planned_total_sec=float(c['planned_complete_export_sec']),headroom_sec=float(c['remaining_headroom_sec']),export_status='NOT_RENDERED') for c in cuts],audio_modified=False,new_tts_jobs=0,new_visual_generations=0,resolve_called=False,downstream_state_preserved=True,semantic_pronunciation_review='OWNER_ACCEPTED_NOT_AN_AUTOMATED_SEMANTIC_AUDIT')
(OUT/'11_STAGE11_QC.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2),flush=True)
