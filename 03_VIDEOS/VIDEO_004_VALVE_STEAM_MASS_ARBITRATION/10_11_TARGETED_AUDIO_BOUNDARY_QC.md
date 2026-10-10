# VIDEO004 Stage10/11 targeted audio boundary QC — 2026-10-10

**Status: TECHNICAL WAVEFORM CHECK PASS / GENUINE AUDITORY REVIEW NOT PERFORMED.**

Source `VIDEO004_HARRISON_V11_MASTER.wav`: SHA256 `8c11be2619a6a84b7e1a6cbe0cb8c708d72dff556d1d737dd46f596ea21f65d7`, 808.000s, PCM 48kHz stereo.

Four production Shorts only: SH01/SH02/SH04/SH08. Audio listening ZIP, made with no new TTS, contains 14 source-derived MP3 excerpts: the eight ASR lexical concerns at 3.86, 142.76, 197.60, 225.82, 251.98, 427.22, 490.24, 735.04 seconds, both joins at 284.96/535.76, and four complete contiguous Short audio extracts. ZIP generated locally in current conversation under `VIDEO004_STAGE10_11_AUDITORY_REVIEW.zip`; may be moved into approved local production storage. No paid generation.

## Waveform/sample checks

Adjacent-sample mono changes and local RMS for a 25ms window either side, normalized amplitude scale. These are **measurements, not an audibility/quality verdict**.

| Boundary | Master time | Adjacent sample amplitude difference | 25ms pre/post RMS |
|---|---:|---:|---|
| A/B |284.960|0.000053|0.000196 / 0.001715|
| B/C |535.760|0.007972|0.039270 / 0.000041|
| SH01 end |18.660|0.000271|0.000910 / 0.000443|
| SH02 start |118.200|0.060832|0.038738 / 0.131481|
| SH02 end |135.820|0.015462|0.032297 / 0.030929|
| SH04 start |285.260|0.001110|0.113217 / 0.129415|
| SH04 end |300.440|0.010240|0.023531 / 0.009034|
| SH08 start |627.640|0.004075|0.041175 / 0.031395|
| SH08 end |645.960|0.001274|0.033811 / 0.010339|

**Priority listening:** B/C join (nonzero jump), SH02 start (cut in active speech), SH02 end / SH04 end and SH08 start. A sample difference is not proof of an audible click; do not cut or regenerate based solely on it. ASR word changes can be recognition noise. Audition full 808s for prosody and timbre prior to Stage10 lock; audition every Short with proper CTA before Stage11 final lock. No new TTS authorized.

Audio lock FALSE; Stage11 transcript/cut map remains provisional. These findings do not block preparation of Resolve picture comps but block final edit/publish PASS.
