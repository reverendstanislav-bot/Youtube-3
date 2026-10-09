# VIDEO 004 — Stage 09 Voice QA + Input Lock

Date: 2026-10-09
Result: **HISTORICAL V09 PASS_INPUT_LOCK — NOW INACTIVE / AUDIO_NOT_GENERATED**

Owner reopened the episode for minimum90 on2026-10-09. Current V11 wording invalidates this V09 payload lock and42-credit price for downstream use. The original QA/quote record below is history only; no generation was submitted.
Scope: exact V09 generation input and episode settings only. No script rewrite, voice test, narration generation, media QC or Stage10 advancement.

## Independent review

Maker mechanical check; independent precision critic `/root/v08_precision`: PASS; independent delivery critic `/root/review_correction`: PASS_INPUT_PREPARATION. Both read current files and reported no blocking text/input issue. Lead accepts the input lock, not a heard-performance or release verdict.

## Canonical fidelity

- 17 canonical sections;149 canonical paragraphs correspond in order to149 voice paragraphs.
- 2080 canonical tokens;2140 normalized spoken tokens. Exactly18 paragraphs differ only by explicit numbers, years, dates, acronym/caption pronunciation and removed Markdown italics.
- Zero omissions, duplications, attribution changes, extra voiceover or reordered paragraphs.
- No section/part heading, instruction, SSML, lock note or spend gate is included in a generation payload.
- Only the exact three payloads beneath PART A/B/C in08_VOICE_SCRIPT.md may be submitted; never submit the full Markdown file.

## Locked per-episode input/settings

Provider: Higgsfield. Planned episode wrapper `text2speech_v2`, variant `elevenlabs`, voice type `preset`, Harrison voice ID `573e5163-59b3-4926-aab1-951ef2985f81`; count1 per part. No additional tuning/SSML/ad-libs or independent Shorts TTS is authorized.

Foundation locks narrator identity Harrison, but lists the global synthesis engine as NOT_YET_LOCKED. This episode-specific input/settings freeze does not alter that channel lock or imply owner-approved spend. The proposed engine/cost must be explicitly approved for submission.

Exact payload hashes are SHA-256 of UTF-8 text with LF paragraph separators and no surrounding whitespace.

| Part | Sections | Characters | Normalized tokens | Exact payload SHA-256 | Fresh credits |
|---|---|---:|---:|---|---:|
| A | S01–S06 | 4929 | 770 | e26b0cf977411f932b5ebf01b11f5385991bca2b0eb9e67743e3447b007be10a | 14.85 |
| B | S07–S11 | 4210 | 638 | 116a642bdd448a9062b299790b4582f1b96c5ae56efe46fc17387d59dedfe590 | 12.75 |
| C | S12–S17 | 4793 | 732 | 03b334387e8d92c2415eb022ee8b733d9f74b4a7a2e553c94ae39ba888139a17 | 14.40 |
| TOTAL | S01–S17 | 13932 | 2140 | Three locked payloads above | 42.00 |

All parts are below the5000-character provider limit. A has71-character headroom. Boundaries afterS06 andS11 are sentence- and section-safe. Do not add a breathing/tone instruction to the spoken text; any needed changes require recheck and a new quote.

## Names / numbers / status

Written pronunciation preparation preserves Valve, Steam, American Arbitration Association and A-A-A/A-A-A's; In re Valve Antitrust Litigation; preliminary injunction; irreparable; unconscionable; Ninth Circuit; Fish. Pronunciation of the eventual render is NOT_REVIEWED.

Counts997/4991/454/572/118/624 and years/dates are spoken explicitly.64-day interval retained; appeal26-6269 becomes twenty-six dash six two six nine; v. becomes versus. Conditional appellate review, likely/preliminary/nonfinal scope, opposing positions and record-bounded current-status wording are unchanged. No new official docket refresh.

## Pauses / continuity / editability

