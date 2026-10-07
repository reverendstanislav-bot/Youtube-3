# VIDEO 004 — Stage 04 Fact / Legal Review

Date: 2026-10-07  
Reviewed file: `03_SCRIPT_V1.md`  
Result: **PASS WITH LOCKED GUARDRAILS**

Evidence controls at review close:
- `SOURCE_INDEX.csv`: 9 sources.
- `CLAIMS_LEDGER.csv`: 23 material claims.
- `CASE_EVENT_LEDGER.csv`: 13 procedural/contract events.
- `03_SHORTS_MAP.csv`: 8 contiguous extracts, each reviewed in isolation.

## Hard-metric scorecard

| Metric | Score | Result |
|---|---:|---|
| Claim-to-source traceability | 5/5 | PASS |
| Allegation/status precision | 5/5 | PASS |
| Procedural chronology | 5/5 | PASS |
| Quote/context accuracy | 4/5 | PASS |
| Current-status freshness | 5/5 | PASS |
| Numerical accuracy | 5/5 | PASS |
| Party-position fairness | 5/5 | PASS |
| Primary-source sufficiency | 4/5 | PASS |

No unresolved BLOCKER or HIGH accuracy issue at Stage 04.

## Runtime check

- Approximate spoken words: 3,125.
- Estimated narration at 145 wpm: 21.55 minutes.
- Target runtime: 15–22 minutes.
- Result: PASS.

## Claim audit

| Script claim | Evidence | Result |
|---|---|---|
| Valve added individual AAA arbitration in 2012 | Dkt. 169, background | PASS |
| Consumer plaintiffs were compelled to arbitration in 2021 | Dkt. 169 citing *Wolfire* order | PASS |
| First coordinated group contained 997 demands | Dkt. 169, pp. 3–4 | PASS |
| 4,991 claimants at the cited stage | Dkt. 169, p. 4 | PASS — correctly attributed and not treated as victories |
| Valve removed arbitration and class waiver on Sep. 26, 2024 | Valve announcement; Dkt. 169 | PASS |
| Updated clause reached older claims | Updated SSA; Dkt. 169 | PASS |
| 454 affirmative acceptances and 118 post-effective-date logins | Valve evidence summarized in Dkt. 169 | PASS — attribution preserved |
| Claimed average library value above $3,000 | Defendants' evidence; disputed by Valve | PASS — dispute explicitly stated |
| AAA declined administrative closure | Dkt. 169 | PASS — script does not misstate this as a merits ruling |
| 624 original respondents; 572 complaint defendants | Dkt. 169 | PASS |
| Roughly 400 active by May 2026 according to Valve | Hearing representations summarized in Dkt. 169 | PASS — uncertainty preserved |
| Mixed arbitral outcomes | Dkt. 169 | PASS |
| Preliminary injunction denied May 27, 2026 | Dkt. 169 | PASS |
| Interlocutory appeal certified and case stayed July 30, 2026 | Dkt. 192 | PASS |
| Ninth Circuit No. 26-6269 opened Sep. 25, 2026 | Appellate docket mirror | PASS — refresh before publication |

## Legal characterization audit

- The script repeatedly distinguishes a preliminary injunction from a final judgment: PASS.
- It does not say Valve lost the antitrust merits: PASS.
- It does not say every arbitration claim was valid: PASS.
- It separates the publisher class, core injunction action, individual award cases and *Bucher Law*: PASS.
- It attributes contested positions to Valve or defendants: PASS.
- It treats district-court unconscionability analysis as stage-specific: PASS.
- It identifies the appeal as unresolved: PASS.

## Money audit

- The `$20 million` framing is explicitly rejected as unverified.
- AAA fees are described as a multi-stage mechanism, not a calculated liability.
- No damages, invoice, settlement or payment is invented.
- Result: PASS.

## Shorts audit

- Eight clean contiguous windows are present.
- Each has a standalone hook, context, payoff and required caveat.
- Estimated body durations remain compatible with a sub-60-second output after a 3-second CTA.
- No window depends on burned subtitles.
- Result: PASS.

## Required later refreshes

1. Refresh Ninth Circuit docket `26-6269` immediately before Stage 16 and publication.
2. Replace scheduled brief dates if the court changes them.
3. Review the underlying filings cited as Dkt. 78, 79, 92 and 106 before Stage 07 if their details remain in the canonical narration.
4. Review the actual appellate briefs after filing or remove any schedule-dependent detail before final legal lock.
5. Continue excluding any total fee claim unless invoices and payment status are authenticated.

## Verdict

**PASS.** No factual correction is required before Script V2. Stage 05 may focus on narration flow, sentence rhythm and retention without changing the locked legal meaning.
