from pathlib import Path
import json,csv,re,io,subprocess
p=Path(r'C:\Users\KK\channel-audit-20261010\06_ANALYTICS\CHANNEL_FORENSIC_AUDIT')
# Standalone integrity validation; no repeated report appends.
required=sorted([x for x in p.iterdir() if re.match(r'^\d\d_',x.name)])
result={'required_count':len(required),'broken_local_links':[],'csv_rows':{}}
for f in required:
 s=f.read_text(encoding='utf-8')
 if '\ufffd' in s or 'continuouscontinuous' in s:raise ValueError(f.name)
 if f.suffix=='.csv':result['csv_rows'][f.name]=len(list(csv.DictReader(io.StringIO(s))))
 for dest in re.findall(r'\]\(([^)]+)\)',s):
  if not dest.startswith(('http','C:','/','#','<')) and not(p/dest.split('#')[0]).exists():result['broken_local_links'].append([f.name,dest])
for n in ['studio_snapshot.json','shorts_metrics.json']:json.loads((p/'evidence'/n).read_text(encoding='utf-8'))
result['owner_answers']=len(re.findall(r'^## \d+\.',(p/'14_OWNER_REVIEW_RU.md').read_text(encoding='utf-8'),re.M))
j=json.loads(subprocess.check_output(['ffprobe','-v','error','-select_streams','v:0','-show_frames','-show_entries','frame=best_effort_timestamp_time','-of','json',r'C:\Users\KK\Downloads\UMG_DISTROKID_FINAL_ENDSCREEN_YOUTUBE_FINAL_HQ.mp4']))
ts=[float(x['best_effort_timestamp_time']) for x in j['frames'] if 'best_effort_timestamp_time'in x]
bad=[{'frame':i,'previous':ts[i-1],'current':ts[i]}for i in range(1,len(ts))if ts[i]<=ts[i-1]]
result['HQ_decoded_frames']=len(ts);result['HQ_nonincreasing_decoded_timestamps']=bad
(p/'evidence/package_integrity.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
