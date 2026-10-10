> Final production-state refresh: **0bc1e6f**. Initial findings at67b940a are historical where superseded. Valve audio technical verification is now complete; full listening/Resolve runtime/final release gates remain open. Four production Shorts. See [final source reconciliation](evidence/repo_refresh_0bc1e6f.md).

﻿# 08 — Production efficiency and control-system audit
Audit date: 2026-10-10, America/Los_Angeles. Baseline `67b940a1389ca4ffcdf8c82e6f9afef7bc11ed74`. Scope: read-only production forensic review and this assigned report. No media generated, provider job submitted, billable credit used, upload modified, canonical artifact changed, commit or push.

## Executive finding
The strongest verified process defects are status drift, repeated visual text/layout failures and weak asset persistence. These are demonstrated by repository evidence. Whether they caused low views is NOT established. Strong legal guardrails and independent current-version review exist; implementing them consistently is the opportunity.

A short documentary is not ready because its script scores 90+, a provider says COMPLETED, or an image batch has 0 current rejects. Text acceptance, media integrity, legal freshness, creative approval and publication settings are separate gates.

## What was measured and what was not
Reviewed AGENTS, Foundation, Core schemas/gates, manifests/STATE/index, current and historical reviews, voice/master records, visual QC waves, job/result ledgers, asset manifests, version logs and publication reconciliation. Exact evidence locations below refer to the baseline SHA. Historical reported QC is identified as historical, not rerun verification.

- Labor tracking by stage: NOT AVAILABLE. Git timestamps/version dates measure calendar intervals, not focused labor.
- Complete provider invoice/credit-account reconciliation: NOT AVAILABLE. Credits below are episode record totals/quotes, not US dollars or a balance audit.
- Binary review/decode/auditory approval: NOT performed by this production-review agent. Existing checksums/probe/QC are evidence of historical checks; a URI or hash is not proof current download works.
- CDN resolution failure for 004 is recorded in repository, not independently retried here; root audit may add live access evidence.
- Structural integrity is distinct from release readiness and measured audience performance.

## Current status and misleading handoffs
|Episode|Observed repository condition|Consequence|Disposition|
|---|---|---|---|
|001 eBay|Published; stages/locks largely reflect final voice-only master; earlier music/SFX proofs are explicitly retired|Good example of keeping rejected history separate, but lengthy STATE still mixes many superseded directions|Preserve final lock; move historical narrative out of concise current handoff on future authorized maintenance|
|002 Adobe|Published/Stage 19, but Stage 16–18 NOT_STARTED, edit/release locks false; old invalidated assembly fields prominent|An operator resuming from manifest cannot safely identify a fully certified final release|Reconcile from actual final evidence; publication does not retroactively pass rights/legal/settings gates|
|003 DistroKid|Published/Stage 19, Stage 15–18 NOT_STARTED, visual_assets=false despite final 120 PASS; old generated-awaiting-QC blocks coexist with final lock|Queue may regenerate or reapprove completed work, or presume release certification that does not exist|Resolve active-versus-historical state explicitly; retain unresolved checks as unknown|
|004 Valve|STATE says 3 voice jobs complete/master pending; manifest Stage 09/Stage 10 NOT_STARTED; index Stage 08|Concrete duplicate-spend risk if next operator trusts outdated next_action|Resume retrieval of exact existing job IDs; never resubmit because download failed|
|005 Waymo|LockedT005 backlog entry, no registered 005 package|A planned topic cannot provide production backlog or a promised release date|Qualification/research only after separately authorized; preserve approved order|

Evidence: `02_PIPELINE/VIDEO_INDEX.csv:2–5`; `03_VIDEOS/VIDEO_002_ADOBE_FIGMA_FAILED_DEAL_COST_1_BILLION/manifest.yaml:7–11,30–34,45–70`; `03_VIDEOS/VIDEO_003_UMG_DISTROKID_AI_COPYRIGHT_LAWSUIT/manifest.yaml:7–11,30–49,312–401`; `03_VIDEOS/VIDEO_004_VALVE_STEAM_MASS_ARBITRATION/STATE.md:3–29`, `manifest.yaml:11–12,25–27`. All VIDEO paths are under `03_VIDEOS/`; full folder names are listed in the index.

