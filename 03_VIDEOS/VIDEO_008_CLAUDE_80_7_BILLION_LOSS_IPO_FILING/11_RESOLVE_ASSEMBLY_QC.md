# VIDEO 008 — Resolve Assembly V1 QC

Date: 2026-10-28  
Project: `YT3 VID8`  
Timeline: `VIDEO008_ASSEMBLY_V1_25FPS`

## Verified structural state

- Timeline rate: **25 fps**.
- Timeline span: **24695 frames / 00:16:27:20 / 987.800 seconds**.
- A1: one unchanged `VIDEO008_HARRISON_V5_MASTER_24K_MONO_S16.wav`, frame 0 through 24695.
- V1: all **110 planned scenes** present in canonical order.
- Twelve mixed-source-frame-rate boundaries required a **one-frame hold of the previous real source frame**. These are gap fillers, not additional story scenes.
- Final Resolve readback: **0 gaps, 0 overlaps** across video and audio.
- Subtitle tracks: **0**.
- Music/SFX: **not added** in this assembly pass.
- Final render: **not started**.

## Asset handling

- Seventy-one still/photo/document/graphic scenes were encoded as exact-duration 1920x1080, 25 fps H.264 plates. Every plate passed frame-count, resolution, and frame-rate QC; see `11_RESOLVE_PLATE_MANIFEST.csv`.
- SC085 and SC087 source videos were shorter than their audio-aligned spans. Their exact 25 fps Resolve cuts retain all source motion and hold the last frame for the missing tail.
- SC043 uses SC040 only as a neutral contextual capital-stack graphic. It is **not** represented as authentic Broadcom evidence.
- SC106 uses the passed SEC crop only; the missing Broadcom juxtaposition remains a source HOLD.

## Timing QC

- Faster-Whisper base / CPU int8 / English / beam 5 / word timestamps / VAD off.
- ASR is timing evidence only; canonical narration remains `08_VOICE_SCRIPT_MASTER.txt`.
- Canonical exact token match: **91.39%**.
- Paragraphs aligned: **50/50**.
- Scenes aligned: **110/110**, continuous from frame 0 through 24695.
- Locked Shorts within 30-second cap: **4/4**.

## Remaining gate

The in-app Resolve bridge disconnected when a processed timeline-frame capture exceeded the 120-second tool timeout. The structural timeline readback above completed before that disconnect. Project save after the final QC, representative processed-frame inspection, and a full real-time audio/video review are therefore **not yet verified**. Do not call this a final edit or render until those checks pass.
