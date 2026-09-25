# VIDEO 002 — 09 Voice QA + Production Lock

Status: **PASS — 4/4 HARRISON SOURCE JOBS COMPLETE**

Date: **2026-09-25**

Canonical narration:
`07_SCRIPT_FINAL.md` — R2

Exact TTS input:
`08_VOICE_SCRIPT.md`

Narrator:
**Harrison**

Engine:
- model wrapper: `text2speech_v2`
- variant: **ElevenLabs**
- voice type: `preset`
- voice ID: `573e5163-59b3-4926-aab1-951ef2985f81`

## Owner-approved spend

Owner explicitly approved:
**4 Harrison jobs / 44.40 credits total**

Actual cost preflight immediately before submission:

| Part | Sections | Cost |
|---|---|---:|
| A | S01–S03 | 10.50 credits |
| B | S04–S06 | 9.45 credits |
| C | S07–S09 | 11.25 credits |
| D | S10–S13 | 13.20 credits |
| **TOTAL** | S01–S13 | **44.40 credits** |

No automatic retry was submitted.

## Production jobs

| Part | Job ID | Status | Duration |
|---|---|---|---:|
| A | `0b948be1-ad0f-4c4f-999f-45523b4fa791` | COMPLETED | 230.034 sec |
| B | `af0f4549-72c1-4730-8891-8df06d2920af` | COMPLETED | 189.153 sec |
| C | `2842d972-f1db-4231-8dc1-c418d69ef3d4` | COMPLETED | 242.364 sec |
| D | `cbf8e230-da8b-4d1a-8bcc-004b70b6bad2` | COMPLETED | 276.924 sec |

Raw source-audio sum:
**938.475 sec / 15:38.475**

This is the sum of the four source jobs, not yet the Stage 10 master runtime.

## Technical QC

All four files:
- codec: MP3
- sample rate: **44.1 kHz**
- channels: **mono**
- decode: PASS

Measured levels:

| Part | Mean | Peak |
|---|---:|---:|
| A | -16.6 dB | -1.0 dB |
| B | -16.5 dB | -0.8 dB |
| C | -16.5 dB | -0.8 dB |
| D | -16.3 dB | -0.9 dB |

No source part shows a material loudness mismatch.

## ASR-assisted semantic QC

Independent base.en transcription produced:
- A: 509 recognized words
- B: 478
- C: 562
- D: 648

Critical content confirmed in the rendered audio by ASR:
- Adobe agreed to acquire Figma for about **$20B**;
- acquisition did not close;
- Adobe paid Figma **$1B**;
- fee is not a government fine;
- June 19 / July 5 / July 20 negotiation sequence present;
- liquidated-damages language present;
- CMA provisional status present;
- European Commission preliminary-status distinction present;
- DOJ investigation / no filed merger-lawsuit framing present;
- mutual termination present;
- **$20B vs $1B** distinction present;
- **no $21B purchase-cost claim**;
- Figma IPO section contains **12.5M shares at $33/share** and **~$393.1M** net proceeds;
- no-causation IPO caveat present;
- final "That is what it cost" payoff present.

A second small.en pass on Part D independently resolved the IPO line as:
**12.5 million ... shares at $33 per share**
and the later proceeds as:
**$393.1 million**.

ASR is a QA aid, not a substitute for human hearing. No paid corrective job is authorized or required by the current technical/semantic evidence.

## Runtime note

The four rendered source parts total **15:38.475**, around 21.5 seconds below the 16:00 lower edge of the working target.

This is **not** grounds for a paid retry.

Stage 10 can resolve final pacing through deterministic master assembly / chapter breathing room if desired. No narration wording change is required.

## Stage 09 decision

**PASS**

- 4/4 jobs completed;
- exact approved spend consumed: **44.40 credits**;
- retries: **0**;
- technical QC: PASS;
- semantic/number/legal ASR QC: PASS;
- source audio ready for Stage 10.

## Stage boundary

**STOP.**

Stage 10 Audio Master is **NOT STARTED**.
Do not concatenate, retime, insert pauses, or alter source audio until explicit owner instruction.
