> Final production-state refresh: **0bc1e6f**. Initial findings at67b940a are historical where superseded. Valve audio technical verification is now complete; full listening/Resolve runtime/final release gates remain open. Four production Shorts. See [final source reconciliation](evidence/repo_refresh_0bc1e6f.md).

# Shorts audit — все 26 опубликованных Shorts
Studio2026-10-10; панели sincepublished, contentrowviews могут отставать отanalytics/realtime. Сумма26rowviews=539, channelShorts536 заSep12–Oct9; не принудительносводить разные refreshсрезы. Rawтаблица сохраняется в evidence/shorts_metrics.json.

## Решение: RESTRUCTURE, затем TEST ALTERNATIVE
MEDIUM приоритет: feedstayed20.3%/swiped79.7% показывает проблему на входе агрегированного Shorts потока. UNKNOWN фактический вклад в longform. Не расширять postingvolume по просмотрам Shorts. Нельзя считать 26 коротких роликов 26 независимыми экспериментами.

Восемь DKOct9 опубликованы до Oct10 в одной почасовойсерии; по Studio все PublicOct9. Разная выдержка 4–11h и тема мешают сравнению 8vs1perday. Audit не меняетих metadata/disclosure/frames/сроки. Новая productionpolicyOct8<=30secincludingCTA ужеесть в Git; выпущенные DK48–58s ей не соответствуют по runtime, но нет оснований удалять их или делатьплатныеретейки.

## Каждый Short: наблюдения и конкретное решение
AVD по engagedviewers, stayed имеет feeddenominator, viewsincludesstarts/replays. Engaged/views НЕзамена stayed. APV/complete/rewatch/subgains/relatedclicks — NOTAVAILABLE длякаждого в текущем capture. Формула AVD/duration не выдается за completion.

