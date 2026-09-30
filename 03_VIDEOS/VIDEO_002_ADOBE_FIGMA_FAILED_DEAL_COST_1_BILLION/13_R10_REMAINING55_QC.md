# VIDEO 002 — R10 Remaining-55 Hard QC

Date: 2026-09-29

## Result
- New frames audited: **55 / 55**
- PASS: **39**
- REJECT: **16**
- Existing locked usable PASS before this batch: **55**
- Total usable PASS now: **94 / 110**
- Remaining without PASS: **16 / 110**
- Paid retries: **0**
- QC spend: **0 credits**

Checks performed on every new frame: exact headline, source fidelity against the prepared attachment and intended R9 source role, composition/story/canon fit, and bottom-15% subtitle safety.

The 16 rejects are material source-fidelity failures, not cosmetic nitpicks. They trace to **10 defective source-prep assets**. Retrying before fixing those inputs would waste credits.

## REJECT slots
- **F007** — SOURCE_PREP_DEFECT: RV027/RV028 are the same generic Figma hero artwork, not search/workspace UI; generated frame substitutes invented UI.
- **F010** — SOURCE_PREP_DEFECT: RV034 is generic Figma artwork, not design-system UI.
- **F011** — SOURCE_PREP_DEFECT: RV037 is promotional artwork, not the required Dev Mode product screenshot.
- **F051** — SOURCE_PREP_DEFECT: RV054 CMA timeline prep is malformed escaped/HTML extraction text.
- **F053** — SOURCE_PREP_DEFECT: RV056 provisional-findings prep contains extraction/escape artifacts, not a clean authentic excerpt.
- **F054** — SOURCE_PREP_DEFECT: RV037 is promotional artwork, not authentic Dev Mode UI.
- **F059** — SOURCE_PREP_DEFECT: mandatory RV056 provisional-findings evidence is malformed.
- **F061** — SOURCE_PREP_DEFECT: RV042 is generic Figma artwork, not advanced-prototyping UI.
- **F062** — SOURCE_PREP_DEFECT: RV054 CMA timeline evidence is malformed/unreadable.
- **F063** — SOURCE_PREP_DEFECT: mandatory RV056 provisional-findings evidence contains extraction artifacts.
- **F073** — SOURCE_PREP_DEFECT: RV054 timeline source is malformed.
- **F093** — SOURCE_PREP_DEFECT: RV015 is generic Figma artwork, not the required Config 2023 keynote-stage photo.
- **F095** — SOURCE_PREP_DEFECT: RV072 S-1 announcement prep is CSS/style-text garbage rather than announcement evidence.
- **F100** — SOURCE_PREP_DEFECT + SOURCE_SUBSTITUTION: RV018 is generic Figma artwork, not the required IPO-era portrait; output invents a portrait absent from source.
- **F104** — SOURCE_PREP_DEFECT: RV056 provisional-findings source is malformed.
- **F105** — SOURCE_PREP_DEFECT: RV054 CMA timeline source is malformed, so the UK evidence track is not production-safe.

See `13_R10_SOURCE_PREP_DEFECTS.csv` for the 10 source inputs that must be rebuilt before any retry.
