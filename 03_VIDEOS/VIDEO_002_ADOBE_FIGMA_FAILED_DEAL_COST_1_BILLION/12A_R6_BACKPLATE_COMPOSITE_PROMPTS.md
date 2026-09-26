# VIDEO 002 — Stage 12A-R6: Backplate Generation + Deterministic Source/Headline Composite

Status: **CANONICAL PRODUCTION PROMPTS / NO SPEND / NOT GENERATED**
Date: 2026-09-25
Supersedes for production: `12A_R4_DIRECTION_AND_PROMPTS.md` (kept as history).
Beat/headline authority: R4/R2 preserved exactly.
Source authority: `12A_R2_REFERENCE_BINDINGS.csv` + `12A_R2_SOURCE_PREP_QUEUE.csv`.

## Why R6 exists

Repeated R3/R4/R5 tests showed that asking an image model to reproduce an authentic document, UI, logo or photograph "unchanged" is structurally unreliable. The model resynthesizes pixels, invents text/UI, alters faces/logos and can convert film frames into poster/thumbnail compositions. More prompt prohibitions do not solve that.

R6 changes the production method instead of adding more negative wording.

## R6 production method — HARD LOCK

### A. Generated backplate
Higgsfield generates **only the cinematic environment/backplate and non-source physical props**.

For every G001–G085 backplate:
- one 16:9 finished film backplate;
- WHAT IT COST / VIDEO 001 R7 palette/material/lighting;
- **zero readable generated text**;
- **zero generated source content**;
- no logos, UI, legal text, dates, numbers, signatures, seals or authentic-photo recreation;
- no generated faces for source-bound portraits/photos;
- source insertion regions stay clean and unobstructed;
- bottom 22% stays caption-safe.

If the scene description mentions a document, photograph, screenshot, portrait, deal graphic, logo or identifier that is listed under SOURCE INSERTS, **do not render that content in the backplate**. Leave its intended region clean for deterministic compositing.

### B. Deterministic editor composite
After the backplate is generated:
1. insert the exact prepared source file from `12_SOURCE_PREP/`;
2. crop/scale/perspective-position only — no generative resynthesis;
3. preserve source pixels, faces, UI and legal text;
4. add paper border/frame/drop shadow/clip/red bracket/tab/highlight as editor-native elements where the shot calls for them;
5. add the exact locked headline as editor typography;
6. add the short deep-red underline as editor graphics.

### C. Headline lock
The image model generates **no headline at all**. Every headline below is editor-native and must match the locked text exactly.

### D. Source-relative marks
Any red bracket, underline, highlight, tab, pin/thread attachment or clip that must align to source content is **editor-native**, not generated into the backplate.

### E. Failure condition
A source-bound frame is not complete until the exact listed source files have been composited. A generated backplate by itself is never evidence and must not enter the final edit as a substitute for the source.

---

## G001 / Beat B002

**РЕЖИССУРА R6:**  
Постановка из теста подтвердилась. Здесь закреплены только авторский кроп Section 8.2 и красная скобка на полях вместо подчёркивания. Договор крупно справа, заголовок слева сверху: это язык контракта, а не наказание.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV049_S8_2_TERMINATION_FEE_CROP.png` — DOCUMENT / RV049

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Merger Agreement Section 8.2 termination-fee excerpt; it is the page itself, shown unchanged — never retype, redraw or extend its text. No other document, photo or logo may appear.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: one contract page rests at a slight angle on a dark desk, held by a black binder clip at its top edge; a thin vertical deep-red bracket is drawn in its left margin, beside the text, never over it.

Composition: headline zone inside the top 45% and left 40% of the frame. The page fills the right 55%, between 10% and 75% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: underlining inside the document, courts, gavels, government buildings, cash.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **NOT A FINE**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G002 / Beat B003

**РЕЖИССУРА R6:**  
Изменено после теста: модель перевернула композицию, поэтому кадр построен по стандартной схеме. Заголовок сверху слева, справа крупно официальная графика сделки в раме. Из-под рамы торчит угол пачки договора с одной красной закладкой: условие выхода за публичной сделкой.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV025_ADOBE_FIGMA_DEAL_GRAPHIC.png` — PRODUCT-UI / RV025

**R4 SOURCE ROLE / PLACEMENT:** image 1 = official Adobe + Figma deal graphic; it is the framed print, shown unchanged — never redraw or restyle its logos. No other logo, document or photo may appear.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a framed print leans against a dark wall on a desk; beneath its lower edge the corner of a thick stack of blank contract paper protrudes, with one deep-red index tab sticking out.

Composition: headline zone inside the top 45% and left 40% of the frame. The framed print fills the right 55%, between 8% and 65% of frame height; the paper corner and red tab just below it, above 78%. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: writing on the tab, boardrooms, handshakes, people, cash.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **CONTRACTUAL EXIT COST**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G003 / Beat B004

**РЕЖИССУРА R6:**  
Изменено после теста: идея хронологии работает, но модель нарисовала графику. Теперь это прямо снятые предметы: пробковая доска, латунные булавки, натянутая красная нить. Заголовок стоит в верхней четверти и не выше нужного размера. Кроп 20 июля у первой булавки, дальше всё уходит в темноту.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV052_JULY20_FEE_AGREED_CROP.png` — DOCUMENT / RV052

**R4 SOURCE ROLE / PLACEMENT:** image 1 = 424B3 excerpt (July 20: fee agreed); it is the pinned paper, shown unchanged — never retype it. No other document may appear.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: one taut deep-red thread runs horizontally across a dark cork board through exactly three brass pins. At the first pin (left) one small paper excerpt is pinned, sharp and lit; the second pin is in soft light; the third fades into darkness and blur. Nothing is written on the board.

Composition: headline zone inside the top 25% of the frame, left half. The thread at about 55% of frame height; the pinned excerpt just above the first pin. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: labels, dates or numbers on pins, arrows, printed timeline graphics.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **NEGOTIATED BEFORE FAILURE**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G004 / Beat B005

**РЕЖИССУРА R6:**  
Постановка из теста подтвердилась. Закреплены только заголовок сверху по центру и то, что оба фото берутся из вложений. Два отпечатка лежат порознь, между ними пустая бирка на красной нити к обоим: риск, который оценили вместе.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV004_ADOBE_HQ_SAN_JOSE.jpg` — REAL-PHOTO / RV004
2. `12_SOURCE_PREP/RV015_CONFIG_2023_KEYNOTE.jpg` — REAL-PHOTO / RV015

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe headquarters, San Jose (left print); image 2 = Figma Config 2023 keynote stage (right print). Show both unchanged; keep every face and person exactly as photographed; add no people.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: top-down view of a dark desk; two photographic prints lie apart, the left slightly larger; between them sits one blank manila shipping tag whose thin deep-red string runs to a corner of each print.

Composition: headline zone = top center, inside the top 22% of the frame. Prints in the band between 28% and 76% of frame height, left and right; the tag at the exact center. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: writing on the tag, handshakes, money, government buildings.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **PRICING THE RISK**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G005 / Beat B006

**РЕЖИССУРА R6:**  
Постановка подтвердилась. Модель нарисовала свою выписку с «$1,000,000,000», поэтому первая строка прямо говорит: никаких цифр, кроме тех, что во вложении. Один лист по диагонали в жёстком боковом свете, скрепка, скобка на полях.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV063_10K_PAYMENT_CROP.png` — DOCUMENT / RV063

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe FY2023 10-K payment excerpt; it is the paper, shown unchanged — never retype, redraw or extend it. No other document may appear.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: top-down view of a single paper excerpt lying diagonally on a dark desk, caught in one hard beam of side light, a brass paperclip on its upper corner, a thin vertical deep-red bracket in its margin beside the text.

Composition: headline zone inside the top 45% and left 45% of the frame. The paper sits center-right, between 15% and 75% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: banknotes, cash stacks, coins, vaults, underlining inside the document.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **THE RISK BECAME CASH**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G006 / Beat B011

**РЕЖИССУРА R6:**  
Изменено после теста: модель «ответила» на вопрос диаграммой Венна и красной линией. Теперь в кадре ровно два планшета, а тёмная стена между ними описана как намеренная пустота. Заголовок-вопрос занимает только верхнюю полосу кадра.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV037_FIGMA_DEV_MODE_UI.png` — PRODUCT-UI / RV037
2. `12_SOURCE_PREP/RV044_ADOBE_XD_WORKFLOW_UI.png` — PRODUCT-UI / RV044

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Figma Dev Mode product screenshot (left board); image 2 = Adobe XD documentation visual (right board). Show both unchanged — never redraw or invent interface.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: two screenshots mounted on separate matte paper boards hang side by side on a dark wall, evenly lit, equal size. The wide space between them is plain, empty dark wall — a deliberate void with no line, shape, tag or symbol.

Composition: headline zone = top center, inside the top 20% of the frame. Boards in the band between 26% and 74% of frame height, one in the left third, one in the right third. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: Venn diagrams, overlapping circles, connecting lines, arrows, versus signs, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **HOW DIRECTLY DID THEY COMPETE?**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G007 / Beat B013

**РЕЖИССУРА R6:**  
Изменено после теста: модель подставила банкноты, сертификат и график. Запрет на деньги и ценные бумаги стоит в первой строке. Главный предмет — один согнутый пополам чистый лист, половины разного оттенка. Небольшой кроп 8-K прикреплён к углу.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV048_8K_MERGER_AGREEMENT_CROP.png` — DOCUMENT / RV048

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe Form 8-K merger-agreement excerpt; it is the clipped excerpt, shown unchanged — never retype it. No other document may appear.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: one heavy blank sheet of paper folded exactly in half lies open on a dark desk: left half warm ivory, right half cool grey, a thin deep-red line along the fold. One small paper excerpt is paper-clipped to the sheet's upper-right corner.

Composition: headline zone inside the top 45% and left 40% of the frame. The folded sheet center-right, between 20% and 76% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: writing on the folded sheet, dollar or percent signs, numbers.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **HALF CASH / HALF STOCK**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G008 / Beat B014

**РЕЖИССУРА R6:**  
Изменено после теста: чекбоксы превратились в чек-лист с галочками, а штаб-квартира пропала. Теперь главное — отпечаток штаб-квартиры Adobe, а условия показаны тремя чистыми карточками без единой отметки. Сделка подписана, условия ещё не выполнены.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV004_ADOBE_HQ_SAN_JOSE.jpg` — REAL-PHOTO / RV004

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe headquarters, San Jose; it is the print, shown unchanged. No other photo, document or logo may appear.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a large photographic print of a corporate headquarters at dusk stands on a dark desk. In front of it, three identical blank ivory index cards lie in a neat row, face up, the first one with a thin deep-red top edge.

