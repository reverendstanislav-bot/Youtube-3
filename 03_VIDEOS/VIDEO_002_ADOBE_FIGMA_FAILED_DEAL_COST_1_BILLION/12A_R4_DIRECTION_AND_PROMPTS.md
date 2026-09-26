# VIDEO 002 — Stage 12A-R4: Direction + Production Prompts (G001–G085)

Status: **PROMPTS WRITTEN / NO SPEND / NOT GENERATED**
Date: 2026-09-25
Supersedes: `12A_R3_DIRECTION_AND_PROMPTS.md` (kept as history).
Base: `12A_R2_HIGGSFIELD_PROMPTS.csv` (exact_text, beat and input files preserved).
Evidence for R4: `TEMP_GENERATED_QC_R3_TEST/G001–G010` (owner QC: 0 PASS / 5 EDIT_FIX / 5 REJECT; generated without source attachments).

## R4 changes vs R3 (all 85 prompts)
1. Headline position given as frame-percentage zones; almost all frames use headline top-left or top-center (fixes headline drifting low and layout flips — R3 test G002/G003/G004/G006).
2. The beat's single most dangerous failure is stated in the first line (fixes G007 banknotes, G008 ticks, G010 multiple images).
3. Deliberate emptiness is described as an object ("empty wall — a deliberate void") instead of only forbidden (fixes G006).
4. Pin/thread/timeline frames are specified as real photographed objects, not graphic diagrams (fixes G003).
5. Sources: only attached images may supply documents, photos, screenshots and logos; a style reference sets only the look.
6. Document emphasis = thin vertical red margin bracket, never underlining inside the document (fixes G001).
7. Headline line count and moderate size stated explicitly.

## Generation requirement
Each job must attach: R4 prompt + that slot's exact source files from `12_SOURCE_PREP/` (R2 `input_files`, as image 1/2/3 in that order) + optional style reference. Without source attachments the test is not valid.
Model/settings unchanged: Higgsfield GPT Image 2 · 1k · low · 16:9 · 0.5 credit. Generation authorized: 0 jobs.

## Часть 1 — G001–G028

**G001 / Beat B002**
РЕЖИССУРА:
Постановка из теста подтвердилась. Здесь закреплены только авторский кроп Section 8.2 и красная скобка на полях вместо подчёркивания. Договор крупно справа, заголовок слева сверху: это язык контракта, а не наказание.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one photographed scene, not a poster, thumbnail, collage or multi-panel layout. The only document in the frame is the attached one.
Scene: one contract page rests at a slight angle on a dark desk, held by a black binder clip at its top edge; a thin vertical deep-red bracket is drawn in its left margin, beside the text, never over it.
Layout: headline zone inside the top 45% and left 40% of the frame. The page fills the right 55%, between 10% and 75% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = Merger Agreement Section 8.2 termination-fee excerpt; it is the page itself, shown unchanged — never retype, redraw or extend its text. No other document, photo or logo may appear. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "NOT A FINE" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: underlining inside the document, courts, gavels, government buildings, cash.
```

**G002 / Beat B003**
РЕЖИССУРА:
Изменено после теста: модель перевернула композицию, поэтому кадр построен по стандартной схеме. Заголовок сверху слева, справа крупно официальная графика сделки в раме. Из-под рамы торчит угол пачки договора с одной красной закладкой: условие выхода за публичной сделкой.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one photographed scene, not a poster, thumbnail, collage or multi-panel layout. The only logos in the frame are the ones inside the attached image.
Scene: a framed print leans against a dark wall on a desk; beneath its lower edge the corner of a thick stack of blank contract paper protrudes, with one deep-red index tab sticking out.
Layout: headline zone inside the top 45% and left 40% of the frame. The framed print fills the right 55%, between 8% and 65% of frame height; the paper corner and red tab just below it, above 78%. The bottom 22% is empty dark charcoal.
Sources: image 1 = official Adobe + Figma deal graphic; it is the framed print, shown unchanged — never redraw or restyle its logos. No other logo, document or photo may appear. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "CONTRACTUAL EXIT COST" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: writing on the tab, boardrooms, handshakes, people, cash.
```

**G003 / Beat B004**
РЕЖИССУРА:
Изменено после теста: идея хронологии работает, но модель нарисовала графику. Теперь это прямо снятые предметы: пробковая доска, латунные булавки, натянутая красная нить. Заголовок стоит в верхней четверти и не выше нужного размера. Кроп 20 июля у первой булавки, дальше всё уходит в темноту.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — a real photographed cork board with physical brass pins and red thread, not a graphic timeline or diagram.
Scene: one taut deep-red thread runs horizontally across a dark cork board through exactly three brass pins. At the first pin (left) one small paper excerpt is pinned, sharp and lit; the second pin is in soft light; the third fades into darkness and blur. Nothing is written on the board.
Layout: headline zone inside the top 25% of the frame, left half. The thread at about 55% of frame height; the pinned excerpt just above the first pin. The bottom 22% is empty dark charcoal.
Sources: image 1 = 424B3 excerpt (July 20: fee agreed); it is the pinned paper, shown unchanged — never retype it. No other document may appear. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "NEGOTIATED BEFORE FAILURE" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: labels, dates or numbers on pins, arrows, printed timeline graphics.
```

**G004 / Beat B005**
РЕЖИССУРА:
Постановка из теста подтвердилась. Закреплены только заголовок сверху по центру и то, что оба фото берутся из вложений. Два отпечатка лежат порознь, между ними пустая бирка на красной нити к обоим: риск, который оценили вместе.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one photographed scene, not a poster, thumbnail, collage or multi-panel layout. The only photographs are the two attached ones.
Scene: top-down view of a dark desk; two photographic prints lie apart, the left slightly larger; between them sits one blank manila shipping tag whose thin deep-red string runs to a corner of each print.
Layout: headline zone = top center, inside the top 22% of the frame. Prints in the band between 28% and 76% of frame height, left and right; the tag at the exact center. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe headquarters, San Jose (left print); image 2 = Figma Config 2023 keynote stage (right print). Show both unchanged; keep every face and person exactly as photographed; add no people. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "PRICING THE RISK" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: writing on the tag, handshakes, money, government buildings.
```

**G005 / Beat B006**
РЕЖИССУРА:
Постановка подтвердилась. Модель нарисовала свою выписку с «$1,000,000,000», поэтому первая строка прямо говорит: никаких цифр, кроме тех, что во вложении. Один лист по диагонали в жёстком боковом свете, скрепка, скобка на полях.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one photographed scene. No numbers, dollar signs or money appear anywhere except inside the attached document.
Scene: top-down view of a single paper excerpt lying diagonally on a dark desk, caught in one hard beam of side light, a brass paperclip on its upper corner, a thin vertical deep-red bracket in its margin beside the text.
Layout: headline zone inside the top 45% and left 45% of the frame. The paper sits center-right, between 15% and 75% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe FY2023 10-K payment excerpt; it is the paper, shown unchanged — never retype, redraw or extend it. No other document may appear. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "THE RISK BECAME CASH" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: banknotes, cash stacks, coins, vaults, underlining inside the document.
```

**G006 / Beat B011**
РЕЖИССУРА:
Изменено после теста: модель «ответила» на вопрос диаграммой Венна и красной линией. Теперь в кадре ровно два планшета, а тёмная стена между ними описана как намеренная пустота. Заголовок-вопрос занимает только верхнюю полосу кадра.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — exactly two mounted screenshots on a wall and nothing between them; the empty wall between them is the point of the image.
Scene: two screenshots mounted on separate matte paper boards hang side by side on a dark wall, evenly lit, equal size. The wide space between them is plain, empty dark wall — a deliberate void with no line, shape, tag or symbol.
Layout: headline zone = top center, inside the top 20% of the frame. Boards in the band between 26% and 74% of frame height, one in the left third, one in the right third. The bottom 22% is empty dark charcoal.
Sources: image 1 = Figma Dev Mode product screenshot (left board); image 2 = Adobe XD documentation visual (right board). Show both unchanged — never redraw or invent interface. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "HOW DIRECTLY DID THEY COMPETE?" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: Venn diagrams, overlapping circles, connecting lines, arrows, versus signs, people.
```

**G007 / Beat B013**
РЕЖИССУРА:
Изменено после теста: модель подставила банкноты, сертификат и график. Запрет на деньги и ценные бумаги стоит в первой строке. Главный предмет — один согнутый пополам чистый лист, половины разного оттенка. Небольшой кроп 8-K прикреплён к углу.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — no money, banknotes, coins, stock certificates or charts appear anywhere; the whole idea is one blank folded sheet of paper.
Scene: one heavy blank sheet of paper folded exactly in half lies open on a dark desk: left half warm ivory, right half cool grey, a thin deep-red line along the fold. One small paper excerpt is paper-clipped to the sheet's upper-right corner.
Layout: headline zone inside the top 45% and left 40% of the frame. The folded sheet center-right, between 20% and 76% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe Form 8-K merger-agreement excerpt; it is the clipped excerpt, shown unchanged — never retype it. No other document may appear. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "HALF CASH / HALF STOCK" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: writing on the folded sheet, dollar or percent signs, numbers.
```

**G008 / Beat B014**
РЕЖИССУРА:
Изменено после теста: чекбоксы превратились в чек-лист с галочками, а штаб-квартира пропала. Теперь главное — отпечаток штаб-квартиры Adobe, а условия показаны тремя чистыми карточками без единой отметки. Сделка подписана, условия ещё не выполнены.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — the attached headquarters photograph is the main subject; three index cards in front of it are completely blank, with no marks, ticks or text.
Scene: a large photographic print of a corporate headquarters at dusk stands on a dark desk. In front of it, three identical blank ivory index cards lie in a neat row, face up, the first one with a thin deep-red top edge.
Layout: headline zone inside the top 40% and left 38% of the frame. The print fills the right 60%, between 8% and 70% of frame height; the cards lie in front of its lower edge, above 78%. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe headquarters, San Jose; it is the print, shown unchanged. No other photo, document or logo may appear. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "CLOSING CONDITIONS" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: check marks, checklists, timelines, nodes, icons, stamps, gavels.
```

