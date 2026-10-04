# VIDEO 003 — State

## Goal
Why Universal Music Just Sued DistroKid

## Current
- Status: **IN_PREPARATION**
- Stage 07 Final Script Lock: **PASS / CANONICAL — R3 RETENTION POLISH**
- Stage 08 Voice Script: **PASS — EXACT HARRISON INPUT READY**
- Stage 09 Voice QA + Lock: **PASS — 4/4 HARRISON SOURCE JOBS COMPLETE**
- Stage 10 Audio Master: **PASS / LOCKED**
- Stage 11 Transcript + Visual Timeline: **PASS / LOCKED — 2,391 spoken tokens corrected**
- Stage 12 Visual Source / Generation Plan: **PASS / R2 CORRECTED CANONICAL**
- Stage 13 Visual Asset QC: **ACTIVE — R6 root-cause repair complete; 80/80 remaining prompts hard-preflight PASS; 40 PASS locked**
- Current pipeline stage: **13_VISUAL_ASSET_QC**
- Canonical narration: `07_SCRIPT_FINAL.md`
- Voice input: `08_VOICE_SCRIPT.md`
- Job plan: `08_VOICE_JOB_PLAN.csv`
- Harrison: **CHANNEL LOCK**
- Model preflight: **Higgsfield `text2speech_v2` + ElevenLabs**
- Paid Harrison generation: **COMPLETE — 46.65 credits / 0 retries**

## Stage 08 exact input
Only delivery-form normalization was applied:
- UMG -> U-M-G
- AI -> A-I
- ISRC -> I-S-R-C
- CVC -> C-V-C
- IFPI -> I-F-P-I
- 4,562 -> four thousand five hundred sixty-two
- 1,000 -> one thousand
- 2,000 -> two thousand
- 150 -> one hundred fifty
- $150,000 -> one hundred fifty thousand dollars

No factual, legal, numerical or causal meaning was changed.

## Production split
| Part | Sections | Characters | Normalized words | Live quoted cost |
|---|---|---:|---:|---:|
| A | S01–S03 | 3,773 | 597 | 11.40 credits |
| B | S04–S06 | 4,125 | 642 | 12.45 credits |
| C | S07–S09 | 3,779 | 584 | 11.40 credits |
| D | S10–S12 | 3,798 | 592 | 11.40 credits |
| **TOTAL** | S01–S12 | **15,475** | **2,415** | **46.65 credits** |

Quote source:
**live Higgsfield cost preflight on 2026-10-04; no jobs submitted.**

## Chunk safety
- 4 sentence-safe jobs.
- Every split is on a section boundary.
- No locked Short is cut by a job boundary.
- No SSML.
- No retries authorized.
- Stage 09 must compare exact input against Stage 07 before locking voice input.

## Stage 09 QA lock result
Before paid submission:
- 4/4 exact normalized parts: **PASS**
- omissions: **0**
- duplications: **0**
- unauthorized rewrites: **0**
- legal/attribution hard gate: **PASS**
- chunking/editability: **PASS**
- live cost re-preflight: **46.65 credits**
- exact review: `09_VOICE_REVIEW.md`

## Approved spend result
Owner approved the locked production step:
**4 Harrison jobs = 46.65 credits total.**

Execution:
- jobs submitted: **4**
- jobs completed: **4**
- failed: **0**
- paid retries: **0**
- actual spend: **46.65 credits**

## Harrison production result
- Part A: `2c4cd5da-7f49-4dc3-8f7a-2bb56428fa64` — **COMPLETED / 235.20 sec**
- Part B: `10c300ad-d52a-459d-930b-170e0e6acd4d` — **COMPLETED / 274.72 sec**
- Part C: `13728239-5079-49e4-934a-b75d7956097e` — **COMPLETED / 230.16 sec**
- Part D: `fb7b4115-3ba6-416a-9168-0e67f7bd0d74` — **COMPLETED / 245.92 sec**
- Raw source sum: **986.00 sec / 16:26.000**
- Actual approved spend: **46.65 credits**
- Paid retries: **0**
- Source ledger: `09_TTS_SOURCE_JOBS.csv`

Provider status is 4/4 COMPLETED and each result exposes an MP3 source URL plus waveform metadata. Local master-level codec/loudness normalization belongs to Stage 10.

## Stage 10 Audio Master
- Master: `VIDEO_003_HARRISON_AUDIO_MASTER.mp3`
- Media ID: `3927e3f3-6b64-4214-8bc0-144d59214b81`
- Runtime: **988.290612 sec / 16:28.291**
- Assembly: **A → 0.75s → B → 0.75s → C → 0.75s → D**
- MP3 / **44.1 kHz / mono / 192 kbps**
- Mean: **-16.8 dBFS**
- Peak: **-0.9 dBFS**
- SHA-256: `d6f149bc0d24be1f40c766ad3b68adfc94720ea67d547d22906cd963f2d551e8`
- Decode: **PASS**
- ASR semantic hard checks: **PASS**
- New credits spent at Stage 10: **0**
- Record: `10_AUDIO_MASTER.md`

