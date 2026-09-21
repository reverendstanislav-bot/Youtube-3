# VIDEO 001 — 10 Audio Master

Status: **PREFLIGHT COMPLETE / AWAITING OWNER SPEND APPROVAL**

No audio generation has been submitted.

## Locked inputs

- Canonical narration authority: `07_SCRIPT_FINAL.md`
- Canonical TTS input: `08_VOICE_SCRIPT.md`
- Voice QA authority: `09_VOICE_QA.md`
- Narrator: **Bram**
- Voice type: `preset`
- Voice ID: `549ff70a-3ee7-4f04-a4d9-89a24fab7709`

## Proposed synthesis engine

- Provider surface: Higgsfield
- Model: `seed_audio`
- Engine: **Seed Audio 1.0 / ByteDance**
- Reason: default supported Higgsfield speech engine for the locked Bram preset; exposes deterministic speed/loudness/pitch controls and WAV output.

This engine is **proposed for the approved production run**. No generation has been authorized yet.

## Proposed production settings

- format: `wav`
- sample rate: `48000 Hz`
- speech rate: `0`
- loudness rate: `0`
- pitch rate: `0`
- count per request: `1`

Rationale:
- preserve Bram's selected/default character;
- avoid speculative speed or pitch manipulation before hearing production audio;
- 48 kHz WAV is the preferred edit/master source format.

## Provider input limit

Read-only cost validation confirmed:
- `seed_audio` prompt maximum: **2048 characters per job**
- full canonical TTS narration is larger than one request
- one-job full-script generation is therefore invalid

The narration is packed on existing paragraph boundaries only.
No sentence is split.

## Generation plan

Exact planned job count: **8**

| Job | Narrative coverage | Characters | Exact cost |
|---|---|---:|---:|
| 01 | S01 → S02 | 1,949 | 12.0 credits |
| 02 | S02 → S03 → S04 | 1,983 | 12.0 credits |
| 03 | S04 → S05 → S06 | 1,950 | 12.0 credits |
| 04 | S06 → S07 → S08 | 1,961 | 12.0 credits |
| 05 | S08 → S09 | 1,996 | 12.0 credits |
| 06 | S09 → S10 → S11 | 2,030 | 12.0 credits |
| 07 | S11 → S12 | 1,960 | 12.0 credits |
| 08 | S12 ending | 714 | 4.8 credits |

**Exact provider-reported total: 88.8 Higgsfield credits**

Cost was obtained with `get_cost:true`.
That mode performs validation/cost lookup and does **not** submit generation jobs.

## Spend gate — HARD

Before any TTS submission, the owner must explicitly approve all of the following:

- model: `seed_audio` / Seed Audio 1.0
- voice: Bram / `549ff70a-3ee7-4f04-a4d9-89a24fab7709`
- scope: full locked narration in 8 chunks
- settings: WAV 48 kHz, speech/loudness/pitch at default 0
- job count: **8**
- exact estimated charge: **88.8 Higgsfield credits**

Until that approval is received:
- do not call TTS generation;
- do not submit even one test chunk;
- do not treat Stage 10 as PASS;
- do not advance to Stage 11.

## Post-generation QA required before PASS

If generation is explicitly approved, Stage 10 still requires:
- all 8 jobs complete;
- exact text coverage with no missing/duplicated passages;
- Bram voice identity consistent across chunks;
- names/pronunciations audited against `09_VOICE_QA.md`;
- all dollar values/numbers checked;
- no audible synthesis artifacts;
- chunk joins checked for pacing/level discontinuity;
- final assembled runtime recorded;
- master asset URI/path recorded;
- checksum recorded;
- generation date recorded;
- QC result recorded.

Any failed chunk must be identified before any regeneration request. A regeneration is a new paid job and requires separate spend approval unless the owner explicitly authorizes retries in advance.

## Stage boundary

Stage 10 is currently **blocked only at the owner spend-approval gate**.

Stage 11 has not started.
