from pathlib import Path
import urllib.request,json,hashlib,datetime
ROOT=Path(__file__).resolve().parent;EP=ROOT.parent
API='http://127.0.0.1:17493';PROFILE='228d3d8a-096f-461b-bf11-4f9415e2dafc'
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def api(path,payload=None):
 req=urllib.request.Request(API+path,data=None if payload is None else json.dumps(payload).encode(),headers={'Content-Type':'application/json'})
 with urllib.request.urlopen(req,timeout=150) as r:
  raw=r.read()
 try:return json.loads(raw)
 except (ValueError,UnicodeDecodeError):
  for line in raw.decode().splitlines():
   if line.startswith('data:'):
    value=json.loads(line[5:].strip())
    if isinstance(value,dict) and ('id' in value or 'error' in value):return value
  raise RuntimeError('Unknown response; do not resubmit, inspect Voicebox history')
def blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def save(state):
 p=ROOT/'GENERATION_QUEUE.json';tmp=p.with_suffix('.tmp');tmp.write_text(json.dumps(state,indent=2)+'\n');tmp.replace(p)
master=(EP/'08_VOICE_SCRIPT_MASTER.txt').read_bytes();assert blob(master)=='c3269a579798b78578d8f57fd77df964c8c352ba'
texts=[(EP/f'08_VOICE_SEGMENT_0{i}.txt').read_text(encoding='utf-8') for i in range(1,6)]
assert '\n\n'.join(t.rstrip() for t in texts)+'\n'==master.decode()
assert [len(t.split()) for t in texts]==[489,535,543,552,429]
profile=api('/profiles/'+PROFILE);assert profile['name']=='Harrison' and profile['voice_type']=='cloned'
health=api('/health');assert health['gpu_available']
statefile=ROOT/'GENERATION_QUEUE.json'
state=json.loads(statefile.read_text()) if statefile.exists() else dict(video_id='008',stage='09_VOICE_QA',state='OWNER_APPROVED_QUEUE_SUBMISSION',authorization='Owner explicitly said запускай after Voicebox Harrison/Qwen3-TTS1.7B five-job zero-credit plan; then requested enqueue all and stop monitoring.',approved_jobs=5,engine='qwen',model='Qwen/Qwen3-TTS-12Hz-1.7B-Base',profile_id=PROFILE,profile_name='Harrison',identity_provenance='Existing local clone from clean Video 4 narration; not a direct Higgsfield preset invocation',credits_spent=0,api_spend_usd=0,source_master_git_blob=blob(master),started_utc=now(),jobs=[])
for i,text in enumerate(texts,1):
 existing=next((x for x in state['jobs'] if x['segment']==i),None)
 if existing:
  if existing.get('generation_id'):continue
  raise RuntimeError('Uncertain prior submission: inspect Voicebox history before retry')
 payload=dict(profile_id=PROFILE,text=text,language='en',model_size='1.7B',engine='qwen',seed=20261027,personality=False,normalize=False,crossfade_ms=50,max_chunk_chars=800,effects_chain=[],instruct='Calm, measured American English business documentary narration. Composed delivery, clear articulation, restrained emphasis and natural pauses. No announcer hype, excessive emotion or theatrical pauses.')
 record=dict(segment=i,input_file=f'08_VOICE_SEGMENT_0{i}.txt',input_git_blob=blob(text.encode()),input_sha256=hashlib.sha256(text.encode()).hexdigest(),words=len(text.split()),characters=len(text),status='SUBMITTING_DO_NOT_RETRY',submitted_utc=now())
 state['jobs'].append(record);save(state)
 (ROOT/f'REQUEST_0{i}.json').write_text(json.dumps(payload,indent=2)+'\n')
 print('SUBMIT',i,flush=True)
 result=api('/generate',payload)
 if not result.get('id'):raise RuntimeError('Missing generation ID; submission outcome uncertain: '+str(result))
 record.update(generation_id=result['id'],status=result.get('status','submitted'),response_utc=now())
 save(state);print('QUEUED',i,result['id'],record['status'],flush=True)
state.update(state='FIVE_JOBS_SUBMITTED_STOPPED_MONITORING_PER_OWNER',submitted_count=len(state['jobs']),queue_submission_finished_utc=now(),qc_status='NOT_RUN_GENERATION_PENDING',stage09_pass=False,stage10_started=False)
save(state);print(json.dumps(state,indent=2),flush=True)
