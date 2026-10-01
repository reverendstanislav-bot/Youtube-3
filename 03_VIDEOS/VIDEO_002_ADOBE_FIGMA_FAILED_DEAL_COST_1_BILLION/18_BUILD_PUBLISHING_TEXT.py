#!/usr/bin/env python3
"""VIDEO 002 — Stage 18: publishing texts (same layout as the channel-2 upload packs).

Writes into <media>/18_UPLOAD_PACK/PUBLISHING + SHORTS and mirrors the text files into
18_PUBLISHING/ in Git. Chapters come from the locked section starts in 11_VISUAL_TIMELINE.csv.
"""
import csv, json, shutil, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MEDIA = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("C:/Users/KK/Documents/WhatItCost_media/002-adobe-figma")
PACK = MEDIA / "18_UPLOAD_PACK"
PUB, SHORTS, GIT = PACK / "PUBLISHING", PACK / "SHORTS", HERE / "18_PUBLISHING"
for d in (PUB, SHORTS, GIT):
    d.mkdir(parents=True, exist_ok=True)

TITLE = "Adobe Paid $1 Billion for a Deal That Never Happened"
CHAPTER_TITLES = {
    "S01": "A Billion Dollars for a Deal That Never Closed",
    "S02": "The Twenty-Billion-Dollar Bet",
    "S03": "The Clause Existed Before the Deal",
    "S04": "What a Reverse Termination Fee Actually Does",
    "S05": "Then the Deal Became Public",
    "S06": "The Reviews Expand",
    "S07": "The Concerns Become Hard to Ignore",
    "S08": "Adobe and Figma Push Back",
    "S09": "The Deal Ends Before the Final \u201cNo\u201d",
    "S10": "Three Days Later, the Contract Fires",
    "S11": "The Two Numbers People Confuse",
    "S12": "Figma After Adobe",
    "S13": "What the Clause Was Really Pricing",
}
rows = sorted(csv.DictReader(open(HERE / "11_VISUAL_TIMELINE.csv", encoding="utf-8-sig")), key=lambda r: float(r["start"]))
starts = {}
for r in rows:
    starts.setdefault(r["section"], 0.0 if not starts else float(r["start"]))
chapters = "\n".join(f"{int(s // 60):02d}:{int(s % 60):02d} {CHAPTER_TITLES[k]}" for k, s in starts.items())

SOURCES = [
    ("Adobe \u2014 Adobe to Acquire Figma (Sept. 15, 2022)", "https://news.adobe.com/news/news-details/2022/adobe-to-acquire-figma"),
    ("Agreement and Plan of Merger, Adobe / Figma (SEC Exhibit 2.1)", "https://www.sec.gov/Archives/edgar/data/796343/000114036122033413/ny20005310x2_ex2-1.htm"),
    ("Figma consent solicitation / Adobe prospectus (SEC 424B3) \u2014 background of the merger", "https://www.sec.gov/Archives/edgar/data/796343/000114036123001357/ny20005310x21_424b3.htm"),
    ("UK CMA \u2014 Adobe / Figma merger inquiry", "https://www.gov.uk/cma-cases/adobe-slash-figma-merger-inquiry"),
    ("UK CMA \u2014 Adobe / Figma deal could harm UK digital design sector (provisional findings)", "https://www.gov.uk/government/news/adobe-figma-deal-could-harm-uk-digital-design-sector"),
    ("European Commission \u2014 Competition Merger Brief 2/2024, M.11033 Adobe/Figma", "https://competition-policy.ec.europa.eu/document/download/4e7dcad9-4787-4cef-885b-dcc5f8f1244c_en?filename=kd0124001enn_mergers_brief_2024_2.pdf"),
    ("Adobe and Figma Mutually Agree to Terminate Merger Agreement (Dec. 18, 2023)", "https://news.adobe.com/news/news-details/2023/adobe-and-figma-mutually-agree-to-terminate-merger-agreement"),
    ("Mutual Termination Agreement, Adobe / Figma (SEC)", "https://www.sec.gov/Archives/edgar/data/796343/000079634323000254/mutualterminationagreement.htm"),
    ("Adobe FY2023 Form 10-K", "https://www.sec.gov/Archives/edgar/data/796343/000079634324000006/adbe-20231201.htm"),
    ("Figma Form S-1 Registration Statement", "https://www.sec.gov/Archives/edgar/data/1579878/000162828025033742/figma-sx1.htm"),
    ("Figma 2025 Form 10-K", "https://www.sec.gov/Archives/edgar/data/1579878/000162828026009228/fig-20251231.htm"),
]
sources = "\n\n".join(f"{t}:\n{u}" for t, u in SOURCES)

