> Final production-state refresh: **0bc1e6f**. Initial findings at67b940a are historical where superseded. Valve audio technical verification is now complete; full listening/Resolve runtime/final release gates remain open. Four production Shorts. See [final source reconciliation](evidence/repo_refresh_0bc1e6f.md).

# Individual long-form forensic audit

Audit date: 2026-10-10 (America/Los_Angeles). Read-only. Published episodes 001-003;004 receives a separate forward review. No canonical script, metadata, schedule, binary or approved lock changed.

## Evidence and verification limits

Repository checkout67b940a: Foundation locks; Core protocols/gates; storytelling, title, thumbnail and voice bibles; VIDEO_INDEX; each STATE/manifest; complete07_SCRIPT_FINAL text; relevant packaging, upload and QC records. A placeholder file marked NOT_STARTED was not mistaken for a current final. Concrete citations below use canonical episode folders under03_VIDEOS.

Direct inspection of the actual accessible delivery files included SHA-256, ffprobe, decoding the entire file, blackdetect/loudness analysis, selected extracted frames throughout each film, complete opening-frame contact sheets and two full-resolution document frames. This is direct media inspection, **not a full continuous human watch-through**. Motion quality, transitions between unsampled frames, uninterrupted continuity and speech/caption synchronization do not receive PASS.

**AUDIO QUALITY: NOT VERIFIED BY LISTENING.** Harrison's intelligibility, emphasis, pauses, monotony, pronunciation, seams, artifacts and music balance could not be heard in this audit. Objective loudness/decode checks are separately reported and cannot establish auditory quality.

The local delivery files are not automatically byte-identical to YouTube's uploaded source or transcoded version. A server-side upload receipt/source hash is missing. A file called final is not accepted solely on its name; hashes below identify precisely what was inspected. Exact current Studio observations are documented in 01_DATA_INVENTORY and 02_CHANNEL_PERFORMANCE. Creative findings below are not measured causes of audience abandonment.

## Actual binaries inspected

|Episode|Local file|SHA-256|Runtime|Video/audio|Container bitrate|
|---|---|---|---:|---|---:|
|001|C:/YOUTUBE/Youtube 3/Video 1/VIDEO_001_UPLOAD_MASTER_1080P.mp4|512bb6c804ef68d314ba13909fec0c0c84d723dc595148b90ecce88f71351c25|957.370s|H2641920x1080 nominal25fps;AAC44.1k mono|1.869Mb/s|
|002|C:/YOUTUBE/Youtube 3/Video 2/ADOBE FIGMA - FINAL WITH END SCREEN.mp4|fb6e79a32d3f205d75912324de2f11efd309f7a99186c4e80ebb72669fe20b45|960.741s|H2641920x1080 25fps;AAC48k stereo|15.878Mb/s|
|003|C:/YOUTUBE/Youtube 3/Video 3/UMG DISTROKID - FINAL WITH END SCREEN.mp4|d643a4b0bf29fe3b8bccf9984eb4a86f78d3a87b2686caec141286ab528f7204|1008.291s|H2641920x1080 25fps;AAC48k stereo|1.487Mb/s|

Reproducible evidence: [probe](video_media_probe.json), [eBay contact sheet](video_001_contact.png), [Adobe](video_002_contact.png), [DistroKid](video_003_contact.png), `video_inspect.py`, `video_00N_decode_loudness_black.log`. Screenshots were extracted at0,2,5,10,15,20,30,45,60,90,180,300,450,600,750,runtime-25,runtime-5 seconds. The final eBay seek produced no image;16/17 frames exist, not17/17.

|Episode|Measured INPUT LUFS-I|Input true peak dBTP|LRA LU|Decode errors found|Reported black intervals|
|---|---:|---:|---:|---|---|
|001|-16.97|-1.13|2.40|0|0|
|002|-16.79|-3.87|2.30|0|0|
|003|-16.33|-3.31|2.00|0|0|

