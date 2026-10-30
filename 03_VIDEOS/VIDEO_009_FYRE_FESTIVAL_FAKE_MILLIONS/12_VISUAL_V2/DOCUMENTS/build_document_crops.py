from pathlib import Path
import pymupdf, json, hashlib, csv, shutil, zipfile, re
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parent
REPO=Path(r'C:\Users\KK\Youtube-3-video009-visual-v2\03_VIDEOS\VIDEO_009_FYRE_FESTIVAL_FAKE_MILLIONS\12_VISUAL_V2\DOCUMENTS')
for x in ('CROPS','REFERENCE_PAGES','REJECTED_NETWORK_RESPONSES'):(ROOT/x).mkdir(exist_ok=True)
REPO.mkdir(parents=True,exist_ok=True)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
browser=json.loads((ROOT/'BROWSER_ORIGINAL_RESPONSES.json').read_text(encoding='utf-8'))
downloads=json.loads((ROOT/'SOURCE_DOWNLOADS.json').read_text(encoding='utf-8'))
fallbacks=json.loads((ROOT/'SEC_FALLBACK_DOWNLOADS.json').read_text(encoding='utf-8'))
# Interstitial/error payloads are retained as network audit evidence, never verified sources.
for p in list((ROOT/'ORIGINALS').glob('*.html')):
    text=p.read_text(encoding='utf-8',errors='replace')
    if 'triggerInterstitialChallenge' in text or 'Access Denied' in text or 'Automated access to our sites' in text or p.name in ('SEC_RELEASE.html','SEC_COMPLAINT_PDF.html','SEC_COPYRIGHT_POLICY.html','SEC_COMPLAINT_OFFICIAL_ALIAS.html','SEC_COMPLAINT_OFFICIAL_PR.html'):
        dest=ROOT/'REJECTED_NETWORK_RESPONSES'/p.name
        if not dest.exists():shutil.move(str(p),str(dest))
for p in list((ROOT/'RENDERED_PAGES').glob('SEC*')):
    dest=ROOT/'REJECTED_NETWORK_RESPONSES'/p.name
    if not dest.exists():shutil.move(str(p),str(dest))

sources={}
for row in browser:
    assert row['valid_official_content']
    sid=row['source_id'];pdf=ROOT/'RENDERED_PAGES'/(sid+'_BROWSER_PRINT.pdf');d=pymupdf.open(pdf)
    text='\n\n'.join(f'BROWSER_PRINT_PAGE {i+1}\n'+p.get_text() for i,p in enumerate(d))
    pdf.with_suffix('.txt').write_text(text,encoding='utf-8')
    sources[sid]={'source_id':sid,'url':row['url'],'download_url':row['final_url'],'original_file':row['file'],'original_sha256':row['sha256'],'original_bytes':row['bytes'],'provenance':'OFFICIAL_DOJ_HTML_RESPONSE_BODY','pixel_document':str(pdf),'pixel_document_sha256':sha(pdf),'pages':len(d),'pixel_document_type':'BROWSER_PRINT_OF_OFFICIAL_WEBPAGE_NOT_NATIVE_AGENCY_PDF','rights':'US_FEDERAL_GOVERNMENT_AUTHORED_TEXT_PUBLIC_DOMAIN; DOJ policy captured; seals/third-party images excluded','qc':'PASS_ACTUAL_FILE_CONTENT_VERIFIED'}
