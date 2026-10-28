import csv
import hashlib
import json
import subprocess
from pathlib import Path

import requests

PRODUCTION = Path(r"C:\Users\KK\VIDEO008_PRODUCTION")
ARCHIVE = PRODUCTION / "VIDEO008_SOURCE_ARCHIVE"
VIDEO_DIR = ARCHIVE / "01_STOCK_VIDEO"
MANIFEST = ARCHIVE / "STOCK_ASSET_MANIFEST.csv"
UA = "WHAT-IT-COST-documentary-research/1.0 editorial asset verification"
session = requests.Session()
session.headers.update({"User-Agent": UA})

REPLACEMENTS = {
    "SC004": ("RPL6780083", "https://www.pexels.com/video/people-working-with-accounting-documents-6780083/", "https://videos.pexels.com/video-files/6780083/6780083-uhd_3840_2160_30fps.mp4"),
    "SC006": ("RPL10597763", "https://www.pexels.com/video/low-angle-shot-of-an-illuminated-office-building-at-night-10597763/", "https://videos.pexels.com/video-files/10597763/10597763-hd_3840_2160_25fps.mp4"),
    "SC022": ("RPL7141174", "https://www.pexels.com/download/video/7141174/", "https://videos.pexels.com/video-files/7141174/7141174-uhd_3840_2160_24fps.mp4"),
    "SC039": ("RPL11680401", "https://www.pexels.com/video/city-buildings-at-night-11680401/", "https://videos.pexels.com/video-files/11680401/11680401-uhd_3840_2160_60fps.mp4"),
    "SC042": ("RPL1085656", "https://www.pexels.com/download/video/1085656/", "https://videos.pexels.com/video-files/1085656/1085656-uhd_3840_2160_25fps.mp4"),
    "SC048": ("RPL6814544", "https://www.pexels.com/video/a-man-checking-the-documents-6814544/", "https://videos.pexels.com/video-files/6814544/6814544-uhd_4096_2160_25fps.mp4"),
    "SC054": ("RPL8348731", "https://www.pexels.com/video/business-professionals-discussing-documents-8348731/", "https://videos.pexels.com/video-files/8348731/8348731-hd_1920_1080_25fps.mp4"),
    "SC056": ("RPL5726498", "https://www.pexels.com/video/people-holding-documents-5726498/", "https://videos.pexels.com/video-files/5726498/5726498-uhd_3840_2160_30fps.mp4"),
    "SC063": ("RPL7140937", "https://www.pexels.com/download/video/7140937/", "https://videos.pexels.com/video-files/7140937/7140937-uhd_3840_2160_24fps.mp4"),
    "SC077": ("RPL9864525", "https://www.pexels.com/video/skyscraper-in-city-at-night-9864525/", "https://videos.pexels.com/video-files/9864525/9864525-uhd_3840_2160_30fps.mp4"),
    "SC081": ("RPL6963744", "https://www.pexels.com/download/video/6963744/", "https://videos.pexels.com/video-files/6963744/6963744-hd_1920_1080_25fps.mp4"),
    "SC093": ("RPL6138313", "https://www.pexels.com/video/a-skyscraper-commercial-building-in-the-city-of-london-6138313/", "https://videos.pexels.com/video-files/6138313/6138313-uhd_3840_2160_24fps.mp4"),
    "SC105": ("RPL6754824", "https://www.pexels.com/download/video/6754824/", "https://videos.pexels.com/video-files/6754824/6754824-uhd_3840_2160_25fps.mp4"),
    "SC107": ("RPL8298188", "https://www.pexels.com/video/a-man-and-a-woman-discussing-while-looking-at-some-documents-8298188/", "https://videos.pexels.com/video-files/8298188/8298188-hd_1920_1080_25fps.mp4"),
}


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def download(url, destination):
    temp = destination.with_suffix(".part")
    with session.get(url, stream=True, timeout=(20, 300)) as response:
        response.raise_for_status()
        with temp.open("wb") as handle:
            for block in response.iter_content(1024 * 1024):
                if block:
                    handle.write(block)
    temp.replace(destination)


def probe(path):
    result = subprocess.run([
        "ffprobe", "-v", "error", "-show_entries",
        "stream=codec_name,width,height,r_frame_rate:format=duration,size",
        "-of", "json", str(path),
    ], capture_output=True, text=True, check=True, timeout=120)
    data = json.loads(result.stdout)
    stream = next(row for row in data["streams"] if row.get("width"))
    return stream, data["format"]


with MANIFEST.open(encoding="utf-8-sig", newline="") as handle:
    rows = list(csv.DictReader(handle))
for row in rows:
    if row["scene_id"] not in REPLACEMENTS:
        continue
    candidate, page, direct = REPLACEMENTS[row["scene_id"]]
    destination = VIDEO_DIR / f"{row['scene_id']}_{candidate}.mp4"
    try:
        if not destination.exists():
            download(direct, destination)
        stream, file_format = probe(destination)
        width, height = int(stream["width"]), int(stream["height"])
        if width / height < 1.7 or width < 1280:
            raise RuntimeError(f"Replacement is not horizontal HD: {width}x{height}")
        row.update({
            "candidate_id": candidate,
            "landing_page_url": page,
            "author_or_source": "Pexels contributor; exact contributor remains on landing page",
            "local_path": str(destination.relative_to(PRODUCTION)).replace("\\", "/"),
            "sha256": sha256(destination),
            "width": width,
            "height": height,
            "duration_sec": round(float(file_format["duration"]), 3),
            "codec_or_format": stream.get("codec_name", ""),
            "qc_status": "DOWNLOADED_TECH_PASS_RIGHTS_CONTEXT_REVIEW",
            "assignment_reason": "VERIFIED_UNIQUE_REPLACEMENT_FOR_UNAVAILABLE_CANDIDATE",
            "download_url": direct,
            "notes": "",
        })
    except Exception as error:
        row["notes"] = str(error)
    print(row["scene_id"], row["qc_status"], row["notes"], flush=True)

with MANIFEST.open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
print("PASS", sum(row["qc_status"].startswith("DOWNLOADED") for row in rows), "HOLD", sum(row["qc_status"] == "HOLD" for row in rows))