Composition: headline zone inside the top 40% and left 38% of the frame. The print fills the right 60%, between 8% and 70% of frame height; the cards lie in front of its lower edge, above 78%. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: check marks, checklists, timelines, nodes, icons, stamps, gavels.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **CLOSING CONDITIONS**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G009 / Beat B015

**РЕЖИССУРА R6:**  
Постановка подтвердилась: две глубины. Позади размытый кроп пресс-релиза, впереди резкий кроп Section 8.2. Закреплено только то, что оба документа берутся из вложений и что их ровно два.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV047_ANNOUNCEMENT_HEADLINE_CROP.png` — DOCUMENT / RV047
2. `12_SOURCE_PREP/RV049_S8_2_TERMINATION_FEE_CROP.png` — DOCUMENT / RV049

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe acquisition announcement headline (blurred background page); image 2 = Merger Agreement Section 8.2 fee excerpt (sharp front excerpt). Both unchanged — never retype either.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: behind, a large announcement page lies softly out of focus on a dark desk; in front, a smaller contract excerpt is tack-sharp, overlapping the background page's lower-left corner, a thin vertical deep-red bracket in its margin.

Composition: headline zone inside the top 40% and left 40% of the frame. The blurred page spans the center-right; the sharp excerpt at mid-height, center; both end above 78% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: generated numbers or dollar signs, cash, arrows.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **THE OTHER NUMBER**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G010 / Beat B017

**РЕЖИССУРА R6:**  
Изменено после теста: вместо одного фото вышла подборка с логотипами и сценой. Первая строка теперь гласит «ровно одна фотография». Архивный отпечаток основателей на стене, одна булавка, свободно висящая красная нить, которая ни к чему не ведёт.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV013_FIGMA_FOUNDERS_ARCHIVAL.jpg` — REAL-PHOTO / RV013

**R4 SOURCE ROLE / PLACEMENT:** image 1 = archival Figma founders office photo; it is the print, unchanged — keep every face and person exactly as photographed; add no people.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: one old, slightly faded photographic print with a curled corner hangs alone on a dark wall, fixed by a single brass pin. From the pin a short deep-red thread hangs loose and ends in empty air, attached to nothing.

Composition: headline zone inside the top 45% and left 40% of the frame. The print on the right half, between 10% and 70% of frame height, slightly tilted; the loose thread ends above 78%. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: additional photos, company logos, stages, timelines, dates.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **BEFORE 2022**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G011 / Beat B018

**РЕЖИССУРА R6:**  
Изменено: заголовок перенесён влево вверх, чтобы модель не перевернула композицию. Вид сверху: две карточки-идентификатора, между ними красная нить с узлом («связь восстановлена»), рядом закрытая папка, перевязанная красной тесьмой.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV065_ADOBE_IDENTIFIER.png` — CONTEXT / RV065
2. `12_SOURCE_PREP/RV066_FIGMA_IDENTIFIER.png` — CONTEXT / RV066

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe identifier; image 2 = Figma identifier — each on its own card, unchanged, never broken or redrawn.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: top-down view of a dark desk. Two small paper cards, each carrying one company identifier, lie a short distance apart, joined by a deep-red thread with one neat knot in the middle. To the right lies a closed plain manila folder tied shut with red string.

Composition: headline zone inside the top 40% and left 40% of the frame. Cards and thread center, folder right, all between 30% and 76% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: folder labels, numbers, broken or shattered logos, handshakes, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **TALKS RESTART**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G012 / Beat B019

**РЕЖИССУРА R6:**  
Портрет CEO Adobe справа, запечатанный пустой конверт на красной нити слева по центру: «затем пришла цена». В первой строке прямо сказано: одна сцена, без панелей (в первом тесте на этом месте была раскадровка).

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV001_NARAYEN_PORTRAIT.jpg` — REAL-PHOTO / RV001

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe CEO portrait; it is the print, unchanged — keep the face exactly as photographed; add no people.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: on a dark desk, one portrait photograph printed on warm paper lies on the right; in the left-center a single sealed blank ivory envelope bound with a thin deep-red string rests in soft light.

Composition: headline zone inside the top 40% and left 42% of the frame; the envelope below it, between 45% and 72% of frame height. The portrait fills the right half, between 10% and 72%. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: writing on the envelope, numbers, cash, logos, other people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **THEN CAME THE PRICE**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G013 / Beat B021

**РЕЖИССУРА R6:**  
Кадр без вложений: чистый лист с пустым держателем для закладки. Место под комиссию есть, самой комиссии ещё нет. Пустота держателя описана как главный предмет кадра.

**GENERATION MODE:** BACKPLATE_ONLY + EDITOR_HEADLINE

**SOURCE INSERTS:**  
None. This is a source-free illustrative backplate.

**R4 SOURCE ROLE / PLACEMENT:** none — the frame contains no documents, photos, screenshots or logos.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-FREE illustrative backplate. Generate the physical metaphor/props only; do not add readable text, logos, UI or pseudo-document content.

Physical scene geometry: one clean blank ivory sheet lies on a dark desk. Clipped to its right edge is a clear index-tab holder with a thin deep-red rim, visibly empty — nothing is inside it.

Composition: headline zone inside the top 45% and left 40% of the frame. The sheet center-right, between 20% and 74% of frame height, with generous dark space around. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: writing on the sheet, numbers, dollar signs, people, gavels, government imagery.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **NO FEE YET**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- No authentic source insert is required for this frame.
- Add only the locked headline + short deep-red underline in the editor.

## G014 / Beat B024

**РЕЖИССУРА R6:**  
Рифма с G013: закладка появилась. Портрет CEO Figma справа, к его левому краю прищеплена красная закладка, рядом маленькая карточка Adobe. Figma добилась защиты.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV012_FIELD_PORTRAIT.jpg` — REAL-PHOTO / RV012
2. `12_SOURCE_PREP/RV065_ADOBE_IDENTIFIER.png` — CONTEXT / RV065

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Figma CEO portrait (the print) — keep the face exactly as photographed, add no people; image 2 = Adobe identifier (on the small card), unchanged.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: on a dark desk, a portrait photograph printed on warm paper lies on the right; one solid deep-red blank index tab is clipped to its left edge. A small paper card with a company identifier sits left-center, the red tab reaching toward it.

Composition: headline zone inside the top 40% and left 42% of the frame; the identifier card below it, between 48% and 72% of frame height. The portrait fills the right half, between 10% and 72%. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: writing on the tab, numbers, money, courts, gavels.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **THE FEE ENTERS THE DEAL**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G015 / Beat B026

**РЕЖИССУРА R6:**  
Штаб-квартира Adobe крупно справа, на переднем плане на краю бланка лежит закрытая перьевая ручка. Согласие без драмы.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV004_ADOBE_HQ_SAN_JOSE.jpg` — REAL-PHOTO / RV004

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe headquarters, San Jose; it is the print, shown unchanged. No other photo or logo may appear.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a wide photograph of a corporate headquarters under muted dusk light stands as a large print; in front of it, a closed black fountain pen rests across the edge of a blank contract page.

Composition: headline zone inside the top 45% and left 36% of the frame. The print fills the right 64%, between 8% and 70% of frame height; pen and page in front of its lower edge, above 78%. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: signatures, writing on the page, handshakes, people, cash.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **ADOBE AGREES**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G016 / Beat B027

**РЕЖИССУРА R6:**  
Макро на торец толстой пачки бумаги: один лист, кроп 10-Q, выдвинут из середины. Стоимость давно лежит внутри документов.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV053_10Q_CLOSING_RISK_CROP.png` — DOCUMENT / RV053

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe 10-Q closing-risk disclosure excerpt; it is the pulled sheet, shown unchanged — never retype it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a low-angle close view of a thick stack of blank paper on a dark desk; one sheet is pulled a few centimeters out of the middle of the stack, lit by a narrow beam, a thin vertical deep-red bracket in its margin.

Composition: headline zone inside the top 40% and left 42% of the frame. The stack spans center-right between 30% and 76% of frame height; the pulled sheet is the sharpest element. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: writing on other sheets, numbers, money, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **THE COST WAS ALREADY THERE**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G017 / Beat B028

**РЕЖИССУРА R6:**  
Вид сверху: стол разделён тонкой линией, по обе стороны карточки компаний. Красный бумажный брусок риска лежит на стороне покупателя. Распределение, а не наказание.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV065_ADOBE_IDENTIFIER.png` — CONTEXT / RV065
2. `12_SOURCE_PREP/RV066_FIGMA_IDENTIFIER.png` — CONTEXT / RV066

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe identifier (left card); image 2 = Figma identifier (right card). Both unchanged and small.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a dark desk divided by one thin pale line. Left of the line, a small paper card with a company identifier; right of the line, another card with the second identifier. A solid deep-red paper block rests on the left side, next to the left card.

Composition: headline zone inside the top 25% of the frame, left half. The two sides fill the band between 32% and 76% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: scales of justice, gavels, government imagery, money, arrows, writing on the block.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **RISK ALLOCATION**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G018 / Beat B029

**РЕЖИССУРА R6:**  
Изменено по уроку G003: развилка снята как настоящие предметы на пробковой доске, а не графикой. Одна нить раздваивается у булавки: серая идёт к пустой карточке, красная к сплошной красной карточке.

**GENERATION MODE:** BACKPLATE_ONLY + EDITOR_HEADLINE

**SOURCE INSERTS:**  
None. This is a source-free illustrative backplate.

**R4 SOURCE ROLE / PLACEMENT:** none — the frame contains no documents, photos, screenshots or logos.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-FREE illustrative backplate. Generate the physical metaphor/props only; do not add readable text, logos, UI or pseudo-document content.

Physical scene geometry: one thread enters from the left and meets a brass pin, where it splits: an upper pale-grey thread runs to an empty outlined ivory card; a lower deep-red thread runs to a solid deep-red card. Nothing is written anywhere.

