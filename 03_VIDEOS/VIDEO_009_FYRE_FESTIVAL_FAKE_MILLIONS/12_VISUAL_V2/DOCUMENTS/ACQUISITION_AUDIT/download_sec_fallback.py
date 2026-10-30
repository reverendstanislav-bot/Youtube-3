import requests,hashlib,json,concurrent.futures
from pathlib import Path
r=Path(__file__).resolve().parent/'ORIGINALS'
urls=[('SEC_COMPLAINT_OFFICIAL_ALIAS','https://www.sec.gov/file/sec-complaint-1545'),('SEC_COMPLAINT_CCH_MIRROR','https://business.cch.com/srd/comp-pr2018-141-20180724.pdf'),('SEC_COMPLAINT_OFFICIAL_PR','https://www.sec.gov/litigation/complaints/2018/comp-pr2018-141.pdf')]
def run(x):
 sid,url=x
 try:
  q=requests.get(url,timeout=40,headers={'User-Agent':'Mozilla/5.0'});data=q.content;p=r/(sid+('.pdf' if data.startswith(b'%PDF-') else '.html'));p.write_bytes(data)
  return {'source_id':sid,'url':url,'final_url':q.url,'status':q.status_code,'file':str(p),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'pdf':data.startswith(b'%PDF-')}
 except Exception as e:return {'source_id':sid,'error':str(e)}
out=list(concurrent.futures.ThreadPoolExecutor(3).map(run,urls))
(r.parent/'SEC_FALLBACK_DOWNLOADS.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