Both `03_VIDEOS/VIDEO_002_ADOBE_FIGMA_FAILED_DEAL_COST_1_BILLION/19_REPOSITORY_AUDIT_2026-10-08.md:1–8` and `03_VIDEOS/VIDEO_003_UMG_DISTROKID_AI_COPYRIGHT_LAWSUIT/19_REPOSITORY_AUDIT_2026-10-08.md:1–11` explicitly report stage-aware audit FAIL, open HIGH/BLOCKER issues and unresolved templates. They correctly avoid turning publication into retrospective certification. This report does not assert that every historical open issue remains an actual defect in the published media: final evidence must first be mapped to it.

004 STATE itself contains older“0 generated jobs/0 generation spend” and“quote next” text above the execution addendum. Append-only handoffs accumulate contradictory operational instructions even when an addendum is accurate.

## Voice generation: costs and avoidable retries
|Episode|Recorded production cost|Correction/retry|Total or current boundary|
|---|---:|---|---|
|001|43.80 credits for 4 jobs|One separately approved 0.60 credit patch|44.40 credits; no additional retry recorded|
|002|44.40 credits for 4 jobs|0 retries recorded|44.40 credits|
|003|46.65 credits for 4 jobs|0 retries recorded|46.65 credits|
|004|FreshV11 quoted 39.45 credits,3 jobs submitted once|No retries permitted; sources complete, retrieval failed|Quote/submission evidence, not independently reconciled debit; master pending|

Sources: `03_VIDEOS/VIDEO_001_THE_EBAY_HARASSMENT_SCANDAL_THAT_COST_56_MILLION/10_AUDIO_MASTER.md:18–63`; `03_VIDEOS/VIDEO_002_ADOBE_FIGMA_FAILED_DEAL_COST_1_BILLION/10_AUDIO_MASTER.md:17–29`; `03_VIDEOS/VIDEO_003_UMG_DISTROKID_AI_COPYRIGHT_LAWSUIT/10_AUDIO_MASTER.md:12–21`; `03_VIDEOS/VIDEO_004_VALVE_STEAM_MASS_ARBITRATION/STATE.md:21–29`.

Known 001–003 narration subtotal =44.40+44.40+46.65=135.45 credits. Do not add 004's quote as a verified invoice. Do not add narration test/preview costs unless their distinct job IDs/debits are available.

004's older 41.10(V08) and 42.00(V09) estimates are superseded, not extra charges. Reusing quotes across script versions would be a control defect. Current V11 input hashes, exact pronunciation-only normalization and Short-safe split are strong preflight practices; preserve them.

## DistroKid image waves: exact arithmetic
The pipeline's final 120/120 PASS is a completion statement. It is NOT a 0% historical reject rate and NOT 120 total paid generations.

|Wave|Jobs|Credits|PASS submissions|REJECT submissions|New final slots covered / issue|
|---|---:|---:|---:|---:|---|
|Initial Test 30|30|15.0|19|11|30 first attempts|
|R5 Test 30|30|15.0|21|9|11 repairs +19 new slots|
|R6 Test 30|30|15.0|26|4|9 repairs +21 new slots|
|R6 remaining 50|50|25.0|44|6|50 new slots|
|R7 reject 10|10|5.0|10|0|10 repairs|
|Total|150|75.0|120|30|120 unique final slots|

Reproduced by parsing four `*GENERATION_LEDGER.csv` files plus `13F_R5_TEST30_VISUAL_QC.csv`:150 job rows,150 unique nonblank job IDs. The R5 QC CSV preserves job IDs and URLs even though no separate R5 generation ledger with that naming convention exists. Costs for R5 are supported by its summary/STATE; they were not invented from an absent cost column.

Calculations:

