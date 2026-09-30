# VIDEO 002 — R14 Preview-40 Release-Resolution Regeneration Pack

Date: 2026-09-30
Status: **PROMPTS + REFERENCES LOCKED / PAID GENERATION NOT AUTHORIZED**

Scope: the 40 slots that Stage 15 picture assembly V1 could only source from 960×540 recovery previews (`15_PICTURE_ASSEMBLY_RESULT.md`, release-resolution hold):

`F001 F009 F012 F013 F014 F016 F017 F018 F019 F021 F023 F024 F026 F027 F029 F030 F032 F033 F034 F035 F037 F043 F045 F046 F048 F058 F060 F066 F069 F070 F074 F075 F080 F081 F082 F083 F084 F085 F087 F088`

Owner decision (2026-09-30): **regenerate in Higgsfield** instead of accepting the upscale or recovering ChatGPT originals.

- Prompts: **40 / 40**
- Reference bindings: R9 source bindings, media IDs resolved via `13_R11_REPAIRED_REFERENCE_RESOLVER.csv` first, then `12_SOURCE_PREP/HIGGSFIELD_MEDIA_MAP.csv`
- Source-prep work required: **0**
- Model if later approved: **Higgsfield GPT Image 2 / 1k / low / 16:9** (same as R10–R13)
- Base cost if approved: **40 × 0.5 = 20.0 credits**
- Paid generation authorization: **NO**
- Automatic retries: **PROHIBITED**
- QC: **PASS / REJECT only**, same gates as R12/R13. The existing preview-backed frame stays the locked fallback for any slot that REJECTs.

## Prompt construction

The R10 umbrella prompt file has empty beat-specific fields (see `12A_R10_REMAINING55_EXECUTION_PACK.md`). Each prompt below is therefore:

1. the populated R9 final-frame prompt (story purpose, locked headline, sources, role, composition);
2. the R10 canon-style override (F039 first, F015 second);
3. an R14 caption-safe hard gate carrying the R12/R13 layout fix (headline in top 8–34%, all content above 77%, bottom 23% dark) — the only failure mode that survived R11–R13.

No facts, headlines or source bindings are changed.

## Reference blocker — 18 of 40 slots

The 22 slots marked `READY` in `13_R14_PREVIEW40_REGEN_QUEUE.csv` have every reference already persisted in Higgsfield. The other **18 slots are `BLOCKED_MISSING_MEDIA`**: they were originally generated in ChatGPT, so their 12 unique references were never prepared into `12_SOURCE_PREP/` or uploaded to Higgsfield, and no binary exists in Git.

| Reference (R9 binding path) | Source (01B manifest) | Slots |
|---|---|---|
| `B012_RV047_DOCUMENT.png` | Adobe press release PDF | F012 |
| `RV048_8K_MERGER_AGREEMENT_CROP.png` | SEC Form 8-K | F013, F033, F048 |
| `B016_RV050_DOCUMENT.png` | SEC 424B3 | F016 |
| `B023_RV052_DOCUMENT.png` | SEC 424B3 | F023 |
| `B030_RV049_DOCUMENT.png` | SEC Agreement and Plan of Merger | F030 |
| `B069_RV062_DOCUMENT.png` | SEC Mutual Termination Agreement | F069 |
| `RV055_CMA_PHASE1_DECISION_CROP.png` | UK CMA Phase 1 decision | F043, F046 |
| `RV060_DOJ_STATEMENT_CROP.png` | DOJ statement | F045, F074 |
| `RV001_NARAYEN_PORTRAIT.jpg` | Wikimedia Commons (CC BY-SA 4.0) | F019 |
| `RV012_FIELD_PORTRAIT.jpg` | Figma Events | F021, F024, F060 |
| `RV013_FIGMA_FOUNDERS_ARCHIVAL.jpg` | Figma blog | F017 |
| `RV016_CONFIG_2023_CROWD.jpg` | Figma blog / Config 2023 | F037 |

**R14 source prep (2026-09-30, owner-approved, ledger `13_R14_SOURCE_PREP.csv`):**
- 5 document paths resolved as aliases of already-uploaded crops (B012→RV047, B016/B020→RV050, B023→RV052, B030→RV049 §8.2, B069→RV062).
- 6 references prepared locally from the official sources (RV048, RV055, RV060, RV001, RV012, RV013); binaries in `WhatItCost_media/002-adobe-figma/12_SOURCE_PREP/`, not yet uploaded to Higgsfield.
- RV016 (Config 2023 crowd) not found on the current official page nor in the Wayback snapshot of 2023-07-09 → F037 stays blocked pending owner decision. Note: the locked R10 PASS F037 frame was built on definitive-agreement evidence (~$20B half cash / half stock), which `RV048_8K_MERGER_AGREEMENT_CROP.png` now covers.

Queue after prep: **27 READY**, **13 READY_AFTER_UPLOAD** (F013 F017 F019 F021 F024 F033 F037 F043 F045 F046 F048 F060 F074), **0 BLOCKED**. F037 rebound RV016 → RV048 (see F037 section).

## Resolution note

**Owner decision 2026-09-30: generate at 1k** (1344×752, same as the other 70 locked frames).

A real 1k GPT Image 2 output from R12 (F010) is **1344×752**, not 1920×1080. So the 70 already-locked HTTP/retry frames are also upscaled ×1.43 in the 1080p assembly, and R14 at 1k will produce the same 1344×752. That is a large improvement over 960×540 (×2.0), but not native 1080p. Generating R14 at 2k would exceed 1080p; its cost must be checked in Higgsfield before approval.


---

## F001 / B001

**LOCKED HEADLINE:** `$20B PROPOSED / $1B ACTUAL`

