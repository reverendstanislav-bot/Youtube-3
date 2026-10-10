# VIDEO004 — Stage11 transcript and visual timeline

Status: PROVISIONAL_ASR_TIMELINE / AUDIO_LOCK_PENDING. Owner explicitly requested Stage11 start. This preparation does not advance the authoritative current stage beyond10 or waive its auditory gate. No Stage12 generation/assets/render started.

## Inputs and measured coverage

Unchanged V11 canonical07 and normalized08 payloads; exact8Shorts text lock retained. Source master8c11be2619a6a84b7e1a6cbe0cb8c708d72dff556d1d737dd46f596ea21f65d7,808seconds. Local faster-whisper1.2.1 / small.en, English explicit, CPU int8; no external ASR/TTS API. HyperFrames0.8.145 returned whisper_unavailable on this Windows host; local fallback used av16.1.0 because av19 is incompatible.

11_ASR_RAW.json retains recognition verbatim;11_WORD_LEVEL_TRANSCRIPT.json retains1951observedword rows, not script text assigned invented timings.11_PARAGRAPH_ALIGNMENT.json maps123canonical paragraphs to observed anchors.11_ALIGNMENT_QC.json preserves differences, low-confidence words and44sub-50ms spans. Short/zero word spans are flagged, not silently interpolated or approved for captions. Do not use these provisional words for burned subtitles.

54authored macrobeats in11_BEAT_INTENTS.json cover all123paragraphs. SCENE_TIMELINE.csv has123narration cue spans plus1planned end screen; contiguous0–828seconds at30fps (24840frames), no overlaps/gaps. Narration0–808s; planned no-narration end screen808–828s. Endscreen is not yet in the WAV/video. Scene rows are semantic cues, NOT123mandatory picture cuts or54static-slide holds.

## Directorial contract

Open with the attributed library-access conflict, reveal claimant-to-defendant reversal, then let the two contracts explain it. Preserve open questions until their corresponding evidence/answer. $20M must remain inseparable from UNVERIFIED; claimant counts must carry dates; denial must carry PRELIMINARY, not an antitrust verdict. Keep four-claimant, later-defendant and publisher tracks separate. End on changed contract versus cases not disappearing, then a clean20s native end screen.

Evidence-first, no generated filings/signatures/SteamUI/acceptance pop-ups passed off as real. AUTHENTIC_DOCUMENT means required provenance class, not an asset already downloaded/rights-cleared; Stage12 must bind the actual source and crop. No fake invoice, loss scoreboard or deletion of purchased games.

Picture remains stable: no shake, jumping crops, universal drift or alternating zoom directions. Default straight cuts at evidence/idea changes; hold through explanatory paragraphs where the same evidence continues. Use a named source detail for any deliberate move, and land/hold before reading. Split long evidence passages into useful detail views later, not decorative timer cuts. English visible editorial text only; no burned speech captions.

## Four selected Shorts — ASR anchored, NOT exported

|Short|Master in|Master out|Audio cut(s)|+3s CTA planned(s)|
|---|---|---|---:|---:|
|SH01|00:00:00.000|00:00:18.660|18.66|21.66|
|SH02|00:01:58.200|00:02:15.820|17.62|20.62|
|SH04|00:04:45.260|00:05:00.440|15.18|18.18|
|SH08|00:10:27.640|00:10:45.960|18.32|21.32|

One contiguous source range each. No rewrite, reorder, speedup or separateShortsTTS. Start/end padding never borrows adjacent narration; boundaries still need audition against the waveform, particularly no-gapSH05/06/07/08 edges. Some spoken extracts are below preferred20s: do not add filler or stretch delivery to hit that preference. Owner hard maximum30s takes precedence.

CTA plan:3.00seconds including0.35second transition; finish speech before it, no cut-off last syllable. Maintain coherent evidence behind the bridge; use each locked Short-specific unresolved long-form question from07_SHORTS_LOCK, with a restrained WHAT IT COST subscribe/link cue. This is a plan, not a generated endcard. Vertical alternate layout preserves both disputed positions, dates and legal caveats; never rely on a centre crop that deletes them. Final9:16export duration<=30s must be measured separately atStage15.

## Acceptance still pending

Current artifacts are provisional until Stage10 genuine auditory QC and lock; then verify paragraph anchors/cut auditions, resolve low-confidence events and independent final timeline review. Current script acceptance90.4/100 is text-only, not audio/picture/viral performance. No claim of full audio listening or rendered video QC. Stage16 must refresh current appellate status.

Reproduce: Python3.12 plus faster-whisper1.2.1 and av16.1.0; run11_TRANSCRIBE_LOCAL.py on the hashed master, then11_BUILD_TIMELINE.py. Numeric/punctuation normalization is diagnostic only; raw recognized words preserved. Recheck script11_RECHECK_LOCAL.py processes only8flagged windows with medium.en.

## Independent preparation verdict

review_correction: PASS_PROVISIONAL_STAGE11_PREPARATION / NOT_STAGE11_LOCK. All5inputhashes checked; coverage and8legalstandalone extracts accepted provisionally. See11_STAGE_QC.md for exact hashes and open auditory/anchor/cut-edge acceptance criteria. Medium.en recheck supports source wording at8first-model lexical flags; no genuine hearing claim.

Owner revision 2026-10-10: exactly four production Shorts (SH01, SH02, SH04, SH08); former SH03, SH05, SH06, SH07 are archived candidates only. All four cut edges and full audio still require actual auditory QA before final lock. No export yet.