`blackdetect=d=0.3:pix_th=0.1`, other defaults. This excludes reported black intervals under those thresholds, not every dark image or packet gap. Loudnorm was used with null output for analysis; no normalized production file was written. Bitrate is an engineering observation, not a visual-quality ranking or eligibility test.

##001 - eBay harassment

### Topic, promise and measured evidence

Recognizable company, human targets, physical harassment, documented criminal consequences and a civil settlement create a coherent story. The conflict is understandable without corporate-law knowledge. Relative appeal versus the other topics is an editorial hypothesis, not measured market demand.

Fresh Studio:4 views,11 impressions. Header CTR unavailable; funnel 0 impression-derived views. Engagement AVD 5:57,3 engaged views,approximately 0.3 h. Retention insufficient. Neither strong retention nor weak packaging can be established from this sample.

### Opening 5/15/30/60 seconds

Timing source: delivered `VIDEO_001_SUBTITLES_ENGLISH.vtt`; canonical `VIDEO_001_THE_EBAY_HARASSMENT_SCANDAL_THAT_COST_56_MILLION/07_SCRIPT_FINAL.md` lines19-47. Timed subtitles are alignment evidence, not a fresh listening check.

|Window|Actual narration progression|Actual visual sample|Assessment|
|---|---|---|---|
|0-5 s|August 2019; Massachusetts couple receives strange things|0/2/5 s location map and city collage; bottom captions|Human/location setup, company absent. Not enough evidence to call it a failed hook|
|5-15 s|Insects 6.34 s;threats 7.76 s;pig mask 9.48 s;surveillance/GPS 11.16 s onward|10 s mask;15 s GPS illustration with INSTALLATION NOT ESTABLISHED|Concrete escalation, relevant visual and accurate attempted-installation boundary|
|15-30 s|Not anonymous trolls; eBay security 25.58-29.24 s|20 s GPS layout;30 s eBay security/building|Company reveal arrives around 29 s; clear reversal fulfills scandal promise|
|30-60 s|7 guilty pleas 30.12-36.64; corporate charges/DPA 37.38-52.66; settlement 53.28-61.64|45 s three distinct consequences;60 s 55.7 M settlement package|Dense procedural outcome inventory before the mechanism question. Money promise lands around a minute|

### Narrative and legal integrity

What works: internal messagesS 03 escalate into operationS 05 and obstructionS 06; individual prosecutionsS 07 and corporate DPA S 08 are differentiated;S 09 raises responsibility higher in the organization;S 10 failed initial settlement provides a genuine reversal;S 11 finally explains the package. Strong question/payoff architecture exists.

Legal safeguards: script explicitly attributes Wenig's defense, distinguishes attempted GPS placement, summary-judgment survival from liability, companyDPA from conviction, and settlement from judgment. Packaging's rounded 56 M must remain the 55.7 M total announced CIVIL PACKAGE, not eBay-only payment. Separate 3 M criminal penalty must not become a 58.7 M damages award. eBay announced direct compensation share 46.15 M; executive civil settlement payments do not become criminal convictions.

Documented repetition: S 01 previews all three consequences;S 07/S 08 explain them;S 11 breaks down money;S 12 retells much of the chain. This is a textual observation, not a proven retention mechanism. Future writing can retain one outcome teaser, one financial payoff and one concluding implication. Preserve distinctions at the point a viewer could misread them.

### Picture, captions, delivery and ending

Story-specific maps, buildings, packages, source-document layouts and large headlines are present. At 0/2/5 s the same establishing layout recurs;15/20 s the same GPS layout. This does not prove a lack of animation between samples. Document body at 180/600 s is much harder to read at phone size than its headline. Source/status microlabels need more space. Burned captions are present in sampled frames, below primary graphics. Continuous AV synchronization and motion remain unverified.

**Concrete local technical risk:** ffprobe video-stream duration 952.347578 s versus audio 957.370000 s: difference 5.022422 s. Seek at 952.37 s returned no image. It would be wrong to call this a confirmed online black tail: a player/transcoder may hold the last frame. Check final 10 seconds of the public playback and bind source/hash before any corrective decision. Decode succeeded; blackdetect reported no intervals.