**G009 / Beat B015**
РЕЖИССУРА:
Постановка подтвердилась: две глубины. Позади размытый кроп пресс-релиза, впереди резкий кроп Section 8.2. Закреплено только то, что оба документа берутся из вложений и что их ровно два.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — exactly two documents, both from the attachments, at two depths.
Scene: behind, a large announcement page lies softly out of focus on a dark desk; in front, a smaller contract excerpt is tack-sharp, overlapping the background page's lower-left corner, a thin vertical deep-red bracket in its margin.
Layout: headline zone inside the top 40% and left 40% of the frame. The blurred page spans the center-right; the sharp excerpt at mid-height, center; both end above 78% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe acquisition announcement headline (blurred background page); image 2 = Merger Agreement Section 8.2 fee excerpt (sharp front excerpt). Both unchanged — never retype either. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "THE OTHER NUMBER" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: generated numbers or dollar signs, cash, arrows.
```

**G010 / Beat B017**
РЕЖИССУРА:
Изменено после теста: вместо одного фото вышла подборка с логотипами и сценой. Первая строка теперь гласит «ровно одна фотография». Архивный отпечаток основателей на стене, одна булавка, свободно висящая красная нить, которая ни к чему не ведёт.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — exactly one photograph in the whole frame, and no logos at all.
Scene: one old, slightly faded photographic print with a curled corner hangs alone on a dark wall, fixed by a single brass pin. From the pin a short deep-red thread hangs loose and ends in empty air, attached to nothing.
Layout: headline zone inside the top 45% and left 40% of the frame. The print on the right half, between 10% and 70% of frame height, slightly tilted; the loose thread ends above 78%. The bottom 22% is empty dark charcoal.
Sources: image 1 = archival Figma founders office photo; it is the print, unchanged — keep every face and person exactly as photographed; add no people. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "BEFORE 2022" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: additional photos, company logos, stages, timelines, dates.
```

**G011 / Beat B018**
РЕЖИССУРА:
Изменено: заголовок перенесён влево вверх, чтобы модель не перевернула композицию. Вид сверху: две карточки-идентификатора, между ними красная нить с узлом («связь восстановлена»), рядом закрытая папка, перевязанная красной тесьмой.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one photographed desk scene; both logos appear only as the attached identifier images, small and intact.
Scene: top-down view of a dark desk. Two small paper cards, each carrying one company identifier, lie a short distance apart, joined by a deep-red thread with one neat knot in the middle. To the right lies a closed plain manila folder tied shut with red string.
Layout: headline zone inside the top 40% and left 40% of the frame. Cards and thread center, folder right, all between 30% and 76% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe identifier; image 2 = Figma identifier — each on its own card, unchanged, never broken or redrawn. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "TALKS RESTART" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: folder labels, numbers, broken or shattered logos, handshakes, people.
```

**G012 / Beat B019**
РЕЖИССУРА:
Портрет CEO Adobe справа, запечатанный пустой конверт на красной нити слева по центру: «затем пришла цена». В первой строке прямо сказано: одна сцена, без панелей (в первом тесте на этом месте была раскадровка).
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one scene only; never a storyboard, grid, sequence or multiple panels.
Scene: on a dark desk, one portrait photograph printed on warm paper lies on the right; in the left-center a single sealed blank ivory envelope bound with a thin deep-red string rests in soft light.
Layout: headline zone inside the top 40% and left 42% of the frame; the envelope below it, between 45% and 72% of frame height. The portrait fills the right half, between 10% and 72%. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe CEO portrait; it is the print, unchanged — keep the face exactly as photographed; add no people. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "THEN CAME THE PRICE" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: writing on the envelope, numbers, cash, logos, other people.
```

**G013 / Beat B021**
РЕЖИССУРА:
Кадр без вложений: чистый лист с пустым держателем для закладки. Место под комиссию есть, самой комиссии ещё нет. Пустота держателя описана как главный предмет кадра.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — an almost empty, minimal still life; the emptiness of the tab holder is the subject.
Scene: one clean blank ivory sheet lies on a dark desk. Clipped to its right edge is a clear index-tab holder with a thin deep-red rim, visibly empty — nothing is inside it.
Layout: headline zone inside the top 45% and left 40% of the frame. The sheet center-right, between 20% and 74% of frame height, with generous dark space around. The bottom 22% is empty dark charcoal.
Sources: none — the frame contains no documents, photos, screenshots or logos. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "NO FEE YET" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: writing on the sheet, numbers, dollar signs, people, gavels, government imagery.
```

**G014 / Beat B024**
РЕЖИССУРА:
Рифма с G013: закладка появилась. Портрет CEO Figma справа, к его левому краю прищеплена красная закладка, рядом маленькая карточка Adobe. Figma добилась защиты.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one photographed desk scene with exactly one portrait and one small identifier card.
Scene: on a dark desk, a portrait photograph printed on warm paper lies on the right; one solid deep-red blank index tab is clipped to its left edge. A small paper card with a company identifier sits left-center, the red tab reaching toward it.
Layout: headline zone inside the top 40% and left 42% of the frame; the identifier card below it, between 48% and 72% of frame height. The portrait fills the right half, between 10% and 72%. The bottom 22% is empty dark charcoal.
Sources: image 1 = Figma CEO portrait (the print) — keep the face exactly as photographed, add no people; image 2 = Adobe identifier (on the small card), unchanged. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "THE FEE ENTERS THE DEAL" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: writing on the tab, numbers, money, courts, gavels.
```

**G015 / Beat B026**
РЕЖИССУРА:
Штаб-квартира Adobe крупно справа, на переднем плане на краю бланка лежит закрытая перьевая ручка. Согласие без драмы.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one photographed scene built around the attached headquarters photograph.
Scene: a wide photograph of a corporate headquarters under muted dusk light stands as a large print; in front of it, a closed black fountain pen rests across the edge of a blank contract page.
Layout: headline zone inside the top 45% and left 36% of the frame. The print fills the right 64%, between 8% and 70% of frame height; pen and page in front of its lower edge, above 78%. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe headquarters, San Jose; it is the print, shown unchanged. No other photo or logo may appear. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "ADOBE AGREES" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: signatures, writing on the page, handshakes, people, cash.
```

**G016 / Beat B027**
РЕЖИССУРА:
Макро на торец толстой пачки бумаги: один лист, кроп 10-Q, выдвинут из середины. Стоимость давно лежит внутри документов.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one photographed close-up; the only readable document is the attached excerpt.
Scene: a low-angle close view of a thick stack of blank paper on a dark desk; one sheet is pulled a few centimeters out of the middle of the stack, lit by a narrow beam, a thin vertical deep-red bracket in its margin.
Layout: headline zone inside the top 40% and left 42% of the frame. The stack spans center-right between 30% and 76% of frame height; the pulled sheet is the sharpest element. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe 10-Q closing-risk disclosure excerpt; it is the pulled sheet, shown unchanged — never retype it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "THE COST WAS ALREADY THERE" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: writing on other sheets, numbers, money, people.
```

**G017 / Beat B028**
РЕЖИССУРА:
Вид сверху: стол разделён тонкой линией, по обе стороны карточки компаний. Красный бумажный брусок риска лежит на стороне покупателя. Распределение, а не наказание.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one photographed top-down desk scene; no scales, no justice symbols.
Scene: a dark desk divided by one thin pale line. Left of the line, a small paper card with a company identifier; right of the line, another card with the second identifier. A solid deep-red paper block rests on the left side, next to the left card.
Layout: headline zone inside the top 25% of the frame, left half. The two sides fill the band between 32% and 76% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe identifier (left card); image 2 = Figma identifier (right card). Both unchanged and small. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "RISK ALLOCATION" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: scales of justice, gavels, government imagery, money, arrows, writing on the block.
```

**G018 / Beat B029**
РЕЖИССУРА:
Изменено по уроку G003: развилка снята как настоящие предметы на пробковой доске, а не графикой. Одна нить раздваивается у булавки: серая идёт к пустой карточке, красная к сплошной красной карточке.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — a real photographed cork board with physical pins, thread and paper cards, not a graphic diagram.
Scene: one thread enters from the left and meets a brass pin, where it splits: an upper pale-grey thread runs to an empty outlined ivory card; a lower deep-red thread runs to a solid deep-red card. Nothing is written anywhere.
Layout: headline zone inside the top 25% of the frame, left half. Fork point center-left at 50% of frame height; both cards on the right half, the lower card ending above 78%. The bottom 22% is empty dark charcoal.
Sources: none — the frame contains no documents, photos, screenshots or logos. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "IF CLOSING FAILS" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: labels, icons, numbers, printed flowcharts, people.
```

