# VIDEO007 — Harrison audio QC plan

**Applies only after separately authorized generation. No audio was generated during planning.**

## 1. Identity gate after Job 01

- Compare the generated narrator with the canonical Harrison Higgsfield preview/approved sample in `00_FOUNDATION/VOICE_LOCK.md` and the clean VIDEO004 Harrison reference lineage.
- Require the same perceived speaker identity, controlled US-English documentary tone and stable timbre.
- If identity is materially wrong, stop. Do not submit Jobs 02–05, retry, switch model or create a new profile automatically.

## 2. Pronunciation and legal-language checklist

Listen in context for: Apple; OpenAI; ChatGPT; Siri; `io Products` as “eye-oh Products”; Chang Liu; Tang Yew Tan; Judge Edward Davila; San Jose; Singapore; LINE messages; ECF numbers; preliminary injunction; expedited discovery; forensic inspection; stipulation; counterclaim; moot; trade-secret; intellectual-property; preservation.

Verify dates and counts exactly as written, including June twenty twenty-four, July tenth twenty twenty-six, October ninth/twelfth/thirteenth/fourteenth/sixteenth, five-day and fourteen-day deadlines, fourteen employee devices, dozens of Apple files and more than one hundred OpenAI files. Preserve the distinctions between allegation, filing, party search account, court order, mootness and merits finding.

## 3. Text/order gate

- One output per existing segment; no rewritten input.
- Confirm all 60 paragraphs once, in order, against the five Stage08 files and their SHA-256 values.
- Use ASR/readback as supporting evidence if a local transcription model is separately made available; human review remains controlling for names, numbers and legal qualifiers.
- Reject missing sentences, duplicate passages, reordered paragraphs, inserted headings or spoken metadata.

## 4. Technical audio gate

- Record generation ID, exact model/profile/seed, output filename, duration and SHA-256.
- Require `ffmpeg -v error -xerror` decode PASS and inspect codec, sample rate, channels, clipping, DC offset, peak and integrated loudness.
- Listen for robotic bursts, repeated words, truncated endings, phoneme breaks, metallic ringing, long dead air, clicks and abrupt segment boundaries.
- No automatic regeneration. Log exact timestamp and defect before requesting any retry.

## 5. Assembly and pacing gate

- Preserve paragraph pauses without adding spoken act titles.
- Check opening pace and the transitions between the five outputs before Stage10.
- Do not assemble or label a Stage10 master until all five candidates pass identity, text, pronunciation and technical checks.

## 6. Shorts timing gate

Use `09_SHORTS_AUDIO_EXTRACTION_PLAN.csv`. Extract all four later from the unified long-form master, on sentence/paragraph boundaries, with no separate TTS. Measure narration and complete export including ending/CTA/tail. Each must be `<=35.0` seconds; estimates are not a PASS.
