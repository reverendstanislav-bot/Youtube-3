# Stage 12F — GPT Image Generation Rules

Status: **PROMPT PACK LOCKED / NO GENERATION AUTHORIZED**

## Cost lock
- Route: **GPT image generation via Higgsfield**
- Cost assumption locked by owner: **0.5 credits per image**
- Production beats: **115**
- One first-pass image per beat: **57.5 credits**
- This Stage 12F commit authorizes **0 credits** and submits **0 jobs**.

## Style-reference IDs
The five approved Stage 12D proof frames from the owner's local review pack `STAGE12D_PROOF_FRAMES_PACK.zip` are used as style-only references:
- **SR-A** — `forensic_evidence_pig_mask_and_book.png` — evidence / authentic-case treatment
- **SR-B** — `ebay_executive_legal_status_dossier.png` — executive/legal-status dossier
- **SR-C** — `wide_cinematic_documentary_style_graphic_still_da.png` — court-document treatment
- **SR-D** — `a_wide_cinematic_infographic_poster_dark_gritty.png` — money/settlement treatment
- **SR-E** — `a_cinematic_infographic_style_map_and_timeline_da.png` — map/timeline treatment

Style references control material language, composition density, color and typography. They never supply factual content for another beat.

## Universal image rules
1. 1920×1080 / 16:9.
2. Bottom 20% = Y 864–1080 must stay free for captions.
3. Use source/reference assets selected in the row.
4. Source document text is never invented. If a real source crop is needed, rasterize/use the actual crop.
5. Real-person references are editorial inserts only. Do not synthesize a new likeness, pose, expression or event.
6. Exact factual text is limited to `display_text_exact`; do not let the model improvise extra numbers, dates, names, quotes or legal conclusions.
7. Palette: #0B0B0B / #1F1F1F / #3A3A3A / #EDEDED / #D32222; #B69B68 rare for money.
8. No horror, gore emphasis, fake CCTV, HUD, neon, glossy 3D, gavels, scales, handcuffs, fake seals or cheap crime-poster treatment.
9. Frame should feel assembled from evidence, not like a PowerPoint/dashboard.
10. For Shorts beats, the 16:9 image is not automatically sufficient; the row preserves the Stage 12E 9:16 strategy for later alternate composition.

## Reference-preparation rule
- PNG/JPG/WEBP: attach directly.
- PDF: rasterize the relevant page/crop first.
- HTML: use as verified wording/context; rasterize only when rights status permits, otherwise recreate only the verified labels/facts.
- ZIP map/data: create a clean map base first; do not upload raw ZIP as an image reference.

## Spend gate
No row in this pack is permission to generate.
Generation starts only after an explicit owner approval specifying batch/job count and credit total.


## R2 document/evidence rendering lock

Owner-approved after the five-image Higgsfield test.

For document/evidence-heavy scenes:
- **never generate a full dense legal document, filing, screenshot, chat log, web page or evidence sheet**;
- never use invented small-print paragraphs as texture;
- never create fake docket numbers, signatures, seals, metadata or stamps;
- use at most **one short excerpt / one quote / one highlighted line / one compact evidence tile**;
- real source material may be a compact visual anchor, but the frame's strength must come from composition, atmosphere, hierarchy, paper treatment, lighting and negative space;
- unused paper/document areas must stay clean, cropped, obscured or texture-only;
- if the real source must be readable pixel-for-pixel, composite the authentic crop after generation rather than asking the model to redraw it.

This lock applies to all future prompts, with extra scrutiny for T03, T07 and document-heavy T02/T06/T01 beats.
