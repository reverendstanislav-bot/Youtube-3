# Stage 12F — Batch 1 Visual QC

Status: **PARTIAL PASS / CORRECTION REQUIRED**

Scope: **B001–B035**

## Result
- PASS as generated: **7**
- EDIT_FIX — keep generation, correct in editorial/composite without paid regeneration: **16**
- REGEN — generation itself is not production-acceptable: **12**
- Total checked: **35 / 35**
- Provider failures: **0**
- Additional generations submitted during QC: **0**
- Additional credits spent during QC: **0**
- Batch 2: **BLOCKED pending correction decision**

## QC lenses
1. exact/key on-image text;
2. extra or fabricated factual copy;
3. dense pseudo-document / legal text;
4. bottom-20% subtitle-safe area;
5. visual density / hierarchy;
6. dark documentary palette and restrained Signal Red;
7. obvious repetition / duplicated headline structures;
8. legal/evidence treatment against Stage 12F-R2.

## System-level findings
### What worked
- The overall dark documentary palette is consistent across the batch.
- Most main headlines are legible and correctly spelled.
- No evidence of literal scene duplication.
- The R2 sparse-document rule improved many quote/clarifier scenes.
- B006 and B018 remain owner-approved PASS frames.

### What still failed
The main remaining failure is **reference contamination**: when a court/source image is supplied, GPT Image 2 can still reproduce large parts of the reference page even if the prompt says not to. This caused dense or malformed legal text in B008, B017, B020, B028 and B032, and gibberish secondary text in B026/B027/B031.

Therefore future document-heavy generations need a stricter execution rule:
- do **not attach a full-page text-heavy source reference** when the model only needs style/context;
- attach a pre-cropped short excerpt or non-text visual reference instead;
- if exact court text is needed, generate the clean composition first and composite the authentic crop pixel-for-pixel afterward.

## Subtitle-safe findings
Hard text collisions were detected in:
- **B004** — lower DOJ/FBI source label;
- **B013** — lower eBay mark;
- **B016** — CASE NO / COMPLAINT copy in the subtitle band.

Additional visually busy lower bands requiring editorial darkening/reframe:
B001, B005, B011, B022, B025, B030.

## REGEN list — 12 scenes
- **B008** — Dense pseudo-legal document failure
- **B011** — Wrong legal-document contamination + very busy subtitle area
- **B016** — Subtitle collision + legal-document contamination
- **B017** — Full dense court page
- **B020** — Dense source-page treatment
- **B026** — Gibberish pseudo-text
- **B027** — Gibberish labels
- **B028** — Dense document copy
- **B029** — Key on-image text missing
- **B031** — Garbled source text
- **B032** — Dense pseudo-document copy
- **B034** — Red overuse + invented source label

## EDIT_FIX list — 16 scenes
- **B001** — Subtitle band visually busy
- **B003** — Extra generated threatening-message copy
- **B004** — Source label enters subtitle-safe zone
- **B005** — Subtitle band visually busy
- **B007** — Accountability treatment text-heavy
- **B009** — Duplicated money headline
- **B013** — eBay logo enters subtitle-safe zone
- **B014** — Irrelevant courthouse/John Adams quote dominates secondary layer
- **B015** — Unnecessary court-filing labels
- **B019** — Irrelevant large background legal/courthouse quotation
- **B022** — Lower frame too visually active
- **B024** — Wrong secondary legal labels
- **B025** — Extremely busy lower band
- **B030** — Busy subtitle band
- **B033** — Garbled source/agency label
- **B035** — Questionable extra DOJ/FBI source label + heavy red

## PASS list — 7 scenes
- **B002**
- **B006**
- **B010**
- **B012**
- **B018**
- **B021**
- **B023**

## Gate
Do **not** regenerate the 12 rejected scenes and do **not** start Batch 2 without explicit owner instruction.

The 16 EDIT_FIX scenes should be repaired without paid image generation where possible.
