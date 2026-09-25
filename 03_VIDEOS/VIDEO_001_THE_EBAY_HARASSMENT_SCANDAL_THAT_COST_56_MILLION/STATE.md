# VIDEO 001 — State

## Goal
The eBay Harassment Scandal That Cost $56 Million

## Current
- Status: IN_PREPARATION
- Stage 07 Final Script Lock: **PASS**
- Stage 08 Voice Script: **PASS**
- Stage 09 Voice QA + Lock: **PASS**
- Stage 10 Audio Master: **PASS / LOCKED**
- Stage 11 Transcript + Visual Timeline: **PASS / LOCKED**
- Stage 12 Visual Source / Generation Plan: **PASS / 115-BEAT FINAL ASSET PATH LOCKED**
- Current pipeline stage: 17_PACKAGING — **PASS / OWNER-APPROVED THUMBNAIL LOCKED**
- Canonical narration: `07_SCRIPT_FINAL.md`
- Final script length: ~2,321 words
- Performance review: PASS — 92/100

## Locked script status
`07_SCRIPT_FINAL.md` is now the only canonical narration text.

Historical drafts:
- `03_SCRIPT_V1.md`
- `05_SCRIPT_V2.md`

Do not generate final narration from those historical drafts.

## Stage 07 micro-edits applied
1. S02 background compressed immediately after the hook.
2. S03 first appearances now identify Wenig / Wymer / Baugh / Jones roles more clearly.
3. S09 summary-judgment explanation compressed without removing liability/fairness safeguards.
4. Existing ending preserved with no CTA before the final WHAT IT COST line.

## Claim traceability
All material facts remain inside the same S01–S12 section map used by CLAIMS_LEDGER.

No chronology, dollar figure, legal status or party position changed during Stage 07.

## Voice status
**VOICE LOCKED — HARRISON**

- Provider/catalog: Higgsfield
- Voice type: preset
- Voice ID: `573e5163-59b3-4926-aab1-951ef2985f81`
- Provider preview: https://d1xarpci4ikg0w.cloudfront.net/audio_voice_preset/preview/725aa234-8c64-4a87-8f5e-220aca1375f7.mp3
- Owner-approved same-text test: https://d8j0ntlcm91z4.cloudfront.net/user_3J3zfwu7kpgllQvPySWoLtXHwdR/hf_20260921_053343_e202b139-a5ae-4276-b3f7-109cb955909f.mp3
- Comparison job ID: `e202b139-a5ae-4276-b3f7-109cb955909f`
- Previous Bram lock: **SUPERSEDED BY OWNER**
- No new TTS generation authorized.

Stage 08 result:
- `08_VOICE_SCRIPT.md` created from the locked final script;
- spoken dates/years and unambiguous abbreviations normalized;
- section IDs preserved;
- no factual/legal wording changed;
- no SSML added before engine lock;
- pronunciation targets handed to Stage 09;
- no audio generated and no paid generation authorized.

Stage 09 result:
- semantic fidelity audit PASS;
- Stage 08 correction: 1999 → nineteen ninety-nine;
- dates/numbers/abbreviations QA PASS;
- high-confidence pronunciation locks recorded;
- speculative phonetic respellings prohibited;
- person-specific uncertain pronunciations carried to Stage 10 auditory QC;
- no audio generated.

Stage 10 result:
- Harrison production path: `text2speech_v2` + ElevenLabs;
- 4 approved production jobs completed successfully;
- production spend: **43.80 credits**;
- one owner-approved corrective patch: **0.60 credit**;
- total Stage 10 spend: **44.40 credits**;
- Part D 58.7M spoken-number ambiguity corrected before master lock;
- final master runtime: **15:57.414**;
- clipping: none detected;
- final master SHA-256: `00069b3717cb21a5134d0e0d7cb5ae15836f926a6286adfb66b7eb9103fa14d3`;
- master URI: https://d2ol7oe51mr4n9.cloudfront.net/user_3J3zfwu7kpgllQvPySWoLtXHwdR/4c1aa66b-440d-4fc7-ae95-78e60845ae5f.mp3;
- Stage 10: **PASS / AUDIO MASTER LOCKED**.

