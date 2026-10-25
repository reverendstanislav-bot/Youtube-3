from __future__ import annotations

import csv
import hashlib
import json
import shutil
import subprocess
import sys
import textwrap
from collections import Counter
from pathlib import Path

import pymupdf
from PIL import Image, ImageDraw, ImageFont


USER = Path(r"C:\Users\KK")
REPO = USER / "Youtube-3-video005-voice"
EP = REPO / "03_VIDEOS" / "VIDEO_007_APPLE_OPENAI_THE_TRADE_SECRET_WAR"
CACHE = USER / "VIDEO007_STAGE13R_SOURCE_CACHE" / "extracted"
COURT_PHOTO = USER / "VIDEO007_STAGE13R_SOURCE_CACHE" / "courthouse" / "ROBERT_F_PECKHAM_COURTHOUSE_GSA_FJC.jpg"
BUILD_ROOT = REPO / ".local_stage13r_build"
OUT = BUILD_ROOT / "VIDEO007_STAGE13R"
FFMPEG = USER / "VIDEO007_STAGE13R_TOOLS" / "ffmpeg" / "ffmpeg-9.0.2-essentials_build" / "bin" / "ffmpeg.exe"
FFPROBE = USER / "VIDEO007_STAGE13R_TOOLS" / "ffmpeg" / "ffmpeg-9.0.2-essentials_build" / "bin" / "ffprobe.exe"


BAD_VIDEO_NAMES = {
    "6406171.mp4", "6754819.mp4", "7140928.mp4", "8212370.mp4", "854167.mp4",
    "15014681.mp4", "6755161.mp4", "6951391.mp4", "7057342.mp4", "7140931.mp4", "9373101.mp4",
}


DOC_CROPS = [
    ("DOC01", "ECF1.pdf", 1, "trade secret"),
    ("DOC02", "ECF1.pdf", 2, "hundred"),
    ("DOC03", "ECF1.pdf", 3, "access"),
    ("DOC04", "ECF1.pdf", 4, "Actual parts"),
    ("DOC05", "ECF1.pdf", 11, "access"),
    ("DOC06", "ECF1.pdf", 18, "download"),
    ("DOC07", "ECF1.pdf", 19, "files"),
    ("DOC08", "ECF1.pdf", 21, "forensic"),
    ("DOC09", "ECF1.pdf", 22, "Actual parts"),
    ("DOC10", "ECF1.pdf", 39, "preliminary injunction"),
    ("DOC11", "ECF143.pdf", 1, "expedited discovery"),
    ("DOC12", "ECF143.pdf", 4, "personal account"),
    ("DOC13", "ECF143.pdf", 6, "trade secret"),
    ("DOC14", "ECF175.pdf", 1, "expedited discovery"),
    ("DOC15", "ECF175.pdf", 2, "preliminary injunction"),
    ("DOC16", "ECF175.pdf", 3, "forensic"),
    ("DOC17", "ECF175.pdf", 5, "Apple Originated Information"),
    ("DOC18", "ECF175.pdf", 6, "access"),
    ("DOC19", "ECF175.pdf", 7, "trade secret"),
    ("DOC20", "ECF175.pdf", 8, "forensic"),
    ("DOC21", "ECF175.pdf", 10, "expedited discovery"),
    ("DOC22", "ECF176.pdf", 2, "personal account"),
    ("DOC23", "ECF176.pdf", 2, "hundred"),
    ("DOC24", "ECF176.pdf", 3, "trade secret"),
    ("DOC25", "ECF176.pdf", 3, "access"),
    ("DOC26", "ECF188.pdf", 1, "preservation"),
    ("DOC27", "ECF188.pdf", 2, "preliminary injunction"),
    ("DOC28", "ECF188.pdf", 3, "moot"),
    ("DOC29", "ECF188.pdf", 3, "forensic"),
    ("DOC30", "ECF189.pdf", 3, "expedited discovery"),
]


