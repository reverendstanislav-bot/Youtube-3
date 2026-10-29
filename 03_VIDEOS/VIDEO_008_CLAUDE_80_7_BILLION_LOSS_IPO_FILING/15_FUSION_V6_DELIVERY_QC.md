# VIDEO008 V6: clean Fusion edit and small channel endscreen

Current review master: `WHAT_IT_COST_VIDEO008_V6_SMALL_ENDSCREEN_1080P25.mp4`.
Local directory: `C:\Users\KK\VIDEO008_PRODUCTION\DELIVERY`.
Resolve project `YT3 VID8`, current timeline `VIDEO008_V6_SMALL_ENDSCREEN_25FPS`.

## Owner corrections applied

- V4 was rejected by the owner. V4 and earlier V5 exports are superseded.
- Removed service/provenance bars, SRC captions, floating source strips, duplicate headers and opaque chart backgrounds from all 45 replacement compositions.
- Kept editable native Fusion camera movement, measured yellow marks in four scenes and one transparent chart in SC015 on empty desk space. Removed the duplicate SC092 chart.
- Replaced the invented future worksheet backgrounds in SC064 and SC090 with existing selected illustrations. No new image generation.
- Replaced all 45 legacy black-card source files with duration/frame-matched clean source plates. Original source bytes are backed up locally. This also fixes underlying source clips for timeline items 70/77/83; no further bulk relink was attempted after Resolve restarted.
- Added the existing small WHAT IT COST endscreen on V2 for the last 20 seconds: 16:07.800–16:27.800. 1920x1080 canvas, 720x405 video window, 260x260 subscribe circle. Fine antialiased border contours measure 722x407 and 262x262 in both the native preview and final MP4 last frame.
- V1 retains all 122 original items (110 scenes plus 12 one-frame holds); endscreen adds no runtime. Locked Harrison narration and script remain unchanged.

## Verification and limits

Technical PASS: 24695 frames, 987.800 seconds, 1920x1080, 25 fps, H.264/AAC; full output decode passed. Final audio decoded sample count matches the locked WAV; correlation 0.9999714 and RMS gain ratio 0.9992042. The picture was rendered in Resolve; final mux copies its native video stream and encodes the approved WAV at time zero. No video assembly in ffmpeg and no new TTS.

All 110 V6 scene-midpoint samples were visually inspected by the maker. V5 body samples and corrected key scenes previously passed independent static review. V6 small endscreen was checked in a native preview and the actual last MP4 frame. This is static/technical QC, not continuous real-time AV approval or independent V6 release approval. Continuous AV review and owner picture acceptance remain HOLD. Stage16 and publication were not started.

Generated document backgrounds remain **illustrative reconstructions, not authentic source scans**. Provenance stays in this report and the asset manifest; owner-rejected service labels are not overlaid on the film. Historical acquisition counts and source holds remain in the preproduction snapshot.

## Concrete outputs

- Final MP4 SHA256: `da86b8376d646c5bd3b7c7d11c63c8ba72260bc88f93f92c0e67177f4b44a384`.
- Native project: `VIDEO008_V6_SMALL_ENDSCREEN.drp`, SHA256 `6440648a521c9f1c2560a87bc4fbf5168222a80f55f5eeb7bcad65b1154b5bff`.
- Selected assets, clean sources, Fusion files, endscreen and DRP archive: `C:\Users\KK\VIDEO008_PRODUCTION\DELIVERY\VIDEO008_V6_SMALL_ENDSCREEN_EDIT_ASSETS.zip`. The local ZIP passed integrity and SHA256 checks. GitHub upload timed out; read-only release reconciliation found no V6 asset. There is no verified V6 archive download URL. Local ZIP is retained; do not use an earlier archive as the V6 project.
- Archive SHA256: `c178e234c2fac844d22b9f097d32a4f8568904a8a4163a9a3fbaa0997df3e797`; bytes: 373724991.
- [Original source archive](https://github.com/reverendstanislav-bot/Youtube-3/releases/download/video008-visual-assets-20261027/VIDEO008_SOURCE_ARCHIVE.zip) and [original acquisition pack](https://github.com/reverendstanislav-bot/Youtube-3/releases/download/video008-visual-assets-20261027/VIDEO008_FINAL_VISUAL_PACK.zip) retained as historical source dependencies.
- Machine evidence: `15_FUSION_V6/DELIVERY_QC_V6.json`, `15_FUSION_V6/ENDSCREEN/V6_GEOMETRY_QC.json`, `15_FUSION_V6/EDIT_ASSETS_QC_V6.json`. Native DRP is also preserved in `15_FUSION_V6/`.

The archive build manifest describes the build-time snapshot; final delivery QC above is authoritative for rendered output. Media paths are local production paths: extract the selected-assets archive under the existing production root or relink when transferring to another machine. Original stock files and the approved WAV remain required dependencies. Upload/publishing permission is not implied by this delivery.
