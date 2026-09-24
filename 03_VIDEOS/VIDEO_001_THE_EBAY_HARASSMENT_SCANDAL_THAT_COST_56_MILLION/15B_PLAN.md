# VIDEO 001 — Stage 15B Overlay + Captions Build

Status: **COMPLETE / TECHNICAL PASS / OWNER VISUAL REVIEW PENDING**
Date: 2026-09-24

## Scope
Stage 15B adds the documentary information layer to the approved Stage 15A picture assembly:

- source / date / legal-status metadata from `14_OVERLAY_MAP.csv`;
- mandatory `ILLUSTRATIVE RECONSTRUCTION` labels;
- word-level captions derived from `11_TRANSCRIPT_WORD_LEVEL.json`;
- white base captions with the currently spoken word highlighted orange;
- bottom caption-safe zone retained;
- music and SFX remain excluded until Stage 15C.

## Hard legal/factual locks
- attempted GPS installation must never become successful installation;
- DPA must not be presented as a conviction;
- surviving civil claim must not be presented as liability;
- Wenig / Jones / Wymer must not be presented as criminally charged over the campaign;
- first 2026 settlement remains failed/provisional;
- $55.7M remains the civil settlement package, not a judgment or eBay-only payment;
- $3M DPA and $55.7M civil package remain separate;
- no positive `$58.7M award` frame or overlay.

## Render
- source picture master: Stage 15A review master;
- Harrison Stage 10 master audio remains authoritative;
- render target: 1920×1080 / CFR 25 fps / H.264;
- captions + metadata burned for review;
- no music / SFX;
- no generation and no credits spent.

Build authority: `15B_BUILD.py`.
Workflow: `.github/workflows/video001_stage15b.yml`.

**Do not start Stage 15C automatically.**


## Stage 15B result — 2026-09-24
- Final workflow run: **36018740428** — SUCCESS.
- GitHub Actions artifact: **10817420859** — `VIDEO_001_STAGE15B_REVIEW_V1`.
- Review video: `VIDEO_001_STAGE15B_REVIEW_V1_1080P.mp4`.
- Video: **1920×1080 / H.264 / CFR 25 fps**.
- Audio: **AAC / 44.1 kHz / mono**.
- Measured runtime: **957.370 sec** vs locked **957.414 sec** (delta **−0.044 sec**).
- Video SHA-256: `a4626fed53d09e69cbc59e089f5490695ea7f5243dcec0f41bf7fed72156cf33`.
- Captions: **409 SRT cues / 2151 word-highlight events / 0 fallback cues**.
- Metadata overlays: **83 timed stacks** from the 115-row overlay map.
- Forbidden `100,100)}` caption artifact: **ABSENT**.
- Known `i n` split: **FIXED**.
- GPS / DPA / liability / reconstruction / no-$58.7M legal locks: **PRESENT**.
- B104 fallback inequality glyph: **covered and replaced deterministically**.
- Music/SFX: **NOT INCLUDED**.
- Stage 15B generation spend: **0 credits**.

## Gate
Stage 15B is complete as the caption + source/legal overlay review cut.
Stage 15C remains **NOT STARTED** until explicit owner approval after viewing this build.


## Caption palette correction — 2026-09-24
- Removed the legacy orange highlight inherited from older YouTube projects.
- WHAT IT COST caption palette is now locked to:
  - base text: **#EDEDED**
  - current spoken word: **#D32222**
  - outline / shadow: channel charcoal / black
- Final corrected workflow run: **36021465130 — SUCCESS**
- Final corrected artifact: **10817420859**
- Corrected review SHA-256: `a4626fed53d09e69cbc59e089f5490695ea7f5243dcec0f41bf7fed72156cf33`
