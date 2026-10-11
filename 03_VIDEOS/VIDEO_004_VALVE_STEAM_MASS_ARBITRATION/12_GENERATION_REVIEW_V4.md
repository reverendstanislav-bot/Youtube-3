# V4 — independent count, coverage, director and legal plan review

2026-10-11. Scope: the selected long-form image plan only. No generated pixels, full audio audition, edit, vertical delivery or release approval.

Maker: root. Independent critics: `review_correction` (source/legal/count) and `v08_precision` (director/retention/coverage). Both read the canonical V11 and cue grid; neither edited files or submitted jobs.

Reviewed final plan SHA256 (UTF8/LF normalized): `99a7138f0a2e4a3e1249425dfbf6f276645110c6237f2318bd33fd4b5e2fba7a`.

## Final verdicts received

- `review_correction`: PASS_PLAN_COUNT_AND_LEGAL. Separate Node reconciliation and Python validator confirmed60 used/unique images,124 cues/125 segments,84 placements/24 reuses,20700frames, no gaps/overlaps/source-claim mismatches. Visible request-only status, support condition, preliminary/as-applied qualifiers and dated public-mirror limitation retained. Requested human-summary synchronization applied:84/24,83/9.735 and corrected SH02/SH04 source-asset sequence.
- `v08_precision`: PASS_PLAN_COUNT_AND_DIRECTOR_LOGIC. No remaining blocking coverage issue or justified arbitrary requirement for more than60 images. Early Four, AAA-refusal, closure-answer and count reveals corrected. GF006 callback avoids a proposed20.6s continuous hold. Four selected Shorts retain compatible contiguous narrative coverage, not verified vertical pixel delivery.

## Accepted repairs

| Issue | Final correction |
|---|---|
| GF035 could imply an order existed | Visible text now says VALVE REQUESTED A STOP ORDER |
| GF025 forum too broad | Visible unresolved-support condition added |
| GF058/GF059 could imply live official status | Visible PUBLIC MIRROR SNAPSHOT THROUGH SEPTEMBER28,2026 |
| GF047 denial shown during pre-answer SC099 | SC099 holds GF046; denial first appears at SC100 |
| Four revealed before spoken answer | GF019 carries SC035–36; GF017 starts SC037 and holds through SC038 |
| AAA refusal shown during request | GF005 carries request; GF031 first appears SC070 and holds its narrow qualification |
| No-automatic-closure answer shown before question | GF006 carries SC048–49; GF024 starts SC050 |
| 4,991 shown during initial997 cue | GF013 carries SC020; GF012 begins SC021 |
| Proposed repair created20.6s still hold | GF023 endsSC047; GF006 returnsSC048–49 instead |

Lead synthesis: all60 slots remain used for a concrete reason; no extra slots were added solely to meet a guessed count.59 narrative images +1 endscreen, not175 compulsory generations.84 image placements include24 identical-image returns. Count is exact for this version, not an objectively unique minimum or promised paid-attempt count.

SC106 split at frame16911/676.44s lies between provisional ASR `year.` end676.16 and `The` start676.86. It remains an unauditioned visual boundary, not an audio cut or final word-sync lock.

## Gates explicitly still open

- Actual generation lettering and mobile readability, particularly GF001/GF012/GF038/GF058/GF059. Qualifiers must not become micro-footers.
- Normal-speed pacing of first60s and long coherent holds GF03417s/GF04216.88s/GF01616.68s/GF00615.56s. Maximum hold is not by itself a PASS or FAIL.
- Full808s auditory review, seams and four Short cut edges; final Stage11 lock.
- Vertical layouts/CTA, thumbnails, actual YouTube endscreen geometry, edit and release.
- Official Stage16 legal/source freshness; current appeal absence claim is snapshot-bounded.
- Model choice, exact spend quote and explicit authorization before any paid job.

No billable submissions or accepted generated-asset claims. Historical rejected Fusion canary remains rejected; review approves this new plan only.

## Local verification before GitHub upload

- `python .../12_VALIDATE_GENERATION_PLAN_V4.py`: PASS; final60/84/24 counts and normalized input hashes match all derived files.
- Python compile of the episode validator: PASS.
- `python tools/audit_video.py 03_VIDEOS/VIDEO_004_VALVE_STEAM_MASS_ARBITRATION`: PASS,1package,0warnings.
- `git diff --check`: PASS.
- Global `validate_repo.py`: FAIL on existing tracked `06_ANALYTICS` directory, not allowed by current global validator.
- Global `audit_video.py --all`: FAIL,50 existing findings confined to Video2/3 (open release QA, template tokens and status vocabulary). Neither those episodes nor the global contract were changed in this task. This is not a repository-wide green CI claim.

Upload scope is this episode's V4 plan and its handoff/QA records only, based directly on remote main `d111652ebe80af4aa00ca24843ce9d78809c021c`. Unpushed broader reconciliation and rejected canary-correction commits are deliberately excluded. Publication evidence is the remote Git commit, not this local checklist.