**G019 / Beat B031**
РЕЖИССУРА:
Изменено: заголовок перенесён влево вверх. Отличие от B030 (тот же договор) даёт экстремальное макро: резкая только полоса с нужной фразой, края листа растворяются.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one extreme close-up of the attached contract excerpt; no other document.
Scene: an extreme close-up of one contract excerpt on warm aged paper with very shallow depth of field — a sharp band across the middle lines, paper edges melting into blur — and a thin vertical deep-red bracket in the margin beside the sharp band.
Layout: headline zone inside the top 40% and left 40% of the frame. The excerpt fills the right 60%, between 8% and 76% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = Merger Agreement Section 8.2 "not a penalty" excerpt; it is the paper, shown unchanged — never retype or redraw it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "NOT A PENALTY" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: underlining inside the document, gavels, courts, scales, money.
```

**G020 / Beat B032**
РЕЖИССУРА:
Без вложений: открытая бухгалтерская книга с чистыми строками. Одна строка залита отмеренным красным бруском, рядом лежит латунная линейка без делений. Сумма, согласованная заранее.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — a quiet still life; nothing is written or numbered anywhere.
Scene: an open ledger book on a dark desk, pages blank with faint grey ruled lines. On one line a solid deep-red bar fills a precise measured length; an unmarked brass straightedge lies parallel to it.
Layout: headline zone inside the top 40% and left 40% of the frame. The ledger center-right at a gentle angle, between 25% and 76% of frame height. The bottom 22% is empty dark charcoal.
Sources: none — the frame contains no documents, photos, screenshots or logos. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "LIQUIDATED DAMAGES" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: numbers, ruler markings, currency symbols, cash, gavels, people.
```

**G021 / Beat B033**
РЕЖИССУРА:
К углу кропа 8-K через пробитое отверстие привязана пустая бирка-ценник на красной нити. У провала была цена.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one photographed desk scene; the price tag is completely blank.
Scene: one paper excerpt lies on a dark desk; through a punched hole in its lower-left corner a thin deep-red string is tied to a blank manila price tag resting beside it.
Layout: headline zone inside the top 45% and left 40% of the frame. The excerpt on the right half, between 10% and 70% of frame height; the tag near the center, above 78%. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe Form 8-K merger-agreement excerpt; it is the paper, shown unchanged — never retype it. No other document may appear. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "FAILURE HAD A PRICE" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: writing or numbers on the tag, currency, cash, people.
```

**G022 / Beat B035**
РЕЖИССУРА:
Официальная графика сделки висит в раме на стене под одним прожектором, одна красная булавка над рамой. Кадр отмечает день.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one framed print on a wall; the only logos are those inside the attached image.
Scene: a framed print hangs alone on a dark wall under a single spotlight; one deep-red pin is pushed into the wall just above the frame's top center.
Layout: headline zone inside the top 40% and left 42% of the frame. The framed print center-right, between 12% and 72% of frame height, with wide darkness around. The bottom 22% is empty dark charcoal.
Sources: image 1 = official Adobe + Figma deal graphic; it is the framed print, unchanged — never redraw its logos. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "SEPTEMBER 15, 2022" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: calendars, extra numbers, people, cash.
```

**G023 / Beat B036**
РЕЖИССУРА:
Масштаб: широкий отпечаток сцены Adobe MAX, к правому краю прищеплена маленькая карточка Figma. Лица на фото не трогаем.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one large event photograph from the attachments plus one small identifier card.
Scene: a wide event photograph of a keynote stage and audience is presented as a large print covering most of the frame; a small paper card with a company identifier is clipped to the print's right edge.
Layout: headline zone inside the top 35% and left 40% of the frame, over dark shadow. The print spans from 30% to the right edge, between 18% and 74% of frame height; card at right-middle. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe MAX 2022 keynote stage (the print) — keep every face and person exactly as photographed, add no people; image 2 = Figma identifier (small card), unchanged. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "A GIANT SOFTWARE DEAL" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: invented stage screens or slogans, money, extra logos.
```

**G024 / Beat B037**
РЕЖИССУРА:
Нарочито обычный кадр: небольшой отпечаток толпы на Config и аккуратная закрытая папка на прибранном столе. Красный только под заголовком.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — a calm, orderly, deliberately ordinary desk scene; no alarm cues.
Scene: a tidy dark desk; a medium photographic print of a conference crowd lies squarely on the right; beside it a neatly closed plain grey folder aligned parallel to the print.
Layout: headline zone inside the top 45% and left 40% of the frame. Folder and print center-right, between 25% and 74% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = Figma Config 2023 crowd; it is the print, unchanged — do not alter or add people. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, calm and serious; the only red is the headline underline.
Headline: "THE DEAL LOOKED NORMAL" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: folder labels, money, logos, warning signs.
```

**G025 / Beat B038**
РЕЖИССУРА:
Три предмета в ряд на стене: карточка Adobe, карточка Figma и пустая рамка, одобрения. Пустота рамки описана как предмет.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — exactly three items pinned in a row on a wall; the third is an empty frame with nothing inside.
Scene: on a dark wall, three items are pinned evenly spaced in a straight row: a small card with one company identifier, a small card with a second identifier, and an empty open paper frame — plain dark wall visible through it — with a thin deep-red top edge.
Layout: headline zone = top center, inside the top 22% of the frame. The row sits between 34% and 72% of frame height, left to right. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe identifier (first card); image 2 = Figma identifier (second card). Both unchanged and small. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "BUYER • TARGET • APPROVALS" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: labels under items, government buildings, flags, gavels.
```

**G026 / Beat B039**
РЕЖИССУРА:
Отпечаток графики сделки лежит на столе, его угол отогнут, а под ним виден кроп Section 8.2. Механизм лежит под заголовком.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one print with its corner peeled back revealing one document underneath; both from the attachments.
Scene: a print lies flat on a dark desk; its lower-right corner is physically peeled back and curled up, revealing a contract excerpt underneath, with a thin vertical deep-red bracket in the excerpt's margin.
Layout: headline zone inside the top 45% and left 40% of the frame. The print fills center-right between 10% and 74% of frame height; the revealed corner at right-middle. The bottom 22% is empty dark charcoal.
Sources: image 1 = official Adobe + Figma deal graphic (top print), unchanged; image 2 = Merger Agreement Section 8.2 fee excerpt (revealed underneath), unchanged — never retype it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "THE HIDDEN FAILURE MECHANISM" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: "secret" or "classified" cues, locks, money, people.
```

**G027 / Beat B040**
РЕЖИССУРА:
Низкий ракурс на очень толстый договор, глубоко внутри торчит красная закладка. Сверху маленький кроп пресс-релиза: поверхность против глубины.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one photographed close-up of a thick blank agreement stack; the only readable text is the attached excerpt.
Scene: a low-angle view of a very thick bound agreement on a dark desk, blank page edges facing camera; one deep-red tab sticks out from deep inside the stack near its bottom. A small crisp announcement excerpt lies on top of the stack.
Layout: headline zone inside the top 40% and left 40% of the frame. The stack spans center-right between 30% and 76% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe acquisition announcement headline; it is the excerpt on top, unchanged — never retype it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "DEEPER IN THE AGREEMENT" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: writing on page edges or the tab, money, people.
```

**G028 / Beat B041**
РЕЖИССУРА:
Бит 3 секунды. Отпечаток здания Еврокомиссии в холодных сумерках, одна красная булавка. Входят регуляторы.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — exactly one photograph on a wall; no flags.
Scene: a photographic print of a large institutional building at blue dusk is pinned to a dark wall with one deep-red pin at its top-left corner; cool, still, quiet.
Layout: headline zone inside the top 45% and left 40% of the frame. The print fills the right 60%, between 10% and 72% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = European Commission Berlaymont headquarters; it is the print, unchanged. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light with a cool blue cast on the print, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "2023: THE RISK ARRIVES" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: EU flags, stars, gavels, storm clouds, people.
```

## Часть 2 — G029–G055

**G029 / Beat B042**
РЕЖИССУРА:
Открывается британское расследование. Вид сверху: только что раскрытая папка, внутри кроп таймлайна дела CMA со скобкой на полях. Образ «папку открыли».
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one opened folder on a desk; the only document is the attached excerpt; no flags or crests.
Scene: top-down view of a manila case folder just opened flat on a dark desk; on its right-hand page lies one paper excerpt with a thin vertical deep-red bracket in its margin; the left-hand page is blank.
Layout: headline zone inside the top 45% and left 38% of the frame. The open folder center-right, between 18% and 76% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = UK CMA case-page timeline excerpt; it is the excerpt in the folder, unchanged — never retype it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "UK REVIEW OPENS" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: folder labels, seals, Union Jack, gavels, people.
```

**G030 / Beat B043**
РЕЖИССУРА:
Вид сбоку на архивный бокс: тонкая закрытая папка (фаза 1) с прикреплённым кропом и за ней толстая папка с красной закладкой (фаза 2).
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one archive box with exactly two folders; nothing is written on the box or folders.
Scene: side view of two case folders standing upright in an open cardboard archive box on a dark desk: the front folder thin and closed with one small paper excerpt clipped to its face; the folder behind noticeably thicker, one deep-red tab rising from it.
Layout: headline zone inside the top 40% and left 40% of the frame. The box center-right, between 28% and 76% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = UK CMA Phase 1 decision title block; it is the clipped excerpt, unchanged — never retype it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "PHASE TWO" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: labels, numbers, seals, flags, people.
```

