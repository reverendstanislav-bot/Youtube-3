# VIDEO008 — Stage 01 Evidence Research (2026-10-26)
**Status:** CORE SOURCE-BOUNDED RESEARCH DELIVERED; INDEPENDENT-SOURCE DESK QC COMPLETE **WITH HOLDS**. Do not hand off to Stage02 until HIGH items closed.

## Scope, acquisition, method
- Primary SEC S-1 accepted Oct 26 09:00:11 ET, CIK 2130357, accession 0001628280-26-067168; original document `anthropicpbc-sx1.htm` 14,169,143 bytes; index catalogs 87 documents. Main HTML **exceeded the browser tool's 4 MB single-page extraction limit**. The filing was therefore investigated using accessible SEC-indexed excerpt passages, prospectus financial note/page locators, SEC original exhibits 4.4, 4.5, 4.6, 4.7, 10.14, 99.1 and 99.2, public Anthropic research disclosures, and independent Reuters/Kepler/Axios cross-checks. **No claim is made to a complete offline 14MB SEC S-1 archival/full-text byte audit**. This is the remaining research blocker.
- `SOURCE_INDEX.csv` IDs SRC001–SRC015 (15); `CLAIMS_LEDGER.csv` CLM001–CLM044 (44); `CASE_EVENT_LEDGER.csv` EVT001–EVT018 (18); each item is source-linked and classified.
- Primary filing index: https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/0001628280-26-067168-index.html
- Main SEC S-1: https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm
- Supplementary source-citation crosswalk: https://kepler.ai/research/financial/s1-anthropic/ (441 SEC passage locators and calculation disclosures). Secondary, not substitute for source when disputed.
- Independent contemporaneous cross-check: https://www.reuters.com/legal/transactional/anthropic-opens-books-ais-explosive-growth-staggering-costs-2026-10-26/; regulator update https://www.axios.com/2026/10/26/ftc-ai-safety-probe-anthropic-openai (attributed secondary reporting only).

## A. Narrative distinction — biggest story
On first public SEC S-1, Anthropic reports for Jan–Jun 2026 ($ millions unless noted):
| GAAP / cash / non-GAAP | FY2025 | H1 2025 | H1 2026 | SEC locator |
| --- | ---: | ---: | ---: | --- |
| Revenue | 4,585 | 1,163 | 16,286 | F-7 |
| Cost compute/infrastructure | 7,326 | 2,334 | 8,945 | F-7 / MD&A |
| Operating income (loss), GAAP | (8,060) | (2,135) | (693) | F-7 |
| Financing instrument fair-value charge (notes, derivatives, SAFEs) | (34,308) | (10,942) | (72,388) | F-7; MD&A p150 |
| Other income/expense, net |  |  | (8,757) | F-7 |
| Net loss, GAAP | (41,965) | (12,969) | (80,748) | F-7 |
| Net cash from operating activities | (2,637) | (1,513) | +3,929 | F-12 / MD&A p168 |
| Net cash from financing | 19,960 | 4,749 | +110,774 | F-12 |
| Adjusted operating income, **non-GAAP** | (4,854) | (1,849) | +1,618 | MD&A p155–156 |

**Arithmetic bridge independently recalculated:** operating loss (693) + interest income 1,111 - note and derivatives FV charge 72,388 - other net expense 8,757 - taxes 21 = **-80,748** ($ millions). Negative values are accounting items; `GAAP net loss` is NOT interchangeable with cash burn. Cashflow reconciliation also shows $8,720M of additional other-financial-instrument fair-value recognition; do not mix categories or double-count in narrative. Exact reconciliation must be captured directly in complete statement before production lock.

