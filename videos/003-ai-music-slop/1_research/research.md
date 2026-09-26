# Research — He Did the Math on Fake Streams (U.S. v. Michael Smith → UMG v. Believe/TuneCore → UMG v. DistroKid)

## Researcher response — round 1 (2026-09-26)
| # | Gap | Result |
|---|---|---|
| 1 | Oct 6 sentence | **NOT FINDABLE YET.** The event is 10 days in the future. Script lock stays on hold. On 2026-10-06/07, pull the DOJ SDNY release, the Judgment (RECAP 24-cr-504) and MBW/Billboard/Music Ally/RS. Fields: prison/probation, supervised release, fine, restitution (amount and payee), surrender date, disposition of the indictment counts, appeal waiver, reported remarks from the bench. |
| 2 | Government sentencing submission | **NOT FINDABLE YET.** Searched again 2026-09-26. It is not filed or reported, and the due date (Sept 28/29) has not arrived. Refresh on or after 2026-09-30. Caution added to C060: reprints saying "federal officials recommended two years" mean the Probation PSR, not the prosecutors. |
| 3 | Dkt. 57 memo + Dkt. 55 plea transcript (PACER) | **BLOCKED: owner spend approval needed.** No agent can buy from PACER. Cost is about $0.10/page, capped at $3.00 per document. Until then C053–C056 stay "according to Billboard". |
| 4 | Human on the "paid" side | **PARTLY DONE.** (a) MLC CEO **Kris Ahrend**'s verbatim 2024 statement ("withheld payment of the associated mechanical royalties") found in S027 → C095, E022. (b) **Amount the MLC withheld: not public** (C096). (c) **Michael Lewan**, exec. director of the Music Fights Fraud Alliance, is a named on-record voice answering "no perceptible harm" at industry level (C105). (d) No songwriter/artist-org statement on the case (NMPA, SONA, ARA, Recording Academy) was found (C107). |
| 5 | Who paid | **DONE as far as the record allows.** Spotify's *first* statement was 2024-09-12 ("able to **game** from Spotify", S043), restated 2025 (S035). DMN reports **Apple Music, Boomplay, Tidal, YouTube and Amazon Music** gave "radio silence". SoundCloud gave no figure (C097–C098). The bulk payer remains unknown (C043). |
| 6 | Backstory corroboration + S028 date | **DONE.** S028 = Rolling Stone, **January 2026** (Jon Blistein; display title "'Fake as F-ck': The Wannabe Rock Star Accused of Scamming Streamers"). The Oct 6 "trial" date in it was a trial date later reused for sentencing, so the source is no longer internally inconsistent. One Shot is independently confirmed by S047 (Music Connection, 2016-05-17, with a Smith quote). The jazz No. 1 is confirmed by S048 (promo source, "when they reported their digital album presales"). The Billboard chart-history page for the AC No. 35 was not retrievable (the name collides with other artists called Mike Smith), so it stays RS-only. |
| 7 | Competitor novelty from content | **NOT FINDABLE with my tools.** YouTube pages return no description or transcript to WebFetch, and search has no text for them. **Dispatcher:** run yt-dlp `--skip-download --write-description --write-auto-subs` on gi0QzXFLjLY, 5z3aviP-vGk, ieNa6VcTUzs, zgQ9TparK_A, then grep for: "371", "five years", "cannot be located", "October 6", "still release it", "Master Services", "human author", "debit", "60,000", "ocean". |
| 8 | Arrest scene | **DONE (partial).** Arrested Wednesday morning, 2024-09-04, at home in Cornelius outside Charlotte, to be presented before a U.S. magistrate judge in N.C. (S045, S028). The NY docket logs Rule 5(c)(3) papers from W.D.N.C. plus an unsealing order by M.J. Figueredo (S019 search text; verify). Lawyer declined / did not reply (S027, S046). W.D.N.C. case number and anything said at the appearance: not found. Street address is in S045 and must never be used. |
| 9 | 2020-08 → 2023-03 hole | **DONE: no scene exists.** A full re-read of S006 finds only three dated items: 2020-08-17 "10x-20x better" (E016), 2020–2023 $1.3M debit-card transfers (undated individually, E017) and 2023-03-03 Distribution Company-2 representation (E018). No date is given for the 10,000-bot peak (¶11(c)). **Writer: compress into one summary passage** (quality up, card money cycling, the machine running), then cut to the MLC in March 2023. |
| 10 | People and place visuals | **(a)** Getty (Bennett Raglin, 2016-08-22 One Shot screening) needs an owner license decision; no price was retrievable. A Wikimedia Commons file "Mike Smith BET One Shot DJ Khaled.jpg" (CC BY-SA 4.0) exists, but its provenance is unverified (uploader "own work", no permission ticket) → S050, **owner must view and decide**. **(b)** Courthouse: Commons, Jim.henderson 2018, CC BY-SA 3.0 → S049. **(c)** The June 2018 Instagram post was not retrievable (Instagram and Wayback blocked); only the RS description is available (E044). |
| 11 | DistroKid refresh | **PARTLY.** No first-party DistroKid newsroom statement found, so C066 stays on Variety/Music Ally. The answer is not yet due (Oct 6), so refresh then. S002 is image-only. Its header shows case no. **1:26-cv-01156-MN**, and the "MN" judge suffix is not verified here. Dispatcher: `yt.py pages --sources S002`. |
| 12 | Mechanical checks | **Dispatcher task.** The Read tool cannot render PDFs here (no poppler). Run `yt.py pages --sources S034,S002,S010,S011`. |