CREDITS = (
    "Contains public sector information licensed under the Open Government Licence v3.0 (UK Competition and Markets Authority).\n"
    "European Commission material: \u00a9 European Union, 2023\u20132024, reused under CC BY 4.0.\n"
    "SEC EDGAR filings and company statements are shown as documentary excerpts for news reporting and commentary."
)
DISCLOSURE = (
    "This documentary combines authentic public documents, company and regulator material, custom explanatory graphics, "
    "and AI-generated illustrative reconstructions. Reconstructions are illustrative and are not presented as original documents or footage. "
    "The $1 billion was a contractual termination fee, not a government fine."
)

DESCRIPTION = f"""Adobe agreed to buy Figma for about $20 billion. The acquisition never closed. Adobe still paid Figma $1 billion.

That billion dollars was not a government fine. It came from a reverse termination fee the two companies negotiated before the merger agreement was signed. This episode follows the record \u2014 SEC filings, the merger agreement, UK CMA and European Commission documents \u2014 to show how the clause entered the deal, why the regulators' concerns grew, how the deal ended by mutual termination before any final UK or EU prohibition, and how three business days later the clause became cash.

CHAPTERS
{chapters}

SELECTED SOURCES
{sources}

CREDITS
{CREDITS}

VISUAL DISCLOSURE
{DISCLOSURE}

#Adobe #Figma #WhatItCost #Mergers #BusinessHistory
"""

TAGS = ["Adobe", "Figma", "Adobe Figma deal", "reverse termination fee", "termination fee",
        "merger", "antitrust", "CMA", "European Commission", "business documentary", "What It Cost"]
PINNED = ("Adobe never acquired Figma, but the $1 billion was paid anyway \u2014 because a clause negotiated in 2022 priced the "
          "risk that regulators would stand in the way. Was the $1B a bad bet for Adobe, or a fair price for Figma's risk? "
          "Sources and credits are in the description.")

META = {
    "title": TITLE,
    "category": "Education",
    "language": "English",
    "audience": "Not made for kids",
    "altered_or_synthetic_content": "Yes",
    "music": "None (narration + original sound design)",
    "thumbnail": "VIDEO_002_THUMBNAIL_YOUTUBE_1280x720.jpg",
    "thumbnail_text": "$1 BILLION / FOR A DEAL THAT NEVER HAPPENED",
    "captions": "VIDEO_002_CAPTIONS_EN.srt (optional; captions are burned into the picture)",
    "tags": TAGS,
    "pinned_comment": PINNED,
}