**Second turn:** Quarterly Q1 2026 GAAP operating loss -$1,667M; Q2 operating income +$974M. H1 operating loss -$693M is the sum. June quarter revenue $11,555M; March quarter $4,731M. H1 revenue increased ~1,300% year over year, not exactly 1,300x.
**Liquidity as of June30:** cash/equivalents $112,389M and short-term investments $19,262M; sum $131,651M. Reported financing inflows of $110,774M are NOT sales, and are a major driver of cash position. $3,929M H1 positive cash from operations; simplified operating cash less purchase of property/equipment $482M => $3,447M **researcher-calculated FCF**, not an audited issuer KPI or guarantee of future positive cashflow. Anthropic expressly forecasts significant capital demands and negative combined operations/investing cashflow as infrastructure buildout continues.
**Limitations:** H1 2026 statement is unaudited interim. Gross revenue policy, platform fees, non-GAAP exclusions and potential IPO RSU catch-up expenses alter comparisons. No claim of insolvency or fraudulent accounting is supported by this record.

## B. Contracts, contingent financing and infrastructure
The original preliminary S-1 displays BLANK fields for its single headline aggregate compute commitment, the portion to 2030 and next-12-month amount; **do not supply an exact issuer aggregate**. SEC financial notes disclose distinct categories with differing dates/terms: expected minimum future purchases ~**$265.6B** as of June30; leases entered but not commenced ~**$321.4B** as of June30 (F-35); subsequent arrangements about **$245B** of additional future minimum payments (F-65). Different scope/dates; may overlap contract-by-contract and aggregation contexts; no naive sum as current payable or debt.
Disclosed specific counterparty narrative (approximate, may be included within notes; not additive to already aggregated figures):
- Google Cloud service commitments **at least ~$114.5B**, 2026–2033; source S-1 MD&A p170.
- AWS service commitments **at least $110B**, 2026–2036; S-1 MD&A p171.
- Microsoft Azure commitments **at least ~$44.9B**, 2026–2033; p170.
- Broadcom **2026 Lease Arrangement**, as explicitly stated in SEC S-1 risk factors, is **approximately $125.2B of rent over five years excluding interest**. An earlier $161.2B number was incorrectly conflated with this individual lease and is EXCLUDED pending item-by-item attribution; never use it for the 2026 Lease Arrangement. March31 EX-4.4 separately documents **conditional up to $42B possible notes**, not $42B cash lent. Note says 9% if actually drawn in certain terms; full conditions must be checked.
- SpaceXAI **up to ~$120.5B** conditioned on capacity delivery/early termination; Nscale up to ~$44.6B and Lambda ~$41.3B discussed by independently extracted financial research. **These figures are not hard liabilities already owed**. Different termination/right-on-acceptance triggers; independent exact source verification remains necessary before specific script wording.
- Kepler analyst sums **~$637B** of named arrangements, with ~$431B minimum and ~$206B conditional; **its own calculation**, not filing's intentionally blank headline. Specific statement applicability and possible overlaps still HOLD, so avoid single dramatic definitive commitment figure.
- Various contracts contain confidential omissions `[***]` permitted by SEC redaction rules; unseen terms cannot be invented.

Financing:
- As of June30, reported Amazon notes outstanding principal **$6.2B**, separate from future notes capacity.
- As of June30 the prospective **up-to-$77B** note capacity includes Google $20B, Amazon $15B, Broadcom $42B, all conditional; does not mean $77B drawn. Google EX-4.5 March31 headline agreement was $30B less a $10B separate equity investment in May. Broadcom EX-4.4 original and Google EX-4.5 directly retrieved; EX-4.6 and EX-4.7 describe registration rights rather than proved draws.
- Cloud firms can simultaneously supply compute, act as business partners, invest in equity and compete with Claude. Explain contractual conflicts as disclosed company *risk factors*, never as a proven conspiracy.
- Gross revenue recognition for some cloud marketplace sales depends on Anthropic acting as **principal** under direct customer agreements (S-1 F-21); partnership payments booked as sales/marketing/partnership costs. No unsupported accusation of artificial revenue inflation.

