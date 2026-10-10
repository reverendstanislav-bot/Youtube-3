> Final production-state refresh: **0bc1e6f**. Initial findings at67b940a are historical where superseded. Valve audio technical verification is now complete; full listening/Resolve runtime/final release gates remain open. Four production Shorts. See [final source reconciliation](evidence/repo_refresh_0bc1e6f.md).

# Какие данные ещё нужны
Ничего не требуется, чтобы прочитать и использовать уже завершённый аудит. Этот список повышает уверенность следующего решения; недоступные значения не заполнены догадками.

|Приоритет|Данные|Где получить|Точный состав и зачем|
|---|---|---|---|
|P0|Longform daily/by-source exports|StudioAnalytics→Advancedmode→ContenttypeVideos→Date/Trafficsource→ExportCSV|videoID,publishedtimestamp,date,views,impressions,CTR,engagedviews,watchtime,AVD,APV; age/source normalization|
|P0|Retention3films|Eachvideo→Analytics→Engagement→AudienceRetention→Seemore/export whereoffered; ifnotexportable capturetimestamps|5/15/30/60s,25/50/75%,end, absolute/relativecurve and daterange; Adobechartavailable; eBayinsufficient; DKprocessing|
|P0|Shorts26export|ChannelAnalytics→ContentShorts→Advancedmode→Content/Trafficsource/export|showninfeed/feedopportunities,stayed/swipedcounts,engagedviews,AVD,APV,watchtime,grosssubs;200showfloor otherwiseunmeasurable|
|P0|Artifact/release identity|Localdelivery+uploadmanifest+Studiofilename|exactpath/hash/bytes/probe/releaseURL+actualuploadedhashifretained; localmedia≠YTtranscodeproof|
|P0|004paidjobdownloads|existingproviderjobhistory anddownloadlinks, nojobs|first verify existing808sWAV candidate/hash/sourceparts;3jobIDs/costs/availablefiles/concatprovenance/audioQC;avoid duplicatepaidretry|
|P1|A/B completion report|Eachvideo→Reach→A/Btest→Viewreport|start/end,3packagevariants,exposure/WTshares,winner/confidenceifprovided; currentallinsufficient|
|P1|End-screen counts|VideoEngagement→EndscreenSeemore→Advancedmode|elementimpressions/clicks/destination,notjust0.0%; actualeBayconfigfreshverify|
|P1|Shorts→long conversion|Advancedmode traffic types including Shorts/relatedvideo surfaces ifexposed|relatedclicks, destinationviews/WT,dates/videoIDs; ifnotexposedwriteNOTAVAILABLE, noinventedattribution|
|P1|Gross subscriber gain/loss|Advancedmode→Subscriptionstatus/source→CSV|gained/lostpervideo/format; net—cannotprove0grossgains|
|P1|Returning/overlap|Audience→formats/viewersacrossformats; new/returning exportifavailable|longvsShortscohorts,overlapcounts; monthlyaudiencecategoriesnotexactreturningcount|
|P1|Productionhours/invoices|timeledger/providerinvoices/debitexports|episode/stage/hours/attempt/jobID/credits/refund/rejectionreason; channelmeanotherwiseUNKNOWN|
|P2|Geography+demographics/device split|AudienceAdvancedmodeexportVideos/Shortsseparately|USviews/WT/CTR/ageifprivacyeligible; suppressed≠non-US|
|P2|Publishingtimestamps timezone|Studiocontent+Stage18ledger|Pacific vsbrowserGMT−0600; exactT0 forfuture24/48/72/7d|
|P2|Competition open/audio samples|publiclawfulvideo review/captions whenavailable|competitorfirst60s/fullstructure; currentlyfullscriptcomparisonNOTVERIFIED|

Нет обязанности запускатьплатный API илипокупатьаналитику. Если интерфейс не предоставляет экспорт, сохранить датированный скрин/текст, нужный timestamp и честно NOTAVAILABLE. Метрики в YouTubeAnalyticsAPI могуттребоватьотдельного OAuth; publicDataAPI не заменяет retention/CTR.

## Шаблон наблюдения
videoID | T0timezone | snapshotUTC | agehours | contenttype | topicpillar | title/thumbversion | daterange | source | impressions | CTR | views | engagedviews | WT | AVD | APV | retention30/60s | grosssubs | endshown/clicks | relateddestination | availabilitynotes.
Версионироватьпослеправок, не пересчитыватьстаруюупаковкуподновымименем. Рабочиепорогиисследования в 10 не статистически рассчитанная power и не нормы YouTube.
