> Final production-state refresh: **0bc1e6f**. Initial findings at67b940a are historical where superseded. Valve audio technical verification is now complete; full listening/Resolve runtime/final release gates remain open. Four production Shorts. See [final source reconciliation](evidence/repo_refresh_0bc1e6f.md).

# Channel performance, funnel and competing hypotheses
СрезStudio2026-10-10. Channel rangeSep12–Oct9; фильмы sincepublished доNow. [Evidence](evidence/studio_snapshot.json). Все числа UI, K/h округлены. Никаких универсальных норм CTR/retention не принято.

## История и сопоставимость
|Фильм|Публикация|Завершённых календарных дней до Oct9 включительно|Views|Impressions|CTR|Unique|Engaged|Watchh|AVD|APV|
|---|---|---:|---:|---:|---|---:|---:|---:|---|---|
|eBay|Oct4|6|4|11|—;funnel0.0%|2|3|0.3|5:57|NOT AVAILABLE|
|Adobe/Figma|Oct6|4|34|~3.1K|0.5%|19|32|1.5|2:47|17.4%|
|UMG/DistroKid|Oct8|2|14|212|1.9%|2|9|0.3|2:10|NOT AVAILABLE|

Дни в таблице — длина календарного диапазона funnel, не точный возраст в часах. Точные timestamps и одинаковые T24/48/72/7d cumulative НЕ получены. Нельзя ранжировать темы по этим rawtotals; нельзя превращать views/day в контроль одинаковой аудитории. T7 ещё не закончился у всех. Исторические Oct9 значения не подменяют T24.

Channeloverview589views/3.0h. Contentlong52views/~3.3Kimp/0.6%CTR/2:52AVD; Shorts536views/112engaged/1like/20.3%stayed79.7%swiped. Mixedoverview≈91.0%Shortsviews (536/589), не watchtime. Форматные totals588 vs589 — задержки, не скрытый четвёртый фильм.

## Источники просмотра
|Срез|Suggested|Search|Browse|Direct/unknown|OtherYouTube|
|---|---:|---:|---:|---:|---:|
|LongsSep12–Oct9|57.7%|28.9%|3.9%|7.7%|1.9%|
|eBaylifetime|notlisted|25.0%|50.0%|25.0%|notlisted|
|Adobelifetime|85.3%|2.9%|notlisted|8.8%|2.9%|
|DKlifetime|7.1%|92.9%|notlisted|0.0%|0.0%|

Notlisted≠confirmedzero. Доли — по views, не по impressions. Поэтому нельзя объяснить низкий CTRAdobe «85% показов нерелевантным Suggested»: source-specific impressions/CTR отсутствуют. UI действительно показывает среди recommendingcontent разнородные темы (“My Thoughts on Other Mommy”, “How Do Rich North Koreans Live??” и др.), что поддерживает гипотезу неточного initialmatching, но не доказывает её вклад. Adobefunnel54.6% impressionfromrecommendations; это иной знаменатель, чем 85.3%viewsfromSuggested. DKsearchterm“distrokid”23.1% от searchviews; малыечисла, не структура всего US спроса.

Shorttraffic: feed73.5%,search23.0%,otherfeatures3.2%,channelpages0.4%,direct0.0. Округление>100 возможно. Notification/externalshares, counts, exactsourceCTR — NOTAVAILABLE, не нули.

