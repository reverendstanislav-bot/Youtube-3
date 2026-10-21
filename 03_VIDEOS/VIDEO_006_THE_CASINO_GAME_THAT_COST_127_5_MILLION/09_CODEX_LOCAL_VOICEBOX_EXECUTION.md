# VIDEO006 — Stage09 local Harrison Voicebox execution / Codex handoff

**Status (2026-10-21): EXECUTION BLOCKED IN THIS CHAT; NO WAV GENERATED, NO JOB SUBMITTED, NO SPEND.** Stage08 has PASS_TEXT_PREPARED. The five Voicebox jobs require the local Windows Voicebox service and NVIDIA CUDA machine; neither is accessible to this chat. This handoff specifies the actual next executable work for **Codex with access to that machine**. **Do not misreport this file as generated audio, Stage09 PASS, or active asynchronous processing.**

## Immutable sources

Repo `reverendstanislav-bot/Youtube-3` folder `03_VIDEOS/VIDEO_006_THE_CASINO_GAME_THAT_COST_127_5_MILLION/`.

- Canonical narrative `07_SCRIPT_FINAL.md`, V5 owner-approved, **51 paragraphs P001–P051, 1670 English whitespace words**. Do not change script/paragraph order/capitalization/marks.
- `07_SCRIPT_FINAL_NARRATION_ONLY.md` and Stage08 generated chunks are word-for-word canonical.
- Five exact inputs `08_HARRISON_TTS_CHUNK_01.txt` through `08_HARRISON_TTS_CHUNK_05.txt`, in that numeric order. No act titles or spoken instructions. Do not feed `08_HARRISON_PRONUNCIATION_GUIDE.md` into TTS.
- `08_HARRISON_CHUNK_MAP.csv` has the exact source hashes and ranges: 01 P001–P010 (311 words), 02 P011–P020 (351), 03 P021–P030 (310), 04 P031–P040 (299), 05 P041–P051 (399).
- `07_SHORTS_LOCK.csv`: exactly S01/P003, S04/P023, S05/P027, S07/P043. No standalone Shorts TTS, reorder, rewrite or additional Shorts.
- `08_HARRISON_GENERATION_PLAN.md`: authoritative candidate local generation configuration. Do NOT substitute Higgsfield paid TTS.

## Local voice generation work for Codex

1. **Read-only local preflight:** discover installed Voicebox 0.5.0 local API and actual request schema; query model availability and GPU; confirm selected **Qwen3-TTS 0.6B Base** is usable with CUDA. Confirm existing local clone **Harrison** profile ID `228d3d8a-096f-461b-bf11-4f9415e2dafc`. Preserve canonical channel Harrison identity in `00_FOUNDATION/VOICE_LOCK.md`, Higgsfield preset `573e5163-59b3-4926-aab1-951ef2985f81`. If unavailable, STOP. Do NOT silently change model to 1.7B, voice profile, provider, or paid cloud TTS.
2. Verify SHA-256 of all five text inputs against `08_HARRISON_CHUNK_MAP.csv`; independent text reconstruction must equal all 51 final paragraphs. Stop on mismatch, no TTS request.
3. **Submit job 01 only** with existing chunk01 exact text, US English, Qwen3-TTS 0.6B Base / Harrison profile, seed `20261021`, no added spoken direction, generation segmentation max 800 chars / crossfade 50 ms / normalize only if supported by inspected local API. Do NOT invent endpoints or assume any remote provider API. Name WAV clearly `VIDEO006_HARRISON_CHUNK_01.wav`.
4. Validate Job 01 result: existing output nonempty, uncorrupted PCM audio, independent listening for approved Harrison voice identity and cold-open pronunciation, especially `$127.5 million`, `Light & Wonder`, `Aristocrat`, `Dragon Train`, `Jewel of the Dragon`, `2013`. **If voice identity or text is wrong, STOP. No retry or switch without a separate decision.**
5. If Job01 QC PASS, submit **jobs 02–05 sequentially**, one exact locked text chunk per job, same model/profile/seed/config. No speculative retries. Five jobs maximum, one per provided chunk. No other generated assets.
6. For each WAV record job ID, model/profile, seed, timestamp, native sample rate, channels, sample format, actual duration, filesize and SHA-256; ensure ffmpeg decode succeeds. Listen to beginnings/ends, transitions, all text and dates. Compare ASR readback with canonical paragraphs and document any normalization vs true omission. ASR alone is not human Harrison identity signoff. Identify any clipping, clicks, long silence, chopped words, repeated sentences, glitch, mismatch or unnatural joins. Reject on material defect; **do not regenerate automatically**.
7. Locate exact contiguous native Short paragraph segments S01, S04, S05, S07 in generated audio; record real beginning/end timestamps. Speech-only time may fit, but **final published Shorts including intro, CTA and end frame must be <=30.0 seconds**. Mark finished total duration UNVERIFIED until 9:16 final MP4 exists. Never create separately rewritten Short speech.
8. Deliver reviewable five WAVs, per-chunk ASR/technical results and checksum manifest through an accessible project release/storage; use GitHub Release pattern for VIDEO005 if useful, avoiding large binaries in git tree. Update project Stage09 artifacts (`09_VOICE_REVIEW.md`, per-file QC/asset ledger, `STATE.md`, `manifest.yaml`, `VERSION_LOG.md`, `QA_LEDGER.csv`) only with REAL jobs/results; cite paths and hashes. Do not declare Stage09 PASS until a human listening/A-B check has confirmed canonical Harrison timbre and pronunciation. Do not start Stage10 assembly on assumption.

## Known cost / gate

Stage08 plan: **5 local Voicebox jobs, estimated $0 / 0 provider credits**, excluding local GPU/electricity. User requested progress after this plan. No work was actually submitted from the current chat, and this handoff is not an instruction to spend on paid cloud tools. Pause for direct owner decision on any retry, alternative model, provider, billable work, phonetic input rewrite or Short text edit.

## Current truth

- **Stage08**: PASS text.
- **Stage09**: NOT_STARTED, no WAVs and no voice lock; local execution is unavailable in current connected environment.
- **Stage10**: NOT_STARTED.
- **Stage11**: actual four Short timings and full clips UNVERIFIED.
- **Stage16**: case freshness and media rights remain OPEN.
