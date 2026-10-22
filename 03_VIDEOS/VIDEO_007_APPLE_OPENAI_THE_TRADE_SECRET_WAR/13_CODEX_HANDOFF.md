# CODEX HANDOFF — VIDEO007 STAGE13 REMAINING PRODUCTION WORK (2026-10-22)

## Critical current truth
- Locked Harrison master: 972.36s, 25fps 24,309 frames. Keep original audio, Stage07/08 script, Stage11 timings and exactly FOUR Shorts (complete <=35 seconds) unchanged.
- Stage12 has 239 planned picture shots, 60 narration scenes.
- Stage13 committed 143 editable SVG **SOURCE/DRAFT** files. **Six source-specific bespoke layouts** (`VP002,VP005,VP119,VP170,VP207,VP220`) have NOT been rendered and independently approved. **137 generic template SVGs FAIL editorial premium-film design and require replacement**, not a blind 143-image batch import.
- All 96 non-GFX shots are still **ORIGINAL MEDIA NOT ACQUIRED**. As of latest QC: **0/239 final visual assets approved**.
- `manifest.yaml`, `13_ASSET_MANIFEST.csv`, `13_STAGE_QC.md` control truth. Do not flip PASS without real visual/audio/media evidence.

## Tasks — do not advance beyond Stage13
1. **Acquire original source bytes**, preferably primary court PDFs via documented direct URLs in `SOURCE_INDEX.csv`. Confirm full content and rights for Apple complaint ECF1, OpenAI ECF59/97/143/176, original ECF175 order, Apple ECF177. For Oct16 ECF188/189: court docket confirms disposition, but original signed-order PDFs were not read; do not generate imaginary pages/quotes. Do not use paid PACER unless explicitly authorized.
2. For each PDF segment, use native page crop with its original header/paragraph and store one-based page, bounding rectangle, SHA256, source URL, page image decode and editorial copyright rationale. `13_PRIMARY_DOCUMENT_EXCERPT_LOCK.csv` names high-priority verified exact targets. No document reconstruction passed as actual filing.
3. Acquire and **visually review actual video files** for the 8 Pexels source URLs in `12_VISUAL_SOURCE_RIGHTS.csv`. Original source URL, author, platform license, file hash, 16:9 compatibility, depicted third-party marks/releases, no misleading company attribution. V7 is 9:16 and cannot be treated as native landscape film. Avoid repetition of generic stock filler and source it only when story relevant. Download Commons Apple Park M1 original and document Dicklyon CC BY-SA 4.0 attribution and reuse obligations.
4. **Render six bespoke first** with `python tools/render_video007_gfx.py --root . --dest /.../editor_png` (or targeted Inkscape) and perform image-by-image QC in 1920x1080. Check legibility on phone, margins, visual rhythm, unverified numbers, allegation versus finding language, source labels and no readout of raw instructions. Each needs owner creative signoff; retain both SVG source and PNG export/hash.
5. **Redesign 137 generic drafts individually** according to their `12_DENSE_SHOT_MAP.csv` and native speech cue. Do not generate 137 cards of the same template; create appropriate real vector diagrams, chronology or explanatory graphics when each is genuinely needed. Use `00_FOUNDATION/EDITING_CANON.md`, `VISUAL_LOCK.md`, `01_CHANNEL/VISUAL_BIBLE.md`; no orange collage blocks, neon, fake legal documents or generic law stock.
6. Record every accepted asset in `13_ASSET_MANIFEST.csv` with file path, SHA256, rights determination, exact assigned shot/time window, original frame resolution, QC reviewer status, native source ID and provenance. Raw video/WAV/PDF media should be stored in a properly versioned release/artifact archive, not bloated into Git.
7. Perform **independent visual legal QC**: ECF1 Apple allegations vs ECF176 OpenAI allegations, ECF177 Apple's own search assertion, ECF175 limited discovery and ECF188 PI moot ≠ merits dismissal or victory. Full visual on-screen text must not amplify script allegations. Four Shorts need readable 9:16 framing.
8. Preserve `A02-P01` phoneme review hold (82.5% ASR); Stage16 docket freshness and Stage17 title remain independent later gates. No TTS/audio regeneration, no background image/video spending, no model/paid quota consumption without explicit owner approval.
9. Log exact failed assets and repairs; source-native screenshots, rights notes and rendered contact sheet plus representative full-resolution frames. Stage13 PASS only if actual files and approval evidence exist.

## Already verified external sources
- ECF1 original CourtListener 41-page PDF: `https://storage.courtlistener.com/recap/gov.uscourts.cand.474095/gov.uscourts.cand.474095.1.0.pdf`. “Actual parts” appears on original pp4 and 22; Apple allegation, not confirmed handoff.
- ECF176 4-page PDF: `https://storage.courtlistener.com/recap/gov.uscourts.cand.474095/gov.uscourts.cand.474095.176.0.pdf`; p2 describes claimed 100+ OpenAI-origin files to **personal** accounts.
- ECF177 original 4-page PDF via 9to5Mac mirror: `https://9to5mac.com/wp-content/uploads/sites/6/2026/10/gov.uscourts.cand_.474095.177.0.pdf`; p2 Apple's Oct9/Oct12 response claim.
- ECF175 Oct13 court order Justia native text: `https://law.justia.com/cases/federal/district-courts/california/candce/5%3A2026cv07078/474095/175/`.
- 8 individual Pexels clip URLs catalogued in `12_VISUAL_SOURCE_RIGHTS.csv`; commercial platform license summary `https://www.pexels.com/license/` (third-party rights still apply).
- Apple Park M1: `https://commons.wikimedia.org/wiki/File:Apple_Park_dusk_aerial.jpg`, Dicklyon, CC BY-SA 4.0.

## Acceptance
- No invented files, downloaded material, checked audio, rights passes or silent upstream changes.
- Finish Stage13 only. Leave next stage untouched.
