# VIDEO 002 — 1080p Frame Export Repair

The previous picture-assembly normalization used Pillow `thumbnail()`, which never enlarges a smaller source. A 960×540 recovery preview therefore remained 960×540 and was centered on a 1920×1080 black canvas, producing the inset frame shown in review.

This is a build bug, not an intended visual treatment.

Repair:
- replace `thumbnail()+black canvas` with `ImageOps.fit(..., 1920×1080)`;
- export every locked F001–F110 frame as an individual 1920×1080 JPEG;
- commit those 110 files into `15_FINAL_FRAMES_1080P/`;
- preserve a source-resolution manifest so preview-backed upscales are not misrepresented as native originals.

No image generation is used for this repair.
