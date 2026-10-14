# VIDEO005 — Stage09 Independent Release Audio File and ASR/Signal QC

**2026-10-14. TECHNICAL PASS / AUDITORY HOLD.** No Stage09 voice lock or Stage10 master has been issued.

## Sources actually inspected
Official [Release](https://github.com/reverendstanislav-bot/Youtube-3/releases/tag/video005-harrison-qwen06-20261014), tag `video005-harrison-qwen06-20261014` (Git ref points to commit `94d245e7bd61bcbbf8f825702f8970380e6855d7`). Release contained exactly **14 uploaded assets**: five WAV files, five ASR transcript files, `asr_qc.json`, `generation_manifest.json`, `SHA256SUMS.txt`, `VOICEBOX_GENERATION_QC.md`. All 14 were retrieved in the controlled media sandbox and their sizes checked against GitHub metadata. Each of five WAVs was **byte-for-byte compared against the Release SHA256SUMS and matched**. Original voice-profile claim in producer report: Qwen3-TTS Base 0.6B Voicebox clone from VIDEO004 clean Harrison voice master; **claim cannot independently establish matching timbre**.

## Independently inspected measurements
| chunk | real seconds | encoding | peak dBFS | RMS dBFS | SHA-256 | hard-clip samples | >1.2 s quiet runs | discontinuity jumps >0.58 FS |
|---|---:|---|---:|---:|---|---:|---:|---:|
| 01 | 192.12 | WAV mono PCM s16le 24000Hz | −2.00 | −20.00 | CEB2D5E552410A294BC7E6DB4930A871E4209A8B683F390B2CB0639B160AF6FA | 0 | 0 | 0 |
| 02 | 227.59 | WAV mono PCM s16le 24000Hz | −2.53 | −20.00 | 68433623DC048E3511C722B972B0EA51ADBB0A0FB3F2CD0313F89DAAF847D582 | 0 | 0 | 0 |
| 03 | 189.32 | WAV mono PCM s16le 24000Hz | −2.24 | −20.00 | 70BEBF74808F6ED6C2B3E51665BB28CB00352468B44DAB20D50902B5B5E1E78D | 0 | 0 | 0 |
| 04 | 198.20 | WAV mono PCM s16le 24000Hz | −2.01 | −20.00 | 9728BFD5C0407213630F47C67CB71C86B9838F492CB88778D9AAA4E96A931546 | 0 | 0 | 0 |
| 05 | 187.32 | WAV mono PCM s16le 24000Hz | −2.75 | −20.00 | E9C9B599FB2CE2A9CD0E3318D039D8BB456D47DAAE678B76C264FB56255D027D | 0 | 0 | 0 |

**Total WAV playback 994.55 seconds = 16:34.55**, source file sum, not assembled master. No digital clipping at >=99% of max amplitude; no absolute sample discontinuity jump >0.58 full-scale; no >=1.2s near-silence period (20ms window RMS threshold −42dBFS). This objective signal analysis does **not** verify there are zero audible artifacts, natural prosody or identical voice identity.

## Automated text continuity (rechecked)
- Compared each available original Release ASR transcript with its **exact canonical `08_HARRISON_TTS_MASTER_INPUT.txt` 55-paragraph text** segmented into 5 original chunks (10,12,11,11,11).
- Token-normalized difflib ratios: **0.922 / 0.942 / 0.956 / 0.895 / 0.956**. The 0.895 in chunk04 mainly reflects that the original explicitly spelled out a 17-token exact personal civil judgment `one hundred seventy-nine million...dollars and sixty-four cents`, whereas ASR normalized that whole currency amount as digits. No missing contiguous passage >=6 word tokens was identified beyond that **formatting substitution**. This is a screening check, not word-for-word human signoff on every number.
- The original ASR and an **additional independent faster-whisper tiny.en forced-word timestamp pass** both place speech in the expected five-act-pair order. The latter produced approximate timestamps for all four production Short parent paragraphs; see `09_SHORTS_ASR_WORD_TIMINGS.csv`.

## Production Shorts — speech-only word-aligned estimated windows
| Short | Source | Parent | Chunk-relative start–end | Estimated speech only | Global position in virtual concatenation | Exact source match confidence |
|---|---|---|---|---:|---|---|
| S01 | chunk01 | A00-P01 | **0.00–21.32** | **21.32s** | 00:00.00–00:21.32 | 46/60 token exact matches; numeric formatting/name variations |
| S03 | chunk02 | A02-P03 | **37.10–59.52** | **22.42s** | 03:49.22–04:11.64 | 52/66 token exact matches; currency formatting |
| S05 | chunk03 | A04-P03 | **37.42–59.94** | **22.52s** | 07:37.13–07:59.65 | 56/61; final `Otto` often rendered `Auto`, so actual tail slightly later |
| S08 | chunk05 | A08-P04 | **50.66–70.88** | **20.22s** | 14:17.89–14:38.11 | 53/58; 2022 digit formatting |

**Timing caveat:** These are automatic word-alignment estimates, **not hand-listened full-phrase boundaries** and not final montage cuts. They do not include CTA/end-card, trimming/crossfade or any downstream chapter transitions. S03's measured proxy from existing generated audio is ~22.4s (rather than the earlier 31.5s at hypothetical 120wpm). However **30.0s TOTAL final Short limit is still NOT_VERIFIED**. Do not replace old owner-approved Short with a rewritten one or generate standalone Short TTS.

## Listen-first remaining blockers
1. **Harrison canonical timbre:** Qwen3-TTS was reportedly cloned from clean VIDEO004 Harrison master, but an objective wave shape or ASR transcript does not establish equivalence with the channel-locked Higgsfield Harrison voice. Requires true A/B auditory comparison to genuine approved reference.
2. **Name pronunciation:** ASR frequently detects Levandowski as `Lewandowski`, `Levantowski` and `Levin Dowski`. `Stroz Friedberg` appears as `Strasfriedberg` near **chunk02 01:59.6** and `Straws Friedberg` near **chunk02 02:57.5**. Some Otto tokens are rendered `Auto`; Waymo sometimes becomes `Weimos`. **These are ASR spellings, not conclusive pronunciation failures**. Listen explicitly.
3. **Audible joins:** No final contiguous mix yet. Listen at the ends of chunks 01–05 and the starts of 02–05, plus boundary pauses/internal artifacts. Digital discontinuity scan alone is insufficient to certify natural joins.
4. **Voice prosody / speed / clipping/metallic artifacts:** Signal QC passes objective low-level limits, but genuine listening still required.
5. **Short total runtime with CTA/end screen** and source-accurate cuts must be checked in Stage15 or as soon as finished Short exports exist.

## Stage gate
**G09 AUDIO INTEGRITY AND ASR/TIMING TECHNICAL QC: PASS.** **G09 HARRISON VOICE QA/LOCK: HOLD AUDITORY, not a PASS.** `locks.voice_input=false`, `stage_10_audio_master=NOT_STARTED`. No synthesis, paid generation, audible master, Shorts renders, video or credit spend in this audit. Do not automatically proceed to Stage10. Listening signoff must state which clip/timecodes were checked; if a defect is found, document the exact scope before seeking authorization for any retry.