## Воронка без вымышленных знаменателей
|Этап|Измерение|Потеря/неопределённость|Что проверять|
|---|---|---|---|
|Eligibleexposure|NOTAVAILABLE|YT потенциальнаяаудитория не наблюдается|visibility/restrictions/checks; не «штраф»|
|Impressions|long~3.3K;Adobe~3.1K;eBay11;DK212|distribution резко неодинакова|daily bysource+age|
|Click/view|long0.6%CTR;Adobe0.5;DK1.9|Adobe≈99.5% countedimpressions без click, но repeatimpressionscorrelated|однофакторный package тест после текущего|
|Earlyretention|Adobechart, numeric30/60sNOTACQUIRED|AVD не earlyretention; eBay/DKcurvesmissing|retentionexport5/15/30/60s|
|Midretention|NOTACQUIRED|нет drop-offlocations|25/50/75%runtimecurve|
|Watchtime|channel3.0h;Adobe1.5h/AVD2:47APV17.4|33views не означает 33 независимых людей|sourceAVD+impressionwatchtime|
|Subscriberconversion|current0subs;periodnet—|grossgained/lostnotexported; нельзя считать gainrate0 доказанной|grossgains/losses+format/video|
|Returningaudience|monthly111:new99.1/casual0.9/regular<0.1|поведенческиекогорты не точный returningviewerscount|longonlynew/returning+overlap|
|Sessioncontinuation|NOTAVAILABLE|endCTR0%без elementimpressions|elementshown/clicks+destinationviews|

Adobe impressionfunnel:~3.1K→16engagedviews→1:54AVD→0.51h. DK212→4→1:54→0.13h. eBay11→0→—→0h. Эти воронки относятся Oct4–9/6–9/8–9 и не равныобщему AVD(Adobe2:47,DK2:10), так как другое множество зрителей. Не складыватьцелыеобщие views с funnelCTR.

## Неопределённость
Для иллюстрации масштаба, а не формального A/B: Иллюстративные Wilson95% bounds для funnelviews/impressions, НЕ доверительный интервал причинного CTR эффекта: для Adobe16/3100≈0.32–0.84%; DK4/212≈0.74–4.75%; eBay0/11≈0–25.9%. Adobe rounded3.1K/0.5% и engagedfunnel как доступный count делают интервалы приблизительными. Повторные пользователи, разная аудитория/источники и ongoingAB нарушают независимость, поэтому интервалы не доказывают эффект дизайна. Их смысл: у eBay и DK неопределённость огромна. Не использоватькак platformbenchmark.

Крупнейшая измеримая relative потеря на Adobe — clickstage; дальше APV17.4% у 32engagedviews даёт основание проверить удержание. Нельзя на этом основании заключить, что открытие плохое у всех трёх, фильм надо сокращать до 8 мин или что ни одна тема не работает.

## Аудитория и бренд
Monthly111, new99.1/casual0.9/regular<0.1%; targetUS18–35 пока не подтверждён: age/gender и whenviewersonYouTube insufficient. US10.0% видимых views; undisclosedgeoне равноknownnon-US90%. DeviceWATCHTIME:mobile45.5%,computer38.0%,TV10.0%,tablet6.5%. Нельзя трактоватькакviewershare. CCnone72.2%,English1.5%,EnglishUS1.4%, остатокнеобъяснён/неполнаяпанель; это не опрос предпочтений.

WHATITCOST и About дают последовательное business→decision→mechanism→cost. Ниша связная, но abstractpipeDK слабее узнаваемого бренда как гипотеза. Название не менять. Profilebanner/avatarconfigured. Oct10AdobeplaylistSelect, eBay/DKCorporateScandals. Oct9HomeOFF/playlistdeletedcards — историческое наблюдение требует refresh перед исправлением; effectUNKNOWN. Proposedviewerpromise: “The business decision. The hidden mechanism. The real cost.” Не новое название.