- Submission reject rate =30/150=20.0%.
- Submission acceptance =120/150=80.0%.
- Final completion =120/120=100%.
- Jobs above one per final slot =150−120=30, or 25.0% more than baseline.
- Actual recorded 75.0 credits versus 60.0 one-pass budget =15.0 credits over baseline,25.0%.
- Credits per accepted final slot =75/120=0.625, versus 0.5 nominal per job.
- Technical generation failures were 0 in these summaries. Visual rejection is different from failed delivery.
- “0 retries” in a wave means no automatic repeat within that execution. It does not erase separately approved regeneration waves.

Evidence: `03_VIDEOS/VIDEO_003_UMG_DISTROKID_AI_COPYRIGHT_LAWSUIT/STATE.md:190–203,250–262,294–315,323–377`; `13F_R5_TEST30_VISUAL_QC_SUMMARY.md:6–38`; `13I_R6_TEST30_VISUAL_QC_SUMMARY.md:6–50`; `13K_R6_REMAINING50_VISUAL_QC_SUMMARY.md:6–49`; `13M_R7_REJECT10_VISUAL_QC_SUMMARY.md:6–36`.

The R6 summary calls 110/120 a “first-pass final-frame completion rate.” That is cumulative accepted slots AFTER earlier repairs, not the first-attempt acceptance denominator. Rephrase in future reporting as “slots currently completed 110/120.” True initial attempts: initial 30+R5 new 19+R6 new 21+remaining 50=120; first-attempt rejects 11+5+0+6=22, so first-attempt acceptance 98/120=81.7%, as reconstructed from the wave compositions. The R5 QC CSV splits its 19 new slots into 14 PASS and 5 REJECT; its 11 repair slots split into 7 PASS and 4 REJECT. R6 reports all 21 newly sampled frames PASS. These cohort facts, rather than mixed-wave 70% versus 86.7%, support an observed improvement for the sampled fresh slots.

The apparent R5→R6 pass-rate improvement is not a randomized prompt test: samples differ and mix difficult retries with fresh slots. No causal model-accuracy claim is warranted.

## Repeated visual failures and preflight limits
R5 hard preflight recorded 101/101 PASS before real output. Its next 30 job test still rejected 9/30. R6 preflight recorded 80/80 PASS; later difficult mechanism scenes still failed. Prompt/source review is necessary but not empirical output validation.

Recurring DistroKid defects:

- generated notice/status/body text or identifier fragments;
- pseudo-UI instead of authentic evidence;
- mechanism labels not grounded in attached source;
- logo-board/evidence-pile regression;
- scale or conflict that fails to read at a glance.

Evidence: `13E_R5_HARD_PREFLIGHT_SUMMARY.md:3–20`; `03_VIDEOS/VIDEO_003_UMG_DISTROKID_AI_COPYRIGHT_LAWSUIT/13F_R5_TEST30_VISUAL_QC_SUMMARY.md:23–28`; `03_VIDEOS/VIDEO_003_UMG_DISTROKID_AI_COPYRIGHT_LAWSUIT/13I_R6_TEST30_VISUAL_QC_SUMMARY.md:28–41`; `03_VIDEOS/VIDEO_003_UMG_DISTROKID_AI_COPYRIGHT_LAWSUIT/13K_R6_REMAINING50_VISUAL_QC_SUMMARY.md:24–32`. These are precision/provenance failures, not merely aesthetic differences.

Recommend routing exact legal copy, account identifiers, contract clauses and diagrams to authentic crops or deterministic editor typography. Use generated imagery for clearly illustrative objects/environment where it adds meaning. This is a proposed future routing refinement; it does not authorize changing the existing unified visual lock or regenerating approved frames. Obtain a scoped owner decision before altering a locked production method.

