# VIDEO 004 — Stage 09 V11 Voice QA and exact input/settings lock

Date: 2026-10-09
Result: **PASS_INPUT_LOCK_V11 — NO AUDIO GENERATED / NO PAID SUBMISSION**

## Scope
Owner authorized Stage09. This locks only the current V11 spoken-text payloads and episode voice settings, not a generation, performance assessment or Stage10. V09 historical review and 42-credit quote are superseded; no V09 payload may be submitted.

## Canonical fidelity and preflight
Canonical: `07_SCRIPT_FINAL.md`, V11, 13 sections / 123 narration paragraphs / 1950 raw words. Stage08: 123 paragraphs, 2014 normalized spoken tokens, 16 pronunciation-only paragraph differences, zero semantic omissions/duplications or reordered paragraphs. Stage08 independent precision/delivery preparation reviewers PASS; Stage09 inspected version and three-part mapping. Do not include file headings, Markdown, separators, status notes or instructions inside TTS payloads.

| Part | Exact sections | Characters | Normalized tokens | Exact UTF-8 LF payload SHA-256 |
|---|---|---:|---:|---|
| A | S01–S05 | 4567 | 711 | f81867d76acaa1e33182dee5c766d48cafdb732f3f8f6d0285e06d964122e9d6 |
| B | S06–S09 | 4107 | 624 | 3c38e3759110016120227c7b0f0120f1f914bded957d423daffae453c759505a |
| C | S10–S13 | 4384 | 679 | 5253ebe982b6280e3ae6c850143dcda9b0a23f1f553f5c5819d2c2768dd7c8a3 |
| TOTAL | S01–S13 | 13058 | 2014 | Three separate payloads |

No part exceeds the conservative 5000-character input cap; no sections or Shorts divided across parts. Stage08 and CSV job plan agree on character/word counts, section boundaries, model and voice metadata.

## Locked V11 episode settings
- Service: Higgsfield.
- Engine wrapper: `text2speech_v2`; variant: `elevenlabs`.
- Voice: Harrison, `preset`, ID `573e5163-59b3-4926-aab1-951ef2985f81`.
- Exactly three intended jobs (A/B/C), each count=1; no alternative voice, tuning, SSML or ad-libs.
- Channel-wide synthesis engine remains not globally locked; this is an **episode-only input/settings freeze**.

## Pronunciation and legal risk
Preserve Valve, Steam, American Arbitration Association, King County, Ninth Circuit, Fish; appeal 26-6269 spoken as “twenty-six dash six two six nine”. Dates/counts spoken in normalized natural forms. Preserve all negations and qualifiers: likely/preliminary/as-applied, conditional appellate review, allegations versus rulings, no invented $20M liability or merits outcome. Listening-based pronunciation QA must follow generation; nothing has yet been heard.

## Shorts integrity
Eight contiguous same-audio Shorts (SH01–SH08): three in part A, four in B, one in C; planning 20.06–23.51 seconds including CTA/pause allowance. Real cut times <=30.00 seconds NOT MEASURED. No separate Shorts TTS.

## Cost / authorization gate
**Live V11 quote NOT OBTAINED in this Stage09 update.** Historical V09 42.00 credits is NOT a valid V11 price or spend permission. Before Stage10: obtain read-only fresh quote for all three exact payloads; show owner exact total/settings; require independent explicit credit authorization. Submitted jobs: 0. Spent: 0.

## QA boundary and next action
**PASS_INPUT_LOCK_V11** applies only to text/settings consistency. Stage10/audio master NOT_STARTED; audio quality, pauses, pacing, timbre and phonemes UNTESTED. Last case status refresh 2026-10-07; official release refresh still Stage16. Any change to V11 spoken text or engine/settings invalidates this lock and requires full recheck and re-quote.

Next: read-only V11 exact cost preflight, then separate owner approval before any paid audio job.
