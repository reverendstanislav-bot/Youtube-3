# VIDEO 002 — Chat-generated R8 frame archive

Date: 2026-09-27

This folder freezes the current ChatGPT-generated VIDEO 002 R8 frame work so it is no longer dependent on chat history.

## Contents
- `CANDIDATES/`: 30 slot-addressed frames: G001–G020 and G026–G035.
- `REJECTED_ATTEMPTS/`: 11 superseded / wrong-slot generations kept for provenance and to prevent accidental reuse.
- `FRAME_QC.csv`: quick frame-level status.

Older generated test material already committed earlier remains in:
- `TEMP_GENERATED_QC/` — 14 early PNG tests.
- `TEMP_GENERATED_QC_R3_TEST/` — 10 R3 micro-preview tests.

## Quick QC
- **29 / 30 current slot-addressed frames:** VISUAL_PASS_SOURCE_HOLD.
- **1 / 30 current slot-addressed frames:** REJECT — G015 headline/content mismatch.
- **11 / 11 side attempts:** REJECT / superseded.
- **Canonical slots G021–G025 are still missing.** Only wrong-slot attempts exist for those five.
- Therefore this archive is **not a 35/35 canonical asset lock**.

### Why SOURCE_HOLD
The accepted visual language is strong and consistent: charcoal/aged-paper/ivory/deep-red, informative source-led compositions, readable baked headline, and calm lower caption zone. However, R8's production contract requires authentic bound source material to remain exact. Several generated document/UI/photo surfaces visibly look synthesized or re-typeset. Those frames must not be marked final evidence PASS until exact source fidelity is checked against `12A_R2_REFERENCE_BINDINGS.csv` / prepared source files.

## Production use
Do not auto-use REJECT files. For current candidates, treat `VISUAL_PASS_SOURCE_HOLD` as a visual/layout approval only, not a legal/source-integrity lock.

The JPEG archive preserves the native generated dimensions and is a high-quality Git snapshot. It is an archival/QC copy of the chat generations.