**G031 / Beat B044**
РЕЖИССУРА:
Смена масштаба: фасад Berlaymont во весь кадр, заголовок в тёмном небе сверху слева, низ уходит в тень.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — the attached building photograph fills the frame; no flags, stars or added signage.
Scene: a wide, cinematic full-frame view of a large institutional office building, deep muted grading, darkened sky.
Layout: headline zone inside the top 35% and left 45% of the frame, over the dark sky. The building occupies the center and right. The bottom 22% falls into plain near-black shadow with no building detail.
Sources: image 1 = European Commission Berlaymont exterior (alternate view); it is the photograph, unchanged — do not add or alter architecture or signs. A style reference, if attached, sets only the look.
Look: charcoal-black tones, subtle warm paper-grain texture overlay, low-key light, fine film grain, restrained deep-red accents, calm and serious.
Headline: "EU IN-DEPTH REVIEW" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: people, gavels, storm effects, extra text on the building.
```

**G032 / Beat B046**
РЕЖИССУРА:
Два органа, два возражения. Кроп CMA слева, фото Еврокомиссии справа, у каждого маленький красный флажок. Между ними пустая стена: финального решения нет.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — exactly two items on a wall with an empty wall between them.
Scene: on a dark wall, a paper excerpt (left) and a photographic print of an institutional building (right) are pinned at equal size; each has one small blank deep-red paper flag clipped to its top edge. The wall between them is plain and empty — a deliberate void.
Layout: headline zone = top center, inside the top 22% of the frame. The two items between 30% and 74% of frame height, in the left and right thirds. The bottom 22% is empty dark charcoal.
Sources: image 1 = UK CMA Phase 1 decision title block (left), unchanged — never retype it; image 2 = European Commission Berlaymont (right print), unchanged. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "FORMAL OBJECTIONS" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: writing on flags, stamps, lines between items, national flags, gavels.
```

**G033 / Beat B047**
РЕЖИССУРА:
Отпечаток здания DOJ в холодном свете. На переднем плане закрытая папка и рядом пустой проволочный лоток: иска нет. Пустота лотка — главный предмет кадра.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — the wire tray in front is visibly empty; that emptiness is the point.
Scene: a photographic print of a government headquarters leans upright on a dark desk in cool light; in front, one closed plain folder lies beside an empty black wire document tray with nothing in it.
Layout: headline zone inside the top 45% and left 38% of the frame. The print on the right half, between 8% and 66% of frame height; folder and empty tray in front of it, above 78%. The bottom 22% is empty dark charcoal.
Sources: image 1 = U.S. Department of Justice headquarters exterior; it is the print, unchanged — no seal close-ups. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "INVESTIGATION ≠ LAWSUIT" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: papers in the tray, folder labels, seals, courtrooms, gavels, handcuffs, people.
```

**G034 / Beat B048**
РЕЖИССУРА:
Слева кроп 8-K с перьевой ручкой поперёк (подписано). Справа за широкой пустотой отдельная карточка, очерченная лишь серым контуром (не закрыто).
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — two separate objects with a wide empty gap between them; nothing connects them.
Scene: on a dark desk, left: a paper excerpt with a closed black fountain pen resting across it. Right, across a wide empty gap: one blank card defined only by a thin pale-grey outline, untouched.
Layout: headline zone = top center, inside the top 22% of the frame. Excerpt with pen in the left 40%, outlined card in the right 30%, both between 30% and 74% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe Form 8-K merger-agreement excerpt; it is the left excerpt, unchanged — never retype it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "SIGNED ≠ CLOSED" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: signatures, stamps, arrows, locks, handshakes, people.
```

**G035 / Beat B049**
РЕЖИССУРА:
Резкий кроп Section 8.2 впереди. Сзади в сильном размытии растут стопки чистых бумаг. Пункт договора не меняется, давление растёт.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one sharp document in front of blurred blank paper stacks; the stacks carry no readable text.
Scene: a single contract excerpt lies tack-sharp on a dark desk, a thin vertical deep-red bracket in its margin; behind it, heavily out of focus, tall stacks of blank papers rise and crowd the background.
Layout: headline zone inside the top 40% and left 40% of the frame. The sharp excerpt center-right between 35% and 74% of frame height; blurred stacks behind it. The bottom 22% is empty dark charcoal.
Sources: image 1 = Merger Agreement Section 8.2 fee excerpt; it is the sharp excerpt, unchanged — never retype it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "THE CLAUSE DIDN'T CHANGE" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: text on the stacks, money, government buildings, people.
```

**G036 / Beat B050**
РЕЖИССУРА:
Узкий коридор между двумя стенами из папок. В конце маленькая пустая светлая карточка (закрытие) далеко. Кроп 10-Q приколот на ближней стене.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one photographed perspective scene made of real stacked folders; nothing is labeled.
Scene: a low, deep perspective down a narrow corridor formed by two tall dark walls of stacked file folders on a desk; at the far end a small blank pale card stands in faint light. One paper excerpt is pinned high on the near right wall.
Layout: headline zone inside the top 35% and left 40% of the frame. The corridor converges at center; the excerpt upper right, between 12% and 45% of frame height. The bottom 22% is dark shadow.
Sources: image 1 = Adobe 10-Q closing-risk excerpt; it is the pinned excerpt, unchanged — never retype it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "FAILED CLOSING GETS CLOSER" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: folder labels, clocks, hourglasses, doors, people.
```

**G037 / Beat B051**
РЕЖИССУРА:
Два органа сходятся в одном моменте. Отпечаток Еврокомиссии в сумерках и меньший кроп CMA приколоты к стене и соединены одной короткой красной нитью.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — exactly two pinned items joined by one short thread.
Scene: on a dark wall, a large photographic print of an institutional building at dusk (right) and a smaller paper excerpt (left-center) are pinned; one short taut deep-red thread joins a pin on each.
Layout: headline zone inside the top 35% and left 42% of the frame; the excerpt below it, between 42% and 72% of frame height. The large print on the right half, between 10% and 72%. The bottom 22% is empty dark charcoal.
Sources: image 1 = European Commission Berlaymont (large print), unchanged; image 2 = UK CMA case-page timeline excerpt (small excerpt), unchanged — never retype it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "NOVEMBER 2023" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: calendars, flags, gavels, people.
```

**G038 / Beat B056**
РЕЖИССУРА:
Один лист с двумя прикреплёнными карточками компаний. По красной пунктирной линии между ними лист частично согнут: сделку, возможно, придётся перекроить.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one blank sheet partly folded along a dashed line; nothing is cut or torn.
Scene: top-down view of one blank sheet on a dark desk with two small identifier cards paper-clipped to it, one on each half; a deep-red dashed fold line runs between them and the sheet is partly lifted along that line.
Layout: headline zone inside the top 45% and left 40% of the frame. The sheet center-right, between 22% and 76% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe identifier; image 2 = Figma identifier — each on its own card, unchanged and small. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "REMEDIES CHANGE THE DEAL" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: scissors, tearing, broken logos, gavels, people.
```

**G039 / Beat B057**
РЕЖИССУРА:
Буквально «на столе»: отпечаток скриншота Figma на тёмном столе переговоров. Рядом, не пересекая его, пунктир красным карандашом: возможное выделение.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one printed screenshot from the attachment on an empty conference table; the dashed line never crosses it.
Scene: a long dark conference table at a low angle, empty chairs dissolving into shadow; a printed product screenshot lies on the table; beside it runs a faint deep-red dashed pencil line with a red pencil resting at its end.
Layout: headline zone inside the top 35% and left 42% of the frame. The print center-right, between 35% and 74% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = official Figma collaboration workflow product visual; it is the print, unchanged — never redraw or invent interface. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "FIGMA DESIGN ON THE TABLE" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: people, name plates, scissors, gavels, extra screens.
```

**G040 / Beat B058**
РЕЖИССУРА:
Стальная струбцина прижимает стопку бумаг, к лицевой стороне прикреплён кроп предварительных выводов CMA. Справа нетронутый чистый лист, до которого струбцина не достаёт.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — a heavy clamp on one stack and a separate blank sheet it does not reach.
Scene: on a dark desk, a heavy black steel clamp presses down on a short stack of paper; one paper excerpt is fixed to the front of the stack. To the right a single clean blank sheet lies untouched in soft light.
Layout: headline zone inside the top 40% and left 38% of the frame. Clamp and stack at center, blank sheet center-right, all between 30% and 76% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = UK CMA provisional-findings excerpt; it is the excerpt on the stack, unchanged — never retype it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "PRESSURE, NOT FINALITY" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: writing on the blank sheet, stamps, gavels, government buildings, people.
```