Composition: headline zone inside the top 25% of the frame, left half. Fork point center-left at 50% of frame height; both cards on the right half, the lower card ending above 78%. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: labels, icons, numbers, printed flowcharts, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **IF CLOSING FAILS**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- No authentic source insert is required for this frame.
- Add only the locked headline + short deep-red underline in the editor.

## G019 / Beat B031

**РЕЖИССУРА R6:**  
Изменено: заголовок перенесён влево вверх. Отличие от B030 (тот же договор) даёт экстремальное макро: резкая только полоса с нужной фразой, края листа растворяются.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV049_NOT_A_PENALTY_CROP.png` — DOCUMENT / RV049

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Merger Agreement Section 8.2 "not a penalty" excerpt; it is the paper, shown unchanged — never retype or redraw it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: an extreme close-up of one contract excerpt on warm aged paper with very shallow depth of field — a sharp band across the middle lines, paper edges melting into blur — and a thin vertical deep-red bracket in the margin beside the sharp band.

Composition: headline zone inside the top 40% and left 40% of the frame. The excerpt fills the right 60%, between 8% and 76% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: underlining inside the document, gavels, courts, scales, money.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **NOT A PENALTY**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G020 / Beat B032

**РЕЖИССУРА R6:**  
Без вложений: открытая бухгалтерская книга с чистыми строками. Одна строка залита отмеренным красным бруском, рядом лежит латунная линейка без делений. Сумма, согласованная заранее.

**GENERATION MODE:** BACKPLATE_ONLY + EDITOR_HEADLINE

**SOURCE INSERTS:**  
None. This is a source-free illustrative backplate.

**R4 SOURCE ROLE / PLACEMENT:** none — the frame contains no documents, photos, screenshots or logos.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-FREE illustrative backplate. Generate the physical metaphor/props only; do not add readable text, logos, UI or pseudo-document content.

Physical scene geometry: an open ledger book on a dark desk, pages blank with faint grey ruled lines. On one line a solid deep-red bar fills a precise measured length; an unmarked brass straightedge lies parallel to it.

Composition: headline zone inside the top 40% and left 40% of the frame. The ledger center-right at a gentle angle, between 25% and 76% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: numbers, ruler markings, currency symbols, cash, gavels, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **LIQUIDATED DAMAGES**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- No authentic source insert is required for this frame.
- Add only the locked headline + short deep-red underline in the editor.

## G021 / Beat B033

**РЕЖИССУРА R6:**  
К углу кропа 8-K через пробитое отверстие привязана пустая бирка-ценник на красной нити. У провала была цена.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV048_8K_MERGER_AGREEMENT_CROP.png` — DOCUMENT / RV048

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe Form 8-K merger-agreement excerpt; it is the paper, shown unchanged — never retype it. No other document may appear.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: one paper excerpt lies on a dark desk; through a punched hole in its lower-left corner a thin deep-red string is tied to a blank manila price tag resting beside it.

Composition: headline zone inside the top 45% and left 40% of the frame. The excerpt on the right half, between 10% and 70% of frame height; the tag near the center, above 78%. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: writing or numbers on the tag, currency, cash, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **FAILURE HAD A PRICE**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G022 / Beat B035

**РЕЖИССУРА R6:**  
Официальная графика сделки висит в раме на стене под одним прожектором, одна красная булавка над рамой. Кадр отмечает день.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV025_ADOBE_FIGMA_DEAL_GRAPHIC.png` — PRODUCT-UI / RV025

**R4 SOURCE ROLE / PLACEMENT:** image 1 = official Adobe + Figma deal graphic; it is the framed print, unchanged — never redraw its logos.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a framed print hangs alone on a dark wall under a single spotlight; one deep-red pin is pushed into the wall just above the frame's top center.

Composition: headline zone inside the top 40% and left 42% of the frame. The framed print center-right, between 12% and 72% of frame height, with wide darkness around. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: calendars, extra numbers, people, cash.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **SEPTEMBER 15, 2022**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G023 / Beat B036

**РЕЖИССУРА R6:**  
Масштаб: широкий отпечаток сцены Adobe MAX, к правому краю прищеплена маленькая карточка Figma. Лица на фото не трогаем.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV009_NARAYEN_MAX_2022_STAGE.jpg` — REAL-PHOTO / RV009
2. `12_SOURCE_PREP/RV066_FIGMA_IDENTIFIER.png` — CONTEXT / RV066

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe MAX 2022 keynote stage (the print) — keep every face and person exactly as photographed, add no people; image 2 = Figma identifier (small card), unchanged.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a wide event photograph of a keynote stage and audience is presented as a large print covering most of the frame; a small paper card with a company identifier is clipped to the print's right edge.

Composition: headline zone inside the top 35% and left 40% of the frame, over dark shadow. The print spans from 30% to the right edge, between 18% and 74% of frame height; card at right-middle. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: invented stage screens or slogans, money, extra logos.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **A GIANT SOFTWARE DEAL**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G024 / Beat B037

**РЕЖИССУРА R6:**  
Нарочито обычный кадр: небольшой отпечаток толпы на Config и аккуратная закрытая папка на прибранном столе. Красный только под заголовком.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV016_CONFIG_2023_CROWD.jpg` — REAL-PHOTO / RV016

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Figma Config 2023 crowd; it is the print, unchanged — do not alter or add people.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a tidy dark desk; a medium photographic print of a conference crowd lies squarely on the right; beside it a neatly closed plain grey folder aligned parallel to the print.

Composition: headline zone inside the top 45% and left 40% of the frame. Folder and print center-right, between 25% and 74% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, calm and serious; the only red is the headline underline.

Avoid: folder labels, money, logos, warning signs.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **THE DEAL LOOKED NORMAL**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G025 / Beat B038

**РЕЖИССУРА R6:**  
Три предмета в ряд на стене: карточка Adobe, карточка Figma и пустая рамка, одобрения. Пустота рамки описана как предмет.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV065_ADOBE_IDENTIFIER.png` — CONTEXT / RV065
2. `12_SOURCE_PREP/RV066_FIGMA_IDENTIFIER.png` — CONTEXT / RV066

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe identifier (first card); image 2 = Figma identifier (second card). Both unchanged and small.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: on a dark wall, three items are pinned evenly spaced in a straight row: a small card with one company identifier, a small card with a second identifier, and an empty open paper frame — plain dark wall visible through it — with a thin deep-red top edge.

Composition: headline zone = top center, inside the top 22% of the frame. The row sits between 34% and 72% of frame height, left to right. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: labels under items, government buildings, flags, gavels.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **BUYER • TARGET • APPROVALS**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G026 / Beat B039

**РЕЖИССУРА R6:**  
Отпечаток графики сделки лежит на столе, его угол отогнут, а под ним виден кроп Section 8.2. Механизм лежит под заголовком.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV025_ADOBE_FIGMA_DEAL_GRAPHIC.png` — PRODUCT-UI / RV025
2. `12_SOURCE_PREP/RV049_S8_2_TERMINATION_FEE_CROP.png` — DOCUMENT / RV049

**R4 SOURCE ROLE / PLACEMENT:** image 1 = official Adobe + Figma deal graphic (top print), unchanged; image 2 = Merger Agreement Section 8.2 fee excerpt (revealed underneath), unchanged — never retype it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a print lies flat on a dark desk; its lower-right corner is physically peeled back and curled up, revealing a contract excerpt underneath, with a thin vertical deep-red bracket in the excerpt's margin.

Composition: headline zone inside the top 45% and left 40% of the frame. The print fills center-right between 10% and 74% of frame height; the revealed corner at right-middle. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: "secret" or "classified" cues, locks, money, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **THE HIDDEN FAILURE MECHANISM**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G027 / Beat B040

**РЕЖИССУРА R6:**  
Низкий ракурс на очень толстый договор, глубоко внутри торчит красная закладка. Сверху маленький кроп пресс-релиза: поверхность против глубины.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV047_ANNOUNCEMENT_HEADLINE_CROP.png` — DOCUMENT / RV047

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe acquisition announcement headline; it is the excerpt on top, unchanged — never retype it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a low-angle view of a very thick bound agreement on a dark desk, blank page edges facing camera; one deep-red tab sticks out from deep inside the stack near its bottom. A small crisp announcement excerpt lies on top of the stack.

Composition: headline zone inside the top 40% and left 40% of the frame. The stack spans center-right between 30% and 76% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: writing on page edges or the tab, money, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **DEEPER IN THE AGREEMENT**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G028 / Beat B041

**РЕЖИССУРА R6:**  
Бит 3 секунды. Отпечаток здания Еврокомиссии в холодных сумерках, одна красная булавка. Входят регуляторы.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV068_BERLAYMONT.jpg` — CONTEXT / RV068

**R4 SOURCE ROLE / PLACEMENT:** image 1 = European Commission Berlaymont headquarters; it is the print, unchanged.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a photographic print of a large institutional building at blue dusk is pinned to a dark wall with one deep-red pin at its top-left corner; cool, still, quiet.

Composition: headline zone inside the top 45% and left 40% of the frame. The print fills the right 60%, between 10% and 72% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light with a cool blue cast on the print, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: EU flags, stars, gavels, storm clouds, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **2023: THE RISK ARRIVES**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G029 / Beat B042

**РЕЖИССУРА R6:**  
Открывается британское расследование. Вид сверху: только что раскрытая папка, внутри кроп таймлайна дела CMA со скобкой на полях. Образ «папку открыли».

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV054_CMA_CASE_TIMELINE_CROP.png` — DOCUMENT / RV054

**R4 SOURCE ROLE / PLACEMENT:** image 1 = UK CMA case-page timeline excerpt; it is the excerpt in the folder, unchanged — never retype it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: top-down view of a manila case folder just opened flat on a dark desk; on its right-hand page lies one paper excerpt with a thin vertical deep-red bracket in its margin; the left-hand page is blank.

Composition: headline zone inside the top 45% and left 38% of the frame. The open folder center-right, between 18% and 76% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: folder labels, seals, Union Jack, gavels, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **UK REVIEW OPENS**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G030 / Beat B043