native=next(r for r in downloads if r['source_id']=='DOJ_COMPLAINT_PDF')
sources['DOJ_COMPLAINT_PDF']={'source_id':'DOJ_COMPLAINT_PDF','url':native['url'],'download_url':native['final_url'],'original_file':native['file'],'original_sha256':native['sha256'],'original_bytes':native['bytes'],'provenance':'NATIVE_PDF_DOWNLOADED_FROM_OFFICIAL_DOJ','pixel_document':native['file'],'pixel_document_sha256':native['sha256'],'pages':7,'pixel_document_type':'ORIGINAL_SCANNED_CRIMINAL_COMPLAINT_PDF','rights':'US_FEDERAL_GOVERNMENT_AUTHORED_COURT_COMPLAINT_TEXT_PUBLIC_DOMAIN; selected text only','qc':'PASS_ACTUAL_PDF_AND_VISUAL_PAGE_VERIFIED'}
mirror=next(r for r in fallbacks if r['source_id']=='SEC_COMPLAINT_CCH_MIRROR')
sec=ROOT/'ORIGINALS/SEC_COMPLAINT_CCH_MIRROR.pdf';sd=pymupdf.open(sec)
assert len(sd)==25 and '1:18-cv-06634' in sd[0].get_text() and '$27.4 million' in sd[0].get_text() and '$1,499' in sd[11].get_text()
sources['SEC_COMPLAINT_MIRROR']={'source_id':'SEC_COMPLAINT_MIRROR','url':'https://www.sec.gov/files/litigation/complaints/2018/comp24213.pdf','download_url':mirror['url'],'original_file':str(sec),'original_sha256':sha(sec),'original_bytes':sec.stat().st_size,'provenance':'ORIGINAL_GOVERNMENT_COURT_FILING_COPY_HOSTED_BY_CCH_LEGAL_PUBLISHER_MIRROR','pixel_document':str(sec),'pixel_document_sha256':sha(sec),'pages':25,'pixel_document_type':'COURT_COMPLAINT_PDF_MIRROR_COPY','identity_verification':'Case1:18-cv-06634;Document1;Filed07/24/18;25pages;parties;para1$27.4m andpara44$2.56m/$1499 match agency-hosted primary reader. No agency-byte SHA match claimed.','rights':'US_FEDERAL_GOVERNMENT_AUTHORED_COURT_COMPLAINT_TEXT_PUBLIC_DOMAIN; mirror distribution does not change underlying government text; no publisher editorial additions used','qc':'PASS_DOCUMENT_IDENTITY_AND_PIXELS; HOLD_OFFICIAL_BINARY_ARCHIVAL_IDENTITY'}

