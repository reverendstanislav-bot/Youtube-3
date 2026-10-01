# VIDEO 002 — 18 Upload Package

Status: **READY — upload/publish is a separate owner action**
Date: **2026-10-01**

Built in the channel-2 pack layout (DELIVERY / PUBLISHING / SHORTS).
Binaries live outside Git in `WhatItCost_media/002-adobe-figma/18_UPLOAD_PACK/`; text files are mirrored in `18_PUBLISHING/`.

## Canonical master
- filename: `DELIVERY/VIDEO_002_UPLOAD_MASTER_1080P.mp4`
- checksum: SHA-256 `ac1e3c39cf0fd996f8f2de2865146505d5acd9958020383bc25d9c5e4221c754`
- runtime/resolution: 15:40.600, 1920×1080, 25 fps, 23,515 frames, 2,530,613,593 bytes
- picture: 15F V5 (owner-fixed main cut); sound: 15G V6 (owner-approved)
- manifest + QC: `18_PUBLISHING/VIDEO_002_UPLOAD_MASTER_MANIFEST.json`, `VIDEO_002_UPLOAD_MASTER_QC.md`

## Packaging
- title: **Adobe Paid $1 Billion for a Deal That Never Happened** (owner-selected)
- thumbnail: concept 4, owner-selected — see `17_THUMBNAIL_FINAL_LOCK.md`
- description, 13 chapters, sources, credits: `18_PUBLISHING/YOUTUBE_DESCRIPTION.txt`
- pinned comment and tags: `18_PUBLISHING/YOUTUBE_METADATA.json`
- human upload sheet (RU): `18_PUBLISHING/ДАННЫЕ ДЛЯ ЗАГРУЗКИ.txt`
- playlist: not set

## Captions
- file: `PUBLISHING/VIDEO_002_CAPTIONS_EN.srt` (optional; captions are burned in)
- language: English

## Shorts
- 8 vertical 1080×1920 Shorts, one per locked section in `07_SHORTS_LOCK.csv` (contiguous, no rewrite): `SHORTS/VIDEO_002_SH01.mp4` … `SH08.mp4`, 53–99 s
- builder: `18_BUILD_SHORTS.py`; texts: `18_PUBLISHING/SHORTS_UPLOAD_TEXT_RU.txt`; manifest: `18_PUBLISHING/SHORTS_MANIFEST.json`

## Settings
- audience: not made for kids
- category: Education
- disclosure: altered/synthetic content = YES
- comments / embedding / scheduling: owner decision at upload

## Connections
- end screen, cards, next video: not prepared

## Checks
- Pack checksums: `18_PUBLISHING/SHA256SUMS_UPLOAD_PACKAGE.txt`
- Still open in Git: `16_COPYRIGHT_PROVENANCE_AUDIT.md`, `16_FINAL_FACT_LEGAL_REFRESH.md`, `17_PACKAGING_QC.md`, `18_PREPUBLICATION_QC.md` are NOT_STARTED templates. The pack does not replace them.
- Record processing/copyright/platform checks before Public.