SHORT_TEXT = [
    ("SH01", "Adobe Paid $1 Billion for a Deal That Never Happened",
     "Adobe agreed to buy Figma for about $20B. The deal never closed \u2014 and Adobe still paid Figma $1B. Not a fine: a contract clause.",
     "#Adobe #Figma #Shorts"),
    ("SH02", "Figma Negotiated the $1B Clause Before Signing",
     "June 19: Adobe offers ~$20B, no fee. July 5: Figma asks for protection. July 20: Adobe agrees to a $1B reverse termination fee.",
     "#Figma #Mergers #Shorts"),
    ("SH03", "What a Reverse Termination Fee Actually Is",
     "The Adobe\u2013Figma merger agreement says the $1B fee is not a penalty \u2014 it is liquidated damages for defined closing failures.",
     "#Business #Law #Shorts"),
    ("SH04", "Adobe\u2013Figma: Pressure Was Real, but No Final \u201cNo\u201d",
     "By late 2023 the UK CMA and the European Commission had serious concerns \u2014 but no final prohibition decision had been issued.",
     "#Antitrust #Adobe #Shorts"),
    ("SH05", "How the Adobe\u2013Figma Deal Actually Ended",
     "Adobe and Figma ended the merger themselves by mutual termination, saying there was no clear path to the approvals they needed.",
     "#Adobe #Figma #Shorts"),
    ("SH06", "Three Days Later, Adobe Paid $1 Billion",
     "The deal was terminated on December 17, 2023. The agreement required the $1B within three business days. Adobe paid on December 20.",
     "#Adobe #Business #Shorts"),
    ("SH07", "$20 Billion vs $1 Billion: The Numbers People Confuse",
     "About $20B was the price Adobe proposed. $1B was the termination payment that actually happened. Adobe did not spend $21B on Figma.",
     "#Finance #Adobe #Shorts"),
    ("SH08", "What Happened to Figma After Adobe",
     "The failed acquisition did not end Figma's story: it stayed independent and later became a public company.",
     "#Figma #IPO #Shorts"),
]
shorts_txt = ["VIDEO 002 \u2014 8 SHORTS", "",
              "\u0412\u0441\u0435 \u0440\u043e\u043b\u0438\u043a\u0438 \u0443\u0436\u0435 \u0433\u043e\u0442\u043e\u0432\u044b: 1080\u00d71920, 25 fps, \u0433\u043e\u043b\u043e\u0441 Harrison + \u0437\u0432\u0443\u043a\u043e\u0432\u043e\u0439 \u0434\u0438\u0437\u0430\u0439\u043d V6, \u0441\u0443\u0431\u0442\u0438\u0442\u0440\u044b \u0432\u0448\u0438\u0442\u044b, \u0431\u0435\u0437 \u043c\u0443\u0437\u044b\u043a\u0438.", ""]
for n, (sid, title, desc, tags) in enumerate(SHORT_TEXT, 1):
    shorts_txt += [f"{n}) VIDEO_002_{sid}.mp4", f"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435: {title}", f"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435: {desc}", tags, ""]
shorts_txt += ["\u0414\u043b\u044f \u043a\u0430\u0436\u0434\u043e\u0433\u043e Short:",
               "- \u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u044e\u0449\u0438\u0439 MP4;",
               "- \u0432\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0438 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0438\u0437 \u044d\u0442\u043e\u0433\u043e \u0444\u0430\u0439\u043b\u0430;",
               "- \u0430\u0443\u0434\u0438\u0442\u043e\u0440\u0438\u044f: \u00ab\u041d\u0435 \u0434\u043b\u044f \u0434\u0435\u0442\u0435\u0439\u00bb;",
               "- \u0438\u0437\u043c\u0435\u043d\u0451\u043d\u043d\u044b\u0439/\u0441\u0438\u043d\u0442\u0435\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043a\u043e\u043d\u0442\u0435\u043d\u0442: \u00ab\u0414\u0430\u00bb;",
               "- \u043c\u0443\u0437\u044b\u043a\u0430: \u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442;",
               "- \u043f\u043e\u0441\u043b\u0435 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438 \u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0433\u043e \u0440\u043e\u043b\u0438\u043a\u0430 \u0432 \u043a\u0430\u0436\u0434\u043e\u043c Short \u0443\u043a\u0430\u0437\u0430\u0442\u044c \u0435\u0433\u043e \u043a\u0430\u043a \u0441\u0432\u044f\u0437\u0430\u043d\u043d\u043e\u0435 \u0432\u0438\u0434\u0435\u043e (Related video).", ""]