**РЕЖИССУРА R6:**  
Вид сбоку на архивный бокс: тонкая закрытая папка (фаза 1) с прикреплённым кропом и за ней толстая папка с красной закладкой (фаза 2).

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV055_CMA_PHASE1_DECISION_CROP.png` — DOCUMENT / RV055

**R4 SOURCE ROLE / PLACEMENT:** image 1 = UK CMA Phase 1 decision title block; it is the clipped excerpt, unchanged — never retype it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: side view of two case folders standing upright in an open cardboard archive box on a dark desk: the front folder thin and closed with one small paper excerpt clipped to its face; the folder behind noticeably thicker, one deep-red tab rising from it.

Composition: headline zone inside the top 40% and left 40% of the frame. The box center-right, between 28% and 76% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: labels, numbers, seals, flags, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **PHASE TWO**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G031 / Beat B044

**РЕЖИССУРА R6:**  
Смена масштаба: фасад Berlaymont во весь кадр, заголовок в тёмном небе сверху слева, низ уходит в тень.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV069_BERLAYMONT_ALT.jpg` — CONTEXT / RV069

**R4 SOURCE ROLE / PLACEMENT:** image 1 = European Commission Berlaymont exterior (alternate view); it is the photograph, unchanged — do not add or alter architecture or signs.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a wide, cinematic full-frame view of a large institutional office building, deep muted grading, darkened sky.

Composition: headline zone inside the top 35% and left 45% of the frame, over the dark sky. The building occupies the center and right. The bottom 22% falls into plain near-black shadow with no building detail. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black tones, subtle warm paper-grain texture overlay, low-key light, fine film grain, restrained deep-red accents, calm and serious.

Avoid: people, gavels, storm effects, extra text on the building.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **EU IN-DEPTH REVIEW**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G032 / Beat B046

**РЕЖИССУРА R6:**  
Два органа, два возражения. Кроп CMA слева, фото Еврокомиссии справа, у каждого маленький красный флажок. Между ними пустая стена: финального решения нет.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV055_CMA_PHASE1_DECISION_CROP.png` — DOCUMENT / RV055
2. `12_SOURCE_PREP/RV068_BERLAYMONT.jpg` — CONTEXT / RV068

**R4 SOURCE ROLE / PLACEMENT:** image 1 = UK CMA Phase 1 decision title block (left), unchanged — never retype it; image 2 = European Commission Berlaymont (right print), unchanged.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: on a dark wall, a paper excerpt (left) and a photographic print of an institutional building (right) are pinned at equal size; each has one small blank deep-red paper flag clipped to its top edge. The wall between them is plain and empty — a deliberate void.

Composition: headline zone = top center, inside the top 22% of the frame. The two items between 30% and 74% of frame height, in the left and right thirds. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: writing on flags, stamps, lines between items, national flags, gavels.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **FORMAL OBJECTIONS**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G033 / Beat B047

**РЕЖИССУРА R6:**  
Отпечаток здания DOJ в холодном свете. На переднем плане закрытая папка и рядом пустой проволочный лоток: иска нет. Пустота лотка — главный предмет кадра.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV070_DOJ_HQ.jpg` — CONTEXT / RV070

**R4 SOURCE ROLE / PLACEMENT:** image 1 = U.S. Department of Justice headquarters exterior; it is the print, unchanged — no seal close-ups.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a photographic print of a government headquarters leans upright on a dark desk in cool light; in front, one closed plain folder lies beside an empty black wire document tray with nothing in it.

Composition: headline zone inside the top 45% and left 38% of the frame. The print on the right half, between 8% and 66% of frame height; folder and empty tray in front of it, above 78%. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: papers in the tray, folder labels, seals, courtrooms, gavels, handcuffs, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **INVESTIGATION ≠ LAWSUIT**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G034 / Beat B048

**РЕЖИССУРА R6:**  
Слева кроп 8-K с перьевой ручкой поперёк (подписано). Справа за широкой пустотой отдельная карточка, очерченная лишь серым контуром (не закрыто).

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV048_8K_MERGER_AGREEMENT_CROP.png` — DOCUMENT / RV048

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe Form 8-K merger-agreement excerpt; it is the left excerpt, unchanged — never retype it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: on a dark desk, left: a paper excerpt with a closed black fountain pen resting across it. Right, across a wide empty gap: one blank card defined only by a thin pale-grey outline, untouched.

Composition: headline zone = top center, inside the top 22% of the frame. Excerpt with pen in the left 40%, outlined card in the right 30%, both between 30% and 74% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: signatures, stamps, arrows, locks, handshakes, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **SIGNED ≠ CLOSED**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G035 / Beat B049

**РЕЖИССУРА R6:**  
Резкий кроп Section 8.2 впереди. Сзади в сильном размытии растут стопки чистых бумаг. Пункт договора не меняется, давление растёт.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV049_S8_2_TERMINATION_FEE_CROP.png` — DOCUMENT / RV049

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Merger Agreement Section 8.2 fee excerpt; it is the sharp excerpt, unchanged — never retype it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a single contract excerpt lies tack-sharp on a dark desk, a thin vertical deep-red bracket in its margin; behind it, heavily out of focus, tall stacks of blank papers rise and crowd the background.

Composition: headline zone inside the top 40% and left 40% of the frame. The sharp excerpt center-right between 35% and 74% of frame height; blurred stacks behind it. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: text on the stacks, money, government buildings, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **THE CLAUSE DIDN'T CHANGE**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G036 / Beat B050

**РЕЖИССУРА R6:**  
Узкий коридор между двумя стенами из папок. В конце маленькая пустая светлая карточка (закрытие) далеко. Кроп 10-Q приколот на ближней стене.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV053_10Q_CLOSING_RISK_CROP.png` — DOCUMENT / RV053

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe 10-Q closing-risk excerpt; it is the pinned excerpt, unchanged — never retype it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a low, deep perspective down a narrow corridor formed by two tall dark walls of stacked file folders on a desk; at the far end a small blank pale card stands in faint light. One paper excerpt is pinned high on the near right wall.

Composition: headline zone inside the top 35% and left 40% of the frame. The corridor converges at center; the excerpt upper right, between 12% and 45% of frame height. The bottom 22% is dark shadow. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: folder labels, clocks, hourglasses, doors, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **FAILED CLOSING GETS CLOSER**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G037 / Beat B051

**РЕЖИССУРА R6:**  
Два органа сходятся в одном моменте. Отпечаток Еврокомиссии в сумерках и меньший кроп CMA приколоты к стене и соединены одной короткой красной нитью.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV068_BERLAYMONT.jpg` — CONTEXT / RV068
2. `12_SOURCE_PREP/RV054_CMA_CASE_TIMELINE_CROP.png` — DOCUMENT / RV054

**R4 SOURCE ROLE / PLACEMENT:** image 1 = European Commission Berlaymont (large print), unchanged; image 2 = UK CMA case-page timeline excerpt (small excerpt), unchanged — never retype it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: on a dark wall, a large photographic print of an institutional building at dusk (right) and a smaller paper excerpt (left-center) are pinned; one short taut deep-red thread joins a pin on each.

Composition: headline zone inside the top 35% and left 42% of the frame; the excerpt below it, between 42% and 72% of frame height. The large print on the right half, between 10% and 72%. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: calendars, flags, gavels, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **NOVEMBER 2023**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G038 / Beat B056

**РЕЖИССУРА R6:**  
Один лист с двумя прикреплёнными карточками компаний. По красной пунктирной линии между ними лист частично согнут: сделку, возможно, придётся перекроить.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV065_ADOBE_IDENTIFIER.png` — CONTEXT / RV065
2. `12_SOURCE_PREP/RV066_FIGMA_IDENTIFIER.png` — CONTEXT / RV066

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe identifier; image 2 = Figma identifier — each on its own card, unchanged and small.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: top-down view of one blank sheet on a dark desk with two small identifier cards paper-clipped to it, one on each half; a deep-red dashed fold line runs between them and the sheet is partly lifted along that line.

Composition: headline zone inside the top 45% and left 40% of the frame. The sheet center-right, between 22% and 76% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: scissors, tearing, broken logos, gavels, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **REMEDIES CHANGE THE DEAL**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G039 / Beat B057

**РЕЖИССУРА R6:**  
Буквально «на столе»: отпечаток скриншота Figma на тёмном столе переговоров. Рядом, не пересекая его, пунктир красным карандашом: возможное выделение.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV033_FIGMA_COLLAB_WORKFLOW_UI.png` — PRODUCT-UI / RV033

**R4 SOURCE ROLE / PLACEMENT:** image 1 = official Figma collaboration workflow product visual; it is the print, unchanged — never redraw or invent interface.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a long dark conference table at a low angle, empty chairs dissolving into shadow; a printed product screenshot lies on the table; beside it runs a faint deep-red dashed pencil line with a red pencil resting at its end.

Composition: headline zone inside the top 35% and left 42% of the frame. The print center-right, between 35% and 74% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: people, name plates, scissors, gavels, extra screens.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **FIGMA DESIGN ON THE TABLE**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G040 / Beat B058

**РЕЖИССУРА R6:**  
Стальная струбцина прижимает стопку бумаг, к лицевой стороне прикреплён кроп предварительных выводов CMA. Справа нетронутый чистый лист, до которого струбцина не достаёт.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV056_CMA_PROVISIONAL_FINDINGS_CROP.png` — DOCUMENT / RV056

**R4 SOURCE ROLE / PLACEMENT:** image 1 = UK CMA provisional-findings excerpt; it is the excerpt on the stack, unchanged — never retype it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: on a dark desk, a heavy black steel clamp presses down on a short stack of paper; one paper excerpt is fixed to the front of the stack. To the right a single clean blank sheet lies untouched in soft light.

Composition: headline zone inside the top 40% and left 38% of the frame. Clamp and stack at center, blank sheet center-right, all between 30% and 76% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: writing on the blank sheet, stamps, gavels, government buildings, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **PRESSURE, NOT FINALITY**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G041 / Beat B060

**РЕЖИССУРА R6:**  
Компании возражают. Отпечаток сцены Adobe MAX справа, меньший портрет CEO Figma слева, между ними толстая переплетённая пачка ответа с чистой обложкой. Лица не трогаем.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV009_NARAYEN_MAX_2022_STAGE.jpg` — REAL-PHOTO / RV009
2. `12_SOURCE_PREP/RV012_FIELD_PORTRAIT.jpg` — REAL-PHOTO / RV012

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe MAX 2022 keynote stage (large print); image 2 = Figma CEO portrait (small print). Both unchanged — keep every face and person exactly as photographed; add no people.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: on a dark desk, a large event-photograph print (right) and a smaller portrait print (left-center) lie apart; between them rests a thick bound submission with a plain blank cover.

