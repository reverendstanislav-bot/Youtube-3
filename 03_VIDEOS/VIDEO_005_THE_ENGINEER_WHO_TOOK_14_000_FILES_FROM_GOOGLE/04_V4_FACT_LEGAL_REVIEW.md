# VIDEO 005 — Stage04 Full Independent Fact/Legal Review — V4 RU (2026-10-13)

**Final decision: FAIL (2 HIGH blockers).** This re-audit applies ONLY to `05_SCRIPT_V4_RU.md` (original sha `d6383b05b07fd98cef43442237b4a2f2d2206631`), NOT English V3 or V4 English that does not yet exist. Owner accepted the dramatic direction in chat; owner creative approval does not waive legal gates.

## Method and coverage
- **55/55 unmodified Russian narration paragraphs** inspected individually, same exact spoken texts in `04_V4_PARAGRAPH_AUDIT.csv`. Count: **48 PASS / 5 MEDIUM WARN / 2 HIGH FAIL**.
- **8/8 exact one-paragraph contiguous Shorts** read as stand-alone claims, verified byte-for-byte against full V4 screenplay; `04_V4_SHORTS_ISOLATION_QC.csv`. Count **5 PASS / 3 WARN (S01, S05, S08) / 0 FAIL**. Runtime and Harrison English timing NOT measured, and nobody is claiming <=30sec.
- Cross-checked distinct allegations vs findings vs settlement, party positions, chronological events, money, parties and legal doctrines against locally indexed claim/event/source ledgers and the **actual primary texts**: Delaware Supreme McElrath 2020; DOJ 2020; May2017 injunction; Jan2018 discovery sanctions order; March2023 federal appeal; Jan2025 bankruptcy opinion. The two federal PDF opinions were directly read and their source pages visually checked (2023 p3, 2025 p6/p8/p15/p23). Historical G04 V3 PASS not inherited.
- Script narrative/retention approval not assessed here; this stage is FACT/LEGAL ONLY.

## Blocking issues
### Q046 — HIGH / A00-P03 — inverted direction of contractual obligations
**V4 quote:** «В другой — обязательства Google перед бывшим сотрудником и условия его перехода в новую компанию».
**Problem:** wrong legal subjects: it was Levandowski's **employment duties owed TO Google**, and separately **Uber's disputed conditional indemnification obligation** toward Levandowski. Claim that **Google** owed obligations TO its former employee in this context inverts the legal issue.
**Primary:** S032 (2025 bankruptcy decision background); S033 (2023 federal decision on Google Arbitration and Uber indemnity).
**Required:** rewrite **that paragraph only** to say «обязательства бывшего инженера перед Google и его спорные требования к Uber по договору о возмещении ответственности».
**Consequence:** introduction materially misstates second legal proceeding → hard FAIL.

### Q047 — HIGH / A09-P05 — final takeaway attributes Uber Main Payment to 2016 indemnity agreement
**V4 quote:** «Но другой платёж вырос из условий сделки, подписанной годами раньше».
**Contrary court holding:** bankruptcy court on Jan 24, 2025: main Uber payment was made **under the 2022 Global Settlement Agreement**, **not pursuant to** the contested 2016 indemnification agreement; no court declaration that indemnity contract was enforceable against Uber, and the agreement was terminated with settlement. See S032 pp15/23. Settlement resolves disputed obligation, it does not prove Uber paid because the 2016 contract legally required it.
**Required:** change conclusion to «условия сделки породили спор, который завершился отдельным соглашением в 2022 году; уже по нему Uber перечислила Google засекреченный платёж». Keep a sharp ending without false statutory/contractual cause.
**Consequence:** central promised 'why payment?' answer currently overclaims proven contractual duty.

## Medium precision / standalone issues
- **Q048 MEDIUM | A00-P01 / S01:** «14 тысяч файлов, которые один инженер скопировал **в Google**» semantically could say copied INTO Google; DOJ confirms copied **FROM Google's internal server**. Edit to «скачал с серверов Google» in main film and re-extract S01.
- **Q049 MEDIUM | A00-P02:** hook says 2022 payment chain 'was connected by old contract' without distinguishing 2016 disputed indemnity from 2022 *actual basis* of payment. Clarify as dispute vs payment under 2022 settlement, without opening 15-second legal lecture.
- **Q050 MEDIUM | A04-P03 / S05:** «Uber использовала **украденные коммерческие секреты**» may prematurely presuppose proven source of the secrets in the 2017 case (though Levandowski later separately pleaded guilty on one specific Google document). Prefer «предположительно присвоенные секреты Waymo» in the negative clause. Preserve 'alleged' status; re-extract one-piece S05.
- **Q051 MEDIUM | A08-P04 / S08:** March2023 S033 says Uber was to pay $2m **to estate**; Jan2025 S032 summarizes a $2m payment **to Mr Levandowski to fund the Plan**. Both agree **plan financing**. Without adjudicating a bank-transfer route, say «ещё два миллиона долларов для финансирования плана банкротства» or explicitly attribute the estate wording to the March2023 court. Separate sealed principal is confirmed executed by May20 2022.
- **Q052 MEDIUM | A08-P05:** main payoff needs express 2025 legal guardrail: underlying 2016 indemnification terms were **contested**, and court later categorized main payment as made pursuant to independent 2022 settlement. Do not label the sealed payment an adjudicated duty under 2016 contract.

