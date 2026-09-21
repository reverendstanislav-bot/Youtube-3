# VIDEO 001 — 09 Voice QA + Lock

Status: **PASS / VOICE INPUT LOCKED / NO AUDIO GENERATED**

Canonical voice input:
`08_VOICE_SCRIPT.md`

Narrator:
**Bram — FINAL LOCK**

Voice:
- Provider/catalog: Higgsfield
- Voice type: `preset`
- Voice ID: `549ff70a-3ee7-4f04-a4d9-89a24fab7709`
- Synthesis engine/model: **NOT YET LOCKED**
- Paid generation authorization: **NOT GRANTED**

Stage:
**09_VOICE_QA_LOCK**

---

## Result

Stage 09 passes the **text/input QA lock**.

No audio was generated during this stage.

The next stage may not submit TTS or spend credits until the owner explicitly approves:
1. engine/model;
2. exact generation scope;
3. estimated cost/credits;
4. number of generation jobs.

---

## Semantic fidelity audit

Method:
- isolated S01–S12 narration from `07_SCRIPT_FINAL.md`;
- isolated S01–S12 narration from `08_VOICE_SCRIPT.md`;
- removed section metadata;
- reversed only the Stage 08 spoken normalizations;
- compared the resulting narration text.

Result:
**PASS — semantic text matches the Stage 07 canonical script after reversing allowed delivery normalizations.**

No factual, legal, attribution, chronology, money or party-position changes were introduced.

---

## Stage 09 correction applied

One Stage 08 normalization defect was found and corrected:

- `1999` → `nineteen ninety-nine`

No narrative meaning changed.

---

## Number/date QA

Verified spoken forms in the voice input:

- 2019 → twenty nineteen
- 2020 → twenty twenty
- 2021 → twenty twenty-one
- 2024 → twenty twenty-four
- 2025 → twenty twenty-five
- 2026 → twenty twenty-six
- 2027 → twenty twenty-seven
- 1999 → nineteen ninety-nine
- August 1 → August first
- August 6 → August sixth
- August 15 → August fifteenth
- August 16 → August sixteenth
- February 25 → February twenty-fifth

Money/quantity language remains locked exactly to the Stage 07 meaning, including:
- fifty-five-point-seven million dollars;
- forty-eight-point-seven million dollars;
- forty-six-point-one-five million dollars;
- fifty-eight-point-seven-million-dollar **non-award warning**;
- separate three-million-dollar criminal penalty;
- fifty-seven months;
- twenty-four months.

Result:
**PASS**

---

## Abbreviation QA

Locked spoken treatment:
- CEO → C-E-O
- GPS → G-P-S
- PFC → P-F-C
- DPA → D-P-A

Do not expand DPA into a different legal phrase when the script intentionally uses the abbreviation after the full term has already been introduced.

Result:
**PASS**

---

## Pronunciation lock

### High-confidence locked pronunciations

**Steiner**
- Spoken: **STY-ner**
- IPA reference: /ˈstaɪ.nɚ/ in US English.
- Reference: Cambridge Dictionary, Steiner pronunciation:
  https://dictionary.cambridge.org/pronunciation/english/steiner

**Natick**
- Spoken: **NAY-tick**
- IPA reference: /ˈneɪtɪk/.
- References:
  https://forvo.com/word/natick/
  https://www.collinsdictionary.com/us/dictionary/english/natick

### Safe brand/common-word treatment

- eBay → normal English brand pronunciation; retain spelling `eBay`.
- EcommerceBytes → retain canonical spelling in the source; if the selected engine merges or mangles the word at Stage 10, use the spoken-safe rendering **E-commerce Bytes** without changing the named entity.
- Craigslist → retain canonical spelling.
- FidoMaster → retain exact username spelling. Do not rewrite the username in evidence text; auditory correction may separate the compounds only if needed.

### Names requiring auditory confirmation in Stage 10

Do **not** invent phonetic respellings for these in the canonical text without a reliable person-specific reference:

- Ina Steiner — first name only;
- Steve Wymer;
- Devin Wenig;
- Jim Baugh;
- Wendy Jones;
- Brian Gilbert;
- David Harville;
- Veronica Zea;
- Patti Saris.

Reference leads recorded for Stage 10 auditory QA:
- Steve Wymer appears in an eBay-era podcast/interview:
  https://aaronkwittken.com/brand-on-purpose/ebay-steve-wymer
- Devin Wenig appears in a McKinsey video interview:
  https://www.mckinsey.com/capabilities/operations/our-insights/flow-without-friction-an-interview-with-ebays-devin-wenig
- Ina and David Steiner, Veronica Zea, Jim Baugh, Wenig and Wymer are named in the CBS/60 Minutes segment:
  https://www.cbsnews.com/news/investigation-ebay-employees-stalk-harass-couple-60-minutes-transcript-2023-03-26/
- Patti Saris has recorded public talks/oral-history material:
  https://millercenter.org/the-presidency/presidential-oral-histories/patti-b-saris-oral-history

Important:
**Stage 09 does not claim these person-specific pronunciations were audibly verified when they were not.**
The lock is that no speculative phonetic spelling may be inserted. Stage 10 audio QC must listen for them before accepting the final master.

---

## Legal-term QA

Keep normal American-English legal pronunciation and preserve exact terms:

- deferred prosecution agreement;
- summary judgment;
- tortious conduct;
- interstate stalking;
- witness tampering;
- compliance monitor;
- civil liability;
- criminal Information.

Special delivery rule:
legal caveats must be spoken with the same clarity and weight as damaging allegations or dramatic facts.

Result:
**PASS**

---

## Delivery / pacing QA

Bram delivery remains locked to:
- calm, adult, credible;
- conversational documentary tone;
- no trailer voice;
- no prosecutorial performance;
- no acting of internal quotes;
- no sensational emphasis on harassment objects;
- slightly slower S11 financial breakdown;
- deliberate isolated beats in S01 and S12;
- no CTA before the final line.

Blank-line paragraph structure remains the pause/chunk system.

No SSML is locked at Stage 09 because the synthesis engine/model has not yet been selected.

Result:
**PASS**

---

## Legal/factual boundary check

Confirmed unchanged:
- $55.7M remains the announced total civil settlement package, not an eBay-only payment or judgment;
- eBay direct compensation share remains $46.15M;
- $3M DPA penalty remains separate;
- eBay is not called convicted;
- Wenig, Wymer and Jones are not called criminally charged or convicted;
- surviving summary-judgment claims are not converted into liability findings;
- Wenig's defense remains attributed;
- GPS installation remains an attempt;
- February 2026 remains a failed settlement in principle;
- final WHAT IT COST payoff remains uninterrupted.

Result:
**PASS**

---

## Stage 09 lock

Locked inputs for the next stage:
- narrator: **Bram**;
- voice ID: `549ff70a-3ee7-4f04-a4d9-89a24fab7709`;
- canonical TTS text: `08_VOICE_SCRIPT.md`;
- pronunciation policy: this file;
- factual/legal authority: `07_SCRIPT_FINAL.md`.

Stage 10 must not silently rewrite narration.

Any discovered pronunciation fix at Stage 10 may adjust only spoken rendering, not factual/legal meaning.

**Stage 10 is NOT started by this lock.**
**No audio generation is authorized by this file.**
