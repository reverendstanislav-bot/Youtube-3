import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import urlparse

import requests
from PIL import Image

EPISODE = Path(__file__).resolve().parents[2]
PRODUCTION = Path(r"C:\Users\KK\VIDEO008_PRODUCTION")
ARCHIVE = PRODUCTION / "VIDEO008_SOURCE_ARCHIVE"
VIDEO_DIR = ARCHIVE / "01_STOCK_VIDEO"
PHOTO_DIR = ARCHIVE / "02_STOCK_PHOTOS"
DOC_DIR = ARCHIVE / "03_ORIGINAL_DOCUMENTS"
LICENSE_DIR = ARCHIVE / "06_LICENSES"
PREVIEW_DIR = ARCHIVE / "07_PREVIEWS"
for directory in [VIDEO_DIR, PHOTO_DIR, DOC_DIR, LICENSE_DIR, PREVIEW_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

PEXELS_LICENSE = "https://www.pexels.com/license/"
UA = "WHAT-IT-COST-documentary-research/1.0 editorial asset verification"
session = requests.Session()
session.headers.update({"User-Agent": UA, "Accept": "*/*"})


def read_csv(name):
    with (EPISODE / name).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path, rows):
    assert rows
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def tokens(value):
    return set(re.findall(r"[a-z0-9]+", value.lower()))


def similarity(requirement, candidate):
    left = tokens(requirement["brief"])
    right = tokens(candidate["category"] + " " + candidate["visual_description"])
    return len(left & right) / max(1, len(left | right))


def media_id(url):
    ids = re.findall(r"(\d{5,})", url)
    return ids[-1] if ids else ""


def download(url, destination):
    temp = destination.with_suffix(destination.suffix + ".part")
    with session.get(url, stream=True, timeout=(20, 180), allow_redirects=True) as response:
        response.raise_for_status()
        with temp.open("wb") as handle:
            for block in response.iter_content(1024 * 1024):
                if block:
                    handle.write(block)
    temp.replace(destination)


def curl_download(url, destination):
    command = [
        "curl.exe", "-L", "--fail", "--silent", "--show-error",
        "-A", "Mozilla/5.0 (compatible; WHAT-IT-COST/1.0; editorial@whatitcost.media)",
        "-H", "Accept: text/html,application/xhtml+xml,application/pdf,*/*",
        url, "-o", str(destination),
    ]
    subprocess.run(command, check=True, timeout=300)


def resolve_video(video_id):
    variants = [
        ("hd", 1920, 1080),
        ("uhd", 3840, 2160),
        ("uhd", 2560, 1440),
        ("uhd", 4096, 2160),
        ("hd", 1280, 720),
    ]
    rates = [25, 30, 24, 60, 50]
    for quality, width, height in variants:
        for rate in rates:
            url = f"https://videos.pexels.com/video-files/{video_id}/{video_id}-{quality}_{width}_{height}_{rate}fps.mp4"
            try:
                response = session.head(url, timeout=(10, 30), allow_redirects=True)
                if response.status_code == 200 and int(response.headers.get("Content-Length", "1")) > 100_000:
                    return url
            except requests.RequestException:
                pass
    return ""


def probe_video(path):
    command = [
        "ffprobe", "-v", "error", "-show_entries",
        "stream=codec_name,width,height,r_frame_rate:format=duration,size",
        "-of", "json", str(path),
    ]
    result = subprocess.run(command, capture_output=True, text=True, timeout=90, check=True)
    data = json.loads(result.stdout)
    video_stream = next(stream for stream in data["streams"] if stream.get("width"))
    return {
        "codec": video_stream.get("codec_name", ""),
        "width": int(video_stream["width"]),
        "height": int(video_stream["height"]),
        "fps": video_stream.get("r_frame_rate", ""),
        "duration_sec": round(float(data["format"]["duration"]), 3),
    }