## Adobe: persistent source failures create additional spend
- Salvage audit recovered 15 usable frames for 110 slots; olderR2 batch 0/14 PASS andR3 batch 0/10 PASS. It explicitly says some earlier transient generations were not preserved as binaries. The complete historic spend cannot be reconstructed from final assets alone.
- Forty slots survived only as 960×540 previews. Owner-approved replacement cost 20.0 credits;33 passed,7 rejected. R15 cost 3.5 credits,5 passed,2 rejected; R16 cost 1.0 credit closed the remaining two with deterministic word repairs. R14–R16 total 24.5 credits. This is recoverability/resolution rework, not proof all 24.5 credits would have been avoidable.
- R17 used 7 more jobs/3.5 credits to repair garbled source text; exact short-quote renders replaced long small-type source dumps.
- R11's 16 repair attempts left 5 subtitle-safe composition rejects; R12's 5 attempts left 1. Repeatedly generating document layout near a strict caption boundary is expensive compared with a deterministic layout check.
- An assembly was invalidated for a thumbnail/no-upscale black-canvas inset bug, despite frame-export counts. A count/dimension check alone cannot verify the visible image fills the canvas.

Evidence: `03_VIDEOS/VIDEO_002_ADOBE_FIGMA_FAILED_DEAL_COST_1_BILLION/13_R9_EXISTING_GENERATION_SALVAGE_AUDIT.md:6–31`; `13_R14_PREVIEW40_QC.md:4–31`; `13_R15_RETRY_QC.md:3–14`; `STATE.md:236–254`; `13_R17_TEXT_REPAIR_RESULT.md:3–14`; `13_R11_RETRY_QC.md:7–26`; `13_R12_RETRY_QC.md:6–18`; `manifest.yaml:59–66`.

Do not sum every summary's “spend” blindly: QC notes may restate prior spend or report 0 new spend. Deduplicate by provider job ID, with approved amount, actual debit when known and accepted asset hash. Full Adobe/eBay visual budget and all thumbnail experiments remain NOT RECONCILED in this audit.

## Artifact control: counts from current asset manifests
Reproduced using Import-Csv, all rows in each ASSET_MANIFEST; blank means empty/whitespace, PASS uses case-insensitive status substring.

|Episode|Manifest rows|Blank storage_uri|PASS rows with blank URI|Blank sha 256|
|---|---:|---:|---:|---:|
|001|115|0|0|115|
|002|111|36|36|111|
|003|120|0|0|120|
|004|0|0|0|0|

Evidence: corresponding `ASSET_MANIFEST.csv` at baseline. Counts are table-integrity findings, not proof assets are physically missing. Hashes/paths sometimes exist in other final export/QC manifests; reconciliation can repair the control plane without new production. Some rows represent final-frame/editor assets with different storage conventions.

DistroKid rows still say“generation not yet authorized” in rights/usage notes despitePASS_LOCKEDand resultURLs (`ASSET_MANIFEST.csv:2–4`). Rights assessment, generation authorization and final usability should not share stale boilerplate.

Policy intentionally keeps heavy media outside Git (`00_CORE/STORAGE_POLICY.md:3–18`). Missing anMP4 fromGit is therefore not itself a failure. The failure is an asset with no tested durable route, no checksum and no authoritative mapping to the approved master. Provider URLs and expiring Actions artifacts should have a durable download backup; expiration does not require regeneration if a verified original is retained.

Adobe's upload QC documents a 2,530,613,593 byte 1080 pmaster, full decodePASS andSHA256 ac 1 e 3 c…c 754; it ALSO says Stage 16 rights audit/Stage 18 documents were templates. That is genuine technical evidence plus explicit release-document limitation, not a complete releasePASS. Source: `03_VIDEOS/VIDEO_002_ADOBE_FIGMA_FAILED_DEAL_COST_1_BILLION/18_PUBLISHING/VIDEO_002_UPLOAD_MASTER_QC.md:3–22`.

## Creative QC and costly labor rework
Valve scripts moved through owner-rejected versions and a newly independent review foundV08=75.8 FAIL despite historical acceptance. V09=82.2 did not meet the later owner 90 minimum; V10=86.8 HOLD; V11=90.4 textPASS. Scores are editorial, not retention measurements.

