# VIDEO 001 — SFX-Only Proof

Status: **BUILT / TECHNICAL PASS / OWNER REVIEW PENDING**
Date: 2026-09-24

Owner requested a test with the music removed and the sound design carrying only what is necessary.

## Proof principle
- **NO MUSIC**
- Harrison remains primary.
- Silence and the picture carry the tension.
- Only restrained editor-native micro-SFX are used.
- No third-party SFX source and therefore no stock-library license dependency.
- No model generation / 0 credits.

## SFX pack
1. neutral room tone
2. paper tick
3. page rustle
4. keyboard cluster
5. dry editorial click
6. restrained low transition
7. abstract digital-delete texture
8. soft whoosh

## Proof excerpts
- opening
- executive-message escalation
- operation / physical stakes
- settlement / money
- late-film consequence

This is a **sound-design proof only**, not a final Stage 15C master.


## Result — 2026-09-24
- Workflow run: `36044425718` — SUCCESS
- Proof artifact: `10827149357`
- SFX-pack artifact: `10827199168`
- Proof file: `VIDEO_001_SFX_ONLY_PROOF_V1.mp4`
- Runtime: **190.023 sec**
- 1920×1080 / H.264 / CFR 25 fps
- AAC 44.1 kHz stereo
- Measured integrated loudness: **−16.46 LUFS**
- Measured true peak: **−3.64 dBFS**
- Music: **NONE**
- SFX source: **100% editor-native procedural synthesis**
- Third-party sound libraries: **NONE**
- Paid/model generation: **0**
- Final Stage 15C remains **NOT APPROVED** until owner review.


## V2 audible pass — 2026-09-24
- Owner requested the same proof with effects raised and room tone removed.
- Workflow run: `36046422755` — SUCCESS.
- Proof artifact: `10828686824`.
- SFX-pack artifact: `10828442441`.
- File: `VIDEO_001_SFX_ONLY_PROOF_V2_AUDIBLE.mp4`.
- Runtime: **190.023 sec**.
- Music: **NONE**.
- Room tone: **REMOVED**.
- Event-gain settings raised approximately **+10 dB** from V1.
- Procedural SFX source energy was also rebuilt upward so accents remain audible beneath Harrison.
- Integrated loudness: **−16.4 LUFS**.
- True peak: **−3.8 dBFS**.
- Correct proof-local checkpoints:
  - 00:06.340 paper tick
  - 00:07.760 page rustle
  - 00:50.260 digital-delete texture
  - 01:04.950 page rustle
  - 01:10.180 page rustle
  - 01:35.400 soft whoosh
  - 01:52.080 dry click
  - 02:08.640 dry click
  - 02:18.540 dry click
  - 02:34.240 page rustle
  - 03:09.900 dry click
- Owner review pending. This is still a proof, not a final Stage 15C master.

## Controlled audibility microtest V1 — 2026-09-24
Status: **TECHNICAL PASS / OWNER REVIEW PENDING**

The V1/V2 long SFX proofs were not used as the basis for another gain-only iteration. This test measures the effects against Harrison locally before rendering.

### Scope
- Approved Stage15B film window: `00:00.000–00:34.000` (**34.000 sec**).
- Music: **NONE**.
- Room tone: **NONE**.
- Harrison ducking: **NONE**.
- SFX: four editor-native procedural accents.
- Paid/model generation: **0 credits**.

### Outputs
- Workflow run: `36049666541` — SUCCESS.
- `SFX_SOLO_REFERENCE`: artifact `10830026745`, `VIDEO_001_SFX_SOLO_REFERENCE_V1`.
- `SFX_IN_CONTEXT_PROOF`: artifact `10829862172`, `VIDEO_001_SFX_IN_CONTEXT_PROOF_V1`.
- Measurements/report: artifact `10829897002`, `VIDEO_001_SFX_MICROTEST_QC_V1`.

### Exact in-context checkpoints and measurements
- `00:06.340` paper tick — SFX peak **−4.50 dBFS**, RMS **−21.31 dBFS**; Harrison peak **−3.46**, RMS **−17.70**; Δpeak **−1.04 dB**, ΔRMS **−3.61 dB**; PASS.
- `00:07.760` page rustle — SFX peak **−5.00 dBFS**, RMS **−15.10 dBFS**; Harrison peak **−1.96**, RMS **−20.42**; Δpeak **−3.04 dB**, ΔRMS **+5.32 dB**; PASS.
- `00:21.900` soft whoosh — SFX peak **−7.00 dBFS**, RMS **−19.24 dBFS**; Harrison peak **−5.53**, RMS **−22.57**; Δpeak **−1.47 dB**, ΔRMS **+3.33 dB**; PASS.
- `00:30.120` dry click — SFX peak **−4.00 dBFS**, RMS **−19.25 dBFS**; Harrison peak **−4.31**, RMS **−18.45**; Δpeak **+0.31 dB**, ΔRMS **−0.80 dB**; PASS.

### Solo-reference checkpoints
- `00:02.000` paper tick
- `00:06.000` page rustle
- `00:10.000` soft whoosh
- `00:14.000` dry click

### Verification rule
- Transients: SFX peak no more than **5 dB below** local Harrison peak.
- Textures: SFX peak no more than **7 dB below** local Harrison peak and SFX RMS no more than **10 dB below** local Harrison RMS.
- All four events passed before encoding.

### Gate
This result verifies the technical signal relationship only. Owner must still judge whether the effects are perceptually audible and stylistically right. **Do not scale to the full film and do not close Stage 15C without explicit owner approval.**

