# QC и порядок экспериментов

## Приёмка следующего выпуска
Для каждого текущего master и финального cut:
- URI/локальный путь, SHA-256, bytes, ffprobe, provenance до исходных частей;
- полный decode, временные метки, хвост и end screen, без объявления отсутствия black frames доказательством полного визуального QC;
- реальное непрерывное прослушивание, имена/числа, швы, ритм, музыка; ASR и LUFS не заменяют слух;
- normal-speed просмотр открытия, плотной сцены, поворотов, финала и полного монтажа;
- fresh legal status/rights; точные allegation/settlement/ruling distinctions;
- согласованность title/thumb/opening, mobile reading, platform Checks, metadata/timezone/related links;
- независимая проверка конкретной версии, когда reviewer доступен.

Нельзя получить release PASS из таблицы аудита. Итоговые locks/STATE/manifest изменяются лишь в своей production-задаче после фактической приёмки. В этой задаче они не менялись.

## Последовательность
1. E10 — операционный учёт гейтов/часов; не ростовой A/B.
2. Existing native tests: не сбрасывать; сохранить фактические результаты или INCONCLUSIVE.
3. E01 или E02 после существующего теста: один фактор, сопоставимые источники, watch time per impression и AVD guardrail.
4. E03 → E04: concept clarity → первые30s будущего фильма. Одобрение текста не считается доказательством удержания.
5. E07: до30s, contiguous approved audio, consequence-first vs context-first в сопоставимых парах. No separate TTS.
6. E12 после E07: meaningful vertical composition, тот же контент/аудио; без одновременной смены hook.
7. E08 после E12: CTA. E05/E06/E09/E11 позднее при достаточных данных.

Для Shorts теста нужны feed exposures, stayed, engaged и APV; недоступное поле не восстанавливать из views. Шесть пар, рабочий минимум200feedshows и20engaged/Short — не power calculation. Публикационная фаза14дней, T7 последнегоShort доDay21; если мало данных — доDay28 или INCONCLUSIVE. Остальные критерии зафиксированы в ../10_EXPERIMENT_BACKLOG.csv.

Нельзя совместить новый hook, layout и CTA и затем приписать рост одному фактору. Статус READY означает подготовку; RUNNING — только реально начатое наблюдение с датой/версией; COMPLETED требует результат и решение.
