from pathlib import Path
import csv,io
p=Path(r'C:\Users\KK\channel-audit-20261010\06_ANALYTICS\CHANNEL_FORENSIC_AUDIT')
refresh="""# Final GitHub refresh — 2026-10-10
Initial analytical baseline67b940a; final production-state verification0bc1e6f. origin/main advanced while the audit ran. This is a source refresh, not production work performed by the audit.

## Current004 truth, superseding historical baseline statements
- VIDEO_INDEX now lists Stage10_AUDIO_MASTER, not Stage08.
- Existing A/B/C source jobs, CI artifact11665053402 and808.000s WAV are now bound in10_AUDIO_MASTER.md with ZIP/source/master SHA256 and full decode. The master hash matches the independently found localWAV. Download/technical provenance is no longer a current missing-artifact finding.
- Stage10TECHNICAL_PASS/AUDITORY_QC_PENDING; audio lockfalse. Full listening, eight flagged regions, joins and Short cut edges remain open. ASR and PCM comparisons are not listening.
- Exactly four production Shorts SH01/SH02/SH04/SH08, not eight. The owner count lock supersedes historical maps. Technical previews are under30s, final spoken cut locksfalse.
- Stage11 structural25fps timeline checks and Stage12 source layers/Fusion static build have progressed.175editable compositions and a checksum-verified artifact exist;175is not a paid-generation count.
- 12_RESOLVE_EDITABLE_PACKAGE_V1_QC.md records no real Resolve import/runtimePASS, no exportedDRP, no final motion/render/pictureQC. Audio and publication readiness remain unverified; releaseNOT_READY.
- STATE retains historical bullets saying Stage12notstarted before later appendices supersede them. Consumers must read latest dated outcome and limits. This is chronology/registry usability risk, not proof latest work is missing.

## Updated recommendation
Do not redownload or regenerate already verified audio solely because baseline audit notes saidpending. First read current receipts; perform genuine auditory review and actual Resolve canary, then remaining picture/legal/release gates. No new generation or production action was performed by this audit.

## Sources
[STATE](../../../03_VIDEOS/VIDEO_004_VALVE_STEAM_MASS_ARBITRATION/STATE.md)
[Audio](../../../03_VIDEOS/VIDEO_004_VALVE_STEAM_MASS_ARBITRATION/10_AUDIO_MASTER.md)
[Resolve QA](../../../03_VIDEOS/VIDEO_004_VALVE_STEAM_MASS_ARBITRATION/12_RESOLVE_EDITABLE_PACKAGE_V1_QC.md)
[Current index](../../../02_PIPELINE/VIDEO_INDEX.csv)

Paths above are from evidence/; resolve four parent levels to repository root if viewing source directly. Canonical repository files were fetched read-only, never edited by this audit.
"""
# Correct link relativity: audit/evidence -> audit -> analytics -> root = three levels.
(p/'evidence/repo_refresh_0bc1e6f.md').write_text(refresh,encoding='utf-8')
for f in p.glob('*.md'):
 if f.name[:2].isdigit():
  s=f.read_text('utf-8')
  banner='> Final production-state refresh: **0bc1e6f**. Initial findings at67b940a are historical where superseded. Valve audio technical verification is now complete; full listening/Resolve runtime/final release gates remain open. Four production Shorts. See [final source reconciliation](evidence/repo_refresh_0bc1e6f.md).\n\n'
  s=banner+s
  if f.name.startswith('14'):
   s=s.replace(banner,'> Актуальность производства повторно проверена по **0bc1e6f**. У Valve техническая проверка аудио завершена; слуховой QC, Resolve и готовность к публикации остаются открытыми. [Подробная сверка](evidence/repo_refresh_0bc1e6f.md).\n\n')
   s=s.replace('Локальный WAV на 808 секунд существует, но связь с исходными заданиями и полный слуховой QC не подтверждены. Сначала проверить этот файл; повторять генерацию преждевременно.','В обновлённом Git подтверждены происхождение, скачивание и полный технический decode WAV на 808 секунд; контрольная сумма совпадает с локальным файлом. Слуховой QC пока открыт. Также готов пакет 175 редактируемых композиций, но его работа в Resolve и итоговый монтаж не проверены. Следующий шаг — слуховая проверка и пробный импорт, а не повторная генерация.')
   s=s.replace('проверка хвоста eBay и существующего аудио Valve без новых платных заданий','проверка хвоста eBay, слуховой QC аудио Valve и проверка композиций в Resolve без новых платных заданий')
  if f.name.startswith('11'):
   s=s.replace('004: сначала проверить существующий 808s WAV и связать его с 3 providerjobs; скачивать/собирать заново только при необходимости','004: происхождение и decode уже подтверждены в актуальном Git; выполнить слуховой QC мастера, стыков и четырёх Shorts, затем Resolve canary')
   s=s.replace('004: сначала проверить существующий808sWAV и связать его с3providerjobs; скачивать/собирать заново только при необходимости','004: происхождение и decode уже подтверждены; слуховой QC и Resolve canary')
  f.write_text(s,encoding='utf-8')
f=p/'09_ROOT_CAUSE_MATRIX.csv';rs=list(csv.DictReader(io.StringIO(f.read_text('utf-8'))));fields=list(rs[0])
rs[4]['EVIDENCE']='002/003 historical release registry gaps;004 at0bc1e6f technically verified audio/source/Fusion artifacts, auditory/Resolve/runtime release gates open'
rs[4]['RECOMMENDED_ACTION']='Read latest receipts; close actual auditory/Resolve/picture/release gates; do not redownload/regenerate verified artifacts'
with f.open('w',encoding='utf-8',newline='')as h:
 w=csv.DictWriter(h,fields);w.writeheader();w.writerows(rs)
# Independent review resolution is written by lead, not impersonating independent reviewer.
text="""
## Lead resolution after independent review
The independent review above was completed on arriving report versions. The lead then reread the final package and resolved its enumerated blockers: readable03/06 and natural Russian14; Apple ebooks topic corrected; staged cadence unified including09; explicitPRIORITY and ordinal impact/effort interpretation; Day21/28Shorts followup and inaccessible-denominatorINCONCLUSIVE; observed-data chart with proportional eBay marker; existingWAV first.
A final live GitHub refresh to0bc1e6f supersedes the baseline004 missingdownload/provenance finding. Current audio technicalPASS and175Fusion static build are recorded, while auditory/Resolve/runtime/release gates remain open. Exact Studio-name DK HQ candidate was separately hashed/probed/frame-inspected and decoded; timestamp warnings are disclosed, no blanketcleanPASS.
This paragraph is a lead reconciliation, not a claim that the independent reviewer reran every final binary check. Remaining source/age/denominator/listening/attribution limits are intentional and explicit.
"""
with (p/'evidence/independent_review.md').open('a',encoding='utf-8')as h:h.write(text)
print('Live production refresh and independent-review resolutions recorded')
