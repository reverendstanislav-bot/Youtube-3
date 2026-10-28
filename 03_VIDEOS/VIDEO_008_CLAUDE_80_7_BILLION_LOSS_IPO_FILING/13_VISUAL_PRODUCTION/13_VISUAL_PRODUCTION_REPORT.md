# VIDEO008 — Full Asset Download and Visual Production Report

Date: 2026-10-27

Plan authority: current 110-scene plan only; superseded 200-scene plans were not used.

Formal pipeline stage: **08 remains current**. This package is not audio-synchronized and does not claim Stage11–15 completion.

## Delivered inventory

| Class | Planned | Materialized | Technical result |
|---|---:|---:|---|
| Stock video | 40 | 40 | 40/40 unique files; ffprobe + full ffmpeg decode PASS |
| Stock photos | 25 | 25 | 20 active assignments plus 5 retained fallbacks; all crops PASS |
| Authentic evidence | 24 | 23 crops | 22 full PASS; SC106 partial PASS/HOLD; SC043 HOLD |
| Remotion graphics | 21 | 21 | 21/21 PNG 1920×1080 PASS; editable sources included |
| Generated replacement stills | 5 | 5 | 5/5 normalized to 1920×1080 and visual QC PASS |
| Total scene rows | 110 | 109 files / 110 manifest rows | 108 full PASS, 1 partial/HOLD, 1 HOLD |

## Rights and provenance

Every stock row records the Pexels landing page, direct asset URL, source, Pexels License, technical metadata and SHA-256. The [Pexels License](https://www.pexels.com/license/) and [commercial-use guidance](https://help.pexels.com/hc/en-us/articles/360042295214-Can-I-use-the-photos-and-videos-for-a-commercial-project) were checked. This does not waive trademark, privacy, endorsement, contextual-use or final Stage16 review requirements.

Document crops use actual downloaded SEC/issuer pixels with a local yellow outline only. No synthetic SEC page, reconstructed filing, invented signature or fake quote was created.

## Holds

- `SC043`: official Broadcom infographic/source endpoint returned Access Denied. Rejected denial pages were deleted; no substitute was presented as Broadcom evidence.
- `SC106`: SEC ~$125.2B lease crop is authentic and passed. Required Broadcom-side juxtaposition remains HOLD for the same source-access reason.
- `SC023`, `SC047`, `SC079`, `SC096`, `SC110`: owner-authorized conceptual replacements were generated on 2026-10-28. Original stock assignments remain packaged as fallbacks. The built-in tool did not expose per-image credit accounting, so no numeric cost claim is made.

## Archives

- `VIDEO008_SOURCE_ARCHIVE.zip` — 849,021,568 bytes — SHA-256 `0D96E76793E4E88C581368B8DA9AA96B206425035838D04E277F09AA06948CC3`
- `VIDEO008_FINAL_VISUAL_PACK.zip` — 833,356,031 bytes — SHA-256 `A036C4BE2A478DB8DE35FBBFBB000FA67049FC356F75E2BEF5FAC56BAB602D1A`
- Both archives passed `ZipFile.testzip()`.
- Release: `video008-visual-assets-20261027`.

## Boundary

The assets are visually planned but not aligned to Harrison audio. Stage09/10 audio lock and Stage11 word timing must precede a canonical edit timeline. Final rights/legal refresh remains mandatory at Stage16.