Composition: headline zone inside the top 35% and left 42% of the frame; the portrait print below it, between 40% and 74% of frame height. The large print on the right half, between 10% and 72%. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: cover titles, fists, courtroom imagery, extra logos.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **ADOBE + FIGMA PUSH BACK**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G042 / Beat B062

**РЕЖИССУРА R6:**  
Открытый скоросшиватель: на ранних листах кроп таймлайна CMA, последний раздел открыт на совершенно чистой странице. Решения по существу нет.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV054_CMA_CASE_TIMELINE_CROP.png` — DOCUMENT / RV054

**R4 SOURCE ROLE / PLACEMENT:** image 1 = UK CMA case-page timeline excerpt; it is the excerpt, unchanged — never retype it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: an open ring binder on a dark desk; on its left side a paper excerpt sits on the earlier pages; the binder is opened at its last section — a divider with a deep-red edge followed by a completely blank white page.

Composition: headline zone inside the top 40% and left 38% of the frame. The binder center-right, between 24% and 76% of frame height; the blank page is the brightest area. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: divider labels, writing on the blank page, stamps, gavels, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **NO FINAL MERITS DECISION**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G043 / Beat B063

**РЕЖИССУРА R6:**  
Две открытые папки одинакового размера лежат симметрично, в них позиция CMA и ответ компаний. Между ними нейтральная линейка. Весов нет.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV056_CMA_PROVISIONAL_FINDINGS_CROP.png` — DOCUMENT / RV056
2. `12_SOURCE_PREP/RV058_PARTIES_RESPONSE_CROP.png` — DOCUMENT / RV058

**R4 SOURCE ROLE / PLACEMENT:** image 1 = UK CMA provisional-findings excerpt (left folder); image 2 = Adobe/Figma response excerpt (right folder). Both unchanged — never retype them.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: top-down view of two open manila folders of identical size lying side by side on a dark desk, a thin neutral grey unmarked ruler between them; each folder holds one paper excerpt.

Composition: headline zone = top center, inside the top 22% of the frame. The folders fill the band between 28% and 76% of frame height, symmetrically. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: scales of justice, versus signs, ruler markings, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **TWO SIDES OF THE RECORD**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G044 / Beat B064

**РЕЖИССУРА R6:**  
Изменено: заголовок перенесён влево вверх. Рядом с кропом о возможных средствах лежат три латунные заготовки ключей, одна перевязана красной нитью. Подбор решения.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV057_CMA_POSSIBLE_REMEDIES_CROP.png` — DOCUMENT / RV057

**R4 SOURCE ROLE / PLACEMENT:** image 1 = UK CMA Notice of Possible Remedies title excerpt; it is the paper, unchanged — never retype it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: on a dark desk, one paper excerpt lies at a slight angle; beside it three uncut, unengraved brass key blanks lie in a neat row, one tied with a thin deep-red thread.

Composition: headline zone inside the top 40% and left 40% of the frame. Excerpt and keys on the right 58%, between 22% and 76% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: locks, padlocks, engraved keys, gavels, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **WHAT REMEDY COULD WORK?**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G045 / Beat B066

**РЕЖИССУРА R6:**  
Позиция компаний, со ссылкой на них. Отпечаток штаб-квартиры Adobe частично накрыт чистым листом ответа с вертикальной красной полосой цитаты, к углу прикреплена карточка Figma.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV004_ADOBE_HQ_SAN_JOSE.jpg` — REAL-PHOTO / RV004
2. `12_SOURCE_PREP/RV066_FIGMA_IDENTIFIER.png` — CONTEXT / RV066

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe headquarters, San Jose (the print), unchanged; image 2 = Figma identifier (small card), unchanged.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: on a dark desk, a photographic print of a corporate headquarters lies partly covered by a single blank response sheet; a solid vertical deep-red quote bar runs along the sheet's left edge; a small identifier card is clipped to the sheet's top corner.

Composition: headline zone inside the top 40% and left 40% of the frame. Print and sheet center-right, between 18% and 76% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: quotation text, writing on the sheet, gavels, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **THE COMPANIES' CHARACTERIZATION**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G046 / Beat B067

**РЕЖИССУРА R6:**  
Здание Berlaymont ночью во весь кадр, окна горят: процесс ещё открыт. Простота намеренная.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV069_BERLAYMONT_ALT.jpg` — CONTEXT / RV069

**R4 SOURCE ROLE / PLACEMENT:** image 1 = European Commission Berlaymont exterior (alternate view); it is the photograph, unchanged — do not add signs or alter the building.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a large institutional office building at night with some windows lit, full-frame, deep muted grading.

Composition: headline zone inside the top 35% and left 45% of the frame, over dark sky. The building fills center and right. The bottom 22% falls into plain near-black shadow with no detail. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black tones, subtle warm paper-grain texture overlay, low-key light, fine film grain, restrained deep-red accents, calm and serious.

Avoid: EU flags, stars, stamps, people, gavels.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **NO FINAL PROHIBITION**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G047 / Beat B068

**РЕЖИССУРА R6:**  
Взгляд через узкую щель между двумя шкафами для документов. В глубине на свету выцветший отпечаток графики сделки. Вопрос, а не ответ.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV025_ADOBE_FIGMA_DEAL_GRAPHIC.png` — PRODUCT-UI / RV025

**R4 SOURCE ROLE / PLACEMENT:** image 1 = official Adobe + Figma deal graphic; it is the faded print, unchanged apart from muted color — never redraw logos.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a view through a narrow vertical gap between two dark filing cabinets; in the lit space beyond, a faded print stands on a desk, visible but hard to reach.

Composition: headline zone inside the top 35% and left 40% of the frame, over the dark cabinet side. The gap slightly right of center; the print inside it between 30% and 70% of frame height. The bottom 22% is dark cabinet shadow. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: cabinet labels, doors, locks, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **COULD THIS STILL CLOSE?**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G048 / Beat B070

**РЕЖИССУРА R6:**  
Классическая документальная подача: кроп 8-K о прекращении справа, скобка у обоснования. Прямая речь компаний.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV061_8K_TERMINATION_CROP.png` — DOCUMENT / RV061

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe Form 8-K termination excerpt; it is the paper, unchanged — never retype, redraw or extend it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: one paper excerpt on warm aged paper lies slightly angled on a dark desk, held by a black binder clip, a thin vertical deep-red bracket in its margin beside the text.

Composition: headline zone inside the top 45% and left 40% of the frame. The excerpt fills the right 55%, between 10% and 75% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: underlining inside the document, stamps, gavels, government buildings.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **NO CLEAR PATH**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G049 / Beat B071

**РЕЖИССУРА R6:**  
Отпечаток здания Еврокомиссии, перед ним открытая пустая папка расследования. Внутри ничего не проштамповано.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV068_BERLAYMONT.jpg` — CONTEXT / RV068

**R4 SOURCE ROLE / PLACEMENT:** image 1 = European Commission Berlaymont; it is the print, unchanged.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a photographic print of an institutional building stands upright on a dark desk; in front of it lies an open plain review folder with blank pages and nothing inside.

Composition: headline zone inside the top 45% and left 38% of the frame. The print on the right half, between 8% and 64% of frame height; the open folder in front, above 78%. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: stamps, seals, writing on pages, flags, gavels, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **NOT A FINAL PROHIBITION**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G050 / Beat B072

**РЕЖИССУРА R6:**  
Вид сверху: две карточки компаний, красная нить между ними аккуратно перерезана, концы лежат ровно на чистом листе. Взаимно, спокойно.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV065_ADOBE_IDENTIFIER.png` — CONTEXT / RV065
2. `12_SOURCE_PREP/RV066_FIGMA_IDENTIFIER.png` — CONTEXT / RV066

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe identifier; image 2 = Figma identifier — each on its own card, unchanged, never broken.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: top-down view of a dark desk: two small identifier cards far apart, joined by a deep-red thread that has been cleanly cut in the middle; the two cut ends lie neatly side by side on one blank sheet placed between the cards.

Composition: headline zone inside the top 30% of the frame, left half. Cards, thread and sheet between 36% and 74% of frame height, left to right. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: scissors, cracks, broken logos, fire, writing on the sheet, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **MUTUAL TERMINATION**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G051 / Beat B073

**РЕЖИССУРА R6:**  
Две закрытые папки, перевязанные серой тесьмой, уложены в архивный бокс, к верхней прикреплён кроп CMA. Серый тон: процедура закрыта, вердикта нет.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV054_CMA_CASE_TIMELINE_CROP.png` — DOCUMENT / RV054

**R4 SOURCE ROLE / PLACEMENT:** image 1 = UK CMA case-page timeline excerpt; it is the clipped excerpt, unchanged — never retype it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: two closed case folders tied with plain grey tape lie stacked inside an open cardboard archive box on a dark desk, seen from a high angle; one paper excerpt is clipped to the top folder.

Composition: headline zone inside the top 45% and left 38% of the frame. The box center-right, between 20% and 76% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, calm and serious; red only in the headline underline.

Avoid: box labels, stamps, verdict imagery, gavels, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **REVIEWS END**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G052 / Beat B074

**РЕЖИССУРА R6:**  
Изменено: заголовок перенесён влево вверх. Главное — кроп заявления DOJ, крупно справа со скобкой. Небольшой отпечаток здания DOJ подложен под его угол.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV060_DOJ_STATEMENT_CROP.png` — DOCUMENT / RV060
2. `12_SOURCE_PREP/RV070_DOJ_HQ.jpg` — CONTEXT / RV070

**R4 SOURCE ROLE / PLACEMENT:** image 1 = DOJ Antitrust Division statement excerpt (main), unchanged — never retype it; image 2 = U.S. Department of Justice headquarters (small print), unchanged.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: on a dark desk a paper excerpt lies large and sharp with a thin vertical deep-red bracket in its margin; a small photographic print of a government building sits partly tucked under its upper-right corner.

Composition: headline zone inside the top 45% and left 40% of the frame. The excerpt fills the right 55%, between 12% and 76% of frame height; the small print at its upper-right. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: seals, courtrooms, gavels, handcuffs, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **DOJ WELCOMES ABANDONMENT**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G053 / Beat B075

**РЕЖИССУРА R6:**  
Отпечаток здания DOJ в очень холодном свете, поверх него одна закрытая папка. Расследование закрыто без суда.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV070_DOJ_HQ.jpg` — CONTEXT / RV070

