# NEW CHAT HANDOFF — VIDEO 001 / WHAT IT COST
Date: 2026-09-24
Repo: `reverendstanislav-bot/Youtube-3`
Video folder: `03_VIDEOS/VIDEO_001_THE_EBAY_HARASSMENT_SCANDAL_THAT_COST_56_MILLION/`

## Permanent rules
- GitHub is source of truth.
- `Youtube-1` is reference/read-only; never modify it.
- Re-read current `main` and relevant files before every GitHub write.
- Use atomic writes, `force:false`.
- Never claim completion unless verified.
- No paid generation without explicit owner approval.
- No video generation.
- Do not auto-advance stages.
- Bottom subtitle-safe zone: min 20%, target 22%.
- Channel: **WHAT IT COST**
- Positioning: **Business Stories Where Money & Law Collide**
- Style: premium investigative business documentary.
- Palette: #0B0B0B / #1F1F1F / #3A3A3A / #EDEDED / #D32222.
- Captions: #EDEDED base + #D32222 active word. Orange is retired.

## Video 001 locks
Title: **The eBay Harassment Scandal That Cost $56 Million**
Narrator: Harrison
Runtime target: **957.414 sec**
Visual beats: **115**
Canonical script: `07_SCRIPT_FINAL.md`
Canonical timeline: `11_VISUAL_TIMELINE.csv`
Word transcript: `11_TRANSCRIPT_WORD_LEVEL.json`
Captions: `11_CAPTIONS.srt`

Critical factual/legal locks:
- $55.7M = final civil settlement package, not judgment and not eBay-only.
- $48.7M compensation + $7M charity.
- eBay compensation $46.15M.
- Wenig $2M; Wendy Jones $500K; Steve Wymer $50K.
- Charity: eBay $6M, Wenig $1M.
- Separate $3M criminal DPA penalty.
- DPA ≠ conviction.
- GPS tracker attempted; successful installation not established.
- Surviving claim ≠ liability.
- Wenig/Wymer/Jones were not criminally charged over the campaign.
- Feb 2026 settlement-in-principle failed.
- Final settlement late July 2026.
- Never create a $58.7M award.
- B101 must keep seven guilty pleas / $3M criminal DPA / $55.7M civil settlement package as separate tracks.

## Stage 14 / GFX
12/12 final GFX passed QC and are locked.
B101 final media ID: `20f94d5e-d9a5-4af0-989d-7d2ec28e1244`
GFX archive media ID: `4eb621b3-decd-427f-8730-580d55779b91`

## Stage 15A — picture resolution complete
`15A_ASSET_RESOLUTION.csv`: 115/115 resolved.
Stage15A review master media ID: `174a262e-958f-4b63-b215-1a6ab385b755`
Runtime 957.371 sec.
Lock commit: `dee8b110f5fbe93a3870e66f8631fda9c1f806e8`

## Stage 15B — approved picture/captions/overlays
This is the current approved picture basis for every audio test.
Corrected run: `36021465130`
Artifact: `10817420859`
File: `VIDEO_001_STAGE15B_REVIEW_V1_1080P.mp4`
1920×1080 / H.264 / CFR25 / AAC 44.1k mono
Runtime: 957.370 sec
SHA256: `a4626fed53d09e69cbc59e089f5490695ea7f5243dcec0f41bf7fed72156cf33`
409 caption cues / 2151 word-highlight events / 0 fallback cues.
83 metadata/source/legal/reconstruction overlay events.
B104 inequality patch fixed.
Owner accepted Stage 15B.

## Stage 15C — complete path so far

### Attempt 1 — Scott Buckley full music mix
Tracks: Resonance / Intervention / Chronicle / Life Is.
Run `36033748640`; artifacts `10823619066` and `10823599106`.
Owner verdict: music unsuitable / bad for this film.
Status: **REJECTED. Historical only. Do not reuse.**

### Attempt 2 — Mixkit replacement audition
Run `36036170552`.
Pack artifact `10825021726`; reel artifact `10824876844`.
Owner verdict: **“полная хуйня”**.
Status: **REJECTED. Do not return to this pack.**