Stage 11 result:
- final Stage 10 audio SHA-256 reverified before alignment;
- **2,152** canonical narration words aligned to the final Harrison master;
- authored-script / ASR similarity: **0.944**;
- `11_CAPTIONS.srt`: **409** authored-text cues;
- `11_VISUAL_TIMELINE.csv`: **115** locked visual beats, median **7.42s**, max **16.86s**;
- **52** beats flagged HIGH legal sensitivity;
- timeline uses a compact codebook documented in `11_TRANSCRIPT_VISUAL_QA.md`;
- every visual beat remains `UNSOURCED` for Stage 12;
- no visual assets were searched, downloaded or generated;
- Stage 11: **PASS / VISUAL TIMELINE LOCKED**.

Stage 12 binding subtask result:
- **115 / 115** Stage 11 beats mapped to concrete visual treatment;
- **115 / 115** beats have source IDs and claim IDs;
- **87** beats use at least one GFX family;
- **69** require source-document treatment;
- **28** use rights-safe photo/archive material;
- **7** specifically require archive-web capture;
- **7** use editor-built map/location treatment;
- **12** beats allow clearly labelled reconstruction;
- **11** reusable source-gap packages identified;
- **5** reconstruction candidates covering **6** potential images if later approved;
- exact money, dates, legal labels and quotations remain editor-native;
- real-person likeness generation prohibited;
- no image/video generation submitted and no credits spent.

Shorts architecture backfill:
- **10** contiguous canonical Shorts locked to final Harrison audio;
- exact cuts: `11_SHORTS_CUT_MAP.csv`;
- no rewritten/reordered narration and no new TTS;
- Stage 12 beat map carries `short_ids` plus 9:16-safe requirements.

Stage 12 publication-safe source rebuild:
- rejected placeholder Stage 12B commit was reverted in corrective commit `7238548486b582401ce92934f8171b4790f9f64a`;
- S009 canonical visual source moved from the Justia mirror to the official GovInfo court PDF;
- official GovInfo/DOJ document crop plan is now defined by exact document pages;
- source-rights candidates are classified as U.S.-government/public-domain, CC0, CC BY-SA, editorial-fair-use-review, terms-unclear hold, or reference-only;
- Natural Earth is the preferred public-domain base for editor-built maps;
- publication-safe context candidates now exist for eBay HQ, Natick, insects/parcel/wreath, generic GPS device, generic office, and a Massachusetts fence;
- authentic DOJ/FBI case-evidence photo of the bloody pig Halloween mask + book is now selected for GAP-005; contextually wrong Saw/cosplay/ceremonial stock remains rejected;
- CM/ECF Document 986 (July 27, 2026) is captured as S020 and confirms dismissal with prejudice of all civil claims;
- no final visual asset has been marked acquired/approved and no generation has been submitted.

Source-rights rebuild result:
- **11 / 11 Stage 12 source gaps now have a publication-safe path**;
- this is a source/provenance milestone only — it does not mean final assets have been acquired, rendered or QC-approved;
- source-heavy copyrighted pages (EcommerceBytes, eBay statement, Reuters/Bloomberg) default to editor-native recreation/factual attribution rather than assumed screenshot reuse;
- authentic DOJ/FBI pig-mask evidence replaces the need for a generated pig-mask source visual.

Next action:
- **Stage 14 real assets COMPLETE: 12/12 GFX packages built and QC-passed; 4/4 licensed music tracks selected. Next stage is Stage 15 assembly/edit.**

## Spend lock — HARD

No new TTS/audio generation may be submitted without explicit owner approval of:
- provider/model;
- candidate count;
- test scope;
- estimated cost/credits.

Existing provider preview samples may be used for read-only shortlisting.

Prior paid voice-test submissions were made without owner spend approval. Do not treat that as precedent or implied authorization.

## Blockers
- Source-rights layer: none blocking; all 11 gaps have safe paths.
- **Stage 12C live-source pack is physically acquired in GitHub under `12B_SOURCE_ASSETS/`** with checksums and rights metadata.
- **Document crops: 19/19 rendered and QA-checked.**
- Visual proof set has not been built/owner-approved.
- Stage 13 remains NOT_STARTED.

## Important
The working title is still provisional and remains a Stage 17 packaging decision.


## Task-scope lock — HARD
For VIDEO_001, execute only the stage/action explicitly requested by the owner.

Do not:
- auto-advance to the next stage;
- generate paid or free samples without explicit instruction;
- create downstream artifacts early;
- treat a recommendation as authorization;
- continue after the requested deliverable is complete.

Voice selection is complete.

**Harrison is FINAL LOCK.**

The previous Bram lock is superseded.

Do not reopen selection, test substitutes, or generate audio unless the owner explicitly requests it.



