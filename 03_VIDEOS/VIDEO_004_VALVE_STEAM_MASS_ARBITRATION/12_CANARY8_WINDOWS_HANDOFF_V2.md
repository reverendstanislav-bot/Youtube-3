# VIDEO004 — Eight-shot real Resolve canary handoff (v2 repair)

Date: 2026-10-10.

**Current status: ACTUAL_IMPORT_AND_TECH_RENDER_PASS / CONTACT_SHEET_VISUAL_FAIL / FULL175_HOLD. See12_CANARY8_ACTUAL_RESULT_20261010.md. The preparation notes below are historical.**

## What was corrected before Windows import

1. Legacy Fusion .setting output from `12_BUILD_EDITABLE_FUSION_PACKAGE.py` encoded TextPlus StyledText as nested StyledText metadata rather than a straightforward string. Generator fixed for all future builds; **do not automatically rebuild or accept all 175 before the eight-shot real canary**.
2. Legacy importer uses an editor still image as long timeline media. Canary uses a technical 30s 1920×1080 25fps neutral MP4 source so each first-eight clip has sufficient sample frames; this is not a finished visual/render.
3. Legacy importer passed zero-based story frames directly into Resolve `recordFrame`. Actual Resolve defaults its timeline origin to an hour offset (e.g. 90000 at 25fps); canary uses `timeline.GetStartFrame()+relative_start` and compares the recorded absolute start/end.
4. Legacy project naming overwrote or loaded fixed review names. Canary creates unique `VIDEO004_CANARY8_<timestamp>_<suffix>` and refuses collisions.

## Actual reproducible local build

Canary package name: `VIDEO004_CANARY8_REPAIRED.zip`.
SHA256 **d290803a4f6d2ff3f3fb73a0c5966d92867845005b4844b5b60ef16c40c5a8d3**.
Exact ZIP successfully decompressed in technical container; 23 files, 8 .comp + 8 .setting, 1 H.264 neutral base, 1 source-derived Harrison FLAC at 30.600s, manifest, Python canary importer, PowerShell + Windows batch launcher and Russian guide.

Eight shots:
- SH-001 000–130
- SH-002 130–226
- SH-003 226–322
- SH-004 322–397
- SH-005 397–472
- SH-006 472–539
- SH-007 539–652
- SH-008 652–765
Total **765 frames / 30.600s @ 25fps**.

Embedded Harrison excerpt checksum `54d74f990c46c716f63311190e426634845afa322bf7c30033cf6b5d69666510`, lossless FLAC decoded from actual master WAV SHA `8c11be2619a6a84b7e1a6cbe0cb8c708d72dff556d1d737dd46f596ea21f65d7`.

Video plate SHA256 `7e80414890df36a28426c54c0bf687f6b0520822576199e79a10c27ac5035733`.

Static checks PASS: 8 contiguous intervals, Fusion source-graph references resolved, corrected TextPlus StyledText string type, balanced graph structure, exact media hashes/codec/fps, ZIP checksum and decompression.

A simulated Resolve API test with a nonzero timeline origin (90000) completed eight trial imports and mock project export. **Simulation DOES NOT equal Resolve runtime, fusion tool parse or graphical render.** No true DaVinci project .drp or video export exists in this execution environment.

## Windows user action to complete actual canary

1. Unzip the entire package on the Windows machine running DaVinci Resolve.
2. Double-click `RUN_CANARY8_WINDOWS.cmd`. The launcher starts Resolve if necessary, runs static checks, then uses the Resolve Python scripting API to create a **new** canary project. Python3 and local Resolve scripting must be available.
3. Check the project in Resolve in real-time for full 30.6 seconds. Verify seven boundaries, heading/source context, no black bands, 1920×1080@25fps, safe captions area and synced voice. **No automatic PASS for mere import**.
4. Bring back `Logs/CANARY_RESULT_*.json` and real-time preview/render for independent QC. Failures must be fixed in only the affected shots. Do not build/rewrite all175 on a canary defect.

## Production gate

- FULL_175_IMPORT = **NOT AUTHORIZED BY QC** until actual eight-shot Resolve import and real-time motion review pass.
- STAGE10_11_AUDITORY_LOCK = **FALSE**, human/full listening and 4 Shorts cut edges still pending.
- STAGE12_REAL_RESOLVE_IMPORT = **NOT_RUN**.
- VIDEO004_RELEASE_READY = FALSE.
- No paid generations, no video AI work or retries.

The current project environment has only Linux terminal and no access to the user's installed Windows Resolve; actual program execution cannot be faked.
