> Final production-state refresh: **0bc1e6f**. Initial findings at67b940a are historical where superseded. Valve audio technical verification is now complete; full listening/Resolve runtime/final release gates remain open. Four production Shorts. See [final source reconciliation](evidence/repo_refresh_0bc1e6f.md).

# Инвентаризация источников
Срез2026-10-10; canonical origin/main67b940a. Сырые тексты: evidence/studio_snapshot.json. Это authenticated Studio, не публичные счётчики. Отдельные UI sections since published обновляются быстрее/медленнее; не следует складывать их как одну транзакционную БД.

|SOURCE|ACCESS STATUS|DATE RANGE|AVAILABLE METRICS|DATA QUALITY|LIMITATIONS|
|---|---|---|---|---|---|
|Studio channel Overview|AVAILABLE|Sep12–Oct9|views589,watchhours3.0,subscriber display—,realtime current0subs|HIGH для отображённого среза|rounded, processing, realtime иной период|
|Studio Content Videos|AVAILABLE|Sep12–Oct9|views52,impressions3.3K,CTR0.6%,AVD2:52,trafficshares|HIGH observed; LOW причинные выводы|нет source-specific CTR/impressions точных|
|Studio Content Shorts|AVAILABLE|Sep12–Oct9|views536,engaged112,stayed20.3%,swiped79.7%,sources|HIGH observed|stayed denominator не totalviews|
|Studio Audience|AVAILABLE|Sep12–Oct9|monthly111;new99.1/casual0.9/regular<0.1;device/geography/CC|MEDIUM|privacy suppression; часы активности и demographic unavailable|
|3 longform Reach|AVAILABLE|Oct4/6/8–now|11/3.1K/212imp;—/0.5/1.9CTR;4/34/14views;2/19/2unique;funnels;ABstatus|HIGH observed|разный возраст; uniques delayed; rounded|
|3 longform Engagement|AVAILABLE|since published|3/32/9engaged;0.3/1.5/0.3h;5:57/2:47/2:10AVD;AdobeAPV17.4|HIGH observed|views≠engaged; cannot derive watchtime as allviews×AVD|
|Retention eBay|NOT AVAILABLE|lifetime|Studio insufficient data|UNKNOWN|export later when available|
|Retention Adobe|PARTIALLY AVAILABLE|lifetime|chart visible, AVD/APV|MEDIUM|numeric 5/15/30/60/mid/end not acquired; no invented curve|
|Retention DK|NOT AVAILABLE|lifetime|processing notice|UNKNOWN|may take2days|
|26Shorts Engagement|AVAILABLE|sincepublished Oct4–9|eachengaged/AVD/stayed; allIDs and lengths|HIGH observed|APV unavailable in captured panels, no completion/rewatch data|
|Shorts→long attribution|NOT AVAILABLE|history|relatedlinks previously inspected, no measured clicks/export|UNKNOWN|a link is not conversion|
|Endscreens|PARTIALLY AVAILABLE|lifetime|all0.0%display; elements historicalOct9|LOW effectiveness|elementimpressions/clickcounts missing; Oct10not reverified config|
|Current longform details|AVAILABLE|Oct10|public, filenames, descriptions/chapters, playlists, ABtitles|HIGH|DKlivevisual inspected WHOOWNS THERISK; allvariant images not fully captured|
|Channel customization Profile|AVAILABLE|Oct10|name/handle/About/banner/avatar configured|HIGH textual|HomeOFF andplaylistdeletedcards observedOct9 only, notfreshverified|
|YTAnalyticsAPI|NOT AVAILABLE|—|no connected OAuth exporter found|UNKNOWN|do not call public totals private analytics|
|Historical age-matchedsnapshots|NOT AVAILABLE|T24/48/72/7d|publicationdates+currentcumulative only|UNKNOWN|don't reconstruct from cumulative totals|
|GitHub canonical repo/history|AVAILABLE|through67b940a|locks/scripts/QC/ledgers/states/index/thumbs/cutmaps|HIGH existence; mixed consistency|manifest/status drift; productionfilesystem separate|
|Delivered local media|AVAILABLE, scope in03|Video1–3 masters|ffprobe/decode/frame samples/loudness measurements|HIGH technical where checked|local delivery does not prove byteidentity to YouTube transcode; audio auditoryNOTVERIFIED|
|Competitor public pages/Nexlev|AVAILABLE with cap|liveOct10|titles/cards/views/runtime/channelcounts|MEDIUM|relative reconstructed publishdates excluded; privateanalytics unavailable; freequota reached, no upgrade|
|Credits/time accounting|PARTIALLY AVAILABLE|ep001–004 repo ledgers|episode retries/submissioncounts/quotedcredits|MEDIUM|no complete channel invoice/timeledger; averagechannelcostUNKNOWN|

## Publication and source precedence
Studio confirms all001–003 public. Index lists Oct4/6/8 respectively,004IN_PREPARATION Stage08. 004STATE/manifest disagree in progress detail;005plan is not a verified publication. Repo status text is not proof a paid download or listeningQC completed. See08.

Brand source: Profile about promises hidden business stories, lawsuits/deals/failures and expensive consequences. Good semantic fit with locks; visible EnglishUS, no proof achieved18–35 target because demographics suppressed.

Only analytical files are changed in this package. No metadata, disclosures, schedules, masters, scripts or generations changed.

## Data safety
Studio private metrics are being written to the owner-designated repository as expressly requested. No Gmail/X content collected. AdsPower profile used only to read Studio. Public competitor counts are never substituted for StudioCTR/retention.

Локальное дополнение004: найден VIDEO004_HARRISON_V11_MASTER.wav,808s,48kHz/24bit/stereo; SHA2568c11be2619a6a84b7e1a6cbe0cb8c708d72dff556d1d737dd46f596ea21f65d7. Это кандидат: связь с providerparts, полныйdecode и слуховойQC не подтверждены. Репозиторноеpending не означает, что файла нет. Сначала проверить кандидата, а не повторять генерацию.
