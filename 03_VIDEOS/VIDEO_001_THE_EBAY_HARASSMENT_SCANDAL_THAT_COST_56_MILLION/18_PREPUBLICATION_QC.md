# VIDEO 001 — 18 Prepublication QC

Status: **PASS / RELEASE_READY**
Date: **2026-09-25**

## Final upload master
Canonical release file is byte-identical to the owner-approved Stage15B voice-only master.

- release filename: `VIDEO_001_UPLOAD_MASTER_1080P.mp4`
- canonical source: Stage15B artifact `10817420859`
- original file: `VIDEO_001_STAGE15B_REVIEW_V1_1080P.mp4`
- re-encoded in Stage18: **NO**
- SHA-256: `a4626fed53d09e69cbc59e089f5490695ea7f5243dcec0f41bf7fed72156cf33`
- H.264 / 1920×1080 / yuv420p
- CFR: 25 fps
- runtime: **957.370 sec**
- locked runtime delta: **−0.044 sec**

## Video QC
- black-frame detector: **0 black events >0.15 sec**
- dense 40-frame contact-sheet review: PASS
- long still/freeze detections correspond to the intentional held-still editorial construction and are not playback freezes
- no missing sampled section found
- no re-render introduced

## Audio QC
- AAC / 44.1 kHz / mono
- canonical content: **Harrison narration only**
- music: **NONE**
- SFX: **NONE**
- ambience: **NONE**
- integrated loudness: **−16.9 LUFS**
- true peak: **−1.1 dBFS**
- LRA: **2.3 LU**
- 11 natural narration pauses >1 sec; no long accidental mute detected

## Captions / overlays
Approved burned-in Stage15B caption/overlay layer retained.

- 409 authored caption cues
- 2151 word-highlight events
- 0 fallback cues
- base: `#EDEDED`
- active word: `#D32222`
- forbidden `100,100)}` artifact: ABSENT
- known `i n` split: FIXED
- source/legal/reconstruction overlays retained
- GPS attempt / installation-not-established distinction retained
- DPA / conviction distinction retained
- surviving claim / liability distinction retained
- no positive `$58.7M award` claim

A clean optional upload SRT was deterministically reconstructed from the approved ASS:
- `VIDEO_001_CAPTIONS_UPLOAD.srt`
- 409 cues
- SHA-256 `036bf7b63daaf1e0c9e2683caed577f7f9f2e109a000ba65dd3851c5b49cce6e`

## Thumbnail
Owner-approved Stage17 master verified byte-for-byte.

- canonical master: 1672×941 PNG
- SHA-256: `0686bb5c0476b355a179ef2a93f548c3da48bdaade0d518f7a674bab83c519f2`
- upload derivative: 1280×720 JPG, same composition/content
- upload JPG SHA-256: `12fb6a088e2fe997615f9f65263a36917c97bd539d3ca13deb10af35f9cd918c`

## Metadata
- title: **The eBay Harassment Scandal That Cost $56 Million**
- title length: 49 / 100
- description length: 2711 / 5000
- manual chapters: 12
- mandatory CC BY-SA credits: 2 / 2 present
- altered/synthetic-content disclosure: **YES**
- audience: **Not made for kids**
- paid promotion: **No**
- license: **Standard YouTube License**
- language: **English (United States)**
- category: **Education**

## Source-link refresh
Checked 2026-09-25:
- DOJ eBay case page: reachable
- GovInfo summary-judgment PDF: reachable
- eBay final settlement statement: reachable
- Reuters final settlement article: current/discoverable

Known DOJ overview date typo (`January 2023`) remains documented; the official Jan. 11, 2024 release/DPA/docket remain controlling. No film change required.

## Legal packaging gate
PASS:
- `$56M` is ordinary rounding of the **$55.7M civil settlement package**
- separate **$3M DPA penalty** is not added to the civil package
- no judgment/award implication
- no jury-verdict implication
- no eBay-only `$56M` payment implication

## Stage18 archive
Archive:
`VIDEO_001_STAGE18_FINAL_UPLOAD_PACKAGE.zip`

Size:
**215,775,061 bytes**

SHA-256:
`457ddb685c0b0b487a0639b82600d4a7af81bf8ed29cffbd08c41e881d62551e`

The archive contains the exact MP4 master, canonical thumbnail master, YouTube-ready thumbnail JPG, upload SRT, title, description, chapters, tags, settings, rights/credits, legal guardrails, QC report, contact sheet and per-file checksums.

## Gate
**G18 PREPUBLICATION: PASS**
**VIDEO 001: RELEASE_READY**

YouTube upload/publication has **NOT** been performed.
Do not start Stage19 until the video is actually published.