## H1–H10: независимые конкурирующие объяснения
|H|Поддержка|Против/ограничение|Не хватает|Confidence и эффект|Дешёвый тест / критерий|
|---|---|---|---|---|---|
|H1 мало impressions|eBay11,DK212|Adobe~3100 ужесигналнизкогоклика|exactsource/agecounts|HIGH для eBay,MEDIUMDK;необщаяпричина|полные dailyexports; считать eBayinconclusive до достаточнойсравнимойэкспозиции|
|H2 слабаяупаковка|Adobe0.5%,DKabstractvisual|recommendingaudience разнородна; совместный AB|variantviews/watchtime/sourceCTR|MEDIUM гипотеза; эффектнеоценим|завершить AB; следующийтестодногофактора,watchtime/impression+AVDguardrail|
|H3 opening неисполняет promise|AdobeAPV17.4, editorial review03|нетчисленных earlycurve; smallN|retention30/60s bysource|LOW causal|будущий 004openingreview+curve; поддержкаесли earlydropaligned и matchedcohortimproves|
|H4 слишкоммного legalcontext|Shortstitles“SummaryJudgment”,“ReverseTerminationFee”;scriptmechanismdense|AdobefeeShort57.1%stayed, legal точностьценность|coldviewercomprehension|LOW|5naiveviewers paraphrase конфликт/ставкипосле 15s,>=4/5 ясно; researchnotgrowthproof|
|H5 темыузкие|DKrecognitionbelowAdobe/eBay|только 3topics не age/sourcecontrolled|topiccohorts/marketexamples|LOW|оставить 004/005; наблюдать 2consumer/2platformstories matchedwindows|
|H6 volume вредит QC|statusesconflict,retries,004notready|частотасама не доказаннаяпричина просмотров|timeledger/backlog/gatedreleasehistory|MEDIUM process;LOWgrowth|2/weekfeasibility4weeks;>=90%gatecompletion,0hardfail,rework<=20%hoursworkingtarget|
|H7 Shorts другаяаудитория|~91%viewsShorts;79.7swipe|нет overlap/attribution|relatedclicks,formatreturning|UNKNOWNcause|14daypairedShorts thenexportattribution; linksalone неуспех|
|H8 обещаниенепоследовательно|playlist/navigationgaps;legalcorrectiontitlescold|About/identity/longtopicsconsistent|coldrecall/continuation|LOW|5viewers сформулируютканал;>=4/5 сходно; navigationQC|
|H9 малоистории|3filmsOct4–8,52views,0subs|Adobe уже clicksignal|4–8 независимых launchcohorts|HIGH ограничение,неоправдание|30daymeasurement; решатьнишупосленесколькихсопоставимыхкейсов|
|H10 technicaleligibility|local/repoQCdriftиз08/03|3public/noNotices;Adobegetsimp|StudioChecksclaimsrestrict/fulluploadedhash|UNKNOWN severeeligibility;нетshadowbanproof|releasechecklist+actualclaims; technicalfixonlyеслиobservedhardfail|

## Частота и время: операционный тест, не algorithm claim
|Cadence|Cost/workload при Ccredits,Hhoursperfilm|Research/QC/testing|Learning|Sustainability|
|---|---|---|---|---|
|Every2days|~3.5C/3.5Hperweek|мало резервного времени без backlog|больше launches,но мало trafficpervariant|неподтверждена;004gatespending|
|2/week|2C/2Hperweek|2–3days между для review|8launches/4weeks с jointlog|условнаяфаза 2 после 14 дней MEDIUM|
|1premium/week|C/Hperweek;premiumC можетвыше|глубже research/archive|4launches/4weeks,медленнопри smallN|резервесли 2/week несдаётгейты|

C/H фактические средние UNKNOWN; ни один вариант не даёт прогноз views. Рекомендуемый после принятия владельцем stagedpilot: первые 14 дней максимум 1 готовый long/week, Friday15:00America/Los_Angeles; затем Tue/Fri2/week только после 2 полных PASS,1 готового backlog и подтверждённого time/costbudget. Это организационное время, не доказанное оптимальное US окно. Порядок 004→005 сохраняется. В аудите календарь не менялся. Productionbudget alternatives in08.

RootcauseCSV: impact1–5 = ожидаемая операционная/учебная ценность, не оценка причинного роста; effort1–5ordinal. Ratio — эвристика. Порядок учитывает risk/confidence и не сортируется исключительно по ratio. P0=измерение/сохранность/расходы; P1=креативныйтест; P2=следующееуточнение.