## Stage 11 Transcript + Visual Timeline
- Canonical tokens timed: **2,391 / 2,391**
- DIRECT: **2,338 / 97.78%**
- ALIGNED: **53 / 2.22%**
- Word transcript: `11_WORD_TRANSCRIPT.csv.gz`
- Alignment QC: `11_ALIGNMENT_QC.json`
- Visual timeline: **120 beats**
- Visual route assignment: **UNASSIGNED_STAGE12**
- Shorts: **8/8 TIMED_LOCKED**
- Short durations: **44.960–54.600 sec**
- Stage 11 credits: **0**
- Record: `11_TRANSCRIPT_VISUAL_TIMELINE.md`

Stage 12 QA corrected one Stage 11 tokenizer defect: the final Markdown separator `---` had been counted as a 2,392nd token. Correct spoken authority is **2,391**. Final spoken word “battleground” ends at **987.120 sec**. Script/audio/Shorts are unchanged.

## Stage 12 Visual Source / Generation Plan — R2 corrected production model
The prior v01 split of 12 REAL / 18 DOCUMENT / 10 UI / 43 GFX / 37 RECONSTRUCTION is **SUPERSEDED as a final-output model**.

Correct WHAT IT COST model inherited from VIDEO001 final + VIDEO002 R9/R10:
- B001–B120 → **F001–F120**
- finished source-grounded Higgsfield final-frame targets: **120**
- exact in-frame locked headlines: **120**
- source-bound frames: **120 / 120**
- mandatory authentic source inputs per frame: **1–3**
- real source pool: **32**
- source-prep queue: **32 unique prepared inputs**
- raw editor-only/document-only final targets: **0**
- model: **Higgsfield GPT Image 2 / 1k / low / 16:9**
- live rate: **0.5 credit/image**
- paid jobs required: **120**
- base image budget: **60.0 credits**
- image jobs submitted: **0**
- video jobs: **0**
- retries authorized: **0**
- Stage 12 correction spend: **0**

Canonical files:
- `12A_R2_STYLE_LOCK.md`
- `12A_R2_UNIFIED_120_FINAL_FRAME_PROMPTS.md`
- `12A_R2_FINAL_FRAME_PROMPTS_001_030.md`
- `12A_R2_FINAL_FRAME_PROMPTS_031_060.md`
- `12A_R2_FINAL_FRAME_PROMPTS_061_090.md`
- `12A_R2_FINAL_FRAME_PROMPTS_091_120.md`
- `12A_R2_UNIFIED_120_SOURCE_BINDINGS.csv`
- `12A_R2_SOURCE_PREP_QUEUE.csv`
- `12_GENERATION_COUNT_LOCK.md`
- `12_BEAT_ROUTE_MAP.csv`
- `ASSET_MANIFEST.csv`

Every frame carries one exact locked headline directly in the image and uses authentic document/UI/photo/logo references as mandatory factual inputs. The generated environment may compose/frame/light those sources but may not replace or hallucinate them.

## Stage 13 result
- physical prepared references: **32 / 32**
- persistent Higgsfield image uploads: **32 / 32**
- prompt targets reviewed: **120 / 120**
- pre-generation QC rows: **120 / 120 PASS**
- generation-reference bindings: **228**
- unique locked headlines: **120**
- maximum identical adjacent source-set run: **2**
- legal-headline repairs: **4**
- source-diversity repairs: **5**
- paid image jobs submitted: **0**
- Stage 13 credits spent: **0**

Canonical Stage 13 files:
- `13_REFERENCE_FILES.csv`
- `13_SOURCE_VISUAL_QC.csv`
- `13_GENERATION_REFERENCE_BINDINGS.csv`
- `13_PREGEN_QC.csv`
- `12A_R3_UNIFIED_120_FINAL_FRAME_PROMPTS.md`
- `12A_R3_FINAL_FRAME_PROMPTS_001_030.md`
- `12A_R3_FINAL_FRAME_PROMPTS_031_060.md`
- `12A_R3_FINAL_FRAME_PROMPTS_061_090.md`
- `12A_R3_FINAL_FRAME_PROMPTS_091_120.md`

## Next action
Paid generation remains blocked pending explicit owner approval.

Current R6 one-pass remainder if separately approved:
**80 Higgsfield GPT Image 2 jobs × 0.5 credit = 40.0 credits**.

This includes 9 current reject slots and 71 never-generated slots.
Retries authorized: **0**.

