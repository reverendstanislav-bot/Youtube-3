from pathlib import Path
import re,csv,io
p=Path(r'C:\Users\KK\channel-audit-20261010\06_ANALYTICS\CHANNEL_FORENSIC_AUDIT')
for name in ['00_EXECUTIVE_VERDICT.md','02_CHANNEL_PERFORMANCE.md']:
 f=p/name;s=f.read_text('utf-8')
 if name.startswith('00'):
  s=s.replace('временно проверять возможность двух качественных longform в неделю','первые14дней предложить максимум1полностьюпроверенныйlong/week, затем2/week только при двухPASS, одномготовомbacklog и подтверждённойcapacity')
 else:
  s=s.replace('предпочтительныйcapacitytestMEDIUM','условнаяфаза2после14днейMEDIUM')
  a=s.index('Рекомендуемый тест послеутверждения cadence:')
  b=s.index('Productionbudget alternatives in08.',a)+len('Productionbudget alternatives in08.')
  s=s[:a]+'Рекомендуемый после принятия владельцем stagedpilot: первые14дней максимум1готовыйlong/week, Friday15:00America/Los_Angeles; затемTue/Fri2/week только после2полныхPASS,1готовогоbacklog и подтверждённогоtime/costbudget. Это организационное время, не доказанное оптимальноеUSокно. Порядок004→005сохраняется. В аудите календарь не менялся. Productionbudget alternatives in08.'+s[b:]
  s=s.replace('Wilson95%','Иллюстративные Wilson95% bounds для funnelviews/impressions, НЕ доверительный интервал причинногоCTRэффекта:')
 f.write_text(s,encoding='utf-8')
for name in ['00_EXECUTIVE_VERDICT.md','01_DATA_INVENTORY.md','11_48H_14D_30D_ACTION_PLAN.md','13_DATA_REQUESTS.md']:
 f=p/name;s=f.read_text('utf-8')
 if name.startswith('11'):
  s=s.replace('004: сначала скачать3уже завершённыхTTSjobs, собрать мастер и проверить','004: сначала проверить существующий808sWAV и связать его с3providerjobs; скачивать/собирать заново только при необходимости')
 if name.startswith('13'):
  s=s.replace('3jobIDs/costs/availablefiles/checksums/concatprovenance/audioQC; avoidduplicatepaidretry','first verify existing808sWAV candidate/hash/sourceparts;3jobIDs/costs/availablefiles/concatprovenance/audioQC;avoid duplicatepaidretry')
 if name.startswith(('00','01')):
  s+='\nЛокальное дополнение004: найден VIDEO004_HARRISON_V11_MASTER.wav,808s,48kHz/24bit/stereo; SHA2568c11be2619a6a84b7e1a6cbe0cb8c708d72dff556d1d737dd46f596ea21f65d7. Это кандидат: связь с providerparts, полныйdecode и слуховойQC не подтверждены. Репозиторноеpending не означает, что файла нет. Сначала проверить кандидата, а не повторять генерацию.\n'
 f.write_text(s,encoding='utf-8')
f=p/'09_ROOT_CAUSE_MATRIX.csv';rows=list(csv.DictReader(io.StringIO(f.read_text('utf-8'))));fields=list(rows[0]);fields.insert(fields.index('RECOMMENDED_ACTION'),'PRIORITY')
for r in rows:r['PRIORITY']='P0' if int(r['RANK']) in [1,5,6] else 'P1' if int(r['RANK'])<=8 else 'P2'
with f.open('w',encoding='utf-8',newline='') as h:
 w=csv.DictWriter(h,fields);w.writeheader();w.writerows(rows)
for name in ['02_CHANNEL_PERFORMANCE.md','04_SHORTS_AUDIT.md','11_48H_14D_30D_ACTION_PLAN.md']:
 f=p/name;s=f.read_text('utf-8')
 s=s.replace('evidence/video_','video_')
 if name.startswith('04'):
  s+='\nФактическийT7для последнегоShortDay14 доступен не раньшеDay21. Если feeddenominator или APV не доступны в экспорте, соответствующий тест/guardrail непроверяем: INCOMPLETE/INCONCLUSIVE, а не PASS по просмотрам.\n'
 if name.startswith('02'):
  s+='\nRootcauseCSV: impact1–5 = ожидаемая операционная/учебная ценность, не оценка причинного роста; effort1–5ordinal. Ratio — эвристика. Порядок учитывает risk/confidence и не сортируется исключительно по ratio. P0=измерение/сохранность/расходы; P1=креативныйтест; P2=следующееуточнение.\n'
 f.write_text(s,encoding='utf-8')
# Restore clear boundaries in Russian prose without changing evidence or links.
names=[x for x in p.glob('*.md') if x.name[:2] in ['00','01','02','04','11','12','13','14']]
for f in names:
 lines=[]
 for line in f.read_text('utf-8').splitlines():
  if 'http' not in line and 'SHA' not in line and 'sha' not in line and 'evidence/' not in line:
   line=re.sub(r'([А-Яа-яЁё])([A-Za-z0-9])',r'\1 \2',line)
   line=re.sub(r'([A-Za-z0-9])([А-Яа-яЁё])',r'\1 \2',line)
  lines.append(line)
 s='\n'.join(lines)+'\n'
 s=s.replace('**ПЛАН НА 48 ЧАСОВ**','**ПЛАН НА 48 ЧАСОВ**').replace('**ПЛАН НА 14 ДНЕЙ**','**ПЛАН НА 14 ДНЕЙ**').replace('**ПЛАН НА 30 ДНЕЙ**','**ПЛАН НА 30 ДНЕЙ**')
 f.write_text(s,encoding='utf-8')
print('Reconciled cadence, WAV evidence, priorities, timing and prose boundaries')
