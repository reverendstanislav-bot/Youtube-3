# YouTube 3 — Business Stories Where Money & Law Collide

Agent-first production operating system for an English-language, US-focused, faceless long-form documentary channel.

## Positioning
**The hidden lawsuits, contracts and scandals behind companies, creators and products people already know.**

Law is the mechanism of the story, not the lecture topic.

Core story formula:

`Company / Creator + Money + Conflict + Hidden Problem + Legal Mechanism + Consequence`

## Repository model
- `00_FOUNDATION/` — channel-wide locks and source/legal standards.
- `00_CORE/` — schemas, stage contracts, QA gates and agent operating rules.
- `01_CHANNEL/` — storytelling, fact-checking, legal-editorial, visual, voice and packaging bibles.
- `02_PIPELINE/` — topic backlog and video locator only.
- `03_VIDEOS/` — all episode-specific work; one durable package per video ID.
- `04_SHARED/` — proven reusable assets/components only.
- `tools/` — package creation and audits.
- `.github/` — structural CI.

## Non-negotiable legal/factual rule
Never upgrade an allegation, complaint, charge or claim into an established fact.

Every material factual/legal statement must be traceable through the episode's:
- `SOURCE_INDEX.csv`
- `CLAIMS_LEDGER.csv`
- `CASE_EVENT_LEDGER.csv`

## Read order
1. `AGENTS.md`
2. `00_FOUNDATION/`
3. `00_CORE/`
4. relevant `01_CHANNEL/` bibles
5. `02_PIPELINE/VIDEO_INDEX.csv`
6. target video's `STATE.md` + `manifest.yaml`
7. only the artifacts required for the current stage

Git is the control plane, not the raw-media warehouse.