Script endingS 12 lines 363+ connects the cost to the decision to treat criticism as a security problem. It provides a meaningful brand payoff without a premature genericCTA. Sample 932.4 s is still substantive; a dedicated end-screen background was not found in these local tail samples. Clickable YouTube end-screen elements require separate Studio inspection; a background does not establish one.

|What works / fails|Evidence|Confidence|Likely impact|Correction, cost, test|
|---|---|---|---|---|
|Recognizable human conflict|S 01/S 03/S 05;direct visuals|MEDIUM editorial;UNKNOWN demand|Not estimable|Preserve topic; obtain source-qualified impressions before judging demand|
|Outcome-heavy first minute|VTT 30-61.64 s;S 01|HIGH observation;LOW retention causality|Not estimable|Future hook draft in 06;1-2 editor-hours,0 credits;compare first 30/60 s only with adequate retention data|
|Repeated final summaries|S 07/S 08/S 11/S 12|MEDIUM editorial|Not estimable|Future outline: one payoff and one implication; no recut authorized|
|5.02 s stream mismatch|probe+failed tail seek|HIGH local;UNKNOWN online|Release-QC risk|Read-only tail playback and receipt check,about 20 min; accept if reconciled or intentional freeze documented|

##002 - Adobe/Figma

### Topic and performance

The 1 B actual transfer despite failed 20 B acquisition is immediately understandable. Contract risk is a differentiated mechanism; regulatory chronology is supporting context. Familiar Adobe products can bridge less-familiar Figma.

Fresh Studio:34 views,3.1 Kimpressions,0.5%CTR,19 unique viewers;85.3%views Suggested. Engagement 32 engaged,approximately 1.5 h,AVD 2:47,APV 17.4%. Separate impressions funnel 16 views,AVD 1:54,0.51 h uses a different denominator. Retention graph is now available; exact 30/60 s numerical export not acquired. Low observed click conversion is measurable; its attribution to a particular thumbnail element is unproven.

### Opening

Timing source: delivered `ADOBE FIGMA - ENGLISH SUBTITLES.srt`; canonical `VIDEO_002_ADOBE_FIGMA_FAILED_DEAL_COST_1_BILLION/07_SCRIPT_FINAL.md` lines16-40.

|Window|Actual narration|Actual visual evidence|Assessment|
|---|---|---|---|
|0-5 s|20 B purchase proposal 0-3.86;never closed 3.86-5.96|0/2/5 s 20 B PROPOSED /1 B ACTUAL with two source pages|Immediate financial contrast; graphic precedes full spoken explanation|
|5-15 s|1 B paid 6.44-9.08;not government fine 9.08-12.12;not judgment 12.24-14.04|10/15 s highlighted contract clause|Promise fulfilled around 9 s; then categorical corrections|
|15-30 s|not purchase price 14.08-17.48;contractual payment 17.58-27.30;consequence pre-existed failure 27.44+|20 s contractual-exit logos;30 s negotiation source|Nearly 18 s classification after surprise; credible but new dramatic question delayed|
|30-60 s|negotiated before signing 32.84-36.70;pricing risk 37.04-52.92;Figma background 53.32+|45 s PRICING THE RISK;60 s actual product UI|Question partly repeats explained premise, followed by background. Editorial judgment, not measured drop-off|

### Architecture and factual safeguards

S 03 negotiation before signing is substantive evidence. S 06-S 08 regulator concerns and company opposition create competing pressures. S 09 ends by mutual termination before finalUK/EUprohibition. S 10 makes the cash transfer concrete. S 12 independent IPO adds an outcome. These are genuine narrative assets.

Repeated definitions appear inS 01/S 10/S 11/S 13: not fine,not judgment,not purchase. S 11 re-explains 20 B versus 1 B after that distinction appears from frame 0. S 13 restates much of the regulatory/payment sequence. Future scripts can give one short positive definition early and compact context-specific reminders later. Never substitute 'regulators banned the deal' for mutual termination, and do not causally attribute FigmaIPO to termination fee.

