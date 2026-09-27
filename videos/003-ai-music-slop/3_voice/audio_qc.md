# Audio QC

- **File / sha256 / duration:** voice/narration.mp3 · 3c2d11ff9a3f24e44672a128fde7b41df70467cd0cb86ccb9cd8560fe867d991 · 22:15 (1334.88 sec) — Parts 1–7 only
- **Loudness (integrated LUFS / true peak) — after loudnorm:** −15.3 LUFS / −1.6 dBFS — ✓ **PASS** (−15.3 within target −16…−14; true peak −1.6 dBFS is better than limit ≤−1.0)
- **Clipping / clicks:** no clipping risk; 0 silences >1.5s ✓
- **Narration locked by owner:** status.yaml decision approved.

## Transcription Artifact Resolution

Coordinator re-transcribed with Whisper medium.en. Four previously flagged "critical" mismatches were **Whisper Base mishearings, not TTS errors:**

| Time | Base heard | Medium heard (TTS correct) |
|---|---|---|
| 09:04 | "body counts" | "pay for bot accounts" ✓ |
| 10:52 | "reconnaissance" | "personal recognizance bond" ✓ |
| 17:51 | "trucks" | "tracks a day" ✓ |
| 14:34 | "boom play title" | "Boom Play, Tidal" ✓ |

**Acronym spacing (B-E-T, V-P-Ns, M-L-C, U.S., I-F-P-I):** Cannot be verified from any transcript; spacing/letter-by-letter delivery is inaudible in transcript form.

## Remaining Pronunciation Uncertainties (Owner-Accepted)

Per uncertain-names list, these are hard-to-verify names marked for "check." Whisper medium transcriptions suggest reasonable approximations:

- **Koeltl** (Judge John): medium heard "Kotal" — phonetically close; owner approval overrides.
- **Lewan** (Michael): medium heard "Lewin" — phonetically close; owner approval overrides.
- **Suno** (platform): medium heard "Suno" correctly — Base's "soono" was transcription artifact.

---

## Verdict: **PASS**

All measurements within spec. Four semantic errors were Whisper Base transcription artifacts, not TTS defects. Acronym delivery cannot be judged from transcript. Remaining name uncertainties are within acceptable tolerance per uncertain-names list; **owner has locked narration.**

No regeneration required.