# Rectangles are native PDF points. Outputs are direct 3x rasterizations of those rectangles.
plan=[
 ('DOC001',1,'DOJ_PLEA',1,(28,134,588,448),'March 6, 2018','P001-P004','Plea headline/date/agency, opening proof',''),
 ('DOC002',1,'DOJ_PLEA',2,(28,290,588,503),'2,500','P002','Complete revenue and booking-count paragraph; one-month/year distinction retained',''),
 ('DOC003',2,'DOJ_PLEA',2,(28,88,588,291),'digital application','P005-P007','Founding and artist-booking-platform context, including admission context above',''),
 ('DOC004',3,'DOJ_PLEA',2,(28,439,588,501),'single month','P008-P010','Tight booking-count source excerpt, not festival lineup',''),
 ('DOC005',4,'DOJ_COMPLAINT_PDF',6,(40,35,572,181),'SCANNED_PAGE_VISUALLY_VERIFIED','P011-P012','Original scanned criminal complaint paragraph8 continued: May2016–April2017 $57,443 revenue',''),
 ('DOC006',5,'SEC_COMPLAINT_MIRROR',12,(62,4,552,299),'$1,499','P013-P017','Original court complaint paragraph44, purported$2.56m vsactual$1499; no stock-theft claim','Source substitution: requested SEC release pixels inaccessible403; genuine SEC complaint paragraph44 directly supports the same facts. Mirror provenance disclosed.'),
 ('DOC007',5,'SEC_COMPLAINT_MIRROR',1,(61,4,553,428),'18-CV-6634','P015-P017','Authentic complaint cover, case header, parties and filing identity','Official binary blocked; verified CCH-hosted copy, not byte-compared to SEC binary.'),
 ('DOC008',6,'DOJ_SENTENCE',3,(28,67,588,244),'no event cancellation insurance','P018-P021','Complete unexecuted-policy paragraph from DOJ sentencing release','Uses later admitted-conduct sentencing source for the same insurance fact.'),
 ('DOC009',7,'DOJ_PLEA',1,(28,134,588,730),'pled guilty today','P022-P025','March2018 plea headline/date plus outcome paragraph','Repeated source revisited with broader context; not a new source.'),
 ('DOC010',7,'DOJ_INITIAL_CHARGES',1,(28,134,588,718),'June 30, 2017','P024','June30 2017 original charge announcement; allegations kept distinct from later pleas',''),
 ('DOC011',8,'DOJ_VIP',1,(28,134,588,662),'July 26, 2018','P026-P029','July2018 separate NYC VIP plea headline/date/agency',''),
 ('DOC012',8,'DOJ_VIP',2,(28,27,588,625),'NYC VIP Access','P026-P029','Plea continuation and U.S. Attorney quote about separate VIP scam; admissions and original case context','Browser retrieval-date header excluded from selected crop; original source unchanged.'),
 ('DOC013',9,'DOJ_SENTENCE',1,(28,134,588,524),'October 11, 2018','P030-P034','Sentencing headline/date/agency','Final forfeiture amount separately verified on browser-print page5; do not replace it with earlier plea forfeiture.'),
 ('DOC014',9,'SEC_COMPLAINT_MIRROR',1,(61,439,553,777),'$27.4 million','P033','SEC complaint introduction paragraph1: funds raised, not additional investor losses','Archive URL pointed to release despite describing complaint intro; corrected to complaint page1. Official binary blocked; disclosed legal-publisher mirror copy.')
]
registries=[]; pages={}
for aid,act,sid,page,bbox,needle,paras,purpose,note in plan:
    source=sources[sid];doc=pymupdf.open(source['pixel_document']);p=doc[page-1];clip=pymupdf.Rect(bbox)&p.rect
    text=p.get_text(clip=clip)
    if needle!='SCANNED_PAGE_VISUALLY_VERIFIED':assert needle.lower() in ' '.join(text.lower().split()),(aid,needle,text)
    file=ROOT/'CROPS'/(aid+'_'+sid+'_P'+str(page).zfill(2)+'.png');pix=p.get_pixmap(matrix=pymupdf.Matrix(3,3),clip=clip,alpha=False);pix.save(file)
    key=(sid,page)
    if key not in pages:
        full=ROOT/'REFERENCE_PAGES'/(sid+'_P'+str(page).zfill(2)+'.png');p.get_pixmap(matrix=pymupdf.Matrix(2,2),alpha=False).save(full);pages[key]=str(full)
    registries.append({'asset_id':aid,'act':act,'paragraph_range':paras,'source_id':sid,'official_source_url':source['url'],'actual_download_url':source['download_url'],'source_file':source['original_file'],'source_sha256':source['original_sha256'],'pixel_document':source['pixel_document'],'pixel_document_sha256':source['pixel_document_sha256'],'source_provenance':source['provenance'],'page_1_based':page,'page_number_type':'BROWSER_PRINT_PAGE_NOT_NATIVE_AGENCY_PAGINATION' if sid.startswith('DOJ_') and sid!='DOJ_COMPLAINT_PDF' else 'NATIVE_COURT_PDF_PAGE','bbox_pdf_points':json.dumps(list(clip)),'render_scale':3,'file':str(file),'sha256':sha(file),'width':pix.width,'height':pix.height,'full_source_page':pages[key],'purpose':purpose,'verified_source_passage':text if text.strip() else 'Scanned native PDF page6 top: May2016 toApril2017 revenue$57,443. Visually verified; no OCR text substituted.','rights':source['rights'],'source_substitution_or_limits':note,'pixel_qc':'PASS_REAL_SOURCE_PIXELS_NO_RETYPE_NO_OVERLAYS','source_identity_qc':'PASS_DOCUMENT_COPY_IDENTITY_MIRROR_OFFICIAL_BINARY_HOLD' if sid=='SEC_COMPLAINT_MIRROR' else 'PASS','status':'PASS_CROP_PREPARED_COMMERCIAL_GOVERNMENT_TEXT_SCOPE; FINAL_EDIT_CONTEXT_REVIEW_REQUIRED'})