**R4 SOURCE ROLE / PLACEMENT:** image 1 = U.S. Department of Justice headquarters exterior; it is the print, unchanged — no seal close-ups.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a photographic print of a government headquarters lies flat on a dark desk in cold blue-grey light; one closed plain folder rests across its lower-right corner.

Composition: headline zone inside the top 45% and left 40% of the frame. Print and folder center-right, between 18% and 76% of frame height, generous darkness around. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light with a colder grade, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: folder labels, courtrooms, judges, gavels, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **INVESTIGATION, NO BLOCKING LAWSUIT**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G054 / Beat B076

**РЕЖИССУРА R6:**  
Штаб-квартира Adobe в сумерках во весь кадр, без предметов. Суда нигде нет. Пауза перед кульминацией.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV004_ADOBE_HQ_SAN_JOSE.jpg` — REAL-PHOTO / RV004

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe headquarters, San Jose; it is the photograph, unchanged — do not alter signs or architecture.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a wide cinematic full-frame view of a corporate headquarters at dusk, deep muted grading, still and quiet.

Composition: headline zone inside the top 40% and left 38% of the frame, over the darker left side. The buildings fill center and right. The bottom 22% falls into plain near-black shadow with no detail. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black tones, subtle warm paper-grain texture overlay, low-key light, fine film grain, restrained deep-red accents, calm and serious.

Avoid: courtrooms, judges, gavels, verdict imagery, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **NO COURTROOM LOSS**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G055 / Beat B077

**РЕЖИССУРА R6:**  
Кульминация, 3.4 секунды. Темнота, один луч света на кропе Section 8.2, яркая красная скобка на полях. Больше ничего.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV049_S8_2_TERMINATION_FEE_CROP.png` — DOCUMENT / RV049

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Merger Agreement Section 8.2 fee excerpt; it is the lit excerpt, unchanged — never retype it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: near-total darkness; a single narrow spotlight falls on one contract excerpt lying on a desk, a bright thin vertical deep-red bracket in its margin; everything else dissolves into black.

Composition: headline zone inside the top 40% and left 40% of the frame. The lit excerpt center-right, between 32% and 74% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, hard single-source light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: money, explosions, glow effects, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **THE CLAUSE BECOMES REAL**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G056 / Beat B078

**РЕЖИССУРА R6:**  
Верхний лист кропа Mutual Termination Agreement переворачивается, под ним чистая страница с красной закладкой. Что дальше.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV062_TERMINATION_AGREEMENT_CROP.png` — DOCUMENT / RV062

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Mutual Termination Agreement excerpt; it is printed on the turning top sheet, unchanged — never retype it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: top-down view of a small bound document on a dark desk; its top sheet is mid-turn, lifted and curving; beneath it the next page is blank with one deep-red tab at its edge.

Composition: headline zone inside the top 45% and left 38% of the frame. The document center-right, between 20% and 76% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: writing on the blank page, money, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **WHAT HAPPENS NEXT**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G057 / Beat B079

**РЕЖИССУРА R6:**  
Справа кроп 8-K о сроке платежа. Под заголовком три пустые карточки-ступени к сплошной красной. Отсчёт дней без цифр: цифры на карточках запрещены первой строкой.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV061_8K_TERMINATION_CROP.png` — DOCUMENT / RV061

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe Form 8-K termination excerpt (payment-timing passage); unchanged — never retype it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: on a dark desk, a paper excerpt lies on the right with a thin vertical deep-red bracket in its margin; on the left, three small blank ivory cards step upward in a row toward a fourth card of solid deep red.

Composition: headline zone inside the top 36% and left 42% of the frame; step cards below it, between 44% and 74% of frame height. The excerpt on the right half, between 10% and 74%. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: calendars, clocks, cash.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **DUE IN THREE BUSINESS DAYS**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G058 / Beat B080

**РЕЖИССУРА R6:**  
Рифма с G022. Отпечаток штаб-квартиры Adobe в холодном утреннем свете на стене, одна красная булавка. День платежа.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV004_ADOBE_HQ_SAN_JOSE.jpg` — REAL-PHOTO / RV004

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe headquarters, San Jose; it is the print, unchanged.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a photographic print of a corporate headquarters in cool early-morning light hangs on a dark wall; one deep-red pin is pushed in just above its top edge.

Composition: headline zone inside the top 40% and left 42% of the frame. The print center-right, between 12% and 72% of frame height, wide darkness around. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light with a cool morning cast on the print, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: calendars, extra numbers, cash, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **DECEMBER 20, 2023**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G059 / Beat B081

**РЕЖИССУРА R6:**  
Вид сверху: кроп 10-K Adobe слева, кроп S-1 Figma справа, их соединяет одна прямая красная линия. Симметрия бухгалтерской проводки.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV063_10K_PAYMENT_CROP.png` — DOCUMENT / RV063
2. `12_SOURCE_PREP/RV064_S1_FEE_RECEIPT_CROP.png` — DOCUMENT / RV064

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe FY2023 10-K payment excerpt (left); image 2 = Figma S-1 fee-receipt excerpt (right). Both unchanged — never retype them.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: top-down view of a dark desk; two paper excerpts lie far apart, left and right, joined by one straight thin deep-red line across the empty dark space between them.

Composition: headline zone = top center, inside the top 22% of the frame. Excerpts symmetric between 30% and 76% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: labels on the line, currency symbols, cash, logos.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **ADOBE PAYS • FIGMA RECEIVES**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G060 / Beat B082

**РЕЖИССУРА R6:**  
Ракурс сбоку вдоль стены: две карточки компаний далеко друг от друга, между ними натянутая красная нить уходит в перспективу. Настоящий перевод.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV065_ADOBE_IDENTIFIER.png` — CONTEXT / RV065
2. `12_SOURCE_PREP/RV066_FIGMA_IDENTIFIER.png` — CONTEXT / RV066

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe identifier (near card); image 2 = Figma identifier (far card). Both unchanged and small.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a dark wall seen at a raking side angle; two small identifier cards are pinned far apart along it, and one taut deep-red thread runs between them, receding in perspective.

Composition: headline zone inside the top 35% and left 42% of the frame. Near card center-left, far card toward the right edge; the thread crosses the band between 40% and 70% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: banknotes, coins, cash stacks, arrows, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **THE MONEY MOVED**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G061 / Beat B084

**РЕЖИССУРА R6:**  
Обесцвеченная графика сделки слева уходит в темноту. Кроп Section 8.2 справа тёплый и резкий. Сделка исчезает, комиссия остаётся.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV025_ADOBE_FIGMA_DEAL_GRAPHIC.png` — PRODUCT-UI / RV025
2. `12_SOURCE_PREP/RV049_S8_2_TERMINATION_FEE_CROP.png` — DOCUMENT / RV049

**R4 SOURCE ROLE / PLACEMENT:** image 1 = official Adobe + Figma deal graphic (fading print), unchanged apart from dim desaturated color; image 2 = Merger Agreement Section 8.2 fee excerpt (lit), unchanged — never retype it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: on a dark desk, a desaturated print on the left fades into shadow, barely visible; on the right, a contract excerpt is warm, sharp and lit, with a thin vertical deep-red bracket in its margin.

Composition: headline zone inside the top 32% of the frame, left 60%. The fading print left-center between 38% and 74% of frame height; the lit excerpt on the right, between 14% and 74%. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: fire, torn paper, regulator imagery, cash.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **THE DEAL DISAPPEARED. THE FEE DIDN'T.**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G062 / Beat B085

**РЕЖИССУРА R6:**  
Изменено: заголовок перенесён влево вверх. Макро на кроп Mutual Termination Agreement. Источник платежа — договор.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV062_TERMINATION_AGREEMENT_CROP.png` — DOCUMENT / RV062

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Mutual Termination Agreement excerpt (liquidated damages / sole remedy); it is the paper, unchanged — never retype or redraw it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: an extreme close-up of one contract excerpt on warm aged paper, very shallow depth of field, a sharp band across the key lines, a thin vertical deep-red bracket in the margin beside them.

Composition: headline zone inside the top 45% and left 40% of the frame. The excerpt fills the right 60%, between 8% and 76% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: underlining inside the document, government buildings, seals, gavels, cash.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **THE CONTRACT, NOT A REGULATOR**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G063 / Beat B087

**РЕЖИССУРА R6:**  
Выцветший отпечаток графики сделки один лежит на дне пустого архивного бокса. Покупка ушла в архив, так и не состоявшись.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV025_ADOBE_FIGMA_DEAL_GRAPHIC.png` — PRODUCT-UI / RV025

**R4 SOURCE ROLE / PLACEMENT:** image 1 = official Adobe + Figma deal graphic; it is the faded print, unchanged apart from muted desaturated color.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a high-angle view into an empty, clean cardboard archive box on a dark desk; a single faded print lies alone on its bottom.

Composition: headline zone inside the top 45% and left 38% of the frame. The box center-right, between 18% and 76% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: box labels, cancellation stamps, tearing, cash.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **THE PURCHASE NEVER HAPPENED**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G064 / Beat B088

**РЕЖИССУРА R6:**  
Кадр без вложений: одна тяжёлая чистая карточка с красным обрезом в жёстком свете отбрасывает плотную тень. Реальный весомый предмет.

**GENERATION MODE:** BACKPLATE_ONLY + EDITOR_HEADLINE

**SOURCE INSERTS:**  
None. This is a source-free illustrative backplate.

**R4 SOURCE ROLE / PLACEMENT:** none — the frame contains no documents, photos, screenshots or logos.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-FREE illustrative backplate. Generate the physical metaphor/props only; do not add readable text, logos, UI or pseudo-document content.

Physical scene geometry: one thick, heavy blank ivory card with a deep-red painted edge lies on a dark desk in hard directional light, casting a crisp solid shadow.

Composition: headline zone inside the top 45% and left 40% of the frame. The card center-right, between 30% and 72% of frame height, large, with generous darkness around. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: currency symbols, cash, coins, logos, people, documents.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **THE PAYMENT WAS REAL**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- No authentic source insert is required for this frame.
- Add only the locked headline + short deep-red underline in the editor.

## G065 / Beat B089