### Actual visual/audio/end treatment

Direct frames show source closeups, product interfaces, event image, contract objects and coherent brand type. Full-resolution 10 s clause is legible on desktop; whole paragraph is unrealistic phone reading. The left-side wordFINE is partly outside crop; the meaningful highlighted 1 B line remains visible. Use one readable clause excerpt, not a page-reading task.

**No burned captions were observed in sampled actual delivery frames**, despite old 18_UPLOAD_PACKAGE stating captions were burned. A separate deliveredSRT exists. This is a release-document mismatch; absence of burned captions is not proof of missing optional YouTubeCC. Verify current player track. Quality of music/narration and continuous synchronization remains NOTVERIFIED. Bitrate 15.878 Mb/s does not establish superiority by itself. A proper end-screen background exists at 955.7 s; clickable objects are separately audited inStudio.

S 13 lines 382+ ends with the contractual mechanism, but repeats the chronology and negative definitions. Future version: financial transfer as payoff, one broader implication, then a relevant next-film bridge after the WHATITCOST line. Preserve locked paid content unless a separately approved change is required.

|What works / fails|Evidence|Confidence|Impact|Correction, cost, test|
|---|---|---|---|---|
|Immediate promise delivery|SRT 0-9.08/frame 0|HIGH observation|Retention benefit unknown|Preserve paradox; no speculative revoice|
|Low conversion of shown impressions|3.1 K/0.5%liveStudio|HIGH observation;LOW precise cause|Measured bottleneck;uplift unknown|Preserve runningA/B;future alternative brief in 06,1-3 hours existing-assets work|
|Repeated category corrections|S 01/S 10/S 11/S 13|HIGH repetition;LOW retention causality|Not estimable|Future positive definition once;export exactcurve first|
|Caption state differs from upload document|actual frames vs 18 Upload|HIGH local mismatch|Traceability/verification risk|Current playerCCcheck;exactrelease receipt,20-40 min,0 credits|

##003 - Universal Music/DistroKid

### Topic and performance

The distributor between creators andSpotify is an unexpected defendant. The actual allegation concerns conduct and rights notices; a blanketAIban angle would misrepresent it. DistroKid recognition is likely narrower thanAdobe/eBay, but that is a familiarity hypothesis, not a measured audience-size conclusion.

Fresh Studio:14 views,212 impressions,CTR 1.9%,2 unique viewers from Reach;92.9%viewsSearch. Engagement 9 engaged,approximately 0.3 h,AVD 2:10;curve processing. Separate funnel 4 views,AVD 1:54,0.13 h. Different latency/windows mean 14 views/2 unique cannot be called 7 rewatches. Approximately 4 impression-derived views do not establish a better package thanAdobe.

### Opening

Timing authority: `VIDEO_003_UMG_DISTROKID_AI_COPYRIGHT_LAWSUIT/11_WORD_TRANSCRIPT.csv.gz`; canonical2391tokens aligned97.78%DIRECT and2.22%interpolated. S01=0-54.600s;S02=55.460-138.640s. This is existing alignment,not new auditory verification.

|Window|Narrative state|Actual visual evidence|Assessment|
|---|---|---|---|
|0-5 s|One account,4562 tracks,twelvemonths|0/2 s count+complaint;5 s overlapping transition|Concrete number;music context initially implicit;claimant attribution follows|
|5-15 s|UMGsays;not only uploader;distributor sued|10 s UNIVERSAL SAYS IT HAPPENED;15 s WHY DISTROKID?|Claimant and defendant identified, no guilt claim|
|15-30 s|DistroKid routes toSpotify/Apple/TikTok/150 destinations;notice allegation starts|20 s middle-company routing diagram;30 s complaint|Familiar destination bridges unfamiliar service;several ideas accumulate|
|30-60 s|continued distribution allegation;denial/no merits decision;warning question;S 02 repeats service premise 55.46 s|45 s NO RULING YET;60 s UPLOAD ONCE|Fairness integrated;after question, narration restarts previously explained routing|