**G041 / Beat B060**
РЕЖИССУРА:
Компании возражают. Отпечаток сцены Adobe MAX справа, меньший портрет CEO Figma слева, между ними толстая переплетённая пачка ответа с чистой обложкой. Лица не трогаем.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — exactly two photographs from the attachments and one blank bound document.
Scene: on a dark desk, a large event-photograph print (right) and a smaller portrait print (left-center) lie apart; between them rests a thick bound submission with a plain blank cover.
Layout: headline zone inside the top 35% and left 42% of the frame; the portrait print below it, between 40% and 74% of frame height. The large print on the right half, between 10% and 72%. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe MAX 2022 keynote stage (large print); image 2 = Figma CEO portrait (small print). Both unchanged — keep every face and person exactly as photographed; add no people. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "ADOBE + FIGMA PUSH BACK" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: cover titles, fists, courtroom imagery, extra logos.
```

**G042 / Beat B062**
РЕЖИССУРА:
Открытый скоросшиватель: на ранних листах кроп таймлайна CMA, последний раздел открыт на совершенно чистой странице. Решения по существу нет.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — an open binder whose final page is completely blank; that blank page is the point.
Scene: an open ring binder on a dark desk; on its left side a paper excerpt sits on the earlier pages; the binder is opened at its last section — a divider with a deep-red edge followed by a completely blank white page.
Layout: headline zone inside the top 40% and left 38% of the frame. The binder center-right, between 24% and 76% of frame height; the blank page is the brightest area. The bottom 22% is empty dark charcoal.
Sources: image 1 = UK CMA case-page timeline excerpt; it is the excerpt, unchanged — never retype it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "NO FINAL MERITS DECISION" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: divider labels, writing on the blank page, stamps, gavels, people.
```

**G043 / Beat B063**
РЕЖИССУРА:
Две открытые папки одинакового размера лежат симметрично, в них позиция CMA и ответ компаний. Между ними нейтральная линейка. Весов нет.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — two equal open folders side by side; no scales or balance imagery.
Scene: top-down view of two open manila folders of identical size lying side by side on a dark desk, a thin neutral grey unmarked ruler between them; each folder holds one paper excerpt.
Layout: headline zone = top center, inside the top 22% of the frame. The folders fill the band between 28% and 76% of frame height, symmetrically. The bottom 22% is empty dark charcoal.
Sources: image 1 = UK CMA provisional-findings excerpt (left folder); image 2 = Adobe/Figma response excerpt (right folder). Both unchanged — never retype them. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "TWO SIDES OF THE RECORD" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: scales of justice, versus signs, ruler markings, people.
```

**G044 / Beat B064**
РЕЖИССУРА:
Изменено: заголовок перенесён влево вверх. Рядом с кропом о возможных средствах лежат три латунные заготовки ключей, одна перевязана красной нитью. Подбор решения.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one excerpt and three plain key blanks; no locks anywhere.
Scene: on a dark desk, one paper excerpt lies at a slight angle; beside it three uncut, unengraved brass key blanks lie in a neat row, one tied with a thin deep-red thread.
Layout: headline zone inside the top 40% and left 40% of the frame. Excerpt and keys on the right 58%, between 22% and 76% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = UK CMA Notice of Possible Remedies title excerpt; it is the paper, unchanged — never retype it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "WHAT REMEDY COULD WORK?" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: locks, padlocks, engraved keys, gavels, people.
```

**G045 / Beat B066**
РЕЖИССУРА:
Позиция компаний, со ссылкой на них. Отпечаток штаб-квартиры Adobe частично накрыт чистым листом ответа с вертикальной красной полосой цитаты, к углу прикреплена карточка Figma.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one photograph, one blank sheet, one small identifier card; the sheet has no text.
Scene: on a dark desk, a photographic print of a corporate headquarters lies partly covered by a single blank response sheet; a solid vertical deep-red quote bar runs along the sheet's left edge; a small identifier card is clipped to the sheet's top corner.
Layout: headline zone inside the top 40% and left 40% of the frame. Print and sheet center-right, between 18% and 76% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe headquarters, San Jose (the print), unchanged; image 2 = Figma identifier (small card), unchanged. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "THE COMPANIES' CHARACTERIZATION" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: quotation text, writing on the sheet, gavels, people.
```

**G046 / Beat B067**
РЕЖИССУРА:
Здание Berlaymont ночью во весь кадр, окна горят: процесс ещё открыт. Простота намеренная.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — the attached building photograph fills the frame at night; no stamps, flags or symbols.
Scene: a large institutional office building at night with some windows lit, full-frame, deep muted grading.
Layout: headline zone inside the top 35% and left 45% of the frame, over dark sky. The building fills center and right. The bottom 22% falls into plain near-black shadow with no detail.
Sources: image 1 = European Commission Berlaymont exterior (alternate view); it is the photograph, unchanged — do not add signs or alter the building. A style reference, if attached, sets only the look.
Look: charcoal-black tones, subtle warm paper-grain texture overlay, low-key light, fine film grain, restrained deep-red accents, calm and serious.
Headline: "NO FINAL PROHIBITION" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: EU flags, stars, stamps, people, gavels.
```

**G047 / Beat B068**
РЕЖИССУРА:
Взгляд через узкую щель между двумя шкафами для документов. В глубине на свету выцветший отпечаток графики сделки. Вопрос, а не ответ.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one photographed view through a narrow gap; the only logos are inside the attached print.
Scene: a view through a narrow vertical gap between two dark filing cabinets; in the lit space beyond, a faded print stands on a desk, visible but hard to reach.
Layout: headline zone inside the top 35% and left 40% of the frame, over the dark cabinet side. The gap slightly right of center; the print inside it between 30% and 70% of frame height. The bottom 22% is dark cabinet shadow.
Sources: image 1 = official Adobe + Figma deal graphic; it is the faded print, unchanged apart from muted color — never redraw logos. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "COULD THIS STILL CLOSE?" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: cabinet labels, doors, locks, people.
```

**G048 / Beat B070**
РЕЖИССУРА:
Классическая документальная подача: кроп 8-K о прекращении справа, скобка у обоснования. Прямая речь компаний.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one attached document on a desk; no roads, mazes or regulators.
Scene: one paper excerpt on warm aged paper lies slightly angled on a dark desk, held by a black binder clip, a thin vertical deep-red bracket in its margin beside the text.
Layout: headline zone inside the top 45% and left 40% of the frame. The excerpt fills the right 55%, between 10% and 75% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe Form 8-K termination excerpt; it is the paper, unchanged — never retype, redraw or extend it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "NO CLEAR PATH" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: underlining inside the document, stamps, gavels, government buildings.
```

**G049 / Beat B071**
РЕЖИССУРА:
Отпечаток здания Еврокомиссии, перед ним открытая пустая папка расследования. Внутри ничего не проштамповано.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — the open folder in front is empty; no stamp exists anywhere.
Scene: a photographic print of an institutional building stands upright on a dark desk; in front of it lies an open plain review folder with blank pages and nothing inside.
Layout: headline zone inside the top 45% and left 38% of the frame. The print on the right half, between 8% and 64% of frame height; the open folder in front, above 78%. The bottom 22% is empty dark charcoal.
Sources: image 1 = European Commission Berlaymont; it is the print, unchanged. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "NOT A FINAL PROHIBITION" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: stamps, seals, writing on pages, flags, gavels, people.
```

**G050 / Beat B072**
РЕЖИССУРА:
Вид сверху: две карточки компаний, красная нить между ними аккуратно перерезана, концы лежат ровно на чистом листе. Взаимно, спокойно.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — an orderly, calm separation; logos stay intact and small.
Scene: top-down view of a dark desk: two small identifier cards far apart, joined by a deep-red thread that has been cleanly cut in the middle; the two cut ends lie neatly side by side on one blank sheet placed between the cards.
Layout: headline zone inside the top 30% of the frame, left half. Cards, thread and sheet between 36% and 74% of frame height, left to right. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe identifier; image 2 = Figma identifier — each on its own card, unchanged, never broken. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "MUTUAL TERMINATION" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: scissors, cracks, broken logos, fire, writing on the sheet, people.
```

**G051 / Beat B073**
РЕЖИССУРА:
Две закрытые папки, перевязанные серой тесьмой, уложены в архивный бокс, к верхней прикреплён кроп CMA. Серый тон: процедура закрыта, вердикта нет.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — two closed folders in an archive box; procedural, not a verdict.
Scene: two closed case folders tied with plain grey tape lie stacked inside an open cardboard archive box on a dark desk, seen from a high angle; one paper excerpt is clipped to the top folder.
Layout: headline zone inside the top 45% and left 38% of the frame. The box center-right, between 20% and 76% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = UK CMA case-page timeline excerpt; it is the clipped excerpt, unchanged — never retype it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, calm and serious; red only in the headline underline.
Headline: "REVIEWS END" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: box labels, stamps, verdict imagery, gavels, people.
```

**G052 / Beat B074**
РЕЖИССУРА:
Изменено: заголовок перенесён влево вверх. Главное — кроп заявления DOJ, крупно справа со скобкой. Небольшой отпечаток здания DOJ подложен под его угол.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one statement excerpt and one small building print, both from the attachments; no seals.
Scene: on a dark desk a paper excerpt lies large and sharp with a thin vertical deep-red bracket in its margin; a small photographic print of a government building sits partly tucked under its upper-right corner.
Layout: headline zone inside the top 45% and left 40% of the frame. The excerpt fills the right 55%, between 12% and 76% of frame height; the small print at its upper-right. The bottom 22% is empty dark charcoal.
Sources: image 1 = DOJ Antitrust Division statement excerpt (main), unchanged — never retype it; image 2 = U.S. Department of Justice headquarters (small print), unchanged. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "DOJ WELCOMES ABANDONMENT" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: seals, courtrooms, gavels, handcuffs, people.
```