## Stage 12C result
- **PASS — LIVE SOURCE EXPANSION COMPLETE**
- 115/115 beats audited.
- 93/115 beats have a live-source-led visual path.
- 22/115 are intentionally factual GFX-led with live source files retained underneath.
- 0 mandatory generation gaps remain before proof review.
- exact court/DOJ crops physically rendered into `12B_SOURCE_ASSETS/` (**19/19 crop QA PASS**).
- new primary/first-party sources S021–S026 added.
- no paid generation; Stage 12C spend: 0.
- Stage 13 remains NOT_STARTED.


## Stage 12D result
- **PASS — PROOF STYLE + PRODUCTION SYSTEM LOCKED**
- owner-approved proof direction converted into a binding style bible.
- channel `VISUAL_LOCK.md` extended to v1.1 with subtitle-safe rules.
- 7 reusable template families locked: T01–T07.
- 115/115 beats assigned a template family, frame type, primary live asset, GFX status and subtitle-safe rule.
- 16:9 bottom 20% (Y 864–1080) reserved for subtitles.
- 9:16 bottom 22% reserved for captions/platform UI.
- proof images are style references only; generated evidence/likenesses are prohibited in final factual production.
- Stage 12 remains IN_PROGRESS; Stage 13 remains NOT_STARTED.

## Stage 12E result
- **PASS — PRODUCTION ROLLOUT MAP COMPLETE**
- 115/115 beats have deterministic build instructions.
- each beat has layout variant, physical asset sequence, GFX action, motion sequence, transition, caption-safe rule and Shorts strategy.
- missing physical asset references: 0.
- three identical layout variants in a row: 0.
- three identical hero assets in a row: 0.
- no paid generation submitted.
- no visual render/build executed in this stage; this is the production execution map.
- Stage 13 remains NOT_STARTED.

## Stage 12E-R2 result
- **PASS — DOCUMENTARY RHYTHM CORRECTION**
- 45 beats redirected across existing T01–T07 families.
- longest continuous perceptual-mode run: 29.74 sec; runs >35 sec: 0.
- no three identical layouts or hero assets in a row.
- script/source/claim/legal locks unchanged.
- no paid generation; Stage 13 NOT_STARTED.

## Stage 12F result
- **PASS — GPT IMAGE PROMPT PACK COMPLETE**
- 115 / 115 detailed beat prompts.
- all prompts bound to approved Stage 12D style references SR-A..SR-E.
- semantic reference selection validated against physical Stage 12C assets.
- exact on-image text and legal guardrails locked.
- one-pass future cost: 57.5 credits.
- jobs submitted: 0; spend: 0.
- Stage 13 remains NOT_STARTED.

## Stage 12F-R2 Batch 1
- B001–B035 prompts corrected with the owner-approved sparse document/evidence rule.
- B006 and B018 accepted from the five-image test and marked TEST_PASS_REUSE.
- New jobs required for Batch 1: 33.
- New Batch 1 spend ceiling: 16.5 credits (below the previously approved 17.5-credit ceiling).
- No automatic retries or extra variants are authorized.

## Stage 12F-R2 Batch 1 generation
- **COMPLETE — OWNER QC PENDING**
- 35 scene outputs present for B001–B035.
- 33 new Higgsfield GPT Image 2 jobs completed; 0 provider failures.
- B006 and B018 reused from accepted test outputs.
- new spend: 16.5 credits; effective Batch 1 scene cost including reused test jobs: 17.5 credits.
- no retries or extra variants were submitted.
- Stage 13 remains NOT_STARTED.

## Stage 12F-R2 Batch 1 visual QC
- **PARTIAL PASS — CORRECTION REQUIRED**
- PASS: 7
- EDIT_FIX: 16
- REGEN: 12
- QC spend: 0 credits.
- no regeneration submitted.
- Batch 2 blocked.
- Stage 13 remains NOT_STARTED.

## Stage 12F-R3 five-scene generation
- 5 / 5 jobs completed.
- B008, B017, B026, B029, B034.
- spend: 2.5 credits.
- no retries.
- visual QC pending.
- Batch 2 remains blocked.

## Stage 12F-R4 full beat-to-script audit
- **COMPLETE / CANONICAL PLANNING LAYER**
- 115/115 beats audited against locked narration.
- 115/115 final-frame rows rebuilt.
- 115/115 physical source bindings validated.
- 115/115 prompts/build instructions rebuilt from scratch.
- zero missing physical source bindings.
- zero “blank plate / insert source later” workflows.
- old Stage 12F prompt pack is superseded for future production.
- generation spend in R4: 0 credits.
- Stage 13 remains NOT_STARTED.

