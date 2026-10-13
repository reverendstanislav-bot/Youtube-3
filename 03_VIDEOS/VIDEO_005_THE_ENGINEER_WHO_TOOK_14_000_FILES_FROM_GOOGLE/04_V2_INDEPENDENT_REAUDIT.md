# VIDEO 005 — Stage 04 independent full re-audit of V2
**Date:** 2026-10-13 | **Script frozen for review:** `05_SCRIPT_V2.md` blob `bf2804139c1ac6e0560e78949ba9ab6dc2370a12`
**FINAL G04 V2 VERDICT: FAIL.** Independent from the Stage05 targeted self-recheck; original V1 G04 FAIL remains historical and unchanged.

## Exact scope and count
- Read all 53/53 **verbatim V2** narration paragraphs (2841 spoken words per Stage05 count) across A00–A09, not only seven Stage05 edits.
- Compared claim IDs, party positions, procedure, numbers, chronology and court treatment against linked `CLAIMS_LEDGER.csv` / `SOURCE_INDEX.csv` and directly checked key original DOJ, Delaware Supreme, May2017 Alsup, Jan2018 Alsup, March2023 federal and January2025 bankruptcy primary texts. Reports/secondary coverage were used only for the contemporaneous approximate stock valuation.
- Examined all 8/8 **verbatim one-paragraph contiguous** Shorts *in isolation*; no context silently borrowed from adjoining narration. Confirmed matches to `05_SHORTS_MAP_V2.csv`.
- **Long-form:** 49 PASS, 2 WARN (scope), 2 FAIL (material fact).
- **Shorts:** 7 PASS_TEXT, 1 WARN_TEXT (S04), 0 isolated FAIL. No real Harrison audio/duration tested.
- Per-paragraph, full exact text, claim IDs, sources and findings: `04_V2_PARAGRAPH_AUDIT.csv`.
- Per-Short, full exact excerpt, source and isolated finding: `04_V2_SHORTS_ISOLATION_QC.csv`.

## BLOCKING factual/legal findings
### Q043 — HIGH | A06-P05 | impossible financial comparison
**Verbatim problem:** “This case would produce the one number larger than Uber's stock settlement”.
**Contradiction:** earlier A06-P02 identifies the Uber–Waymo stock settlement as **approximately $245 million**. A07-P02 and A00-P01 identify the individual's later civil judgment as **approximately $179 million**. $179m is **less**, not greater, than $245m.
**Sources:** S032 (March 2020 personal $179,047,998.64 judgment); S022/S023 (contemporaneous ~ $245m stock value); S005 (2018 settlement dismissal).
**Acceptance:** Remove/rewrite numerical comparison **inside canonical long-form**, keeping legal matters separate. Recheck the resulting full paragraph and neighboring transition.

### Q044 — HIGH | A08-P04 | wrong payee + speculation about sealed number
**Verbatim problems:** “A separate two-million-dollar payment was provided to Levandowski to fund the bankruptcy plan”; “the larger, confidential payment”.
**Record:** The March 2023 federal decision says Uber would pay **$2 million to the bankruptcy estate** (for the proposed plan), *not to Levandowski personally*. The direct Uber→Google “Main Uber Payment” was **sealed**; the public cited decision does **not** establish that its amount exceeded $2m.
**Source:** S033, U.S. District Court for ND Cal, March 14, 2023, Document 77 pp.3–4; S032 Jan24 2025 bankruptcy opinion.
**Acceptance:** Change payee to **bankruptcy estate / funding the plan**, and remove “larger” and any unsupported comparative-size language. Do not invent a value for the sealed payment.

## MEDIUM scope caveat, including one Short
### Q045 — MEDIUM | A03-P03, A03-P04 and S04
**Problem:** “people around the deal” / “former Google employees” immediately precedes “the information” in Stroz's negative transfer finding. This can overgeneralize the specific Stroz quote, which addressed **Levandowski's retained Google confidential information**, to all employees or all documents.
**Source:** S008, McElrath v. Kalanick, Delaware Supreme Court (2020), footnote citing Stroz report.
**Acceptance:** Scope the report's finding to Levandowski's Google data **inside both paragraphs**, and re-extract S04 verbatim from corrected A03-P04. Preserve the distinction “no evidence found of transfer” vs. “impossible that any information transferred”.