**G053 / Beat B075**
РЕЖИССУРА:
Отпечаток здания DOJ в очень холодном свете, поверх него одна закрытая папка. Расследование закрыто без суда.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one building print and one closed folder; nothing else.
Scene: a photographic print of a government headquarters lies flat on a dark desk in cold blue-grey light; one closed plain folder rests across its lower-right corner.
Layout: headline zone inside the top 45% and left 40% of the frame. Print and folder center-right, between 18% and 76% of frame height, generous darkness around. The bottom 22% is empty dark charcoal.
Sources: image 1 = U.S. Department of Justice headquarters exterior; it is the print, unchanged — no seal close-ups. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light with a colder grade, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "INVESTIGATION, NO BLOCKING LAWSUIT" — the only generated text; off-white distressed condensed sans-serif capitals, three lines, moderate size, short deep-red underline bar beneath it.
Avoid: folder labels, courtrooms, judges, gavels, people.
```

**G054 / Beat B076**
РЕЖИССУРА:
Штаб-квартира Adobe в сумерках во весь кадр, без предметов. Суда нигде нет. Пауза перед кульминацией.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — the attached headquarters photograph fills the frame; no courtroom imagery of any kind.
Scene: a wide cinematic full-frame view of a corporate headquarters at dusk, deep muted grading, still and quiet.
Layout: headline zone inside the top 40% and left 38% of the frame, over the darker left side. The buildings fill center and right. The bottom 22% falls into plain near-black shadow with no detail.
Sources: image 1 = Adobe headquarters, San Jose; it is the photograph, unchanged — do not alter signs or architecture. A style reference, if attached, sets only the look.
Look: charcoal-black tones, subtle warm paper-grain texture overlay, low-key light, fine film grain, restrained deep-red accents, calm and serious.
Headline: "NO COURTROOM LOSS" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: courtrooms, judges, gavels, verdict imagery, people.
```

**G055 / Beat B077**
РЕЖИССУРА:
Кульминация, 3.4 секунды. Темнота, один луч света на кропе Section 8.2, яркая красная скобка на полях. Больше ничего.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one spotlit document in darkness; nothing else in the frame.
Scene: near-total darkness; a single narrow spotlight falls on one contract excerpt lying on a desk, a bright thin vertical deep-red bracket in its margin; everything else dissolves into black.
Layout: headline zone inside the top 40% and left 40% of the frame. The lit excerpt center-right, between 32% and 74% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = Merger Agreement Section 8.2 fee excerpt; it is the lit excerpt, unchanged — never retype it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, hard single-source light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "THE CLAUSE BECOMES REAL" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: money, explosions, glow effects, people.
```

## Часть 3 — G056–G085

**G056 / Beat B078**
РЕЖИССУРА:
Верхний лист кропа Mutual Termination Agreement переворачивается, под ним чистая страница с красной закладкой. Что дальше.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one small document mid page-turn; the page underneath is blank.
Scene: top-down view of a small bound document on a dark desk; its top sheet is mid-turn, lifted and curving; beneath it the next page is blank with one deep-red tab at its edge.
Layout: headline zone inside the top 45% and left 38% of the frame. The document center-right, between 20% and 76% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = Mutual Termination Agreement excerpt; it is printed on the turning top sheet, unchanged — never retype it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "WHAT HAPPENS NEXT" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: writing on the blank page, money, people.
```

**G057 / Beat B079**
РЕЖИССУРА:
Справа кроп 8-K о сроке платежа. Под заголовком три пустые карточки-ступени к сплошной красной. Отсчёт дней без цифр: цифры на карточках запрещены первой строкой.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — the step cards are completely blank; no digits, calendar marks or numbers anywhere outside the attached document.
Scene: on a dark desk, a paper excerpt lies on the right with a thin vertical deep-red bracket in its margin; on the left, three small blank ivory cards step upward in a row toward a fourth card of solid deep red.
Layout: headline zone inside the top 36% and left 42% of the frame; step cards below it, between 44% and 74% of frame height. The excerpt on the right half, between 10% and 74%. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe Form 8-K termination excerpt (payment-timing passage); unchanged — never retype it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "DUE IN THREE BUSINESS DAYS" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: calendars, clocks, cash.
```

**G058 / Beat B080**
РЕЖИССУРА:
Рифма с G022. Отпечаток штаб-квартиры Adobe в холодном утреннем свете на стене, одна красная булавка. День платежа.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one photograph on a wall; no money in the frame.
Scene: a photographic print of a corporate headquarters in cool early-morning light hangs on a dark wall; one deep-red pin is pushed in just above its top edge.
Layout: headline zone inside the top 40% and left 42% of the frame. The print center-right, between 12% and 72% of frame height, wide darkness around. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe headquarters, San Jose; it is the print, unchanged. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light with a cool morning cast on the print, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "DECEMBER 20, 2023" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: calendars, extra numbers, cash, people.
```

**G059 / Beat B081**
РЕЖИССУРА:
Вид сверху: кроп 10-K Adobe слева, кроп S-1 Figma справа, их соединяет одна прямая красная линия. Симметрия бухгалтерской проводки.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — exactly two documents joined by one thin line; no money or symbols.
Scene: top-down view of a dark desk; two paper excerpts lie far apart, left and right, joined by one straight thin deep-red line across the empty dark space between them.
Layout: headline zone = top center, inside the top 22% of the frame. Excerpts symmetric between 30% and 76% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe FY2023 10-K payment excerpt (left); image 2 = Figma S-1 fee-receipt excerpt (right). Both unchanged — never retype them. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "ADOBE PAYS • FIGMA RECEIVES" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: labels on the line, currency symbols, cash, logos.
```

**G060 / Beat B082**
РЕЖИССУРА:
Ракурс сбоку вдоль стены: две карточки компаний далеко друг от друга, между ними натянутая красная нить уходит в перспективу. Настоящий перевод.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — two small identifier cards and one taut thread; no money anywhere.
Scene: a dark wall seen at a raking side angle; two small identifier cards are pinned far apart along it, and one taut deep-red thread runs between them, receding in perspective.
Layout: headline zone inside the top 35% and left 42% of the frame. Near card center-left, far card toward the right edge; the thread crosses the band between 40% and 70% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe identifier (near card); image 2 = Figma identifier (far card). Both unchanged and small. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "THE MONEY MOVED" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: banknotes, coins, cash stacks, arrows, people.
```

**G061 / Beat B084**
РЕЖИССУРА:
Обесцвеченная графика сделки слева уходит в темноту. Кроп Section 8.2 справа тёплый и резкий. Сделка исчезает, комиссия остаётся.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one fading print and one lit document; no burning or tearing.
Scene: on a dark desk, a desaturated print on the left fades into shadow, barely visible; on the right, a contract excerpt is warm, sharp and lit, with a thin vertical deep-red bracket in its margin.
Layout: headline zone inside the top 32% of the frame, left 60%. The fading print left-center between 38% and 74% of frame height; the lit excerpt on the right, between 14% and 74%. The bottom 22% is empty dark charcoal.
Sources: image 1 = official Adobe + Figma deal graphic (fading print), unchanged apart from dim desaturated color; image 2 = Merger Agreement Section 8.2 fee excerpt (lit), unchanged — never retype it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "THE DEAL DISAPPEARED. THE FEE DIDN'T." — the only generated text; off-white distressed condensed sans-serif capitals, two lines (one sentence per line), moderate size, short deep-red underline bar beneath it.
Avoid: fire, torn paper, regulator imagery, cash.
```

**G062 / Beat B085**
РЕЖИССУРА:
Изменено: заголовок перенесён влево вверх. Макро на кроп Mutual Termination Agreement. Источник платежа — договор.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one extreme close-up of the attached contract excerpt; no government imagery.
Scene: an extreme close-up of one contract excerpt on warm aged paper, very shallow depth of field, a sharp band across the key lines, a thin vertical deep-red bracket in the margin beside them.
Layout: headline zone inside the top 45% and left 40% of the frame. The excerpt fills the right 60%, between 8% and 76% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = Mutual Termination Agreement excerpt (liquidated damages / sole remedy); it is the paper, unchanged — never retype or redraw it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "THE CONTRACT, NOT A REGULATOR" — the only generated text; off-white distressed condensed sans-serif capitals, three lines, moderate size, short deep-red underline bar beneath it.
Avoid: underlining inside the document, government buildings, seals, gavels, cash.
```

**G063 / Beat B087**
РЕЖИССУРА:
Выцветший отпечаток графики сделки один лежит на дне пустого архивного бокса. Покупка ушла в архив, так и не состоявшись.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one faded print alone in an otherwise empty box; no stamps.
Scene: a high-angle view into an empty, clean cardboard archive box on a dark desk; a single faded print lies alone on its bottom.
Layout: headline zone inside the top 45% and left 38% of the frame. The box center-right, between 18% and 76% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = official Adobe + Figma deal graphic; it is the faded print, unchanged apart from muted desaturated color. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "THE PURCHASE NEVER HAPPENED" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: box labels, cancellation stamps, tearing, cash.
```

**G064 / Beat B088**
РЕЖИССУРА:
Кадр без вложений: одна тяжёлая чистая карточка с красным обрезом в жёстком свете отбрасывает плотную тень. Реальный весомый предмет.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one blank heavy card and its shadow; no money, numbers or text on it.
Scene: one thick, heavy blank ivory card with a deep-red painted edge lies on a dark desk in hard directional light, casting a crisp solid shadow.
Layout: headline zone inside the top 45% and left 40% of the frame. The card center-right, between 30% and 72% of frame height, large, with generous darkness around. The bottom 22% is empty dark charcoal.
Sources: none — the frame contains no documents, photos, screenshots or logos. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "THE PAYMENT WAS REAL" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: currency symbols, cash, coins, logos, people, documents.
```

