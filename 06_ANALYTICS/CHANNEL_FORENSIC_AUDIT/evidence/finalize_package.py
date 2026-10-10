from pathlib import Path
import csv,io,json,re,xml.etree.ElementTree as ET
p=Path(r'C:\Users\KK\channel-audit-20261010\06_ANALYTICS\CHANNEL_FORENSIC_AUDIT')
f=p/'09_ROOT_CAUSE_MATRIX.csv';rows=list(csv.DictReader(io.StringIO(f.read_text('utf-8'))));fields=list(rows[0])
rows[7]['RECOMMENDED_ACTION']='Staged pilot: first14days max1/week; conditional2/week after2fullPASS,1finishedbacklog and verifiedcapacity; ownerdecision required'
with f.open('w',encoding='utf-8',newline='') as h:
 w=csv.DictWriter(h,fields);w.writeheader();w.writerows(rows)
f=p/'evidence/performance_observed.svg';s=f.read_text();s=s.replace('width="3" height="32"','width="1.6323" height="32"');f.write_text(s)
add="""
## Final reconciliation: exact Studio-named DistroKid HQ candidate

Studio's filename is UMG_DISTROKID_FINAL_ENDSCREEN_YOUTUBE_FINAL_HQ.mp4. The exact-name candidate was located in C:/Users/KK/Downloads, and was independently inspected; it is NOT byte-identical to the initially inspected spaced-name delivery file. This section supersedes that earlier candidate for release-file technical conclusions.

- SHA-256: f2b4a827a1feb78e54e9766952b34d25c713b6236e046667921c23203b3ea037.
- Size188,989,202 bytes; container duration1008.422031s; H.2641920x1080,25fps,25,210frames, video bitrate1,304,321bit/s; AAC48kHz stereo188,905bit/s; container1,499,286bit/s.
- Filename matching plus local provenance is stronger evidence than the former candidate, but no source upload hash/receipt was available to prove byte identity with the actual server upload. No online-transcode verdict is inferred.
- Measured input loudness -16.32LUFS-I, true peak -3.31dBTP, LRA1.90LU. Audio NOT VERIFIED BY LISTENING.
- Exact-name frames at0/5/15/30/60/300/600/750/983/1003s were directly inspected by the lead. The same authored document scenes, overlap of outgoing/incoming headlines at5s and750s, and end-screen background at1003s are present. Whole complaint paragraphs remain too small for mobile reading; the large labels are clear. No burned subtitles were present in these sampled frames. This is sampled visual inspection, not continuous playback or audio-sync certification.
- The original filtered full-decode log reached25,210frames but emitted a non-monotonic DTS warning at the null output muxer. That warning must not be silently erased or equated with a damaged source. A separate passthrough full-decode verification is recorded in video_003_actual_hq_decode_errors.log; status is documented in the final integrity report.
- A low bitrate alone is not a quality FAIL, eligibility defect or demonstrated cause of retention loss. No master was replaced or reuploaded.

Evidence: [probe](video_003_actual_hq_probe.json), [exact-name contact sheet](video_003_hq_contact.png), [original decode and loudness log](video_003_actual_hq_decode.log), [passthrough errors](video_003_actual_hq_decode_errors.log).
"""
with (p/'03_VIDEO_BY_VIDEO_AUDIT.md').open('a',encoding='utf-8') as h:h.write(add)
add2="""
## Current published-title supplement
These are the actual Studio titles on2026-10-10; repository working titles above are retained only as historical baselines.

|Current title|C|S|Q|M|A|Total|Interpretation|
|---|---:|---:|---:|---:|---:|---:|---|
|They Criticized eBay. Then the Harassment Started.|2|1|2|2|2|9|Clear escalating human conflict and opening alignment. Avoid turning company-level wording into an unsupported claim that every executive ordered the acts. Eleven impressions cannot validate effectiveness.|
|The Lawsuit That Could Break DistroKid|2|1|1|2|1|7|Clear defendant and threat, but 'break' promises a business-survival stake not established by the reviewed complaint/opening. Prefer a concrete disputed action or legal question; do not infer insolvency, inevitable damages or liability.|

The current live DistroKid thumbnail WHO OWNS THE RISK was directly viewed in Studio onOct10. The historic eBay/Adobe visible-thumbnail observations dateOct9; their full current variant images were not recaptured. Exact controls must be recorded before any later experiment. These scores are editorial judgments, never CTR predictions.
"""
with (p/'06_PACKAGING_AND_RETENTION.md').open('a',encoding='utf-8') as h:h.write(add2)
# Update owner report with verified candidate finding, preserving uncertainty.
f=p/'14_OWNER_REVIEW_RU.md';s=f.read_text('utf-8');s=s.replace('У DistroKid имя загруженного файла отличается от первоначально найденного локального кандидата: выводы о сжатии надо привязывать к точному мастеру.','Точный по имени HQ-кандидат DistroKid найден и отдельно проверен: он отличается от первоначального файла; его контейнерный битрейт — около 1,50 Мбит/с. Само слово HQ не доказывает качество, а низкий битрейт сам по себе не доказывает дефект. Контрольная сумма исходной загрузки в YouTube недоступна, поэтому полная идентичность серверному источнику не подтверждена.');f.write_text(s,encoding='utf-8')
required=['00_EXECUTIVE_VERDICT.md','01_DATA_INVENTORY.md','02_CHANNEL_PERFORMANCE.md','03_VIDEO_BY_VIDEO_AUDIT.md','04_SHORTS_AUDIT.md','05_COMPETITOR_INTELLIGENCE.md','06_PACKAGING_AND_RETENTION.md','07_TOPIC_MARKET_FIT.md','08_PRODUCTION_EFFICIENCY.md','09_ROOT_CAUSE_MATRIX.csv','10_EXPERIMENT_BACKLOG.csv','11_48H_14D_30D_ACTION_PLAN.md','12_FINAL_STRATEGIC_DECISION.md','13_DATA_REQUESTS.md','14_OWNER_REVIEW_RU.md']
result={'required_count':len(required),'missing':[n for n in required if not(p/n).exists()],'broken_local_links':[],'csv_rows':{}}
for n in required:
 s=(p/n).read_text('utf-8')
 if '\ufffd' in s or 'continuouscontinuous' in s:raise ValueError('corrupttext:'+n)
 if n.endswith('.csv'):result['csv_rows'][n]=len(list(csv.DictReader(io.StringIO(s))))
 for dest in re.findall(r'\]\(([^)]+)\)',s):
  if dest.startswith(('http','C:','/','#','<')):continue
  if not(p/dest.split('#')[0]).exists():result['broken_local_links'].append([n,dest])
json.loads((p/'evidence/studio_snapshot.json').read_text())
json.loads((p/'evidence/shorts_metrics.json').read_text())
ET.parse(p/'evidence/performance_observed.svg')
result['owner_answers']=len(re.findall(r'^## \d+\.',(p/'14_OWNER_REVIEW_RU.md').read_text('utf-8'),re.M))
(p/'evidence/package_integrity.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
