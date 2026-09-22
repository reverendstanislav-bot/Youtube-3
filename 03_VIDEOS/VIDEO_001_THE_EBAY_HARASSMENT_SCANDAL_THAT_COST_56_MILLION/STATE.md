# VIDEO 001 — State

## Goal
The eBay Harassment Scandal That Cost $56 Million

## Current
- Status: IN_PREPARATION
- Stage 07 Final Script Lock: **PASS**
- Stage 08 Voice Script: **PASS**
- Stage 09 Voice QA + Lock: **PASS**
- Stage 10 Audio Master: **PASS / LOCKED**
- Stage 11 Transcript + Visual Timeline: **PASS / LOCKED**
- Stage 12 Visual Source / Generation Plan: **PASS / ASSET-READY — STAGE 12B COMPLETE**
- Current pipeline stage: 12_VISUAL_SOURCE_GENERATION_PLAN — **PASS; STAGE 13 NOT STARTED**
- Canonical narration: `07_SCRIPT_FINAL.md`
- Final script length: ~2,321 words
- Performance review: PASS — 92/100

## Locked script status
`07_SCRIPT_FINAL.md` is now the only canonical narration text.

Historical drafts:
- `03_SCRIPT_V1.md`
- `05_SCRIPT_V2.md`

Do not generate final narration from those historical drafts.

## Stage 07 micro-edits applied
1. S02 background compressed immediately after the hook.
2. S03 first appearances now identify Wenig / Wymer / Baugh / Jones roles more clearly.
3. S09 summary-judgment explanation compressed without removing liability/fairness safeguards.
4. Existing ending preserved with no CTA before the final WHAT IT COST line.

## Claim traceability
All material facts remain inside the same S01–S12 section map used by CLAIMS_LEDGER.

No chronology, dollar figure, legal status or party position changed during Stage 07.

## Voice status
**VOICE LOCKED — HARRISON**

- Provider/catalog: Higgsfield
- Voice type: preset
- Voice ID: `573e5163-59b3-4926-aab1-951ef2985f81`
- Provider preview: https://d1xarpci4ikg0w.cloudfront.net/audio_voice_preset/preview/725aa234-8c64-4a87-8f5e-220aca1375f7.mp3
- Owner-approved same-text test: https://d8j0ntlcm91z4.cloudfront.net/user_3J3zfwu7kpgllQvPySWoLtXHwdR/hf_20260921_053343_e202b139-a5ae-4276-b3f7-109cb955909f.mp3
- Comparison job ID: `e202b139-a5ae-4276-b3f7-109cb955909f`
- Previous Bram lock: **SUPERSEDED BY OWNER**
- No new TTS generation authorized.

Stage 08 result:
- `08_VOICE_SCRIPT.md` created from the locked final script;
- spoken dates/years and unambiguous abbreviations normalized;
- section IDs preserved;
- no factual/legal wording changed;
- no SSML added before engine lock;
- pronunciation targets handed to Stage 09;
- no audio generated and no paid generation authorized.

Stage 09 result:
- semantic fidelity audit PASS;
- Stage 08 correction: 1999 → nineteen ninety-nine;
- dates/numbers/abbreviations QA PASS;
- high-confidence pronunciation locks recorded;
- speculative phonetic respellings prohibited;
- person-specific uncertain pronunciations carried to Stage 10 auditory QC;
- no audio generated.

Stage 10 result:
- Harrison production path: `text2speech_v2` + ElevenLabs;
- 4 approved production jobs completed successfully;
- production spend: **43.80 credits**;
- one owner-approved corrective patch: **0.60 credit**;
- total Stage 10 spend: **44.40 credits**;
- Part D 58.7M spoken-number ambiguity corrected before master lock;
- final master runtime: **15:57.414**;
- clipping: none detected;
- final master SHA-256: `00069b3717cb21a5134d0e0d7cb5ae15836f926a6286adfb66b7eb9103fa14d3`;
- master URI: https://d2ol7oe51mr4n9.cloudfront.net/user_3J3zfwu7kpgllQvPySWoLtXHwdR/4c1aa66b-440d-4fc7-ae95-78e60845ae5f.mp3;
- Stage 10: **PASS / AUDIO MASTER LOCKED**.

