# VIDEO007 — Version Log

| Date | Stage | Version | Change | Result |
|---|---|---|---|---|
| 2026-10-19 | Stage07–08 | Script Lock / Voice Text | Owner-accepted R3 locked as 60 paragraphs and 2,517 words; five exact narration segments and four native Shorts prepared without audio. Source commit `cd3f20d89e614646747f834e16eea58dd5de4435`. | Stage07 PASS; Stage08 PASS; Stage09 NOT_STARTED |
| 2026-10-21 | Stage09 preparation | Harrison Voicebox plan | Independently rechecked 60/60 paragraphs, five exact segments and 4/4 Short locations. Selected local Voicebox Qwen3-TTS 1.7B Base candidate route: five sequential jobs, seed 20261021, $0/0 provider credits. Added identity/pronunciation/text/technical/Short QC plans and repaired VIDEO_INDEX omission. | READY_FOR_OWNER_GENERATION_APPROVAL; no TTS/audio; Stage10 NOT_STARTED |
| 2026-10-22 | Stage09 generation + Stage10 master | QWEN17_TECH_PASS | Generated all five locked segments sequentially with local Harrison/Qwen3-TTS 1.7B/CUDA/seed 20261021; 971.88s source audio, zero retries and $0 provider cost. Five decode/hash/ASR checks PASS. Built 972.36s 48k mono master at -16.1 LUFS/-1.5 dBTP with four 120ms chapter pauses. | STAGE09_TECH_PASS_HUMAN_A_B_HOLD; STAGE10_MASTER_TECH_PASS_AUDITORY_HOLD; STAGE11_NOT_STARTED |
