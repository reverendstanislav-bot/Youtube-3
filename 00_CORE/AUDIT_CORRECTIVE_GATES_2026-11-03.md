# Audit corrective gates — 2026-11-03 (proposal)
Scope: WHAT IT COST / Youtube-3. Existing AGENTS.md, spend lock, task-scope lock, legal standards, and episode stage gates take precedence. This document NEVER authorizes new production, publishing, paid jobs, or reopening locked episodes.

## 0. Truth at session start
- Fetch current origin/main HEAD and read AGENTS.md, 00_FOUNDATION, relevant 00_CORE / 01_CHANNEL policies, VIDEO_INDEX.csv, episode manifest.yaml + STATE.md. Record read SHA/ref/time in the work report.
- Memory is a navigation hint, not a source of repository state. Never assert a file, commit, remote sync, CI run or artifact exists without a verified path and ref.
- Compare manifest, STATE and VIDEO_INDEX; if they disagree: HOLD, record drift, do not advance.
- No fabricated tool actions, links, metrics, sources, transcripts, video inspections or claim that a check ran.

## 1. Deliverable / evidence status vocabulary
Use exactly:
- PLANNED — no source/asset exists.
- DISCOVERED — identified candidate, not independently inspected.
- INSPECTED — original or reliable preview actually opened; record URL/path and method.
- FACT_CHECKED — material claims tied to primary sources and appropriately qualified.
- RIGHTS_OK — item-level permission/terms confirmed for intended use.
- PACKAGED — manifest and required files exist; not proof they work.
- VERIFIED — file(s) actually inspected/probed, SHA256 recorded where practical, links checked, ledger completed.
- PASS — all mandatory stage-specific gates green, reviewer/proof linked.
- HOLD — unknown or missing required verification; never imply GO.
- REJECT — fails scope/accuracy/rights/quality.
For Git separately: LOCAL, COMMITTED, PUSHED, REMOTE_HEAD_VERIFIED, CI_VERIFIED. Do not equate any two statuses.
A structural validator PASS does not imply visual/legal/editorial PASS.

## 2. Blockers / review decisions
Every decision MUST cite artifact path + revision, source URLs or evidence IDs, what was actually checked, remaining HOLDs, and one precise next action. When inaccessible write NOT VERIFIED (tool error/reason). Never substitute "0 competitors" or "0 defects" for "not observed".
Owner approval is required before paid generations, stage advances, publishing, and changing locked assets.

## 3. Script gate
Before Stage 07 lock review:
- First 60 seconds: clear specific conflict, stakes, new fact/reversal; no repeated premise.
- First 5 minutes: beat-by-beat escalation, each segment adds a new fact, mechanism or consequence.
- Causal question → partial answer → new question; factual/legal caution at the right moment.
- Mark duplicate information by act/time and resolve; compress unproductive ending.
- Exactly 4 contiguous cut-ready Shorts of <=35 seconds for WIC unless a newer explicit owner lock changes this requirement.
- Russian preview before Harrison voice when required; no TTS on unapproved script.
Produce a pass/hold checklist with precise time/text evidence; do not state a numerical retention score as measured analytics.

## 4. Visual coverage / source reality
Map *each narration beat* to asset ID, source or original generation prompt, media type, intended shot duration, editorial purpose, rights/provenance, editorial status and source-to-timeline mapping.
- Footage/photo: subject-specific, native horizontal 16:9 where required; rights reviewed item by item; no generic filler or side-blurred vertical conversions.
- Real documents: authenticate source and preserve real pixels; distinguish cited originals from recreations.
- Graphics: each must explain one specific factual mechanism; cite underlying data; no repetitive slide/card replacements.
- Generated stills: one separate 16:9 image per asset, approved revision/reference and precise brief, subtitle-safe zone, PASS/HOLD/REJECT. Never represent generated scenes/documents as archive.
- Count usable, physically verified bytes/assets separately from planned positions; inspect actual folders/crops/stills and rejects. No fixed stock/gen ratio or arbitrary frame count in place of coverage.
- Image editing must actually preserve the approved parent; record edit relationship and compare output. New generation is not an edit.
- Video generation remains prohibited. Paid still generation requires explicit specific owner spend approval.

## 5. Thumbnails & metadata
For each long video provide 3 genuinely distinct creative hypotheses (not font/background swaps), each in a separate image: recognizable subject, single concrete conflict, one clear click motive and accurate documentary aesthetic. Compare visual read at small size and source/claim accuracy. Owner selection and actual YouTube experiments are different statuses.
No fake legal imagery, invented numbers or unsupported accusation. EN publication copy + RU translation when requested; preserve per-channel metadata rules.

## 6. Codex handoff
READY_FOR_CODEX only if manifest and exact input URLs/paths exist and verify, rights/provenance known, asset IDs and scene/time mappings complete, checksums for actual bytes available, missing files enumerated, outputs and acceptance tests defined. Codex may verify downloads/assemble; must return BLOCKED for 404, mismatched bytes, missing rights, missing source, unsupported environment. Never ask Codex to improvise sources or report a nonexistent run.
Use a machine-readable blockers report; completed work and unperformed verification must be explicitly separated.

## 7. Post-task mandatory report
1. HEAD/ref actually read;
2. files actually changed with paths;
3. executed checks and results;
4. artifact links/commits/PR; 
5. blockers (even if zero verified);
6. stage status with explanation;
7. next step, not automatically executed.
If time or access prevents completion, report partial completion — never fabricate PASS.

## 8. Governance
This addendum is an enforceable review checklist once merged; it does NOT retroactively change any episode's PASS. Historical artifacts require separate item-level audit. Human review is required for evidence and artistic decisions; automated tests alone cannot establish them.
