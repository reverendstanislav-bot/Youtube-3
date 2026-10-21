# VIDEO007 — Stage09 Harrison Voice QA + Lock Preparation

**Status: READY_FOR_OWNER_GENERATION_APPROVAL — NO TTS SUBMITTED — NO AUDIO EXISTS (2026-10-21).**

## Upstream integrity

- Canonical Stage07 script: `07_SCRIPT_FINAL.md`, SHA-256 `8EDCAF0F0461F2B568B2803A6CF1C0457C37D4433D9641AF22E60398DE1F0250`.
- Stage08 master: `08_VOICE_SCRIPT_MASTER.txt`, SHA-256 `1EE926364C616AF59EF049E1CCCC20EA3FF78DF8ADE1FAEAE903E2F1840BA5C1`.
- `07_SCRIPT_FINAL_NARRATION_ONLY.txt` and `08_VOICE_SCRIPT_MASTER.txt` are byte-identical.
- Independent extraction confirms 60/60 ordered paragraphs and 2,517 lexical words. The repository count excludes seven standalone em-dash separator tokens.
- Five Stage08 segments reconstruct the master exactly: zero omissions, duplications, reordering or wording changes.
- Exactly four locked Shorts remain SH01/A00-P01, SH02/A05-P03, SH03/A07-P03 and SH04/A09-P03.
- Read-only Voicebox history audit: 27 older records exist, but **0 exact matches** to any VIDEO007 Stage08 segment. Several newest unrelated records show empty audio paths and `generating`; they are not VIDEO007 outputs and were not modified.

Full evidence is in `09_TEXT_INTEGRITY_QC.md`.

## Selected synthesis route

**Primary:** local Voicebox 0.5.0, Qwen3-TTS 1.7B Base, CUDA, cloned profile candidate `Harrison` ID `228d3d8a-096f-461b-bf11-4f9415e2dafc`.

Why: the installed API reports Qwen TTS 1.7B downloaded and loaded, CUDA active on the NVIDIA RTX 3050 6 GB, about 4,160.9 MB VRAM in use and no compatibility warning. Voicebox documents the 1.7B Base model as its highest-quality cloning option. Every prepared segment is below the API's 5,000-character request limit.

The channel identity authority remains the Higgsfield Harrison preset `573e5163-59b3-4926-aab1-951ef2985f81`. The local profile has one 28.4-second sample and is described as cloned from the clean VIDEO004 narration master, but generated timbre has not been A/B-approved against canonical Harrison for VIDEO007. Therefore the profile is a candidate implementation, not a silent replacement of the channel lock.

**Fallback:** Qwen3-TTS 0.6B Base is downloaded and lighter, but it is not selected because 1.7B is currently healthy and offers the better quality tier. No automatic fallback is allowed. Qwen CustomVoice models use preset speakers rather than this cloned Harrison profile; LuxTTS, Chatterbox, TADA and Kokoro are not downloaded and have no verified Harrison match.

## Exact proposed submission

- Five sequential local jobs, one existing Stage08 segment per job.
- Model size: `1.7B`; language: `en`; fixed seed: `20261021`.
- No delivery instruction field: Qwen Base cloning does not support the CustomVoice instruction path.
- Submit Job 01 first. Perform immediate voice-identity and pronunciation spot-check. Continue Jobs 02–05 only if Job 01 passes; otherwise stop with no retry or fallback.
- Planned job inputs, hashes and output names: `09_HARRISON_GENERATION_PLAN.csv`.

## Cost

Voicebox runs locally: **$0 provider charge and 0 generation credits** for the five planned jobs. GPU time and electricity are local operating costs and are not priced here. No model download is required for the selected route.

## Gate boundary

This preparation does not pass Stage09 Voice Lock. No VIDEO007 TTS request was submitted. After explicit owner authorization, generated audio must pass `09_VOICE_QC_PLAN.md`, including human Harrison A/B, pronunciation, exact text/order, decode/artifact checks, paragraph joins and four-Short timing. Stage10 remains NOT_STARTED.
