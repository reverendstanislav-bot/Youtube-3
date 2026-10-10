"""Validate recovery tracking. Does not certify media or trigger external actions."""
from pathlib import Path
import csv,json,re,math
from datetime import datetime,timedelta
ROOT=Path(__file__).resolve().parent
AUDIT=ROOT.parent
def read(name):
 with (ROOT/name).open(encoding='utf-8',newline='')as f:return list(csv.DictReader(f))
def validate_measurements(rows):
 errors=[]
 for n,r in enumerate(rows,2):
  for k in ['views','impressions','ctr_percent','engaged_views','avd_seconds','apv_percent','stayed_percent','feed_exposures','retention30_percent','retention60_percent','subscribers_gained','related_clicks']:
   v=r.get(k,'')
   if v:
    try:
     v=float(v)
     if not math.isfinite(v) or v<0 or (k in ['ctr_percent','stayed_percent']and v>100):errors.append(f'measurements:{n}:invalid {k}')
    except ValueError:errors.append(f'measurements:{n}:nonnumeric {k}')
  if not r.get('evidence')or not r.get('availability_notes'):errors.append(f'measurements:{n}:missing evidence/limits')
  if r.get('checkpoint')!='OBSERVATIONAL':
   try:
    t0=datetime.fromisoformat(r['publication_at']);tc=datetime.fromisoformat(r['captured_at'])
    assert t0.tzinfo is not None and tc.tzinfo is not None
    target={'T24':24,'T48':48,'T72':72,'T7':168}[r['checkpoint']]
    assert abs((tc-t0).total_seconds()/3600-target)<=3
   except (ValueError,KeyError,AssertionError):errors.append(f'measurements:{n}:invalid age-normalized checkpoint')
  ev=AUDIT/r.get('evidence','')
  if not ev.is_file():errors.append(f'measurements:{n}:evidence missing')
 return errors
def main():
 measurements=read('MEASUREMENTS.csv');errors=validate_measurements(measurements)
 qc=read('QC_EVIDENCE.csv');experiments=read('EXPERIMENT_STATUS.csv');tasks=read('TASK_BOARD.csv')
 for name,entries,allowed in [
  ('QC',qc,{'PASS','REVIEW','NOT_VERIFIED','FAIL'}),
  ('experiments',experiments,{'PREPARED','RUNNING','COMPLETED','INCONCLUSIVE','HOLD','CANCELLED'}),
  ('tasks',tasks,{'DONE','READY','WAITING','BLOCKED','CANCELLED'})]:
  for r in entries:
   if r['status']not in allowed:errors.append(name+':unknown status '+r['status'])
 for r in read('SNAPSHOT_QUEUE.csv'):
  if r['status']not in {'WAITING_FOR_PUBLICATION','SCHEDULED','COLLECTED'}:errors.append('queue:unknown status')
  if r['checkpoint']not in {'T24','T48','T72','T7'}:errors.append('queue:unknown checkpoint')
  if r['status']in {'SCHEDULED','COLLECTED'}:
   try:
    t0=datetime.fromisoformat(r['publication_at']);due=datetime.fromisoformat(r['due_at'])
    assert t0.tzinfo is not None and due.tzinfo is not None
    assert due==t0+timedelta(hours={'T24':24,'T48':48,'T72':72,'T7':168}[r['checkpoint']])
    if r['status']=='COLLECTED':
     cap=datetime.fromisoformat(r['captured_at']);assert cap.tzinfo is not None
     assert abs((cap-due).total_seconds())<=10800
     assert r['evidence'] and (AUDIT/r['evidence']).is_file()
   except (ValueError,AssertionError,KeyError):errors.append('queue:invalid timestamp/evidence')
 for r in qc:
  if r['status']=='PASS'and(not re.fullmatch('[a-f0-9]{64}',r['artifact_sha256'])or not r['review_date']or not r['reviewer']or not(AUDIT/r['evidence']).is_file()):
   errors.append('QC PASS lacks artifact/reviewer/date/evidence:'+r['episode']+'/'+r['gate'])
 for r in experiments:
  if r['status']=='RUNNING'and any(not r[x]for x in ['start_at','control_version','variant_version']):errors.append('RUNNING without live start/versions:'+r['id'])
  if r['status']in {'COMPLETED','INCONCLUSIVE'}and any(not r[x]for x in ['end_at','result','decision']):errors.append('COMPLETED without outcome:'+r['id'])
 for r in tasks:
  if r['status']=='DONE'and(not r['evidence']or not(AUDIT/r['evidence']).is_file()):errors.append('DONE without evidence:'+r['id'])
 # Meaningful negative controls: reject fake percentage and fake age windows.
 bad=dict(measurements[0]);bad['ctr_percent']='101';assert validate_measurements([bad])
 bad=dict(measurements[0]);bad['checkpoint']='T24';assert validate_measurements([bad])
 result={'tracking_validation':'PASS'if not errors else'FAIL','errors':errors,'measurements':len(measurements),'future_checkpoints':len(read('SNAPSHOT_QUEUE.csv')),'QC_entries':len(qc),'experiments_prepared':sum(r['status']=='PREPARED'for r in experiments),'experiments_launched_by_this_task':0,'negative_controls_passed':2,'limits':'Validates records only. No auditory/visual/legal/release/experiment-effectiveness PASS.'}
 (ROOT/'validation_result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(result,ensure_ascii=False))
 return bool(errors)
if __name__=='__main__':raise SystemExit(main())
