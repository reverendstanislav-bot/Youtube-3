# VIDEO 002 — Chat-generated R8 frame archive

Date: 2026-09-27

This folder freezes the current ChatGPT-generated VIDEO 002 R8 work so it no longer depends on chat history.

## Contents
- `CANDIDATES/`: 30 slot-addressed recovered frames: G001–G020 and G026–G035.
- `REJECTED_ATTEMPTS/`: 11 known wrong-slot / superseded generations retained for provenance.
- `FRAME_QC.csv`: strict short QC against the locked R8 beat/source expectations.
- Older tests remain in `TEMP_GENERATED_QC/` and `TEMP_GENERATED_QC_R3_TEST/`.

## Current QC summary
- **Binary QC only: PASS or REJECT. No HOLD / EDIT_FIX state exists.**
- **5 PASS**: G018, G020, G031, G033, G034.
- **25 current-candidate REJECT**: all other archived candidates among G001–G020 and G026–G035.
  - 16 of those are rejected because exact bound source fidelity is not verified.
  - 9 are rejected for wrong source / wrong beat / source fidelity / headline mismatch.
- **G021–G025 are REJECT / NOT READY**: only wrong-slot attempts exist; no canonical frame is available.
- Therefore across **G001–G035: 5 PASS / 30 REJECT**.
- **11 / 11 side attempts are rejected/superseded.**

This folder is an archive + binary QC checkpoint, not a final 35/35 asset lock.

The approved look remains `12A_R8_APPROVED_FRAME_STYLE_LOCK.md`. Final promotion requires the locked beat, headline and bound source to match.
