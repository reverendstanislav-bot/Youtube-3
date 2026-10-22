# VIDEO007 — Stage09 Harrison Voice QA

**Status: HOLD — TECHNICAL PASS; HUMAN HARRISON LISTENING LOCK PENDING (2026-10-22).**

Five locked Stage08 inputs were generated sequentially with local Voicebox 0.5.0, Harrison clone profile `228d3d8a-096f-461b-bf11-4f9415e2dafc`, Qwen3-TTS 1.7B Base, CUDA and seed `20261021`. Provider cost was **$0 / 0 credits**. No retry, fallback or parallel generation was used.

The five accepted WAVs total **971.88 seconds (16:11.88)**. All are PCM s16le, 24 kHz, mono and pass `ffmpeg -v error -xerror` decoding. SHA-256 values and job IDs are recorded in `09_GENERATION_MANIFEST.json`; technical results are in `09_AUDIO_QC.csv`.

Faster-Whisper sequence ratios are 0.969935, 0.972710, 0.981207, 0.980525 and 0.979554. No long missing passage, duplicate section or reordered block was found. Recognition differences mainly normalize dates/numbers and joined names. Human listening must specifically verify Harrison identity and pronunciation of Chang Liu, Tang Yew Tan, Judge Edward Davila, io Products, OpenAI, ChatGPT and the legal terms listed in `09_VOICE_QC_PLAN.md`.

Stage09 is technically complete but is not falsely marked final Voice Lock. `locks.voice_input` remains true for the approved text input; `voice_identity_status` remains pending human A/B listening.
