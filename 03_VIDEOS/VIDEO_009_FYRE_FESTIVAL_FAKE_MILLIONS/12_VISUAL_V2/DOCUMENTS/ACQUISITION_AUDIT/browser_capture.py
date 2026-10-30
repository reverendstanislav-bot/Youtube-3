from pathlib import Path
import subprocess,json,hashlib,datetime,concurrent.futures
ROOT=Path(__file__).resolve().parent
rows=json.loads((ROOT/'SOURCE_DOWNLOADS.json').read_text())
rows=[r for r in rows if r['source_id'] in ('DOJ_PLEA','DOJ_VIP','DOJ_SENTENCE','SEC_RELEASE','SEC_COMPLAINT_PDF','SEC_COPYRIGHT_POLICY')]
EDGE=r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
(ROOT/'RENDERED_PAGES').mkdir(exist_ok=True)
result=[]
for row in rows:
    sid=row['source_id'];out=ROOT/'RENDERED_PAGES'/(sid+'_BROWSER_PRINT.pdf')
    common=[EDGE,'--headless','--disable-gpu','--disable-extensions','--no-first-run','--no-default-browser-check','--user-data-dir='+str(ROOT/'EDGE_PROFILE')]
    if not out.exists():
        run=subprocess.run(common+['--print-to-pdf='+str(out),row['url']],timeout=100,capture_output=True)
    entry={'source_id':sid,'url':row['url'],'browser_print_file':str(out),'capture_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'provenance':'Browser-native rendering of the official live URL; NOT an original agency PDF and no source text retyped'}
    if out.exists():
        import pymupdf
        doc=pymupdf.open(out);text='\n\n'.join('BROWSER_PRINT_PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(doc))
        textfile=out.with_suffix('.txt');textfile.write_text(text,encoding='utf-8')
        entry.update(bytes=out.stat().st_size,sha256=hashlib.sha256(out.read_bytes()).hexdigest(),pages=len(doc),text_file=str(textfile),characters=len(text),content_excerpt=text[:180])
        entry['status']='PASS_BROWSER_PAGE_CAPTURE' if len(text)>4000 and not ('Access Denied' in text[:400] or 'Reference #' in text[:400]) else 'HOLD_BROWSER_CAPTURE_UNVERIFIED'
    result.append(entry)
    (ROOT/'BROWSER_CAPTURES.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(entry),flush=True)