The good practice is exact reviewed artifact hashes and preserving historical acceptance as history. The defect to prevent is quoting an older high score for a changed artifact or creating downstream payloads before current review is stable. Existing correction protocol already addresses this; enforce rather than invent another redundant layer. Evidence: `03_VIDEOS/VIDEO_004_VALVE_STEAM_MASS_ARBITRATION/06_V11_OWNER90_REVIEW.md:3–21,39–72`; `VERSION_LOG.md:15–20`; `00_CORE/QUALITY_GATES.md:57–59`.

eBay's SFX proofs passed loudness/encode checks but owner still could not hear them as intended. Final direction was Harrison only, previousSFXretired, and no unnecessary rerender was needed. Technical LUFS does not certify in-context audibility or taste. Evidence: `03_VIDEOS/VIDEO_001_THE_EBAY_HARASSMENT_SCANDAL_THAT_COST_56_MILLION/STATE.md:495–552`. Do not reinstate music/SFX based on generic documentary advice.

## Explicit improved gates — proposal only
Existing pipeline provides most controls. Make current evidence unambiguous:

|Gate|Required proof before next step|Prevents|
|---|---|---|
|RESEARCH|Primary chronology, money/status ledger, opposing positions, freshness date, rights path|Expensive story built on unsourced hook|
|SCRIPT|Exact canonical text and contiguousShorts; claim refs; one clear audience promise|Rewriting paid narration downstream|
|RETENTION REVIEW|Independent review of CURRENTtext/hash; hook/promise/legal hard gates; owner-specific threshold|Oldscore approving a new version|
|LEGAL REVIEW|Precision after any narrative rewrite, unresolvedHIGH/BLOCKERclosed, current-status boundary|“Dramatic” rewriting overstating allegations|
|VOICE LOCK|Exact normalized text hashes, model/voice/settings, safe splits, fresh quote|Wrong draft/voice/price|
|OWNER SPEND|Explicit provider/model/job count/cost authorization tied to exact payload|Speculative batch or auto-retry|
|VISUAL PREFLIGHT|Source-native crop/rights/readability, approved layout, deterministic text strategy, capped representative test if authorized|Hundreds of unvalidated prompts|
|ASSET QC|Downloaded original bytes, dimensions/format/decode, hash, provenance and independent visualPASS; separate first attempts/retries|ProviderCOMPLETEDorpreview mistaken forusable asset|
|EDIT QC|Approved source mapping, sampled and full-film inspection, audible QA, no-caption/caption policy correct, measuredShortsduration|Black inset bug or unreadable evidence surviving export|
|PACKAGING|Title/thumbnail/opening alignment, accurate legal force, mobile view, owner acceptance|Unapproved attractive-but-misleading cover|
|RELEASE|Current legal refresh, masterhash+decode+auditory/visualreview, durable retrieval, exact metadata/settings/timezone/related links|Wrongmasteroruncertifiedpublication|
|POST PUBLISH|Studio confirmation and 24/48/72 h/7 d exports; snapshot experiment state|Chat claim replacing actual analytics|

Every gate records artifact hash/version, reviewer, timestamp, verdict, remaining limitations and next authorized action. “PASSwithreleaseHOLD” must not feed a releasePASS. Fail-safe resumption reads existing job IDs before permitting any new job.

## Economics and feasible cadence
Observed 001–003 TTS44.40–46.65 credits/episode; DistroKid visual 75 credits/120 finalframes. These are historical task records, not current provider quotes. An illustrative episode retaining that scale would use about 119.4–121.65 credits for narration+images before thumbnail work, retries outside the example, storage, rendering and labor. This is a scenario, not a channel-wide unit-cost estimate; lengths/models/visualcount differ.

|Cadence alternative|Planning labor at 30–50 hours/episode|Illustrative narration+image credits/week at~120/episode|Learning/quality implication|
|---|---:|---:|---|
|One every 2 days (~3.5/week)|105–175 hours/week|~420|Only plausible with multiple measured parallel roles; current unfinished 004 and unqualified 005 do not establish this capacity|
|Two/week|60–100 hours/week|~240|Possible with a working team/buffer; leaves limited room for deep source work and independent packaging|
|One premium/week|30–50 hours/week|~120|Most feasible initial recovery test while logging actual labor/rework and preserving review|