### Attempt 3 — TeknoAXE A/B music proofs on real film
Run `36038105016`.
Proof A artifact `10824924864`.
Proof B artifact `10824904874`.
Owner verdict: music itself kills the film / is too bad.
Strategic conclusion: **continuous music bed is not the default anymore.**
Status: **REJECTED.**

### Strategic pivot
Current desired direction:
**Harrison + silence + sparse SFX.**
Music may be removed completely. If it ever returns, only tiny isolated entries after separate approval.

### SFX-only proof V1
No music.
190.023 sec real-film proof using opening / messages / operation / money / ending.
Run `36044425718`.
Proof artifact `10827149357`.
SFX pack artifact `10827199168`.
SFX types: room tone / paper tick / page rustle / keyboard cluster / dry click / low transition / digital-delete / soft whoosh.
Owner verdict: **“не одного звука не услышал”**.
Reason: SFX were around roughly -28 to -36 dB and disappeared under Harrison.
Status: **REJECTED — inaudible.**

### SFX-only proof V2
Changes:
- removed room tone completely;
- event gains raised about +10 dB;
- procedural source amplitudes rebuilt stronger;
- still no music.
Run `36046422755`.
Proof artifact `10828686824`.
SFX pack artifact `10828442441`.
Runtime 190.023 sec.
Aggregate QC approximately -16.4 LUFS integrated / -3.8 dBFS true peak.
Owner verdict after listening: **“их вообще не слышно”**.
Important: aggregate loudness passing did NOT mean local SFX were perceptually audible.
Status: **REJECTED — still inaudible.**

## Current exact status
- Stage 15B picture: APPROVED.
- Captions/overlays: APPROVED.
- Music: REJECTED.
- Scott Buckley mix: REJECTED.
- Mixkit: REJECTED.
- TeknoAXE A/B: REJECTED.
- SFX-only V1: REJECTED, inaudible.
- SFX-only V2: REJECTED, still inaudible.
- Stage 15C: **OPEN / NOT APPROVED / NOT FINAL**.
- Final master/QC: NOT STARTED.
- Paid/model generation during these audio iterations: 0 credits.

## Current files relevant to continuation
- `STATE.md`
- `VERSION_LOG.md`
- `QA_LEDGER.csv`
- `15C_SFX_PROOF.md`
- `15C_SFX_PROOF_BUILD.py`
- `15C_SFX_PROOF_TRIGGER.txt`
- `11_VISUAL_TIMELINE.csv`
- approved Stage15B picture master from artifact `10817420859`

## Previous SFX proof window map
Proof V2 concatenation:
- 00:00–00:34 = original film 00:00–00:34
- 00:34–01:10 = original film 02:44–03:20
- 01:10–01:48 = original film 04:44–05:22
- 01:48–02:30 = original film 12:38–13:20
- 02:30–03:10 = original film 14:18–14:58

Intended proof-local SFX checkpoints:
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

Owner still could not meaningfully hear them.

## NEXT CHAT — exact first task
Do NOT search for more music first.
Do NOT render another 3-minute proof blindly.
Do NOT use whole-program LUFS as proof that SFX are audible.

First solve SFX audibility in a controlled micro-test:
1. Re-read current `main`, `STATE.md`, this handoff, `15C_SFX_PROOF_BUILD.py`, `11_VISUAL_TIMELINE.csv`.
2. Select only 3–4 representative SFX and only 20–40 seconds of actual approved Stage15B film.
3. Export each chosen SFX as an **SFX SOLO REFERENCE** first so the owner can hear the effect by itself.
4. Measure each effect itself and the local Harrison level around its insertion.
5. Mix the same effects into the short real-film excerpt at a **clearly audible relative level**.
6. Export two files:
   - `SFX_SOLO_REFERENCE`
   - `SFX_IN_CONTEXT_PROOF`
7. Give exact local timecodes for every effect.
8. Verify audibility before presenting it.
9. Keep sound premium and restrained: no TikTok sound spam, horror, trailer booms, gavel, sirens, cash-register, fake event-implying foley.
10. Only after owner explicitly says the SFX are audible and stylistically correct should the system expand the design across the full 15:57 film.

Do not simply add another arbitrary +10 dB. The previous two attempts prove that blind gain changes are not enough. Verify the local signal relationship first.

## Gate
Remain inside Stage 15C until owner explicitly approves the audio direction.
Do not auto-start final master/QC.
