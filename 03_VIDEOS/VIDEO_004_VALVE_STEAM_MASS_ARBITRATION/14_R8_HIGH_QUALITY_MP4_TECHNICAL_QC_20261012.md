> **OWNER REJECT — 2026-10-13:** This rendered MP4 contains unauthorized burned-in narration subtitles (white with orange word highlighting) copied from another project's conventions. `Youtube-3/00_FOUNDATION/EDITING_CANON.md` does not authorize this style. **DO NOT PUBLISH / DO NOT MARK RELEASE PASS.** Technical decode and bitrate checks do not override owner's rejection. The correct replacement must be built from native R8 assets with NO generated/burned narrative captions unless separately authorized; do not edit the encoded pixels to mask them.

# VIDEO004 — R8 corrected high-quality MP4 export technical QC

**Status: HQ TECHNICAL EXPORT PASS; CREATIVE/FULL SOURCE-PIXEL QC NOT CLAIMED.**

The initial MP4 delivered on 2026-10-12 (`VIDEO004_WHAT_IT_COST_R8_MASTER_1080P25.mp4`, 77,374,261 bytes, 0.553 Mbps video) was too aggressively compressed for the user-requested high-quality master. That initial file is **SUPERSEDED** and should not be used for publishing.

## Verified replacement output

- Conversation-only file: `VIDEO004_WHAT_IT_COST_R8_HIGH_QUALITY_1080P25.mp4`
- Exact size: **639,200,335 bytes** (~639.2 MB decimal / 609.6 MiB)
- Exact SHA256: `34ea776c20d89a2163c6f2083cabab8d0a649292b42760127b4c00a27105af6b`
- From original 60 R8 PNGs; NOT an upscale/re-encode of the 77 MB old MP4, and NOT any earlier owner-rejected chat-image batch.
- Caveat: **59 originals are 1672x941**, so this 1920x1080 export is resized and is not native 1080p source detail; GF060 original is 1920x1080.
- Video: 1920x1080, 25/1 FPS, H.264 High, YUV420P, BT.709 primaries/transfer/matrix, actual video bitrate **5,917,071 bit/s**.
- x264 encode: `-preset faster -tune stillimage -crf 8 -g 50 -keyint_min 25`. The CRF8 encoder runs directly on image-based R8 canonical 84-placement sequence, with seven limited timeline motion treatments and the previously prepared real-time captions.
- Audio: original 808s Harrison V11 master (not regenerated or cut), encoded AAC stereo 48kHz, actual stream average ~252,670 bit/s. 20s quiet endscreen.
- Runtime: exactly 828.000s (13:48), 20700/20700 video frames, sequence three verified sections 7289 + 7034 + 6377 frames.
- FFmpeg `-xerror` **full final video/audio decode completed successfully** with no errors.
- FFmpeg `silencedetect` independently verified the last 20 seconds are silent.
- Start and end thumbnails inspected.

**Important constraints**: This corrects excessive lossy video encoding only. It does **not** constitute full creative montage, cinematic movement or shot-by-shot source-legal approval. Resolve was not run in this environment. A 639 MB output alone is not proof of good editing. The actual MP4 binary has NOT been uploaded to GitHub; Git here is the text audit trail. The user can download the real verified MP4 from the conversation file link.