Paragraph breaks preserve reveal beats, questions, answers and standalone caveats without embedding arbitrary pause commands. A ends the contract-change setup; B begins the actual rewrite. B ends mixed-result setup; C begins the documented distinctions. These cuts avoid mid-sentence/breath editing in text; audible transitions still require listening after generation.

Controlled documentary delivery remains the target: curiosity without prosecution, complete negations/legal qualifiers, clear counts, no shouting or artificial acceleration. Actual Harrison pace, pauses, timbre and continuity are NOT_MEASURED. Planning15:21 at139.4wpm is not an audio-runtime lock.

## Shorts integrity

| Short | Exact source paragraphs | Normalized tokens | Part | Planning total139.4wpm +3s CTA +2s pause allowance |
|---|---|---:|---|---:|
| SH01 | S01 p1-4 | 34 | A | 19.63s |
| SH02 | S04 p1-4 | 40 | A | 22.22s |
| SH03 | S05 p1-4 | 44 | A | 23.94s |
| SH04 | S07 p1-4 | 38 | B | 21.36s |
| SH05 | S08 p1-5 | 43 | B | 23.51s |
| SH06 | S10 p1-5 | 36 | B | 20.49s |
| SH07 | S11 p1-5 | 43 | B | 23.51s |
| SH08 | S14 p1-4 | 37 | C | 20.93s |

All8 cuts are contiguous long-form source text, wholly inside one part. No extra/reordered canonical Short VO.0.35s soft transition remains inside the silent3s CTA budget. Text timing has margin, but final delivered files must each be measured<=30.00s. No burned captions, shake or crop jumps; smooth CTA ending remains a later edit obligation, not a completed media verdict.

## Cost preflight and spend boundary

Fresh exact-input get_cost:true responses obtained2026-10-09, verification timestamp 2026-10-09T14:22:46.059Z. The service explicitly returned No job submitted for all3 estimates: A14.85, B12.75, C14.40; total42.00 credits. Prior41.10V08 price and earlier missing V09 estimate are superseded. Quotes do not promise quality/runtime and may need refreshing if input/settings or pricing changes.

Read-only balance snapshot:1166.67 credits, ultra plan; unlim_available=false. No applicable unlimited audio entitlement reported. Paid generation authorization remains false. Submitted jobs0; this stage only read/preflighted inputs, no generation credit consumed.

## Provenance / deterministic verification

| File | SHA-256, actual workspace bytes |
|---|---|
|07_SCRIPT_FINAL.md|699b20b87a889a7c3647b05321ac77530ae8431dc4e81d0c114a516efdb3cdb5|
|08_VOICE_SCRIPT.md|94abbe907679435424f77ff85963a069f5ad59dcefeb2a6f9b5eec84a7c452c8|
|07_SHORTS_LOCK.csv|16d154521a6c9f622053a67b2ed0d8ccd051c025d91375951581940a6bfbb6a8|

The three upstream artifacts remain byte-identical to the accepted V09 text. CSV counts/settings and all Short ranges checked. Exact-input mechanical comparison passed with zero mismatch. Strict package audit and repository contract validation must pass before committing the state transition.

## Acceptance and handoff

voice_input=true locks text/settings only. audio_master=false; Stage10 NOT_STARTED. Current stage09_VOICE_QA_LOCK. No factual rewriting during later performance polishing. Any input/settings change invalidates the payload lock and requires review/requote.

Before Stage10 submission obtain explicit owner approval for Higgsfield/text2speech_v2/elevenlabs/Harrison, exactly3 parts,42.00 credits quoted; no extra test or retry authorized.

After authorized generation: listen to all parts at normal speed; compare every paragraph/count/date/negation; inspect pronunciation of the terms above; check A→B/B→C loudness, timbre, pauses and clipped breath; decode/probe the final audio and measure all8 exact Shorts+CTA. The opening/library stake, S09 and S14–17 need real timing and meaningful pauses. Keep final two lines unhurried. Official release refresh remains Stage16.