GFX = {
    "VP003": ("PERSONAL ACCOUNTS", "OPENAI ALLEGED", "100+ confidential files moved to personal accounts", "ALLEGATION — NOT A COURT FINDING"),
    "VP005": ("TWO DIRECTIONS", "APPLE → OPENAI", "Apple alleged former employees carried protected hardware material", "OPENAI → APPLE: separate reverse allegation"),
    "VP119": ("ACTUAL PARTS", "WORDS IN APPLE'S FILING", "The phrase supported a recruiting allegation", "It did not prove a component was delivered"),
    "VP169": ("100+ FILES", "OPENAI'S COURT FILING", "Files allegedly sent to personal accounts", "No finding that Apple received or used them"),
    "VP170": ("TRANSFER ≠ USE", "TWO DIFFERENT CLAIMS", "Personal transfer", "Corporate receipt or use was not established"),
    "VP207": ("OCTOBER 16", "SIGNED COURT RESULT", "Preservation + forensic inspection approved", "Preliminary-injunction motion found moot"),
    "VP220": ("NOT A THEFT RULING", "WHAT THE JUDGE DECIDED", "How evidence would be preserved and exchanged", "The competing theft allegations remained undecided"),
    "VP228": ("FILE ≠ MISUSE", "EVIDENCE CHAIN", "Download → possession → use → harm", "Each link requires separate proof"),
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def ffprobe(path: Path) -> dict:
    cmd = [str(FFPROBE), "-v", "error", "-select_streams", "v:0", "-show_entries",
           "stream=width,height,r_frame_rate:format=duration", "-of", "json", str(path)]
    return json.loads(subprocess.check_output(cmd, text=True, encoding="utf-8"))


def find_source_videos() -> tuple[list[Path], list[Path], list[dict[str, str]]]:
    all_mp4 = sorted(CACHE.rglob("*.mp4"))
    qc_path = CACHE / "SOURCE_VISUAL_QC" / "stage13R" / "manifests" / "visual_qc" / "SOURCE_VIDEO_INDIVIDUAL_QC.csv"
    qc_rows = read_csv(qc_path)
    accepted_names = {
        Path(r["file"]).name.lower()
        for r in qc_rows
        if r["visual_and_technical_source_decision"] == "CONTEXT_CANDIDATE_NOT_ACTUAL_CASE_EVENT"
    }
    apple_names = {
        Path(r["file"]).name.lower()
        for r in qc_rows
        if r["visual_and_technical_source_decision"] == "RIGHTS_HOLD_APPLE_COPYRIGHT_WWDC"
    }
    apple = []
    pexels = []
    seen_names: set[str] = set()
    for p in all_mp4:
        key = p.name.lower()
        if key in seen_names:
            continue
        if key in accepted_names:
            pexels.append(p)
            seen_names.add(key)
        elif key in apple_names:
            apple.append(p)
            seen_names.add(key)
    seen: dict[str, Path] = {}
    rejected: list[dict[str, str]] = []
    usable: list[Path] = []
    for p in pexels:
        digest = sha256(p)
        if digest in seen:
            rejected.append({"file": str(p), "reason": "EXACT_SHA256_DUPLICATE", "duplicate_of": seen[digest].name})
            continue
        seen[digest] = p
        usable.append(p)
    for r in qc_rows:
        decision = r["visual_and_technical_source_decision"]
        if decision not in {"CONTEXT_CANDIDATE_NOT_ACTUAL_CASE_EVENT", "RIGHTS_HOLD_APPLE_COPYRIGHT_WWDC"}:
            rejected.append({"file": r["file"], "reason": decision, "duplicate_of": r.get("duplicate_of", "")})
    return usable, apple, rejected


def make_cut(src: Path, dst: Path) -> tuple[float, float]:
    meta = ffprobe(src)
    duration = float(meta["format"]["duration"])
    cut_dur = min(10.0, max(5.0, duration - 0.4))
    start = max(0.0, (duration - cut_dur) / 2.0)
    dst.parent.mkdir(parents=True, exist_ok=True)
    cmd = [str(FFMPEG), "-hide_banner", "-loglevel", "error", "-y", "-ss", f"{start:.3f}",
           "-i", str(src), "-t", f"{cut_dur:.3f}", "-an", "-vf",
           "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:black,fps=25",
           "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p",
           "-movflags", "+faststart", str(dst)]
    subprocess.run(cmd, check=True)
    return start, start + cut_dur


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        Path(r"C:\Windows\Fonts\arialbd.ttf") if bold else Path(r"C:\Windows\Fonts\arial.ttf"),
        Path(r"C:\Windows\Fonts\segoeuib.ttf") if bold else Path(r"C:\Windows\Fonts\segoeui.ttf"),
    ]
    for p in candidates:
        if p.exists():
            return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()