**TIMING:** 0.000 → 8.160 (8.160 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV047_ANNOUNCEMENT_HEADLINE_CROP.png` → Higgsfield media `c300e57c-6744-4757-8c86-43a3b50095de`
- Image 2: `12_SOURCE_PREP/RV063_10K_PAYMENT_CROP.png` → Higgsfield media `ec7d4f0b-ad22-406d-b354-d8c0a83249ef`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B001, ready to place directly into the finished film.

STORY PURPOSE:
Adobe agreed to buy Figma for about twenty billion dollars. The acquisition never closed. Adobe still paid Figma one billion

LOCKED HEADLINE:
"$20B PROPOSED / $1B ACTUAL"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV047_ANNOUNCEMENT_HEADLINE_CROP.png
Image 2: 12_SOURCE_PREP/RV063_10K_PAYMENT_CROP.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline and exact fact labels explicitly required by this beat.

SOURCE ROLE:
Attached sources ground the verified numbers/dates/statuses. Two-column opening contradiction: left ~$20B PROPOSED ACQUISITION, right $1B ACTUAL TERMINATION PAYMENT; center DEAL NEVER CLOSED.

COMPOSITION:
Create a premium information frame from verified facts. Bebas Neue amounts/headings, Inter qualifiers; $1B signal red; ~$20B paper white; no fake $21B. One dominant statement plus one clear comparison/timeline/status structure; source excerpts support the information without PowerPoint styling. Turn only the verified source-grounded facts into an elegant cinematic information composition; exact numbers/dates only; never PowerPoint.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate. Do not fall back to a generic dark desk with random papers.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, flag/Capitol symbolism unrelated to the source, unverified numbers, misleading arithmetic, fake $21B total.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions. No editor instructions inside the image.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F009 / B009

**LOCKED HEADLINE:** `ADOBE XD — DESIGN / PROTOTYPE / SHARE`

**TIMING:** 71.060 → 78.520 (7.460 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV044_ADOBE_XD_WORKFLOW_UI.png` → Higgsfield media `5920ca42-6870-4166-aa56-f0d330e78500`
- Image 2: `12_SOURCE_PREP/RV045_ADOBE_XD_PROTOTYPING_UI.png` → Higgsfield media `df875d57-c51d-4db8-ab46-68934e7398a0`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B009, ready to place directly into the finished film.

STORY PURPOSE:
Adobe was one of the world's largest creative-software companies, with products including Photoshop, Illustrator and Adobe XD.

LOCKED HEADLINE:
"ADOBE XD — DESIGN / PROTOTYPE / SHARE"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV044_ADOBE_XD_WORKFLOW_UI.png
Image 2: 12_SOURCE_PREP/RV045_ADOBE_XD_PROTOTYPING_UI.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline and exact fact labels explicitly required by this beat.

SOURCE ROLE:
Exact authentic product UI. Authentic Adobe XD workflow and prototype interaction UI.

COMPOSITION:
Preserve native UI content/colors. Authentic UI crop(s) inside WHAT IT COST charcoal/warm-paper frame; signal-red accent only; bottom 22% quiet. One UI primary, second supporting with depth/asymmetry; never a sterile split-screen. Preserve both authentic interfaces with asymmetry and physical depth; no fake controls and no sterile split-screen.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate. Do not fall back to a generic dark desk with random papers.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, flag/Capitol symbolism unrelated to the source.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions. No editor instructions inside the image.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F012 / B012

**LOCKED HEADLINE:** `DEAL ANNOUNCEMENT — ~$20B`

**TIMING:** 95.480 → 104.940 (9.460 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/B012_RV047_DOCUMENT.png` → Higgsfield media `c300e57c-6744-4757-8c86-43a3b50095de` (alias of `12_SOURCE_PREP/RV047_ANNOUNCEMENT_HEADLINE_CROP.png`)

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B012, ready to place directly into the finished film.

STORY PURPOSE:
On September fifteenth, twenty twenty-two, Adobe and Figma announced a definitive merger agreement. The headline number was approximately twenty billion dollars.

LOCKED HEADLINE:
"DEAL ANNOUNCEMENT — ~$20B"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/B012_RV047_DOCUMENT.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline and exact fact labels explicitly required by this beat.

SOURCE ROLE:
Primary authentic evidence from Adobe acquisition press release PDF. Crop official Adobe acquisition announcement around headline and approximately $20B consideration language; preserve source/date context.

COMPOSITION:
Present the exact source crop as the hero. Hero paper upper-right; editor date tab SEPT 15 2022; no AI redraw. Headline on dark negative space; large readable source crop; one restrained red bracket/highlight only. Make the exact document the hero at roughly 55–70% of frame; preserve readable wording; at most one red bracket and one restrained yellow highlight.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate. Do not fall back to a generic dark desk with random papers.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, flag/Capitol symbolism unrelated to the source.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions. No editor instructions inside the image.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F013 / B013

**LOCKED HEADLINE:** `HALF CASH / HALF STOCK`

**TIMING:** 105.940 → 114.760 (8.820 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV048_8K_MERGER_AGREEMENT_CROP.png` → Higgsfield media `3ebe0696-9f75-4eb8-8105-e7eb75ac056c`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B013, ready to place directly into the finished film.

STORY PURPOSE:
The consideration was expected to be roughly half cash and half Adobe stock. But the agreement did not guarantee that the transaction would close.

LOCKED HEADLINE:
"HALF CASH / HALF STOCK"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV048_8K_MERGER_AGREEMENT_CROP.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
image 1 = Adobe Form 8-K merger-agreement excerpt; it is the clipped excerpt, shown unchanged — never retype it. No other document may appear.

COMPOSITION:
one heavy blank sheet of paper folded exactly in half lies open on a dark desk: left half warm ivory, right half cool grey, a thin deep-red line along the fold. One small paper excerpt is paper-clipped to the sheet's upper-right corner. headline zone inside the top 45% and left 40% of the frame. The folded sheet center-right, between 20% and 76% of frame height. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Make the authentic document the hero at roughly 55–70% of frame; preserve readable wording; at most one deep-red bracket and one restrained warm-yellow highlight.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F014 / B014

**LOCKED HEADLINE:** `CLOSING CONDITIONS`

**TIMING:** 115.820 → 123.680 (7.860 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV004_ADOBE_HQ_SAN_JOSE.jpg` → Higgsfield media `8b56d0ef-20ce-4620-9fbc-a533787b332f`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B014, ready to place directly into the finished film.

STORY PURPOSE:
It still depended on regulatory approvals and other closing conditions. And by the time the public heard the twenty-billion-dollar headline,

LOCKED HEADLINE:
"CLOSING CONDITIONS"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV004_ADOBE_HQ_SAN_JOSE.jpg

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
image 1 = Adobe headquarters, San Jose; it is the print, shown unchanged. No other photo, document or logo may appear.

COMPOSITION:
a large photographic print of a corporate headquarters at dusk stands on a dark desk. In front of it, three identical blank ivory index cards lie in a neat row, face up, the first one with a thin deep-red top edge. headline zone inside the top 40% and left 38% of the frame. The print fills the right 60%, between 8% and 70% of frame height; the cards lie in front of its lower edge, above 78%. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Make authentic photo evidence large enough to identify the people/place/event; preserve faces and source composition.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F016 / B016

**LOCKED HEADLINE:** `NEGOTIATION RECORD`

**TIMING:** 131.120 → 137.460 (6.340 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/B016_RV050_DOCUMENT.png` → Higgsfield media `4d458471-bcf8-4c86-808e-98fc73c9ac62` (alias of `12_SOURCE_PREP/RV050_JUNE19_NO_FEE_CROP.png`)

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B016, ready to place directly into the finished film.

STORY PURPOSE:
The negotiation record filed with the Securities and Exchange Commission shows how that number entered the deal.

LOCKED HEADLINE:
"NEGOTIATION RECORD"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/B016_RV050_DOCUMENT.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline and exact fact labels explicitly required by this beat.

SOURCE ROLE:
Primary authentic evidence from SEC / 424B3 prospectus. Crop 424B3 Background of the Merger area that establishes negotiation chronology; documentary bridge, not text wall.

COMPOSITION:
Present the exact source crop as the hero. Tight authentic paper excerpt with one source label. Headline on dark negative space; large readable source crop; one restrained red bracket/highlight only. Make the exact document the hero at roughly 55–70% of frame; preserve readable wording; at most one red bracket and one restrained yellow highlight.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate. Do not fall back to a generic dark desk with random papers.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, flag/Capitol symbolism unrelated to the source.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions. No editor instructions inside the image.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F017 / B017

**LOCKED HEADLINE:** `BEFORE 2022`

**TIMING:** 138.300 → 146.580 (8.280 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV013_FIGMA_FOUNDERS_ARCHIVAL.jpg` → Higgsfield media `cd54ef67-c63d-4d13-be87-97556941d0de`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B017, ready to place directly into the finished film.

STORY PURPOSE:
Adobe and Figma had discussed possible combinations before twenty twenty-two, but those earlier conversations did not produce a transaction.

LOCKED HEADLINE:
"BEFORE 2022"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV013_FIGMA_FOUNDERS_ARCHIVAL.jpg

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
image 1 = archival Figma founders office photo; it is the print, unchanged — keep every face and person exactly as photographed; add no people.

COMPOSITION:
one old, slightly faded photographic print with a curled corner hangs alone on a dark wall, fixed by a single brass pin. From the pin a short deep-red thread hangs loose and ends in empty air, attached to nothing. headline zone inside the top 45% and left 40% of the frame. The print on the right half, between 10% and 70% of frame height, slightly tilted; the loose thread ends above 78%. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Make authentic photo evidence large enough to identify the people/place/event; preserve faces and source composition.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F018 / B018

**LOCKED HEADLINE:** `TALKS RESTART`

**TIMING:** 147.460 → 155.480 (8.020 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV065_ADOBE_IDENTIFIER.png` → Higgsfield media `d22816b6-faa3-45eb-a5f3-ef985e2375ce`
- Image 2: `12_SOURCE_PREP/RV066_FIGMA_IDENTIFIER.png` → Higgsfield media `413e03f3-a9a9-4e43-8de0-888ed029875a`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B018, ready to place directly into the finished film.

STORY PURPOSE:
Serious acquisition talks restarted in April twenty twenty-two. In May, the companies entered a confidentiality agreement

LOCKED HEADLINE:
"TALKS RESTART"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV065_ADOBE_IDENTIFIER.png
Image 2: 12_SOURCE_PREP/RV066_FIGMA_IDENTIFIER.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
image 1 = Adobe identifier; image 2 = Figma identifier — each on its own card, unchanged, never broken or redrawn.

COMPOSITION:
top-down view of a dark desk. Two small paper cards, each carrying one company identifier, lie a short distance apart, joined by a deep-red thread with one neat knot in the middle. To the right lies a closed plain manila folder tied shut with red string. headline zone inside the top 40% and left 40% of the frame. Cards and thread center, folder right, all between 30% and 76% of frame height. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Establish one dominant factual source and subordinate support; communicate the beat in under one second.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F019 / B019

**LOCKED HEADLINE:** `THEN CAME THE PRICE`

**TIMING:** 155.480 → 161.160 (5.680 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV001_NARAYEN_PORTRAIT.jpg` → Higgsfield media `7c86652d-2b71-42f6-99c7-3a4b1a78a5ff`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B019, ready to place directly into the finished film.

STORY PURPOSE:
and Figma began providing confidential information to Adobe. Then came the price.

LOCKED HEADLINE:
"THEN CAME THE PRICE"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV001_NARAYEN_PORTRAIT.jpg

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
image 1 = Adobe CEO portrait; it is the print, unchanged — keep the face exactly as photographed; add no people.

COMPOSITION:
on a dark desk, one portrait photograph printed on warm paper lies on the right; in the left-center a single sealed blank ivory envelope bound with a thin deep-red string rests in soft light. headline zone inside the top 40% and left 42% of the frame; the envelope below it, between 45% and 72% of frame height. The portrait fills the right half, between 10% and 72%. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Make authentic photo evidence large enough to identify the people/place/event; preserve faces and source composition.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F021 / B021

**LOCKED HEADLINE:** `NO FEE YET`

**TIMING:** 170.080 → 179.580 (9.500 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV012_FIELD_PORTRAIT.jpg` → Higgsfield media `11ed80fd-8035-4260-94c1-e6faa0bf96f9`
- Image 2: `12_SOURCE_PREP/RV050_JUNE19_NO_FEE_CROP.png` → Higgsfield media `4d458471-bcf8-4c86-808e-98fc73c9ac62`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B021, ready to place directly into the finished film.

STORY PURPOSE:
roughly half cash and half stock. That proposal did not yet include a termination fee. Figma did not negotiate only the headline price.

LOCKED HEADLINE:
"NO FEE YET"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV012_FIELD_PORTRAIT.jpg
Image 2: 12_SOURCE_PREP/RV050_JUNE19_NO_FEE_CROP.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
none — the frame contains no documents, photos, screenshots or logos.

COMPOSITION:
one clean blank ivory sheet lies on a dark desk. Clipped to its right edge is a clear index-tab holder with a thin deep-red rim, visibly empty — nothing is inside it. headline zone inside the top 45% and left 40% of the frame. The sheet center-right, between 20% and 74% of frame height, with generous dark space around. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Establish one dominant factual source and subordinate support; communicate the beat in under one second.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F023 / B023

**LOCKED HEADLINE:** `JULY 20 — ADOBE AGREES TO $1B FEE`

**TIMING:** 189.880 → 197.260 (7.380 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/B023_RV052_DOCUMENT.png` → Higgsfield media `4800d63a-3f98-4b76-a2d3-41eb300faf30` (alias of `12_SOURCE_PREP/RV052_JULY20_FEE_AGREED_CROP.png`)

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B023, ready to place directly into the finished film.

STORY PURPOSE:
to obtain required antitrust approvals. Then, on July twentieth, Adobe came back with a revised proposal.

LOCKED HEADLINE:
"JULY 20 — ADOBE AGREES TO $1B FEE"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/B023_RV052_DOCUMENT.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline and exact fact labels explicitly required by this beat.

SOURCE ROLE:
Primary authentic evidence from SEC / 424B3 prospectus. Crop July 20 paragraph establishing Adobe's revised proposal with $1B reverse termination fee.

COMPOSITION:
Present the exact source crop as the hero. Exact crop; date and $1B summary editor-built outside source pixels. Headline on dark negative space; large readable source crop; one restrained red bracket/highlight only. Make the exact document the hero at roughly 55–70% of frame; preserve readable wording; at most one red bracket and one restrained yellow highlight.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate. Do not fall back to a generic dark desk with random papers.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, flag/Capitol symbolism unrelated to the source.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions. No editor instructions inside the image.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F024 / B024

**LOCKED HEADLINE:** `THE FEE ENTERS THE DEAL`

**TIMING:** 198.400 → 207.520 (9.120 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV012_FIELD_PORTRAIT.jpg` → Higgsfield media `11ed80fd-8035-4260-94c1-e6faa0bf96f9`
- Image 2: `12_SOURCE_PREP/RV065_ADOBE_IDENTIFIER.png` → Higgsfield media `d22816b6-faa3-45eb-a5f3-ef985e2375ce`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B024, ready to place directly into the finished film.

STORY PURPOSE:
The twenty-billion-dollar price remained. And now the proposal included a one-billion-dollar reverse termination fee. That sequence matters.

LOCKED HEADLINE:
"THE FEE ENTERS THE DEAL"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV012_FIELD_PORTRAIT.jpg
Image 2: 12_SOURCE_PREP/RV065_ADOBE_IDENTIFIER.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
image 1 = Figma CEO portrait (the print) — keep the face exactly as photographed, add no people; image 2 = Adobe identifier (on the small card), unchanged.

COMPOSITION:
on a dark desk, a portrait photograph printed on warm paper lies on the right; one solid deep-red blank index tab is clipped to its left edge. A small paper card with a company identifier sits left-center, the red tab reaching toward it. headline zone inside the top 40% and left 42% of the frame; the identifier card below it, between 48% and 72% of frame height. The portrait fills the right half, between 10% and 72%. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Make authentic photo evidence large enough to identify the people/place/event; preserve faces and source composition.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F026 / B026

**LOCKED HEADLINE:** `ADOBE AGREES`

**TIMING:** 217.820 → 222.920 (5.100 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV004_ADOBE_HQ_SAN_JOSE.jpg` → Higgsfield media `8b56d0ef-20ce-4620-9fbc-a533787b332f`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B026, ready to place directly into the finished film.

STORY PURPOSE:
July twentieth: Adobe agrees to a one-billion-dollar reverse termination fee.

LOCKED HEADLINE:
"ADOBE AGREES"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV004_ADOBE_HQ_SAN_JOSE.jpg

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
image 1 = Adobe headquarters, San Jose; it is the print, shown unchanged. No other photo or logo may appear.

COMPOSITION:
a wide photograph of a corporate headquarters under muted dusk light stands as a large print; in front of it, a closed black fountain pen rests across the edge of a blank contract page. headline zone inside the top 45% and left 36% of the frame. The print fills the right 64%, between 8% and 70% of frame height; pen and page in front of its lower edge, above 78%. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Make authentic photo evidence large enough to identify the people/place/event; preserve faces and source composition.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F027 / B027

**LOCKED HEADLINE:** `THE COST WAS ALREADY THERE`

**TIMING:** 223.680 → 229.520 (5.840 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV053_10Q_CLOSING_RISK_CROP.png` → Higgsfield media `a338e919-ab01-48d7-b42e-16fa2ac08da5`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B027, ready to place directly into the finished film.

STORY PURPOSE:
More than a year before the acquisition ended, the billion-dollar cost was already inside the deal architecture.

LOCKED HEADLINE:
"THE COST WAS ALREADY THERE"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV053_10Q_CLOSING_RISK_CROP.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
image 1 = Adobe 10-Q closing-risk disclosure excerpt; it is the pulled sheet, shown unchanged — never retype it.

COMPOSITION:
a low-angle close view of a thick stack of blank paper on a dark desk; one sheet is pulled a few centimeters out of the middle of the stack, lit by a narrow beam, a thin vertical deep-red bracket in its margin. headline zone inside the top 40% and left 42% of the frame. The stack spans center-right between 30% and 76% of frame height; the pulled sheet is the sharpest element. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Make the authentic document the hero at roughly 55–70% of frame; preserve readable wording; at most one deep-red bracket and one restrained warm-yellow highlight.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F029 / B029

**LOCKED HEADLINE:** `IF CLOSING FAILS`

**TIMING:** 238.600 → 246.320 (7.720 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV062_TERMINATION_AGREEMENT_CROP.png` → Higgsfield media `434ba753-529b-46bc-b1ad-3992af41be27`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B029, ready to place directly into the finished film.

STORY PURPOSE:
In simple terms, the buyer agrees that if specified closing failures occur, the seller can receive a defined payment.

LOCKED HEADLINE:
"IF CLOSING FAILS"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV062_TERMINATION_AGREEMENT_CROP.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
none — the frame contains no documents, photos, screenshots or logos.

COMPOSITION:
one thread enters from the left and meets a brass pin, where it splits: an upper pale-grey thread runs to an empty outlined ivory card; a lower deep-red thread runs to a solid deep-red card. Nothing is written anywhere. headline zone inside the top 25% of the frame, left half. Fork point center-left at 50% of frame height; both cards on the right half, the lower card ending above 78%. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Establish one dominant factual source and subordinate support; communicate the beat in under one second.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F030 / B030

**LOCKED HEADLINE:** `SECTION 8.2 — $1B / NOT A PENALTY`

**TIMING:** 247.160 → 257.520 (10.360 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/B030_RV049_DOCUMENT.png` → Higgsfield media `b14e6e93-386d-44fd-8137-2b399880d46c` (alias of `12_SOURCE_PREP/RV049_S8_2_TERMINATION_FEE_CROP.png`)

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B030, ready to place directly into the finished film.

STORY PURPOSE:
In the Adobe-Figma agreement, the number was one billion dollars. Section eight-point-two of the merger agreement set out the fee in defined antitrust and closing circumstances.

LOCKED HEADLINE:
"SECTION 8.2 — $1B / NOT A PENALTY"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/B030_RV049_DOCUMENT.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline and exact fact labels explicitly required by this beat.

SOURCE ROLE:
Primary authentic evidence from SEC / Agreement and Plan of Merger. Crop Section 8.2 around termination-fee/liquidated-damages language and not-a-penalty distinction.

COMPOSITION:
Present the exact source crop as the hero. Large authentic crop; one verified-line highlight; no fake signature/seal. Headline on dark negative space; large readable source crop; one restrained red bracket/highlight only. Make the exact document the hero at roughly 55–70% of frame; preserve readable wording; at most one red bracket and one restrained yellow highlight.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate. Do not fall back to a generic dark desk with random papers.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, flag/Capitol symbolism unrelated to the source.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions. No editor instructions inside the image.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F032 / B032

**LOCKED HEADLINE:** `LIQUIDATED DAMAGES`

**TIMING:** 265.220 → 273.100 (7.880 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV061_8K_TERMINATION_CROP.png` → Higgsfield media `a38da969-fa87-4ece-83eb-98a5d82f6ed9`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B032, ready to place directly into the finished film.

STORY PURPOSE:
It describes the payment as liquidated damages. So the agreement did more than describe the deal the companies wanted to close.

LOCKED HEADLINE:
"LIQUIDATED DAMAGES"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV061_8K_TERMINATION_CROP.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
none — the frame contains no documents, photos, screenshots or logos.

COMPOSITION:
an open ledger book on a dark desk, pages blank with faint grey ruled lines. On one line a solid deep-red bar fills a precise measured length; an unmarked brass straightedge lies parallel to it. headline zone inside the top 40% and left 40% of the frame. The ledger center-right at a gentle angle, between 25% and 76% of frame height. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Establish one dominant factual source and subordinate support; communicate the beat in under one second.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F033 / B033

**LOCKED HEADLINE:** `FAILURE HAD A PRICE`

**TIMING:** 273.980 → 278.820 (4.840 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV048_8K_MERGER_AGREEMENT_CROP.png` → Higgsfield media `3ebe0696-9f75-4eb8-8105-e7eb75ac056c`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B033, ready to place directly into the finished film.

STORY PURPOSE:
It also described a financial consequence if that deal failed under the specified conditions.

LOCKED HEADLINE:
"FAILURE HAD A PRICE"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV048_8K_MERGER_AGREEMENT_CROP.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
image 1 = Adobe Form 8-K merger-agreement excerpt; it is the paper, shown unchanged — never retype it. No other document may appear.

COMPOSITION:
one paper excerpt lies on a dark desk; through a punched hole in its lower-left corner a thin deep-red string is tied to a blank manila price tag resting beside it. headline zone inside the top 45% and left 40% of the frame. The excerpt on the right half, between 10% and 70% of frame height; the tag near the center, above 78%. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Make the authentic document the hero at roughly 55–70% of frame; preserve readable wording; at most one deep-red bracket and one restrained warm-yellow highlight.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F034 / B034

**LOCKED HEADLINE:** `UPSIDE ~$20B / DOWNSIDE $1B`

**TIMING:** 279.980 → 285.720 (5.740 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV047_ANNOUNCEMENT_HEADLINE_CROP.png` → Higgsfield media `c300e57c-6744-4757-8c86-43a3b50095de`
- Image 2: `12_SOURCE_PREP/RV049_S8_2_TERMINATION_FEE_CROP.png` → Higgsfield media `b14e6e93-386d-44fd-8137-2b399880d46c`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B034, ready to place directly into the finished film.

STORY PURPOSE:
The twenty-billion-dollar number described the upside. The one-billion-dollar clause priced part of the downside.

LOCKED HEADLINE:
"UPSIDE ~$20B / DOWNSIDE $1B"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV047_ANNOUNCEMENT_HEADLINE_CROP.png
Image 2: 12_SOURCE_PREP/RV049_S8_2_TERMINATION_FEE_CROP.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline and exact fact labels explicitly required by this beat.

SOURCE ROLE:
Attached sources ground the verified numbers/dates/statuses. Split economics: PROPOSED ACQUISITION ~$20B left; REVERSE TERMINATION FEE $1B right; small CONTRACTUAL RISK ALLOCATION.

COMPOSITION:
Create a premium information frame from verified facts. No plus sign or summed total; one red downside tab. One dominant statement plus one clear comparison/timeline/status structure; source excerpts support the information without PowerPoint styling. Turn only the verified source-grounded facts into an elegant cinematic information composition; exact numbers/dates only; never PowerPoint.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate. Do not fall back to a generic dark desk with random papers.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, flag/Capitol symbolism unrelated to the source, unverified numbers, misleading arithmetic, fake $21B total.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions. No editor instructions inside the image.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F035 / B035

**LOCKED HEADLINE:** `SEPTEMBER 15, 2022`

**TIMING:** 286.680 → 292.860 (6.180 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV025_ADOBE_FIGMA_DEAL_GRAPHIC.png` → Higgsfield media `9ca85935-d9a9-431a-9e5b-9e9de093e54a`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B035, ready to place directly into the finished film.

STORY PURPOSE:
On September fifteenth, twenty twenty-two, the definitive agreement was signed and the transaction became public.

LOCKED HEADLINE:
"SEPTEMBER 15, 2022"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV025_ADOBE_FIGMA_DEAL_GRAPHIC.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
image 1 = official Adobe + Figma deal graphic; it is the framed print, unchanged — never redraw its logos.

COMPOSITION:
a framed print hangs alone on a dark wall under a single spotlight; one deep-red pin is pushed into the wall just above the frame's top center. headline zone inside the top 40% and left 42% of the frame. The framed print center-right, between 12% and 72% of frame height, with wide darkness around. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Make the authentic interface large and readable; preserve native controls, colors and proportions.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F037 / B037

**LOCKED HEADLINE:** `THE DEAL LOOKED NORMAL`

**TIMING:** 303.880 → 308.020 (4.140 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV048_8K_MERGER_AGREEMENT_CROP.png` → Higgsfield media `3ebe0696-9f75-4eb8-8105-e7eb75ac056c`

**R14 SOURCE REBIND (2026-09-30, owner delegated):** RV016 Config 2023 crowd photo does not exist on the official page (current or Wayback 2023). Rebound to RV048 8-K merger-agreement excerpt — the same definitive-agreement evidence (~$20B, half cash / half stock) the locked R10 PASS F037 frame was built on.

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B037, ready to place directly into the finished film.

STORY PURPOSE:
At that moment, the story looked like a conventional giant technology acquisition.

LOCKED HEADLINE:
"THE DEAL LOOKED NORMAL"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV048_8K_MERGER_AGREEMENT_CROP.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
image 1 = Adobe Form 8-K merger-agreement excerpt (Item 1.01, Merger Consideration: approximately $10 billion in cash and approximately $10 billion in Company Shares); it is the paper, shown unchanged — never retype it. No other document may appear.

COMPOSITION:
a tidy dark desk; the authentic 8-K excerpt printed on warm ivory paper lies squarely on the right, calm and orderly like routine corporate paperwork; beside it a neatly closed plain grey folder aligned parallel to the page. headline zone inside the top 45% and left 40% of the frame. Folder and page center-right, between 25% and 74% of frame height. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Make the authentic filing excerpt large enough that the Merger Consideration wording is legible; preserve its exact wording and layout.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same beat meaning, the attached rebound source, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F043 / B043

**LOCKED HEADLINE:** `PHASE TWO`

**TIMING:** 349.400 → 359.780 (10.380 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV055_CMA_PHASE1_DECISION_CROP.png` → Higgsfield media `7b1daf92-ae5f-4190-a979-df9b434a702b`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B043, ready to place directly into the finished film.

STORY PURPOSE:
By June thirtieth, the CMA said there were grounds for deeper competition concerns. On July thirteenth, the transaction was referred for an in-depth Phase Two investigation.

LOCKED HEADLINE:
"PHASE TWO"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV055_CMA_PHASE1_DECISION_CROP.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
image 1 = UK CMA Phase 1 decision title block; it is the clipped excerpt, unchanged — never retype it.

COMPOSITION:
side view of two case folders standing upright in an open cardboard archive box on a dark desk: the front folder thin and closed with one small paper excerpt clipped to its face; the folder behind noticeably thicker, one deep-red tab rising from it. headline zone inside the top 40% and left 40% of the frame. The box center-right, between 28% and 76% of frame height. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Make the authentic document the hero at roughly 55–70% of frame; preserve readable wording; at most one deep-red bracket and one restrained warm-yellow highlight.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F045 / B045

**LOCKED HEADLINE:** `UK / EU / U.S. — THREE SEPARATE PROCESSES`

**TIMING:** 369.060 → 377.820 (8.760 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV054_CMA_CASE_TIMELINE_CROP.png` → Higgsfield media `2be9b5d2-084c-4c6e-bd2f-b5dcc0cfc798`
- Image 2: `12_SOURCE_PREP/RV068_BERLAYMONT.jpg` → Higgsfield media `a3f3abf1-ac8b-4668-9e2c-8f906599b70e`
- Image 3: `12_SOURCE_PREP/RV060_DOJ_STATEMENT_CROP.png` → Higgsfield media `6c87dd96-a09c-44e7-879f-211ceb4098de`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B045, ready to place directly into the finished film.

STORY PURPOSE:
And in the United States, the Justice Department's Antitrust Division was also investigating the transaction. These were separate processes with different procedures.

LOCKED HEADLINE:
"UK / EU / U.S. — THREE SEPARATE PROCESSES"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV054_CMA_CASE_TIMELINE_CROP.png
Image 2: 12_SOURCE_PREP/RV068_BERLAYMONT.jpg
Image 3: 12_SOURCE_PREP/RV060_DOJ_STATEMENT_CROP.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline and exact fact labels explicitly required by this beat.

SOURCE ROLE:
Attached sources ground the verified numbers/dates/statuses. Three-lane map/timeline: UK CMA — MERGER REVIEW; EU COMMISSION — IN-DEPTH REVIEW; U.S. DOJ — INVESTIGATION.

COMPOSITION:
Create a premium information frame from verified facts. No seals; simple labels/dates; distinct lanes. One dominant statement plus one clear comparison/timeline/status structure; source excerpts support the information without PowerPoint styling. Turn only the verified source-grounded facts into an elegant cinematic information composition; exact numbers/dates only; never PowerPoint.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate. Do not fall back to a generic dark desk with random papers.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, flag/Capitol symbolism unrelated to the source, unverified numbers, misleading arithmetic, fake $21B total.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions. No editor instructions inside the image.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F046 / B046

**LOCKED HEADLINE:** `FORMAL OBJECTIONS`

**TIMING:** 378.720 → 382.580 (3.860 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV055_CMA_PHASE1_DECISION_CROP.png` → Higgsfield media `7b1daf92-ae5f-4190-a979-df9b434a702b`
- Image 2: `12_SOURCE_PREP/RV068_BERLAYMONT.jpg` → Higgsfield media `a3f3abf1-ac8b-4668-9e2c-8f906599b70e`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B046, ready to place directly into the finished film.

STORY PURPOSE:
The UK and EU reviews developed formal competition objections.

LOCKED HEADLINE:
"FORMAL OBJECTIONS"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV055_CMA_PHASE1_DECISION_CROP.png
Image 2: 12_SOURCE_PREP/RV068_BERLAYMONT.jpg

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
image 1 = UK CMA Phase 1 decision title block (left), unchanged — never retype it; image 2 = European Commission Berlaymont (right print), unchanged.

COMPOSITION:
on a dark wall, a paper excerpt (left) and a photographic print of an institutional building (right) are pinned at equal size; each has one small blank deep-red paper flag clipped to its top edge. The wall between them is plain and empty — a deliberate void. headline zone = top center, inside the top 22% of the frame. The two items between 30% and 74% of frame height, in the left and right thirds. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Establish one dominant factual source and subordinate support; communicate the beat in under one second.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F048 / B048

**LOCKED HEADLINE:** `SIGNED ≠ CLOSED`

**TIMING:** 395.560 → 403.160 (7.600 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV048_8K_MERGER_AGREEMENT_CROP.png` → Higgsfield media `3ebe0696-9f75-4eb8-8105-e7eb75ac056c`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B048, ready to place directly into the finished film.

STORY PURPOSE:
Adobe and Figma already had a merger agreement, but the companies still needed the required approvals before the transaction could actually be completed.

LOCKED HEADLINE:
"SIGNED ≠ CLOSED"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV048_8K_MERGER_AGREEMENT_CROP.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
image 1 = Adobe Form 8-K merger-agreement excerpt; it is the left excerpt, unchanged — never retype it.

COMPOSITION:
on a dark desk, left: a paper excerpt with a closed black fountain pen resting across it. Right, across a wide empty gap: one blank card defined only by a thin pale-grey outline, untouched. headline zone = top center, inside the top 22% of the frame. Excerpt with pen in the left 40%, outlined card in the right 30%, both between 30% and 74% of frame height. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Make the authentic document the hero at roughly 55–70% of frame; preserve readable wording; at most one deep-red bracket and one restrained warm-yellow highlight.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F058 / B058

**LOCKED HEADLINE:** `PRESSURE, NOT FINALITY`

**TIMING:** 481.820 → 490.200 (8.380 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV056_CMA_PROVISIONAL_FINDINGS_CROP.png` → Higgsfield media `a6e23092-1989-4904-abbb-00b14e45b417`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B058, ready to place directly into the finished film.

STORY PURPOSE:
and said that remedy would be substantially similar to prohibition while introducing additional risks. The pressure was real.

LOCKED HEADLINE:
"PRESSURE, NOT FINALITY"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV056_CMA_PROVISIONAL_FINDINGS_CROP.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
image 1 = UK CMA provisional-findings excerpt; it is the excerpt on the stack, unchanged — never retype it.

COMPOSITION:
on a dark desk, a heavy black steel clamp presses down on a short stack of paper; one paper excerpt is fixed to the front of the stack. To the right a single clean blank sheet lies untouched in soft light. headline zone inside the top 40% and left 38% of the frame. Clamp and stack at center, blank sheet center-right, all between 30% and 76% of frame height. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Make the authentic document the hero at roughly 55–70% of frame; preserve readable wording; at most one deep-red bracket and one restrained warm-yellow highlight.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F060 / B060

**LOCKED HEADLINE:** `ADOBE + FIGMA PUSH BACK`

**TIMING:** 502.040 → 509.740 (7.700 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV009_NARAYEN_MAX_2022_STAGE.jpg` → Higgsfield media `78c95d50-0a84-43d0-bb88-55b8e24190b4`
- Image 2: `12_SOURCE_PREP/RV012_FIELD_PORTRAIT.jpg` → Higgsfield media `11ed80fd-8035-4260-94c1-e6faa0bf96f9`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B060, ready to place directly into the finished film.

STORY PURPOSE:
Adobe and Figma did not accept the regulators' theories as settled fact. In their submissions to the CMA, the companies argued

LOCKED HEADLINE:
"ADOBE + FIGMA PUSH BACK"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV009_NARAYEN_MAX_2022_STAGE.jpg
Image 2: 12_SOURCE_PREP/RV012_FIELD_PORTRAIT.jpg

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
image 1 = Adobe MAX 2022 keynote stage (large print); image 2 = Figma CEO portrait (small print). Both unchanged — keep every face and person exactly as photographed; add no people.

COMPOSITION:
on a dark desk, a large event-photograph print (right) and a smaller portrait print (left-center) lie apart; between them rests a thick bound submission with a plain blank cover. headline zone inside the top 35% and left 42% of the frame; the portrait print below it, between 40% and 74% of frame height. The large print on the right half, between 10% and 72%. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Make authentic photo evidence large enough to identify the people/place/event; preserve faces and source composition.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F066 / B066

**LOCKED HEADLINE:** `THE COMPANIES' CHARACTERIZATION`

**TIMING:** 555.500 → 563.200 (7.700 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV004_ADOBE_HQ_SAN_JOSE.jpg` → Higgsfield media `8b56d0ef-20ce-4620-9fbc-a533787b332f`
- Image 2: `12_SOURCE_PREP/RV066_FIGMA_IDENTIFIER.png` → Higgsfield media `413e03f3-a9a9-4e43-8de0-888ed029875a`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B066, ready to place directly into the finished film.

STORY PURPOSE:
effectively pointed toward either prohibition or divestiture of Figma Design. That was the companies' characterization.

LOCKED HEADLINE:
"THE COMPANIES' CHARACTERIZATION"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV004_ADOBE_HQ_SAN_JOSE.jpg
Image 2: 12_SOURCE_PREP/RV066_FIGMA_IDENTIFIER.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
image 1 = Adobe headquarters, San Jose (the print), unchanged; image 2 = Figma identifier (small card), unchanged.

COMPOSITION:
on a dark desk, a photographic print of a corporate headquarters lies partly covered by a single blank response sheet; a solid vertical deep-red quote bar runs along the sheet's left edge; a small identifier card is clipped to the sheet's top corner. headline zone inside the top 40% and left 40% of the frame. Print and sheet center-right, between 18% and 76% of frame height. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Make authentic photo evidence large enough to identify the people/place/event; preserve faces and source composition.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F069 / B069

**LOCKED HEADLINE:** `MUTUAL TERMINATION — DEC 17 2023`

**TIMING:** 582.720 → 592.620 (9.900 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/B069_RV062_DOCUMENT.png` → Higgsfield media `434ba753-529b-46bc-b1ad-3992af41be27` (alias of `12_SOURCE_PREP/RV062_TERMINATION_AGREEMENT_CROP.png`)

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B069, ready to place directly into the finished film.

STORY PURPOSE:
The final move came from Adobe and Figma themselves. On December seventeenth, twenty twenty-three, the companies approved and signed a mutual termination agreement.

LOCKED HEADLINE:
"MUTUAL TERMINATION — DEC 17 2023"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/B069_RV062_DOCUMENT.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline and exact fact labels explicitly required by this beat.

SOURCE ROLE:
Primary authentic evidence from SEC / Mutual Termination Agreement. Crop Mutual Termination Agreement title/date and operative termination context.

COMPOSITION:
Present the exact source crop as the hero. Exact SEC-hosted agreement crop; editor label MUTUAL TERMINATION, no court styling. Headline on dark negative space; large readable source crop; one restrained red bracket/highlight only. Make the exact document the hero at roughly 55–70% of frame; preserve readable wording; at most one red bracket and one restrained yellow highlight.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate. Do not fall back to a generic dark desk with random papers.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, flag/Capitol symbolism unrelated to the source.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions. No editor instructions inside the image.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F070 / B070

**LOCKED HEADLINE:** `NO CLEAR PATH`

**TIMING:** 593.360 → 603.920 (10.560 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV061_8K_TERMINATION_CROP.png` → Higgsfield media `a38da969-fa87-4ece-83eb-98a5d82f6ed9`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B070, ready to place directly into the finished film.

STORY PURPOSE:
The next day, they announced that the acquisition was over. Their public explanation was direct. They said there was no clear path to obtaining the necessary regulatory approvals

LOCKED HEADLINE:
"NO CLEAR PATH"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV061_8K_TERMINATION_CROP.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
image 1 = Adobe Form 8-K termination excerpt; it is the paper, unchanged — never retype, redraw or extend it.

COMPOSITION:
one paper excerpt on warm aged paper lies slightly angled on a dark desk, held by a black binder clip, a thin vertical deep-red bracket in its margin beside the text. headline zone inside the top 45% and left 40% of the frame. The excerpt fills the right 55%, between 10% and 75% of frame height. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Make the authentic document the hero at roughly 55–70% of frame; preserve readable wording; at most one deep-red bracket and one restrained warm-yellow highlight.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F074 / B074

**LOCKED HEADLINE:** `DOJ WELCOMES ABANDONMENT`

**TIMING:** 631.240 → 639.700 (8.460 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV060_DOJ_STATEMENT_CROP.png` → Higgsfield media `6c87dd96-a09c-44e7-879f-211ceb4098de`
- Image 2: `12_SOURCE_PREP/RV070_DOJ_HQ.jpg` → Higgsfield media `7c2e44fc-214e-44de-a75f-f84ace946e33`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B074, ready to place directly into the finished film.

STORY PURPOSE:
And in the United States, the Justice Department's Antitrust Division publicly welcomed the abandonment and confirmed that it had investigated the transaction.

LOCKED HEADLINE:
"DOJ WELCOMES ABANDONMENT"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV060_DOJ_STATEMENT_CROP.png
Image 2: 12_SOURCE_PREP/RV070_DOJ_HQ.jpg

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
image 1 = DOJ Antitrust Division statement excerpt (main), unchanged — never retype it; image 2 = U.S. Department of Justice headquarters (small print), unchanged.

COMPOSITION:
on a dark desk a paper excerpt lies large and sharp with a thin vertical deep-red bracket in its margin; a small photographic print of a government building sits partly tucked under its upper-right corner. headline zone inside the top 45% and left 40% of the frame. The excerpt fills the right 55%, between 12% and 76% of frame height; the small print at its upper-right. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Establish one dominant factual source and subordinate support; communicate the beat in under one second.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F075 / B075

**LOCKED HEADLINE:** `INVESTIGATION, NO BLOCKING LAWSUIT`

**TIMING:** 640.700 → 647.060 (6.360 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV070_DOJ_HQ.jpg` → Higgsfield media `7c2e44fc-214e-44de-a75f-f84ace946e33`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B075, ready to place directly into the finished film.

STORY PURPOSE:
The public Stage One record does not show a DOJ merger lawsuit or a court judgment blocking the deal.

LOCKED HEADLINE:
"INVESTIGATION, NO BLOCKING LAWSUIT"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV070_DOJ_HQ.jpg

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
image 1 = U.S. Department of Justice headquarters exterior; it is the print, unchanged — no seal close-ups.

COMPOSITION:
a photographic print of a government headquarters lies flat on a dark desk in cold blue-grey light; one closed plain folder rests across its lower-right corner. headline zone inside the top 45% and left 40% of the frame. Print and folder center-right, between 18% and 76% of frame height, generous darkness around. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Establish one dominant factual source and subordinate support; communicate the beat in under one second.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F080 / B080

**LOCKED HEADLINE:** `DECEMBER 20, 2023`

**TIMING:** 680.580 → 689.260 (8.680 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV004_ADOBE_HQ_SAN_JOSE.jpg` → Higgsfield media `8b56d0ef-20ce-4620-9fbc-a533787b332f`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B080, ready to place directly into the finished film.

STORY PURPOSE:
It also made the payment Figma's sole and exclusive remedy under the merger agreement. On December twentieth, twenty twenty-three, Adobe paid.

LOCKED HEADLINE:
"DECEMBER 20, 2023"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV004_ADOBE_HQ_SAN_JOSE.jpg

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
image 1 = Adobe headquarters, San Jose; it is the print, unchanged.

COMPOSITION:
a photographic print of a corporate headquarters in cool early-morning light hangs on a dark wall; one deep-red pin is pushed in just above its top edge. headline zone inside the top 40% and left 42% of the frame. The print center-right, between 12% and 72% of frame height, wide darkness around. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Make authentic photo evidence large enough to identify the people/place/event; preserve faces and source composition.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F081 / B081

**LOCKED HEADLINE:** `ADOBE PAYS • FIGMA RECEIVES`

**TIMING:** 690.300 → 697.820 (7.520 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV063_10K_PAYMENT_CROP.png` → Higgsfield media `ec7d4f0b-ad22-406d-b354-d8c0a83249ef`
- Image 2: `12_SOURCE_PREP/RV064_S1_FEE_RECEIPT_CROP.png` → Higgsfield media `25f3e436-2ef9-442d-b9d4-8829963b2646`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B081, ready to place directly into the finished film.

STORY PURPOSE:
Adobe later disclosed that it used cash on hand. Figma later disclosed that it received the same one-billion-dollar payment.

LOCKED HEADLINE:
"ADOBE PAYS • FIGMA RECEIVES"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV063_10K_PAYMENT_CROP.png
Image 2: 12_SOURCE_PREP/RV064_S1_FEE_RECEIPT_CROP.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
image 1 = Adobe FY2023 10-K payment excerpt (left); image 2 = Figma S-1 fee-receipt excerpt (right). Both unchanged — never retype them.

COMPOSITION:
top-down view of a dark desk; two paper excerpts lie far apart, left and right, joined by one straight thin deep-red line across the empty dark space between them. headline zone = top center, inside the top 22% of the frame. Excerpts symmetric between 30% and 76% of frame height. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Establish one dominant factual source and subordinate support; communicate the beat in under one second.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F082 / B082

**LOCKED HEADLINE:** `THE MONEY MOVED`

**TIMING:** 698.480 → 707.700 (9.220 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV065_ADOBE_IDENTIFIER.png` → Higgsfield media `d22816b6-faa3-45eb-a5f3-ef985e2375ce`
- Image 2: `12_SOURCE_PREP/RV066_FIGMA_IDENTIFIER.png` → Higgsfield media `413e03f3-a9a9-4e43-8de0-888ed029875a`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B082, ready to place directly into the finished film.

STORY PURPOSE:
Those later filings are important because they confirm the consequence from both sides of the transaction. The fee was not merely a number left in an abandoned contract.

LOCKED HEADLINE:
"THE MONEY MOVED"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV065_ADOBE_IDENTIFIER.png
Image 2: 12_SOURCE_PREP/RV066_FIGMA_IDENTIFIER.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
image 1 = Adobe identifier (near card); image 2 = Figma identifier (far card). Both unchanged and small.

COMPOSITION:
a dark wall seen at a raking side angle; two small identifier cards are pinned far apart along it, and one taut deep-red thread runs between them, receding in perspective. headline zone inside the top 35% and left 42% of the frame. Near card center-left, far card toward the right edge; the thread crosses the band between 40% and 70% of frame height. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Establish one dominant factual source and subordinate support; communicate the beat in under one second.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F083 / B083

**LOCKED HEADLINE:** `DEC 17 → DEC 20`

**TIMING:** 708.420 → 718.400 (9.980 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV062_TERMINATION_AGREEMENT_CROP.png` → Higgsfield media `434ba753-529b-46bc-b1ad-3992af41be27`
- Image 2: `12_SOURCE_PREP/RV063_10K_PAYMENT_CROP.png` → Higgsfield media `ec7d4f0b-ad22-406d-b354-d8c0a83249ef`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B083, ready to place directly into the finished film.

STORY PURPOSE:
It became an actual transfer of cash. On December seventeenth, the companies ended the merger. Three days later, the one-billion-dollar clause became cash.

LOCKED HEADLINE:
"DEC 17 → DEC 20"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV062_TERMINATION_AGREEMENT_CROP.png
Image 2: 12_SOURCE_PREP/RV063_10K_PAYMENT_CROP.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline and exact fact labels explicitly required by this beat.

SOURCE ROLE:
Attached sources ground the verified numbers/dates/statuses. DEC 17 2023 — MUTUAL TERMINATION; DEC 20 2023 — $1B PAID TO FIGMA.

COMPOSITION:
Create a premium information frame from verified facts. Single red connector; contract paper only, no regulator invoice. One dominant statement plus one clear comparison/timeline/status structure; source excerpts support the information without PowerPoint styling. Turn only the verified source-grounded facts into an elegant cinematic information composition; exact numbers/dates only; never PowerPoint.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate. Do not fall back to a generic dark desk with random papers.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, flag/Capitol symbolism unrelated to the source, unverified numbers, misleading arithmetic, fake $21B total.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions. No editor instructions inside the image.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F084 / B084

**LOCKED HEADLINE:** `THE DEAL DISAPPEARED. THE FEE DIDN'T.`

**TIMING:** 719.220 → 725.420 (6.200 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV025_ADOBE_FIGMA_DEAL_GRAPHIC.png` → Higgsfield media `9ca85935-d9a9-431a-9e5b-9e9de093e54a`
- Image 2: `12_SOURCE_PREP/RV049_S8_2_TERMINATION_FEE_CROP.png` → Higgsfield media `b14e6e93-386d-44fd-8137-2b399880d46c`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B084, ready to place directly into the finished film.

STORY PURPOSE:
The acquisition disappeared. The termination fee did not. And the payment did not come from a regulator's invoice.

LOCKED HEADLINE:
"THE DEAL DISAPPEARED. THE FEE DIDN'T."
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV025_ADOBE_FIGMA_DEAL_GRAPHIC.png
Image 2: 12_SOURCE_PREP/RV049_S8_2_TERMINATION_FEE_CROP.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
image 1 = official Adobe + Figma deal graphic (fading print), unchanged apart from dim desaturated color; image 2 = Merger Agreement Section 8.2 fee excerpt (lit), unchanged — never retype it.

COMPOSITION:
on a dark desk, a desaturated print on the left fades into shadow, barely visible; on the right, a contract excerpt is warm, sharp and lit, with a thin vertical deep-red bracket in its margin. headline zone inside the top 32% of the frame, left 60%. The fading print left-center between 38% and 74% of frame height; the lit excerpt on the right, between 14% and 74%. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Make the authentic interface large and readable; preserve native controls, colors and proportions.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F085 / B085

**LOCKED HEADLINE:** `THE CONTRACT, NOT A REGULATOR`

**TIMING:** 726.300 → 729.080 (2.780 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV062_TERMINATION_AGREEMENT_CROP.png` → Higgsfield media `434ba753-529b-46bc-b1ad-3992af41be27`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B085, ready to place directly into the finished film.

STORY PURPOSE:
It came from a contract the companies had negotiated themselves.

LOCKED HEADLINE:
"THE CONTRACT, NOT A REGULATOR"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV062_TERMINATION_AGREEMENT_CROP.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
image 1 = Mutual Termination Agreement excerpt (liquidated damages / sole remedy); it is the paper, unchanged — never retype or redraw it.

COMPOSITION:
an extreme close-up of one contract excerpt on warm aged paper, very shallow depth of field, a sharp band across the key lines, a thin vertical deep-red bracket in the margin beside them. headline zone inside the top 45% and left 40% of the frame. The excerpt fills the right 60%, between 8% and 76% of frame height. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Make the authentic document the hero at roughly 55–70% of frame; preserve readable wording; at most one deep-red bracket and one restrained warm-yellow highlight.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F087 / B087

**LOCKED HEADLINE:** `THE PURCHASE NEVER HAPPENED`

**TIMING:** 739.440 → 749.260 (9.820 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV025_ADOBE_FIGMA_DEAL_GRAPHIC.png` → Higgsfield media `9ca85935-d9a9-431a-9e5b-9e9de093e54a`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B087, ready to place directly into the finished film.

STORY PURPOSE:
That was the amount associated with the deal Adobe wanted to close. Because the acquisition never closed, Adobe did not pay Figma twenty billion dollars to buy the company.

LOCKED HEADLINE:
"THE PURCHASE NEVER HAPPENED"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV025_ADOBE_FIGMA_DEAL_GRAPHIC.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
image 1 = official Adobe + Figma deal graphic; it is the faded print, unchanged apart from muted desaturated color.

COMPOSITION:
a high-angle view into an empty, clean cardboard archive box on a dark desk; a single faded print lies alone on its bottom. headline zone inside the top 45% and left 38% of the frame. The box center-right, between 18% and 76% of frame height. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Make the authentic interface large and readable; preserve native controls, colors and proportions.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---

## F088 / B088

**LOCKED HEADLINE:** `THE PAYMENT WAS REAL`

**TIMING:** 750.260 → 760.640 (10.380 sec)

**LOCKED REFERENCES — REUSE UNCHANGED:**
- Image 1: `12_SOURCE_PREP/RV063_10K_PAYMENT_CROP.png` → Higgsfield media `ec7d4f0b-ad22-406d-b354-d8c0a83249ef`

### R14 EXECUTION PROMPT

```text
FINAL FRAME ONLY. Create one complete 16:9 WHAT IT COST documentary image for Beat B088, ready to place directly into the finished film.

STORY PURPOSE:
One billion dollars was the actual termination payment. Adobe paid it. Figma received it. Adobe later recorded the one-billion-dollar fee in operating expenses.

LOCKED HEADLINE:
"THE PAYMENT WAS REAL"
Render it directly in the image with exact spelling and punctuation, distressed condensed ivory/off-white capitals, one or two lines where practical, plus one short deep-red underline. No secondary generated copy.

MANDATORY SOURCES:
Image 1: 12_SOURCE_PREP/RV063_10K_PAYMENT_CROP.png

SOURCE FIDELITY:
Use every attached image as the actual factual visual content. Preserve authentic document wording, UI controls, logos, faces, people, architecture and source composition. Never redraw, paraphrase, replace, synthesize or invent a substitute source. Source-native text may remain readable; generated text is limited to the locked headline.

SOURCE ROLE:
none — the frame contains no documents, photos, screenshots or logos.

COMPOSITION:
one thick, heavy blank ivory card with a deep-red painted edge lies on a dark desk in hard directional light, casting a crisp solid shadow. headline zone inside the top 45% and left 40% of the frame. The card center-right, between 30% and 72% of frame height, large, with generous darkness around. The bottom 22% is empty dark charcoal. Treat that layout as a guide for hierarchy, not as a rigid graphic grid. Keep the evidence large, legible and visually dominant. Headline and evidence must feel designed together as one cinematic shot. Establish one dominant factual source and subordinate support; communicate the beat in under one second.

STYLE:
Approved R9 evidence-editorial language: deep charcoal-black textured environment, warm aged ivory paper/matte surfaces, low-key directional warm key light, subtle cool shadow falloff, fine cinematic grain, restrained deep-red accents, elegant information-rich business documentary photography. The source is the hero; decoration is subordinate.

CAPTION SAFE:
Keep the bottom 15% visually calm and free of headline, faces, key evidence and tiny text.

ABSOLUTELY AVOID:
fake legal text, fake UI, invented logos, substituted source images, extra people, warped faces, collage/contact sheet/storyboard, random giant arrows/circles/icons, neon/glossy ad styling, generic desk clutter, black subtitle boxes, courtroom/gavel/Lady Justice clichés, unrelated flag/Capitol symbolism.

OUTPUT:
One finished cinematic frame only. No backplate. No placeholder. No alternate versions.

R10 CANON STYLE OVERRIDE — MANDATORY:
Match the approved canon grammar of F039 first and F015 second for hierarchy, typography feel, charcoal / warm-ivory / deep-red palette, evidence scale, tactile materials, warm directional lighting, subtle cool shadows, fine grain and publication-level polish. Canon frames are visual-style references only; never borrow their factual content.
Source fidelity is absolute. Every attached source must remain authentic and visibly recognizable. Do not invent or retype document body text, UI controls, logos, faces, people, architecture, dates or numbers.
The frame must not look like a collage, contact sheet, slideshow, generic dark desk, legal-thriller cliché or glossy ad. No orange collage blocks. No black caption box.
Keep the bottom 15% of the full 16:9 frame calm, dark and free of headline, faces, key evidence, key numbers/dates, tiny UI, evidence highlights and important object edges.
Deliver exactly one finished cinematic 16:9 frame.

R14 RELEASE-RESOLUTION REGENERATION — HIGHEST PRIORITY:
This slot previously passed QC but only a 960x540 preview survives. Regenerate the same beat as a fresh finished frame: same locked headline, same attached sources, same beat meaning, same canon style.
Proven caption-safe layout from R12/R13: keep the headline inside the top 8%-34% of frame height; every source board, label, face, key number and bright paper edge must end ABOVE 77% of frame height.
The bottom 23% of the frame must be uninterrupted deep charcoal with only subtle texture/light falloff.

HARD PASS GATE:
The bottom 15% must contain only dark, low-detail background. If anything important enters the bottom 15%, the frame is a failure.
```

---
