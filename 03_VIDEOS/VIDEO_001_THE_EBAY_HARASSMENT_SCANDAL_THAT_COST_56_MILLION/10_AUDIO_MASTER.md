# VIDEO 001 — 10 Audio Master

Status: **VOICE CHANGED / COST REVALIDATION REQUIRED / NO PRODUCTION AUDIO GENERATED**

No audio generation has been submitted.

## Locked inputs

- Canonical narration authority: `07_SCRIPT_FINAL.md`
- Canonical TTS input: `08_VOICE_SCRIPT.md`
- Voice QA authority: `09_VOICE_QA.md`
- Narrator: **Harrison**
- Voice type: `preset`
- Voice ID: `573e5163-59b3-4926-aab1-951ef2985f81`

## Corrected synthesis engine

The initial Stage 10 preflight incorrectly selected `seed_audio`, whose 2048-character prompt cap forced 8 jobs.

That was not the established production pattern from the reference workflow.

Corrected production path:
- frontend: **Higgsfield**
- model wrapper: `text2speech_v2`
- engine/variant: **ElevenLabs**
- voice: **Harrison**
- voice type: `preset`
- voice ID: `573e5163-59b3-4926-aab1-951ef2985f81`
- batch size per job: 1
- unobserved controls: provider defaults

This mirrors the proven four-chunk approach used in the reference YouTube workflow.

## Previous 4-part structure and Bram cost reference

| Part | Sections | Characters | Words | Exact cost |
|---|---|---:|---:|---:|
| A | S01–S03 | 3,499 | 532 | 10.50 credits |
| B | S04–S06 | 2,999 | 452 | 9.00 credits |
| C | S07–S09 | 4,124 | 612 | 12.45 credits |
| D | S10–S12 | 3,929 | 554 | 11.85 credits |

Total:
- **4 jobs**
- **14,551 narration characters**
- **2,150 spoken words**
- **43.80 Higgsfield credits exact provider-reported cost**

The four-part structure was previously validated with `text2speech_v2 + elevenlabs + Bram`, but Bram is now superseded as narrator.

The **43.80-credit figure is historical Bram preflight data only and is not an approved Harrison production quote**.

A fresh read-only cost validation for Harrison is required before any production spend approval.

No full-production generation was submitted.

## Why the previous 8-job plan was rejected

The previous 8-job / 88.8-credit plan was caused by selecting `seed_audio`, which has a 2048-character prompt cap.

The current script itself does **not** require 8 jobs.

The proven `text2speech_v2` wrapper accepts the larger four-part inputs above, matching the production pattern previously used for long-form narration.

The 8-job Seed Audio plan is therefore **SUPERSEDED / REJECTED**.

## Spend gate — HARD

Before any TTS submission, the owner must explicitly approve:

- model wrapper: `text2speech_v2`
- engine: **ElevenLabs**
- voice: **Harrison**
- scope: full locked narration in the final validated chunk plan
- job count and exact estimated total: **must be revalidated read-only for Harrison before approval**

Until that approval:
- do not submit TTS;
- do not generate any additional test chunk without separate explicit spend approval;
- do not advance to Stage 11.

## Post-generation QA required before PASS

If the owner approves generation:
- generate A → B → C → D only;
- verify complete text coverage;
- verify Harrison identity across all production parts;
- verify names, numbers, dates and legal terms;
- inspect artifacts, clipping and pacing;
- inspect joins between parts;
- concatenate only after all four source jobs pass;
- record final runtime, source job IDs, asset URI/path and checksum.

Any retry is a new paid generation and requires separate approval unless explicitly pre-authorized.

## Stage boundary

Stage 10 remains **BLOCKED ON READ-ONLY HARRISON COST REVALIDATION, THEN OWNER SPEND APPROVAL**.

Stage 11 has not started.
