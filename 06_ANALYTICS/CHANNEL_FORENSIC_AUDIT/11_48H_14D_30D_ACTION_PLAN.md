> Исполнение поручено владельцем 2026-10-10. Рабочий статус, реестры и проверка: [IMPLEMENTATION](IMPLEMENTATION/README_RU.md). Перечень ниже остаётся планом; фактическое выполнение отмечается отдельно, без ретроспективного PASS.

> Final production-state refresh: **0bc1e6f**. Initial findings at67b940a are historical where superseded. Valve audio technical verification is now complete; full listening/Resolve runtime/final release gates remain open. Four production Shorts. See [final source reconciliation](evidence/repo_refresh_0bc1e6f.md).

# План на 48 часов,14 дней и 30 дней
Это план для принятия владельцем. В ходе аудита ничего не опубликовано заново, расписание и канонические материалы не менялись. Confidence: HIGH необходимость проверок; MEDIUM операционный режим; LOW прогноз влияния творческих решений на рост.

## Следующие 48 часов
|Действие|Исполнитель|Acceptance criterion|Стоимость/зависимость|
|---|---|---|---|
|Сохранить исходные exports Studio по всем 3long/26Shorts|аналитик|CSV с диапазоном, часовым поясом, ID, source и denominator; список отсутствующих полей|0 paid credits; requests13|
|Проверить release evidence для 001–004|release/QC|каждый master связан с URI/hash/probe/decode/listeningreview; unknown отдельно; нет новых ложных PASS|0 generation; затраты времени|
|004: сначала проверить существующий 808sWAV и связать его с 3providerjobs; скачивать/собирать заново только при необходимости|audio/QC после отдельной productionauthorization|3jobIDs без дублей; доступные audiofiles; ffprobe+listening+seamcheck; gatePASS или аргументированный FAIL|не запускать новые paidjobs пока старые не восстановлены|
|Проверить eBaytail на actualuploaded/player без изменения|mediaQC|описано поведение последних 10s; local5.02s mismatch связан или не связан с uploadedartifact|нет reupload без отдельного решения|
|Refresh Home/playlists/end-screen configuration|publisher readonlyinspection|таблица актуальных элементов/доступныхвидео/404; plan конкретныхправок|исторические Oct9 наблюдения не считать current|
|Не перезапускать текущие совместные A/B|аналитик|сохранены 3 варианта/остатоквремени/статус; winners невыдуманы|enddates ~Oct18/20/22 уточнить Studio|
|Подготовить opening/thumbnail concept004 без assets|editor/legal|5coldviewers:4/5 понимают Steam, конфликт и ставку; legalPASS; ownerdecision если canonicalchange|0 generation; rubric06|
|Согласовать phasedcadence|владелец по готовому capacityplan|зафиксировано решение: принять pilot или сохранить calendar с признанными рисками|audit не меняет calendar|

Уже запланированное не сдвигать автоматически. Новые дорогие визуальные партии рекомендовано удержать до проверки готовности аудио/выгрузок и representativeframe; это рекомендация, не выполненная остановка чужих jobs.

## Дни 1–14: стабилизация
Рекомендуемый ограничитель после принятия: **не более 1 premiumlong/week**, в порядке 004→005, только с полными gate evidence. Временной ориентир Friday15:00America/Los_Angeles — организационный, не оптимум алгоритма. Не обещать Oct10 готовый 004, когда мастер/QC ещё не подтверждены.

|Поток|Действие|Acceptance criterion/decision|
|---|---|---|
|Production|закрыть 2 последовательных release без hardfail; ежедневный timeledger по этапам|2 полных PASS до publish, фактические credits/hours, rework отделён; еслинеготово, FAIL честно|
|Analytics|T24/48/72/7d для каждого новогофильма|одинаковые agewindows, source-specificimpressions/CTR/AVD/retention; no invented past|
|Packaging|датьсуществующим AB закончиться, затем выбратьодинследующий factor|nativeplatformresult или INCONCLUSIVE; не использовать 0.5%как доказательствоплохого thumbalone|
|Openings|review004/005 по 5/15/30/60s; numericretentionexport при eligibletraffic|проверен promise→stakes→question; 30/60s values либо NOTAVAILABLE; не склеивать fictionfacts|
|Shorts|6matchedpairs по 04, максимум 1/day12days,<=30s, relatedlong|200feedshows+20engagedminimum/Short еслидоступны; иначе INCONCLUSIVE/extend; никакойгарантии day14|
|Brand/navigation|после freshinspection предложитьконкретные Home/playlist/end-pathchanges|owner-approvedchecklist и screenshotbefore/after толькоесли отдельно выполнено|
|Topics|004/005 неразблокировать молча; nextcandidates07review|для top5 есть primarysources/legalangle/costassumptions; ниоднойгенерации|

Не тестировать одновременно opening, runtime, voice, thumb, title и cadence как одну причиннуюпроверку. Пилот QC можно вести параллельно с observationalanalytics, но он не докажетпричинуизмененияпросмотров.

## Дни 15–30: условный разгон
Переход к Tue/Fri15:00LA **2longs/week** только если:2 последовательных release полностью PASS, есть 1 готовыйпроверенный longbacklog, доступный timebudget покрывает 2H/неделю+20%reserve, spendingledger полон. Еслиусловияне выполнены —1/week; every2days пока неподтверждённая capacity.

|Действие|Acceptance criterion|
|---|---|
|Сопоставитькак минимум4новыхlaunchcohorts наT7 гдеуспели|таблицаage/source/packageversions; отсутствиеsample обозначено; выводыбезshadowban|
|Рассмотреть packageexperiment после ongoingAB|E01/E02 не одновременно; predefinedguardrails; INCONCLUSIVE разрешён|
|Выбратьследующуюпосле 005 историю|07weightedmatrix+freshprimary-sourcecheck+productionbudget,ownerapprovalcanonicaltopic|
|Ресурсы|initialworkingallocationhours: research/legal30%,script/opening20%,visual/edit30%,QC/packaging/analytics20%; не invoice/не факт|
|Shortsconversion|exports relatedclicks/destinationwatchtime/grosssubs; еслинет —UNKNOWN; решение reduce/continue пооперационнымзатратам+engagement|
|Cadencereview|0technical/legalhardfails; минимум 90%scheduledgatesontime; <=20%reworkhoursworkingtarget; реальные credits/film|
|Strategyreview|keepnicheunlessrepeatedtopic/source/ageevidence; не broadpivot поодномууспехуилипровалу|

## Критерии продолжить / изменить / отменить
Продолжить нишу и QC-план при росте качества доказательств и отсутствии hardfails. Сохранить 2/week только при capacityPASS. Изменятьупаковку если nativeAB crediblewinner или повторяемый directionalWTI с guardrails; отменятьконкретныйтестпри legal/accuracyfail. Если 30 дней traffic мал — заключение **INCONCLUSIVE**, а не «ниша мертва». Полный contentpivot рассматриватьлишьпосле несколькихсопоставимых consumer/platform и industry кейсов, источников изатрат; не заданмагический views порог.
