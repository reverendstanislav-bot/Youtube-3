# VIDEO005 — Stage11 transcript + visual timeline

**2026-10-14 | Stage11 structural timeline PASS, ASR WORD TIMINGS PROVISIONAL.** No narration, audio, licensed visuals, scenes, Shorts or video was generated at this stage. The picture is NOT edited or rendered.

**Canonical script:** `07_SCRIPT_FINAL.md`, 55 V4.4 paragraphs, 2,551 written words. **Master:** `VIDEO005_HARRISON_QWEN06_STAGE10_AUDIO_MASTER_48K_MONO.wav`, WAV SHA-256 `0db92584d7eddd70914b800cb981250463d222cc4db1245444a8153c782847a0`, 995.03 seconds, mono PCM16 48kHz. **Four Shorts only:** S01, S03, S05, S08.


## Exact runtime and mapped evidence
- **10 acts / 55 narrated paragraphs / 55 source-aware editorial scene cues / 110 proposed picture placements**. The two picture placements per paragraph are *visual intentions*, not 110 image generation jobs or 110 already-authored assets.
- Master audio real duration **995.03 sec (16:35.03)**. At **25fps**, the frame-complete visual timeline is **24,876 frames = 995.04 seconds**. The last **0.01sec** is video frame quantization, *not* fabricated narration. **0 scene frame gaps / 0 scene overlaps**. A separate Stage15 end screen is not inserted here.
- Word-level transcript is aligned to the **actual Stage10 master offset positions**, respecting five source WAV segments and four inserted 120ms inter-part pauses. There are **2,627 TTS whitespace-word rows**, of which **2,451** received direct Whisper token anchors and **176** are explicitly marked `ASR_INTERPOLATED_UNMATCHED_TOKEN`. The latter are **NOT** claimed to have exact ASR-timed syllables. No missing canonical paragraphs.
- Independent `faster-whisper tiny.en` automatically timed transcription of each of the five real source WAVs underlies the word alignment. Per-chunk lexical tokens and accuracy statistics are in `11_ALIGNMENT_QC.json`; old Release ASR additionally passed the Stage09 multiword-content screening. Source script numerals (e.g. `$179,047,998.64`) are semantically preserved from locked V4.4 but may cause ASR normalization/interpolation.
- **Seven boundary-watch paragraphs**: `A04-P01`, `A04-P03` (selected S05), `A06-P03`, `A07-P02`, `A07-P05`, `A07-P06`, `A08-P06`. These have a weak first or last ASR token or incomplete match. They are explicitly flagged, **not an automatic finding of missing speech**. Stage15 should audition/correct precise cut/caption anchors before export.
- Paragraph SRT is a **55-cue text-aligned DRAFT only**, not platform-ready captions; real subtitle segmentation/word highlighting later must be independently QCed. No narration subtitles burned into any images or picture frames in this stage.

## Timed act architecture
| Act | Master time (approximately) | Role |
|---|---|---|
| A00 | 00:00.00–01:34.08 | 14k Google copied files, personal judgment and separate Uber payment hook |
| A01 | 01:34.08–03:12.16 | LiDAR, Dec 2015 copying, Otto founding and market stakes |
| A02 | 03:12.16–05:10.12 | Conditional acquisition max ~$680m vs $100k initial cash, risk terms |
| A03 | 05:10.12–07:01.24 | Stroz due diligence and limited finding, Uber board decision |
| A04 | 07:01.24–08:38.88 | Wrongly sent PCB design email, competing source lines, Waymo claim |
| A05 | 08:38.88–10:09.20 | Five reported disks and permissive evidentiary inference |
| A06 | 10:09.20–11:34.44 | Waymo/Uber equity settlement no verdict; separate Google obligations |
| A07 | 11:34.44–13:27.44 | Levandowski's separate personal civil judgment; criminal track |
| A08 | 13:27.44–15:12.32 | Disputed indemnity vs new 2022 sealed Global Settlement |
| A09 | 15:12.32–16:35.04 | Tax afterlife in 2025 and source-constrained final cost |

`11_ACT_TIMELINE.csv` contains the exact 25fps scene boundaries. The `11_VISUAL_TIMELINE.csv` has a numbered **SC001–SC055** for every locked script paragraph; `11_VISUAL_PLACEMENTS_DRAFT.csv` has **VP001–VP110**, two distinct editorial purposes per paragraph with frame-exact time ranges. These are not 110 repeated placeholders or a requirement to present 55 static slides: Stage12 may break source appearances into natural multiple views and must distinguish authentic document crops, editor graphics and sourced contextual images.