## Stage 13B test generation + hard QC
- test range: **F001–F030**
- generated: **30 / 30**
- completed: **30 / 30**
- generation failures: **0**
- paid retries: **0**
- actual spend: **15.0 credits**
- hard visual QC: **19 PASS / 11 REJECT**
- PASS frames: **F001, F002, F004, F005, F007, F009, F010, F011, F012, F013, F017, F018, F020, F022, F024, F025, F027, F028, F030**
- REJECT frames: **F003, F006, F008, F014, F015, F016, F019, F021, F023, F026, F029**
- generation ledger: `13B_TEST30_GENERATION_LEDGER.csv`
- QC ledger: `13C_TEST30_VISUAL_QC.csv`
- next paid generation authorized: **NO**
- reject retries authorized: **0**


## Stage 13D — R4 remaining-101 prompt rewrite
Test30 arithmetic is now the production authority:
- total final frames: **120**
- PASS locked and excluded from regeneration: **19**
- remaining prompts: **101**
  - Test30 REJECT repairs: **11**
  - never generated: **90**
- R4 prompt sections: **101 / 101**
- max factual references per R4 frame: **2**
- maximum identical adjacent source-set run: **2**
- paid jobs submitted by R4 rewrite: **0**
- credits spent by R4 rewrite: **0**

Canonical R4 generation authority:
- `13D_R4_REMAINING_101_PROMPTS.md`
- `13D_R4_REMAINING_101_BINDINGS.csv`
- `13D_R4_PASS19_LOCK.csv`

The 19 PASS frames are frozen. R3 is superseded only for the other 101 frames.
No retry or F031+ generation is authorized.


## Stage 13E — Hard preflight 101/101
- audited: **101 / 101**
- final preflight result: **101 PASS / 0 REJECT**
- semantic/legal/reference/layout repairs applied: **31**
- R4 prompts retained unchanged after hard review: **70**
- existing Test30 PASS frames still frozen: **19**
- missing references/media IDs: **0**
- duplicate frames/headlines: **0**
- PASS19 overlap: **0**
- refs per R5 frame: **1–2**
- max identical adjacent source-set run: **2**
- max identical adjacent layout-mode run: **1**
- paid jobs submitted: **0**
- credits spent: **0**

Canonical next-generation authority:
- `13E_R5_REMAINING_101_PROMPTS.md`
- `13E_R5_REMAINING_101_BINDINGS.csv`
- `13E_R5_HARD_PREFLIGHT_QC.csv`
- `13E_R5_HARD_PREFLIGHT_SUMMARY.md`

R5 supersedes R4 for the 101 non-PASS frames. No paid generation is authorized by Stage13E.


## Stage 13F — R5 Test30 generation + hard visual QC
- owner-approved wave: **30 jobs × 0.5 = 15.0 credits**
- model/settings: **Higgsfield GPT Image 2 / 1k / low / 16:9**
- completed: **30/30**
- generation failures: **0**
- approved prior-reject regenerations: **11**
- first-generation R5 frames: **19**
- hard visual QC: **21 PASS / 9 REJECT**
- new PASS locked: **21**
- total locked PASS: **40 / 120**
- remaining non-PASS: **80 = 9 current rejects + 71 never-generated**
- further paid generation authorized: **NO**
- automatic retries authorized: **0**
- QC ledger: `13F_R5_TEST30_VISUAL_QC.csv`
- summary: `13F_R5_TEST30_VISUAL_QC_SUMMARY.md`


## Stage 13G — R6 root-cause prompt repair
- trigger: **R5 Test30 still produced 9/30 REJECT**
- remaining slots rewritten: **80 / 80**
- current rejects repaired: **9 / 9**
- never-generated remaining prompts preventively rewritten: **71 / 71**
- existing PASS locked and excluded: **40 / 120**
- source-binding simplifications/relevance repairs: **16**
- source-repair frames: **F023, F031, F041, F056, F058, F059, F062, F080, F085, F088, F094, F101, F105, F107, F108, F110**
- exact-headline-only generated-text lock: **80 / 80**
- no-generated-logo lock: **80 / 80**
- source pixel-fidelity / no-reconstruction lock: **80 / 80**
- bottom 20% subtitle-safe: **80 / 80**
- hard preflight: **80 PASS / 0 REJECT**
- canonical prompt pack: `13G_R6_REMAINING_80_PROMPTS.md`
- canonical bindings: `13G_R6_REMAINING_80_BINDINGS.csv`
- QC: `13G_R6_HARD_PREFLIGHT_QC.csv`
- summary: `13G_R6_REPAIR_SUMMARY.md`
- R6 supersedes R5 for these 80 slots only
- paid jobs submitted: **0**
- credits spent: **0**
- next paid generation authorized: **NO**
- retries authorized: **0**
