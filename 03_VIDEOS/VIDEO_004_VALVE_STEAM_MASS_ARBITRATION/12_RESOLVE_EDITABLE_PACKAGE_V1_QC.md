# VIDEO004 — Resolve editable pack V1: delivery and QA

Date: 2026-10-10. Status: STATIC BUILD PASS / DA VINCI RUNTIME AND LISTENING QC HOLD.

## Downloaded deliverable
- GitHub Actions run https://github.com/reverendstanislav-bot/Youtube-3/actions/runs/38058941643
- Artifact ID 11671589261; VIDEO004_RESOLVE_EDITABLE_COMPS_V1.
- Downloaded ZIP SHA256: 30936da1746c560a5a929228acd632291b10d8c7189e88da36abae2563fffd42.
- 194 entries: 175 Fusion .setting files, 15 PNG (11 real PDF crop images, 4 alpha masks, 1 neutral canvas), timeline importer, manifest and build receipt.
- All 175 settings statically checked: brace balance, declared node references and source-to-shot frame continuity; 0 unresolved SourceOp links.
- Timeline frame 0–20700 inclusive boundary / 25fps; narration 808s, planned end screen 20s. No generated voice/footage/images or paid credits.
- Source-derived overlays have Blend=0 by default pending human listening; four active Shorts SH01, SH02, SH04 and SH08 only.
- Palette/typography follows 00_FOUNDATION/VISUAL_LOCK.md: charcoal, paper white and restrained signal red; Bebas Neue and Inter; exact font appearance depends on installed fonts.

## Automation and important limitations
- Script 12_IMPORT_EDITABLE_RESOLVE_PROJECT.py and bundled IMPORT_IN_DAVINCI_RESOLVE.py build a new named review project, first --canary 8, then --all after checking the canary. They verify expected start/end and master SHA256.
- Resolve is not installed in execution environment. No project .drp was actually exported, and Fusion tool import/runtime was not tested in the application. The 175 compositions are *import candidates*, not finished motion/edit approval.
- A canvas still underlying each Fusion comp may exhibit version-specific duration behavior. If the canary fails a clip frame check, stop. Do not call that a complete edit.
- HTML-based Steam and appellate docket visuals and additional source/rights checks are pending. Static source layers are genuine verified document pixels, not court-document reconstructions.

## Audio Stage10/11
- The 808s Harrison master SHA256 8c11be2619a6a84b7e1a6cbe0cb8c708d72dff556d1d737dd46f596ea21f65d7 was programmatically inspected.
- 10_11_TARGETED_AUDIO_BOUNDARY_QC.md has measured A/B and B/C joins and four Shorts in/out sample behavior.
- VIDEO004_STAGE10_11_AUDITORY_REVIEW.zip contains 14 WAV-derived MP3 excerpts (8 ASR flags, 2 joins, 4 full Shorts extracts). This does not constitute genuine listening. Audio master and Shorts cut locks remain FALSE.

## Final gates
1. Run the eight-shot canary in the actual Resolve host and inspect Fusion errors, keyframes, no black masks, typography, exact source lines and five real motion transitions.
2. Expand to all 175 only on canary PASS, validate actual timeline positions and true 25fps real-time playback.
3. Full audio listening of 808s and 14 priority excerpts; correct syllable cut edges; lock four Shorts only after spoken review.
4. Final legal refresh, authentic external UI/source captures, ownership/right-of-use checks and complete editor render QC.

VERDICT: EDITABLE PACK STATIC PASS. Actual DaVinci import, render, spoken auditory QC and publication readiness NOT VERIFIED.