# VIDEO 002 — Queue 001–075 Reject Recheck R2

Date: 2026-09-28  
QC policy: **PASS / REJECT only**  
New image spend: **0**

## Why R2 exists

The first recovery QC was too conservative. It treated any non-exact headline wording, editorial source synthesis, or uncertain pixel-level source fidelity as an automatic REJECT even when the frame was visually strong, factually safe, and usable in the actual edit.

R2 uses a stricter distinction between **material failure** and **non-material variation**:

### PASS is allowed when
- the frame communicates the correct script beat;
- an alternate headline is semantically equivalent and factually safe;
- source/reference material is represented correctly enough for the intended editorial use;
- there is no material legal/factual contradiction;
- the frame is visually on-canon and usable with the bottom subtitle area.

### REJECT remains mandatory when
- a number/date/legal claim is wrong;
- the image contradicts the narration;
- fake UI/document content materially changes the factual meaning;
- the wrong beat is shown;
- the asset is missing/unrecoverable;
- the image introduces prohibited claims such as a DOJ blocking lawsuit or a final regulator prohibition that did not occur.

## R2 promotions

- **F009** → PASS — `adobe_xd_vs_figma_competition_in_focus.png` — alternate headline is semantically equivalent; the Adobe XD/Figma capability comparison supports the beat and contains no material factual contradiction.
- **F012** → PASS — `adobe_figma_deal_overview.png` — the frame accurately communicates the announced ~ $20B transaction and half-cash/half-stock structure; headline wording differs but the beat meaning is intact.
- **F016** → PASS — `negotiated_before_failure_timeline.png` — negotiation/timeline visual directly supports the negotiation-record beat; no material story or legal contradiction is visible.
- **F023** → PASS — `written_into_the_deal.png` — recovered candidate explicitly shows July 20, 2022 and Adobe agreeing to a $1B reverse termination fee; strong source-led fit.
- **F026** → PASS — `the_1_billion_termination_fee.png` — recovered candidate combines the July 20 negotiation record with the $1B termination-fee clause and directly communicates Adobe agreeing to the fee.
- **F027** → PASS — `contractual_exit_cost.png` — 'CONTRACTUAL EXIT COST' is a faithful semantic equivalent of 'THE COST WAS ALREADY THERE' and the visual is on-canon with no hard factual error.
- **F029** → PASS — `closing_conditions_merger_termination_fee.png` — Section 8.2 closing-condition language and the $1B fee directly communicate what happens if closing fails; strong source/evidence frame.
- **F032** → PASS — `not_a_fine_merger_termination_fee.png` — the visible clause explicitly states the fee is not a penalty but liquidated damages, which directly satisfies the LIQUIDATED DAMAGES beat.
- **F033** → PASS — `the_1_billion_backstop_document.png` — July 20 record and $1B reverse termination fee are clear; 'backstop' is an accurate editorial shorthand for the failure-price beat.
- **F034** → PASS — `from_20b_to_1b.png` — the frame clearly contrasts the ~$20B proposed transaction with the $1B reverse termination fee/payment; no fake $21B arithmetic or material contradiction.
- **F035** → PASS — `the_deal_is_signed.png` — the source text visibly anchors September 15, 2022 and the definitive merger agreement; alternate headline remains fully on-beat.
- **F037** → PASS — `the_deal_was_real.png` — the definitive-agreement evidence and ~ $20B half-cash/half-stock terms accurately support the 'deal looked normal' beat.
- **F066** → PASS — `the_defense_adobe_and_figma_brief.png` — the frame is clearly an editorial response summary of the parties' own characterization/defense and does not present a regulator conclusion as fact.
- **F069** → PASS — `wide_cinematic_still_life_composition_on_a_dark_t.png` — mutual termination is communicated immediately and cleanly; the date can remain in narration rather than being mandatory in the headline.
- **F070** → PASS — `the_clock_ran_out_termination_fee.png` — the termination-outcome frame accurately conveys that the parties saw no clear approval path and ended the deal; no final prohibition is claimed.
- **F080** → PASS — `the_payment_hits_the_books.png` — Adobe 10-K payment evidence clearly confirms the $1B payment in December 2023; exact day remains in narration, while the frame accurately shows the accounting consequence.
- **F082** → PASS — `conversation:file_000000008eb882109f40a2e06ce0fcb2` — exact recovered chat artifact shows THE MONEY MOVED with Adobe/Figma source-faithful identifier cards and restrained red connector; clean subtitle-safe composition.
- **F083** → PASS — `conversation:file_00000000d3f082109da712e784eba65f` — exact recovered chat artifact shows DEC 17 → DEC 20 with termination/payment evidence and correct $1B timing; on-canon and subtitle-safe.

## Still-hard REJECT examples
- **F011** — recreated UI instead of usable authentic/source-faithful UI.
- **F020** — headline says no fee yet while the visible document says July 20 and a $1B fee; direct contradiction.
- **F050** — invents a DOJ lawsuit / Jan 2024 closing path after the deal had already been terminated.
- **F061** — visible summary says the products overlapped, which conflicts with the parties-characterization beat.
- **F072** — wrong subject; frame is HALF CASH / HALF STOCK, not mutual termination.
- **F086** — hard consideration-language error in generated source text.
- **F089** — hard $250M error; actual termination payment was $1.0B.
- **F090** — no completed generation recovered.

## Revised result
- Queue positions audited: **75**
- PASS: **40**
- REJECT: **35**
- Pre-existing canon PASS: **15**
- Total usable frames: **55 / 110**
- Remaining without PASS: **55 / 110**
- New paid generation: **0**

The original 149-image recovery ZIP and SHA-256 remain unchanged. Two additional exact conversation artifacts for F082/F083 were recovered during this recheck and are referenced by conversation file ID in the canonical QC CSV.