### Narrative, repetition and ending

S 05 recording identifiers andS 06 notice introduce concrete mechanisms. S 07 gives DistroKid's opposition. S 08 distinguishes conditional 150 K-per-work maximum from award. No fabricated aggregate damages and no dishonest declared winner. These protect credibility.

Repeated exposition is substantial: S 01 route;S 02 route/150 destinations/importance of middle layer;S 03 AIban correction;S 04 complaint-not-findings;S 08 damages caveats;S 10 dated docket limitations;S 11/S 12 middle-layer summaries. This is documented structural repetition,not causal retention evidence. Future story should use one sourced upload/notice/action sequence, explain only the rule needed at that beat, and place brief caveats where inference changes. Do not invent an accessible email, track, uploader identity or response.

S 11/S 12 provide successive open-ended summaries. Conditional outcomes are honest but can feel less resolved than a completed case. Future payoff: what precisely must be proved, visualized as three evidence checkpoints, then one broader implication. Do not promise a court answer that does not yet exist.

### Direct visual/edit inspection

Actual 0/2/10/15/20/30/45/60 s graphics support the spoken argument;983.3 sBATTLEGROUND and 1003.3 send-screen match ending. Most sampled midpoints use dark-paper/document/headline stages. The visual function is often assertion illustration rather than showing a changed system state. This is an editorial finding,not a claim viewers dislike documents.

Two readable headlines overlap at 5 s and 750 s sampled crossfades. Duration of overlap is unknown without continuous playback. Future edit: clear old headline before new one becomes readable; no shake/crop jumps required. Fullres 30 s shows accusatory complaint text under MORE THAN A BAD UPLOAD without a visible persistent COMPLAINT/ALLEGATIONS label. Script attributes the allegations and 45 s says NO RULING YET; therefore do not declare a proven legal violation. A source/status line on such evidence frames would reduce ambiguity,especially in extracts.

Large headings readable; full complaint paragraphs unsuitable for phone reading. No burned captions observed in sampled frames;YouTube CC state not established.1.487 Mb/s container/video 1.293 Mb/s warrants careful full-resolution playback of texture/documents,not a qualityFAIL or eligibility diagnosis. No encode change performed.

|What works / fails|Evidence|Confidence|Impact|Correction, cost, test|
|---|---|---|---|---|
|Notice-focused differentiating angle|S 01/S 06/S 11|MEDIUM editorial;UNKNOWN demand|Not estimable|Preserve legal mechanism;future case framed around a real disputed decision|
|Abstract pipe packaging requires context|direct local variants;current live binding ininventory|HIGH design property;LOW CTR cause|Not estimable|Recognizable upload-chain variant 06;runningA/Bpreserved|
|Routing repeats after coldopen|S 01/S 02;55.46-138.64 s|HIGH text;LOW audiencecause|Not estimable|Future outline merge,1-2 hours;early retention export required|
|Twoheadline transition overlap|actual 5 s/750 s|HIGH frame;UNKNOWN duration/effect|Readability risk|Future frame-by-frame transitionQC,about 0.5 h|

##004 - Steam/Valve forward review

This is not a published-video performance verdict. CanonicalV11 `VIDEO_004_VALVE_STEAM_MASS_ARBITRATION/07_SCRIPT_FINAL.md`S01lines11-31: customers fear license implications;Valve gives opposing position;claimants become defendants;Valve seeks to stop arbitrations;oneclick question. It starts with a recognizable product and contract reversal before doctrine. Textual meritMEDIUM;measured retention UNKNOWN.

Actual `C:/YOUTUBE/Youtube 3/Video 4/VIDEO004_HARRISON_V11_MASTER.wav` exists;production reviewer checks provenance/status. No finalvideo in that delivery folder;visual5/15/30/60s cannot be assessed. Internal90.4/100rubric is not90.4%retention or audience validation. Manifest/STATEdrift belongs to08report.

Future edit guardrails without reopening paid audio:

