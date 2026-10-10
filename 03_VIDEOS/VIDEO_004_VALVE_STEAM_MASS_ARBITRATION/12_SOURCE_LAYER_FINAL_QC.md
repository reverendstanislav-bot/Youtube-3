# VIDEO004 — Stage12 V3 Source-Layer Artifact QC

Date: 2026-10-10. Status: **SOURCE LAYER ARTIFACT TECHNICAL PASS / FULL FILM VISUAL QC NOT RUN**.

## Canonical delivered artifact

GitHub Actions run: https://github.com/reverendstanislav-bot/Youtube-3/actions/runs/38057742171

Artifact ID **11671183129**, name `VIDEO004_STAGE12_VERIFIED_DOCUMENT_LAYERS_V3`. Validated locally from downloaded ZIP `VIDEO004_STAGE12_VERIFIED_SOURCE_LAYERS_FINAL.zip`:

- ZIP SHA256: **843ec588c1db1b4365d3d2316ee6572f1b2fe609148fa89883333f1205e0cb12**.
- 23 ZIP entries: **22 PNG (1920×1080 RGBA)** + source-to-shot JSON manifest.
- **11 distinct document source crops**, exactly mapped to **56 source-backed shot states**.
- Source mix: Dkt.169 `S004` = 9 distinct crops; Dkt.192 `S005` = 1; AAA fee schedule `S006` = 1. `S007` PDF was verified but is not selected in this deliverable.
- Four mask animations enabled in manifest: **SH-072, SH-137, SH-144, SH-155**. These have word-level ASR candidate timing **not final auditory approval**.
- The other 15 historical marker candidates are gated DISABLED in `12_RESOLVE_MARKER_WORD_SYNC_V3.csv`.
- All 22 PNGs decoded; no empty alpha masks; all 11 document PNG SHA256s matched the manifest; no dimension exceptions.
- One representative Dkt.169 page-4 crop was visually reviewed after a full-PDF-width recrop and feathered vertical boundaries. No horizontal partial-line cuts in this reviewed sample. This is not an 11/11 full editorial visual review.
- Main evidence rectangle x245, y105, w1250, h775 stays above y918 caption-safe baseline. Marker overlays remain separate from source pixels.
- The document pixels are derived from downloaded original PDFs with separately recorded original SHA256 receipts (`12_SOURCE_DOCUMENT_GEOMETRY.json`).

## Layer semantics

`*_DOCUMENT.png`: genuine rasterized PDF crop in a 1920×1080 transparent-canvas layer. Use as primary evidence, not an artificially generated court filing.

`*_MARKER_ALPHA.png`: a transparent, owner-style subdued warm-yellow candidate marker mask in original 1920×1080 source-local coordinates; **only apply where the manifest says `marker_allowed=true`** and in a separate Resolve/Fusion layer. It is not baked into the document image. Human hearing and source line alignment are still mandatory before render PASS.

`12_LAYER_ASSET_MANIFEST.json`: maps all56 shots to content-addressed source files and to the four active marker cues.

## Unfinished gates

- 175 states in `12_RESOLVE_COMPOSITIONS_V3.csv` are an **editing blueprint**, not 175 exported picture assets. Non-PDF authentic screenshots for Steam / public appellate docket and editor-native diagrams still need source pixel/rights QC and real Resolve layer creation.
- Four S008/docket-related document states `SH-166…SH-169` are not matched to original PDF bboxes; use dated public source capture only, without making a false court PDF.
- Four active mask cues use ASR word start, not independently verified listening; 15 uncertain cues disabled. No automatic animation of them.
- Full narration and four Shorts auditory cut-edge checks remain open under Stage10/11. This Stage12 package does **not** override their LOCK=false.
- No final DaVinci .drp, no rendered full film, no Shorts video export, no paid image/video generation, no Stage13 PASS and no publication approval.

**Verdict:** PASS for delivered source integrity, mapping, 25fps geometry and PNG technical correctness. HOLD for every creative/renders/auditory/rights gate not explicitly completed.