Stage 11 result:
- final Stage 10 audio SHA-256 reverified before alignment;
- **2,152** canonical narration words aligned to the final Harrison master;
- authored-script / ASR similarity: **0.944**;
- `11_CAPTIONS.srt`: **409** authored-text cues;
- `11_VISUAL_TIMELINE.csv`: **115** locked visual beats, median **7.42s**, max **16.86s**;
- **52** beats flagged HIGH legal sensitivity;
- timeline uses a compact codebook documented in `11_TRANSCRIPT_VISUAL_QA.md`;
- every visual beat remains `UNSOURCED` for Stage 12;
- no visual assets were searched, downloaded or generated;
- Stage 11: **PASS / VISUAL TIMELINE LOCKED**.

Stage 12 binding subtask result:
- **115 / 115** Stage 11 beats mapped to concrete visual treatment;
- **115 / 115** beats have source IDs and claim IDs;
- **87** beats use at least one GFX family;
- **69** require source-document treatment;
- **28** use rights-safe photo/archive material;
- **7** specifically require archive-web capture;
- **7** use editor-built map/location treatment;
- **12** beats allow clearly labelled reconstruction;
- **11** reusable source-gap packages identified;
- **5** reconstruction candidates covering **6** potential images if later approved;
- exact money, dates, legal labels and quotations remain editor-native;
- real-person likeness generation prohibited;
- no image/video generation submitted and no credits spent.

Shorts architecture backfill:
- **10** contiguous canonical Shorts locked to final Harrison audio;
- exact cuts: `11_SHORTS_CUT_MAP.csv`;
- no rewritten/reordered narration and no new TTS;
- Stage 12 beat map carries `short_ids` plus 9:16-safe requirements.

Stage 12B result:
- authentic source/reference package acquired and provenance-logged;
- exact document crop sheet prepared;
- 15 / 15 editor-native GFX SVG masters built;
- 2 schematic map SVGs built;
- 6 labelled editor-native reconstruction fallback SVGs built;
- all 11 source gaps now have non-blocking asset paths;
- optional AI reconstruction package remains ungenerated;
- read-only cost preflight: 6 independent GPT Image 2 jobs × 0.5 credit = **3.0 credits**;
- Stage 12B spend: **0 credits**.

Next action:
- **Stage 12 PASS. Await explicit owner authorization before starting Stage 13 Visual Asset QC.**

## Spend lock — HARD

No new TTS/audio generation may be submitted without explicit owner approval of:
- provider/model;
- candidate count;
- test scope;
- estimated cost/credits.

Existing provider preview samples may be used for read-only shortlisting.

Prior paid voice-test submissions were made without owner spend approval. Do not treat that as precedent or implied authorization.

## Blockers
- No Stage 12 blocker. Optional AI reconstruction upgrade is unapproved but non-blocking because editor-native fallbacks exist.

## Important
The working title is still provisional and remains a Stage 17 packaging decision.


## Task-scope lock — HARD
For VIDEO_001, execute only the stage/action explicitly requested by the owner.

Do not:
- auto-advance to the next stage;
- generate paid or free samples without explicit instruction;
- create downstream artifacts early;
- treat a recommendation as authorization;
- continue after the requested deliverable is complete.

Voice selection is complete.

**Harrison is FINAL LOCK.**

The previous Bram lock is superseded.

Do not reopen selection, test substitutes, or generate audio unless the owner explicitly requests it.



## Stage 12B spend gate
No reconstruction generation was submitted. Optional six-image GPT Image 2 upgrade remains gated at 3.0 credits total and requires explicit owner approval.
