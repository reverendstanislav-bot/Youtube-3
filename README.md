# WHAT IT COST — YouTube Production OS

Agent-first production operating system for an English-language, US-focused, faceless long-form documentary channel.

**Tagline:** Where business decisions get expensive.

## Positioning
**The hidden lawsuits, deals and decisions behind companies, creators and products people already know.**

Law is the mechanism of the story, not the lecture topic.

Core story formula:

`Company / Creator + Money + Conflict + Hidden Problem + Legal Mechanism + Consequence`

## Repository model
- `00_FOUNDATION/` — channel-wide locks, qualification, source/legal standards and launch shortlist.
- `00_CORE/` — schemas, stage contracts, QA gates, qualification scoring and agent operating rules.
- `01_CHANNEL/` — storytelling, competitor research, source capture, fact-checking, legal wording, visual, voice and packaging bibles.
- `02_PIPELINE/` — topic backlog and video locator only.
- `03_VIDEOS/` — all episode-specific work; one durable package per immutable video ID.
- `04_SHARED/` — proven reusable assets/components only.
- `tools/` — package creation and audits.
- `.github/` — structural CI.

## Before a video exists
Discovery stays in `TOPIC_BACKLOG.csv`.

A topic must pass `TOPIC_QUALIFICATION_SCHEMA.md` and the hard locks in `TOPIC_QUALIFICATION_LOCK.md` before a durable video package is created.

Decision states:
- GO
- HOLD
- NO-GO

## Non-negotiable legal/factual rule
Never upgrade an allegation, complaint, charge or claim into an established fact.

Every material factual/legal statement must be traceable through the episode's:
- `SOURCE_INDEX.csv`
- `CLAIMS_LEDGER.csv`
- `CASE_EVENT_LEDGER.csv`

## Read order
1. `AGENTS.md`
2. `00_FOUNDATION/`
3. `00_CORE/CHANNEL_OPERATING_MAP.md` + relevant schemas
4. relevant `01_CHANNEL/` bibles
5. `02_PIPELINE/VIDEO_INDEX.csv`
6. target video's `STATE.md` + `manifest.yaml`
7. only artifacts required for the current stage

Git is the control plane, not the raw-media warehouse.