## C. Control, ownership, special classes
Direct authenticated exhibit links:
- EX-10.14 https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/exhibit1014-sx1.htm: shareholders agreement with Founder LLC and LTBT. **Effective from IPO closing**, not proof those post-IPO provisions are currently operative.
- EX-99.1 https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/exhibit991-sx1.htm: Long-Term Benefit Trust, created June 29, 2023, special Class T shares and mandate to balance stockholder economics, impact on people and public-benefit AI development.
- EX-99.2 https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/exhibit992-sx1.htm: Anthropic Founders LLC member agreement with draft IPO-linked effective time.
S-1 describes Class F **single share in Founder LLC of seven cofounders carrying 50.1% of total general stockholder votes** after the offering. It confers no equivalent 50.1% economic ownership. Class T LTBT is empowered generally to choose/remove four of seven authorized directors, while Founder LLC controls at-large votes; oversimplified 'Dario personally owns/controls 50.1% of Anthropic or appoints all directors' is false. Some strategic partner shares are Class N non-voting. Founders' pledge to donate 80% of their individual stakes is described as voluntary, not legally binding.
**Important legal nuance:** S-1 says structure has limited court precedent; do not assert LTBT is judicially guaranteed to dominate all policy/board actions. Distinguish seven founders from single CEO.

## D. Revenue/customer caveats, real economic risk
The S-1 reports growth in enterprise usage, continued shift to more consumption-driven revenue, and cloud-marketplace distribution. Relevant proof locators: MD&A How We Generate Revenue p138, Revenue Recognition F-21; customer spending MD&A p149.
Management estimates 5–7% of revenue in first nine months of 2026 came from accounts later found violating usage policy or commercial terms; this is an issuer estimate about **terms-of-service customers**, not a law enforcement fraud verdict or admission company committed fraud. August/September 2026 enforcement stepped up and future impact uncertain.
Near-term computed profitability could compress as larger compute deliveries commence; long-term agreements can include pay regardless of use. The story is the mismatch between fast-moving revenue demand and long-dated fixed resource commitments.

## E. Security, FTC and regulatory status
The S-1 says FTC issued a **civil investigative demand in October 2026** seeking information on consumer protection, privacy, data protection, product safety and security. This is an inquiry; no FTC liability finding, regulatory charge or fine established. Axios Oct26, quoting FTC spokesperson, separately reports demands for Anthropic executives' testimony: secondary attributed claim; subpoena and testimony originals have not been obtained. If stated, always "according to Axios, citing the FTC".
The S-1 summarizes four incidents of model unauthorized access to real third-party systems during third-party cybersecurity evaluations. These were NOT newly revealed on Oct26: Anthropic separately reported three on July30 and fourth by September9. Primary company safety account https://www.anthropic.com/research/alignment-assessment-cybersecurity-incidents: environment incorrectly connected to internet; special evaluation ran without production safeguards; single model instances, active sessions roughly 10–34 hours; affected parties notified; investigators reported no independent coordinated attack or evidence actions beyond task scope. METR independent investigation announced but no final report established in this package.
Never claim ordinary production Claude autonomously hacked users or that security defects were proven systematic in live deployments. Distinguish **actual real-system unauthorized accesses** (reported by company) from conditions under which they occurred. No operational intrusion techniques are needed in narration.

## F. Chronology and source-type caution
2023 LTBT created; 2023/24 Amazon financing notes; March2026 Google and Broadcom agreements; May2026 Google preferred financing and Series H fundraising; June30 H1 reporting date; July30 + Sept9 previous safety disclosures; October2026 FTC CID; October26 SEC S-1 and Axios testimony report. Some numbers describe H1 through June30, others customer reporting through Sept30: never visually superimpose same time series without labels.
Unlike a lawsuit documentary, this episode is an IPO financial disclosure and risk examination. No guilt, liability, scam or illegal activity finding. SEC receiving an S-1 is not SEC approval of accuracy, nor endorsement of investment value.