## Original Stage05 repairs independently tested
- A00-P01 and S01: qualified corporate indemnity mechanism inside excerpt — supported.
- A02-P06: Stroz forensic inquiry before 2016 acquisition close — supported.
- A03-P06: wrong-recipient email not sole cause — supported.
- A04-P01: design resemblance alleged — supported.
- A05-P03/P04 and S05: March 2016 reported disks vs Jan 2018 late-disclosure inference, permissive instruction — supported.
- A07-P05: contract coverage attributed to Levandowski's argument and Uber's opposing position — supported.
These specific G04 V1 defects are **repaired in V2**, but the two newly found HIGH defects block G04 V2.

## Eight Shorts isolation decisions
| Short | Canonical paragraph | Verdict | Legal conclusion |
|---|---|---|---|
| S01 | A00-P01 | PASS_TEXT | Personal judgment; conditional Uber indemnity question |
| S02 | A01-P03 | PASS_TEXT | ~14k file transfer; no proof Uber used all |
| S03 | A02-P03 | PASS_TEXT | $680m potential vs $100k upfront |
| S04 | A03-P04 | **WARN_TEXT** | Stroz negative-finding scope needs precision |
| S05 | A05-P04 | PASS_TEXT | Reported discs / late disclosure / optional inference |
| S06 | A06-P02 | PASS_TEXT | 2018 stock settlement, no jury verdict |
| S07 | A07-P02 | PASS_TEXT | Individual $179m arbitration judgment and bankruptcy |
| S08 | A08-P05 | PASS_TEXT | Main Uber payment sealed; separate $2m funding |
None has been timed against Harrison; 20–27s estimates / <=30sec hard export remain Stage11, not this factual gate.

## Hard metrics (0–5, standard requires >=4 across all eight and NO blocker)
| Metric | Score | Reason |
|---|---:|---|
| Claim-to-source traceability | 4 | 53/53 mapped; source-scope wording needs repair |
| Allegation/status precision | 4 | Plea, civil settlement, preliminary rulings and party positions separated |
| Procedural chronology | 5 | Stroz and 2016 disks chronology repaired; Feb2018 trial correctly not verdict |
| Quote/context accuracy | 4 | No invented literal court quote; Stroz paraphrase too broadly scoped |
| Current-status freshness | 4 | Core court records checked through 2025; publication still requires separate Stage16 freshness |
| Numerical accuracy | **2 FAIL** | $179m falsely called larger than ~$245m; unsupported ordering of sealed payment |
| Party-position fairness | 4 | Waymo accusations and Uber denial both attributed |
| Primary-source sufficiency | 4 | DOJ, Delaware and federal/bankruptcy court first-party record inspected; stock value supported contemporaneously |

**G04 V2 FAIL:** HIGH Q043 + HIGH Q044, plus MEDIUM Q045. Gate not waived. Stage01 and Stage02 remain OWNER HOLD; Stage06 NOT_STARTED, Stage07 lock forbidden; no narration, paid generations, images, edit, rights clearance or timing run.

## Primary records consulted (content and court posture)
- S010 DOJ: https://www.justice.gov/usao-ndca/pr/former-uber-self-driving-car-executive-signs-agreement-plead-guilty-theft-trade-secrets
- S008 Delaware Supreme: https://law.justia.com/cases/delaware/supreme-court/2020/181-2019.html
- S003 May2017 partial provisional relief: https://law.justia.com/cases/federal/district-courts/california/candce/3:2017cv00939/308136/433/
- S031 Jan2018 five-discs order: https://docs.justia.com/cases/federal/district-courts/california/candce/3:2017cv00939/308136/2585
- S033 March2023 federal appeal, original: https://www.govinfo.gov/content/pkg/USCOURTS-cand-4_22-cv-02781/pdf/USCOURTS-cand-4_22-cv-02781-0.pdf
- S032 Jan2025 bankruptcy tax order: https://www.govinfo.gov/content/pkg/USCOURTS-canb-3_20-bk-30242/pdf/USCOURTS-canb-3_20-bk-30242-0.pdf
- S005 Feb2018 dismissal: https://business.cch.com/ipld/WaymoUberTechnologiesDiismissal20180209.pdf
- S022 contemporaneous equity valuation: https://techcrunch.com/2018/02/09/uber-settles-lawsuit-with-waymo/

## Strict handoff
**Stop here.** Next action only if owner separately authorizes: **Stage05 V3 targeted source-grounded repair** of A06-P05, A08-P04, A03-P03/A03-P04 including S04; retain immutable V2, recalculate trace and Shorts, rerun independent G04 V3. No Stage06.
