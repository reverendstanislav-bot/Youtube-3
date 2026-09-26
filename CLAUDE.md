# WHAT IT COST — Claude Code operating rules

Faceless US business/legal documentary channel. Claude (main session) is the **dispatcher**: reads `status.yaml`, runs the right agent, stops at every owner gate. Talk to the owner in **Russian**; all channel content (research, script, prompts, packaging) is in **English**.

## Where things live
| Path | What |
|---|---|
| `channel/` | channel rules: `brand.md`, `storytelling.md`, `legal.md`, `voice.md`, `visual_style.md` |
| `.claude/agents/` | one file per agent |
| `topics/backlog.csv` | topic backlog (scout) |
| `videos/<id>-<slug>/` | text files of one video; `status.yaml` is the only status |
| `videos/_template/` | copied by `python tools/yt.py new` |
| `tools/yt.py` | state keeper, media librarian, render QC, credit tracker |
| `weftcut/` | brand motifs for WeftCut (captions with red active word, headline, money, lower third, card, quote, labels) — see `weftcut/README.md` |
| `C:/Users/KK/Documents/WhatItCost_media/<id>-<slug>/` | all media (never in git) |

**Legacy — do not modify:** `00_FOUNDATION/`, `00_CORE/`, `01_CHANNEL/`, `02_PIPELINE/`, `03_VIDEOS/`, `04_SHARED/`, `AGENTS.md`, old `tools/*.py` (only exception: new top-level dirs are whitelisted in `validate_repo.py` so legacy CI passes), `.github/workflows/video001_*`. VIDEO_001 and VIDEO_002 live there and stay untouched. New work starts at VIDEO_003 in `videos/`.

## Pipeline
| # | Phase | Agents | Ends with owner gate |
|---|---|---|---|
| 1 | Qualification | `yt.py court` → researcher 1a (source path) → `yt.py fetch-sources` + `yt.py yt-search` → scout B (competitors) → researcher 1b (reads docs, scores) → packaging 1 (concepts) | **G1** GO + pick title/thumbnail concept |
| 2 | Research | researcher Mode 2 (deep story research) → `yt.py fetch-sources` + `texts` + `pages` → critic Mode R (research review) → researcher Mode 2b (fill gaps) → critic Mode R again (max 2 rounds; stop early on READY; WEAK TOPIC → tell owner) | — (report only) |
| 3 | Script | writer → critic Mode S + hook-doctor + defamation-risk → writer (≤3 rounds) → writer voice script | **G2** script + Shorts lock |
| 4 | Voice | Higgsfield TTS (spend gate) → WeftCut `transcribe_clip` → `yt.py words` → `yt.py audio-metrics` → audio-qc | **G3** spend approval before TTS |
| 5 | Visual | visual-director (beats), prompt-engineer (image prompts) → owner generates → visual-director QC → prompt-engineer (video prompts) → owner generates → `yt.py frames` → QC → `yt.py hash-beats`; document-designer → `yt.py doc-shots` | **G4** images, **G5** videos |
| 6 | Edit | Claude assembles in WeftCut (brand motifs) → `yt.py frames` → retention-editor → fixes → `yt.py render-qc` → Shorts 9:16 | **G6** rough cut, **G7** Shorts |
| 7 | Release | final-check, packaging (titles, desc, chapters, Shorts, release plan); Claude builds thumbnail | **G8** pick title + thumbnail |
| 8 | Publish | owner uploads | — |

Run independent agents in parallel (e.g. critic + hook-doctor + defamation-risk).

## Agents — token discipline
- Models: **opus** researcher, writer, critic · **sonnet** scout, hook-doctor, defamation-risk, visual-director, prompt-engineer, retention-editor, final-check, packaging · **haiku** audio-qc, document-designer.
- No agent has Bash. Everything mechanical (downloads, hashing, measuring, frames, rendering) is a `yt.py` command the dispatcher runs — 0 tokens.
- Each agent has `maxTurns` and a PreToolUse lock (`tools/agent_guard.py`) that blocks writes outside its own files.
- Give every agent a short prompt: video id, mode, and the exact files/beats it should handle. Nothing else.

## HARD rules
1. **Scope.** Do only what the owner asked this turn. At a gate: stop, report what was done, name the next step, wait. "Continue"/"do stage N" authorizes only that stage.
2. **Spend.** Any paid generation (Higgsfield TTS, images, video) needs explicit owner approval *before* submission: provider/model, job count, estimated credits. Log it with `yt.py credit`. One approval = those jobs only.
3. **Evidence.** Never state an allegation/complaint/charge/claim as fact. Script wording must match `claims.csv` status. See `channel/legal.md`.
4. **No music, no SFX.** Narration only.
5. **One truth.** Status lives only in `status.yaml`. One current version per file — history is git. Never create `_v2`, `_final`, `_R3` files.
6. **Media outside git.** Files go under `media_root`; git stores path + sha256 (`yt.py hash`).
7. **Legacy untouched** (see above).
8. Verify before claiming done. Report failures plainly.

## Commands
```
python tools/yt.py new <id> <slug> "<working title>"   # create videos/<id>-<slug>/ + media folder
python tools/yt.py status <id>                          # show stage, gates, next action
python tools/yt.py check <id>                           # validate files/tables for current stage
python tools/yt.py gate <id> <gate> <APPROVED|REJECTED|WAITING_OWNER> "<note>"
python tools/yt.py stage <id> <stage> "<next action>"
python tools/yt.py hash <id> <relative media path>      # print sha256 + size
python tools/yt.py credit <id> <provider> <jobs> <credits> "<note>"
python tools/yt.py render-qc <id> <relative media path> # ffprobe + loudness + black frames → 5_edit/render_qc.md
python tools/yt.py yt-search <id> "query" ["query2"] [-n 10]  # real YouTube titles/views/dates → 1_research/yt_search.md
python tools/yt.py court <id> "<query>"                # CourtListener dockets + direct PDF links → 1_research/court_search.md
python tools/yt.py fetch-sources <id>                   # download tier-1/2 sources → media/sources, hash into sources.csv (+ .txt for HTML)
python tools/yt.py texts <id>                           # re-extract .txt from archived HTML sources
python tools/yt.py words <id> <envelope.json>           # WeftCut transcript → 3_voice/words.json + captions.srt
python tools/yt.py audio-metrics <id> [path]            # loudness, silences, transcript-vs-script diff → 3_voice/audio_metrics.txt
python tools/yt.py frames <id> <render path>            # frames + contact sheets + freeze/black report → 5_edit/frames_report.txt
python tools/yt.py pages <id> [--sources S004] [--pages 1,3]  # PDF pages → media/sources/pages/*.png (PyMuPDF)
python tools/yt.py doc-shots <id> [--only B010,B011]    # render document shots from 4_visual/doc_shots.csv
python tools/yt.py hash-beats <id>                      # sha256 for every asset_file in beats.csv
```

## Git
Commit after each completed phase with a clear message. Push only with owner approval.
