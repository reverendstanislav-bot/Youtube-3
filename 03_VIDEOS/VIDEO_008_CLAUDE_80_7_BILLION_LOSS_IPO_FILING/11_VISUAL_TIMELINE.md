# VIDEO 008 — Stage 11 Audio-Aligned Visual Timeline

Status: **PASS — RESOLVE ASSEMBLY V1 STRUCTURALLY COMPLETE; SAVE/VISUAL/REAL-TIME AV REVIEW HOLD**

- Locked Harrison master: `VIDEO008_HARRISON_V5_MASTER_24K_MONO_S16.wav`
- Runtime: **987.800 s** / **00:16:27:20** at 25 fps
- Paragraphs: **50**
- Visual scenes: **110**, continuous from frame 0 through 24695
- ASR: Faster-Whisper base, CPU int8, English, beam 5, word timestamps, VAD off
- Canonical-to-ASR exact token matches: **2463/2695 (91.4%)**
- Minimum paragraph match ratio: **71.0%**
- Locked Shorts within their export cap: **4/4**

ASR is timing evidence only. It did not change, normalize, shorten, or rewrite the locked narration. Scene boundaries are proportional subdivisions of each audio-aligned paragraph, snapped to whole 25 fps frames with no gaps or overlaps.

## Resolve assembly rules

- A1: owner-accepted Harrison master, unchanged.
- V1: one active visual per scene from `VIDEO008_FINAL_VISUAL_PACK`.
- No subtitles, music, SFX, speed change, pitch change, or audio normalization in this assembly pass.
- SC043 uses a clearly contextual neutral graphic fallback; it must not be presented as authentic Broadcom evidence.
- SC106 may use the passed SEC lease crop only; the missing Broadcom juxtaposition remains a sourcing HOLD.

## Resolve V1 readback

- Project/timeline: `YT3 VID8` / `VIDEO008_ASSEMBLY_V1_25FPS`.
- 110 canonical scenes plus 12 one-frame last-frame holds at mixed-fps rounding boundaries.
- A1 and V1 span exactly 24695 frames.
- Gap/overlap detection: 0/0.
- Project save after final QC and processed-frame review are pending bridge restart; no final render was started.

## Stage11 verification and Shorts corrections — 2026-10-28

Verified existing Faster-Whisper timing data against the locked 987.800-second master SHA256 5cf8cf37bb728e8a50456b08240824eca4a8d03583626519396eca0258a7ad72. No redundant ASR or TTS was run. 2576 raw ASR word timestamps; all 50 canonical paragraphs and 110 scenes cover frames0–24695 continuously at25fps. Existing downstream project/stage state is preserved; this verification did not call Resolve.

Corrected SH01 start to frame3334 /133.36s: the previous133.76s cut clipped the first word Four (ASR digit4 at133.66–133.96s). SH04 now starts atframe15812 /632.48s, before Anthropic onset632.80s. SH02/SH03 ranges unchanged. Including a PLANNED 3-second canonical Shorts CTA, total durations are20.16 /20.60 /22.76 /22.88 seconds. These are audio-cut plus tail budgets, NOT rendered Shorts measurements.

Independent Stage11 timing review passed with explicit ASR limitations:10 paragraphs below85% exact lexical matching and2 zero-duration ASR word points (306.10s and484.86s) are flagged; these do not establish narration errors. Original ASR words retained; canonical narration/audio unchanged. Existing scene boundaries remain paragraph-anchored weighted visual planning subdivisions, not phoneme-accurate audio cuts. P008 andP049 visual-boundary caveats are recorded. Use11_SHORTS_CUT_MAP.csv for extracting audio, not visual allocation boundaries.

Files:11_ASR_WORD_TIMINGS.csv,11_TRANSCRIPT_ASR_ALIGNED.csv,11_SCENE_WORD_ANCHORS.csv,11_STAGE11_QC.json,11_STAGE11_INDEPENDENT_QC.md. No final render or new stage advancement performed.
