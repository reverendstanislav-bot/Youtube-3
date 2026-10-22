# VIDEO006 — Stage09 Harrison Voice QA

**Status: HOLD — TECHNICAL PASS; HUMAN HARRISON LISTENING LOCK PENDING (2026-10-21).**

Voicebox 0.5.0 generated the locked V5 narration locally with the canonical Harrison clone profile `228d3d8a-096f-461b-bf11-4f9415e2dafc`, Qwen3-TTS 0.6B Base, CUDA and seed `20261021`. Provider cost was **$0 / 0 credits**.

Release: `https://github.com/reverendstanislav-bot/Youtube-3/releases/tag/video006-harrison-qwen06-20261021`

## Accepted audio

| Chunk | Job ID | Duration | SHA-256 | ASR ratio |
|---|---|---:|---|---:|
| 01 | `98e9fafb-e777-4d1e-809f-5ed1a9942713` | 114.22 s | `3366017A74A5B948538EE1EF233F2F7607D2BA2D9483127C722DDF32FA0C4F70` | 0.948882 |
| 02 | `2143ba5b-4bdb-42e1-9c52-0c3d9e145e8f` | 136.62 s | `3102E1602D97C4A46571E2EB59BAA23E550ED96632BB76A742F2C57E342A6BA2` | 0.970381 |
| 03 | `f6d011dc-d6e4-40a8-863f-06005a5b3528` | 118.06 s | `4FEAEC6504095BF545EBABAEDC30CBD4A9C0DCE498B0E4CE4C541B4AFCF0F525` | 0.969600 |
| 04 | `97ee77e3-069a-459c-9759-5c0aef3f0ae9` | 119.98 s | `AFAA948DC66C0291B069CBAC40B13B48206C04F2C8065B58099026B3D93FD04D` | 0.936378 |
| 05 | split jobs below | 163.77 s | `18DE314E04D43D22B73C8AF391658132B621CDBC4973F3322DE750DAE01AAB3C` | 0.956737 |

Chunk 05's first job `59b2676d-b818-43ea-9bd3-43b79712db02` produced a 774.57-second runaway and was rejected. With explicit owner authorization, the same unchanged canonical text was split only at the P046/P047 paragraph boundary. Jobs `2d9a17bb-2ed6-4c34-94e5-0a8ec03158bd` (101.98 s) and `b361f7a0-11a7-46fe-8104-583ef7267d62` (61.79 s) were concatenated in order. No words were rewritten, removed or reordered.

All five accepted WAVs are PCM s16le, 24 kHz, mono and pass `ffmpeg -v error -xerror` decoding. Faster-Whisper comparisons found no missing long narrative passage; ASR normalization differences and possible single-word recognition differences remain listening-review items.

Human review must still confirm canonical Harrison timbre, listed pronunciations, joins and artifacts. Therefore Stage09 is not falsely marked final PASS and `locks.voice_input` remains false.


## Direct-file independent signal QA — 2026-10-21
User uploaded verified master WAV and it was decoded and directly measured. **SHA-256 identical to release, 653.13s, s16le/48kHz/mono, −16.2 LUFS, true peak −1.5 dBTP, zero clipped samples, no ≥1s near-silent gaps**; five sections have matching −16.1dBFS RMS. See `09_MASTER_INDEPENDENT_SIGNAL_QC.md` and `09_MASTER_BOUNDARY_SIGNAL_QC.csv` for five potential listening-watch boundaries. **Does not certify canonical Harrison voice identity, pronunciation, lack of audible splice defects, or ASR/Short timing**. Stage09/10 auditory lock remains HOLD.
