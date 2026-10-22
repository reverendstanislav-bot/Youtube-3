# VIDEO006 — Stage10 Audio Master

**Status: MASTER TECHNICAL PASS; AUDITORY VOICE LOCK PENDING (2026-10-21).**

- File: `VIDEO006_HARRISON_STAGE10_AUDIO_MASTER_48K_MONO.wav`
- Download: `https://github.com/reverendstanislav-bot/Youtube-3/releases/download/video006-harrison-qwen06-20261021/VIDEO006_HARRISON_STAGE10_AUDIO_MASTER_48K_MONO.wav`
- Runtime: **653.13 seconds (10:53.13)**
- Format: PCM s16le, 48 kHz, mono
- Integrated loudness: **-16.2 LUFS**
- True peak: **-1.5 dBTP**
- LRA: **2.4 LU**
- SHA-256: `A42C0E6245D66F4DA25B5528BEC04047B9E7F7EBF759E412E6490D627CF8D308`
- Decode: PASS (`ffmpeg -v error -xerror`)

The master uses the five accepted Stage09 chunks in locked order and inserts four 120 ms chapter pauses. Loudness normalization and 48 kHz conversion were applied after assembly. No narration was rewritten, cut or reordered.

Stage10 assembly is complete at the technical level. Final audio lock remains pending human listening for Harrison identity, pronunciation, joins and artifacts; `locks.audio_master` remains false until that review.


## Direct-file independent signal QA — 2026-10-21
User uploaded verified master WAV and it was decoded and directly measured. **SHA-256 identical to release, 653.13s, s16le/48kHz/mono, −16.2 LUFS, true peak −1.5 dBTP, zero clipped samples, no ≥1s near-silent gaps**; five sections have matching −16.1dBFS RMS. See `09_MASTER_INDEPENDENT_SIGNAL_QC.md` and `09_MASTER_BOUNDARY_SIGNAL_QC.csv` for five potential listening-watch boundaries. **Does not certify canonical Harrison voice identity, pronunciation, lack of audible splice defects, or ASR/Short timing**. Stage09/10 auditory lock remains HOLD.
