# VIDEO 001 — YouTube CC positioning addendum

Status: **READY FOR UNLISTED PLATFORM TEST**
Date: **2026-09-25**

## Goal
Keep the existing WHAT IT COST burned-in captions at the **very bottom** of the video, unchanged.

When a viewer enables YouTube captions / Auto-translate, the platform caption track should target a position **above** the burned-in captions.

## File
`18_YOUTUBE_ENGLISH_CC_POSITIONED.vtt`

- source: canonical `11_CAPTIONS.srt`
- cues: **409**
- language: English (United States)
- WebVTT positioning on every cue:
  - `line:78%`
  - `position:50%`
  - `align:center`
  - `size:88%`

## Upload instruction
Upload `18_YOUTUBE_ENGLISH_CC_POSITIONED.vtt` as the English caption track.

Do **not** move or remove the burned-in channel captions in the MP4.

Before public release, upload the video as **Unlisted** and verify:
1. desktop browser;
2. mobile app;
3. English CC;
4. Auto-translate to at least one non-English language.

## Platform limitation
YouTube Help currently states that WebVTT positioning is supported, but YouTube describes WebVTT as an initial implementation. Rendering may differ by client/device, so the exact relative position of an Auto-translated track must be checked in the real player.

This addendum does not modify the release MP4.
Stage18 remains **PASS / RELEASE_READY**, with a platform-positioning test recommended before public release.

## Stage18 V2 archive
`VIDEO_001_STAGE18_FINAL_UPLOAD_PACKAGE_V2_CC_POSITIONED.zip`

SHA-256:
`4c21eca671c99e7db4dce1f7c6070315166bc538336114d167492a7d8fad6530`
