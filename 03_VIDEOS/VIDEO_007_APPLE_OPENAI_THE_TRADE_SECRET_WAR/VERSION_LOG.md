# VIDEO007 — Version Log

| Date | Stage | Version | Change | Result |
|---|---|---|---|---|
| 2026-10-19 | Stage07–08 | Script Lock / Voice Text | Owner-accepted R3 locked as 60 paragraphs and 2,517 words; five exact narration segments and four native Shorts prepared without audio. Source commit `cd3f20d89e614646747f834e16eea58dd5de4435`. | Stage07 PASS; Stage08 PASS; Stage09 NOT_STARTED |
| 2026-10-21 | Stage09 preparation | Harrison Voicebox plan | Independently rechecked 60/60 paragraphs, five exact segments and 4/4 Short locations. Selected local Voicebox Qwen3-TTS 1.7B Base candidate route: five sequential jobs, seed 20261021, $0/0 provider credits. Added identity/pronunciation/text/technical/Short QC plans and repaired VIDEO_INDEX omission. | READY_FOR_OWNER_GENERATION_APPROVAL; no TTS/audio; Stage10 NOT_STARTED |
| 2026-10-22 | Stage09 generation + Stage10 master | QWEN17_TECH_PASS | Generated all five locked segments sequentially with local Harrison/Qwen3-TTS 1.7B/CUDA/seed 20261021; 971.88s source audio, zero retries and $0 provider cost. Five decode/hash/ASR checks PASS. Built 972.36s 48k mono master at -16.1 LUFS/-1.5 dBTP with four 120ms chapter pauses. | STAGE09_TECH_PASS_HUMAN_A_B_HOLD; STAGE10_MASTER_TECH_PASS_AUDITORY_HOLD; STAGE11_NOT_STARTED |
| 2026-10-22 | Stage09–11 | OWNER_AUDIO_LOCK_AND_ASR_TIMELINE | Owner accepted Harrison/master. Aligned 60/60 paragraphs to real word timestamps at 97.71% exact normalized token match; created continuous 24309-frame/25fps visual timeline, paragraph SRT and four real master Short ranges of 23.00–25.04s. | STAGE09 PASS; STAGE10 PASS; STAGE11 PASS_ASR_SOURCE_ANCHORED; Stage12 NOT_STARTED |

| 2026-10-22 | Stage12 | Dense Picture Plan | Kept 60 semantic scenes as master source and authored 239 montage shots with exact 25fps cut planning, one-to-one acquisition/rights queue, authentic source vs contextual stock, 4 vertical Shorts and 6 canon patterns. | PASS_PLANNING_WITH_RIGHTS_HOLDS; no image/video/media acquired; Stage13 NOT STARTED |

| 2026-10-22 | Stage13 partial | 143 editable source SVGs | Created 143 per-shot source GFX files and checked primary ECF1/176/177 pages, 8 licensed stock video pages and 1 CC BY-SA still page. External binary source/media fetch blocked, actual PNG render visual QC pending. | PARTIAL: 143 SVG CREATED; 96 EXTERNAL HOLD; no Stage13 asset-lock PASS |

| 2026-10-22 | Stage13 independent visual critique | QC_REJECT_TEMPLATE | One 1920x1080 exported draft frame visually inspected; repetitive generic panels and raw production instructions failed premium documentary canon. Six bespoke replacements committed; 137 generic SVGs await redesign and render review. | Stage13 HOLD; 0/239 final assets approved |

| 2026-10-22 | Stage13 real-source acquisition and batch render | 6 PDFs, 5 MP4, 1 Commons JPEG, 6 page crops, 143 1080p PNG renders | Actual files in verified uploaded cloud ZIP incl per-file SHA256; missing 3 original MP4 candidates; art/legal QC of 137 generic/6 bespoke pending. | TECHNICAL ASSET ACQUISITION PARTIAL; STAGE13 QC HOLD |

| 2026-10-22 | Stage13 completion of real technical asset package | 239 decoded output media files | Source-native 79 court document shots from 9 PDFs, 143 original graphic outputs with 137 redone, 8 original editor substitutes for company press web pages, 1 Commons still, 8 25fps licensed-context MP4 trims. VP001 and VP205 crop repairs, 239/239 technical QC, archived with checksums. | PASS TECHNICAL ONLY; CREATIVE RIGHTS/QC HOLD |

| 2026-10-22 | Stage13R Rebuild map after owner rejection | REJECT_LEGACY_239 | Replaced old picture planning targets with 239 exact VP slot-level story and source records, 65 native video targets, 41 real ECF line crops, 125 bespoke graphics and 8 authentic stills. All original sources pending rights and picture rebuild. | PLAN PASS ONLY / Stage13 OWNER REJECT |
