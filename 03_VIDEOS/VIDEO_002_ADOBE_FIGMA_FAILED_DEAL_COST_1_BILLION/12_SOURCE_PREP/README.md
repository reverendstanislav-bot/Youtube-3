# VIDEO 002 — 12_SOURCE_PREP resolver

Date: 2026-09-29

This directory is the canonical resolver layer for the physical reference inputs required by the remaining R10 generation queue.

## Lock

- Canonical reference paths: **50 / 50 resolved**
- Distinct persisted Higgsfield media objects: **44**
- Logical aliases sharing the same prepared binary: **6**
- Higgsfield upload verification: **44 / 44 UPLOADED**
- Remaining F-slots with all mandatory attachments resolved: **55 / 55**
- Paid image generations executed by this prep step: **0**
- Credits spent by this prep step: **0**

The image binaries are persisted in the Higgsfield media library because that is the execution backend used for the later reference-based image jobs. Git stores the stable path → media UUID resolver in `HIGGSFIELD_MEDIA_MAP.csv`.

Do not regenerate or re-upload these references unless a reference itself fails QC.

## Controlled source substitutions

Three legacy source endpoints could not be retrieved directly in the source-prep runtime, so source-faithful official replacements were used:

- `RV044_ADOBE_XD_WORKFLOW_UI.png`: official Adobe Blog XD UI image.
- `RV045_ADOBE_XD_PROTOTYPING_UI.png`: official Adobe Blog XD prototype UI image.
- `RV059_EC_STATEMENT_OF_OBJECTIONS_CROP.png`: official European Commission Presscorner Adobe/Figma Statement of Objections PDF.

These are not synthetic substitutes and do not alter the beat facts.

## Generation gate

The remaining 55 frames are now technically attachment-ready. Paid generation remains blocked until explicit owner approval for the base spend of **27.5 credits (55 × 0.5)**.
