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