## Stage 12F-R5 115-prompt pack
- 115/115 ready production prompts created.
- owner-supplied style refs uploaded to Higgsfield and locked by media ID.
- 115/115 prompts contain ATTACH source list.
- text-heavy document sources require tight crop before job.
- 115/115 prompts reserve bottom >=20%, target 22%, for subtitles.
- source material must be inside final frame; no later insertion workflow.
- prompt QA 115/115 PASS.
- generation spend: 0.
- generation is NOT authorized by this stage.

## Stage 12F-R5 representative test10
- 10/10 representative frames completed.
- all seven T01–T07 frame families are covered across the test set.
- provider failures: 0.
- retries: 0.
- spend: 5.0 credits.
- further R5 generation blocked pending visual QC.

## Stage 12F-R5 Test10 script QC
- 10/10 frames checked against locked narration.
- PASS: 5
- EDIT_FIX: 3
- REGEN: 2
- hard rejects: B018, B041.
- additional QC spend: 0 credits.
- R5 full production remains blocked.

## Stage 12F-R6 prompt pack
- 115/115 prompts rewritten.
- factual references first; style reference last.
- style refs are explicitly non-factual and forbidden from donating subject matter.
- raw PDF/HTML inputs removed from model attachments.
- document inputs require tight pre-crop before job.
- bottom 22% subtitle-safe.
- Test10 defects B007/B008/B018/B024/B041 explicitly corrected.
- generation spend: 0.
- no generation authorized.


## Stage 12F-R6 pipeline repair audit
- corrected an overclaim in the prior R6 status: structural prompt QA was not equivalent to semantic/source/input QA;
- 115/115 beats now have explicit narration → source-plan QA in `12F_R6_SOURCE_BINDING_QA.csv`;
- three clean content-neutral style references are designed in `12F_R6_STYLE_ONLY_REF_DESIGN.md` but **not generated**;
- all old R5 style media IDs are retired from future R6 production jobs because of demonstrated subject leakage;
- 115/115 production instructions are rewritten in `12F_R6_HIGGSFIELD_PROMPTS.csv`;
- B038, B042, B047 and B048 receive explicit semantic source repairs; B041 fix retained;
- document/legal preprocessing is enumerated in `12F_R6_INPUT_PREP_PLAN.csv`; raw PDF/HTML is never model input;
- B088–B101 stay deterministic editor GFX; B077/B078/B102/B103 are editor-only legal/reference treatments;
- production-prompt average reduced from ~3357 chars to ~993 chars;
- execution inventory: 90 blocked Higgsfield candidates / 25 editor-only;
- prep inventory: 69 beats, 146 prep/source-lock rows;
- neutral refs generated: 0/3;
- paid jobs: 0; credits: 0; retries: 0;
- new paid Test10 is not yet authorized and remains blocked until neutral refs + selected Test10 input prep assets are owner-approved and QC-checked.


## Stage 12F-R7 Batch15 generation + QC
- Generated beats: B002, B003, B005, B009, B010, B011, B012, B013, B014, B015, B016, B017, B019, B020, B021.
- Model: Higgsfield GPT Image 2; 1K Low; 16:9.
- Jobs: 15/15 completed; provider failures: 0; retries: 0.
- Spend: **7.5 credits** (15 × 0.5).
- QC PASS: B002, B005, B009, B010, B011, B013, B016, B019, B020, B021.
- HOLD: B003 source-authenticity; B012 rhythm/repetition; B014 source mismatch; B015 rhythm/repetition.
- HARD REJECT: B017 generated an unauthorized male portrait / likeness-like subject.
- Accepted-ready total: **24 / 115**.
- No automatic retry or regeneration authorized.


## Stage 12F-R7 Batch35 generation
- Scope: 5 owner-authorized regens (B003, B012, B014, B015, B017) + 30 previously ungenerated beats (B022-B054 selection recorded in batch CSV).
- Model: Higgsfield GPT Image 2; 1K Low; 16:9.
- Jobs: **35/35 completed**; provider submission failures: 0; provider completion failures: 0; retries: 0.
- Spend: **17.5 credits** (35 × 0.5).
- B014 used a newly prepared authentic S009 court-record crop to address the prior source mismatch.
- Visual QC is **not yet locked** for this batch; provider completion is not a PASS verdict.
- No automatic retry or additional generation authorized.


