# VIDEO 003 — State

## Goal
Why Universal Music Just Sued DistroKid

## Current
- Status: **IN_PREPARATION**
- Stage 07 Final Script Lock: **PASS / CANONICAL — R3 RETENTION POLISH**
- Stage 08 Voice Script: **PASS — EXACT HARRISON INPUT READY**
- Current pipeline stage: **08_VOICE_SCRIPT**
- Canonical narration: `07_SCRIPT_FINAL.md`
- Voice input: `08_VOICE_SCRIPT.md`
- Job plan: `08_VOICE_JOB_PLAN.csv`
- Harrison: **CHANNEL LOCK**
- Model preflight: **Higgsfield `text2speech_v2` + ElevenLabs**
- Paid generation through Stage 08: **NONE**

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

## Next action
**Stage 09 — Voice QA + Lock**, only on explicit owner instruction.

Stage 09 must verify semantic fidelity, omissions/duplications, pronunciation, numbers/currency/dates, legal terms, attribution, chunking and editability. On PASS it may lock the exact input/settings, but must not submit paid TTS without separate owner approval.

## Blockers
None.
