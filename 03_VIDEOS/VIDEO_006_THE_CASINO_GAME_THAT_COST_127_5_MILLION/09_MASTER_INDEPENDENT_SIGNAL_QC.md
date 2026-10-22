# VIDEO006 — Independent DIRECT WAV signal / seam QC (uploaded master)

**2026-10-21 | TECHNICAL SIGNAL PASS / SPEAKER IDENTITY AND SEMANTIC LISTENING HOLD.** Unlike the prior GitHub-only producer report, this review used actual bytes of user-uploaded `VIDEO006_HARRISON_STAGE10_AUDIO_MASTER_48K_MONO.wav` in the ChatGPT sandbox, not just repository metadata. **No pretrained ASR / actual speech transcription was available** and **no reliable human ear-to-ear A/B of the canonical Higgsfield Harrison reference was completed**, so do not call Stage09 or Stage10 final AUDITORY PASS. No change to the actual master was made.

## Directly reproduced from uploaded binary

| Test | Actual measured | Status |
|---|---|---|
| File SHA-256 | `a42c0e6245d66f4da25b5528bec04047b9e7f7ebf759e412e6490d627cf8d308` | **PASS** exact match with locked Release/manifest hash |
| PCM stream | s16le, mono, 48,000 Hz | PASS |
| Exact length | 31,350,240 samples; 653.130000 seconds (10:53.13) | PASS |
| File size | 62,700,558 bytes | PASS |
| Independent FFmpeg decode | No errors | PASS |
| Independent FFmpeg EBU R128 integrated loudness | **−16.2 LUFS** | PASS |
| Independent FFmpeg EBU R128 true peak | **−1.5 dBTP** | PASS |
| Independent FFmpeg EBU R128 loudness range | **2.5 LU** (previous report 2.4, negligible rounding/method difference) | PASS |
| Actual peak amplitude | 0.84296 FS (≈−1.48 dBFS sample peak) | PASS |
| DC offset | approx −0.00000815 FS | PASS |
| Hard clip samples at |amplitude| ≥0.999 FS | **0** | PASS |
| Long quiet periods | **0 runs ≥1.0 s** at 20ms RMS window / threshold −42 dBFS; longest about **0.72 s** | PASS; perceptual pause judgment still unverified |
| Maximum adjacent-sample jump | **0.4135 FS** near 08:36.35 | BELOW 0.58 legacy threshold; not sufficient to assert zero audible clicks |

## Accepted five-part master structure: measured from actual PCM

| Part | Master interval (s) | Seconds | Observed RMS dBFS | Observed sample peak dBFS |
|---|---|---:|---:|---:|
| 01 | 0.00–114.22 | 114.22 | −16.17 | −1.49 |
| 02 | 114.34–250.96 | 136.62 | −16.11 | −1.50 |
| 03 | 251.08–369.14 | 118.06 | −16.13 | −1.49 |
| 04 | 369.26–489.24 | 119.98 | −16.13 | −1.49 |
| 05 | 489.36–653.13 | 163.77 | −16.11 | −1.48 |

Each transition (114.22→114.34, 250.96→251.08, 369.14→369.26, 489.24→489.36) has the expected ~0.12 s low-level chapter gap. Measured sample jumps at incoming borders range ~0.0223–0.0245 FS. Levels across parts closely match; technical continuity is satisfactory, but no spectrogram-only or sample-based statistic proves the **sound of the same speaker** or all word/number pronunciation.

## Specific listening watch points / risks

- **00:02.60–00:03.30**, **00:07.98–00:08.64**, **00:11.34–00:11.90**: pronounced sub-one-second intro pauses in waveform; *check retention/pacing by ear*, not inherently errors.
- **01:54.34, 04:11.08, 06:09.26, 08:09.36**: four assembled chunk starts; check first consonant, natural handoff, and possible click/breath interruption.
- **09:51.34**: expected join in *fifth chunk* after originally rejected runaway, between P046/P047 (post-Regeneration split at chunk-local 101.98 seconds). Preceding 0.10-second RMS around −40.6dBFS, next about −23.3 dBFS, one-sample jump about 0.0252 FS. **Requires human A/B listening to determine audibility/naturalness; not an automatically observed audible defect.**
- **08:36.35**: largest single-sample jump (0.4135 FS), embedded in active speech, not a proven glitch. Check if an impulsive click is heard.
- **Master end 10:53.13**: a level taper is present over the last ~0.2s; verify final word is fully audible, not unintentionally cut.

## What remains not proven

1. Exact canonical Higgsfield **Harrison** timbre against approved reference, and natural delivery by human listening: **HOLD**.
2. Hearing exact names, dates, amounts, every paragraph once and all legal disclaimers: **HOLD**. Repo ASR ratios alone do not prove 51/51 audible fidelity.
3. Independent master word-level ASR and real first/last audible-word anchors per paragraph: **HOLD**. Existing Stage11 provisional timeline is word-proportional and cannot serve as edit, subtitle or Short extraction timestamps.
4. Four actual final 9:16 Shorts length ≤30.0s incl CTA and tail: **HOLD**. Original V5 script unchanged and 4 Short IDs unchanged.

**Source provenance:** uploaded master hash equals GitHub release and `manifest.yaml`. This file contains direct signal findings, not invented subjective hearing. No new TTS, no regeneration, no spend, no video.
