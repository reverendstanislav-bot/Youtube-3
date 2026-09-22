# AGENTS.md — YouTube 3 Production OS

ChatGPT is the lead operator. Repository truth overrides chat memory.

## Mandatory read order
1. `00_FOUNDATION/README.md` and relevant locks.
2. `00_CORE/AGENT_PROTOCOL.md`, `AGENT_PLAYBOOK.md`, schemas and gates.
3. Relevant `01_CHANNEL/` bibles.
4. `02_PIPELINE/VIDEO_INDEX.csv`.
5. Target video's `STATE.md` + `manifest.yaml`.
6. Only files needed for the active stage.

## First principle
Global folders contain durable reusable truth only. Any information about one identifiable episode belongs inside that video's folder.

## Evidence rule
Never convert an allegation, complaint, charge, claim, accusation or party assertion into established fact. Script wording must match the status recorded in `CLAIMS_LEDGER.csv` and `CASE_EVENT_LEDGER.csv`.

## Execution
Use maker → independent critics → lead synthesis for research, legal/fact QA, script review, packaging and release QA. A maker must not be the sole approver of a critical artifact when an independent review is available.

## State
`manifest.yaml` is authoritative. `STATE.md` is the concise handoff. `VIDEO_INDEX.csv` mirrors locator/status fields. Drift is an error.

## Do not
- invent missing filings, quotes, rulings, dates or source text;
- rely on an article summary when a material primary source is available and practical to obtain;
- reuse a video ID for a different concept;
- create ad-hoc top-level folders;
- place episode research or analytics in global folders;
- present a recreated/generated document as authentic;
- advance after a FAIL gate;
- silently change channel locks.

## Material changes
Update manifest, STATE, VERSION_LOG and all affected ledgers after material changes.


## Spend approval — HARD LOCK
Any action that can consume paid credits, tokens, generations, API balance, trial allowance or other billable quota requires the owner's explicit approval **before submission**.

This applies to all paid or quota-consuming generation/action tools, including audio/TTS, image, video and external AI services.

Allowed without approval:
- read-only discovery/listing;
- previews already provided by a service;
- read-only balance checks;
- cost estimates that explicitly do not submit a generation/job.

Required before any billable submission:
1. identify the exact provider/model/tool;
2. state the exact or estimated cost/credit usage when available;
3. state how many jobs/generations will be submitted;
4. receive explicit owner approval for that spend.

Do not interpret approval to browse/select voices as approval to generate paid voice tests.
Do not batch paid tests speculatively.


## Task-scope approval — HARD LOCK
Execute only the task the owner explicitly requested in the current turn.

Never expand scope on your own.

Without explicit owner approval, do NOT:
- advance to the next pipeline stage;
- start a "logical next step";
- generate assets, audio, images, video, code, prompts or variants not explicitly requested;
- run optional tests, A/B tests, experiments or candidate generations;
- perform extra research beyond what is required to answer/execute the requested task;
- modify unrelated repository files;
- create new artifacts merely because they may be useful later;
- turn analysis/selection into production/generation;
- interpret "continue", "do this stage", or "pick/select" as permission for downstream work.

Default behavior at task boundary:
1. stop;
2. report exactly what was completed;
3. state the next possible step without executing it;
4. wait for explicit owner instruction.

If the requested task can be completed read-only, keep it read-only unless a write is necessary to fulfill that exact task.
If uncertain whether an action is in scope, do not execute it.


## Shorts architecture — HARD
Every long-form video must be written with cut-ready Shorts from Stage 02 onward. Follow `00_CORE/SHORTS_ARCHITECTURE.md`. Canonical Shorts are contiguous extracts from long-form narration, not post-production rewrites. Stage 07 script lock requires a Shorts lock unless the owner explicitly waives it.
