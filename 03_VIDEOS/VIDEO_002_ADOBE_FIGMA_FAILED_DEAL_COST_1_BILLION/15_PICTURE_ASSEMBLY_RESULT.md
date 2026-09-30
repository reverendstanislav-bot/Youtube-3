# INVALIDATED — DO NOT USE THIS V1 MP4

The previously recorded Picture Assembly V1 is invalidated because the frame normalizer used Pillow `thumbnail()`, which never enlarges smaller inputs. This caused smaller frames to be centered inside a black 1920×1080 canvas.

The bug is fixed in `15_BUILD_PICTURE_ASSEMBLY.py`, and all 110 frames have been exported individually at 1920×1080 under `15_FINAL_FRAMES_1080P/`.

---

# VIDEO 002 — Stage 15 Picture Assembly V1 Result

Status: **PASS WITH RELEASE-RESOLUTION HOLD**

Date: 2026-09-30

## Deterministic assembly result

- Locked visual slots used: **110 / 110**
- Locked narration master: **Harrison Stage 10 master**
- Target runtime: **940.617 sec / 15:40.617**
- Container runtime: **940.600 sec**
- Resolution: **1920×1080**
- Frame rate: **25 fps**
- Video codec: **H.264**
- Audio codec: **AAC**
- Audio: **48 kHz / stereo / 192 kbps**
- Color metadata: **BT.709**
- File size: **190,700,575 bytes**
- SHA-256: `b3b6bf5e29964a4b231334fb738c57e6085c59694dc7ec991eab8d06db17b120`

## Persisted assembly candidate

- Higgsfield media ID: `942946e7-2b5d-4a39-b439-9777dee28f0b`
- URI: `https://d2ol7oe51mr4n9.cloudfront.net/user_3J3zfwu7kpgllQvPySWoLtXHwdR/942946e7-2b5d-4a39-b439-9777dee28f0b.mp4`
- Upload status: **UPLOADED**

## Source-resolution audit

Effective source classes in this assembly:

- latest retry full outputs: **16**
- other HTTP-backed locked outputs: **39**
- Git-relative canon assets: **15**
- recovery-preview sources: **36**
- chat/library recovery-preview sources: **4**

Therefore **40 / 110 frames** are currently sourced from **960×540 recovery-preview images** and were deterministically upscaled into the 1920×1080 picture assembly.

### Release-resolution hold

The assembly is valid for:
- full-film edit review;
- beat/timing review;
- narrative continuity review;
- audio/picture sync review;
- transition/caption planning.

It is **not yet a release-resolution master** because 40 locked PASS slots do not currently have full-resolution originals available to this deterministic build.

No visual generation was performed during this assembly stage.

## What is not yet integrated

This V1 is a **picture + locked narration assembly**. It does not yet close:
- final music / SFX;
- final captions;
- final overlay pass;
- final transition / motion polish;
- release-master QC.

## Gate to release master

Either:
1. recover/replace the 40 preview-backed slots with their full-resolution originals, preserving the same locked frame identity; or
2. owner explicitly accepts the 960×540-upscaled sources for release.

Until one of those happens, `edit_master` remains **false**.

---

# Picture Assembly V2 — 2026-09-30

Status: **BUILT / NO PREVIEW-BACKED SLOTS**

- R14–R16 replaced all 40 former 960×540 recovery-preview slots with 1344×752 GPT Image 2 frames (R14 33, R15 5, R16 2 with deterministic one-word text fixes). See `13_R14_PREVIEW40_QC.md`, `13_R15_RETRY_QC.md`, `13_R16_RESULTS.csv`.
- `15_FINAL_FRAMES_1080P/` updated for those 40 slots (ImageOps.fit → 1920×1080, JPEG q95 4:4:4); manifest updated. Source classes now: http 39, r14-regen 33, latest-retry 16, git-relative 15, r15-retry 5, r16 2. **recovery-preview: 0.**
- Note: all generated frames are native 1344×752 (git-relative canon 1672×941), so every slot is still upscaled to 1080p; none is a 960×540 preview any more.
- Build: same concat/timing as V1 from `11_VISUAL_TIMELINE.csv`, locked Harrison master (sha256 `6b0da92f…` verified).
- Output (local, not in Git): `WhatItCost_media/002-adobe-figma/15_ASSEMBLY_V2/VIDEO_002_ADOBE_FIGMA_PICTURE_ASSEMBLY_V2_1080P25.mp4`
  - 1920×1080 · 25 fps · H.264 + AAC 48 kHz stereo · 940.600 s · 89,097,788 bytes
  - SHA-256 `919e70f5ec1f859253215e3a79f498d8144cb90d1a225cefb0313fd15ee57b3e`
- Spot check of rendered frames (F001, F012, F037, F055, F088, F110): full-frame, no inset borders.
- Not integrated yet: captions, overlays, transitions, release-master QC.
