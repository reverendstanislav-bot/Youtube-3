# VIDEO 002 — Stage 15C motion edit result

- Script: `15C_BUILD_MOTION.py` (inputs: `15_FINAL_FRAMES_1080P/`, Harrison master, 15B `.ass` captions)
- Motion: per-beat cosine-eased push-in / pull-out / lateral / vertical drift, zoom 1.00–1.10, rendered from a 4K upscale
- Transitions: 0.5 s cross-dissolve on every cut; 0.9 s dip-to-black at 12 chapter changes; all centred on the locked cut times (narration sync unchanged)
- Audio: voice only (no music / SFX), AAC 192k 48 kHz
- Output (outside Git): `WhatItCost_media/002-adobe-figma/15C_MOTION/VIDEO_002_STAGE15C_REVIEW_V1_1080P25.mp4`
  - 1920×1080, 25 fps, H.264 CRF 18, 940.600 s, 633,708,433 bytes
  - SHA-256 `03bda993b0e7d53fa3210603f973a51651482b062fdcb400b81e15a4682d3a39`
- QC stills: dissolve at 89.96 s, chapter dip at 131.12 s, F059 "NO FINAL DECISION" at 496 s — PASS
- Gate: owner visual review pending

## V2 (owner: "unnatural shaking", "zooms cut text")
- Cause: ffmpeg zoompan snaps the crop window to whole pixels -> per-frame jitter; lateral drift + 10 % zoom cropped headlines (e.g. F016)
- Fix: centred push-in / pull-out only, max 3 % (<= 29 px per side), rendered per frame with sub-pixel bicubic affine (PIL); no lateral drift
- Output: `VIDEO_002_STAGE15C_REVIEW_V2_1080P25.mp4`, 940.600 s, 851,990,062 bytes, SHA-256 `c38dfa33845bf5e2895444f67a5a3927d9229df951f6618e85d0a5f90d64d3a9`
- Smoothness QC: frame-difference curve monotonic, no jitter spikes; V1 superseded
