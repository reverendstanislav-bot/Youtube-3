# RUNBOOK — exact dispatch steps per phase

Dispatcher = main Claude session. Read only the section of the phase you are running.
Conventions:
- `<id>` = 3-digit video id, `V` = `videos/<id>-<slug>`, `M` = media root from `status.yaml`.
- Agent prompts are short and literal. Copy the template, fill the brackets, add nothing else.
- Agents that are independent run **in parallel** (one message, several Agent calls).
- After every agent: `python tools/yt.py check <id>`; fix mechanical problems yourself, send content problems back to the same agent once.
- Agents never see each other's replies — everything passes through files.
- Several videos in flight: `python tools/yt.py board` shows every video's stage and what waits for the owner.
- At the end of each phase: update `status.yaml` (`yt.py stage`, `yt.py gate`), commit to branch `claude-code-setup`, push, report to the owner in Russian (≤12 lines: what was done, key numbers, what needs the owner), and STOP.

---

## Phase 1 — Qualification → gate G1

1. New topic: `python tools/yt.py new <id> <slug> "<working title>" --topic T###`. Re-run: reset `1_research/qualification.md` and `competitors.md` from `videos/_template`.
2. Scripts (parallel, 0 tokens):
   - `python tools/yt.py court <id> "<case name or party>"` (one call per case)
   - `python tools/yt.py yt-search <id> "<query 1>" "<query 2>" "<query 3>" -n 10` (case name, company + lawsuit, the angle)
3. **researcher** — `Video <id>. Step 1a. Topic: <one line>. Cases: <names>. Build the primary-source path.`
4. Scripts: `python tools/yt.py fetch-sources <id>` then `python tools/yt.py texts <id>` (PDF/HTML → .txt, scanned pages → PNG).
5. Parallel:
   - **scout** — `Video <id>. Task B. Topic: <one line>.`
   - (wait for scout, then) **researcher** — `Video <id>. Step 1b. Read the .txt of every downloaded primary source before scoring.`
   Order: scout first, then researcher 1b (1b uses competitors.md).
6. **packaging** — `Video <id>. Mode 1.`
7. `yt.py gate <id> g1 WAITING_OWNER`. Report: decision + score, the materialized cost, top 3 story beats, competitors (count, top views), the 2–3 concepts. Ask: GO / HOLD / NO-GO and which concept. On GO: `yt.py gate <id> g1 APPROVED "<concept>"`, `yt.py concept <id> "<title — thumbnail idea>"`, `yt.py stage <id> research "..."`.

## Phase 2 — Deep research (no owner gate; report and stop)

1. **researcher** — `Video <id>. Mode 2. Packaging concept: <from status.yaml>.`
2. Scripts: `fetch-sources`, `texts` (new sources only are fetched).
3. **critic** — `Video <id>. Mode R, round 1.`
4. If verdict GAPS: **researcher** — `Video <id>. Mode 2b, round 1.` → scripts `fetch-sources`, `texts` → **critic** `Mode R, round 2`. Max 2 rounds.
5. READY → `yt.py stage <id> script "..."`, report. WEAK TOPIC → report to the owner with the critic's reason; propose HOLD or a new angle. Do not start the script.

## Phase 3 — Script → gate G2

1. **writer** — `Video <id>. Mode 1.`
2. Parallel: **critic** `Video <id>. Mode S, round N.` · **hook-doctor** `Video <id>.` · **defamation-risk** `Video <id>. Script mode.`
3. **writer** — `Video <id>. Mode 2, round N.`
4. Repeat 2–3 until critic PASS and defamation-risk CLEAR, max 3 rounds.
5. Report: score, runtime, Shorts list, the opening (first 120 words), open risks. `yt.py gate <id> g2 WAITING_OWNER`. Owner locks → `g2 APPROVED`.
6. After lock: **writer** — `Video <id>. Mode 3.` → `yt.py stage <id> voice "..."`.

## Phase 4 — Voice → gate G3 (spend)