**РЕЖИССУРА R6:**  
Два отдельных листа бухгалтерской книги по диагонали: 10-K Adobe (расход) справа сверху, S-1 Figma (доход) слева ниже. Листы не соприкасаются.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV063_10K_PAYMENT_CROP.png` — DOCUMENT / RV063
2. `12_SOURCE_PREP/RV064_S1_FEE_RECEIPT_CROP.png` — DOCUMENT / RV064

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe FY2023 10-K payment excerpt (upper-right sheet); image 2 = Figma S-1 fee-receipt excerpt (lower-left sheet). Both unchanged — never retype them.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: two separate faint-ruled ledger sheets on a dark desk, offset diagonally — one upper-right, one lower-left — separated by a clear dark gap; each carries one paper excerpt.

Composition: headline zone inside the top 36% and left 40% of the frame. Upper-right sheet between 10% and 50% of frame height; lower-left sheet between 44% and 76%. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: numbers, plus/minus signs, calculators, cash.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **EXPENSE VS INCOME**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G066 / Beat B090

**РЕЖИССУРА R6:**  
Выцветший кроп пресс-релиза лежит далеко слева, тяжёлая карточка платежа далеко справа, между ними широкая пустота. Сложить их нельзя.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV047_ANNOUNCEMENT_HEADLINE_CROP.png` — DOCUMENT / RV047

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe acquisition announcement headline; it is the faded left excerpt, unchanged apart from muted color — never retype it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: on a wide dark desk, a faded paper excerpt lies at the far left; at the far right lies one heavy blank ivory card with a deep-red edge; the space between is completely empty.

Composition: headline zone = top center, inside the top 22% of the frame. The two objects in the outer thirds, between 32% and 74% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: plus signs, totals, numbers on the card, lines between objects, cash.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **PROPOSED ≠ PAID**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G067 / Beat B092

**РЕЖИССУРА R6:**  
Очень крупный заголовок в левой половине. Маленький кроп Section 8.2 одиноко лежит справа в тёмном пространстве. Центр истории.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV049_S8_2_TERMINATION_FEE_CROP.png` — DOCUMENT / RV049

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Merger Agreement Section 8.2 fee excerpt; unchanged — never retype it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a vast dark desk surface; one small contract excerpt lies alone on the right, softly lit, a thin vertical deep-red bracket in its margin.

Composition: headline zone = left half, between 12% and 60% of frame height, large. The small excerpt at right, between 36% and 64% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: dollar signs, cash, gold, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **THE BILLION-DOLLAR COST**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G068 / Beat B093

**РЕЖИССУРА R6:**  
Крупный отпечаток кейноута Config справа, за ним маленький выцветший отпечаток графики сделки. Независимость без триумфа. Лица не трогаем.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV015_CONFIG_2023_KEYNOTE.jpg` — REAL-PHOTO / RV015
2. `12_SOURCE_PREP/RV025_ADOBE_FIGMA_DEAL_GRAPHIC.png` — PRODUCT-UI / RV025

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Figma Config 2023 keynote stage (large print) — keep every face and person exactly as photographed, add no people; image 2 = official Adobe + Figma deal graphic (small faded print), unchanged apart from muted color.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a large event-photograph print stands on a dark desk, warmly lit; behind it and to one side a small faded print lies flat, half in shadow.

Composition: headline zone inside the top 45% and left 38% of the frame. The large print on the right half, between 8% and 72% of frame height; the small faded print partly visible behind its left edge. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: trophies, confetti, extra logos.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **FIGMA STAYS INDEPENDENT**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G069 / Beat B094

**РЕЖИССУРА R6:**  
Раскрытый толстый том отчётности, на правой странице кроп S-1 со скобкой. Платёж вошёл в историю компании.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV064_S1_FEE_RECEIPT_CROP.png` — DOCUMENT / RV064

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Figma S-1 fee-receipt excerpt; unchanged — never retype it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a thick bound filing volume lies open on a dark desk; on its right-hand page rests one paper excerpt with a thin vertical deep-red bracket in its margin; all other pages are blank.

Composition: headline zone inside the top 45% and left 38% of the frame. The open volume center-right, between 20% and 76% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: text on other pages, cash, logos, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **THE PAYMENT ENTERS FIGMA'S HISTORY**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G070 / Beat B095

**РЕЖИССУРА R6:**  
Фасад NYSE с баннером Figma во весь кадр, в правом верхнем углу небольшой кроп анонса S-1. Фактологично, без праздника.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV019_NYSE_FIGMA_BANNER.jpg` — REAL-PHOTO / RV019
2. `12_SOURCE_PREP/RV072_S1_ANNOUNCEMENT_CROP.png` — CONTEXT / RV072

**R4 SOURCE ROLE / PLACEMENT:** image 1 = NYSE facade with Figma banner (the photograph) — keep people exactly as photographed, add none; image 2 = Figma S-1 announcement headline block (small excerpt), unchanged.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a full-frame photograph of a stock-exchange facade with a large company banner, muted documentary grading; a small paper excerpt is clipped as a print in the upper-right corner.

Composition: headline zone inside the top 35% and left 42% of the frame, over the darker left side. The excerpt upper right, between 8% and 36% of frame height. The bottom 22% falls into plain dark shadow with no people or detail. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black tones, subtle warm paper-grain texture overlay, low-key light, fine film grain, restrained deep-red accents, calm and serious.

Avoid: confetti, fireworks, stock tickers, charts, added banner text.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **FIGMA GOES PUBLIC**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G071 / Beat B096

**РЕЖИССУРА R6:**  
Кроп анонса цены IPO крупно справа. Цифры есть только внутри кропа. Тихий документальный кадр после широкого G070.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV071_IPO_PRICING_CROP.png` — CONTEXT / RV071

**R4 SOURCE ROLE / PLACEMENT:** image 1 = official Figma IPO pricing announcement; unchanged — never retype, redraw or re-letter it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: one printed excerpt lies slightly angled on a dark desk, held by a black binder clip, a thin vertical deep-red bracket in its margin.

Composition: headline zone inside the top 45% and left 40% of the frame. The excerpt fills the right 55%, between 10% and 75% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: generated numbers, stock tickers, charts, cash.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **IPO SHARE SALE**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G072 / Beat B097

**РЕЖИССУРА R6:**  
Отпечаток уличной сцены у NYSE справа. Слева чистый разлинованный лист с одной красной строкой: место под точную сумму, которую наложат в монтаже.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV020_NYSE_FIGMA_STREET.jpg` — REAL-PHOTO / RV020

**R4 SOURCE ROLE / PLACEMENT:** image 1 = NYSE / Figma street scene; it is the print, unchanged — keep people exactly as photographed, add none.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: on a dark desk, a street-level event photograph lies as a print on the right; on the left, a blank faint-ruled ledger sheet with one line marked by a thin deep-red rule, nothing written on it.

Composition: headline zone inside the top 36% and left 42% of the frame; the ledger sheet below it, between 42% and 74% of frame height. The print on the right half, between 10% and 72%. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: numbers, currency, cash, charts.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **NET PROCEEDS**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G073 / Beat B098

**РЕЖИССУРА R6:**  
Отпечаток инсталляции Figma у NYSE слева, маленький кроп Section 8.2 справа. Серая нить между ними оборвана: причинной связи нет.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV021_FIGMA_COMMONS_NYSE.jpg` — REAL-PHOTO / RV021
2. `12_SOURCE_PREP/RV049_S8_2_TERMINATION_FEE_CROP.png` — DOCUMENT / RV049

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Figma Commons NYSE installation (print) — keep people exactly as photographed, add none; image 2 = Merger Agreement Section 8.2 fee excerpt (small), unchanged.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: on a dark wall, an event-photograph print (left) and a small contract excerpt (far right) are pinned apart; a pale-grey thread runs from each toward the other but is broken in the middle, leaving a clean empty gap.

Composition: headline zone = top center, inside the top 22% of the frame. Print on the left half, excerpt at right, both between 30% and 74% of frame height; the gap at center. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: arrows, question marks, charts, cash.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **LATER SUCCESS ≠ PROVEN CAUSE**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G074 / Beat B099

**РЕЖИССУРА R6:**  
Отпечаток билборда на Таймс-сквер справа, карточка платежа отдельно слева. Их ничто не соединяет.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV023_TIMES_SQUARE_BILLBOARD.jpg` — REAL-PHOTO / RV023

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Times Square billboard photo; it is the print, unchanged — add no text to the billboard.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: on a dark desk, a city-billboard photograph lies as a large print on the right; on the left one heavy blank ivory card with a deep-red edge lies apart; no line, thread or arrow links them.

Composition: headline zone inside the top 36% and left 42% of the frame; the card below it, between 46% and 72% of frame height. The print on the right half, between 10% and 72%. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: connecting lines, arrows, charts, cash, numbers on the card.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **NO PROVEN IPO CAUSATION**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G075 / Beat B100

**РЕЖИССУРА R6:**  
Ровно один портрет CEO Figma эпохи IPO на тёмной стене. Никаких символов Adobe. Лицо не трогаем.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV018_FIELD_IPO_ERA.jpg` — REAL-PHOTO / RV018

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Figma CEO, IPO-era portrait; it is the print, unchanged — keep the face exactly as photographed; add no people.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a single portrait photograph print hangs alone on a dark wall under soft light, nothing else around it.

Composition: headline zone inside the top 45% and left 40% of the frame. The portrait on the right half, between 10% and 72% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: extra prints, company logos, trophies, cash.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **ADOBE DID NOT ACQUIRE FIGMA**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G076 / Beat B101

**РЕЖИССУРА R6:**  
По уроку G003: настоящая пробковая доска. Две булавки, серая и красная, между ними простая нить без стрелки. Над красной булавкой приколото фото монтажа баннера у NYSE. Хронология без причинности.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV022_NYSE_BANNER_SETUP.jpg` — REAL-PHOTO / RV022

**R4 SOURCE ROLE / PLACEMENT:** image 1 = NYSE banner setup / scaffolding photo; it is the print, unchanged — keep people exactly as photographed, add none.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a dark cork board; two pins joined by a plain neutral thread with no arrowhead — a grey pin at left, a deep-red pin at right; above the right pin hangs one pinned photographic print.

Composition: headline zone inside the top 30% of the frame, left half. The thread at about 58% of frame height across the center; the print upper right, between 12% and 52%. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: dates, labels, arrowheads, charts, confetti.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **PUBLIC COMPANY**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G077 / Beat B102