# Additional genuine full pages support prompt references without inventing extra DOC IDs.
for sid,page in [('DOJ_SENTENCE',3),('DOJ_SENTENCE',5),('DOJ_PLEA',3),('DOJ_VIP',3)]:
    key=(sid,page)
    if key in pages:continue
    doc=pymupdf.open(sources[sid]['pixel_document']);file=ROOT/'REFERENCE_PAGES'/(sid+'_P'+str(page).zfill(2)+'.png');doc[page-1].get_pixmap(matrix=pymupdf.Matrix(2,2),alpha=False).save(file);pages[key]=str(file)

factspec=[
 ('BOOKINGS','DOJ_PLEA',2,'2,500','More than2500 purported platform bookings inoneMONTH versus60 confirmed inoneYEAR; not a direct like-period ratio or festival lineup'),
 ('REVENUE','DOJ_PLEA',2,'$57,443','Actual platform booking income approximatelyMay2016–Apr2017; not festival ticket revenue'),
 ('MAGNISES','DOJ_SENTENCE',3,'$40 million','Purported$40m sale hadnotoccurred asrepresented'),
 ('BROKERAGE','SEC_COMPLAINT_MIRROR',12,'$1,499','Complaint paragraph44: purported$2.56m inFacebook shares versus$1499 actual; not sharetheft'),
 ('INSURANCE','DOJ_SENTENCE',3,'insurance','Noevent cancellation policies executed; not denialofclaim byinsurer'),
 ('INVESTOR_LOSSES','DOJ_PLEA',2,'$24 million','Over$24m investorlosses andatleast80victims, not festival productioncost'),
 ('VENDOR_LOSSES','DOJ_PLEA',3,'$2 million','Vendor advanced$2m; separatescope, do notsum with SECraisedfunds'),
 ('JUNE_CHARGES','DOJ_INITIAL_CHARGES',1,'June 30, 2017','Original charge, notconviction'),
 ('MARCH_PLEA','DOJ_PLEA',1,'March 6, 2018','Guilty plea toinvestor andvendor wirefraud'),
 ('JULY_PLEA','DOJ_VIP',1,'July 26, 2018','SeparateNYC VIPAccess plea, bankfraud andfalsestatements describedinpage2'),
 ('SENTENCE','DOJ_SENTENCE',1,'October 11, 2018','Six-year historicalsentence, no presentwhereaboutsassertion'),
 ('FORFEITURE','DOJ_SENTENCE',5,'$26,191,306.28','Final forfeitureordered, not proof victimsrecovered thatamount; earlierplea$26,040,099.48issupersededforfinalamount'),
 ('SEC_RAISED','SEC_COMPLAINT_MIRROR',1,'$27.4 million','Raised acrossmultipleentities; notadditive investorlosses norfestivalbudget')
]
facts=[]
for fid,sid,page,needle,guardrail in factspec:
    source=sources[sid];p=pymupdf.open(source['pixel_document'])[page-1];txt=p.get_text();assert needle.lower() in txt.lower(),fid
    blocks=[b[4].strip() for b in p.get_text('blocks') if needle.lower() in b[4].lower()]
    facts.append({'fact_id':fid,'source_id':sid,'page_1_based':page,'official_url':source['url'],'actual_download_url':source['download_url'],'pixel_document':source['pixel_document'],'reference_page':pages.get((sid,page),''),'source_sha256':source['original_sha256'],'verified_passage':'\n'.join(blocks),'guardrail':guardrail,'status':'PASS_LOCAL_SOURCE_PASSAGE_VERIFIED'})
facts.append({'fact_id':'SEC_OTHER_RESPONDENTS_NONADMISSION','source_id':'SEC_RELEASE','official_url':'https://www.sec.gov/newsroom/press-releases/2018-141','actual_download_url':'','page_1_based':'HTML release paragraph4','pixel_document':'','reference_page':'','source_sha256':'','verified_passage':'Agency webpage read through primary-source web reader; not locally available as a genuine HTML response or source-pixel image. McFarland admitted SEC allegations; Margolin/Simon/FyreMedia/Magnises settled withoutadmittingordenying.','guardrail':'Do not assignMcFarlandadmissions tootherrespondents; localpixel evidence forsettlement paragraphstillHOLD','status':'PASS_WEB_PRIMARY_TEXT_ONLY_HOLD_LOCAL_RELEASE_ARCHIVE'})