**G065 / Beat B089**
РЕЖИССУРА:
Два отдельных листа бухгалтерской книги по диагонали: 10-K Adobe (расход) справа сверху, S-1 Figma (доход) слева ниже. Листы не соприкасаются.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — two separate ledger sheets that never touch, each with one attached excerpt.
Scene: two separate faint-ruled ledger sheets on a dark desk, offset diagonally — one upper-right, one lower-left — separated by a clear dark gap; each carries one paper excerpt.
Layout: headline zone inside the top 36% and left 40% of the frame. Upper-right sheet between 10% and 50% of frame height; lower-left sheet between 44% and 76%. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe FY2023 10-K payment excerpt (upper-right sheet); image 2 = Figma S-1 fee-receipt excerpt (lower-left sheet). Both unchanged — never retype them. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "EXPENSE VS INCOME" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: numbers, plus/minus signs, calculators, cash.
```

**G066 / Beat B090**
РЕЖИССУРА:
Выцветший кроп пресс-релиза лежит далеко слева, тяжёлая карточка платежа далеко справа, между ними широкая пустота. Сложить их нельзя.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — two objects at opposite sides; the wide empty desk between them is a deliberate void.
Scene: on a wide dark desk, a faded paper excerpt lies at the far left; at the far right lies one heavy blank ivory card with a deep-red edge; the space between is completely empty.
Layout: headline zone = top center, inside the top 22% of the frame. The two objects in the outer thirds, between 32% and 74% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe acquisition announcement headline; it is the faded left excerpt, unchanged apart from muted color — never retype it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "PROPOSED ≠ PAID" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: plus signs, totals, numbers on the card, lines between objects, cash.
```

**G067 / Beat B092**
РЕЖИССУРА:
Очень крупный заголовок в левой половине. Маленький кроп Section 8.2 одиноко лежит справа в тёмном пространстве. Центр истории.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one small document in a vast dark space; nothing else.
Scene: a vast dark desk surface; one small contract excerpt lies alone on the right, softly lit, a thin vertical deep-red bracket in its margin.
Layout: headline zone = left half, between 12% and 60% of frame height, large. The small excerpt at right, between 36% and 64% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = Merger Agreement Section 8.2 fee excerpt; unchanged — never retype it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "THE BILLION-DOLLAR COST" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, large, short deep-red underline bar beneath it.
Avoid: dollar signs, cash, gold, people.
```

**G068 / Beat B093**
РЕЖИССУРА:
Крупный отпечаток кейноута Config справа, за ним маленький выцветший отпечаток графики сделки. Независимость без триумфа. Лица не трогаем.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — exactly two prints from the attachments; no celebration effects.
Scene: a large event-photograph print stands on a dark desk, warmly lit; behind it and to one side a small faded print lies flat, half in shadow.
Layout: headline zone inside the top 45% and left 38% of the frame. The large print on the right half, between 8% and 72% of frame height; the small faded print partly visible behind its left edge. The bottom 22% is empty dark charcoal.
Sources: image 1 = Figma Config 2023 keynote stage (large print) — keep every face and person exactly as photographed, add no people; image 2 = official Adobe + Figma deal graphic (small faded print), unchanged apart from muted color. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "FIGMA STAYS INDEPENDENT" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: trophies, confetti, extra logos.
```

**G069 / Beat B094**
РЕЖИССУРА:
Раскрытый толстый том отчётности, на правой странице кроп S-1 со скобкой. Платёж вошёл в историю компании.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one open bound volume; the only readable text is the attached excerpt.
Scene: a thick bound filing volume lies open on a dark desk; on its right-hand page rests one paper excerpt with a thin vertical deep-red bracket in its margin; all other pages are blank.
Layout: headline zone inside the top 45% and left 38% of the frame. The open volume center-right, between 20% and 76% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = Figma S-1 fee-receipt excerpt; unchanged — never retype it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "THE PAYMENT ENTERS FIGMA'S HISTORY" — the only generated text; off-white distressed condensed sans-serif capitals, three lines, moderate size, short deep-red underline bar beneath it.
Avoid: text on other pages, cash, logos, people.
```

**G070 / Beat B095**
РЕЖИССУРА:
Фасад NYSE с баннером Figma во весь кадр, в правом верхнем углу небольшой кроп анонса S-1. Фактологично, без праздника.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — the attached exchange photograph fills the frame; no confetti or tickers.
Scene: a full-frame photograph of a stock-exchange facade with a large company banner, muted documentary grading; a small paper excerpt is clipped as a print in the upper-right corner.
Layout: headline zone inside the top 35% and left 42% of the frame, over the darker left side. The excerpt upper right, between 8% and 36% of frame height. The bottom 22% falls into plain dark shadow with no people or detail.
Sources: image 1 = NYSE facade with Figma banner (the photograph) — keep people exactly as photographed, add none; image 2 = Figma S-1 announcement headline block (small excerpt), unchanged. A style reference, if attached, sets only the look.
Look: charcoal-black tones, subtle warm paper-grain texture overlay, low-key light, fine film grain, restrained deep-red accents, calm and serious.
Headline: "FIGMA GOES PUBLIC" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: confetti, fireworks, stock tickers, charts, added banner text.
```

**G071 / Beat B096**
РЕЖИССУРА:
Кроп анонса цены IPO крупно справа. Цифры есть только внутри кропа. Тихий документальный кадр после широкого G070.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — numbers appear only inside the attached excerpt, exactly as supplied.
Scene: one printed excerpt lies slightly angled on a dark desk, held by a black binder clip, a thin vertical deep-red bracket in its margin.
Layout: headline zone inside the top 45% and left 40% of the frame. The excerpt fills the right 55%, between 10% and 75% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = official Figma IPO pricing announcement; unchanged — never retype, redraw or re-letter it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "IPO SHARE SALE" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: generated numbers, stock tickers, charts, cash.
```

**G072 / Beat B097**
РЕЖИССУРА:
Отпечаток уличной сцены у NYSE справа. Слева чистый разлинованный лист с одной красной строкой: место под точную сумму, которую наложат в монтаже.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — the ledger sheet stays completely blank; no numbers anywhere.
Scene: on a dark desk, a street-level event photograph lies as a print on the right; on the left, a blank faint-ruled ledger sheet with one line marked by a thin deep-red rule, nothing written on it.
Layout: headline zone inside the top 36% and left 42% of the frame; the ledger sheet below it, between 42% and 74% of frame height. The print on the right half, between 10% and 72%. The bottom 22% is empty dark charcoal.
Sources: image 1 = NYSE / Figma street scene; it is the print, unchanged — keep people exactly as photographed, add none. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "NET PROCEEDS" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: numbers, currency, cash, charts.
```

**G073 / Beat B098**
РЕЖИССУРА:
Отпечаток инсталляции Figma у NYSE слева, маленький кроп Section 8.2 справа. Серая нить между ними оборвана: причинной связи нет.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — the thread between the two items is visibly broken; no arrows.
Scene: on a dark wall, an event-photograph print (left) and a small contract excerpt (far right) are pinned apart; a pale-grey thread runs from each toward the other but is broken in the middle, leaving a clean empty gap.
Layout: headline zone = top center, inside the top 22% of the frame. Print on the left half, excerpt at right, both between 30% and 74% of frame height; the gap at center. The bottom 22% is empty dark charcoal.
Sources: image 1 = Figma Commons NYSE installation (print) — keep people exactly as photographed, add none; image 2 = Merger Agreement Section 8.2 fee excerpt (small), unchanged. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "LATER SUCCESS ≠ PROVEN CAUSE" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: arrows, question marks, charts, cash.
```

**G074 / Beat B099**
РЕЖИССУРА:
Отпечаток билборда на Таймс-сквер справа, карточка платежа отдельно слева. Их ничто не соединяет.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — two objects with nothing connecting them.
Scene: on a dark desk, a city-billboard photograph lies as a large print on the right; on the left one heavy blank ivory card with a deep-red edge lies apart; no line, thread or arrow links them.
Layout: headline zone inside the top 36% and left 42% of the frame; the card below it, between 46% and 72% of frame height. The print on the right half, between 10% and 72%. The bottom 22% is empty dark charcoal.
Sources: image 1 = Times Square billboard photo; it is the print, unchanged — add no text to the billboard. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "NO PROVEN IPO CAUSATION" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: connecting lines, arrows, charts, cash, numbers on the card.
```