1. Count parts in `voice_script.md`; estimate credits (Harrison via Higgsfield: ~11 credits per ~4 min part). Ask the owner: provider, jobs, credits. Wait for approval. `yt.py credit` after each job.
2. Generate each part with the Higgsfield MCP (voice ID in `channel/voice.md`), save to `M/voice/part_NN.mp3`; join with ffmpeg into `M/voice/narration.mp3`; `yt.py hash`, write `voice.file` in `status.yaml`.
3. Transcription in WeftCut (engine: Whisper Base, local). Import the narration, place it on a track, call `transcribe_clip` with `word_timestamps: true`, save the returned envelope to `M/voice/transcript.json` → `python tools/yt.py words <id> <that file>`. If the engine is not active, ask the owner to enable Whisper Base in WeftCut model settings. Whisper Base can mishear names — audio-qc compares against the voice script anyway; names in captions are corrected with `correct_caption_text` or by fixing `words.json`.
4. `python tools/yt.py audio-metrics <id>` → **audio-qc** — `Video <id>.`
5. FIX → regenerate only listed sentences (new spend approval), re-join, repeat 3–4.

## Phase 5 — Visual → gates G4, G5

1. **visual-director** — `Video <id>. Mode 1.`
2. Parallel: **prompt-engineer** — `Video <id>. Image prompts for all image/video_gen beats.` · **document-designer** — `Video <id>. All document beats.` (before it: `python tools/yt.py pages <id> --sources <ids>` for the pages it needs).
3. `python tools/yt.py doc-shots <id>` · `python tools/yt.py handoff <id> --kind img` (several videos at once: `handoff 003,004,005 --kind img` → one folder `WhatItCost_media/_handoff/<batch>/`) → tell the owner the folder path and the count. Wait.
4. Owner drops files (named `<video>_IMG-###.png` etc.) into `return/` → `python tools/yt.py ingest <id>` for each video (crops to 16:9, fills beats, writes rights) → **visual-director** — `Video <id>. Mode 2.`
5. Rejects → **prompt-engineer** `Video <id>. Fixes.` → `handoff --kind img` → owner → back to 4. When all image beats ACCEPTED: `g4 APPROVED` (owner confirms).
6. **prompt-engineer** — `Video <id>. Video prompts.` → `handoff --kind vid` → owner → `ingest` → `python tools/yt.py frames <id> video_gen/<file>` per clip if needed → **visual-director** Mode 2 → `g5`.
7. `python tools/yt.py hash-beats <id>`.

## Phase 6 — Edit in WeftCut → gates G6, G7

1. Check `beats.csv`: every beat ACCEPTED with `asset_file` and/or `motif`. `python tools/yt.py hash-beats <id>`.
2. `python tools/yt.py weftcut-plan <id> --cut N` → `5_edit/weftcut_plan.json` (every WeftCut call with final parameters: tracks, narration, pictures with push-in, brand motifs, captions). Read the WARN lines and fix `beats.csv` first if needed.
3. In WeftCut open a new, empty project for this video (1920×1080, 25 fps) — ask the owner if one must be created in the GUI. Reset `5_edit/weftcut_log.md` from the template.
4. **assembler** — `Video <id>. Steps 1–150.` then `Steps 151–300.` … until the last step (each chunk resumes from the log). Check the log for ERROR lines; fix and re-run only those steps.
5. **Owner exports** the cut from WeftCut to `M/renders/cut_vN.mp4` (there is no export over MCP). Wait for the file.
6. `python tools/yt.py frames <id> renders/cut_vN.mp4` → **retention-editor** — `Video <id>. Cut vN.` → apply fixes in WeftCut directly (small) or in `beats.csv` + new plan (large) → owner re-exports.
7. `python tools/yt.py render-qc <id> renders/cut_vN.mp4`. Report → `g6`.
8. Shorts: in WeftCut, per row of `shorts.csv`, a 1080×1920 composition with the same beats for that range (pictures scaled to cover) and `wic-captions-9-16` (`words_json` of the range, `offset_s` = range start). Owner exports `M/shorts/SHxx.mp4`; `render-qc` each → `g7`.

## Phase 7 — Release → gate G8

1. Parallel: **final-check** — `Video <id>.` · **packaging** — `Video <id>. Mode 2.`
2. **defamation-risk** — `Video <id>. Packaging mode.`
3. Thumbnail: packaging wrote `THM-###` blocks → `python tools/yt.py handoff <id> --kind thm` → owner generates → `ingest` (→ `M/thumbnail/`). In WeftCut, a 1920×1080 frame: base image + `wic-headline` (2–4 words, red keyword) — owner exports a still as `M/thumbnail/thumb_A.png` (+B, C) and a 1280×720 copy.
4. Report titles, thumbnails, description, release plan → `g8`. Owner uploads.