## Eight Shorts fact/legal isolation
| Short | Main text ID | Result | Issue |
|---|---|---|---|
| S01 | A00-P01 | **WARN** | Ambiguous 'в Google' transfer direction; Q048 |
| S02 | A01-P03 | PASS | 14k downloads proven; all Uber use unproven |
| S03 | A02-P03 | PASS | Conditional ~$680m headline vs upfront $100k |
| S04 | A03-P04 | PASS | Stroz Levandowski-specific no-evidence-of-transfer preserved |
| S05 | A04-P03 | **WARN** | 'украденные' presupposition; Q050 |
| S06 | A05-P04 | PASS | Mar2016 discs vs Jan2018 order optional inference |
| S07 | A06-P02 | PASS | ~245m equity settlement, not jury verdict |
| S08 | A08-P04 | **WARN** | $2m exact payee wording conflict between S033/S032; Q051 |

## Primary source mapping (openable)
- S008 — Supreme Court Delaware 2020 Otto acquisition terms Stroz due diligence, allegations and stock agreement: https://law.justia.com/cases/delaware/supreme-court/2020/181-2019.html
- S010 — DOJ admission December 2015 14k SVN files and different personal Google Drive document: https://www.justice.gov/usao-ndca/pr/former-uber-self-driving-car-executive-signs-agreement-plead-guilty-theft-trade-secrets
- S011 — DOJ August2020 one-count plea, 33 originally charged, 18 months: https://www.justice.gov/usao-ndca/pr/former-uber-executive-sentenced-18-months-jail-trade-secret-theft-google
- S003 — 2017 preliminary injunction partial order: https://law.justia.com/cases/federal/district-courts/california/candce/3:2017cv00939/308136/433/
- S031 — 2018 discs delayed disclosure/optional adverse jury inference: https://docs.justia.com/cases/federal/district-courts/california/candce/3:2017cv00939/308136/2585
- S032 — 2025 court: 2020 judgment, 2022 funding, actual main payment under settlement not indemnity, tax gross income: https://www.govinfo.gov/content/pkg/USCOURTS-canb-3_20-bk-30242/pdf/USCOURTS-canb-3_20-bk-30242-0.pdf
- S033 — 2023 court: settlement sealed direct payment and $2m estate, payment completed by May20 2022: https://www.govinfo.gov/content/pkg/USCOURTS-cand-4_22-cv-02781/pdf/USCOURTS-cand-4_22-cv-02781-0.pdf

## Eight G04 hard metric grades (0–5; every dimension >=4 and zero blockers required)
| Metric | Score | Why |
|---|---:|---|
| Claim/source traceability | 4 | 55 tagged evidence families; needs individual claim-ID granular trace after legal fixes |
| Allegation/status precision | 3 | Misidentified debtor/creditor in A00-P03 and guilt-presupposition S05 |
| Procedural chronology | 5 | 2015 downloads→2016 acquisition→2018 settlement→2020 judgment→2022 payment→2025 tax order |
| Quotation/context fidelity | 4 | Source text original accessible; attribution refinements needed |
| Current-status freshness | 4 | 2025 court order checked; Stage16 prepublication refresh still required |
| Numerical accuracy | 4 | Known numbers/units consistent; $2m court descriptions differ by payee wording |
| Party-position fairness | 4 | Waymo/Uber rebuttal both included |
| Primary-source sufficiency | 5 | S003/S008/S010/S011/S031/S032/S033 directly examined |

**FACT/LEGAL V4: FAIL**, since 2 blockers and metric below 4. No auto-propagation of G04 V3 PASS. Rewriting/correcting V4 text belongs to a separate owner-authorized Stage05 scope.

## Handoff / legal fix acceptance
If separately authorized: minimally rewrite exactly seven identified paragraphs (A00-P01/P02/P03; A04-P03; A08-P04/P05; A09-P05). Keep all other 48 paragraphs **verbatim**. Re-extract S01/S05/S08 from their modified long-form paragraphs. Rebuild exact V4.1 trace, recheck all 55 paragraphs and eight Shorts independently. **Do not** start Stage06, audio, image or video production.