## G. Production relevance / future evidence needs
These are **potential factual document beats**, not Stage02 scene plan: S-1 cover date/accession; F-7 loss bridge; F-12 cashflow; p169 blank commitment; specific provider commitment table; EX-4.4/4.5 excerpts; EX-10.14/EX-99.1/EX-99.2 founder versus LTBT rights; FTC CID risk paragraph; July30/Sep9 safety chronology. Original documents may be depicted editorially with correct provenance; rights and download quality require Stage12/13 work later. No footage or paid assets sourced as part of Stage01.

## H. Final Stage01 boundary
**DELIVERED:** 15 source entries, 44 individually classified claim rows, 18 chronology rows and independent-source desk audit. **NOT FULL PASS:** full 14MB filing and all exhibit terms not directly extracted end-to-end; $637B combined commitment not issuer aggregate; original FTC CID not obtained; third-party independent financial/legal professional review not performed. `01_INDEPENDENT_FACT_QC.md` controls corrections and unresolved items. **Stage02 BLOCKED.**


## 2026-10-26 Stage01 corrective documentary gate: target-only source audit
- Research team could **not** download/parse the complete original 14,169,143-byte main SEC HTML file: official SEC fetch exceeded browsing read limit, and outbound container network rejected retrieval. No claim of full-file audit is made. Material **story-map-core** numbers were individually cross-checked in SEC indexed text for S-1 financial-table excerpts and actual SEC exhibits EX-4.4 (Broadcom), EX-4.5 (Google), EX-10.14 (shareholders) and EX-99.1/99.2 (trust/founders). All other unreviewed exhibits / exact footnote nuances remain HOLD before Stage03/04 final assertions.
- Primary issuer SEC S-1 directly identifies the March 2026 Broadcom **2026 Lease Arrangement** as about **$125.2 billion rent, excluding interest, over five years**, not $161.2B. Corrected CLM026 and maintained QA017 correction receipt; lease ≠ note facility. SEC notes noncancelable except default, rents begin upon ready-for-service, and early default may accelerate payment. Source link: https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm (risk factor/direct-lease discussion, linked search excerpts).
- Confirmed EX-4.4 definition "Total Commitment" of **$42B**, with Section 2.1 note issuance conditional upon quarterly rent and conditions and potentially cashless application, not drawn bank credit or total lease price. Confirmed EX-4.5 definition "Aggregate Purchase Price" of **$30B** before separate financing changes; agreement is contingent, and includes *optional* IPO acceleration rights, not already completed IPO funding.
- Confirmed EX-10.14 states agreement effective as of **IPO Closing Date**. Sections 2.2, 2.5 include a special nominated Class T seat with **nominating committee / Class E approval exception** before sunset. Do not say trust freely replaces *every* director; Class F general vote is not economic majority or automatic board appointment.
- Official S-1 summary and risk material include **blank aggregate compute totals**. Close headline $637B claim by permanent EXCLUSION: CLM022 remains HOLD, not a number for plan or script; no purchase-minimum/lease/subsequent totals summed. Descriptive fact of noncancelable/take-or-pay commitments and SEC-stated $125.2B specific lease is sufficient to structure the business risk.
- Original FTC CID and reported individual testimony instruments **not located publicly**. Stage02 uses only company-reported fact of CID within S-1 with status inquiry; standalone Axios testimony is **excluded**, not independently verified or upgraded to fact. Any prosecution, settlement or official enforcement implied by CID is prohibited.
- The F-7 SEC-indexed financial statement arithmetic is verified, but F-12 cashflow reconciliation cannot be independently ingested from the complete original file. **Operational cash flow $3.929B is a secondary-crosschecked research number only, not narration-ready without direct F-12 read**. Likewise CLM008 ($8.720B) and CLM012 calculated FCF are excluded from currently approved narrative. That closes the **core loss-vs-operations story** without pretending full cashflow-note authentication.
- End result: **Stage01 PASS FOR RESTRICTED NARRATIVE PLANNING**, not unconditional full financial-document QC. OPEN source-file acquisition and specific footnotes explicitly block strong script claims at Stage03/04; no unsupported detailed dollar claim may propagate.
