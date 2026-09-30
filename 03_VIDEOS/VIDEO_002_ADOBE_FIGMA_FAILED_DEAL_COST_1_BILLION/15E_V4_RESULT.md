# VIDEO 002 — Stage 15E (V4) result

Owner on V3: number graphics good but need to be smoother / more premium; base zoom in-out ruins it;
text punch-ins were great; still a slideshow, not a film. Script: `15E_BUILD_V4.py` (V2 / V3 untouched).

- Camera: constant-velocity push-in on every beat (0.35 %/s, <= ~4 %), no in/out alternation, no ease-to-stop at cuts
- Punch-ins (same 7 beats as V3): smootherstep over 1.2 s, then keep drifting forward
- Number cards: per-frame eased ASS events — plate fade, blur-to-sharp + 110 % -> 100 % settle + tracking close, ease-out-expo count-up, red rule grows from centre, label rises in late, soft exit
- Cut rhythm unchanged: 73 hard / 24 dissolve / 12 dip-to-black
- Output (outside Git): `WhatItCost_media/002-adobe-figma/15E_V4/VIDEO_002_STAGE15E_REVIEW_V4_1080P25.mp4`, 940.600 s, 963,364,444 bytes, SHA-256 `e9ba99d63559ec6cd700502032d6e3ea547044418c67b6566dc16c3f63762a2a`
- Smoothness QC (20–60 s): frame-difference median 0.56, p95 0.61, no stutter (zero-diff frames only inside a dip-to-black)
- Gate: owner visual review pending
