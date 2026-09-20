# Repository Contract

## Global truth
Outside video folders store only reusable channel/system truth:
- Foundation locks;
- Core schemas/rules;
- Channel bibles;
- pipeline locators/backlog;
- shared approved components;
- automation.

## Video truth
Any information about one identifiable episode belongs in `03_VIDEOS/VIDEO_0XX_*`, including:
research, sources, case chronology, claims, competitor notes, scripts, reviews, audio, visual plan, prompts, documents, assets, edit QA, packaging, upload package and analytics.

## Canonical state
- channel locks: `00_FOUNDATION/`;
- topic candidates: `02_PIPELINE/TOPIC_BACKLOG.csv`;
- video locator: `02_PIPELINE/VIDEO_INDEX.csv`;
- machine state: `<video>/manifest.yaml`;
- handoff: `<video>/STATE.md`;
- source catalog: `SOURCE_INDEX.csv`;
- material assertions: `CLAIMS_LEDGER.csv`;
- procedural chronology: `CASE_EVENT_LEDGER.csv`;
- QA issues: `QA_LEDGER.csv`;
- assets: `ASSET_MANIFEST.csv`.

## No duplicate truth
Do not maintain a second status narrative, second case chronology or global episode research ledger.

## Video ID immutability
A numeric video ID is never reused for another concept. Cancelled/abandoned packages retain their ID and receive an appropriate status.

## Heavy media
Git stores control-plane text/metadata and small references. Large media lives in approved artifact/external storage and is referenced by manifest/asset ledger.
