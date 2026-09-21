# VIDEO 001 — 10 Audio Master

Status: **PREFLIGHT CORRECTED / AWAITING OWNER SPEND APPROVAL**

No audio generation has been submitted.

## Locked inputs

- Canonical narration authority: `07_SCRIPT_FINAL.md`
- Canonical TTS input: `08_VOICE_SCRIPT.md`
- Voice QA authority: `09_VOICE_QA.md`
- Narrator: **Bram**
- Voice type: `preset`
- Voice ID: `549ff70a-3ee7-4f04-a4d9-89a24fab7709`

## Corrected synthesis engine

The initial Stage 10 preflight incorrectly selected `seed_audio`, whose 2048-character prompt cap forced 8 jobs.

That was not the established production pattern from the reference workflow.

Corrected production path:
- frontend: **Higgsfield**
- model wrapper: `text2speech_v2`
- engine/variant: **ElevenLabs**
- voice: **Bram**
- voice type: `preset`
- voice ID: `549ff70a-3ee7-4f04-a4d9-89a24fab7709`
- batch size per job: 1
- unobserved controls: provider defaults

This mirrors the proven four-chunk approach used in the reference YouTube workflow.

## Corrected 4-part generation plan

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

All four read-only cost validations succeeded with `text2speech_v2 + elevenlabs + Bram`.

No generation was submitted.

## Why the previous 8-job plan was rejected

The previous 8-job / 88.8-credit plan was caused by selecting `seed_audio`, which has a 2048-character prompt cap.

The current script itself does **not** require 8 jobs.

The proven `text2speech_v2` wrapper accepts the larger four-part inputs above, matching the production pattern previously used for long-form narration.

The 8-job Seed Audio plan is therefore **SUPERSEDED / REJECTED**.

## Spend gate — HARD

Before any TTS submission, the owner must explicitly approve:

- model wrapper: `text2speech_v2`
- engine: **ElevenLabs**
- voice: **Bram**
- scope: full locked narration in 4 parts
- job count: **4**
- exact estimated total: **43.80 Higgsfield credits**

Until that approval:
- do not submit TTS;
- do not generate a test chunk;
- do not advance to Stage 11.

## Post-generation QA required before PASS

If the owner approves generation:
- generate A → B → C → D only;
- verify complete text coverage;
- verify Bram identity across all four parts;
- verify names, numbers, dates and legal terms;
- inspect artifacts, clipping and pacing;
- inspect joins between parts;
- concatenate only after all four source jobs pass;
- record final runtime, source job IDs, asset URI/path and checksum.

Any retry is a new paid generation and requires separate approval unless explicitly pre-authorized.

## Stage boundary

Stage 10 remains **AWAITING OWNER SPEND APPROVAL**.

Stage 11 has not started.
