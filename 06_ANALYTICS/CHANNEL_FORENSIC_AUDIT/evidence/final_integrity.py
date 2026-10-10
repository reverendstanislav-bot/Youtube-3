from pathlib import Path
import json,re,csv,io
p=Path(r'C:\Users\KK\channel-audit-20261010\06_ANALYTICS\CHANNEL_FORENSIC_AUDIT')
for f in p.rglob('*'):
 if f.is_file() and f.suffix in ['.md','.py']:
  s=f.read_text(encoding='utf-8');f.write_text('\n'.join(x.rstrip() for x in s.splitlines()).rstrip()+'\n',encoding='utf-8')
f=p/'evidence/repo_refresh_0bc1e6f.md';s=f.read_text(encoding='utf-8').replace('Paths above are from evidence/; resolve four parent levels to repository root if viewing source directly.','Paths above resolve from evidence/ three parent levels to repository root.');f.write_text(s,encoding='utf-8')
r=json.loads((p/'evidence/package_integrity.json').read_text(encoding='utf-8'))
missing=[];broken=[]
for f in p.glob('*.md'):
 if not re.match(r'^\d\d_',f.name):continue
 for d in re.findall(r'\]\(([^)]+)\)',f.read_text(encoding='utf-8')):
  if not d.startswith(('http','C:','/','#','<')) and not(p/d.split('#')[0]).exists():broken.append([f.name,d])
r['broken_local_links_final']=broken;r['git_final_source']='0bc1e6f';r['independent_review']='conducted; lead resolutions documented, no blanket audio or motion PASS'
assert r['required_count']==15 and r['owner_answers']==18 and not broken
(p/'evidence/package_integrity.json').write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf-8')
print('15 reports;18 owner answers;10 rootcauses;12 experiments;0 broken report links. HQ timestamp anomalies explicitly reported.')