## Stage 12F-R7 Batch35 visual QC
- QC scope: all 35 Batch35 outputs checked against locked beat meaning, source intent, legal/factual guardrails, subtitle-safe zone and sequence rhythm.
- Result: **30 PASS / 5 HOLD / 0 REJECT**.
- All five prior problem-frame regens now PASS: B003, B012, B014, B015, B017.
- HOLD_SOURCE_MISMATCH: B026, B032, B042, B046, B047.
- No visual hard rejects in this batch.
- Accepted-ready total across VIDEO_001: **54 / 115**.
- Unfinished: 61 beats = 5 held generated frames + 32 ungenerated Higgsfield candidates + 24 deterministic editor/source builds.
- QC spend: 0; retries submitted: 0.


## Stage 12F-R7 Final61 completion + QC — 2026-09-23
- Starting point: **54 / 115** accepted-ready frames.
- Owner authorization: close all remaining 61 beats under a **40-credit cap**.
- Paid generation: **61 jobs × 0.5 = 30.5 credits**, Higgsfield GPT Image 2, 1K Low, 16:9.
- Provider result: **61/61 completed**, 0 submission failures, 0 completion failures, **0 automatic retries**.
- Visual QC: 60 generated outputs PASS directly.
- B101 generated output invented **$58.7M** and failed the factual lock. No paid retry was used. It was replaced at **0 additional credits** with deterministic media **27b4440d-ead7-4a52-9ec9-dbf9a089b4de**, preserving the separate $3M criminal DPA and $55.7M civil settlement package.
- Final visual status: **115 / 115 beats final-ready**.
- Completion-run spend: **30.5 credits**, 9.5 credits below the owner cap.
- Video generation used: **NO**.
- Do not begin assembly/montage without explicit owner instruction.


## B101 canonical replacement — 2026-09-23
- Owner requested replacement of only B101; no other frame regenerated.
- New B101 was generated in ChatGPT, visually QC'd, resized to 1920×1080, and uploaded into the Higgsfield media library.
- Canonical B101 media: **20f94d5e-d9a5-4af0-989d-7d2ec28e1244**.
- QC PASS: exact three-track structure — SEVEN GUILTY PLEAS / $3M CRIMINAL DPA / $55.7M CIVIL SETTLEMENT PACKAGE; **no $58.7M combined figure**; subtitle-safe lower zone preserved.
- Previous deterministic B101 replacement remains historical fallback only and is no longer canonical.
- VIDEO_001 visual status remains **115 / 115 final-ready**.

## Stage 14 production packaging — 2026-09-23
- Document Plan: **LOCKED** — 23 document/source packages with source labels, rights class and legal guardrails.
- Graphics Plan: **LOCKED** — 12 editor-native packages covering message chronology, GPS distinction, DPA, civil-liability ladder, settlement timeline, exact money breakdown and ending recap.
- Overlays: **LOCKED** — 115/115 beats mapped for source/date/legal-status/reconstruction metadata; bottom 22% caption-safe rule preserved.
- Music/SFX: **CUE SHEET LOCKED** — 12 section cues across 00:00.000–15:57.414; actual track acquisition/license logging occurs during Stage 15 assembly.
- No image/video/audio generation and no credits spent in Stage 14.
- Stage 15 assembly is **NOT STARTED**.


## Stage 14 real asset lock — 2026-09-23
- 12/12 real GFX packages built: master PNG, transparent overlay, animation spec, and 8s/25fps preview.
- Technical/contact-sheet QC: PASS.
- Four licensed Scott Buckley tracks selected for the four music families and uploaded to Higgsfield media.
- License class: CC BY 4.0; YouTube description attribution required.
- Paid generation spend: 0.
- Stage 15 assembly: NOT STARTED.


## Stage 14 final GFX replacement + music audition archive — 2026-09-23
- Retired the earlier editor-native GFX placeholder masters.
- Canonical GFX selection is now **12/12 generated in-chat frames**, all QC PASS.
- Canonical GFX archive: media `4eb621b3-decd-427f-8730-580d55779b91`, `VIDEO_001_STAGE14_GFX_12_FINAL.zip`.
- Four Scott Buckley tracks are downloaded and packed for owner audition.
- Music audition archive: media `49b0482b-026a-441a-b514-ee2b35278843`, SHA-256 `b7a90eda0acaf602a693ddfd3836561e5dea5408a5c4f1f5c3b1cd05a189e97e`.
- Licenses re-verified from official Scott Buckley pages: CC BY 4.0, YouTube-description attribution required.
- Stage 15 assembly remains **NOT STARTED**, but the music gate is cleared: owner provisionally approved the current 4-track set on 2026-09-24.


