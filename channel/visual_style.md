# Visual Style

**Premium investigative business documentary — evidence, money, power, consequence.**
The film must look *constructed from evidence*, not decorated with legal clichés.

Palette, type and safe zones: see `brand.md`.

## Truth hierarchy on screen
1. Authentic source / evidence (with `source_id`).
2. Licensed real-world context (places, buildings, products).
3. Editor-built factual graphics (money, timelines, ownership maps).
4. Illustrative generated imagery — only where it cannot be mistaken for evidence.

## Canonical frame style (paste into every image prompt)
> WHAT IT COST canonical frame style: premium investigative business documentary; charcoal/black textured background; warm aged-paper evidence layers; off-white distressed condensed headline; restrained deep-red underline/tab accents; realistic paper depth and film grain; strong cinematic negative space; serious corporate/legal tone; no horror, no crime-poster look, no neon, no dashboard/card-grid, no decorative clutter.

## Style reference images (`WhatItCost_media/_style_refs/`)
Approved VIDEO_001 frames. Attach one per image prompt as **style only** (never copy their content — eBay, insects, names, numbers, logos):
| File | Use for |
|---|---|
| `style_evidence.png` | T01 evidence, T05 place — headline left, photo stack on paper right |
| `style_cards.png` | T07 accountability / comparisons — several items on aged paper cards |
| `style_money.png` | T04 money — one dominant amount + real-world photo |
| `style_quote_document.png` | T03 document / quote — quote headline + document excerpt with red highlight |
| `style_timeline_place.png` | T05 / T06 — date headline over darkened place/aerial photo |

## Frame families
| ID | Family | Use |
|---|---|---|
| T01 | Evidence | physical/authentic evidence, one object hero |
| T02 | Person / legal status | who someone is + exact status |
| T03 | Document / quote | one real crop, one highlighted line |
| T04 | Money | one dominant verified figure + caveat |
| T05 | Place / real world | location, building, breather beats |
| T06 | Timeline / cause | date spine, cause → effect, flows |
| T07 | Accountability | roster of outcomes per person/entity |

Vary at least two of: focal side, crop, paper layering, document/photo balance, headline placement. Never the same family three beats in a row.

## Prompt rules (image models)
1. 16:9, 1920×1080 target; bottom 22% dark and quiet.
2. Generated readable text = only the exact headline (+ optional one support line). No pseudo-text, no small print.
3. One hero idea + one support idea max.
4. Never generate full documents, filings, screenshots, chat logs, web pages, seals, signatures, docket numbers, stamps.
5. Real documents: composite the authentic crop afterwards — never ask the model to redraw it.
6. No real-person likeness synthesis.
7. Style references carry only palette/texture/type scale/framing — never factual content (VIDEO_001 lesson: refs leaked content into other frames).
8. Raw PDF/HTML never goes to the image model; prepare a tight crop first.
9. Final usable frame, not a style board; no post-generation fixing should be needed.

## Image → video (animation) prompts
- Only for beats marked `video_gen` in `beats.csv`.
- Describe: camera move (slow push, parallax, pan), subject motion (subtle), duration (match beat length, usually 3–6 s), what must stay still (text, documents, faces).
- Text and documents must not morph. Faces of real people are not animated.
- No shake, whip-zoom, glitch, bounce.

## Motion in edit
Deliberate push-ins, masked document reveals, highlight sweeps, date-spine progression, map-line reveals, factual count-ups, subtle parallax.
Avoid: constant glitch, fake CCTV, typewriter gimmicks, HUDs, stock law imagery, anything that blurs whether material is authentic.

## Forbidden
Key content in the subtitle zone · crime-poster/horror/gore · fake CCTV · HUD/glitch overload · floating black info cards · card-grid dashboards · overcrowded panels · neon · gavel/scales/courthouse as default · fabricated documents · generated likenesses of real people · fake evidence labels/stamps.

## Allowed on-screen labels
COURT RECORD · DOJ SOURCE IMAGE · AUTHENTIC CASE EVIDENCE · CIVIL CASE · CRIMINAL CASE · NOT A JUDGMENT · ALLEGED · SOURCE / DATE / ROLE / LOCATION. Short, factual, source-bound. Never invent file numbers or case metadata.
