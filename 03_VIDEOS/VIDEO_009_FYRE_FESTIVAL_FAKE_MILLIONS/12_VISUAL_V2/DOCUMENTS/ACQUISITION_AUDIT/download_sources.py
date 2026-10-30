from pathlib import Path
import csv,requests,json,hashlib,datetime,concurrent.futures
ROOT=Path(__file__).resolve().parent
INPUT=ROOT.parent/'INPUT_PACKAGE/VIDEO009_CODEX_VISUAL_PACKAGE'
(ROOT/'ORIGINALS').mkdir(parents=True,exist_ok=True)
rows=list(csv.DictReader((INPUT/'SOURCE_URLS.csv').open(encoding='utf-8-sig',newline='')))
rows=[r for r in rows if r['source_type']=='official_primary']
rows += [{'source_id':'DOJ_COPYRIGHT_POLICY','url':'https://www.justice.gov/legalpolicies','source_type':'official_rights_policy'},{'source_id':'SEC_COPYRIGHT_POLICY','url':'https://www.sec.gov/about/privacy-information','source_type':'official_rights_policy'}]
def download(row):
    row=dict(row);row['retrieved_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    try:
        r=requests.get(row['url'],headers={'User-Agent':'Mozilla/5.0 (compatible; documentary primary-source verification; public information request)'},timeout=60)
        row.update(http_status=r.status_code,final_url=r.url,content_type=r.headers.get('Content-Type',''))
        ext='.pdf' if r.content.startswith(b'%PDF-') else '.html'
        file=ROOT/'ORIGINALS'/(row['source_id']+ext)
        file.write_bytes(r.content)
        row.update(file=str(file),bytes=len(r.content),sha256=hashlib.sha256(r.content).hexdigest(),download_status='DOWNLOADED' if r.status_code==200 else 'HOLD_HTTP_ERROR_BODY_RETAINED')
        if ext=='.pdf':
            import fitz
            d=fitz.open(file);row['pdf_pages']=len(d)
            (ROOT/'ORIGINALS'/(row['source_id']+'_TEXT.txt')).write_text('\n\n'.join(f'PAGE {i+1}\n'+p.get_text() for i,p in enumerate(d)),encoding='utf-8')
    except Exception as e:row.update(download_status='HOLD_DOWNLOAD_ERROR',error=repr(e))
    return row
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:result=list(pool.map(download,rows))
(ROOT/'SOURCE_DOWNLOADS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
for r in result: print(json.dumps(r,ensure_ascii=False))
