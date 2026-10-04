# VIDEO 003 — State

## Goal
Why Universal Music Just Sued DistroKid

## Current
- Status: **IN_PREPARATION**
- Stage 07 Final Script Lock: **PASS / CANONICAL — R3 RETENTION POLISH**
- Stage 08 Voice Script: **PASS — EXACT HARRISON INPUT READY**
- Stage 09 Voice QA + Lock: **PASS — 4/4 HARRISON SOURCE JOBS COMPLETE**
- Current pipeline stage: **09_VOICE_QA_LOCK**
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

## Spend gate
**NOT AUTHORIZED.**

Current planned paid step after Stage 09, if owner approves:
**4 Harrison jobs = 46.65 credits total.**

## Stage 09 lock result
- 4/4 exact normalized parts: **PASS**
- omissions: **0**
- duplications: **0**
- unauthorized rewrites: **0**
- legal/attribution hard gate: **PASS**
- chunking/editability: **PASS**
- live cost re-preflight: **46.65 credits**
- TTS jobs submitted: **0**
- credits consumed: **0**
- exact review: `09_VOICE_REVIEW.md`

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

## Next action
**Stage 10 — Audio Master**, only on explicit owner instruction.

## Blockers
None.
