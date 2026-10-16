# VIDEO 005 - Edit-ready picture package

This package contains the verified 110-frame picture sequence for DaVinci assembly.

## Exact picture composition

- 60 `EDITOR_GRAPHIC`: the designed GFX composition is the complete picture frame.
- 37 `AUTHENTIC_SOURCE`: authentic source crops with intentional editorial labels or legal disclaimers.
- 10 `GENERATED_ILLUSTRATION`: clean generated images; only center resize/crop was applied. No added GFX covers them.
- 3 `LICENSED_OR_USABLE_CONTEXT`: context photography with factual non-event labels.

Every deliverable is a self-contained 1920x1080 PNG. No DaVinci/Fusion overlay is required to reveal or complete a frame. No final DaVinci montage or motion treatment is represented as complete.

## Files

- `PICTURE_SEQUENCE.csv`: canonical order and exact 25 fps in/out frames.
- `FRAME_AUDIT.csv`: class, source path, SHA256, and treatment for every frame.
- `GENERATED_ILLUSTRATION_AUDIT.json`: original-vs-master comparison for all 10 generated illustrations.
- `TECHNICAL_QC.json`: 110-frame technical gate.
- `CONTACT_SHEET_ALL_110.jpg`: single visual overview.
- `AUDIO_REFERENCE.txt`: local locked narration path and hash.
- `TIMELINE_CHUNKS/`: seven linked FCP7 XML chunks totaling 110 assets.

## Safe DaVinci import

Import the seven XML chunks one at a time in numeric order. Do not import the former full 110-file XML through the MCP bridge; that path repeatedly stalled Resolve and has been removed from the package. The chunks only establish exact still durations. Motion, transitions, emphasis, and final playback QC remain separate editing work.

## Gates

- Picture assets: `PASS_FOR_EDIT`.
- Generated illustrations unobscured: `PASS_RESIZE_CROP_ONLY_NO_ADDED_GFX` (10/10).
- Authentic-source release rights: `HOLD_CASE_BY_CASE` (37 assets).
- Motion/readability/final render: pending DaVinci edit and review.
