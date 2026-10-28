from pathlib import Path
import json,hashlib,wave,shutil,subprocess,datetime,csv,io
import numpy as np
EP=Path(__file__).resolve().parent.parent;OUT=EP/'10_AUDIO_MASTER';RAW=OUT/'SOURCE_WAV';RAW.mkdir(exist_ok=True)
VB=Path(r'C:\Users\KK\AppData\Roaming\sh.voicebox.app\generations')
queue=json.loads((EP/'09_VOICEBOX_HARRISON/GENERATION_QUEUE.json').read_text())
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def decode(p):
 r=subprocess.run(['ffmpeg','-v','error','-xerror','-i',str(p),'-f','null','-'],stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
 assert r.returncode==0,(p,r.stderr.decode())
master=OUT/'VIDEO008_HARRISON_V5_MASTER_24K_MONO_S16.wav';records=[];blobs=[];offset=0
for job in queue['jobs']:
 source=VB/(job['generation_id']+'.wav');target=RAW/f"VIDEO008_HARRISON_SEGMENT_{job['segment']:02d}.wav"
 if not target.exists():shutil.copy2(source,target)
 assert sha(source)==sha(target);decode(target)
 with wave.open(str(target),'rb') as w:
  fmt=(w.getnchannels(),w.getsampwidth(),w.getframerate(),w.getcomptype());assert fmt==(1,2,24000,'NONE'),fmt
  n=w.getnframes();pcm=w.readframes(n);assert len(pcm)==n*2
 a=np.frombuffer(pcm,dtype='<i2');edge=int(24000*.05)
 records.append(dict(segment=job['segment'],generation_id=job['generation_id'],file=target.relative_to(EP).as_posix(),source_file=str(source),input_file=job['input_file'],input_git_blob=job['input_git_blob'],sha256=sha(target),sample_rate=24000,channels=1,bits_per_sample=16,samples=n,duration_sec=n/24000,start_sample=offset,end_sample_exclusive=offset+n,start_sec=offset/24000,end_sec=(offset+n)/24000,peak_dbfs=round(20*np.log10(max(1,int(np.max(np.abs(a.astype(np.int32)))))/32768),3),full_scale_samples=int(np.sum(np.abs(a.astype(np.int32))>=32767)),head_50ms_peak=int(np.max(np.abs(a[:edge].astype(np.int32)))),tail_50ms_peak=int(np.max(np.abs(a[-edge:].astype(np.int32)))),decode='PASS'))
 blobs.append(pcm);offset+=n
with wave.open(str(master),'wb') as w:
 w.setnchannels(1);w.setsampwidth(2);w.setframerate(24000)
 for b in blobs:w.writeframes(b)
decode(master)
with wave.open(str(master),'rb') as w:
 assert w.getnframes()==offset
 for rec,original in zip(records,blobs):assert w.readframes(rec['samples'])==original
 assert w.readframes(1)==b''
joins=[]
for before,after,b1,b2 in zip(records,records[1:],blobs,blobs[1:]):
 a=np.frombuffer(b1,dtype='<i2');b=np.frombuffer(b2,dtype='<i2')
 joins.append(dict(before_segment=before['segment'],after_segment=after['segment'],master_time_sec=before['end_sec'],sample_jump=int(b[0])-int(a[-1]),tail_sample=int(a[-1]),head_sample=int(b[0]),samples_changed=0))
report=dict(video_id='008',stage='10_AUDIO_MASTER',created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),owner_source_listening_acceptance='2026-10-28: Проверил, норм; owner explicitly authorized Stage10 assembly without speed or timbre changes',semantic_pronunciation_review='OWNER_ACCEPTED; no independent automated semantic audit claimed',master_file=master.relative_to(EP).as_posix(),master_sha256=sha(master),master_bytes=master.stat().st_size,sample_rate=24000,channels=1,bits_per_sample=16,samples=offset,duration_sec=offset/24000,source_count=5,source_words=2548,source_paragraphs=50,pcm_preservation='PASS_EXACT_SAMPLE_FOR_SAMPLE',full_decode='PASS',speed_change=False,pitch_change=False,normalization=False,effects=False,resampling=False,added_silence_seconds=0,cut_samples=0,crossfades_added=0,joins=joins,sources=records,new_generations=0,credits_spent=0,stage11_started=False)
(OUT/'MASTER_QC.json').write_text(json.dumps(report,indent=2)+'\n')
buf=io.StringIO();fields=['segment','generation_id','file','sha256','samples','duration_sec','start_sample','end_sample_exclusive','start_sec','end_sec','decode'];writer=csv.DictWriter(buf,fieldnames=fields,extrasaction='ignore');writer.writeheader();writer.writerows(records);(OUT/'SEGMENT_OFFSETS.csv').write_text(buf.getvalue(),newline='\n')
for rec in records:print(json.dumps({k:rec[k] for k in ['segment','duration_sec','peak_dbfs','full_scale_samples','head_50ms_peak','tail_50ms_peak']}),flush=True)
print(json.dumps({k:report[k] for k in ['master_file','duration_sec','master_sha256','samples','pcm_preservation','joins']},indent=2),flush=True)
