# VIDEO004 — Stage10 audio master verification

Status: TECHNICAL_PASS / AUDITORY_QC_PENDING. No full Stage10 PASS or audio lock.
Verified 2026-10-10. Owner authorized existing-master verification and Stage11 preparation; no new paid jobs submitted.

## Provenance and delivery

Existing Harrison V11 jobs A d72c01ce-3a67-4e9a-92b9-3333a609921c, B 7ad513f0-00a1-4360-b8bf-8faf1717a348, C 1216264c-c198-4667-91e4-7c0a38a6527a. Provider/model: Higgsfield text2speech_v2 / elevenlabs, locked Harrison preset573e5163-59b3-4926-aab1-951ef2985f81. Historical approved quoted budget39.45 credits; actual account debit not re-verified. Additional generation this task:0.

[Successful existing Actions run](https://github.com/reverendstanislav-bot/Youtube-3/actions/runs/38039673597), head67b940a, artifact11665053402 VIDEO004_HARRISON_V11_MASTER_AND_SOURCES. ZIP178117046 bytes, SHA256201f98a12b28c442f9bb3cbf178d26cbba910cb38e88a9253d5a818faf19754f verified before extraction.

Delivery: C:/YOUTUBE/Youtube 3/Video 4/VIDEO004_HARRISON_V11_MASTER.wav. Delivery-copy hash verified; this is narration under QC, not a finished video/upload package. Sources and QC cache kept outside the delivery root to avoid clutter.

| File | Bytes | SHA256 |
|---|---:|---|
| A.mp3 |4560396|ee327e7f553435ef380e0a55c1e5d301e5d2b9d345c53d35285e1de2568aa368|
| B.mp3 |4013706|343b066e0a2e3eb777f14cdbf7cc66a151691c6207bcaf78415a756305214dfd|
| C.mp3 |4356850|4fadf37e31ec5b633cbea51f10e9b407e0bfee9b77a1cb5ec175e0cfa6f3760e|
| Master.wav |232704102|8c11be2619a6a84b7e1a6cbe0cb8c708d72dff556d1d737dd46f596ea21f65d7|

## Completed technical checks

WAV pcm_s24le,48000Hz,2channels,24bits,38784000sampleframes,808.000000seconds (13:28). All three source MP3s and master fully decode with ffmpeg -v error -xerror. Every hash matches artifact SHA256SUMS. Peak measured by volumedetect:-3.8dBFS; mean:-19.6dBFS (not LUFS). No clipping suggested by measured peak; not an auditory click/noise PASS. Silence scan at-45dB/0.8s found321.223–322.087,768.878–769.722,780.201–781.091; pauses not automatically defects.

Decoded source lengths A284.960/B250.800/C272.240s. Actual seams284.960 and535.760s, not sums of MP3 container durations. Independent source/master PCM comparison confirms sequence and length;104sample differences across the entire stereo stream, max3339/8388608, sample correlation1.0. Different FFmpeg decoder/resampler versions mean not bit-identical decoded PCM; this is not a proved audible defect. Workflow contains no editorial audio edits.

24-bit WAV is a decoded working master from MP3; it does not restore information lost in source compression. Original narration is not retimed, normalized, truncated or padded.

## Semantic and auditory boundary

Full local small.en ASR yields1951word rows. Independent reviewer v08_precision: PASS_PROVENANCE / PASS_ASR_COVERAGE_WITH_REVIEW_FLAGS; substantive numbers, attribution, negations, preliminary/as-applied and conditional-appeal qualifications recognized. ASR is not proof of pronunciation, timbre or prosody. Eight lexical candidate anomalies require listening, not automatic edits/re-generation: purchased/purchase3.86s; however142.76s; cases197.60s; court226.16s; instance251.98s; question/questioned427.22s; defendants490.24s; missing stop about735s. A local medium.en region recheck is supplementary recognition, never a hearing claim.

Stage10 acceptance still requires genuine full listening for Harrison consistency, pronunciation, semantic fidelity, join noise and cadence. No auditory reviewer or PASS fabricated. Master and visual-timeline locks remain false. If audio changes, invalidate/rebuild Stage11 timing and Shorts ranges. Official legal-status refresh remains Stage16; no fresh case research asserted.

## Local second-model result

11_ASR_MEDIUM_RECHECK.json supports locked wording at all8candidate locations: purchased/question and stop recognized; five spurious insertions absent. stop measured734.880–735.120s. This supports recognizer-artifact interpretation, not an auditory PASS. Raw small.en kept unchanged. Independent preparation review and remaining lock criteria recorded in11_STAGE_QC.md.
