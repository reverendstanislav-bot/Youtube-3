# Legal & Evidence Rules

**Core rule: never upgrade an allegation, complaint, charge or claim into an established fact.**
Order is always: source → claim status → script wording. Never reverse it.

## Claim status values (`claims.csv` → `status`)
| Status | Means | Safe wording | Never |
|---|---|---|---|
| ALLEGATION / COMPLAINT | asserted by a party, not established | "the complaint alleges…", "according to the lawsuit…" | "X did…" |
| CLAIM | a party's position | "X argues / says / claims…" | stating it as fact |
| CHARGE | formal criminal accusation | "prosecutors charged X with…" | "X committed…" |
| RULING | court decision on a defined issue | "the judge ruled / the court held…" + scope | broader than the holding |
| VERDICT | factfinder result | "the jury found…" + which counts, later status | ignoring appeals |
| SETTLEMENT | negotiated resolution | "the parties settled", "X agreed to pay…" | "X admitted wrongdoing" (unless documented) |
| DISMISSAL | ended at that stage | "the judge dismissed [claim]…" + with/without prejudice | "proved false" |
| CONVICTION | guilt by plea or verdict | "X pleaded guilty / was convicted of…" + posture | — |
| ADMISSION | expressly admitted by the party | "X admitted…" | — |
| DENIAL | disputed | "X denied…" | treating it as proof of falsity |
| UNDISPUTED_FACT | supported, not materially disputed | plain statement | — |
| REPORTED_FACT | responsibly reported, not a finding | "according to [outlet]…" | — |
| ANALYSIS / OPINION | our inference | clearly framed as analysis | — |
| UNKNOWN | unresolved | — | **blocks the script** |

## Invariants
- Civil ≠ criminal ≠ regulatory. Never blur them.
- Settlement ≠ admission ≠ judgment. Dismissal of a count ≠ dismissal of the case.
- Surviving a motion ≠ liability. Attempt ≠ completed act.
- A number must say what it is: demand, alleged loss, award, settlement, valuation, estimate — with its date basis.
- A source proves someone **said** something; it does not prove the thing is true.
- No motive unless documented or clearly framed as analysis.
- Include material denials/responses.
- Current case status is refreshed before release.

## Source tiers (`sources.csv` → `tier`)
1. Primary: filings, orders, judgments, dockets, verdict forms, statutes, agency records, SEC filings, official statements, record exhibits.
2. Original high-quality journalism.
3. Specialist/trade reporting — corroborate disputed claims.
4. General secondary — background only.

Never sufficient alone for a material disputed claim: AI summaries, search snippets, aggregators, unsourced blogs, reposts, anonymous social posts, Reddit/forums, another YouTube video.

## Packaging
Titles and thumbnails may simplify but may never make a stronger accusation than the record supports. If the punchy verb needs a stronger status — pick another verb.

## Documents on screen
- AUTHENTIC_SOURCE — real document with `source_id`; crop must not hide material context.
- EDITOR_RECREATION — built from verified text; never passed off as a scan.
- ILLUSTRATIVE — metaphor; must not look like real evidence.
- Never generate filings, emails, signatures, docket stamps, seals, letterheads or quotes. If exact text must be readable, composite the authentic crop — do not let an image model redraw it.
- No AI likeness of real people. Real photos may be cropped/framed, not reinvented.

## Rights
Every image/video in the final cut has a row in `rights.csv`: origin, license (CC0 / CC BY / CC BY-SA / public record / own generation / fair-use editorial), attribution text, source URL. CC BY/BY-SA require on-screen or description credit.
