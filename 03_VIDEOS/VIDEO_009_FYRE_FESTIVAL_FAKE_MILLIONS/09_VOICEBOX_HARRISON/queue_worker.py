"""Five approved local jobs, one at a time. SSE completion events; no status-poll loop or retries."""
from pathlib import Path
import datetime,hashlib,json,os,re,sqlite3,sys,urllib.parse,urllib.request
sys.stdout.reconfigure(encoding='utf-8')
EP=Path(r'C:\Users\KK\Youtube-3-video009-visual-v2\03_VIDEOS\VIDEO_009_FYRE_FESTIVAL_FAKE_MILLIONS')
ROOT=EP/'09_VOICEBOX_HARRISON';ROOT.mkdir(exist_ok=True)
API='http://127.0.0.1:17493';PROFILE='228d3d8a-096f-461b-bf11-4f9415e2dafc'
STATE=ROOT/'GENERATION_QUEUE.json'
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(state):
    state['updated_utc']=now();tmp=STATE.with_suffix('.tmp');tmp.write_text(json.dumps(state,indent=2)+'\n',encoding='utf-8');tmp.replace(STATE)
def api(path,payload=None):
    req=urllib.request.Request(API+path,data=json.dumps(payload).encode() if payload is not None else None,headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(req,timeout=150) as response:raw=response.read()
    try:return json.loads(raw)
    except (ValueError,UnicodeDecodeError):
        for line in raw.decode().splitlines():
            if line.startswith('data:'):
                value=json.loads(line[5:].strip())
                if isinstance(value,dict) and ('id' in value or 'error' in value):return value
        raise RuntimeError('Unknown submission response; stop without resubmitting')
def wait_sse(generation_id):
    req=urllib.request.Request(API+'/generate/'+generation_id+'/status',headers={'Accept':'text/event-stream'})
    with urllib.request.urlopen(req,timeout=300) as response:
        assert 'text/event-stream' in response.headers.get('Content-Type','')
        for raw in response:
            line=raw.decode('utf-8').strip()
            if not line.startswith('data:'):continue
            event=json.loads(line[5:].strip());status=event.get('status')
            if status=='completed':return event
            if status in ('failed','error','cancelled','canceled') or event.get('error'):
                raise RuntimeError('Terminal failure; no retry: '+str(event))
    raise RuntimeError('Status event stream ended without confirmed completion; no retry or next job')
def normalize(text):return ' '.join(text.split())

texts=[(EP/f'08_HARRISON_PART_{i:02}.txt').read_text(encoding='utf-8-sig') for i in range(1,6)]
master=' '.join(x.strip() for x in re.split(r'\n\s*\n',(EP/'08_VOICE_SCRIPT.md').read_text(encoding='utf-8-sig')) if x.strip() and not x.strip().startswith('#'))
assert normalize(' '.join(texts))==normalize(master)
assert [len(x.split()) for x in texts]==[251,274,456,448,375]
assert sum(len(x.split()) for x in texts)==1804
if STATE.exists():
    prior=json.loads(STATE.read_text(encoding='utf-8'))
    safe_preflight_resume=('--resume-preflight-only' in sys.argv and prior['state']=='STOPPED_FAILURE_OR_UNCERTAIN_NO_RETRY' and all(j['status']=='QUEUED_LOCAL_NOT_YET_SUBMITTED' and not j.get('generation_id') for j in prior['jobs']) and not list(ROOT.glob('REQUEST_*.json')))
    if not safe_preflight_resume:raise RuntimeError('Queue state already exists. Recover persisted IDs; never start a duplicate runner.')
    (ROOT/'PRESERVED_INITIAL_PREFLIGHT_FAILURE.json').write_text(json.dumps(prior,indent=2),encoding='utf-8')
state={'video_id':'009','queue_mode':'LOCAL_PERSISTENT_SEQUENTIAL_DISPATCHER_WITH_SSE_EVENTS','authorization':'Owner2026-10-30: after visual preparation, start Voicebox audio queue, leave it running and begin frames. Five locked Stage08 parts; no retries.','engine':'qwen','model':'Qwen/Qwen3-TTS-12Hz-1.7B-Base','profile_id':PROFILE,'voice_name':'Harrison','voice_provenance':'Existing Video4 clone used in owner-accepted VIDEO008; same profile verified with a real sample. Not a direct Higgsfield preset call.','credits_spent':0,'api_spend_usd':0,'approved_jobs':5,'runner_pid':os.getpid(),'started_utc':now(),'state':'PREFLIGHT','status_polling':False,'completion_transport':'SSE_SERVER_EVENTS','automatic_retries':False,'assistant_should_not_monitor':True,'stage09_pass':False,'stage10_started':False,'jobs':[{'segment':i,'input_file':f'08_HARRISON_PART_{i:02}.txt','input_sha256':hashlib.sha256(text.encode()).hexdigest(),'words':len(text.split()),'status':'QUEUED_LOCAL_NOT_YET_SUBMITTED','generation_id':None} for i,text in enumerate(texts,1)]}
save(state)
try:
    health=api('/health');profile=api('/profiles/'+PROFILE);samples=api('/profiles/'+PROFILE+'/samples')
    assert health['gpu_available'] and health['model_loaded'] and health['model_size']=='1.7B'
    assert profile['name']=='Harrison' and profile['voice_type']=='cloned' and samples
    (ROOT/'PREFLIGHT.json').write_text(json.dumps({'health':health,'profile':profile,'samples':samples,'locked_part_words':[len(x.split()) for x in texts],'cost_usd':0,'credits':0,'checked_utc':now()},indent=2),encoding='utf-8')
    # One initial history reconciliation prevents duplicate submission after an earlier/user-started run.
    # The server's read-only/history endpoint returns500 before submissions.
    # Read the same application DB in strictly read-only mode; no schema/data mutation.
    database=Path(r'C:\Users\KK\AppData\Roaming\sh.voicebox.app\voicebox.db')
    with sqlite3.connect(database.as_uri()+'?mode=ro',uri=True) as connection:
        connection.row_factory=sqlite3.Row
        history=[dict(r) for r in connection.execute('SELECT id,text,status,duration,error FROM generations WHERE profile_id=? AND text LIKE ?', (PROFILE,'%Fyre%'))]
    state['history_reconciliation']='VOICEBOX_SQLITE_READ_ONLY; GET_HISTORY_HTTP500_WORKAROUND_NO_DB_WRITES'
    (ROOT/'HISTORY_READONLY_RECONCILIATION.json').write_text(json.dumps({'method':'SQLite mode=ro','matching_fyre_records':len(history),'matched_ids':[r['id'] for r in history],'checked_utc':now(),'no_database_writes':True},indent=2),encoding='utf-8')
    assert isinstance(history,list)
    state['state']='RUNNING_SEQUENTIAL_QUEUE';save(state)
    for record,text in zip(state['jobs'],texts):
        existing=[h for h in history if normalize(h.get('text',''))==normalize(text)]
        if existing:
            assert len(existing)==1,'Ambiguous duplicate history matches; stop for recovery'
            result=existing[0];record.update(generation_id=result['id'],status='RECOVERED_EXISTING_NO_RESUBMIT',submission_recovered=True);save(state)
            if result.get('status') in ('failed','error','cancelled'):raise RuntimeError('Existing matching job failed; no automatic retry allowed')
            if result.get('status')=='completed':
                record.update(status='COMPLETED_EXISTING',duration_sec=result.get('duration'));save(state);continue
        else:
            payload={'profile_id':PROFILE,'text':text,'language':'en','model_size':'1.7B','engine':'qwen','seed':20261030,'personality':False,'normalize':False,'crossfade_ms':50,'max_chunk_chars':800,'effects_chain':[],'instruct':'Calm, measured American English business documentary narration. Clear articulation, restrained emphasis and natural pauses. No announcer hype, theatrical pauses, music, or extra words.'}
            (ROOT/f'REQUEST_{record["segment"]:02}.json').write_text(json.dumps(payload,indent=2),encoding='utf-8')
            record.update(status='SUBMITTING_DO_NOT_RETRY',submitted_utc=now());save(state)
            result=api('/generate',payload)
            assert result.get('id'),'No generation ID; uncertain submission, no retry'
            record.update(generation_id=result['id'],status=result.get('status','submitted'),response_utc=now());save(state)
            print('SUBMITTED',record['segment'],record['generation_id'],flush=True)
        completed=wait_sse(record['generation_id'])
        record.update(status='completed',duration_sec=completed.get('duration'),completed_utc=now());save(state)
        print('COMPLETED',record['segment'],flush=True)
    state.update(state='FIVE_GENERATIONS_COMPLETED_QC_NOT_RUN',qc_status='PENDING_OWNER_LISTENING_AND_TECHNICAL_QC');save(state)
except Exception as exc:
    state.update(state='STOPPED_FAILURE_OR_UNCERTAIN_NO_RETRY',error=type(exc).__name__+': '+str(exc),qc_status='NOT_RUN')
    save(state);print(state['error'],file=sys.stderr,flush=True);raise
