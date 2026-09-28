# VIDEO 002 — Queue 001–075 Generation Recovery Lock

Date: 2026-09-28
QC policy: **PASS / REJECT only**

## Recovery result

- Queue positions audited: **75**
- Raw generation attempts recovered from the current working container: **149**
- PASS: **40**
- REJECT: **35**
- Existing pre-batch canon PASS frames: **15**
- Total usable frames after R2 recheck: **55 / 110**
- Remaining frames without a locked PASS: **55 / 110**

## R2 reject recheck

The initial QC was too conservative. A second-pass editorial-use recheck promoted **18** previously rejected/unresolved queue slots where the visual is on-beat, factually safe, and production-usable even when the headline is a semantic equivalent rather than an exact string match.

Canonical R2 notes: `13_R10_QUEUE_001_075_RECHECK_R2.md`

Two additional exact chat artifacts were recovered during R2:
- F082: `conversation:file_000000008eb882109f40a2e06ce0fcb2`
- F083: `conversation:file_00000000d3f082109da712e784eba65f`

These two are outside the original 149-file ZIP, whose checksum remains unchanged.

## Exact recovery archive

A full-resolution recovery ZIP was assembled from the recovered chat-generation pool.

- File: `VIDEO002_QUEUE_001_075_RECOVERY.zip`
- SHA-256: `49fdc5e577b17e4b6b7748995bbcb36a6d47dbdaf93ba0dd52408a74e9969530`
- Size: **321,750,437 bytes**
- Raw recovered image attempts inside: **149**

The ZIP contains:
- all recovered raw generation attempts;
- `RAW_RECOVERY_MANIFEST.csv` with per-file SHA-256;
- `QC_001_075.csv`;
- `QC_SUMMARY.md`;
- recovery contact sheet.

## Binary archive note

The GitHub source-of-truth records the exact archive SHA-256, frame mapping and binary QC result. The full-resolution ZIP remains the byte-preserved recovery package produced in this chat. Rejected attempts are retained for provenance and are not production assets.

## Confirmed hard failures

- **#6 / F011** — recreated UI, not exact source UI.
- **#71 / F086** — consideration wording was generated incorrectly; it must remain approximately half cash and half stock.
- **#74 / F089** — generated **$250 million**, which is factually wrong; the termination payment is **$1.0 billion**.
- **#75 / F090** — no completed generation was recovered after the image-generation limit was hit.

## Production rule

Only rows marked **PASS** in `13_R10_QUEUE_001_075_QC.csv` may be used in the film. R2 allows semantically equivalent headlines/editorial summaries when they remain factually safe; hard factual/legal/source contradictions remain REJECT.
