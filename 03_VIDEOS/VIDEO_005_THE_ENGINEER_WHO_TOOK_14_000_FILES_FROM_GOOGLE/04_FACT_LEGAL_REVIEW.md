# VIDEO005 — G04 Independent Fact + Legal Review
**Date: 2026-10-13 | Script snapshot: `03_SCRIPT_V1.md` V1 (2,828 spoken words; 53 paragraphs).**
**VERDICT: FAIL — 2 HIGH factual timeline failures; 4 MEDIUM wording risks; 2/8 Shorts isolated FAIL. Stage05 repairs required.**

## Audit methodology / exact traceability
- Examined **all 53/53 original narration paragraphs** (A00-P01 to A09-P04) against script-linked C-IDs and primary courts, DOJ, SEC and quoted corporate sources in `SOURCE_INDEX.csv`.
- Audited full **unchanged verbatim passage**, claim IDs, cited original and editorial/legal distinction for each paragraph. See `04_PARAGRAPH_AUDIT.csv` (53 full passages with verdicts, direct source IDs and exact repair instruction).
- Re-read **each of the 8 actual contiguous S01–S08 excerpts in isolation**, not relying on setup before the clip or context after the cut. See `04_SHORTS_ISOLATION_QC.csv` with verbatim excerpts and individual findings.
- Primary direct inspections: [S010 DOJ plea](https://www.justice.gov/usao-ndca/pr/former-uber-self-driving-car-executive-signs-agreement-plead-guilty-theft-trade-secrets), [S008 Delaware Supreme McElrath](https://law.justia.com/cases/delaware/supreme-court/2020/181-2019.html), [S003 Alsup preliminary order](https://law.justia.com/cases/federal/district-courts/california/candce/3:2017cv00939/308136/433/), [S031 Alsup Jan2018 discovery order](https://docs.justia.com/cases/federal/district-courts/california/candce/3:2017cv00939/308136/2585), [S032 Jan2025 bankruptcy opinion](https://www.govinfo.gov/content/pkg/USCOURTS-canb-3_20-bk-30242/pdf/USCOURTS-canb-3_20-bk-30242-0.pdf), [S033 Mar2023 federal district opinion](https://www.govinfo.gov/content/pkg/USCOURTS-cand-4_22-cv-02781/pdf/USCOURTS-cand-4_22-cv-02781-0.pdf), and DOJ sentencing & public dismissal / company-source evidence ledgers. This is direct substantive source comparison, **not merely link or CSV counting**.
- `SOURCE_INDEX.csv` URLs refer to authentic records but original document pixels, provenance permissions and final factual refresh are later stages; no license clearance claimed.

## Exact result — every paragraph
| Metric | Result |
|---|---|
| Paragraphs with no identified substantive error | **47 / 53** |
| Medium risks requiring attribution/chronology/rhetorical precision | **4 / 53** |
| High factual inaccuracies | **2 / 53** |
| All paragraph claim IDs/source references existing | **PASS** |
| Standalone Shorts legal text | **6 provisional PASS / 2 FAIL** |
| Shorts spoken 20–27 sec / <=30sec including ending | **NOT MEASURED — no Harrison generation authorized** |
| Overall **G04** | **FAIL**, as per quality gate (any unresolved HIGH accuracy issue blocks approval) |

## HIGH errors that MUST be corrected in Stage05
### Q034 — A02-P06 — chronology of Stroz investigation reversed
**Current sentence:** "So Uber brought in a forensic investigation."
**Problem:** As placed **after** the preceding story's acquisition-closing language, it reads as a later investigation after purchase. Delaware Supreme opinion S008 dates the Stroz investigation **after February2016 term sheet and before acquisition closing**; preliminary findings existed before the April11 board decision and final report before August closing.
**Safe replacement:** "That was why Uber had already hired forensic investigators before the acquisition closed. Their findings would become part of the risk calculation."
**Required:** Move/rework passage's temporal connective in **canonical main Script V1**, ensure the following A03-P01 identifies Stroz as **pre-closing**. No modifying audio or after-the-fact captions.

### Q035 — A05-P04 and S05 — reported disk destruction falsely dated to the lawsuit period
**Current sentence:** "In January 2018, a federal judge addressed five computer disks reportedly destroyed during the Waymo–Uber dispute."
**Problem:** Uber told Waymo that Levandowski informed executives about five discs **around March 11, 2016** and subsequently said he destroyed them. Federal **Waymo v Uber** complaint was filed in **February 2017**; Judge Alsup's ruling about Uber's **LATE DISCLOSURE** was **Jan 30, 2018**, not a finding the physical destruction happened during the lawsuit.
**Proposed entire one-paragraph replacement suitable for both full film AND Short S05:**
"In January 2018, a judge in Waymo's lawsuit against Uber reviewed a late disclosure: engineer Anthony Levandowski had reportedly destroyed five disks containing Google information back in 2016. Jurors could, but did not have to, draw an unfavorable inference from Uber's late disclosure. The case settled before a verdict."
**Legal note:** Contents of those disks **not established**, the alleged destruction must not be changed into proven destruction of the ~14,000 downloaded files. Source S031 contains competing corporate explanations and express permissive-vs-mandatory inference distinction. Actual sound timing remains unknown.

## MEDIUM sentence-level corrections
- **Q036 — A03-P06:** "it would take a mistake ... to bring the conflict into the open" makes an unsupported necessary causal claim. Prefer "A misaddressed supplier email soon gave Google an additional reason to investigate." [S003,S008].
- **Q037 — A04-P01:** "Similar-looking engineering material" makes disputed resemblance sound established. State Waymo **alleged** the circuit-board drawings resembled its engineering materials [S008,S003].
- **Q038 — A05-P03:** "could not simply be repaired by replaying a backup" speculates about missing or unavailable backup evidence. Remove; focus on Uber's late disclosure and unresolved contents [S031].
- **Q039 — A07-P05:** "Levandowski wanted to know whether" infers internal intention. Change to source-observable "Levandowski later argued that the April2016 agreement required Uber to cover the judgment" [S032].

## Isolated Shorts — eight independent verdicts
| Short | Actual paragraph (one uninterrupted passage) | Words | Result | Standalone decision |
|---|---|---:|---|---|
| **S01** | A00-P01 | 52 | **FAIL** | Uber is named only as possible payer without explaining the acquisition/indemnity link. Intro must be self-contained. |
| S02 | A01-P03 | 48 | PASS, provisional | DOJ ~14k SVN copies and explicit no proof Uber used all files. |
| S03 | A02-P03 | 52 | PASS, provisional | ~$680m contingent consideration vs $100k up-front, not engineer cash. |
| S04 | A03-P04 | 50 | PASS, provisional | Shareholder **allegations**, Stroz limitation preserved. |
| **S05** | A05-P04 | 53 | **FAIL** | Same 2016 vs 2017–18 chronology mistake as Q035; revise LONG-FORM paragraph. |
| S06 | A06-P02 | 55 | PASS, provisional | 2018 stock settlement, no verdict, no cash fine. |
| S07 | A07-P02 | 53 | PASS, provisional | Personal Google arbitration $179m / bankruptcy, not Uber criminal fine. |
| S08 | A08-P05 | 54 | PASS, provisional | 2022 actual Uber→Google payment confirmed; main amount sealed; separate $2m. |

**Q040 — S01:** Suggested contiguous long-form in-paragraph replacement: 
"In March 2020, former Google engineer Anthony Levandowski faced a civil judgment exceeding one hundred seventy-nine million dollars. He filed for bankruptcy hours later. Years earlier, Uber had acquired his startup and signed a conditional indemnification agreement. The judgment was his personal liability, not an Uber verdict. Could that deal obligate Uber to help pay?"
Approx 55 words. Does not prove Uber was automatically liable, and names **why** Uber enters the question. Fix in long-form, not a separately voiced Short intro.

**Q041 — S05:** Fails legal isolation due to historical date. Reuse Q035 replacement in whole film.

**All six provisional PASS Shorts** still require original audio timing + exactly bounded single continuous cut plus Stage16 freshness and independent captions/visual legality.

## Verified substantive foundation that must NOT be broken by revisions
1. **14,000** internal SVN file downloads and personal transfer (DOJ); a distinct Google Drive file underlies an **individual one-count guilty plea**. Neither is a verdict Uber deployed all files. S010/S011.
2. **Otto ~ $680m** is structured conditional potential consideration with **$100k up-front cash** per Delaware opinion, not amount paid in cash to Levandowski. S008.
3. **Stroz** report's actual phrase concerns **no discovered evidence** transfer to Ottomotto or third parties, which does not establish no possible use. Shareholder diligence allegations are not director bad-faith findings. S008.
4. May2017 court found sufficient reasons for **limited provisional relief**, but patent theory inadequate at this stage and not all 121 alleged secrets qualified/traced. S003.
5. Feb2018 civil Waymo/Uber case **settled/dismissed with prejudice**, no jury verdict; ~**$245m** approximate Uber stock value at 2018 time, not cash damages. S005,S008.
6. **$179,047,998.64** was a **personal civil Google arbitration judgment** against Levandowski March4 2020, with Chapter11 filing hours later; no conflation with federal criminal sentence. S032.
7. **2022 Uber Main Payment** to Google **actually made on or before May20 2022**, amount SEALED; separate $2m funding for Levandowski's bankruptcy plan, no documentary basis to say Uber paid all $179m. S032,S033.
8. Jan2025 tax ruling classifies Main Uber Payment as gross income to individual, not a final quantified tax bill and not invalidation of global settlement. S032.
9. Corporate denial from 2018 Uber statement appears close to plaintiff allegations in A04/A06. Denial is Uber's position, not independent clearance.
10. 2018 pretrial five-disk instruction was **permissive**; only **eight** alleged secrets remained in narrowed trial case at that stage, not a verdict on original 121. S031.

## Final Stage04 decision
**FAIL / corrective handoff to Stage05**. Fix at least Q034, Q035, Q040 and all medium issues Q036–Q039 IN the original long-form script, rebuild exact IDs and `03_SHORTS_MAP.csv` and `03_SCRIPT_CLAIM_TRACE.csv` if wording/durations change. Rerun this G04 audit independently on the **changed final text**, then consider G04 PASS. Do not automatically mark earlier owner-held Stage01/Stage02 as approved.

No audio, TTS, paid generation, screenshots, image creation, video editing or Stage05 modifications were made by this Stage04 audit.