**РЕЖИССУРА R6:**  
Вертикаль: графика сделки наверху (выгода), кроп Section 8.2 ниже со смещением вправо (риск). Возвращение к исходной архитектуре.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV025_ADOBE_FIGMA_DEAL_GRAPHIC.png` — PRODUCT-UI / RV025
2. `12_SOURCE_PREP/RV049_S8_2_TERMINATION_FEE_CROP.png` — DOCUMENT / RV049

**R4 SOURCE ROLE / PLACEMENT:** image 1 = official Adobe + Figma deal graphic (upper print), unchanged; image 2 = Merger Agreement Section 8.2 fee excerpt (lower), unchanged — never retype it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: on a dark desk, a print lies high in the frame; below it and offset to the right, a contract excerpt with a thin vertical deep-red bracket in its margin.

Composition: headline zone inside the top 45% and left 38% of the frame. The print center-right between 6% and 42% of frame height; the excerpt right, between 46% and 76%. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: arrows, charts, numbers, cash.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **UPSIDE / DOWNSIDE**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G078 / Beat B103

**РЕЖИССУРА R6:**  
Изменено: заголовок перенесён влево вверх. Кроп 5 июля лежит на тёмном столе переговоров рядом с закрытой ручкой. Риск получил цену за столом.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV051_JULY5_REVERSE_FEE_CROP.png` — DOCUMENT / RV051

**R4 SOURCE ROLE / PLACEMENT:** image 1 = 424B3 excerpt (July 5: reverse-fee proposal); unchanged — never retype it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: on a dark negotiating table one paper excerpt lies with a thin vertical deep-red bracket in its margin; a closed black fountain pen rests beside it; empty chairs dissolve into the dark background.

Composition: headline zone inside the top 45% and left 40% of the frame. Excerpt and pen on the right 58%, between 18% and 76% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: people, handshakes, price tags, numbers, cash.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **THE RISK WAS PRICED**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G079 / Beat B104

**РЕЖИССУРА R6:**  
Два кропа CMA внахлёст. Справа от них на столе чистый прямоугольный след: места под финальный приказ нет.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV056_CMA_PROVISIONAL_FINDINGS_CROP.png` — DOCUMENT / RV056
2. `12_SOURCE_PREP/RV057_CMA_POSSIBLE_REMEDIES_CROP.png` — DOCUMENT / RV057

**R4 SOURCE ROLE / PLACEMENT:** image 1 = UK CMA provisional-findings excerpt (front); image 2 = UK CMA possible-remedies excerpt (behind). Both unchanged — never retype them.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: on a dark desk two paper excerpts overlap slightly, one in front, one behind; to their right a faint clean rectangular outline on the desk marks an empty place — nothing lies inside it.

Composition: headline zone inside the top 45% and left 38% of the frame. The overlapping excerpts at center between 22% and 76% of frame height; the empty outline center-right. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: stamps, flags, gavels, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **REGULATORY PRESSURE BECOMES REAL**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G080 / Beat B105

**РЕЖИССУРА R6:**  
По уроку G003: настоящая пробковая доска, три коротких параллельных нити. В начале каждой маленький источник (CMA, Еврокомиссия, DOJ), и все нити обрываются, не дойдя до края.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV054_CMA_CASE_TIMELINE_CROP.png` — DOCUMENT / RV054
2. `12_SOURCE_PREP/RV068_BERLAYMONT.jpg` — CONTEXT / RV068
3. `12_SOURCE_PREP/RV070_DOJ_HQ.jpg` — CONTEXT / RV070

**R4 SOURCE ROLE / PLACEMENT:** image 1 = UK CMA case-page excerpt (top track); image 2 = European Commission Berlaymont (middle track); image 3 = U.S. Department of Justice headquarters (bottom track). All unchanged and small.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 3 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: three short parallel horizontal threads stacked one above another on a dark cork board; at the left start of each thread one small item is pinned; each thread stops well before the right edge, ending at an empty pin.

Composition: headline zone inside the top 24% of the frame, left half. The three tracks between 30% and 75% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: track labels, flags, map outlines, gavels.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **THREE FRONTS**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G081 / Beat B106

**РЕЖИССУРА R6:**  
Изменено: заголовок перенесён влево вверх. Эхо G048, но теснее: кроп 8-K крупнее и ближе. Документ узнаётся, но кадр не повторяется.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV061_8K_TERMINATION_CROP.png` — DOCUMENT / RV061

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe Form 8-K termination excerpt; unchanged — never retype, redraw or re-letter it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a tight close-up of one paper excerpt on warm aged paper, cropped closer than a full page, a thin vertical deep-red bracket in its margin, soft focus falloff at the edges.

Composition: headline zone inside the top 40% and left 38% of the frame. The excerpt fills the right 62%, between 6% and 76% of frame height. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: underlining inside the document, government buildings, gavels.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **NO CLEAR PATH**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G082 / Beat B107

**РЕЖИССУРА R6:**  
Настоящая пробковая доска: кроп соглашения о прекращении слева, кроп платежа в 10-K справа. Их соединяет красная нить с бумажным наконечником стрелки.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV062_TERMINATION_AGREEMENT_CROP.png` — DOCUMENT / RV062
2. `12_SOURCE_PREP/RV063_10K_PAYMENT_CROP.png` — DOCUMENT / RV063

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Mutual Termination Agreement excerpt (left); image 2 = Adobe FY2023 10-K payment excerpt (right). Both unchanged — never retype them.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: two paper excerpts pinned left and right on a dark cork board, joined by one taut deep-red thread ending in a small neat red paper arrowhead touching the right excerpt.

Composition: headline zone = top center, inside the top 22% of the frame. Excerpts between 30% and 76% of frame height, in the left and right thirds. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: labels, cash, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **TERMINATION → PAYMENT**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G083 / Beat B108

**РЕЖИССУРА R6:**  
Тройное отрицание столбцом в три строки слева, справа кроп «not a penalty». Только договор, никаких образов суда, регулятора или покупки.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV049_NOT_A_PENALTY_CROP.png` — DOCUMENT / RV049

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Merger Agreement Section 8.2 "not a penalty" excerpt; unchanged — never retype, redraw or re-letter it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 1 exact source insert. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: one contract excerpt on warm aged paper lies on a dark desk, held by a black binder clip, a thin vertical deep-red bracket in its margin.

Composition: headline zone = left 50%, between 10% and 70% of frame height. The excerpt fills the right 45%, between 10% and 74%. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: courtrooms, gavels, government buildings, cash.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **NOT A JUDGMENT • NOT A FINE • NOT A PURCHASE**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G084 / Beat B109

**РЕЖИССУРА R6:**  
Резкий кроп 20 июля впереди, размытое здание Еврокомиссии позади. Пункт договора впереди и во времени, и в кадре.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV052_JULY20_FEE_AGREED_CROP.png` — DOCUMENT / RV052
2. `12_SOURCE_PREP/RV068_BERLAYMONT.jpg` — CONTEXT / RV068

**R4 SOURCE ROLE / PLACEMENT:** image 1 = 424B3 excerpt (July 20: fee agreed), sharp, unchanged — never retype it; image 2 = European Commission Berlaymont, blurred background print, unchanged.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 2 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a paper excerpt lies tack-sharp in the foreground of a dark desk, a thin vertical deep-red bracket in its margin; behind it, heavily out of focus, stands a photographic print of an institutional building.

Composition: headline zone inside the top 35% and left 42% of the frame. The sharp excerpt left-center between 42% and 76% of frame height; the blurred print fills the right background. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: boxing gloves, fight imagery, gavels, flags, people.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **NEGOTIATED BEFORE THE FIGHT**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

## G085 / Beat B110

**РЕЖИССУРА R6:**  
Финальная секунда. Крупное название серии слева по центру, справа край кропа Section 8.2 и две крошечные карточки компаний. Рифма с G001.

**GENERATION MODE:** BACKPLATE_ONLY + EXACT_EDITOR_COMPOSITE

**SOURCE INSERTS:**  
1. `12_SOURCE_PREP/RV065_ADOBE_IDENTIFIER.png` — CONTEXT / RV065
2. `12_SOURCE_PREP/RV066_FIGMA_IDENTIFIER.png` — CONTEXT / RV066
3. `12_SOURCE_PREP/RV049_S8_2_TERMINATION_FEE_CROP.png` — DOCUMENT / RV049

**R4 SOURCE ROLE / PLACEMENT:** image 1 = Adobe identifier; image 2 = Figma identifier (the two tiny cards), unchanged; image 3 = Merger Agreement Section 8.2 fee excerpt (the paper edge), unchanged — never retype it.

**FINAL BACKPLATE PROMPT:**
```text
Single 16:9 finished WHAT IT COST documentary backplate. One photographed cinematic scene only — never a poster, thumbnail, collage, storyboard, split-screen or multi-panel graphic.

BACKPLATE ONLY. Generate no headline and no readable text anywhere. Generate no logos, UI, document text, dates, numbers, signatures, seals or source imagery. This is a SOURCE-BOUND backplate with 3 exact source inserts. Do not generate or imitate any listed source. Leave each intended source region clean and unobstructed for deterministic editor insertion.

Physical scene geometry: a deep charcoal field; at the right edge the edge of a contract excerpt on warm paper enters the frame, with two tiny identifier cards resting beside it.

Composition: headline zone = left of center, between 30% and 62% of frame height, large. Excerpt edge and cards at right, between 18% and 72%. The bottom 22% is empty dark charcoal. Any region intended for an editor-inserted source must remain clean, simple and unobstructed. Do not place props across those regions. Keep the bottom 22% visually calm for subtitles.

Source-relative decorations: do not generate brackets, highlights, tabs, clips or thread crossings that need to align to source pixels; those are added deterministically in the editor after source insertion.

Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.

Avoid: cash, gold, people, extra logos.. No pseudo-text, fake legal pages, invented UI, invented logos, generated faces, clickbait arrows, gavels, courts, Lady Justice, Capitol imagery, money piles, sensational poster styling.
```

**EDITOR COMPOSITE LOCK:**  
- Exact headline: **WHAT IT COST**
- Headline is editor-native only; do not regenerate the image to fix typography.
- Use the R4 layout above for headline placement and source geometry.
- Composite every listed `12_SOURCE_PREP/` file as exact source content; only crop/scale/perspective/mask are allowed.
- Add source border/frame/shadow and any source-relative red bracket/tab/clip/thread as editor-native elements.
- Never use generative fill inside a source rectangle.