Labor ranges are assumptions for planning, not reconstructed hours; Waymo can exceed them. The existing tiny audience provides too little exposure to turn more uploads into clean experiments automatically.

Recommend a 14-day operational trial of one long/week, conditional on release gates, with two-packaging-review opportunities before each release and a buffer of one VERIFIEDfinished episode before increasing cadence. This is a proposed schedule; it does not cancel a promised release, alter dates or authorize production. Track planned versusactual hours per stage, first-attempt asset acceptance, regeneration credits, retrieval failures, reopened gates and days blocked. Move to 2/week only if two consecutive releases meet gates, workload is sustainable and the buffer survives; faster cadence requires measured staffing, not an algorithm claim.

## Prioritized corrective backlog
|Priority|Verified defect/action|Expected benefit|Effort estimate|Acceptance|
|---|---|---|---|---|
|P0|004 job/state reconciliation before any resume|Prevents duplicate 39.45 credit submission risk|30–60 min bookkeeping after live verification|Manifest/STATE/index refer to same 3 IDs/current stage; retrievalfailure never becomesnewgeneration|
|P0|002/003 release evidence reconciliation|Reliable production/publication truth|2–5 hours each, excluding missing substantivechecks|Current master and actualchecks mapped; unknowns remain unknown; no blanketPASS|
|P1|Durable originals/checksums and canonical assetregistry|Reduces preview recovery/regeneration|2–4 hours for inventory; transfers vary|Every activefinalasset resolves, hashesmatch, originalresolutiondistinguished|
|P1|Route exact text/strict layout to deterministic handling, if approved|Targets repeated generatedtext/caption failures|1–2 hours routing review before new visuals|No synthetic evidence text; locked accepted assets unchanged|
|P1|Separate creative/perceptual from technicalPASS|Less whole-film rerender/rework|One short current version review per major change|Reviewer hears/sees real export, not only metrics|
|P2|Job-level consolidated cost ledger and stage-time logging|Makes sustainable cadence measurable|1–2 hours setup proposal|No duplicateIDs, quotes distinct fromdebits, final slot/attempt/statusseparate|

Estimates exclude any new paid generation and do not constitute approval. This audit identifies controls and proposals; it does not execute the maintenance backlog.







## Lead synthesis: staged capacity decision
Recommendation confidence: MEDIUM for production risk control, LOW for any growth effect. Phase 1 is the first 14 days after the owner adopts the proposal: at most one premium long per week, only through complete release gates, retaining the approved 004 then 005 topic order. This audit does not move any already approved publication date. Phase 2 permits a trial of two longs per week only after two consecutive fully passing releases, auditable labor/credit records, and one verified finished episode in reserve. Every-two-day production is not validated by the present evidence. Failure to meet a hard release gate prevents claiming readiness; it does not authorize automatic calendar changes.

## New local evidence: Valve WAV exists despite stale repository state
A later independent filesystem check found `C:/YOUTUBE/Youtube 3/Video 4/VIDEO004_HARRISON_V11_MASTER.wav`, 232,704,102 bytes. Read-only RIFF/WAVE header parsing found WAVE_EXTENSIBLE tag 65534, two channels, 48,000 Hz, 24 bits/sample, 288,000 bytes/second and 232,704,000 data bytes: header-derived duration 808.000 seconds (13:28). SHA-256: `8c11be2619a6a84b7e1a6cbe0cb8c708d72dff556d1d737dd46f596ea21f65d7`.

This establishes that a local audio master candidate exists; the earlier repository addendum saying download/master pending is stale relative to the filesystem. It does not bind this WAV to the three approved provider source jobs, prove a complete faithful assembly, establish a full decode, or certify auditory quality. Provenance, input-to-output fidelity, source-part mapping and listening remain NOT VERIFIED. Resume verification of this existing file before considering any regeneration. Do not state that no master exists, and do not call this file release-approved merely because its name says MASTER.
