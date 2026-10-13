# VIDEO004 — Actual full MP4 render + technical QC (2026-10-12 user local date)

## Actual output: exists and decoded PASS

**Actual rendered MP4** delivered as conversation file: `VIDEO004_WHAT_IT_COST_R8_MASTER_1080P25.mp4`.

| Property | Verified |
|---|---|
| Source picture | User-uploaded `VIDEO004_MASTER60_R8.rar` (60 distinct GF001–GF060 PNG images), NOT prior rejected 61 chat candidates |
| Canonical montage | 84 sequential image placements from Git V5/V6, with seven restrained per-shot detail pushes, no generic wipes |
| Film length | 828.000 seconds (13:48), 20700/20700 frames |
| Picture | 1920x1080, 25/1 fps, H.264 High, Rec.709 VUI primaries/transfer/matrix |
| Narration | Original Harrison V11 WAV SHA256 `8c11be2619a6a84b7e1a6cbe0cb8c708d72dff556d1d737dd46f596ea21f65d7`, AAC 192kbit, 48 kHz stereo |
| Titles | Image-native R8 text; no duplicate editorial headings generated |
| Subtitles | Burned English ASS, white with orange current-word highlight based on existing word-level transcript (1951 ASR words; about 1922 distinct nonzero-duration highlight events), single line at bottom; optional separate `VIDEO004_WHAT_IT_COST_R8_EN.srt` (370 phrase cues) |
| Ending | GF060 endscreen last 500 frames = 20s; audio silence after ~808 seconds verified |
| File bytes | 77374261 |
| MP4 SHA256 | `cd4000ca99ae09305235cf6fde9910ccd258531ac392c49257e3c7fe519e7f7c` |

## Actual QC evidence

- First one-shot mux attempt failed at 19766 frames and was REJECT, not delivered.
- Subsequent in-memory mux attempt was killed by buffer growth around 12:37 and was REJECT, not delivered.
- Fixed by **three frame-exact independently encoded video sections**, for video-only output: 7289 + 7034 + 6377 frames. Each part validated via ffprobe.
- Lossless H264 **stream copy** merge: 20700 verified frames. Original audio encoded once only during final mux, with 20s silence tail.
- Final `ffprobe`: video frame count 20700, all streams and container 828.000s, 1920x1080 25fps Rec.709, audio 48000Hz stereo.
- Full finished MP4 decoded with FFmpeg `-xerror` including video and audio: exit 0, no decoding errors, 19.92s wall time on test container.
- Nineteen source-diverse frame snapshots checked by contact sheet; full continuous human film aesthetic QC and exact phoneme-level SRT accuracy are **not** claimed.
- Last 20 seconds verified via `silencedetect=-45dB` after audio time 808.
- Receipt `VIDEO004_MASTER_QC_RECEIPT.json` with SHA and measured technical metadata in the ChatGPT conversation files.

## Important limitations / Git

- **Binary MP4 was created in the ChatGPT session container and supplied through a sandbox link, not uploaded to GitHub**. Do not assert otherwise.
- **DaVinci Resolve was not installed on this host**. The completed MP4 is a **programmatically rendered canonical 84-placement conform with 7 local accents**, not a DaVinci Resolve runtime-rendered project. It must not be represented as verified Resolve-native Fusion choreography.
- No independent real-time full-film editorial QC, final legal/source-pixel rights clearance, human audio listening, or YouTube Studio end-element overlay validation was performed. TECHNICAL_VIDEO_PASS is not full RELEASE_PASS.
- No new AI image/video generation, no paid Higgsfield jobs, no music/SFX additions and no publishing actions.