requirements = read_csv("12_STOCK_SHOT_REQUIREMENTS.csv")
library = read_csv("12_STOCK_CANDIDATE_LIBRARY.csv")
by_id = {row["candidate_id"]: row for row in library}
available = {
    "STOCK_VIDEO": [row for row in library if row["kind"] == "STOCK_VIDEO" and media_id(row["landing_page_url"])],
    "STOCK_PHOTO": [row for row in library if row["kind"] == "STOCK_PHOTO" and media_id(row["landing_page_url"])],
}
used = set()
assignment = []
for requirement in requirements:
    media = requirement["media"]
    original = by_id.get(requirement["candidate_id"])
    if original and original in available[media] and original["candidate_id"] not in used:
        selected = original
        reason = "CURRENT_PLAN_UNIQUE_CANDIDATE"
    else:
        choices = [row for row in available[media] if row["candidate_id"] not in used]
        if not choices:
            assignment.append({**requirement, "selected_candidate_id": "", "selected_page_url": "", "assignment_reason": "HOLD_NO_UNIQUE_CANDIDATE"})
            continue
        selected = max(choices, key=lambda row: similarity(requirement, row))
        reason = "UNIQUE_REPLACEMENT_FOR_REPEAT_OR_SEARCH"
    used.add(selected["candidate_id"])
    assignment.append({
        **requirement,
        "selected_candidate_id": selected["candidate_id"],
        "selected_page_url": selected["landing_page_url"],
        "selected_description": selected["visual_description"],
        "assignment_reason": reason,
    })

assert len(assignment) == 65
assert len({row["selected_candidate_id"] for row in assignment if row["selected_candidate_id"]}) == 65

stock_manifest = []
for index, row in enumerate(assignment, 1):
    scene = row["scene_id"]
    media = row["media"]
    candidate_id = row["selected_candidate_id"]
    page_url = row["selected_page_url"]
    asset_id = media_id(page_url)
    record = {
        "scene_id": scene,
        "media": media,
        "candidate_id": candidate_id,
        "landing_page_url": page_url,
        "author_or_source": "Pexels contributor; exact contributor remains on landing page",
        "license": "Pexels License",
        "license_url": PEXELS_LICENSE,
        "commercial_youtube": "YES_WITH_PEXELS_RESTRICTIONS_AND_NO_ENDORSEMENT",
        "local_path": "",
        "sha256": "",
        "width": "",
        "height": "",
        "duration_sec": "",
        "codec_or_format": "",
        "qc_status": "HOLD",
        "assignment_reason": row["assignment_reason"],
        "brief": row["brief"],
        "download_url": "",
        "notes": "",
    }
    try:
        if media == "STOCK_VIDEO":
            direct = resolve_video(asset_id)
            if not direct:
                raise RuntimeError("No 16:9 HD CDN variant resolved")
            destination = VIDEO_DIR / f"{scene}_{candidate_id}_{asset_id}.mp4"
            if not destination.exists():
                download(direct, destination)
            metadata = probe_video(destination)
            record.update({
                "local_path": str(destination.relative_to(PRODUCTION)).replace("\\", "/"),
                "sha256": sha256(destination),
                "width": metadata["width"],
                "height": metadata["height"],
                "duration_sec": metadata["duration_sec"],
                "codec_or_format": metadata["codec"],
                "download_url": direct,
            })
            if metadata["width"] / metadata["height"] < 1.7 or metadata["width"] < 1280:
                raise RuntimeError(f"Video is not acceptable horizontal HD: {metadata}")
            record["qc_status"] = "DOWNLOADED_TECH_PASS_RIGHTS_CONTEXT_REVIEW"
        else:
            direct = f"https://images.pexels.com/photos/{asset_id}/pexels-photo-{asset_id}.jpeg"
            destination = PHOTO_DIR / f"{scene}_{candidate_id}_{asset_id}.jpg"
            if not destination.exists():
                download(direct, destination)
            with Image.open(destination) as image:
                image.verify()
            with Image.open(destination) as image:
                width, height = image.size
                image_format = image.format
            record.update({
                "local_path": str(destination.relative_to(PRODUCTION)).replace("\\", "/"),
                "sha256": sha256(destination),
                "width": width,
                "height": height,
                "codec_or_format": image_format,
                "download_url": direct,
            })
            if min(width, height) < 1920:
                raise RuntimeError(f"Photo is below high-resolution threshold: {width}x{height}")
            record["qc_status"] = (
                "DOWNLOADED_TECH_PASS_RIGHTS_CONTEXT_REVIEW"
                if width > height
                else "DOWNLOADED_TECH_PASS_VERTICAL_ORIGINAL_16X9_CROP_REQUIRED_RIGHTS_CONTEXT_REVIEW"
            )
    except Exception as error:
        record["qc_status"] = "HOLD"
        record["notes"] = str(error)
    stock_manifest.append(record)
    print(f"STOCK {index:02d}/65 {scene} {record['qc_status']}", flush=True)