1.S 04 lines 73+ introduces unverified 20 M to rebut it. Show UNVERIFIED simultaneously;never make it a packaging promise.
2.S 13 preserve emergency-request scope;no 'Valve lost antitrust case' or automaticgame-license-loss claim.
3.Date 4991 claimants toMay 2026;not currentactive count.
4.Preserve produced Harrison assets;this audit authorizes no new paid voice/image/video jobs.

##Cross-video verdict and adversarial review

HIGH: introductions are story-specific,not generic channel branding;legal distinctions are substantive;actual sampled visuals are relevant;full local decodes clean. Release-documentdrift and 001 stream-duration mismatch are concrete findings.

MEDIUM editorial: repeated corrective definitions and successive ending summaries offer room to condense future scripts;source pages need selective large callouts forphone.

LOW/UNKNOWN causal claims: these decisions explainAVD;Harrison is boring;faceless format fails;all films need 8 minutes;new channel is suppressed. None established. Do not mass re-render,revoice or reupload. Preserve native A/B tests,obtain exact retention,verify release receipts,then apply learning to future authorized production stages. Lack of a full watch/listen-through remains a material limitation,not a completed creativeQC PASS.

## Final reconciliation: exact Studio-named DistroKid HQ candidate

Studio's filename is UMG_DISTROKID_FINAL_ENDSCREEN_YOUTUBE_FINAL_HQ.mp4. The exact-name candidate was located in C:/Users/KK/Downloads, and was independently inspected; it is NOT byte-identical to the initially inspected spaced-name delivery file. This section supersedes that earlier candidate for release-file technical conclusions.

- SHA-256: f2b4a827a1feb78e54e9766952b34d25c713b6236e046667921c23203b3ea037.
- Size188,989,202 bytes; container duration1008.422031s; H.2641920x1080,25fps,25,210frames, video bitrate1,304,321bit/s; AAC48kHz stereo188,905bit/s; container1,499,286bit/s.
- Filename matching plus local provenance is stronger evidence than the former candidate, but no source upload hash/receipt was available to prove byte identity with the actual server upload. No online-transcode verdict is inferred.
- Measured input loudness -16.32LUFS-I, true peak -3.31dBTP, LRA1.90LU. Audio NOT VERIFIED BY LISTENING.
- Exact-name frames at0/5/15/30/60/300/600/750/983/1003s were directly inspected by the lead. The same authored document scenes, overlap of outgoing/incoming headlines at5s and750s, and end-screen background at1003s are present. Whole complaint paragraphs remain too small for mobile reading; the large labels are clear. No burned subtitles were present in these sampled frames. This is sampled visual inspection, not continuous playback or audio-sync certification.
- The original filtered full-decode log reached25,210frames but emitted a non-monotonic DTS warning at the null output muxer. That warning must not be silently erased or equated with a damaged source. A separate passthrough full-decode verification is recorded in video_003_actual_hq_decode_errors.log; status is documented in the final integrity report.
- A low bitrate alone is not a quality FAIL, eligibility defect or demonstrated cause of retention loss. No master was replaced or reuploaded.

Evidence: [probe](video_003_actual_hq_probe.json), [exact-name contact sheet](video_003_hq_contact.png), [original decode and loudness log](video_003_actual_hq_decode.log), [passthrough errors](video_003_actual_hq_decode_errors.log).

## Exact HQ timestamp finding — final verification
ffprobe decoded all25,210video frames. Two non-increasing best-effort timestamps are present: frame24710 goes from988.502031s to988.462031s; frame25207 repeats1008.302031s. The null-output DTS warnings therefore have a corresponding source decoded-timestamp anomaly and are not dismissed as merely harmless muxer noise. No codec corruption was reported, but this exact candidate does NOT receive a blanket timing-cleanPASS. Check real playback around16:28 and the lastsecond, then compare uploaded/player behavior and retained source before considering any repair. This audit performs no encode/reupload. Evidence: evidence/package_integrity.json and video_003_actual_hq_decode_errors.log. Audio remains NOT VERIFIED BY LISTENING.
