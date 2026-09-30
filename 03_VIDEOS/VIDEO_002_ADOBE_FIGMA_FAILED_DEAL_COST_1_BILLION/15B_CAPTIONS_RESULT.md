# VIDEO 002 — Stage 15B Captions Build

Status: **BUILT / TECHNICAL PASS / OWNER VISUAL REVIEW PENDING**
Date: 2026-09-30

## Scope
Same caption rules as VIDEO_001 Stage 15B, over Picture Assembly V2:
- word-level burned captions from `11_WORD_TRANSCRIPT.csv` (2,185 timed words);
- Montserrat ExtraBold 46, base `#EDEDED`, current spoken word `#D32222`, black outline, bottom-centre, MarginV 46 (inside the frames' calm bottom band);
- up to two lines per cue (≤42 chars per line, ≤64 per cue), new cue on sentence end or pause > 0.7 s;
- **no metadata overlay layer** — VIDEO_002 frames already carry baked headlines and source labels;
- **voice-only** audio (Harrison master, stream copied from V2): no music, no SFX — per the channel rule set in VIDEO_001 Stage 15C.

## Outputs
- `11_CAPTIONS.srt` — 313 cues (canonical caption text)
- `18_YOUTUBE_ENGLISH_CC_POSITIONED.vtt` — same cues, `line:78% position:50% align:center size:88%` (platform CC above the burned captions, as VIDEO_001)
- Review master (local, not in Git): `WhatItCost_media/002-adobe-figma/15B_CAPTIONS/VIDEO_002_STAGE15B_REVIEW_V1_1080P25.mp4`
  - 1920×1080 · 25 fps · H.264 CRF 18 + AAC 48 kHz stereo · 940.600 s · 108,102,109 bytes
  - SHA-256 `3ace86dfc417d817bf0059991b0d179a026fe18dad7eb7167c2ba7b8a892f082`
- Build authority: `15B_BUILD_CAPTIONS.py` (font from `WhatItCost_media/_fonts/Montserrat-ExtraBold.ttf`, OFL)

## QC
- words captioned: 2,185 / 2,185 · highlight events: 2,185 · cue overlaps: 0
- spot check of rendered stills (F001, F016, F027, F045, F059, F074, F085, F088, F100, F104, F110): captions legible, inside the bottom band, no collision with evidence.

## Gate
Owner review of the full review master. Not yet done: final master QC, packaging, thumbnail, upload package.