|Short / link|Length|Views(row)|Engaged|AVD|Stayed|Editorial diagnosis / proposed test|
|---|---|---:|---:|---|---|---|
|[Why $150,000 per Song Is Misleading #Shorts](https://youtube.com/shorts/-OiiiO08A_0)|0:56|4|1|0:21|14.3%|Сильное число; опровержение требует знания исходного мифа. Начать с ceiling≠award, один итог, без нового TTS.|
|[DistroKid Says Universal Has It Wrong #Shorts](https://youtube.com/shorts/og2qxY9qkWI)|0:48|10|1|0:05|9.1%|Название обещает ответ ответчика; оставить конкретную защиту и ясно маркировать dispute, не длинный обзор.|
|[What Happens After a Copyright Warning? #Shorts](https://youtube.com/shorts/R8C_M68osnU)|0:50|12|1|0:05|5.9%|Абстрактный copyrightwarning; назвать distributor и последствие notice в первой фразе.|
|[The Code Behind Every Recorded Song #Shorts](https://youtube.com/shorts/Cc-Y3SP6TvM)|0:52|19|6|0:24|21.1%|Технический ISRC сам по себе слабая ставка; показать duplicateidentifier→конфликт, не лекцию о коде.|
|[UMG Listed 1,000 Alleged Examples #Shorts](https://youtube.com/shorts/jdOfgVUi3SM)|0:49|20|3|0:08|15.0%|1000 examples создаёт масштаб; сразу отличить allegedexamples от findings, затем один payoff.|
|[This Lawsuit Is Not Simply About AI Music #Shorts](https://youtube.com/shorts/GyWdbZu-McY)|0:58|32|4|0:05|11.8%|Отрицательный hook “not simply” +5sAVD; проверить прямой “Why Universal sued the middleman”, без утверждения liability.|
|[The Company Between Artists and Spotify #Shorts](https://youtube.com/shorts/A_aqCuA5feo)|0:56|1|—|—|0%|Spotify узнаваем; почти нет наблюдений. Не признавать проигравшим, проверить ясный intermediarydiagram.|
|[One Account Uploaded 4,562 Tracks in a Year #Shorts](https://youtube.com/shorts/ieXfmBwKxSc)|0:58|7|—|—|0%|4562 сильный конкретный старт;7views/engaged— не тест темы; краткая цепочка uploader→distributor→suit.|
|[What Happened to Figma After Adobe](https://youtube.com/shorts/BB6zlNJ5LfI)|1:14|26|5|0:10|14.3%|Aftermath требует контекста провалившейся сделки; начать independent/public outcome и цену.|
|[$20 Billion vs $1 Billion: The Numbers People Confuse](https://youtube.com/shorts/lp6DwSFjNgw)|1:06|50|10|0:21|16.4%|Числовой контраст понятен; сократить объяснение до proposedprice vsactualfee, один документ.|
|[Three Days Later, Adobe Paid $1 Billion](https://youtube.com/shorts/QkhxStGrOPs)|1:07|13|3|0:12|23.1%|Срок3days+1B конкретен; payoff должен следовать быстро, дата сделки вторична.|
|[How the Adobe–Figma Deal Actually Ended](https://youtube.com/shorts/No4VRNK0jhM)|1:21|89|11|0:22|15.3%|Большеviews≠лучшее качество:15.3%stayed. Вынести mutualtermination beforefinalban в ясную историю.|
|[Pressure Was Real, but No Final “No”](https://youtube.com/shorts/Zv0G8iG7SEE)|1:22|49|5|0:17|8.6%|Абстрактное “No”безбренда;8.6%stayed. Прямое Adobe/Figmaзакрытие, не холодный legalcorrection.|
|[What a Reverse Termination Fee Actually Is](https://youtube.com/shorts/ySfiqde9G_s)|0:56|21|9|0:47|45.0%|45%stayed/0:47AVD на9engaged лучше локально; юридический термин не всегда плох. Проверить упрощённую версию.|
|[Figma Negotiated the $1B Clause Before Signing](https://youtube.com/shorts/eKpwpAzkRSQ)|1:40|8|4|0:06|66.7%|66.7%stayed выглядит высоко, но4engaged/6sAVD из100s. Не выбирать по одному stayed; clausebargaining сократить.|
|[Adobe Paid $1 Billion for a Deal That Never Happened](https://youtube.com/shorts/iiXbDqEzN90)|0:53|24|12|0:26|57.1%|57.1%stayed/26s на12engaged — перспективный локальный контроль:1B/noacquisition ясны. Не объявлять победителем.|
|[What the eBay Harassment Scandal Actually Cost](https://youtube.com/shorts/lvJYXs6qY5s)|0:34|27|1|0:09|3.7%|3.7%stayed/1engaged; genericcostlist. Открывать человеческим последствием+конкретнойcostdistinction.|
|[There Was No $58.7M eBay Award](https://youtube.com/shorts/3E4cFaMxhqk)|0:31|29|9|0:10|33.3%|33.3%stayed; опровергает миф незнакомому зрителю. Сначала twolegalresolutions, потом числа.|
|[What the $55.7M eBay Settlement Actually Was](https://youtube.com/shorts/Gv1WOjpPOhc)|1:02|5|1|0:26|0%|0%feedstayed при1engaged возможен инойsource; не “ошибка”. Unclearaward/settlement distinction дляcoldviewer.|
|[Why Summary Judgment Was Not a Final Verdict](https://youtube.com/shorts/Wvua-Cjxyqw)|0:42|7|1|0:12|12.5%|Summaryjudgment в названии требуетlawknowledge. Перевести stakes: “Why eBay never faced a jury verdict”.|
|[Why eBay Was Charged but Not Convicted](https://youtube.com/shorts/l9JIwcyFl68)|1:11|3|2|0:09|66.7%|66.7% на2engaged не успех; charged≠convictedважно, но сначалакорпорацияvsлюди.|
|[Seven People Pleaded Guilty in the eBay Harassment Case](https://youtube.com/shorts/bn8qQqb7_0M)|1:03|3|—|—|0%|3views/engaged—; guiltypleas конкретныйpayoff, но distributioninsufficient.|
|[The GPS Tracker Attempt in the eBay Harassment Case](https://youtube.com/shorts/7-XFd0-QnDU)|0:37|10|1|0:06|25.0%|GPS человеческий actionhook;6sAVD показывает что досмотр не установлен. Попытка≠успешнаяустановка.|
|[The Internal Messages Behind the eBay Scandal](https://youtube.com/shorts/nAKMi-C6tNY)|0:41|44|11|0:13|25.6%|44views/11engaged25.6%; messages цепляют, но не приписыватькаждомутопменеджерузаказпреступления.|
|[How Criticism Became a Security Operation at eBay](https://youtube.com/shorts/uRrHB-t8oeI)|0:48|6|3|0:19|42.9%|42.9%/3engaged19s — интересныйmechanism, маловато; clarify criticism→securityoperation.|
|[The eBay Harassment Scandal in 60 Seconds](https://youtube.com/shorts/SVHEF0udWqs)|1:06|20|9|0:58|56.3%|56.3%stayed/58sAVD9engaged — локальныйcandidate. “60Seconds”duration66s; не обещатьточнуюминутуеслинесоответствие.|

## Hook, frame, reframing and visual evidence
Название и описания всех 26 проверены непосредственно Studio. Они привязаны к longformcase, но многие объясняют correction/термин, прежде чем дают понятную холодному зрителю ставку. Это editorialhypothesisLOW, а не измеренная причинность. Высокий stayed у FigmaClause66.7% при 6sAVD показывает, почему одного показателя мало.

ActuallocalShortframes/cutmaps inspection см.03 и video_*; если локального Short нет или не просмотрен, openingframe/crop/captionquality длянего NOTVERIFIED. Обложка в channelgrid и первый кадр Shortsfeed — разные объекты; выбранный thumbnail не доказывает хорошую feed остановку. Наличие burnedcaptions не обязательный KPI: действующийвизуальный lock ихнепредусматривает. Тестировать readableEnglishonscreenevidence, а не нарушать lock. Не объявлятьвесьмонтаж плохим поназваниям.

Историческаяпроверка Oct9:18 старых Shorts имеютправильный relatedlong(10eBay/8Adobe),8DK указанына ciFB8WI4sYE. Oct10 повторнаяпроверкавсех relatedsettings не выполнена; значит linkcoverage передновымипубликациямиперепроверить. Отсутствует exportclicks, longdestinationtraffic и overlapformats, поэтому conversionUNKNOWN. Subscriber0current не доказывает 0grosssubscriberconversion каждого Short.

## 14-дневный протокол
Только рекомендация; не запущен. Не изменяет утверждённыйкалендарь.
1. Days1–2: экспорт baseline26, отметить case/id/pubtime/age/length/source/engaged/stayed/APV/grosssubs/relatedclicksavailable. Проверить relatedlinks26/26 без измененияпокааудит read-only. Есликликиневыгружаются, это UNKNOWN во всёмтесте.
2. Days3–14:6 пар новых<=30sShorts изготовых approvedlongs, максимум 1/day12days; contiguousaudio, без separateTTS, рендериз existingassets только при отдельном productionauthorization. Пары однойтемы/похожейдлины/сопоставимых visuals: Acontext-first vsBconcreteconsequence-first; не дублировать один и тот же binary. Сбалансироватьпорядок AB/BA и weekdays, постоянный 15:00LA. Изоляциянеидеальна, обозначить observational.
3. Сниматькаждый T24/72h/7d. Primary stayed rate с feedexposurecount. GuardrailsengagedAVD/APV, nolegaloverpromise, relateddestinationviews/subs если observable. Existinglongcan serveconversiondestination; не обещатьатрибуцию.
4. Минимумрабочий:200feedshowsperShort,20engaged,6pairs. Это learningfloor, не powerproof. Еслине набрано к day14, INCONCLUSIVE и extendobserver до 28days, без volumeincrease.
5. Directionalsuccess: consequence-first лучше>=4/6 пар на>=10percentagepointsstayed, medianAPV нехуже 5pp,0factualhardfails. Это предзаданноеоперационноерешение, не p<0.05. Failure: improvement<=0 в>=4/6 пар либо legalguardrailfail; nofollowonpaidexpansion. Mixed→ещё 3matchedpairs.
6. Conversionseparate: relatedclickrate/destinationwatchtime если export доступен; threshold невыдумыватьбез baseline. Приотсутствииизмеримойпользы через 28days иоперационныхзатратах сократитьдо 2–3 лучших Shorts/long. Не утверждатьчто Shorts вредят longs.

## Что не доказано
Частота 8/day ухудшает distribution; bestpostinghour; Shorts разрушают long аудиторию; повторыполезны;caption обязателен; новый<=30s формат гарантируетрост. Все эти заявления требуют данных. Сравнение старых 53s и 100s свысоким stayed на 4–12engaged не runtimeexperiment.

## Дополнение: непосредственная проверка всех 26 локальных Shorts
Проверены кадры0s,3s,end−1.5s, media probe и SHA-256 каждого. Источники: video_shorts_probe.json и video_shorts_001_contact.png, video_shorts_002_contact.png, video_shorts_003_contact.png; подробности06. Это выборка кадров, не полное слуховое прослушивание.

26/26 используют горизонтальную 16:9 картинку в узкой средней полосе 9:16 с большими чёрными/размытыми областями. У eBay10 мелкие burnedcaptions внутриполосы и крупные genericlabels; Adobe8/DK8 на проверенныхкадрах без burnedcaptions. eBay10+DK8 заканчиваютсяполноэкранной CTA карточкой; у Adobe8 на end−1.5s ещё storypicture, CTA необнаружена ввыборке. Adobe0s часто black/fade, заголовоквиденк 3s; точнаядлительность fade неизмерена. DK часто начинаетабстрактными “THE STORY CHANGES”, “ISRC”, “THIS IS WHERE IT CHANGES”. Этидизайнерскиесвойства HIGHverified; причиннаясвязьс 79.7%swipesLOW. Предложение: meaningfulfirstframe+смысловаявертикальнаякомпоновка изимеющихся assets, безплатнойгенерации; отдельный vertical-layouttest после hooktest, чтобы не смешиватьфакторы.

Фактический T7 для последнего ShortDay14 доступен не раньше Day21. Если feeddenominator или APV не доступны в экспорте, соответствующий тест/guardrail непроверяем: INCOMPLETE/INCONCLUSIVE, а не PASS по просмотрам.