required_source_ids = set()
for task in read_csv("12_DOCUMENT_GRAPHIC_TASKS.csv"):
    if task["media_class"] == "AUTHENTIC_EVIDENCE":
        required_source_ids.update(task["source_ids"].split("|"))
source_rows = {row["source_id"]: row for row in read_csv("SOURCE_INDEX.csv")}
document_manifest = []
for source_id in sorted(required_source_ids):
    source = source_rows[source_id]
    url = source["url"]
    suffix = Path(urlparse(url).path).suffix.lower()
    if suffix not in [".pdf", ".htm", ".html"]:
        suffix = ".pdf" if "static-files" in url else ".html"
    destination = DOC_DIR / f"{source_id}_{re.sub(r'[^A-Za-z0-9]+', '_', source['title']).strip('_')[:70]}{suffix}"
    record = {
        "source_id": source_id,
        "title": source["title"],
        "publisher": source["publisher"],
        "original_url": url,
        "local_path": "",
        "sha256": "",
        "bytes": "",
        "content_type": "",
        "rights_basis": "Primary-source documentary quotation/display; context and attribution required; final rights review Stage16",
        "qc_status": "HOLD",
        "notes": "",
    }
    try:
        if not destination.exists():
            try:
                download(url, destination)
            except Exception:
                curl_download(url, destination)
        head = destination.read_bytes()[:8]
        if destination.suffix == ".pdf" and not head.startswith(b"%PDF"):
            raise RuntimeError("Expected PDF magic not present")
        if destination.suffix in [".htm", ".html"] and b"<" not in head:
            raise RuntimeError("Expected HTML content not present")
        record.update({
            "local_path": str(destination.relative_to(PRODUCTION)).replace("\\", "/"),
            "sha256": sha256(destination),
            "bytes": destination.stat().st_size,
            "content_type": destination.suffix.lstrip("."),
            "qc_status": "DOWNLOADED_PRIMARY_SOURCE_TECH_PASS_CROP_PENDING",
        })
    except Exception as error:
        record["notes"] = str(error)
    document_manifest.append(record)
    print(f"DOC {source_id} {record['qc_status']}", flush=True)

(LICENSE_DIR / "PEXELS_LICENSE_REFERENCE.txt").write_text(
    "Pexels License verified 2026-10-27\n"
    "Official license: https://www.pexels.com/license/\n"
    "Commercial-use help: https://help.pexels.com/hc/en-us/articles/360042295214-Can-I-use-the-photos-and-videos-for-a-commercial-project\n\n"
    "Recorded scope: free commercial use and modification; attribution not required. Do not imply endorsement, depict identifiable people in an offensive/bad-light context, resell standalone assets, or ignore third-party trademark/privacy rights. Each asset retains its individual landing-page URL.\n",
    encoding="utf-8",
)
write_csv(ARCHIVE / "STOCK_ASSET_MANIFEST.csv", stock_manifest)
write_csv(ARCHIVE / "DOCUMENT_SOURCE_MANIFEST.csv", document_manifest)
write_csv(ARCHIVE / "STOCK_ASSIGNMENT_PLAN.csv", assignment)
summary = {
    "stock_total": len(stock_manifest),
    "stock_pass": sum(row["qc_status"].startswith("DOWNLOADED") for row in stock_manifest),
    "stock_hold": sum(row["qc_status"] == "HOLD" for row in stock_manifest),
    "video_pass": sum(row["media"] == "STOCK_VIDEO" and row["qc_status"].startswith("DOWNLOADED") for row in stock_manifest),
    "photo_pass": sum(row["media"] == "STOCK_PHOTO" and row["qc_status"].startswith("DOWNLOADED") for row in stock_manifest),
    "documents_total": len(document_manifest),
    "documents_pass": sum(row["qc_status"].startswith("DOWNLOADED") for row in document_manifest),
    "documents_hold": sum(row["qc_status"] == "HOLD" for row in document_manifest),
}
(ARCHIVE / "DOWNLOAD_SUMMARY.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
print(json.dumps(summary, indent=2), flush=True)
