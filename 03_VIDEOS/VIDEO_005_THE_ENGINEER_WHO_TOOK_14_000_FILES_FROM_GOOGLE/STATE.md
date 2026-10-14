# VIDEO005 — Stage09 release assets uploaded (2026-10-14)

**Stage09: HOLD — TECHNICAL FILE QC PASSED; HUMAN HARRISON LISTENING LOCK PENDING.** Five Voicebox/Qwen3-TTS 0.6B candidate WAV chunks and their QC evidence are available in GitHub Release `video005-harrison-qwen06-20261014`.

## Verified boundary

- Five WAVs; PCM s16le mono 24 kHz.
- Total measured runtime: **994.55 seconds / 16:34.55**.
- Five of five clean ffmpeg decodes and matching SHA-256 hashes.
- ASR comparison retained as supporting evidence; no missing multiword narrative passage found.
- Zero paid credits and no retries.

## Still blocked

Human listening has not yet confirmed canonical Harrison timbre, proper names, joins, artifacts or continuity. S01/S03/S05/S08 final cut durations remain unmeasured. Therefore `locks.voice_input=false`, `locks.audio_master=false`, and Stage10 is NOT_STARTED.

## Next action

Listen to all five release WAVs, record exact defect timestamps, compare against the canonical Harrison reference, and either pass Stage09 or regenerate only failed spans after explicit authorization.

## Additional Stage09 independent file audit (2026-10-14)
All fourteen GitHub Release assets obtained, five WAV SHA256 matches; independent signal inspection PASS: 16:34.55, 24kHz PCM mono, peaks −2.00..−2.75 dBFS, no hard clipping, no >1.2s silence or digital jumps at >0.58FS. Additional ASR word timestamp estimates for same-master Shorts S01 21.32s, S03 22.42s, S05 22.52s, S08 20.22s speech only. These are automatic, not final cut times incl CTA. **G09 still HOLD auditory Harrison identity/name/joins/artifacts; G10 NOT_STARTED.** See `09_VOICE_AUDIO_INDEPENDENT_QC.md`.
