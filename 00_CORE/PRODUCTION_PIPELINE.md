# Production Pipeline — 00 → 19

00 TOPIC QUALIFICATION
01 EVIDENCE RESEARCH
02 CASE / STORY MAP
03 SCRIPT V1
04 FACT + LEGAL CLAIM REVIEW
05 SCRIPT REVISION
06 YOUTUBE PERFORMANCE REVIEW
07 FINAL SCRIPT LOCK
08 VOICE SCRIPT
09 VOICE QA + LOCK
10 AUDIO MASTER
11 TRANSCRIPT + VISUAL TIMELINE
12 VISUAL SOURCE / GENERATION PLAN
13 VISUAL ASSET QC
14 GRAPHICS / DOCUMENTS / MUSIC / SFX PLAN
15 ASSEMBLY / EDIT
16 FINAL FACT + LEGAL REFRESH + RIGHTS REVIEW
17 TITLE + THUMBNAIL PACKAGING
18 UPLOAD / PREPUBLICATION PACKAGE
19 POST-PUBLISH ANALYTICS

## Why Stage 16 exists
Court cases, settlements, appeals, dismissals, company statements and regulatory events can change while a video is in production. Publication uses the refreshed record, not merely the record that existed when research began.

## Shorts contract — mandatory
Canonical Shorts are designed inside the long-form pipeline, not written afterward. Follow `00_CORE/SHORTS_ARCHITECTURE.md`.

- Stage 02: identify 6–10 contiguous short-ready story units.
- Stage 03: create `03_SHORTS_MAP.csv`; long-form wording must already contain hook, context, payoff and required caveat.
- Stage 04: fact/legal review every proposed Short in isolation.
- Stage 05: repair weak Short zones inside the long-form script; no separate rewrite path.
- Stage 06: review Short hook, standalone clarity, density, payoff and visualizability.
- Stage 07: lock `07_SHORTS_LOCK.csv`; normal PASS requires it unless the owner explicitly waives Shorts.
- Stages 08–10: use the same locked long-form narration/audio; no separate canonical Short TTS.
- Stage 11: create `11_SHORTS_CUT_MAP.csv` from exact final-master timestamps.
- Stage 12: every Short-used beat must carry `short_ids` and a 9:16-safe strategy.
- Stage 15: cut/reframe/caption/export from exact long-form ranges; no narration reorder or distant-line stitching.
- Stage 16: refresh factual/legal posture for every Short independently.
- Stage 17: package Shorts separately without strengthening factual claims.