RU = f"""VIDEO 002 \u2014 \u0414\u0410\u041d\u041d\u042b\u0415 \u0414\u041b\u042f \u0417\u0410\u0413\u0420\u0423\u0417\u041a\u0418 \u041d\u0410 YOUTUBE

1. \u0412\u0418\u0414\u0415\u041e
\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u0430\u0439\u043b: ../DELIVERY/VIDEO_002_UPLOAD_MASTER_1080P.mp4

2. \u041e\u0411\u041b\u041e\u0416\u041a\u0410
\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u0430\u0439\u043b: VIDEO_002_THUMBNAIL_YOUTUBE_1280x720.jpg

3. \u041d\u0410\u0417\u0412\u0410\u041d\u0418\u0415
{TITLE}

4. \u041e\u041f\u0418\u0421\u0410\u041d\u0418\u0415
{DESCRIPTION}
5. \u041d\u0410\u0421\u0422\u0420\u041e\u0419\u041a\u0418
\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f: Education
\u042f\u0437\u044b\u043a: English
\u0410\u0443\u0434\u0438\u0442\u043e\u0440\u0438\u044f: \u041d\u0435 \u0434\u043b\u044f \u0434\u0435\u0442\u0435\u0439
\u0418\u0437\u043c\u0435\u043d\u0451\u043d\u043d\u044b\u0439 \u0438\u043b\u0438 \u0441\u0438\u043d\u0442\u0435\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u043a\u043e\u043d\u0442\u0435\u043d\u0442: \u0414\u0430
\u041c\u0443\u0437\u044b\u043a\u0430: \u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442 (\u0442\u043e\u043b\u044c\u043a\u043e \u0433\u043e\u043b\u043e\u0441 \u0438 \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0439 \u0437\u0432\u0443\u043a\u043e\u0432\u043e\u0439 \u0434\u0438\u0437\u0430\u0439\u043d)
\u0422\u0435\u0433\u0438: {", ".join(TAGS)}
\u0421\u0443\u0431\u0442\u0438\u0442\u0440\u044b (\u043f\u043e \u0436\u0435\u043b\u0430\u043d\u0438\u044e): VIDEO_002_CAPTIONS_EN.srt \u2014 \u0441\u0443\u0431\u0442\u0438\u0442\u0440\u044b \u0443\u0436\u0435 \u0432\u0448\u0438\u0442\u044b \u0432 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0443

6. \u0417\u0410\u041a\u0420\u0415\u041f\u041b\u0401\u041d\u041d\u042b\u0419 \u041a\u041e\u041c\u041c\u0415\u041d\u0422\u0410\u0420\u0418\u0419
{PINNED}

7. SHORTS
\u041e\u0442\u043a\u0440\u044b\u0442\u044c \u043f\u0430\u043f\u043a\u0443 ../SHORTS: \u0442\u0430\u043c 8 \u0433\u043e\u0442\u043e\u0432\u044b\u0445 MP4 \u0438 \u0444\u0430\u0439\u043b SHORTS_UPLOAD_TEXT_RU.txt.

8. \u0412\u0410\u0416\u041d\u041e
- \u041d\u0435 \u043f\u0438\u0441\u0430\u0442\u044c, \u0447\u0442\u043e Adobe \u00ab\u043e\u0448\u0442\u0440\u0430\u0444\u043e\u0432\u0430\u043b\u0438\u00bb: $1B \u2014 \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u043d\u0430\u044f \u0432\u044b\u043f\u043b\u0430\u0442\u0430, \u043d\u0435 \u0448\u0442\u0440\u0430\u0444.
- \u041d\u0435 \u043f\u0438\u0441\u0430\u0442\u044c, \u0447\u0442\u043e \u0441\u0434\u0435\u043b\u043a\u0443 \u00ab\u0437\u0430\u043f\u0440\u0435\u0442\u0438\u043b\u0438\u00bb: \u0444\u0438\u043d\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0437\u0430\u043f\u0440\u0435\u0442\u0430 CMA/EC \u043d\u0435 \u0431\u044b\u043b\u043e, \u0441\u0434\u0435\u043b\u043a\u0443 \u0440\u0430\u0441\u0442\u043e\u0440\u0433\u043b\u0438 \u043f\u043e \u0432\u0437\u0430\u0438\u043c\u043d\u043e\u043c\u0443 \u0441\u043e\u0433\u043b\u0430\u0441\u0438\u044e.
- \u0411\u043b\u043e\u043a CREDITS \u0438\u0437 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u044f \u043d\u0435 \u0443\u0434\u0430\u043b\u044f\u0442\u044c (\u0442\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u0435 \u043b\u0438\u0446\u0435\u043d\u0437\u0438\u0439 OGL v3.0 \u0438 CC BY 4.0).
"""