## Music owner approval — 2026-09-24
- Current 4-track music set: **PROVISIONALLY APPROVED BY OWNER**.
- Stage 14 final GFX: **12/12 LOCKED**.
- Stage 15 assembly gate: **CLEARED / READY TO START**.


## Stage 15A result — 2026-09-24
- **COMPLETE — PICTURE ASSEMBLY REVIEW MASTER READY**
- 115/115 beats resolved and assembled.
- 12/12 final generated GFX inserted at locked anchor beats.
- 6 deterministic authentic-source/editor frames used where required.
- Harrison audio is the only audio layer in 15A.
- Review master: `VIDEO_001_STAGE15A_PICTURE_ASSEMBLY_V1_1080P.mp4`
- media id: `174a262e-958f-4b63-b215-1a6ab385b755`
- measured runtime: **957.371 sec** vs locked **957.414 sec** (−0.043 sec).
- review encoding uses VFR hold frames; final delivery after 15B/15C must be **CFR 25 fps**.
- contact-sheet spot QC: no obvious black-frame holes / missing sampled sections.
- captions, Stage14 metadata overlays, music and SFX are intentionally absent.
- Stage 15A spend: **0 credits**; no generation performed.
- **Stage 15B COMPLETE — owner review of caption/overlay cut pending.**


## Stage 15B result — 2026-09-24
- **COMPLETE — TECHNICAL PASS / OWNER REVIEW PENDING**
- Final successful GitHub Actions run: `36018740428`.
- Artifact: `10817420859` / `VIDEO_001_STAGE15B_REVIEW_V1`.
- Review master: `VIDEO_001_STAGE15B_REVIEW_V1_1080P.mp4`.
- CFR **25 fps**, 1920×1080 H.264.
- Runtime: **957.370 sec** vs 957.414 locked target (−0.044 sec).
- Harrison remains the only audio content; no music/SFX yet.
- Captions: white base + channel-red active word; 409 cues / 2151 word events; 0 fallback cues.
- 83 metadata/source/legal/reconstruction overlay events.
- B104 inequality fallback glyph corrected deterministically in the Stage 15B layer.
- Stage 15B spend: **0 credits**; no generation used.
- **Stage 15C NOT STARTED.**


## Stage 15B caption palette correction — 2026-09-24
- Legacy orange highlight removed.
- Captions now match WHAT IT COST palette: **#EDEDED base + #D32222 active word**.
- Corrected Actions run: `36021465130`.
- Corrected artifact: `10817420859`.
- Corrected review SHA-256: `a4626fed53d09e69cbc59e089f5490695ea7f5243dcec0f41bf7fed72156cf33`.


## Stage 15C result — 2026-09-24
- **COMPLETE — TECHNICAL PASS / OWNER LISTEN REVIEW PENDING**
- Run `36033748640` succeeded.
- Full artifact `10823619066`; lite artifact `10823599106`.
- 12/12 locked music cues assembled from the owner-approved four Scott Buckley tracks.
- 20 restrained editor-native SFX accents; no prohibited/horror/gavel/cash-register/siren sounds.
- VO-keyed sidechain ducking + manual legal/quote/money reductions applied.
- Lite QC measured **−14.3 LUFS integrated / −2.5 dBFS true peak / 2.3 LU LRA**.
- Runtime **957.370 sec** vs locked **957.414 sec** (−0.044 sec).
- Stage 15C spend: **0 credits**; no model generation.
- **Final-master/QC stage NOT STARTED.**


## Stage 15C music rejection + replacement audition — 2026-09-24
- Owner rejected the current Scott Buckley score as unsuitable for the film.
- Previous Stage 15C mix remains a historical review only and is **NOT APPROVED / NOT FINAL**.
- Replacement source moved to **Mixkit Stock Music Free License** candidates.
- Audition workflow run: `36036170552` — SUCCESS.
- Full audition artifact: `10825021726` — 8 full tracks + 8 normalized previews + license/map notes.
- Reel artifact: `10824876844` — 8 × 28-second normalized excerpts.
- New score mix is **NOT STARTED** until owner selects/approves tracks.
- No credits/model generation used.


## Stage 15C no-music SFX proof — 2026-09-24
- Built a **190.023 sec** proof using real Stage15B picture/captions + Harrison + editor-native SFX only.
- **No music** is present.
- Proof run `36044425718` succeeded.
- Proof artifact `10827149357`; SFX-pack artifact `10827199168`.
- SFX pack: room tone / paper tick / page rustle / keyboard cluster / dry click / low transition / abstract digital-delete / soft whoosh.
- No stock SFX, no third-party sample library, no model generation, no paid credits.
- Measured proof loudness: **−16.46 LUFS integrated / −3.64 dBFS true peak**.
- Owner review required before extending this sound-design philosophy to the full film.