## Native four Shorts — production timing map
Use exactly `11_SHORTS_CUT_MAP.csv`. All cuts are 25fps-aligned candidate windows from the same uninterrupted master paragraphs (no Short TTS, splice or rewrite). **These are not final exported files, and 3-second CTA is a planning allowance only.**
| Short | Paragraph | Provisional master in–out | Voice cut | Including *planned* 3s end card |
|---|---|---|---:|---:|
| **S01** | A00-P01 | **00:00.00–00:21.44** | **21.44s** | **24.44s** |
| **S03** | A02-P03 | **03:49.28–04:11.88** | **22.60s** | **25.60s** |
| **S05** | A04-P03 | **07:37.28–08:00.04** | **22.76s** | **25.76s** |
| **S08** | A08-P04 | **14:18.28–14:38.72** | **20.44s** | **23.44s** |

All projected totals are below **30.0s**, but their final exported duration is **NOT measured** and S05's last syllable was not a direct ASR anchor; audition exact boundaries and leave appropriate air. Do not attach new narration or fabricate an outro voice.

## Visual provenance and editorial behavior
- The *proposed* evidence class in `11_VISUAL_TIMELINE.csv` or `11_VISUAL_PLACEMENTS_DRAFT.csv` is an instruction for Stage12 research, **not proof a source, crop or license has been obtained or cleared**. Court/legal documents require genuinely extracted pages and dated/source-labeled callouts. Editor graphics must not masquerade as authentic documents.
- Preserve **all distinctions**: copying ~14k Google files ≠ Uber product-use verdict; share settlement ~$245m ≠ jury fine; **$179,047,998.64 is a personal Google employment civil award**, not an Uber fine; reported disks' contents were never established; Uber's **sealed 2022 Main Payment** was under the new Global Settlement **not** a judicial enforcement of the disputed 2016 indemnity; separate $2m supports the bankruptcy plan; 2025 tax holding did not calculate final tax bill.
- Documentary art direction: evidence-first, real contracts/order pages only with provenance, restrained editorial motion, no jumpy zooms, no shaker, no pseudo-forensic reconstructions presented as facts. **Do not burn automatic speech subtitles inside assets**. Where possible change visual evidence at a factual reveal, not every arbitrary sentence.
- Scene and visual placement frame bounds **partition the full 25fps canvas exactly**, but current audio is separate and retains 16:35.03 real duration, so picture 0.01s tail pad is expected. In Stage15 insert the approved end screen ONLY after film narrative; this Stage11 contains no extra silent end-card track.

## Files, traceability and remaining QA
- `11_BUILD_TIMELINE.py`: auditable local reconstruction tool. Inputs: exact Stage07 and Stage08 texts, `07_LOCKED_PARAGRAPH_CLAIM_TRACE.csv`, Stage10 `stage10_build_manifest.json`, five timestamped ASR segment JSONs and the source WAVs. Reconstruct from master/source hashes, not from previous chat memory.
- `11_WORD_LEVEL_TRANSCRIPT.json.gz` and `11_WORD_TRANSCRIPT.csv.gz`: complete **2,627-row** machine-readable source-word-aligned draft; decompress gzip. Contains exact `timestamp_status` per word; never pretend interpolated timestamps were ASR matches.
- `11_PARAGRAPH_ALIGNMENT.json.gz`: each of 55 paragraphs with confidence, aligned words, exact 25fps scene bounds and source claim IDs.
- `11_ALIGNMENT_QC.json`: numerical reconciliation and source anchor flags.
- `11_VISUAL_TIMELINE.csv`, `11_VISUAL_PLACEMENTS_DRAFT.csv`, `11_ACT_TIMELINE.csv`: editable review/source plan across 995.04s.
- `11_SHORTS_CUT_MAP.csv`: the **only four** authorized native Short speech-extract boundaries.
- `11_CAPTIONS_DRAFT.srt`: **draft paragraph-only**, not final publish-caption master or proof of fully correct timing.
- A packed ZIP of complete raw files (including uncompressed word JSON+CSV) may also be used by the editor; GitHub is canonical for statuses and flags.

**G11 verdict:** **PASS_STRUCTURAL_TIMELINE** (55/55 scenes, all 10 acts, 110 picture intentions, 100% 25fps coverage). **WORD_ANCHORS_ASR_PROVISIONAL** (176 unmatched word-token interpolations, seven paragraph flags) and **SHORT_EXPORTS_NOT_VERIFIED**. Stage12 can plan source acquisition with the editorial timeline; Stage15 must audition/fix cut edges, finalize English captions, render four vertical cuts and recheck <=30.0s including CTA/end. No TTS, image/video generations, master audio modification or paid credits in Stage11.