**G075 / Beat B100**
РЕЖИССУРА:
Ровно один портрет CEO Figma эпохи IPO на тёмной стене. Никаких символов Adobe. Лицо не трогаем.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — exactly one photograph in the frame and no logos at all.
Scene: a single portrait photograph print hangs alone on a dark wall under soft light, nothing else around it.
Layout: headline zone inside the top 45% and left 40% of the frame. The portrait on the right half, between 10% and 72% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = Figma CEO, IPO-era portrait; it is the print, unchanged — keep the face exactly as photographed; add no people. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "ADOBE DID NOT ACQUIRE FIGMA" — the only generated text; off-white distressed condensed sans-serif capitals, three lines, moderate size, short deep-red underline bar beneath it.
Avoid: extra prints, company logos, trophies, cash.
```

**G076 / Beat B101**
РЕЖИССУРА:
По уроку G003: настоящая пробковая доска. Две булавки, серая и красная, между ними простая нить без стрелки. Над красной булавкой приколото фото монтажа баннера у NYSE. Хронология без причинности.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — a real photographed cork board with two physical pins and a plain thread, not a graphic timeline.
Scene: a dark cork board; two pins joined by a plain neutral thread with no arrowhead — a grey pin at left, a deep-red pin at right; above the right pin hangs one pinned photographic print.
Layout: headline zone inside the top 30% of the frame, left half. The thread at about 58% of frame height across the center; the print upper right, between 12% and 52%. The bottom 22% is empty dark charcoal.
Sources: image 1 = NYSE banner setup / scaffolding photo; it is the print, unchanged — keep people exactly as photographed, add none. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "PUBLIC COMPANY" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: dates, labels, arrowheads, charts, confetti.
```

**G077 / Beat B102**
РЕЖИССУРА:
Вертикаль: графика сделки наверху (выгода), кроп Section 8.2 ниже со смещением вправо (риск). Возвращение к исходной архитектуре.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — exactly two items stacked vertically, both from the attachments; no arrows or charts.
Scene: on a dark desk, a print lies high in the frame; below it and offset to the right, a contract excerpt with a thin vertical deep-red bracket in its margin.
Layout: headline zone inside the top 45% and left 38% of the frame. The print center-right between 6% and 42% of frame height; the excerpt right, between 46% and 76%. The bottom 22% is empty dark charcoal.
Sources: image 1 = official Adobe + Figma deal graphic (upper print), unchanged; image 2 = Merger Agreement Section 8.2 fee excerpt (lower), unchanged — never retype it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "UPSIDE / DOWNSIDE" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: arrows, charts, numbers, cash.
```

**G078 / Beat B103**
РЕЖИССУРА:
Изменено: заголовок перенесён влево вверх. Кроп 5 июля лежит на тёмном столе переговоров рядом с закрытой ручкой. Риск получил цену за столом.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one document and one pen on an empty negotiating table; no people.
Scene: on a dark negotiating table one paper excerpt lies with a thin vertical deep-red bracket in its margin; a closed black fountain pen rests beside it; empty chairs dissolve into the dark background.
Layout: headline zone inside the top 45% and left 40% of the frame. Excerpt and pen on the right 58%, between 18% and 76% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = 424B3 excerpt (July 5: reverse-fee proposal); unchanged — never retype it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "THE RISK WAS PRICED" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: people, handshakes, price tags, numbers, cash.
```

**G079 / Beat B104**
РЕЖИССУРА:
Два кропа CMA внахлёст. Справа от них на столе чистый прямоугольный след: места под финальный приказ нет.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — two overlapping documents and, beside them, an empty space where no document lies.
Scene: on a dark desk two paper excerpts overlap slightly, one in front, one behind; to their right a faint clean rectangular outline on the desk marks an empty place — nothing lies inside it.
Layout: headline zone inside the top 45% and left 38% of the frame. The overlapping excerpts at center between 22% and 76% of frame height; the empty outline center-right. The bottom 22% is empty dark charcoal.
Sources: image 1 = UK CMA provisional-findings excerpt (front); image 2 = UK CMA possible-remedies excerpt (behind). Both unchanged — never retype them. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "REGULATORY PRESSURE BECOMES REAL" — the only generated text; off-white distressed condensed sans-serif capitals, three lines, moderate size, short deep-red underline bar beneath it.
Avoid: stamps, flags, gavels, people.
```

**G080 / Beat B105**
РЕЖИССУРА:
По уроку G003: настоящая пробковая доска, три коротких параллельных нити. В начале каждой маленький источник (CMA, Еврокомиссия, DOJ), и все нити обрываются, не дойдя до края.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — a real photographed cork board with three physical threads, not a graphic chart or map.
Scene: three short parallel horizontal threads stacked one above another on a dark cork board; at the left start of each thread one small item is pinned; each thread stops well before the right edge, ending at an empty pin.
Layout: headline zone inside the top 24% of the frame, left half. The three tracks between 30% and 75% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = UK CMA case-page excerpt (top track); image 2 = European Commission Berlaymont (middle track); image 3 = U.S. Department of Justice headquarters (bottom track). All unchanged and small. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "THREE FRONTS" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: track labels, flags, map outlines, gavels.
```

**G081 / Beat B106**
РЕЖИССУРА:
Изменено: заголовок перенесён влево вверх. Эхо G048, но теснее: кроп 8-K крупнее и ближе. Документ узнаётся, но кадр не повторяется.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one tight close-up of the attached document; no roads or mazes.
Scene: a tight close-up of one paper excerpt on warm aged paper, cropped closer than a full page, a thin vertical deep-red bracket in its margin, soft focus falloff at the edges.
Layout: headline zone inside the top 40% and left 38% of the frame. The excerpt fills the right 62%, between 6% and 76% of frame height. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe Form 8-K termination excerpt; unchanged — never retype, redraw or re-letter it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "NO CLEAR PATH" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: underlining inside the document, government buildings, gavels.
```

**G082 / Beat B107**
РЕЖИССУРА:
Настоящая пробковая доска: кроп соглашения о прекращении слева, кроп платежа в 10-K справа. Их соединяет красная нить с бумажным наконечником стрелки.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — a real photographed cork board with two pinned documents and one physical thread.
Scene: two paper excerpts pinned left and right on a dark cork board, joined by one taut deep-red thread ending in a small neat red paper arrowhead touching the right excerpt.
Layout: headline zone = top center, inside the top 22% of the frame. Excerpts between 30% and 76% of frame height, in the left and right thirds. The bottom 22% is empty dark charcoal.
Sources: image 1 = Mutual Termination Agreement excerpt (left); image 2 = Adobe FY2023 10-K payment excerpt (right). Both unchanged — never retype them. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "TERMINATION → PAYMENT" — the only generated text; off-white distressed condensed sans-serif capitals, one line, moderate size, short deep-red underline bar beneath it.
Avoid: labels, cash, people.
```

**G083 / Beat B108**
РЕЖИССУРА:
Тройное отрицание столбцом в три строки слева, справа кроп «not a penalty». Только договор, никаких образов суда, регулятора или покупки.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one attached document and a stacked headline; no court, regulator or acquisition imagery.
Scene: one contract excerpt on warm aged paper lies on a dark desk, held by a black binder clip, a thin vertical deep-red bracket in its margin.
Layout: headline zone = left 50%, between 10% and 70% of frame height. The excerpt fills the right 45%, between 10% and 74%. The bottom 22% is empty dark charcoal.
Sources: image 1 = Merger Agreement Section 8.2 "not a penalty" excerpt; unchanged — never retype, redraw or re-letter it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "NOT A JUDGMENT • NOT A FINE • NOT A PURCHASE" — the only generated text; off-white distressed condensed sans-serif capitals, three stacked lines (one phrase per line, bullets kept), moderate size, short deep-red underline bar beneath it.
Avoid: courtrooms, gavels, government buildings, cash.
```

**G084 / Beat B109**
РЕЖИССУРА:
Резкий кроп 20 июля впереди, размытое здание Еврокомиссии позади. Пункт договора впереди и во времени, и в кадре.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — one sharp document in front of one blurred building print; no fight imagery.
Scene: a paper excerpt lies tack-sharp in the foreground of a dark desk, a thin vertical deep-red bracket in its margin; behind it, heavily out of focus, stands a photographic print of an institutional building.
Layout: headline zone inside the top 35% and left 42% of the frame. The sharp excerpt left-center between 42% and 76% of frame height; the blurred print fills the right background. The bottom 22% is empty dark charcoal.
Sources: image 1 = 424B3 excerpt (July 20: fee agreed), sharp, unchanged — never retype it; image 2 = European Commission Berlaymont, blurred background print, unchanged. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "NEGOTIATED BEFORE THE FIGHT" — the only generated text; off-white distressed condensed sans-serif capitals, two lines, moderate size, short deep-red underline bar beneath it.
Avoid: boxing gloves, fight imagery, gavels, flags, people.
```

**G085 / Beat B110**
РЕЖИССУРА:
Финальная секунда. Крупное название серии слева по центру, справа край кропа Section 8.2 и две крошечные карточки компаний. Рифма с G001.
FINAL HIGGSFIELD PROMPT:
```
Single 16:9 documentary film frame — an almost empty, quiet closing still.
Scene: a deep charcoal field; at the right edge the edge of a contract excerpt on warm paper enters the frame, with two tiny identifier cards resting beside it.
Layout: headline zone = left of center, between 30% and 62% of frame height, large. Excerpt edge and cards at right, between 18% and 72%. The bottom 22% is empty dark charcoal.
Sources: image 1 = Adobe identifier; image 2 = Figma identifier (the two tiny cards), unchanged; image 3 = Merger Agreement Section 8.2 fee excerpt (the paper edge), unchanged — never retype it. A style reference, if attached, sets only the look.
Look: charcoal-black textured backdrop, warm aged paper, low-key directional light, fine film grain, shallow depth of field, restrained deep-red accents, calm and serious.
Headline: "WHAT IT COST" — the only generated text; off-white distressed condensed sans-serif capitals, one line, large, short deep-red underline bar beneath it.
Avoid: cash, gold, people, extra logos.
```
