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
