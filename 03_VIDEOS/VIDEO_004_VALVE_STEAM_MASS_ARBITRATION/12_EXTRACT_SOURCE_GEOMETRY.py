#!/usr/bin/env python3
"""Collect verified source PDF geometry for VIDEO004. Never author invented quotes."""
import hashlib, json, os, pathlib, re, sys, urllib.request
import fitz
D=pathlib.Path(__file__).resolve().parent
OUT=D/"12_SOURCE_DOCUMENT_GEOMETRY.json"
PDFS=D/"12_SOURCE_PDF_DOWNLOADS"
PDFS.mkdir(exist_ok=True)
sources={
"S004":"https://cases.justia.com/federal/district-courts/washington/wawdce/2:2024cv01717/340613/169/0.pdf",
"S005":"https://cases.justia.com/federal/district-courts/washington/wawdce/2:2024cv01717/340613/192/0.pdf",
"S006":"https://www.adr.org/media/jixnnl1x/consumer_mass_arbitration_and_mediation_fee_schedule.pdf",
"S007":"https://www.courts.wa.gov/opinions/pdf/865854.pdf"
}
targets={
"S004":[("2023 contract contextual reference","April 25, 2023"),("2012 arbitration origin","individual binding arbitration"),("first claims count","997"),("claimant total","4,991 claimants"),("defendants count","572 Defendants"),("four claimant turning point","four of the twenty-five"),("Steam contract change date","September 26, 2024"),("retroactive rule","retroactive forum"),("AAA refusal","AAA declined"),("Valve civil case procedural filing","struck the petition"),("ruling qualification","unconscionable as applied"),("preliminary conclusion","motion fails")],
"S005":[("appellate certification","CERTIFIES"),("appeal stay","STAYED pending"),("court grant","GRANTS the motion")],
"S006":[("fee mechanism","Initiation Fee"),("fee administration","Administrative Fees"),("mass arbitration","CONSUMER MASS ARBITRATION")],
"S007":[("separate Bucher litigation","Bucher Law")]
}
report={"status":"SOURCE_PDF_GEOMETRY_PREFLIGHT","source_count":len(sources),"sources":{},"coordinate_convention":"PDF points from PyMuPDF, origin top-left, 0-based page number, source page width/height, not timeline pixels. Revalidate after choosing actual source crop/transform.","no_document_replica":True}
for sid,url in sources.items():
 item={"url":url,"status":"NOT_FETCHED","matches":[],"errors":[]}
 report["sources"][sid]=item
 try:
  req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 (documentary source verification)"})
  data=urllib.request.urlopen(req,timeout=45).read()
  if not data.startswith(b"%PDF"):raise ValueError("Not PDF response")
  raw=PDFS/(sid+".pdf")
  raw.write_bytes(data)
  doc=fitz.open(stream=data,filetype="pdf")
  item.update(status="PDF_FETCHED_AND_PARSED",sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),page_count=len(doc))
  for purpose,phrase in targets[sid]:
   hits=[]
   for idx,page in enumerate(doc):
    for rect in page.search_for(phrase):
     hits.append({"page_index_zero_based":idx,"printed_page_number":idx+1,
       "page_size_pdf_pt":[round(page.rect.width,2),round(page.rect.height,2)],
       "line_rect_pdf_pt_top_left":[round(rect.x0,2),round(rect.y0,2),round(rect.x1,2),round(rect.y1,2)],
       "line_rect_normalized":[round(rect.x0/page.rect.width,5),round(rect.y0/page.rect.height,5),round(rect.x1/page.rect.width,5),round(rect.y1/page.rect.height,5)]})
     if len(hits)>=8:break
    if len(hits)>=8:break
   item["matches"].append({"purpose":purpose,"query":phrase,"match_count":len(hits),"exact_pdf_geometry":bool(hits),"hits":hits})
 except Exception as e:item["status"]="FETCH_OR_PARSE_FAILED";item["errors"].append(str(e)[:300])
OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
print(json.dumps({k:{"status":v["status"],"matches":sum(x["match_count"] for x in v["matches"])} for k,v in report["sources"].items()}))
