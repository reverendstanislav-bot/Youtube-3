# VIDEO006 — Stage09/10 listening and Stage11 exact timestamp closure

**CURRENT: HOLD.** Existing GitHub release/master must be retrieved by a local workstation with binary download. This assistant could inspect metadata, not obtain or play the actual WAV; no independent human listening, direct PCM or transcript alignment is claimed.

## Requirements (in order; no new generation)

1. Obtain five existing WAV segments and the master from [Release](https://github.com/reverendstanislav-bot/Youtube-3/releases/tag/video006-harrison-qwen06-20261021); run SHA-256 on all against `ASSET_MANIFEST.csv` and master checksum `A42C0E6245D66F4DA25B5528BEC04047B9E7F7EBF759E412E6490D627CF8D308`. Confirm with ffprobe/ffmpeg full decode, 48kHz mono master, 653.13s, ~-16.2 LUFS and -1.5 dBTP. Reports are **not** independently measured in chat.
2. Human listen on original clean master: P001–P005 pacing, Harrison timbre compared A/B with approved Higgsfield Harrison reference, chapter joins after chunks 01/02/03/04, **P046-P047** original rejected segment 05 split/rebuild, any glitches, repeats, dropped words or robotic artifacts. Check financial/legal dates/values, Emma Charles, Aristocrat, AztecGold, Inception Conception. Document defects by actual timestamp; do not auto-regenerate.
3. Run actual master word-timestamp ASR (faster-whisper or comparable) + align against *exact* 51 canonical P texts. Store `11_ASR_WORD_TIMINGS.csv`, match confidence and interpolated/unmatched status separately. No false precision based on word count. Human-audit first/last audible words for all Short native paragraphs and any weak boundary.
4. Replace all 51 **MODEL** scene boundaries with true speech/pause boundary frames and revalidate contiguous 25fps coverage 0..16329. Emit final `11_VISUAL_TIMELINE.csv` and `11_TRANSCRIPT_ALIGNED.csv`. Do not change script or turn 102 visual intentions into 102 unapproved generated images.
5. Fill real trim in/out for S01/P003 S04/P023 S05/P027 S07/P043 in `11_SHORTS_CUT_MAP.csv` and verify finished 9:16 videos plus CTA/end frames <=30s each (final export durations may remain future HOLD until edited). One continuous longform audio extract per Short; no independently rewritten voice.
6. Only if human Stage09/10 review and G11 actual aligned scene QC pass, update manifest locks and Stage11 current status, `STATE.md`, `VERSION_LOG.md`, `QA_LEDGER.csv` in atomic commit. No changes to legal claims or V5 narration without reopening Stage07. Stage16 remains separate publication release gate.

## Truth table

- Text integrity 51/51 / four Short parent IDs: **PASS structural**.
- Exact editor-planning frame continuity on **modeled** timeline: **PASS model only**, NOT audio alignment.
- Approved Harrison human hearing / pronunciation / audible joins: **HOLD**.
- Real audio timestamps for 51 scenes / Shorts: **HOLD**.
- Final four <=30.0s full exports: **HOLD**.
- G11 full runtime source-audio coverage: **NOT PROVEN**.
