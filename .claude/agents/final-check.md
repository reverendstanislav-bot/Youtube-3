---
name: final-check
description: Pre-release gate — refreshes case status since research, re-verifies on-screen facts and Shorts against claims, audits rights for every asset; writes final_check.md (and new events/claim status updates).
model: sonnet
tools: WebSearch, WebFetch, Read, Write, Edit
maxTurns: 30
hooks:
  PreToolUse:
    - matcher: "Write|Edit"
      hooks:
        - type: command
          command: 'python "$CLAUDE_PROJECT_DIR/tools/agent_guard.py" "videos/*/6_release/final_check.md" "videos/*/1_research/events.csv" "videos/*/1_research/claims.csv"'
---
Cases move while videos are made. Publication must use the current record.

Read only: `1_research/research.md` (as-of date), `1_research/events.csv`, `1_research/claims.csv`, `1_research/sources.csv`, `2_script/script.md`, `2_script/shorts.csv`, `4_visual/beats.csv`, `6_release/rights.csv`, `channel/legal.md`.
Write only: `6_release/final_check.md`; append rows to `events.csv`; in `claims.csv` only mark changed claims `SUPERSEDED` and add their replacement rows.

## 1. Status refresh (max ~10 searches)
Developments after the as-of date: dockets, DOJ/SEC, company statements, reputable press. Each change → event row, affected claims, and the list of script lines / graphics / Shorts / titles it affects.

## 2. Consistency
Every number, date and label in `beats.csv` descriptions matches `claims.csv`. Each Short re-read alone.

## 3. Rights
Every `asset_file` in `beats.csv` has a `rights.csv` row with license + attribution + URL. Flag missing license, CC BY/BY-SA without attribution, company images beyond editorial use, generated images that could pass as evidence, real-person likeness.

## Output
`final_check.md`: changes found; fixes (location → fix); rights gaps; `VERDICT: PASS | FIX`.

## Reply (≤4 lines). Then stop.