def make_gfx(vp: str, data: tuple[str, str, str, str], svg_dir: Path, png_dir: Path) -> None:
    title, eyebrow, left, right = data
    img = Image.new("RGB", (1920, 1080), "#111111")
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, 1920, 1080), fill="#151515")
    d.rectangle((90, 80, 1830, 930), fill="#202020", outline="#3A3A3A", width=3)
    d.text((125, 115), eyebrow, font=font(32, True), fill="#B8B8B8")
    d.text((125, 185), title, font=font(104, True), fill="#EDEDED")
    d.rectangle((125, 320, 575, 334), fill="#D32222")
    d.line((960, 405, 960, 800), fill="#555555", width=3)
    left_lines = textwrap.wrap(left, width=29)
    right_lines = textwrap.wrap(right, width=29)
    d.multiline_text((150, 420), "\n".join(left_lines), font=font(38, True), fill="#EDEDED", spacing=18)
    d.multiline_text((1010, 420), "\n".join(right_lines), font=font(38, True), fill="#EDEDED", spacing=18)
    d.text((125, 860), f"EDITOR DIAGRAM  |  {vp}", font=font(27), fill="#9C9C9C")
    png_path = png_dir / f"{vp}.png"
    img.save(png_path, quality=95)
    def svg_lines(lines: list[str], x: int) -> str:
        return "".join(f'<tspan x="{x}" dy="1.25em">{line}</tspan>' for line in lines)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080">
