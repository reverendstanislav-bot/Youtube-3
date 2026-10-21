# VIDEO007 — Stage09 Harrison generation plan ready — 2026-10-21

**Stage07 Script Lock PASS. Stage08 Voice Script PASS. Stage09 preparation PASS; audio QA/Voice Lock has not run.** GitHub remains the source of truth.

## Verified input

- `07_SCRIPT_FINAL.md`: 60 locked spoken paragraphs.
- `08_VOICE_SCRIPT_MASTER.txt`: 2,517 lexical words; byte-identical to `07_SCRIPT_FINAL_NARRATION_ONLY.txt`.
- Five Stage08 segments reconstruct the master exactly: 60/60, zero omissions, duplicates, reorders or wording changes.
- Exactly four native Shorts: SH01/A00-P01, SH02/A05-P03, SH03/A07-P03, SH04/A09-P03. Their finished `<=35.0s` duration remains unmeasured.

## Selected plan

- Local Voicebox 0.5.0, CUDA, Qwen3-TTS 1.7B Base.
- Candidate Harrison clone profile: `228d3d8a-096f-461b-bf11-4f9415e2dafc`; one 28.4-second reference sample derived from the clean VIDEO004 Harrison workflow.
- Five sequential jobs, fixed seed `20261021`, one existing segment per job.
- Estimated provider cost: **$0 / 0 credits**. No model download needed.
- Qwen3-TTS 0.6B is downloaded but only a manual fallback; no automatic switching or retry.

The channel identity remains canonical Higgsfield Harrison preset `573e5163-59b3-4926-aab1-951ef2985f81`. The local clone must pass generated-audio A/B listening. Submit Job01 first and stop if identity or pronunciation fails.

## New Stage09 artifacts

- `09_VOICE_QA_LOCK.md`
- `09_TEXT_INTEGRITY_QC.md`
- `09_HARRISON_GENERATION_PLAN.csv`
- `09_VOICE_QC_PLAN.md`
- `09_SHORTS_AUDIO_EXTRACTION_PLAN.csv`

## Boundary

No VIDEO007 TTS request, retry, paid credit, audio, image, video or Stage10 work was created. A read-only Voicebox history check found 0 exact matches to the five VIDEO007 inputs; unrelated older history records were left untouched. Next action requires explicit owner authorization for the five listed local Voicebox jobs. Stage16 docket freshness and later packaging title review remain separate.
