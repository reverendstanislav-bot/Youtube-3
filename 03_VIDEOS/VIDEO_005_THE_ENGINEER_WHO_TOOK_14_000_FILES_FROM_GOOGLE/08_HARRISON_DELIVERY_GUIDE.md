# VIDEO005 — Harrison narrator delivery guide (Stage08; NOT a spoken script)

**Source:** 07_SCRIPT_FINAL.md V4.4 US English, Git blob `5f6776bcbafc3f997cc726e857c15617e510ebc9`. **The only aloud text is `08_HARRISON_TTS_MASTER_INPUT.txt` or its exact five non-overlapping contiguous parts**, not this guide or metadata.

## Narrator and synthesis
- **HARRISON** is the owner-locked WHAT IT COST narrator. Provider/catalog: **Higgsfield voice preset**. ID **573e5163-59b3-4926-aab1-951ef2985f81** (authoritative channel lock `00_FOUNDATION/VOICE_LOCK.md`).
- Engine/model, usable text-character limit, synthesis settings, estimated credits and paid-job authorization are **NOT LOCKED / NOT APPROVED**. Stage08 creates NO jobs and plays NO new audio. Stage09 must resolve provider model/config and verify names before paid generation, after owner authorizes any necessary tests.
- English (US) contemporary investigative documentary, **controlled, curious, factual**, not trailer shouting, melodrama, sarcastic mockery or a lawyer impersonation. Medium cadence **planning reference ~145 audible words/min**; measured pace and exact pause timing unknown. A word-count calculation is not an audio QA result.

## Editorial emotion and cadence — silent cue sheet, not pasted to TTS
| Act | Directing note | Critical factual restraint |
|---|---|---|
| A00 | Lead directly with **Anthony Levandowski** and **fourteen thousand**; focus on “The debt wasn't Uber's.” Keep the 2022 question genuinely curious | The personal award is distinct from corporate Waymo case |
| A01 | Explain LiDAR once, neutrally; after copying, distinguish possession from **proof Uber actually used** the files | No "all files stolen by Uber" claim |
| A02 | Deliberately contrast **up to six hundred eighty million** with **one hundred thousand dollars** | The maximum is conditional, NOT engineer cash; S03 sits inside long master |
| A03 | Forensic doubt, then careful scope on Stroz: **no evidence of this specified transfer**, not all-company innocence | Do not punch "no evidence" as a categorical exoneration |
| A04 | Accidental wrong-recipient supplier email is a factual, low-key turning point, not a fictional leak confession | Alleged circuit similarity, not proven infringement; preserve S05 |
| A05 | Five disks/disclosure procedure: underplay missing-object mystery; make **may, not must** inference understandable | Unknown disk contents; no ordered verdict |
| A06 | Corporate resolution: **Uber stock worth about $245 million**, not cash penalty or jury damages | Civil dismissal without verdict |
| A07 | Human consequence as **personal** court judgment, then another distinct criminal proceeding and pardon | One guilty plea ≠ 33 convictions, pardon ≠ erase civil judgment |
| A08 | Main reveal: a **new 2022 Global Settlement**, NOT 2016 indemnification enforcement. Treat sealed amount calmly and plainly | No made-up principal; separate $2m; S08 entire paragraph |
| A09 | Close on the 2025 gross-income finding and unchanged mystery about amount; no triumphant "Uber found guilty" voice | Tax ruling did not fix a final tax bill |

**Breaks:** Natural paragraph punctuation governs pauses; a restrained reset between acts is acceptable, but **avoid forced pauses inside any of four selected Short paragraphs** because their final duration must stay <=30 seconds inclusive of end card/CTA. Never drop legally important qualifiers to speed a read. Do not add standalone introductory or closing narration to the film.