## Stage 15C SFX-only proof V2 — 2026-09-24
- V1 was judged too quiet by owner.
- V2 removes room tone completely and raises working SFX approximately +10 dB, with stronger source synthesis for audible but restrained accents.
- Run `36046422755` succeeded.
- Proof artifact `10828686824`; SFX-pack artifact `10828442441`.
- Proof runtime **190.023 sec**, music **NONE**.
- Audio QC: **−16.4 LUFS integrated / −3.8 dBFS true peak**.
- Final Stage 15C remains NOT APPROVED until owner review.


## Stage 15C SFX-only proof V2 owner verdict — 2026-09-24
- Owner listened to V2 and reports the SFX are still effectively inaudible.
- V2 is therefore **REJECTED FOR AUDIBILITY** despite technical render/QC passing.
- Historical reference only: run `36046422755`, proof artifact `10828686824`, SFX-pack artifact `10828442441`.
- Whole-program loudness values did not prove local SFX audibility under Harrison.
- Room tone remains removed.
- Music remains rejected.
- Current direction remains **voice + silence + sparse SFX**, but SFX audibility must be solved and verified in-context before any further full-film Stage 15C work.
- Final Stage 15C: **NOT APPROVED / NOT FINAL**.

## Stage 15C controlled SFX audibility microtest V1 — 2026-09-24
- **TECHNICAL PASS / OWNER LISTEN + STYLE REVIEW PENDING.**
- Workflow run `36049666541` succeeded from trigger commit `812d7df6b3271e9dfa195972432203f798dd3e51`.
- Scope: **34.000 sec** of the approved Stage15B opening, film `00:00.000–00:34.000`.
- Music: **NONE**. Room tone: **NONE**. Paid/model generation: **0 credits**.
- Four sparse editor-native effects were tested both solo and in the real Harrison mix.
- SOLO artifact: `10830026745` / `VIDEO_001_SFX_SOLO_REFERENCE_V1`.
- IN-CONTEXT artifact: `10829862172` / `VIDEO_001_SFX_IN_CONTEXT_PROOF_V1`.
- QC artifact: `10829897002` / `VIDEO_001_SFX_MICROTEST_QC_V1`.
- In-context checkpoints:
  - `00:06.340` paper tick — SFX peak −4.50 dBFS vs Harrison −3.46 dBFS; Δpeak −1.04 dB; preflight PASS.
  - `00:07.760` page rustle — SFX peak −5.00 dBFS vs Harrison −1.96 dBFS; Δpeak −3.04 dB; SFX RMS is +5.32 dB above local Harrison RMS; preflight PASS.
  - `00:21.900` soft whoosh — SFX peak −7.00 dBFS vs Harrison −5.53 dBFS; Δpeak −1.47 dB; SFX RMS is +3.33 dB above local Harrison RMS; preflight PASS.
  - `00:30.120` dry click — SFX peak −4.00 dBFS vs Harrison −4.31 dBFS; Δpeak +0.31 dB; preflight PASS.
- No Harrison ducking was used; the test checks whether the SFX themselves can remain clearly present against the approved narration.
- This is an **audibility/style gate only**. It does **NOT** approve Stage 15C and does **NOT** authorize scaling the SFX design to the full film.
- Post-encode QC was also performed on the actual downloaded MP4 artifacts: all four SFX survived AAC/stereo/limiter encoding and remain non-silent at their expected checkpoints (context event-window peaks approximately −7.03 / −3.20 / −6.80 / −6.48 dBFS).
- Owner perceptual/style approval is still required despite the technical and post-encode passes.
- Current Stage 15C status remains **OPEN / NOT APPROVED / NOT FINAL**.



## Stage 15C final audio direction — VOICE ONLY LOCK — 2026-09-24
- Owner explicitly removed **all music and all sound effects** from VIDEO 001.
- Canonical audio policy: **Harrison narration only**.
- Music tracks: **0**.
- SFX events: **0**.
- Room tone / ambience bed: **0**.
- No ducking, music fades, SFX stems, transition hits, whooshes, clicks, paper sounds, or tonal accents are permitted in the canonical film.
- The approved Stage15B master already contains exactly this audio configuration: Harrison only.
- Therefore Stage15C requires **no new render and no new audio processing**. Re-encoding would only create avoidable quality loss.
- Canonical picture/audio basis remains:
  - run `36021465130`;
  - artifact `10817420859`;
  - file `VIDEO_001_STAGE15B_REVIEW_V1_1080P.mp4`;
  - SHA256 `a4626fed53d09e69cbc59e089f5490695ea7f5243dcec0f41bf7fed72156cf33`;
  - 1920×1080 / CFR25 / AAC 44.1 kHz mono / 957.370 sec.
