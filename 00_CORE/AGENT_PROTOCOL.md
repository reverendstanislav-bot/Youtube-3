# Agent Protocol

## Authority
Repository truth overrides chat memory. `manifest.yaml` is the authoritative per-video state.

## Resume one video
1. Read Foundation.
2. Read Core schemas/gates.
3. Read relevant Channel bibles.
4. Locate the package in `VIDEO_INDEX.csv`.
5. Read its manifest + STATE.
6. Execute only the next unblocked stage.

## Sequential rule
Stages are dependency-ordered. Downstream canonical artifacts must use locked upstream inputs.

## Evidence
For material legal/factual assertions:
- source first;
- claim classification second;
- script wording third.
Never reverse that order.

## Review separation
Research synthesis, fact/legal review, script performance review, packaging review and final release review require an independent pass when available.

## Stage handoff
After material work update:
- `manifest.yaml`;
- `STATE.md`;
- `VERSION_LOG.md`;
- `SOURCE_INDEX.csv`, `CLAIMS_LEDGER.csv`, `CASE_EVENT_LEDGER.csv` as relevant;
- `QA_LEDGER.csv`;
- `ASSET_MANIFEST.csv` as relevant.

Run the stage-aware audit before advancing.
