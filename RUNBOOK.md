# RUNBOOK — exact dispatch steps per phase

Dispatcher = main Claude session. Read only the section of the phase you are running.
Conventions:
- `<id>` = 3-digit video id, `V` = `videos/<id>-<slug>`, `M` = media root from `status.yaml`.
- Agent prompts are short and literal. Copy the template, fill the brackets, add nothing else.
- Agents that are independent run **in parallel** (one message, several Agent calls).
- After every agent: `python tools/yt.py check <id>`; fix mechanical problems yourself, send content problems back to the same agent once.
- Agents never see each other's replies — everything passes through files.
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
3. WeftCut: import narration, `transcribe_clip` (word timestamps), save the envelope JSON → `python tools/yt.py words <id> <envelope.json>`.
4. `python tools/yt.py audio-metrics <id>` → **audio-qc** — `Video <id>.`
5. FIX → regenerate only listed sentences (new spend approval), re-join, repeat 3–4.

## Phase 5 — Visual → gates G4, G5

1. **visual-director** — `Video <id>. Mode 1.`
2. Parallel: **prompt-engineer** — `Video <id>. Image prompts for all image/video_gen beats.` · **document-designer** — `Video <id>. All document beats.` (before it: `python tools/yt.py pages <id> --sources <ids>` for the pages it needs).
3. `python tools/yt.py doc-shots <id>` · `python tools/yt.py handoff <id> --kind img` → tell the owner the folder path and the count. Wait.
4. Owner drops files → `python tools/yt.py ingest <id>` → **visual-director** — `Video <id>. Mode 2.`
5. Rejects → **prompt-engineer** `Video <id>. Fixes.` → `handoff --kind img` → owner → back to 4. When all image beats ACCEPTED: `g4 APPROVED` (owner confirms).
6. **prompt-engineer** — `Video <id>. Video prompts.` → `handoff --kind vid` → owner → `ingest` → `python tools/yt.py frames <id> video_gen/<file>` per clip if needed → **visual-director** Mode 2 → `g5`.
7. `python tools/yt.py hash-beats <id>`.

## Phase 6 — Edit → gates G6, G7

1. WeftCut: new project for the video, 1920×1080 25 fps. Import narration + all `asset_file`s from `beats.csv`. Lay beats on the timeline by `start`/`end`; graphics beats = brand motifs (`weftcut/README.md`); document beats = `M/documents/*.png` with a slow push; image beats with subtle push/pan; `video_gen` beats as clips. One `wic-captions-16-9` layer over the whole runtime with `words.json`.
2. Render to `M/renders/cut_vN.mp4`. `python tools/yt.py frames <id> renders/cut_vN.mp4` → **retention-editor** — `Video <id>. Cut vN.` → apply fixes → re-render.
3. `python tools/yt.py render-qc <id> renders/cut_vN.mp4`. Report → `g6`.
4. Shorts: for each row in `shorts.csv` build a 9:16 composition from the same beats (+ `wic-captions-9-16` with the words of that range, `offset_s` = range start), render to `M/shorts/SHxx.mp4`, `render-qc` each → `g7`.

## Phase 7 — Release → gate G8

1. Parallel: **final-check** — `Video <id>.` · **packaging** — `Video <id>. Mode 2.`
2. **defamation-risk** — `Video <id>. Packaging mode.`
3. Thumbnail: owner generates the base image from packaging's prompt; Claude composes text/layout (WeftCut or ffmpeg) → `M/thumbnail/thumb_A.png` (+B, C), 1280×720 derivatives.
4. Report titles, thumbnails, description, release plan → `g8`. Owner uploads.
