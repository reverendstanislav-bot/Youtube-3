# VIDEO007 — Stage11 ASR alignment QC

**Result: PASS_ASR_SOURCE_ANCHORED. Owner accepted the Harrison master before Stage11. Final rendered Shorts remain a later-stage hold.**

- Master: `VIDEO007_HARRISON_STAGE10_AUDIO_MASTER_48K_MONO.wav`; 972.36s; SHA-256 `0AF812DB9D7A7CC509DCEC346D6AC9995281816F7505FC704A245867C5225B0C`.
- Alignment: local Faster-Whisper base, CPU int8, English, beam 5, word timestamps, VAD off.
- Canonical paragraphs: 60/60 with ordered ASR anchors.
- Exact normalized token alignment: 2522/2581 = 97.71%.
- Timeline: 0–24309 frames at 25fps, zero gaps and zero overlaps.
- Audio generation/retry/spend during Stage11: none.

## Per-chunk alignment

| Chunk | Script tokens | ASR tokens | Exact matches | Fraction |
|---:|---:|---:|---:|---:|
| 1 | 386 | 382 | 375 | 97.15% |
| 2 | 520 | 522 | 506 | 97.31% |
| 3 | 518 | 522 | 509 | 98.26% |
| 4 | 603 | 608 | 591 | 98.01% |
| 5 | 554 | 557 | 541 | 97.65% |

## Lower-score paragraph review

- `A02-P01` 02:23.890–02:38.710: 82.50%; retain locked text and verify phonemes during final edit QC.

The SRT uses canonical locked narration with ASR speech boundaries. It is a paragraph-level editorial draft, not a word-perfect subtitle export. ASR spelling differences do not modify the approved script.
