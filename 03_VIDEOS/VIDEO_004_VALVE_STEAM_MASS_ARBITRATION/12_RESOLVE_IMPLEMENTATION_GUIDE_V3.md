# VIDEO 004 — Resolve V3 Composition & Source Execution Guide

Status: **FRAME-ACCURATE EDITOR BLUEPRINT PASS / FINAL PICTURE & AUDITORY QC HOLD** (2026-10-10). Authoritative edit rules: `EDITING_CANON.md` owner-locked 2026-10-09. No paid generation or production of new footage authorized.

## What exists, concretely

- `12_RESOLVE_COMPOSITIONS_V3.csv`: **175/175** picture states, exact global frame in/out at **1920×1080, 25fps**, and independent composition/layer plans; all video states cover **0–20,700 frames** without gaps. 0–20,200 frames contain **808s narration**; 20,200–20,700 is the planned **20s YouTube endscreen**, which does not exist in the audio WAV.
- `12_SOURCE_DOCUMENT_GEOMETRY.json`: PDFs really downloaded by the GitHub Actions verifier, PDF hash, exact phrase match, **page index and source-native PDF-point rectangle**.
- `12_RESOLVE_PDF_CROPS_V3.csv`: **56/56** PDF-backed shot states have a deterministic **PDF crop rectangle**, **1920×1080 destination bounding box**, exact destination marker rectangle in pixels and normalized coordinates. These are calculated from actual PDF geometry; no dummy coordinates.
- `12_RESOLVE_MARKER_WORD_SYNC_V3.csv`: **19 source-native highlight candidates**, of which **4** now have provisional matched speech words/time and **15 are explicitly disabled** until genuine audio listening. Original V3 marker keyframe proposals are overridden by this safety gate; the composition table now applies it.
- Source-layer job `.github/workflows/video004_source_layers.yml` produces an importable, authentic unbaked layer pack, with document pixel layers and separate transparent highlight alpha masks. **Successful artifact delivery must be verified independently before claiming the layers are downloaded.**

## DaVinci Resolve timeline / Fusion layering contract

Edit in DaVinci Resolve; FFmpeg may be used only for technical extraction/QC. Project: **1920×1080, 25.000fps**, progressive, color managed consistently with existing WHAT IT COST project profile. Lower **162px** (y≥918) reserved for narration captions. Source citations, labels and the important evidence appear above that area. Captions are not pre-burned into generated frames.

Recommended reusable Fusion node order (native controls, no look-changing ML substitution):

`MediaIn(SourceCrop)` → `Transform(SourceFocus)` → `Merge(EvidenceForeground)` → `Merge(StatementOrCounterposition)` → `Merge(SourceTag)` → optional `Merge(HighlightedSourceLine, ApplyMode=Multiply)` → `MediaOut`.

For document states, the authentic `_DOCUMENT.png` is a transparent canvas-sized evidence layer containing a verified court/AAA crop, and the matching `_MARKER_ALPHA.png` is a **separate** transparent layer. Never bake marker pixels into the document. Set destination canvas to its original 1920×1080, lock marker and document transform hierarchy to the same page coordinate space, then animate only the marker's horizontal reveal mask as a child of the source transform. Source black glyphs must remain readable.

**No automatic camera motion:** a documented native line, number or specific case event is the only acceptable motion target. If exact audio timing or source crop is uncertain, hold the frame. Avoid background replacement, large title arrival and card movement on the same frame.

## Locked treatment decisions by chapter

| Chapter | Visual argument / layer choreography |
|---|---|
| S01 | Steam access concern and Valve's position coexist with explicit attribution; old/new contracts shown as distinct source records; reveal the claimant→defendant reversal with stable opposing labels. |
| S02 | 2012 arbitration mechanism vs actual 2023 Original SSA described in the 2026 order; use the **2020 archival URL as context, never as counterfeit 2023 agreement**. Publisher proceedings never merge into the user arbitration lane. |
| S03 | Dated claimant counts as separate numbers; no animation implying a precise count from an arbitrary number of icons. |
| S04 | Alleged **$20M stays next to UNVERIFIED**; real AAA fee schedule shown with fee category context; do not animate an invented bill or a payment total. |
| S05 | Four-claimant divergence and distinct resulting litigation; judge's 2026 order summarises the 2024 events, not a purported scan of an unavailable Dasteel ruling. |
| S06 | Original vs updated agreement comparison, September 2024 rewrite; updated forum text is not treated as proven retroactively enforceable. |
| S07 | Classify claimed account access risk and Valve's licence response separately, no game deletion image or fake Steam modal. |
| S08 | AAA September 27 request / October 7 response as dated sequence from order; refusal to administratively close is not a merits adjudication. |
| S09 | October 2024 filing struck for procedural error, later civil complaint distinct; procedural setback is not the substantive antitrust verdict. |
| S10 | Two-contract procedural question and disputed active-demand count; withhold court result until S11. |
| S11 | Source Dkt.169 May 27, 2026: DENIED is coupled to **PRELIMINARY / AS APPLIED TO THESE DEFENDANTS**. No sweeping final antitrust outcome language. |
| S12 | Source Dkt.192 July 30, 2026: CERTIFIED interlocutory question / DISTRICT CASE STAYED; not an automatic appellate reversal. |
| S13 | Docket `26-6269` shown with retrieval date and **PUBLIC SNAPSHOT — NOT A CURRENT PACER CERTIFICATION**; official Stage16 refresh still required. |

