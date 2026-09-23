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
- Stage 12 Visual Source / Generation Plan: **IN PROGRESS — 115-BEAT BINDING COMPLETE**
- Current pipeline stage: 12_VISUAL_SOURCE_GENERATION_PLAN — **IN PROGRESS**
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

Stage 12 publication-safe source rebuild:
- rejected placeholder Stage 12B commit was reverted in corrective commit `7238548486b582401ce92934f8171b4790f9f64a`;
- S009 canonical visual source moved from the Justia mirror to the official GovInfo court PDF;
- official GovInfo/DOJ document crop plan is now defined by exact document pages;
- source-rights candidates are classified as U.S.-government/public-domain, CC0, CC BY-SA, editorial-fair-use-review, terms-unclear hold, or reference-only;
- Natural Earth is the preferred public-domain base for editor-built maps;
- publication-safe context candidates now exist for eBay HQ, Natick, insects/parcel/wreath, generic GPS device, generic office, and a Massachusetts fence;
- authentic DOJ/FBI case-evidence photo of the bloody pig Halloween mask + book is now selected for GAP-005; contextually wrong Saw/cosplay/ceremonial stock remains rejected;
- CM/ECF Document 986 (July 27, 2026) is captured as S020 and confirms dismissal with prejudice of all civil claims;
- no final visual asset has been marked acquired/approved and no generation has been submitted.

Source-rights rebuild result:
- **11 / 11 Stage 12 source gaps now have a publication-safe path**;
- this is a source/provenance milestone only — it does not mean final assets have been acquired, rendered or QC-approved;
- source-heavy copyrighted pages (EcommerceBytes, eBay statement, Reuters/Bloomberg) default to editor-native recreation/factual attribution rather than assumed screenshot reuse;
- authentic DOJ/FBI pig-mask evidence replaces the need for a generated pig-mask source visual.

Next action:
- **Stage 12F-R4 COMPLETE: all 115 beats re-audited against locked narration; final-frame/source/prompt chain rebuilt 115/115 with zero missing physical source bindings. No paid generation started. Await owner review/authorization before any test or batch generation.**

## Spend lock — HARD

No new TTS/audio generation may be submitted without explicit owner approval of:
- provider/model;
- candidate count;
- test scope;
- estimated cost/credits.

Existing provider preview samples may be used for read-only shortlisting.

Prior paid voice-test submissions were made without owner spend approval. Do not treat that as precedent or implied authorization.

## Blockers
- Source-rights layer: none blocking; all 11 gaps have safe paths.
- **Stage 12C live-source pack is physically acquired in GitHub under `12B_SOURCE_ASSETS/`** with checksums and rights metadata.
- **Document crops: 19/19 rendered and QA-checked.**
- Visual proof set has not been built/owner-approved.
- Stage 13 remains NOT_STARTED.

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



## Stage 12C result
- **PASS — LIVE SOURCE EXPANSION COMPLETE**
- 115/115 beats audited.
- 93/115 beats have a live-source-led visual path.
- 22/115 are intentionally factual GFX-led with live source files retained underneath.
- 0 mandatory generation gaps remain before proof review.
- exact court/DOJ crops physically rendered into `12B_SOURCE_ASSETS/` (**19/19 crop QA PASS**).
- new primary/first-party sources S021–S026 added.
- no paid generation; Stage 12C spend: 0.
- Stage 13 remains NOT_STARTED.


## Stage 12D result
- **PASS — PROOF STYLE + PRODUCTION SYSTEM LOCKED**
- owner-approved proof direction converted into a binding style bible.
- channel `VISUAL_LOCK.md` extended to v1.1 with subtitle-safe rules.
- 7 reusable template families locked: T01–T07.
- 115/115 beats assigned a template family, frame type, primary live asset, GFX status and subtitle-safe rule.
- 16:9 bottom 20% (Y 864–1080) reserved for subtitles.
- 9:16 bottom 22% reserved for captions/platform UI.
- proof images are style references only; generated evidence/likenesses are prohibited in final factual production.
- Stage 12 remains IN_PROGRESS; Stage 13 remains NOT_STARTED.

## Stage 12E result
- **PASS — PRODUCTION ROLLOUT MAP COMPLETE**
- 115/115 beats have deterministic build instructions.
- each beat has layout variant, physical asset sequence, GFX action, motion sequence, transition, caption-safe rule and Shorts strategy.
- missing physical asset references: 0.
- three identical layout variants in a row: 0.
- three identical hero assets in a row: 0.
- no paid generation submitted.
- no visual render/build executed in this stage; this is the production execution map.
- Stage 13 remains NOT_STARTED.

## Stage 12E-R2 result
- **PASS — DOCUMENTARY RHYTHM CORRECTION**
- 45 beats redirected across existing T01–T07 families.
- longest continuous perceptual-mode run: 29.74 sec; runs >35 sec: 0.
- no three identical layouts or hero assets in a row.
- script/source/claim/legal locks unchanged.
- no paid generation; Stage 13 NOT_STARTED.

## Stage 12F result
- **PASS — GPT IMAGE PROMPT PACK COMPLETE**
- 115 / 115 detailed beat prompts.
- all prompts bound to approved Stage 12D style references SR-A..SR-E.
- semantic reference selection validated against physical Stage 12C assets.
- exact on-image text and legal guardrails locked.
- one-pass future cost: 57.5 credits.
- jobs submitted: 0; spend: 0.
- Stage 13 remains NOT_STARTED.

## Stage 12F-R2 Batch 1
- B001–B035 prompts corrected with the owner-approved sparse document/evidence rule.
- B006 and B018 accepted from the five-image test and marked TEST_PASS_REUSE.
- New jobs required for Batch 1: 33.
- New Batch 1 spend ceiling: 16.5 credits (below the previously approved 17.5-credit ceiling).
- No automatic retries or extra variants are authorized.

## Stage 12F-R2 Batch 1 generation
- **COMPLETE — OWNER QC PENDING**
- 35 scene outputs present for B001–B035.
- 33 new Higgsfield GPT Image 2 jobs completed; 0 provider failures.
- B006 and B018 reused from accepted test outputs.
- new spend: 16.5 credits; effective Batch 1 scene cost including reused test jobs: 17.5 credits.
- no retries or extra variants were submitted.
- Stage 13 remains NOT_STARTED.

## Stage 12F-R2 Batch 1 visual QC
- **PARTIAL PASS — CORRECTION REQUIRED**
- PASS: 7
- EDIT_FIX: 16
- REGEN: 12
- QC spend: 0 credits.
- no regeneration submitted.
- Batch 2 blocked.
- Stage 13 remains NOT_STARTED.

## Stage 12F-R3 five-scene generation
- 5 / 5 jobs completed.
- B008, B017, B026, B029, B034.
- spend: 2.5 credits.
- no retries.
- visual QC pending.
- Batch 2 remains blocked.

## Stage 12F-R4 full beat-to-script audit
- **COMPLETE / CANONICAL PLANNING LAYER**
- 115/115 beats audited against locked narration.
- 115/115 final-frame rows rebuilt.
- 115/115 physical source bindings validated.
- 115/115 prompts/build instructions rebuilt from scratch.
- zero missing physical source bindings.
- zero “blank plate / insert source later” workflows.
- old Stage 12F prompt pack is superseded for future production.
- generation spend in R4: 0 credits.
- Stage 13 remains NOT_STARTED.