**New correction from this round (important for the title and ending):** "cannot be located upon the exercise of due diligence" is the **statutory trigger wording of 21 U.S.C. § 853(p)(1)(A)**, and the identical words already sit in the 2024 indictment's boilerplate (S006 ¶40 p.18; S051). This is a standard formula that lets the government seize *other* property. It is **not** a confession that the money vanished. Little-known fact #2 and review beat 3 ("the missing money") have been re-framed below (C094). The honest "who paid?" loop still stands. The "where did the money go?" loop does not.

**Round-1 counts:** sources 51 (tier 1–2: 44) · claims 109 · events 47.

Mode 2, researched 2026-09-26. Packaging locked at G1: *He Did the Math on Fake Streams. It Cost Him $8 Million.* — indictment self-email math crop + red-circled forfeiture figure.
Criminal (U.S. v. Smith), civil (UMG v. Believe; UMG v. DistroKid) and platform statements are kept separate throughout. Claim IDs → `claims.csv`, event IDs → `events.csv`.

**Packaging guardrails found in Mode 2 (read first):**
- The "math" (1,040 bots / 661,440 streams a day / $1,207,128 a year) is from the **2024 indictment ¶14 (allegation)** — it is *not* in the Superseding Information he pleaded guilty to (S031). On screen: "Indictment, ¶14 — allegation". (C013–C015)
- The "$8 million" is a **consented money judgment of $8,091,843.64** (S033). He also **admits the proceeds "cannot be located"** (C006). *Round 1: that phrase is the statutory § 853(p) trigger for substitute assets and is boilerplate, not a confession that the money vanished (C094).* Whether any of it has been collected is UNKNOWN (C090). "It cost him $8 million" is defensible as the judgment/forfeiture he agreed to; thumbnail text "$8M Forfeited" slightly overstates (implies collected). Safer: "$8M Judgment" / "Agreed to Forfeit $8M". Flag for packaging/defamation-risk.

---