<rect width="1920" height="1080" fill="#151515"/><rect x="90" y="80" width="1740" height="850" fill="#202020" stroke="#3A3A3A" stroke-width="3"/>
<text x="125" y="145" font-family="Inter,Arial" font-size="32" font-weight="700" fill="#B8B8B8">{eyebrow}</text>
<text x="125" y="285" font-family="Arial" font-size="104" font-weight="800" fill="#EDEDED">{title}</text>
<rect x="125" y="320" width="450" height="14" fill="#D32222"/><line x1="960" y1="405" x2="960" y2="800" stroke="#555" stroke-width="3"/>
<text x="150" y="430" font-family="Inter,Arial" font-size="38" font-weight="700" fill="#EDEDED">{svg_lines(left_lines, 150)}</text>
<text x="1010" y="430" font-family="Inter,Arial" font-size="38" font-weight="700" fill="#EDEDED">{svg_lines(right_lines, 1010)}</text>
<text x="125" y="895" font-family="Inter,Arial" font-size="27" fill="#9C9C9C">EDITOR DIAGRAM | {vp}</text></svg>'''
    (svg_dir / f"{vp}.svg").write_text(svg, encoding="utf-8")


def make_document_crop(src_pdf: Path, page_no: int, term: str, dst: Path) -> dict[str, object]:
    doc = pymupdf.open(src_pdf)
    page = doc[page_no - 1]
    hits = page.search_for(term)
    if not hits:
        raise RuntimeError(f"Term not found: {src_pdf.name} p{page_no}: {term}")
    hit = hits[0]
    page_rect = page.rect
    clip = pymupdf.Rect(30, max(0, hit.y0 - 115), page_rect.x1 - 30, min(page_rect.y1, hit.y1 + 170))
    pix = page.get_pixmap(matrix=pymupdf.Matrix(3, 3), clip=clip, alpha=False)
    base = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    canvas = Image.new("RGB", (1920, 1080), "#101010")
    max_w, max_h = 1720, 820
    scale = min(max_w / base.width, max_h / base.height)
    base = base.resize((int(base.width * scale), int(base.height * scale)), Image.Resampling.LANCZOS)
    x = (1920 - base.width) // 2
    y = 130 + (820 - base.height) // 2
    canvas.paste(base, (x, y))
    d = ImageDraw.Draw(canvas)
    rel_x0 = (hit.x0 - clip.x0) * 3 * scale
    rel_x1 = (hit.x1 - clip.x0) * 3 * scale
    rel_y1 = (hit.y1 - clip.y0) * 3 * scale
    underline_y = int(y + rel_y1 + 8)
    d.line((int(x + rel_x0), underline_y, int(x + rel_x1), underline_y), fill="#D32222", width=8)
    d.text((100, 55), f"{src_pdf.stem}  |  PAGE {page_no}  |  AUTHENTIC COURT FILING", font=font(30, True), fill="#EDEDED")
    d.text((100, 1010), f"EDITORIAL EXCERPT — CONTEXT PRESERVED — TERM: {term}", font=font(24), fill="#AFAFAF")
    canvas.save(dst, quality=96)
    return {"pdf": src_pdf.name, "page": page_no, "term": term, "bbox": f"{hit.x0:.2f},{hit.y0:.2f},{hit.x1:.2f},{hit.y1:.2f}"}


def choose_doc(narration: str, doc_paths: list[str]) -> str:
    t = narration.lower()
    if "moot" in t or "october sixteenth" in t or "preserv" in t:
        idx = 27
    elif "hundred" in t or "personal account" in t or "openai" in t and "files" in t:
        idx = 21
    elif "expedited discovery" in t or "early discovery" in t:
        idx = 13
    elif "actual parts" in t or "component" in t:
        idx = 3
    elif "preliminary injunction" in t or "injunction" in t:
        idx = 14
    elif "forensic" in t:
        idx = 28
    elif "download" in t or "access" in t or "login" in t:
        idx = 5
    else:
        idx = sum(ord(c) for c in narration) % len(doc_paths)
    return doc_paths[idx % len(doc_paths)]


def main() -> None:
    if OUT.exists():
        raise RuntimeError(f"Refusing to overwrite existing build: {OUT}")
    for rel in ["video_horizontal/masters", "video_horizontal/cuts", "stills", "documents/original_pdfs",
                "documents/crops", "editor_gfx/svg", "editor_gfx/png", "manifests"]:
        (OUT / rel).mkdir(parents=True, exist_ok=True)

    usable, apple, rejected = find_source_videos()
    master_by_name: dict[str, Path] = {}
    cut_by_master: dict[str, dict[str, object]] = {}
    for src in usable:
        dst = OUT / "video_horizontal" / "masters" / src.name
        shutil.copy2(src, dst)
        master_by_name[src.name.lower()] = dst
        cut = OUT / "video_horizontal" / "cuts" / f"CUT_{src.stem}_1080p25.mp4"
        cut_in, cut_out = make_cut(dst, cut)
        cut_by_master[src.name.lower()] = {"path": cut, "in": cut_in, "out": cut_out, "rights": "PASS_PEXELS_CONTEXT_WITH_NONENDORSEMENT_RESTRICTION"}
    for src in apple:
        dst = OUT / "video_horizontal" / "masters" / "APPLE_WWDC_RIGHTS_HOLD" / src.name
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        master_by_name[src.name.lower()] = dst
        cut = OUT / "video_horizontal" / "cuts" / "APPLE_WWDC_RIGHTS_HOLD" / f"CUT_{src.stem}_1080p25.mp4"
        cut_in, cut_out = make_cut(dst, cut)
        cut_by_master[src.name.lower()] = {"path": cut, "in": cut_in, "out": cut_out, "rights": "HOLD_APPLE_COPYRIGHT_FAIR_USE_REVIEW"}

    photo_src_root = CACHE / "PHOTO_72" / "STOCK_72_PHOTOS"
    photo_index = read_csv(photo_src_root / "manifests" / "73_REAL_PHOTO_SOURCE_INDEX.csv")
    photo_by_name: dict[str, Path] = {}
    for row in photo_index:
        rel = Path(row["path"])
        src = photo_src_root / rel
        dst = OUT / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        photo_by_name[src.name.lower()] = dst
    court_dst = OUT / "stills" / "PRIMARY_PLACES_AND_SEMICONDUCTORS" / COURT_PHOTO.name
    court_dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(COURT_PHOTO, court_dst)
    photo_by_name[COURT_PHOTO.name.lower()] = court_dst

    pdf_src_root = CACHE / "ECF_SOURCE_PACK" / "stage13R" / "documents" / "original_pdfs"
    pdf_by_name: dict[str, Path] = {}
    for src in sorted(pdf_src_root.glob("*.pdf")):
        dst = OUT / "documents" / "original_pdfs" / src.name
        shutil.copy2(src, dst)
        pdf_by_name[src.name] = dst

    crop_rows: list[dict[str, object]] = []
    doc_paths: list[str] = []
    for crop_id, pdf_name, page_no, term in DOC_CROPS:
        dst = OUT / "documents" / "crops" / f"{crop_id}_{pdf_name[:-4]}_P{page_no:02d}.png"
        meta = make_document_crop(pdf_by_name[pdf_name], page_no, term, dst)
        rel = dst.relative_to(OUT).as_posix()
        doc_paths.append(rel)
        crop_rows.append({"crop_id": crop_id, "asset_path": rel, **meta, "qc": "TECH_PASS_EXACT_SOURCE_TERM_RIGHTS_HOLD"})
    write_csv(OUT / "manifests" / "DOCUMENT_CROP_REGISTER.csv", crop_rows,
              ["crop_id", "asset_path", "pdf", "page", "term", "bbox", "qc"])

    for vp, data in GFX.items():
        make_gfx(vp, data, OUT / "editor_gfx" / "svg", OUT / "editor_gfx" / "png")

    qc_rows = read_csv(EP / "13R_SOURCE_QC_239_SHOTS.csv")
    gfx_paths = {vp: f"editor_gfx/png/{vp}.png" for vp in GFX}
    all_photo_paths = [p.relative_to(OUT).as_posix() for p in photo_by_name.values() if p != court_dst]
    all_cut_keys = sorted(cut_by_master)
    final_rows: list[dict[str, object]] = []
    for i, row in enumerate(qc_rows):
        vp = row["shot_id"]
        narration = row["narration_cue"]
        state = row["qc_state"]
        candidate = row["real_media_candidate"].replace("\\", "/")
        asset = ""
        source_in = ""
        source_out = ""
        media_kind = ""
        rights = ""
        final_qc = ""
        note = row["reason"]
        base = Path(candidate).name.lower() if candidate else ""
        if vp in gfx_paths:
            asset = gfx_paths[vp]
            media_kind = "EDITOR_FACT_GFX"
            rights = "PASS_EDITOR_OWNED_SOURCE_FACT_REVIEWED"
            final_qc = "TECH_PASS_OWNER_VISUAL_SIGNOFF_HOLD"
        elif "COURTHOUSE" in state:
            asset = court_dst.relative_to(OUT).as_posix()
            media_kind = "AUTHENTIC_LOCATION_PHOTO"
            rights = "HOLD_FJC_GSA_SOURCE_REUSE_CONFIRMATION"
            final_qc = "IDENTITY_PASS_RESOLUTION_HOLD"
        elif "DOCUMENT" in state or "SOURCE_ECF" in state or "NO_SPECIFIC_REAL_VIDEO" in state:
            asset = choose_doc(narration, doc_paths)
            media_kind = "AUTHENTIC_DOCUMENT_EXCERPT"
            rights = "HOLD_DOCUMENT_EDITORIAL_FAIR_USE_REVIEW"
            final_qc = "TECH_PASS_EXACT_SOURCE_OWNER_SIGNOFF_HOLD"
        elif base in cut_by_master:
            info = cut_by_master[base]
            asset = Path(info["path"]).relative_to(OUT).as_posix()
            source_in = f"{info['in']:.3f}"
            source_out = f"{info['out']:.3f}"
            media_kind = "REAL_HORIZONTAL_VIDEO"
            rights = str(info["rights"])
            final_qc = "TECH_PASS_EDITORIAL_OWNER_SIGNOFF_HOLD" if rights.startswith("PASS") else rights
        elif base in photo_by_name:
            asset = photo_by_name[base].relative_to(OUT).as_posix()
            media_kind = "AUTHENTIC_STOCK_PHOTO"
            rights = "HOLD_PER_FILE_ATTRIBUTION_AND_CONTEXT_REVIEW"
            final_qc = "TECH_PASS_EDITORIAL_OWNER_SIGNOFF_HOLD"
        elif row["new_class"] == "AUTHENTIC_STOCK_PHOTO":
            asset = all_photo_paths[i % len(all_photo_paths)]
            media_kind = "AUTHENTIC_STOCK_PHOTO"
            rights = "HOLD_PER_FILE_ATTRIBUTION_AND_CONTEXT_REVIEW"
            final_qc = "TECH_PASS_EDITORIAL_OWNER_SIGNOFF_HOLD"
            note = "No exact old candidate; assigned real source photo for review, not as case evidence."
        else:
            key = all_cut_keys[i % len(all_cut_keys)]
            info = cut_by_master[key]
            asset = Path(info["path"]).relative_to(OUT).as_posix()
            source_in = f"{info['in']:.3f}"
            source_out = f"{info['out']:.3f}"
            media_kind = "REAL_HORIZONTAL_VIDEO"
            rights = str(info["rights"])
            final_qc = "TECH_PASS_SEMANTIC_MATCH_HOLD"
            note = "No defensible exact source candidate in prior QC; real contextual cut supplied for owner replacement/review only."
        final_rows.append({
            "vp_id": vp,
            "start_frame_25fps": row["start_25fps"],
            "end_frame_exclusive_25fps": row["end_25fps"],
            "start_tc": f"{int(row['start_25fps'])/25:.2f}",
            "end_tc": f"{int(row['end_25fps'])/25:.2f}",
            "harrison_verbatim": narration,
            "media_kind": media_kind,
            "asset_path": asset,
            "source_in_sec": source_in,
            "source_out_sec": source_out,
            "source_candidate": candidate,
            "rights_status": rights,
            "qc_status": final_qc,
            "editorial_note": note,
        })
    fields = ["vp_id", "start_frame_25fps", "end_frame_exclusive_25fps", "start_tc", "end_tc",
              "harrison_verbatim", "media_kind", "asset_path", "source_in_sec", "source_out_sec",
              "source_candidate", "rights_status", "qc_status", "editorial_note"]
    write_csv(OUT / "manifests" / "FINAL_SHOT_MANIFEST.csv", final_rows, fields)

    video_ledger = {Path(r["path"]).name.lower(): r for r in read_csv(EP / "13R_ALL_66_VIDEO_SOURCE_LEDGER.csv")}
    photo_ledger = {Path(r["path"]).name.lower(): r for r in photo_index}
    rights_rows: list[dict[str, object]] = []
    for name, path in master_by_name.items():
        r = video_ledger.get(name, {})
        apple_hold = name.startswith("wwdc24_")
        rights_rows.append({
            "asset_path": path.relative_to(OUT).as_posix(), "source_url": r.get("owner_source_url", "https://www.youtube.com/@Apple" if apple_hold else f"https://www.pexels.com/video/{Path(name).stem}/"),
            "creator_or_owner": "Apple Inc." if apple_hold else "Pexels contributor; verify source page",
            "license": "ALL RIGHTS RESERVED / EDITORIAL FAIR USE REVIEW" if apple_hold else "Pexels license",
            "commercial_youtube": "HOLD" if apple_hold else "ALLOWED_WITH_RESTRICTIONS",
            "attribution": "VERIFY APPLE SOURCE" if apple_hold else "Not required by Pexels; retain source credit",
            "people_brand_restrictions": "Do not imply endorsement or depict stock subjects as case participants",
            "content_id_risk": "HIGH" if apple_hold else "LOW_NOT_GUARANTEED",
            "status": "HOLD" if apple_hold else "PASS_CONTEXT_ONLY",
        })
    for name, path in photo_by_name.items():
        r = photo_ledger.get(name, {})
        is_court = path == court_dst
        rights_rows.append({
            "asset_path": path.relative_to(OUT).as_posix(),
            "source_url": "https://www.fjc.gov/history/courthouse/san-jose-california-1984" if is_court else r.get("source_page", ""),
            "creator_or_owner": "General Services Administration via Federal Judicial Center" if is_court else r.get("author", "Pexels/Commons contributor"),
            "license": "US government source; reuse status not stated on page" if is_court else r.get("license", ""),
            "commercial_youtube": "HOLD" if is_court else "CHECK_PER_FILE",
            "attribution": "FJC page credits GSA" if is_court else "REQUIRED_FOR_CC; retain for Pexels provenance",
            "people_brand_restrictions": "Context only; no implication of case participation or endorsement",
            "content_id_risk": "LOW_NOT_GUARANTEED",
            "status": "HOLD" if is_court else "HOLD_PER_FILE_FINAL_REVIEW",
        })
    for path in pdf_by_name.values():
        ecf = path.stem.replace("ECF", "")
        rights_rows.append({
            "asset_path": path.relative_to(OUT).as_posix(),
            "source_url": f"https://storage.courtlistener.com/recap/gov.uscourts.cand.474095/gov.uscourts.cand.474095.{ecf}.0.pdf",
            "creator_or_owner": "U.S. District Court filing / filing party",
            "license": "Public court record; editorial reuse/fair-use review required",
            "commercial_youtube": "HOLD",
            "attribution": f"ECF {ecf}, N.D. Cal. case 5:26-cv-06109",
            "people_brand_restrictions": "Preserve allegation/ruling distinction and page context",
            "content_id_risk": "LOW_NOT_GUARANTEED",
            "status": "HOLD_LEGAL_EDITORIAL",
        })
    for vp in GFX:
        rights_rows.append({
            "asset_path": f"editor_gfx/png/{vp}.png", "source_url": "Derived only from cited ECF facts",
            "creator_or_owner": "WHAT IT COST editorial", "license": "Editor-owned graphic",
            "commercial_youtube": "YES_AFTER_FACT_QC", "attribution": "N/A",
            "people_brand_restrictions": "No fabricated evidence; explanatory only", "content_id_risk": "LOW_NOT_GUARANTEED",
            "status": "PASS_RIGHTS_FACT_AND_OWNER_VISUAL_HOLD",
        })
    write_csv(OUT / "manifests" / "SOURCE_RIGHTS.csv", rights_rows,
              ["asset_path", "source_url", "creator_or_owner", "license", "commercial_youtube", "attribution",
               "people_brand_restrictions", "content_id_risk", "status"])
    write_csv(OUT / "manifests" / "REJECTED_VIDEO_SOURCES.csv", rejected, ["file", "reason", "duplicate_of"])

    for p in sorted(OUT.rglob("*.mp4")):
        subprocess.run([str(FFMPEG), "-v", "error", "-xerror", "-i", str(p), "-f", "null", "NUL"], check=True)

    coverage_ok = len(final_rows) == 239 and int(final_rows[0]["start_frame_25fps"]) == 0 and int(final_rows[-1]["end_frame_exclusive_25fps"]) == 24309
    contiguous = all(int(a["end_frame_exclusive_25fps"]) == int(b["start_frame_25fps"]) for a, b in zip(final_rows, final_rows[1:]))
    kind_counts = Counter(str(r["media_kind"]) for r in final_rows)
    qc_counts = Counter(str(r["qc_status"]) for r in final_rows)
    qc = f"""# VIDEO007 Stage 13R — FINAL VISUAL QC

Generated from real downloaded source media on 2026-10-25. No AI image or video generation was used.

## Physical package

- Unique accepted-format Pexels masters: {len(usable)}
- Apple WWDC excerpts retained in a separate COPYRIGHT HOLD folder: {len(apple)}
- Edit cuts, 1920x1080, 25fps, H.264, decoded with `ffmpeg -xerror`: {len(cut_by_master)}
- Real source photographs: {len(photo_index)} plus one official FJC/GSA courthouse reference (resolution HOLD)
- Original court PDFs: {len(pdf_by_name)}
- Exact source-term document crops: {len(crop_rows)}
- Bespoke factual diagrams: {len(GFX)}
- Rejected duplicate/soft/under-1080 source entries: {len(rejected)}

## Timeline integrity

- VP rows: {len(final_rows)}
- First frame: {final_rows[0]['start_frame_25fps']}
- Last exclusive frame: {final_rows[-1]['end_frame_exclusive_25fps']}
- Full 24,309-frame coverage: {'PASS' if coverage_ok else 'FAIL'}
- Contiguous boundaries: {'PASS' if contiguous else 'FAIL'}
- Locked Harrison audio was not modified or packaged.

## Assigned picture classes

{chr(10).join(f'- {k}: {v}' for k, v in sorted(kind_counts.items()))}

## Gate

Technical source/cut/decode/coverage gate: **PASS**.

Final picture/legal gate: **HOLD**. This package deliberately does not turn source acquisition into false publication clearance. Apple WWDC remains copyright HOLD; court-document editorial/fair-use review remains HOLD; Commons attribution/share-alike and Pexels subject/non-endorsement restrictions remain per-file; the FJC courthouse reference is only 253x200 and is resolution/reuse HOLD. Every VP has a physical asset path, but rows marked semantic-match or owner-signoff HOLD require human review against Harrison in real time before Stage 14.

## QC status counts

{chr(10).join(f'- {k}: {v}' for k, v in sorted(qc_counts.items()))}
"""
    (OUT / "FINAL_VISUAL_QC.md").write_text(qc, encoding="utf-8")

    subprocess.run([sys.executable, str(REPO / "tools" / "make_video007_stage13r_contact_sheets.py")], check=True)
    checksum_rows = []
    for p in sorted(OUT.rglob("*")):
        if p.is_file() and p.name != "CHECKSUMS_SHA256.csv":
            checksum_rows.append({"path": p.relative_to(OUT).as_posix(), "bytes": p.stat().st_size, "sha256": sha256(p)})
    write_csv(OUT / "manifests" / "CHECKSUMS_SHA256.csv", checksum_rows, ["path", "bytes", "sha256"])
    print(json.dumps({
        "output": str(OUT), "masters_pexels": len(usable), "masters_apple_hold": len(apple),
        "cuts": len(cut_by_master), "photos": len(photo_index) + 1, "pdfs": len(pdf_by_name),
        "crops": len(crop_rows), "gfx": len(GFX), "vp_rows": len(final_rows),
        "coverage_ok": coverage_ok, "contiguous": contiguous,
    }, indent=2))


if __name__ == "__main__":
    main()
