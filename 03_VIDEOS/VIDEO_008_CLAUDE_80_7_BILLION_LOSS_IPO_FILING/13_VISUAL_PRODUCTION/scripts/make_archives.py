from pathlib import Path
import hashlib, json, zipfile

root=Path(r'C:\Users\KK\VIDEO008_PRODUCTION')
items=[('VIDEO008_SOURCE_ARCHIVE','VIDEO008_SOURCE_ARCHIVE.zip'),('VIDEO008_FINAL_VISUAL_PACK','VIDEO008_FINAL_VISUAL_PACK.zip')]
result=[]
for folder,name in items:
 src=root/folder; out=root/name
 with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_STORED,allowZip64=True) as z:
  for p in sorted(src.rglob('*')):
   if p.is_file(): z.write(p,Path(folder)/p.relative_to(src))
 with zipfile.ZipFile(out) as z: bad=z.testzip()
 h=hashlib.sha256()
 with out.open('rb') as f:
  for b in iter(lambda:f.read(4*1024*1024),b''):h.update(b)
 result.append({'file':name,'bytes':out.stat().st_size,'sha256':h.hexdigest().upper(),'zip_test':'PASS' if bad is None else f'FAIL:{bad}'})
(root/'VIDEO008_ARCHIVE_CHECKSUMS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
(root/'VIDEO008_ARCHIVE_CHECKSUMS.txt').write_text('\n'.join(f"{x['sha256']}  {x['file']}" for x in result)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