## Story spine
- **Who we follow:** Michael "Mike" Smith, 52 at arrest / 54 at plea, of Cornelius, North Carolina — a businessman (medical clinics, per Rolling Stone) who spent a decade and a lot of money trying to be taken seriously as a musician (SMH Records, BET's *One Shot*, jazz-chart albums) (S028, C061–C062).
- **What he wanted:** listeners and royalties at scale. His own spreadsheet-email of 20 Oct 2017, as quoted by prosecutors, turns 1,040 bot accounts into a projected $1,207,128 a year (C013–C015).
- **What stood in the way:** fraud detection. Put a billion streams on one song and it gets pulled — "If we get too many streams on one song it comes down" (C025). Distributors flagged him in March and October 2018; a streaming platform flagged him in March 2019; each time, the charge he later pleaded to says, he denied it in writing (C036–C038).
- **The turn:** he didn't need more bots, he needed more *songs*. In 2018, per the indictment, a CEO of an AI-music company started supplying them — eventually "hundreds of thousands" — under a contract for 1,000–10,000 songs a month (C027–C032). "We've proved the model works" (C028). Titles like "Zygotic Washstands", artists like "Calm Knuckles" (C033).
- **Escalation:** "88 million TOTAL STREAMS" by June 2019 (C031); better AI in 2020 ("10x-20x better now", C034); up to 10,000 bot accounts (C016); $1.3M of royalties allegedly recycled into debit cards for bots (C019); by Feb 2024 his own email boasts "over 4 billion streams and $12 million in royalties" (C012).
- **The crisis:** March–April 2023, the MLC stops paying him; his representatives insist "Mike is the 'human' author!" (C039). Sept 4, 2024: indictment unsealed, arrest, three counts at up to 20 years each — the first U.S. criminal streaming-fraud case (C004, C048).
- **The cost:** March 19, 2026 — he waives indictment, is charged in a new one-count information (5-year max) and pleads guilty to conspiracy to commit wire fraud; consents to an $8,091,843.64 money judgment and admits the proceeds "cannot be located" (C001–C009). A federal felony conviction.
- **Where it stands (2026-09-26):** sentencing set for **Tuesday, Oct 6, 2026, 3:00 pm** (S034, C051). Defense asks for probation, arguing each fake stream is "a drop in an ocean" and no artist suffered "perceptible harm" (C053–C054); guideline range reported at 46–57 months, Probation reportedly recommends 24 (C058). Government submission due late September.
- **One level up (the industry thread):** the same shared-pool mechanism is why UMG went after distributors: Believe/TuneCore (2024, "at least $500,000,000" demanded; settled 2026, terms undisclosed) and DistroKid (sued Sept 15, 2026; DistroKid "strongly disagree[s]") (C065–C077). Deezer now says more than half of its daily uploads are fully AI-generated (C078).

## Cast
| Person / entity | Role | What they did (status-accurate) | What it cost them | Verbatim quote (source) |
|---|---|---|---|---|
| Michael Smith | Defendant; musician/businessman, Cornelius NC | Pleaded guilty 2026-03-19 to one count of conspiracy to commit wire fraud (18 U.S.C. § 371) (CONVICTION). Indictment details = allegations; overt acts in the Information = the charge he pleaded to. | Federal conviction; $8,091,843.64 money judgment; admitted proceeds cannot be located; faces up to 5 years; sentencing 2026-10-06 | "This is absolutely wrong and crazy! ... There is absolutely no fraud going on whatsoever! How can I appeal this?" (S031 p.2; S006 ¶27) · "I can't run the bots without content." (S006 ¶15(d)(iii), allegation) |
| Smith's defense team (Justine A. Harris, Noell Tin et al.) | Counsel | Negotiated plea to 5-year count; memo seeks probation (CLAIM, via Billboard) | — | "...it is a drop in an ocean." / "No individual artist or songwriter suffered any perceptible harm from Mr. Smith's conduct." (S013 citing Billboard) · "first-of-its-kind streaming fraud prosecution" (S034 p.1) |
| Judge John G. Koeltl (S.D.N.Y.) | Presiding judge | Set bail (S009); accepted plea; so-ordered forfeiture (S033); adjourned sentencing to 2026-10-06 (S034) | — | — (no reasoning on record yet) |
| Damian Williams | U.S. Attorney at indictment (2024) | Announced charges | — | "it's time for Smith to face the music." (S007) |
| Jay Clayton | U.S. Attorney at plea (2026) | Announced plea; signed Superseding Information (S031 p.5) | — | "Although the songs and listeners were fake, the millions of dollars Smith stole was real." (S008) |
| AUSAs Nicholas W. Chiuchiolo, Kevin Mead | Prosecutors (Complex Frauds & Cybercrime Unit) | Prosecuting; Mead signed forfeiture consent | — | — |
| CC-3 ("Chief Executive Officer of an AI music company") | Unnamed co-conspirator per indictment | Allegedly supplied AI songs under a Master Services Agreement; paid greater of $2,000 or 15% (ALLEGATION) | Not charged; not named in court papers | "this is not 'music,' it's 'instant music' ;)" (S006 ¶20, allegation). **Do not name or speculate on identity.** |
| CC-4 (music promoter), CC-1, CC-2 (music publicist) | Unnamed co-conspirators per indictment | Allegedly helped (ALLEGATION) | Not charged | "we've proved the model works" (CC-4, S006 ¶19). Do not identify. |
| The MLC (Mechanical Licensing Collective) | Nonprofit that pays U.S. digital mechanical royalties | Halted payments to Smith Mar–Apr 2023 (per indictment) | — | "prevented the diversion of mechanical royalties away from rightful songwriters" (S029) |
| Spotify / Pandora | Platforms | Say they paid little: ~$60,000 / $1,500 (CLAIM) | — | "our preventative measures worked" (Spotify, S035) |
| Universal Music Group (+Capitol Records, Capitol CMG) | Plaintiff (civil) | Sued Believe/TuneCore 2024 (settled 2026); sued DistroKid 2026 (ALLEGATION) | Legal costs; undisclosed settlement proceeds | "This lawsuit is not about the distribution of AI-generated music when clearly disclosed as such." (S001 fn.5) |
| DistroKid (DistroKid LLC, Kid Distro Holdings LLC, DK Holdco LLC); President Phil Bauer | Defendant (civil) | Accused of deceptive trade practices and infringement; denies (DENIAL) | Litigation; reputational. Nothing established. | "We strongly disagree with UMG's allegations ... We are confident in our practices and intend to defend DistroKid vigorously." (S005, S026) |
| Believe S.A. / TuneCore | Former defendants | Settled; dismissed with prejudice; no admission documented (SETTLEMENT) | Undisclosed | "strongly refute[d]" the claims (S016) |
| Deezer (CEO Alexis Lanternier) | Platform | Publishes AI-upload and fraud data (CLAIM) | — | "Now that half of all daily uploads are AI-generated tracks, we are taking additional steps..." (S022) |
| Victoria Oakley (IFPI) / Mitch Glazier (RIAA) | Industry bodies | Launched SII; op-ed | — | "This is theft, plain and simple." (S036, S037) |
| Katherine Reilly | Former SDNY fraud-unit chief (now private practice), worked on the case early | Commentary to Rolling Stone on allegations | — | "...identified a pot of money ... and developed a way to give himself access to [it]" (S028) |
| Kris Ahrend (MLC CEO) | Head of the nonprofit that pays U.S. digital mechanical royalties to songwriters | Per the indictment, the MLC halted Smith's payments in Mar–Apr 2023. On arrest day Ahrend said the MLC "withheld payment" (CLAIM). The amount withheld is not public (C096). | — | "As the DOJ recognized, The MLC identified and challenged the alleged misconduct, and withheld payment of the associated mechanical royalties..." (S027, C095) |
| Michael Lewan (Music Fights Fraud Alliance) | Exec. director of the industry anti-fraud group | Industry voice on who pays for fraud (CLAIM). He concedes no "trusted percentage or number" exists. | — | "that is a percentage of royalties not going to artists, creators, and songwriters ... It's being extracted from the royalty pool in relatively large sums." (S028, C105) |
| Tony Mantor | Nashville promoter who worked Smith's 2017 radio single | Took "You're My Kind of Beautiful" to AC radio: 13 weeks, peak No. 35 Billboard (REPORTED_FACT) | — | "That's the beauty of monitored ... They can't manipulate it." (S028, C102) |
| Kxng Crooked | Rapper, One Shot co-creator | Sympathetic voice (opinion) | — | "Whatever he did, he made that bed and he's got to lie in it ... Let's not take the man who's the independent guy [and] string him up." (S028, C106) |

## Turning points
1. **2017-10-20 — The self-email.** 1,040 bots → ~661,440 streams/day → $1,207,128/yr projected (E005; allegation). Cold open / thumbnail.
2. **2018-03-06 & 2018-10 — First flags, first denials.** "I ask that you still release it." / "absolutely no fraud going on whatsoever!" — in the charge he pleaded to (E006–E007).
3. **2018-10-18 — AI "proof of concept".** "We've proved the model works." Songs, not bots, were the bottleneck (E009–E011).
4. **2019-06-05 — "88 million TOTAL STREAMS."** The machine at scale, 10% to each partner, 10,000 more songs requested (E015).
5. **2023-03/04 — The MLC stops paying.** "Mike is the 'human' author!" (E019).
6. **2024-09-04 — Arrest.** On a Wednesday morning he is arrested at home in Cornelius, outside Charlotte, and taken before a federal magistrate in North Carolina. Rule 5 papers go to Manhattan. His lawyer declines to comment. The same day the MLC's CEO says it had "withheld payment". It is the first U.S. criminal streaming-fraud case: 3 counts × 20-year max (E022, C099–C101, C095).
   - *Between turns 4 and 5 (2019-06 → 2023-03) the record has no scene (gap 9).* Compress: "10x-20x better" (2020-08-17), then $1.3M of royalties cycled into bot debit cards (2020–2023), then the MLC.
7. **2026-03-19 — The plea.** Waiver of indictment → one-count § 371 information → guilty plea → $8,091,843.64 money judgment; proceeds "cannot be located" (E029–E030).
8. **2026-09-15 → 2026-10-06 — Industry turn + reckoning.** UMG sues DistroKid (E038); defense memo "drop in an ocean" (E039); sentencing Oct 6 (E040).

## The money
| Figure | Exact meaning | Date basis | Who paid / lost / gained | Source |
|---|---|---|---|---|
| $1,207,128 | Smith's own projected annual royalties in his self-email (with $3,307.20/day, $99,216/month; half a cent per stream) | 2017-10-20 email, alleged | Projection, not a receipt | S006 ¶14 pp.7–8 (C015) |
| ~$110,000/month | Earnings Smith reported to CC-3/CC-4; each partner got 10% | 2019-06-05, alleged | Smith and partners (alleged) | S006 ¶21 (C031) |
| Greater of $2,000 or 15% | Monthly payment to CC-3's company under Master Services Agreement | 2019-02-01, alleged | Paid by Smith to AI supplier (alleged) | S006 ¶22 (C030) |
| $1.3 million | Royalties allegedly moved via "SMH Entertainment" to fund bot debit cards | 2020–2023, alleged | Recycled into the scheme | S006 ¶11(e) (C019) |
| "over 4 billion streams and $12 million in royalties since 2019" | Smith's own boast in an email | Feb 2024, alleged | Smith's claim | S006 ¶25 (C012) |
| "more than $10 million" | Proceeds alleged at charging | 2024-09-04 | Alleged | S006 ¶1, S007 (C011) |
| "more than $8 million" | Proceeds per DOJ at plea | 2026-03-19 | DOJ statement | S008 (C010) |
| **$8,091,843.64** | Consented money judgment = proceeds Smith "personally obtained"; part of sentence; substitute assets may be pursued | Order filed 2026-03-19 | Owed by Smith to the U.S. (Assets Forfeiture Fund); collection UNKNOWN | S033 pp.1–3 (C005–C008) |
| $500,000 | Personal recognizance bond, 2 cosigners (not cash posted) | 2024-09-18 | — | S009 (C049) |
| ~$60,000 | Spotify's estimate of what Smith generated on Spotify | first stated 2024-09-12 ("game"), restated 2025-06-06 ("generate") | Spotify says it paid it | S043, S035, S029 (C041) |
| UNKNOWN | Mechanical royalties the MLC withheld from Smith | 2023 → | Withheld, per the MLC; amount never disclosed | S027, S006 ¶30 (C095–C096) |
| no figure | Apple Music, Boomplay, Tidal, YouTube, Amazon Music: no response; SoundCloud: declined figure | 2024–2026 | Unknown | S044, S035, S028 (C097) |
| $1,500 | Pandora's "estimated royalty exposure" | stated 2025 | Pandora | S035 (C042) |
| 46–57 months / 24 months | Reported guideline range / Probation recommendation | Sept 2026, reported | — | S013 citing Billboard (C058) |
| 5 years | Statutory max of the count he pleaded to | 2026 | — | S008 (C003) |
| "at least $500,000,000" | Damages **demanded** from Believe/TuneCore | 2024-11-04 | Demand, not paid; settled for undisclosed terms | S003 ¶9 (C075) |
| Statutory damages per work (up to the maximum cited in ¶122); 1,000 works in Exhibits A/B | Relief **sought** from DistroKid | 2026-09-15 | Demand only — never multiply | S001 ¶¶15, 122 (C072) |
| $1.3B (2021) / reported $2B (2026) | DistroKid valuations cited in complaint | 2021 / 2026-07 | Investors (Insight; CVC) | S001 ¶¶47–48, S004 (C073) |
| 20% / $29 per track | DistroKid "Social Media Pack" revenue share / "Leave a Legacy" fee (as alleged from help pages) | 2026 | DistroKid revenue lines | S001 ¶¶82–83 (C074) |
| $1B (2014) → $10B (2024) | Spotify total music payouts | Spotify statement 2025-09-25 | Rightsholders | S020 (C083) |

## The mechanism
1. **The shared pot.** Platforms put a share of subscription/ad revenue into royalty pools. Money is split by each rightsholder's *share of total streams* in the period (S006 ¶¶3–4; S008). A fake stream doesn't create new money — it claims a slice of the same pot (prosecution framing, C044).
2. **Accounts.** Bulk-bought email accounts in fictitious names → thousands of streaming accounts, often on cheaper "family plans", paid with corporate debit cards issued in fake "employee" names (alleged, C016–C019).
3. **Playback.** Cloud virtual machines, many browser tabs, modified macros looping playback, VPNs hiding that it all ran from his home (alleged, C020).
4. **The detection problem.** One song with a billion plays gets caught; so spread the plays thin — which requires an enormous catalog (C022–C025).
5. **AI fills the catalog.** AI supplier sends thousands of files a week named with random hashes; Smith attaches random song/artist names so they look like real acts (C030–C033).
6. **Collect and deny.** Royalties flow through distributors, platforms and the MLC; each warning is met with a written denial (C036–C039).
7. **Where it broke.** Platforms (Spotify says early) and the MLC (2023) cut him off (C039–C041); the FBI/SDNY case followed.
8. **One level up (civil).** UMG's theory against distributors: open-access pipes deliver volume that dilutes the same pools; and when ContentID shows a match they click "No, exclude overlaps" but keep delivering the same track elsewhere (C070; same allegation against Believe, S003 ¶8). **Allegations only; DistroKid denies.**

## Both sides' strongest arguments
**Prosecution / industry (criminal thread):**
- The pool is finite, so every fraudulent dollar came from someone streamed by real people (S006 ¶¶3–5; Clayton, C046; Oakley/Glazier, C085).
- Intent is documented in his own words — "Unde[te]ctable", "TON of songs fast ... around the anti fraud policies" (C021, C024) — and in repeated written denials he now concedes were part of a conspiracy he pleaded guilty to (C036–C038).
- Scale: billions of streams; he consented to an $8.09M judgment and admits the money cannot be located (C005–C006).

**Defense (strongest version):**
- Harm per artist was infinitesimal — "a drop in an ocean"; "no individual artist or songwriter suffered any perceptible harm" (C053–C054, via Billboard).
- The loss-driven fraud guideline (§ 2B1.1) may not fit a novel, diffuse-harm case — the parties themselves flagged this (C050).
- Industry hypocrisy: bot fraud "indisputably rampant... including by big labels and publishers" (C055, defense claim — no evidence in our record; attribute).
- No criminal record; letters of support; family impact (C057).
- Supporting facts the defense could point to: Spotify says only ~$60,000 came from it (C041); the MLC says it *prevented* diversion of mechanical royalties (C040); Deezer says fraudulent streams are stripped from its pool so impact on human artists is "minimal on Deezer" (C081). **Our analysis:** these platform statements make "who exactly paid" a genuinely open question — the honest tension for the ending.
- Smith pleaded not guilty for 18 months before pleading (S028); his lawyer disputed several ex-associates' anecdotes (C063).

**UMG (civil):** DistroKid markets itself as "Artist first, always" and anti-spam while its highest-volume accounts post thousands of Suno outputs; it keeps distributing tracks it conceded on ContentID; valuation grows with volume (C065–C074).
**DistroKid (strongest version):** It serves millions of independent artists; has "sophisticated protections"; these are "shared industry challenges"; UMG should have used "established industry processes"; UMG itself concedes disclosed AI music is legitimate (C066, C071). **Our analysis (not DistroKid's filed position — none filed yet):** an open-access distributor passing uploads through at scale is not the same as a person running bots; UMG is also a competitor in distribution (S001 fn.3) — the complaint admits they compete.
**Believe/TuneCore:** "strongly refute[d]"; settled with no admission (C076–C077).

## Little-known facts (≥5)
1. **He never pleaded to the indictment.** On plea day he waived indictment and pleaded to a brand-new one-count *Superseding Information* under 18 U.S.C. § 371 — the general conspiracy statute with a 5-year cap — instead of the § 1349 / 20-year counts (S031 p.1, S032, S033 p.1). *Surprising:* explains why his exposure fell from three 20-year counts to 5 years; no competitor covers the charging switch.
2. **It's a judgment, not a seizure.** In the forfeiture order Smith admits the proceeds he personally obtained "cannot be located upon the exercise of due diligence," which lets the government chase substitute assets (S033 pp.2–3). *Surprising:* the $8M is a judgment against him, not a pile of seized cash. **Round-1 correction:** the quoted words are the statutory § 853(p)(1)(A) trigger and already appeared in the 2024 indictment's boilerplate (C094). Do not dramatise it as "the money vanished". Collection status stays UNKNOWN (C090).
3. **A sentencing date the trade press missed.** On June 9, 2026 Judge Koeltl handwrote: defense submissions Sept 22, government submissions late Sept, "SENTENCING ADJOURNED TO TUESDAY, OCTOBER 6, 2026, AT 3:00PM" (S034). MBW (S013) reported no new date on the docket. The defense letter also calls it a "first-of-its-kind streaming fraud prosecution" and flags whether § 2B1.1 "fairly address[es] Mr. Smith's culpability."
4. **"I ask that you still release it."** The first warning (Mar 6, 2018) and his reply are overt acts in the very charge he pleaded guilty to (S031 p.2). *Surprising:* the plea document itself is built around his denials, not the bots.
5. **Spotify says it paid him about $60,000; Pandora $1,500** (S035, S029, S028). *Surprising:* against an $8.09M judgment — the biggest platform says it caught him early; which services paid the bulk remains unanswered (C043).
6. **The AI contract.** A signed "Master Services Agreement" (Feb 1, 2019): 1,000–10,000 songs a month, Smith owns the IP, pays the greater of $2,000 or 15% (S006 ¶22). Songs arrived as hash-named files like "n_7a2b2d74-...mp3" (S006 ¶23). Competitors cite the fake names, not the contract.
7. **Laundering the bots' bills.** $1.3M of royalties allegedly routed through "SMH Entertainment" to a Manhattan corporate debit-card service with dozens of fake employee names (S006 ¶11(e)) — the basis of the dropped money-laundering count.
8. **"Mike is the 'human' author!"** — what his representatives told the MLC in March 2023 (S006 ¶30(b)).
9. **A real, small music career first.** Rolling Stone: a 2017 adult-contemporary radio chart run peaking at No. 35 on Billboard, No. 1 jazz albums in 2018–2019, 214,875 Spotify monthly listeners posted in June 2018 (S028). *Use carefully — do not imply those charts were faked.*
10. **The industry's integrity pact launched the day before the DistroKid suit** (IFPI SII, Sept 14; suit Sept 15) and DistroKid was not on the launch list (S036, S039, S005).
12. **"They can't manipulate it."** In 2017 his promoter praised the one chart Smith reached that *couldn't* be gamed: monitored radio airplay, peak No. 35 (S028, C102). The same year, per the indictment, he emailed himself the bot math. *Surprising:* the real, modest success came first.
13. **Five services said nothing.** Apple Music, Boomplay, Tidal, YouTube and Amazon Music gave "radio silence" when DMN asked what they paid him (S044, C097). Spotify's first answer came 8 days after the arrest, with the word "game" (S043).
14. **Songwriters' collector held the money back.** On arrest day the MLC's CEO said it had "withheld payment of the associated mechanical royalties" (S027, C095). The amount has never been disclosed (C096).
11. **Deezer's own data cuts both ways:** >50% of uploads AI at June peak, up to 85% of streams on fully-AI tracks fraudulent — yet Deezer says impact on human royalties is "minimal on Deezer" because it strips them out (S022).

## Why now
- **The sentence lands Oct 6, 2026** — the first sentence for AI-assisted streaming fraud in the U.S. (S034, S013).
- **Flood metrics:** Deezer ~75,000 AI tracks/day (≈44%) in April 2026 → ~90,000/day, >50% of uploads at June 2026 peak; 13.4M AI tracks tagged in 2025 (S021, S022). Spotify removed >75M "spammy tracks" in 12 months to Sept 2025; payouts $10B in 2024 (S020).
- **Industry response in 2026:** IFPI/RIAA op-ed (Feb), Believe settlement (Apr), Deezer takedown policy (Jul), CVC majority investment in DistroKid (Jul), IFPI Streaming Integrity Initiative (Sept 14), UMG v. DistroKid (Sept 15).
- **Stakes framing (sourced):** CISAC/PMP study cited by Deezer: nearly 25% of creators' revenues at risk by 2028, up to €4 billion (S021/S022 — third-party study as cited by Deezer; attribute).

## Open loops & ending
- **Round-1 note:** remove the "missing money" open loop. "Cannot be located" is statutory wording (C094). Keep "who paid?" (C043, C097) and "what will it actually cost him?" (Oct 6).
- **Open:** (1) Sentence on Oct 6 — probation (defense) vs reported 46–57-month guidelines vs 24-month PSR recommendation; government's number not yet public. (2) Restitution — to whom, if anyone (C091). (3) Collection of the $8,091,843.64 (C090). (4) Why $10M became $8M (C089). (5) Which platforms paid the bulk (C043). (6) DistroKid's answer/motion (reported due Oct 6) and whether a distributor can be liable for the flood it carries. (7) Co-conspirators remain uncharged in public records.
- **Honest ending (if sentence not yet imposed at lock):** A man who did the math and got the answer he wanted — until the arithmetic came due: a felony, an $8.09M judgment the government can collect from whatever else he owns, and a judge deciding whether a drop in an ocean is still theft. Meanwhile the pipe that carried his songs now carries 90,000 AI tracks a day on one service alone — and the industry is suing the pipe.
- **What would change it:** the Oct 6 sentence (ending rewrite); a government memo with a loss/victim theory; DistroKid's motion to dismiss; any settlement.

## Visual evidence
All AUTHENTIC_SOURCE unless noted; crops must keep attribution line visible.
- **S006 indictment** (DOJ, public domain): p.1 caption "SEALED INDICTMENT"; **pp.7–8 ¶14 self-email math (thumbnail/cold open — label "allegation")**; p.9 "TON of songs" emails; p.10 "proof of concept", "instant music", "88 million TOTAL STREAMS"; **p.11 Zygophyceae / Calm Knuckles lists**; p.12 "10x-20x better" and "$12 million" email; pp.13–15 denials and "Mike is the 'human' author!"; p.18 Damian Williams signature block (official).
- **S031 Superseding Information**: p.1 caption "SUPERSEDING INFORMATION / S1 24 Cr. 504"; p.2 overt act (c) "I ask that you still release it"; p.3 "(Title 18, United States Code, Section 371.)"; p.5 Clayton signature (official).
- **S033 Consent Preliminary Order of Forfeiture/Money Judgment**: **p.1–2 "$8,091,843.64" (red-circle candidate — real crop)**; p.2 "cannot be located upon the exercise of due diligence"; p.3 ¶5 substitute assets. p.4 has Smith's handwritten signature — do not feature.
- **S034 Dkt. 52**: handwritten endorsement "SENTENCING ADJOURNED TO TUESDAY, OCTOBER 6, 2026" (strong authentic visual).
- **S032 Waiver of Indictment** (1 p.) — caption only; signature not featured.
- **S009 bail order** (1 p., Koeltl). **S012 defense letter** (1 p.).
- **S007/S008 DOJ press releases** (headlines, Clayton/Williams quotes).
- **S001 UMG v. DistroKid complaint**: p.7 Figures 1A/1B ("Unholy" vs "Unholy – Radio Edit"); p.16 Fig. 2 "Artist first, always"; p.20 Fig. 3 redacted distributor chart; pp.23–24 Figs 4A/4B ("Impossible"); **p.25 Fig. 5 ContentID reference-overlap screenshot**; p.29 table of tracks (contains uploader names — blur/avoid names). Private-lawyer filing: excerpts for commentary only.
- **S003 Believe complaint**: p.3 ¶6 "Kendrik Laamar / Arriana Gramde / Jutin Biber / Llady Gaga".
- **S020/S021/S022** platform newsroom pages (screenshots of figures).
- **Round-1 visual candidates:** courthouse photo, Commons, Jim.henderson, CC BY-SA 3.0 (S049, credit required). A possible Smith photo on the One Shot set, Commons CC BY-SA 4.0, has **unverified provenance** (S050): the owner must view it and decide. Getty editorial (Bennett Raglin, One Shot screening 2016-08-22) needs an owner license decision. No capture of the June 2018 Instagram post was retrievable.
- **Places (own generation / ILLUSTRATIVE only):** Daniel Patrick Moynihan U.S. Courthouse, 500 Pearl St (address on S012/S034) — real photo via CC if found; suburban Charlotte lake-house setting only as generic illustration, never "his house". No AI likeness of Smith; a real editorial photo exists (Getty, Bennett Raglin 2016, per S015) — license needed; otherwise none.

## Current status (as of 2026-09-26)
- **U.S. v. Smith (S.D.N.Y. 24-cr-504, Judge Koeltl):** Convicted by plea (2026-03-19) of one count of conspiracy to commit wire fraud (18 U.S.C. § 371, Superseding Information S1). Money judgment $8,091,843.64 entered by consent (Dkt. 47). **Not sentenced.** Sentencing set for 2026-10-06 3:00 pm (Dkt. 52 endorsement). Defense memo filed 2026-09-22 (Dkt. 57, PACER-only; sealing granted, Dkt. 59). Government submission due late Sept — not yet seen. Disposition of the original indictment counts: UNKNOWN (typically resolved at sentencing; not verified). On pretrial release.
- **UMG v. Believe/TuneCore (S.D.N.Y. 24-cv-8406):** Dismissed with prejudice by stipulation after settlement (filed 2026-04-03; so-ordered 2026-04-08 per docket listing); terms undisclosed; no admission documented.
- **UMG v. DistroKid (D. Del. 1:26-cv-01156):** Complaint filed 2026-09-15; DistroKid denies; answer reportedly due 2026-10-06; no ruling.

## Open uncertainties
1. Sentence (Oct 6) — **must refresh before script lock and before release**; the ending depends on it.
2. Government submission due date digit (Sept 28 or 29) — handwriting; confirm via `yt.py pages --sources S034`.
3. Guidelines 46–57 / PSR 24 months / all memo quotes are second-hand (Billboard via MBW/Music Ally); Billboard paywalled; Dkt. 57 PACER-only.
4. Plea allocution transcript (Dkt. 55) not public — we cannot say what facts Smith admitted aloud; use "pleaded guilty to" + the Information's text, attributed.
5. $10M → $8M difference unexplained (C089); collection of judgment unknown (C090); restitution unknown (C091).
6. Which services paid the bulk of the money — unknown (C043).
7. Rolling Stone feature (S028): January 2026 (day unconfirmed). Resolved in round 1. Still a single source for most backstory scenes, now partly corroborated (S047, S048).
11. Government sentencing submission: not filed as of 2026-09-26 (due Sept 28/29).
12. MLC withheld amount: not public (C096). W.D.N.C. initial-appearance record: not retrieved (C100).
13. Competitor transcripts not checked (gap 7). Dispatcher yt-dlp needed.
8. DistroKid answer deadline (Oct 6) from search-result docket text; confirm on S002 pages.
9. S002, S010, S011 image-only — need `yt.py pages` visual read.
10. Identity of CC-1…CC-4 — deliberately not researched for script use; secondary outlets name a suspected CC-3 who denies wrongdoing and is uncharged. Excluded.