def writecsv(file,rows):
    fields=list(dict.fromkeys(k for r in rows for k in r))
    with file.open('w',encoding='utf-8',newline='') as f:w=csv.DictWriter(f,fields,lineterminator='\n');w.writeheader();w.writerows(rows)
for row in registries:
    row['legal_status']='CIVIL_COMPLAINT_ALLEGATIONS; MCFARLAND_ADMISSION_CORROBORATED_BY_RELEASE_WEB_TEXT' if row['source_id']=='SEC_COMPLAINT_MIRROR' else ('CHARGING_COMPLAINT_ALLEGATIONS_CORROBORATED_LATER_PLEA' if row['source_id']=='DOJ_COMPLAINT_PDF' else ('ORIGINAL_CHARGES_ALLEGATIONS_NOT_CONVICTION' if row['source_id']=='DOJ_INITIAL_CHARGES' else 'OFFICIAL_REPORT_OF_ADMITTED_CONDUCT_AND_PLEA_OR_SENTENCE'))
writecsv(ROOT/'DOCUMENT_CROP_REGISTRY.csv',registries)
writecsv(ROOT/'DOCUMENT_FACT_REFERENCES.csv',facts)
(ROOT/'VERIFIED_SOURCES.json').write_text(json.dumps(list(sources.values()),indent=2),encoding='utf-8')
for start in (0,7):
    subset=registries[start:start+7];sheet=Image.new('RGB',(1800,1200),'#202020');draw=ImageDraw.Draw(sheet)
    for k,row in enumerate(subset):
        im=Image.open(row['file']).convert('RGB');im.thumbnail((580,260));x=(k%3)*600;y=(k//3)*400;draw.text((x+10,y+8),row['asset_id']+' / '+row['source_id']+' / p'+str(row['page_1_based']),fill='white');sheet.paste(im,(x+(600-im.width)//2,y+38))
    sheet.save(ROOT/('CROP_CONTACT_'+str(start//7+1)+'.jpg'),quality=92)

verified_files=[Path(s['original_file']) for s in sources.values()]+[ROOT/'ORIGINALS/DOJ_COPYRIGHT_POLICY.html']
manifest=[{'file':p.name,'bytes':p.stat().st_size,'sha256':sha(p)} for p in verified_files]
writecsv(ROOT/'ORIGINAL_SOURCE_SHA256.csv',manifest)
archive=ROOT/'VIDEO009_ORIGINAL_DOCUMENT_SOURCES.zip'
with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
    for p in verified_files:z.write(p,'ORIGINALS/'+p.name)
    z.writestr('SOURCE_PROVENANCE.json',json.dumps(list(sources.values()),indent=2));z.writestr('README.txt','6 genuine case sources:4 original DOJ HTML response bodies,1 native official DOJ complaint PDF,1 genuineSEC complaint court-filing copy acquiredfromCCH legal-publishermirror. Mirroridentity25pages/case/date/passagesconfirmedagainstagencyreader; noofficialbytehashcomparisonclaimed. AdditionalDOJcopyrightpolicyincluded. Error/interstitialresponsesexcluded. BrowserprintPDFsandrealpixelcropsareseparate derivatives. No source text retyped. SourceidentitiesandrightsnotesinSOURCE_PROVENANCE.json. Agencylogos/sealsarenotapprovedforbranding.');z.write(ROOT/'ORIGINAL_SOURCE_SHA256.csv','ORIGINAL_SOURCE_SHA256.csv')
with zipfile.ZipFile(archive) as z:assert z.testzip() is None
report={'verified_case_source_files':6,'official_html_response_bodies':4,'official_native_pdf':1,'sec_native_court_filing_mirror_copy':1,'additional_rights_policy_files':1,'official_sec_release_binary':'HOLD_HTTP403','official_sec_pdf_binary':'HOLD_HTTP403_MIRROR_COPY_AVAILABLE','doc_crops':14,'doc_crop_source_substitution':'DOC006 uses original SEC complaint paragraph44 instead of blocked SEC release; DOC014 locator corrected to complaintintro p1','crop_real_pixels_qc':'PASS_MAKER_REVIEW_PENDING_INDEPENDENT_CRITIC','source_archive':str(archive),'source_archive_sha256':sha(archive),'source_archive_bytes':archive.stat().st_size,'source_archive_integrity':'PASS','no_fake_documents':True,'no_source_text_retyped':True,'paid_generation':0,'publication_clearance':'NOT_CLAIMED_FINAL_CONTEXT_AND_GLOBAL_RIGHTS_GATES_SEPARATE'}
(ROOT/'DOCUMENT_QC_SUMMARY.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
(ROOT/'DOCUMENT_QC.md').write_text('''# VIDEO009 authentic document preparation

Fourteen real-pixel source crops are prepared. No source text was recreated, no highlights or service labels were baked. Crop rectangles and page numbers are in `DOCUMENT_CROP_REGISTRY.csv`; PNGs are direct 3x PDF rasterizations. Source pages remain available for context.

Six genuine case-source files are archived: four actual DOJ HTML response bodies obtained by ordinary browser fetch after navigation; one native7-page DOJ criminal complaint from justice.gov; one native25-page SEC civil complaint copy hosted by CCH legal publisher. Official SEC binary requests were denied403. The mirror's case number1:18-cv-06634,Document1,07/24/18 date,25pages,parties and paragraphs1/44 were verified against agency-hosted primary-reader text. **No byte-identical official-SEC SHA claim is made.** Error/interstitial bodies are audit-only and excluded from verified-source counts and ZIP.

The DOJ HTML pages were rendered natively by Edge. Their print PDF page numbers are **browser-print pagination, not native agency PDF pagination**. Original responseHTML files and renderPDF hashes are recorded separately. DOJ scanned criminal complaint and SEC complaint retain native court pagination.

DOC006 source substitution: the blocked SEC press-release paragraph is replaced by the real SEC civil complaint paragraph44,page12,which directly supports the same>$2.5m versus<$1500 brokerage facts. DOC014's conflicting input URL is corrected to complaint introduction,page1. These are explicit substitutions, not recreated press-release pages.

Rights scope: selected text is authored by U.S. federal employees in their official duties. DOJ public-domain policy is preserved at `ORIGINALS/DOJ_COPYRIGHT_POLICY.html`; federal-work text basis is17USC105. No agency seal is licensed for branding; source crops avoid website seals,third-party photography and any editorial material of the mirror publisher. Source attribution belongs in the editor's source record; preserve legal status and surrounding context. This documentary-prep rights assessment does not certify publication or every international jurisdiction.

`DOCUMENT_FACT_REFERENCES.csv` verifies booking period mismatch,revenue date window,false Magnises sale,brokerage discrepancy,unexecuted insurance,distinct investor/vendor loss categories,charging/plea/sentence chronology and final forfeiture. The settlement/nonadmission paragraph is primary-web verified but local release archive remainsHOLD. Final forfeiture$26,191,306.28 must not be replaced by the earlier March plea forfeiture. No asserted recovery of all forfeiture funds.

Maker source/pixel checks passed; independent review remains separate. No paid generation,TTS or montage was performed.
''',encoding='utf-8')
# Keep the scoped Git catalog self-contained, excluding browser profiles and rejected payloads.
for folder in ('ORIGINALS','CROPS','REFERENCE_PAGES','RENDERED_PAGES'):
    dest=REPO/folder;dest.mkdir(exist_ok=True)
    for p in (ROOT/folder).iterdir():
        if p.is_file():shutil.copy2(p,dest/p.name)
for name in ('DOCUMENT_CROP_REGISTRY.csv','DOCUMENT_FACT_REFERENCES.csv','VERIFIED_SOURCES.json','ORIGINAL_SOURCE_SHA256.csv','DOCUMENT_QC_SUMMARY.json','DOCUMENT_QC.md','CROP_CONTACT_1.jpg','CROP_CONTACT_2.jpg','VIDEO009_ORIGINAL_DOCUMENT_SOURCES.zip','build_document_crops.py'):
    shutil.copy2(ROOT/name,REPO/name)
print(json.dumps(report,indent=2))