## Keyframe discipline — per-shot values live in V3 CSV

All keyframe offsets in `12_RESOLVE_COMPOSITIONS_V3.csv` are **local integer frames relative to the shot's global start**. Example: if start_frame=1279, local F12 means timeline frame1291 (51.64 seconds). Use Resolve **ease-in/out** with continuity for source focus; never use linear random motion or default movement on every shot.

- Short duration / dense text: zero motion, hard idea-motivated cut.
- Native evidence establish: source page arrives without a pop; source label gets separate settling timing; meaningful reading hold follows.
- Named source detail: optional focus up to about **1.035×** only toward the verified citation; the heading stays fixed; read hold begins after focus arrives.
- Compare: first source/position held; second counter-position appears separately, without losing the first or compressing important caveats.
- Mechanism: one labelled relationship line appears after both entities are readable. No sweeping wipes.
- Verified marker: start/end frames from `12_RESOLVE_MARKER_WORD_SYNC_V3.csv` ONLY, if the status is ASR anchored. **These four timings remain provisional until actual audible confirmation.** The other 15 markers are disabled, regardless of how attractive the PDF rectangle looks.

## Sample fully traceable documentary crop

A real S004 / Dkt.169 PDF line ("retroactive forum") on printed page 2 has PDF native rect **[152.16, 155.99, 248.99, 174.08] pt** from a source file whose SHA256 is recorded in the geometry report. For shot SH-011 the planned page-crop is **[0, 1.876, 612, 381.316] pt**, displayed at **[245, 105, 1250, 775] pixels** in the 1920×1080 canvas; its fitted source marker rectangle computes to **[555.784, 419.776, 197.774, 36.949] px**. This is an exact computational mapping in the planned crop coordinate system, **not proof the source screenshot was visually approved at edit quality**. A subsequent local preview must confirm the row is actually legible and the intended phrase is in view.

## Real source / rights gate

Actual PDF byte-and-text geometry verified for `S004` (32 pages), `S005` (6), `S006` (4), `S007` (18). Their SHA256 values are written in `12_SOURCE_DOCUMENT_GEOMETRY.json`. Original source URLs are in `SOURCE_INDEX.csv`.

Other sources are HTML/news/docket and are **link/text-checked** but are not yet screenshot-geometry locked: `S001/S002/S003/S008/S009`. These require genuine browser captures or editor-native evidence interpretations—not counterfeit interface or legal pages. `S009` has minimal webpage content; it is context-only and must not be used to assert unavailable allegations.

No sourced image or document automatically receives copyright/rights clearance through web readability. Check license or legal editorial-use basis before distribution.

## Acceptance checklist before Stage13 or picture assembly

1. Verify document-layer artifact (SHA, unique crop count, all shot mappings and decoded PNG transparency). Compare representative PNG crops and marker positions against original PDF pages.
2. View sections S01, S04, S11, S12 as real 25fps sample transitions in DaVinci; check separate layer choreography and exact source line, no black bars/cards, no subtitle occlusion.
3. Verify each of **four** Shorts: SH01, SH02, SH04, SH08. They have ASR provisional boundaries, not final listening approval.
4. Full 808s narration listening, A/B/C joins, eight ASR flags and cut-edge auditions remain **Stage10/11 HOLD**; nothing in Stage12 overrides this.
5. Independent QC for visual diversity/reading-time/attribution and exact audio-word fit. No content replacements outside requested scope.
6. All paid image counts remain **undetermined / 0 authorized**. Current 175 states are editable composition states, not 175 images or billable prompts.

## Verdict

**PASS:** source-linked, frame-continuous 175-shot editor blueprint; 56 source-crop/marker geometries verified numerically from actual PDFs; 4/19 provisional word-triggered marker candidates.

**HOLD:** real picture preview in Resolve; asset-license and screenshot QC; final marker listening; full audio & four Shorts auditions; all non-native source and image generation preflight. Stage12 planning is advanced but **not FINAL ASSET LOCK**.

## Full-width source-crop repair (2026-10-10)
The initial narrow cropped PDF layer cut off the left/right portions of surrounding document lines. This version uses source **full-page width** in the crop and retains vertical evidence focus, with source-native pixel marker coordinates recalculated. Importable source layers remain genuine PDF pixels; the alpha-mask layer is independent. Soft vertical edge feathering in the latest source-layer renderer avoids half-glyphs exactly at crop boundaries without adding black bands or changing the central cited text. QC evidence from the final rebuilt artifact, not the earlier 11-crop run, must determine final visual PASS.
