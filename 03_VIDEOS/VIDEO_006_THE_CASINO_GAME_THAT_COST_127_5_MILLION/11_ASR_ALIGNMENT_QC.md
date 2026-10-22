# VIDEO006 — Stage11 transcript + visual timeline (ASR anchored)

**2026-10-22. Stage09–10: owner ACCEPTED final audio QC; no regeneration. Stage11: PASS_REAL_ASR_PARAGRAPH_ANCHORS / SHORTS EXPORT STILL PENDING.**

## Real audio used

- Master: `VIDEO006_HARRISON_STAGE10_AUDIO_MASTER_48K_MONO.wav`; **10:53.130**, 48k PCM mono, matching locked release SHA-256 `a42c0e6245d66f4da25b5528bec04047b9e7f7ebf759e412e6490d627cf8d308`.
- The exact released WAV was downloaded independently into an audio-capable media sandbox, verified by SHA-256 and decoded; Faster-Whisper **small.en**, 8 CPU threads, int8, English, beam_size=5, word_timestamps=True, VAD filter off was applied to the **real 653.13s master**. ASR produced **1,716 normalized tokens**, aligned against **1,706 canonical V5 tokens** with difflib SequenceMatcher (autojunk=False). **1,660 canonical tokens exact matched = 97.30%**, with script/token normalization differences. This is an independent automatic transcript comparison, not a claimed human pronunciation audit.
- All **51 canonical paragraphs** have a FIRST and LAST script-token matched ASR anchor in correct order; each row records actual audible-word start/end, token-match fraction and 25fps continuous picture-grid edges.
- SRT: `11_PARAGRAPH_TRANSCRIPT_ASR_DRAFT.srt` — 51 paragraph cues using first-to-last ASR-aligned words. Not YouTube-ready short caption layout or word-highlighting captions; separate final caption segmentation later.
- Editorial plan: `11_VISUAL_TIMELINE.csv` = 51 scenes, 102 proposed A/B visual placements, all 51 factual claim/source links carried across, exact output **16,329 frames at 25fps**. Scene edges are midpoints of adjacent ASR paragraph speech anchors so pauses belong to a contiguous picture scene rather than imaginary silent content; **ZERO gaps/overlaps**. No licensed assets or images yet.

## Four locked native Shorts — actual speech windows, not rendered exports

| Short | Paragraph | Real voice interval | Speech-only | Status |
|---|---|---|---:|---|
| S01 | P003 | 00:15.020–00:30.400 | 15.38s | ASR source located / needs final 9:16 cut QC |
| S04 | P023 | 04:29.140–04:46.620 | 17.48s | ASR source located / needs final 9:16 cut QC |
| S05 | P027 | 05:19.640–05:37.280 | 17.64s | ASR source located / needs final 9:16 cut QC |
| S07 | P043 | 08:40.520–08:59.780 | 19.26s | ASR source located / needs final 9:16 cut QC |

All four have **real ASR speech windows**. Do not combine distant excerpts, rewrite their words, or generate separate TTS. The later finished 9:16 clip INCLUDING intro/end card/CTA must measure **<=30.0 seconds**; final duration fields remain blank until actual rendered exports. Only 4 Shorts, no more.

## Boundary/word QC qualifications

The sequence-level match is 97.3%, *not* 100% speech proof. Most variation concerns ASR textual rendering of spelled-out dollar amounts, hyphenated terms, proper nouns and punctuation. These lower-scoring paragraphs need specific listening confirmation before subtitle-final or precise trim acceptance:

- P003 00:15.020–00:30.400: token match 82.6% (**native Short**), check numbers/qualifiers
- P038 07:35.700–07:46.760: token match 89.7%
- P045 09:17.980–09:31.860: token match 81.4%
- P046 09:32.320–09:51.160: token match 89.6%

The user explicitly accepted final Stage09/10 QC; record this as OWNER_APPROVED rather than falsely implying independent human Higgsfield Harrison A/B listening was newly done in this Stage11 computation. Audio master is unchanged. Remaining Stage11 acceptance is speech-to-text automation plus real aligned scene structure, not unmade renders. Stage16 AztecGold current-status and media rights refresh remains open.

## Visual and legal canon

Evidence from actual sources only; editor GFX must be distinguishable from original documents. WHAT IT COST original charcoal/paper-white/red system, restrained source-specific emphasis, no paper fake, courtroom kitsch, repetitive motion or superimposed black title blocks. No paid generative assets, music or SFX at Stage11. Primary corporate controversy resolved by contract, not a jury finding; $127.5m paid does not represent a criminal fine, the accounting $128m is not a second payment, court injunction vacation is separate from contractual restrictions, investor case is distinct from original corporate settlement.

**Decision:** Stage11 transcript/timeline PASS_ASR_SOURCE_ANCHORED, with lower-confidence phoneme/name watch items and Shorts export length HOLD. Stage12 visual sourcing/production planning can begin upon next owner instruction; Stage16 legal refresh still mandatory before publication.