- All previous music/SFX attempts are **REJECTED / RETIRED / NON-CANONICAL**.
- Active music/SFX plans, builders, triggers and workflows were removed from current `main`.
- Historical commits and expired/expiring Actions artifacts remain audit history only and must never be used as production inputs.
- Stage 15C: **PASS / VOICE-ONLY LOCKED**.
- Do **not** start final-master/QC or the next stage without explicit owner instruction.


## Stage 16 final fact / legal / provenance refresh — 2026-09-24
- **FACT / LEGAL: PASS — NO EDIT REOPEN REQUIRED.**
- **COPYRIGHT / PROVENANCE: PASS WITH MANDATORY ATTRIBUTION CARRY-FORWARD.**
- 31/31 claims reviewed; material fact/legal changes: 0.
- 115/115 final beats registered in populated `ASSET_MANIFEST.csv`.
- Final inventory: 96 Higgsfield-generated stills + 1 OpenAI B101 override + 12 editor-native GFX + 6 deterministic editor builds.
- DOJ date anomaly documented: current overview says January 2023; official Jan. 11, 2024 release/DPA/docket establish January 2024. Film remains correct.
- Mandatory Stage17/18 publication credits:
  - JenniferKL / Wikimedia Commons — Devin Wenig photo — CC BY-SA 4.0 — cropped/graded.
  - Coolcaesar / Wikimedia Commons — eBay headquarters 2018 — CC BY-SA 4.0 — cropped/graded.
- Final audio remains Harrison only; music/SFX/ambience remain 0.
- Stage16 made no media/render changes.
- **Next action: await explicit owner instruction before Stage17 Packaging.**
- Stage17: **NOT STARTED**.


## Stage 17 Packaging — 2026-09-24
- **PASS / LAUNCH PACKAGE LOCKED**.
- Final title: **The eBay Harassment Scandal That Cost $56 Million**.
- Final thumbnail thesis: **CRITICISM → SECURITY**.
- Three materially different packaging families developed and QC-reviewed.
- Deterministic 3840×2160 final thumbnail master built with 0 generation credits; editable SVG stored as `17_THUMBNAIL_FINAL.svg`.
- Mobile 320×180 readability: PASS.
- Final YouTube description locked at 2711 characters with 12 manual chapters, current legal caveats, key sources, AI/reconstruction note and both mandatory CC BY-SA credits.
- YouTube metadata lock: English (US), Education, not made for kids, no age restriction, no paid promotion, Standard YouTube License, AI use disclosure = YES.
- Tags intentionally limited; official YouTube guidance treats title/thumbnail/description as more important than tags.
- 10/10 Shorts receive separate Stage17 packaging titles/hooks in `17_SHORTS_PACKAGING.csv`.
- Stage18: **NOT STARTED**.
- Next action: await explicit owner instruction before Stage18 Upload / Prepublication Package.


## Stage 17 thumbnail owner rejection — 2026-09-24
- Owner rejected **all** Stage17 thumbnail concepts and the previously selected launch thumbnail.
- TN-A / TN-B / TN-C / THUMB_FINAL_CRITICISM_TO_SECURITY are historical rejects only.
- No thumbnail is currently canonical.
- Existing title/description/metadata drafts remain untouched.
- Stage17 is **REOPENED / BLOCKED ON THUMBNAIL OWNER APPROVAL**.
- Stage18 remains **NOT STARTED**.


## Stage 17 final thumbnail owner approval — 2026-09-24
- Owner explicitly selected the **SCANDAL / $56M investigative-board composite** as final.
- Canonical master: 1672×941 PNG.
- Master SHA-256: `0686bb5c0476b355a179ef2a93f548c3da48bdaade0d518f7a674bab83c519f2`.
- GitHub visual reference: `17_THUMBNAIL_FINAL_APPROVED_PREVIEW.jpg`.
- Previous Stage17 thumbnail rejects remain historical only.
- Title/description/metadata remain as previously prepared.
- Stage17 is **PASS / OWNER-APPROVED LAUNCH PACKAGE LOCKED**.
- Stage18 remains **NOT STARTED** pending explicit owner instruction.