CREDITS_MD = f"""# VIDEO 002 \u2014 Visual Credits

{CREDITS}

Company material (Adobe, Figma) appears only as documentary context for reporting on the deal (editorial use).
The thumbnail and many frames are AI-generated illustrative composites built around authentic document excerpts;
illustrative elements (cash, stamps, desks, boards) are not presented as authentic evidence.

{DISCLOSURE}
"""

PACKAGE_MD = f"""# VIDEO 002 \u2014 YouTube Upload Package

Status: **READY**

- Video: `../DELIVERY/VIDEO_002_UPLOAD_MASTER_1080P.mp4`
- Thumbnail: `VIDEO_002_THUMBNAIL_YOUTUBE_1280x720.jpg` (master: `VIDEO_002_THUMBNAIL_MASTER.png`)
- Paste-ready description: `YOUTUBE_DESCRIPTION.txt`
- Metadata: `YOUTUBE_METADATA.json`
- Visual credits: `VISUAL_CREDITS.md`
- Captions (optional, burned in): `VIDEO_002_CAPTIONS_EN.srt`
- Eight Shorts: `../SHORTS/VIDEO_002_SH01.mp4` through `VIDEO_002_SH08.mp4`

Title: **{TITLE}**

Music: **none**. Harrison narration + original synthesised sound design (owner-approved V6).
"""

README = f"""# VIDEO 002 Publishing

Status: **READY**

- Upload master: `../DELIVERY/VIDEO_002_UPLOAD_MASTER_1080P.mp4`
- Thumbnail: `VIDEO_002_THUMBNAIL_YOUTUBE_1280x720.jpg`
- Human upload instructions: `\u0414\u0410\u041d\u041d\u042b\u0415 \u0414\u041b\u042f \u0417\u0410\u0413\u0420\u0423\u0417\u041a\u0418.txt`
- English description: `YOUTUBE_DESCRIPTION.txt`
- Metadata: `YOUTUBE_METADATA.json`
- Visual credits: `VISUAL_CREDITS.md`
- Eight Shorts: `../SHORTS/VIDEO_002_SH01.mp4` through `VIDEO_002_SH08.mp4`

No music. Thumbnail generated in Higgsfield (GPT Image 2, 4 concepts, owner picked #4).
"""

files = {
    "YOUTUBE_DESCRIPTION.txt": DESCRIPTION,
    "YOUTUBE_METADATA.json": json.dumps(META, indent=2, ensure_ascii=False) + "\n",
    "VISUAL_CREDITS.md": CREDITS_MD,
    "YOUTUBE_UPLOAD_PACKAGE.md": PACKAGE_MD,
    "README.md": README,
    "\u0414\u0410\u041d\u041d\u042b\u0415 \u0414\u041b\u042f \u0417\u0410\u0413\u0420\u0423\u0417\u041a\u0418.txt": RU,
}
for name, text in files.items():
    for d in (PUB, GIT):
        (d / name).write_text(text, encoding="utf-8-sig" if name.endswith(".txt") else "utf-8")
for d in (SHORTS, GIT):
    (d / "SHORTS_UPLOAD_TEXT_RU.txt").write_text("\n".join(shorts_txt), encoding="utf-8-sig")
shutil.copy2(HERE / "11_CAPTIONS.srt", PUB / "VIDEO_002_CAPTIONS_EN.srt")
print(chapters)