## Proper-name and technical QA list (Stage09 must listen/check)
| Token in locked text | Draft US speech cue | Confidence / action |
|---|---|---|
| **Anthony** | AN-thuh-nee (US; th as in *think*) | Dictionary-confirmed; `https://dictionary.cambridge.org/us/pronunciation/english/anthony` |
| **Levandowski** | **NO unverified phonetic replacement** | Person's exact surname stress not source-verified; keep spelling in TTS, confirm from authentic owner/interview audio or a later approved Harrison sample before locking audio |
| **Stroz Friedberg** | **NO unverified phonetic replacement** | Organization name stress/vowels not source-verified; keep spelling, verify Stage09 |
| **Waymo** | WAY-moh | General US brand speech cue; verify with provider playback |
| **LiDAR** | LYE-dar (not letters L-I-D-A-R) | Standard technical cue; provider pronunciation may vary |
| **Otto** | AHT-oh | Automotive startup name; avoid extra accent/affectation |
| **indemnification** | in-dem-ni-fi-KAY-shun | Legal term, not "indemnity" substituted for a different noun in the locked text |
| **Chapter eleven** | plain chapter + eleven | In numeric verbalization file, `Chapter 11` expands to `Chapter eleven` |

**Do NOT insert the pronunciation guide itself into a TTS request**. If the synth pronounces a name badly, use an approved delivery-level pronunciation control at Stage09 and record its exact changes; never silently change the locked canonical narrator wording.

## Explicit spoken-number equivalence / verification
The TTS-input files verbalize all 23 digit/currency/date patterns using reversible exact substitutions logged by source paragraph ID in `08_HARRISON_NORMALIZATION_AUDIT.csv`. Examples:
- `14,000` → **fourteen thousand**; `$179 million` → **one hundred seventy-nine million dollars**
- `$179,047,998.64` → **one hundred seventy-nine million, forty-seven thousand, nine hundred ninety-eight dollars and sixty-four cents**
- `$245 million` → **two hundred forty-five million dollars**; `$680 million` → **six hundred eighty million dollars**; `$100,000` → **one hundred thousand dollars**
- `$2 million` → **two million dollars**; `2022` → **twenty twenty-two**; dates expanded consistently.
The 2,551 written-word metric from Stage07 becomes **2,627 space-token words in the expanded TTS input**. At 145 such tokens/min, predicted pure spoken ~18:07, rather than prior 17:36 which counted numeric glyphs as one word. **Both are approximate**, no recorded voice duration, and numeric token count is only a better estimate, NOT measured exact words uttered by a voice model.

## Four locked parent Shorts / crucial runtime hazard
**S01=A00-P01; S03=A02-P03; S05=A04-P03; S08=A08-P04.** Each is 100% of one film paragraph from a single chunk and final master; no separate Short TTS. Stage11 must locate actual audio word boundaries in the Harrison MASTER. Stage15 must cut only from those bounds, leaving the **whole Short incl any silent/visual CTA or end card <=30.0 seconds**. This may require trimming nonessential silence or adjusting edits; never delete caveats/reorder words. No audio/timing PASS claimed here.

## File input workflow (PREP ONLY)
1. `08_VOICE_SCRIPT.md`: exact original locked 55 paragraphs with silent act headings and administrative notes.
2. `08_HARRISON_TTS_CHUNK_01.txt` ... `05.txt`: input chunks by consecutive acts A00–A01, A02–A03, A04–A05, A06–A07, A08–A09; neither captions nor Shorts audio generated separately.
3. `08_HARRISON_TTS_MASTER_INPUT.txt`: clean concatenation of all five, no titles or SSML.
4. `08_HARRISON_CHUNK_MAP.csv` and `08_HARRISON_PARAGRAPH_MAP.csv`: paragraph and Shorts coverage.
5. `08_HARRISON_NORMALIZATION_AUDIT.csv`: exact reversible changes for quantities/dates.
6. After **new owner authorization of Stage09**: independent text/voice-read QA and provider-readiness. Before any paid generation name provider/model, #jobs, budget estimate and seek explicit owner approval.

**Never improvise music, sound effects, video generation, or branding from another repository. No paid action was performed.**
