# Video Package Schema

Each video package is a self-contained production record.

## Control files
- STATE.md
- manifest.yaml
- VERSION_LOG.md
- QA_LEDGER.csv
- ASSET_MANIFEST.csv
- QC_CHECKLIST.md

## Evidence controls
- SOURCE_INDEX.csv
- CLAIMS_LEDGER.csv
- CASE_EVENT_LEDGER.csv
- FACT_CHECK.md

## Canonical stage artifacts
00 topic qualification
01 evidence research + competitor research
02 case/story map + timeline
03 script v1
04 fact/legal review
05 script v2
06 performance review
07 final script lock
08 voice script
09 voice review/lock
10 audio master
11 transcript + visual timeline
12 visual source/generation plan
13 visual asset QC
14 graphics/documents/music/SFX
15 assembly/edit
16 final fact/legal refresh + rights/provenance audit
17 title/thumbnail packaging
18 upload/prepublication package
19 post-publish analytics

## Canonical narration
After Stage 07, `07_SCRIPT_FINAL.md` is the only canonical narration text. Later delivery markup must not change factual meaning.

## Completion
A video cannot become RELEASE_READY until Stage 16 fact/legal refresh and Stage 18 prepublication QC pass.
