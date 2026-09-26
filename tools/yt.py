#!/usr/bin/env python3
"""WHAT IT COST — video state keeper, media librarian, credit tracker and render QC.

Standard library only. status.yaml is written by this tool in a fixed layout,
so it is edited with targeted line replacements instead of a YAML parser.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VIDEOS = ROOT / "videos"
TEMPLATE = VIDEOS / "_template"
MEDIA_BASE = Path(os.environ.get("WIC_MEDIA", "C:/Users/KK/Documents/WhatItCost_media"))
FONTS_DIR = Path(os.environ.get("WIC_FONTS", "C:/Users/KK/Documents/WhatItCost_media/_fonts"))
MEDIA_DIRS = ["sources/pages", "voice", "images", "video_gen", "documents",
              "graphics", "renders", "shorts", "thumbnail"]

STAGES = ["qualification", "research", "script", "voice", "visual", "edit", "release", "published"]
GATES = ["g1_topic_go_and_concept", "g2_script_and_shorts_lock", "g3_voice_spend",
         "g4_images_accepted", "g5_video_gen_accepted", "g6_rough_cut",
         "g7_shorts_cut", "g8_packaging_choice"]
GATE_VALUES = {"NOT_STARTED", "WAITING_OWNER", "APPROVED", "REJECTED"}
CLAIM_STATUSES = {"ALLEGATION", "COMPLAINT", "CLAIM", "CHARGE", "RULING", "VERDICT",
                  "SETTLEMENT", "DISMISSAL", "CONVICTION", "ADMISSION", "DENIAL",
                  "UNDISPUTED_FACT", "REPORTED_FACT", "OPINION", "ANALYSIS", "UNKNOWN",
                  "SUPERSEDED"}
VISUAL_TYPES = {"document", "real_photo", "image", "video_gen", "graphic", "map"}
TODAY = dt.date.today().isoformat()


# ---------- helpers ----------

def die(msg: str) -> None:
    print("ERROR: " + msg)
    sys.exit(1)


def video_dir(vid: str) -> Path:
    vid = vid.zfill(3)
    hits = sorted(VIDEOS.glob(f"{vid}-*"))
    if not hits:
        die(f"no folder videos/{vid}-*")
    return hits[0]


def read_status(folder: Path) -> str:
    return (folder / "status.yaml").read_text(encoding="utf-8")


def write_status(folder: Path, text: str) -> None:
    (folder / "status.yaml").write_text(text, encoding="utf-8")


def q(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def get_scalar(text: str, key: str, indent: str = "") -> str:
    m = re.search(rf'^{indent}{re.escape(key)}:\s*(.*?)\s*(#.*)?$', text, re.M)
    if not m:
        return ""
    v = m.group(1)
    return json.loads(v) if v.startswith('"') else v


def set_scalar(text: str, key: str, value: str, indent: str = "", quote: bool = True) -> str:
    pat = re.compile(rf'^({indent}{re.escape(key)}:)[^\n#]*?(\s*#.*)?$', re.M)
    if not pat.search(text):
        die(f"status.yaml has no key {indent}{key}")
    val = q(value) if quote else value
    return pat.sub(lambda m: f"{m.group(1)} {val}{m.group(2) or ''}", text, count=1)


def append_list(text: str, key: str, item: dict) -> str:
    flow = "{" + ", ".join(f"{k}: {q(str(v)) if isinstance(v, str) else v}" for k, v in item.items()) + "}"
    if re.search(rf'^{key}: \[\][ \t]*$', text, re.M):
        return re.sub(rf'^{key}: \[\][ \t]*$', f"{key}:\n  - {flow}", text, count=1, flags=re.M)
    m = re.search(rf'^{key}:\n((?:  - .*\n?)*)', text, re.M)
    if not m:
        die(f"status.yaml has no list {key}")
    end = m.end()
    body = text[:end] if text[:end].endswith("\n") else text[:end] + "\n"
    return body + f"  - {flow}\n" + text[end:]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def media_root(folder: Path) -> Path:
    mr = get_scalar(read_status(folder), "media_root")
    return Path(mr) if mr else MEDIA_BASE / folder.name


# ---------- commands ----------

def cmd_new(a) -> None:
    vid = a.id.zfill(3)
    slug = re.sub(r"[^a-z0-9-]+", "-", a.slug.lower()).strip("-")
    if list(VIDEOS.glob(f"{vid}-*")):
        die(f"video {vid} already exists")
    folder = VIDEOS / f"{vid}-{slug}"
    shutil.copytree(TEMPLATE, folder)
    media = MEDIA_BASE / f"{vid}-{slug}"
    for d in MEDIA_DIRS:
        (media / d).mkdir(parents=True, exist_ok=True)
    t = read_status(folder)
    t = set_scalar(t, "video_id", vid)
    t = set_scalar(t, "slug", slug)
    t = set_scalar(t, "title_working", a.title)
    t = set_scalar(t, "topic_id", a.topic or "")
    t = set_scalar(t, "created", TODAY)
    t = set_scalar(t, "media_root", media.as_posix())
    t = set_scalar(t, "next_action", "Qualification: researcher (quick) + scout (competitors) + packaging (concepts)")
    t = t.replace("# Single source of truth for this video. Updated only via `python tools/yt.py`.",
                  f"# VIDEO {vid} — single source of truth. Update via `python tools/yt.py`.")
    write_status(folder, t)
    print(f"created {folder.relative_to(ROOT)}")
    print(f"media   {media}")


def cmd_status(a) -> None:
    folder = video_dir(a.id)
    t = read_status(folder)
    print(f"{folder.name}  —  {get_scalar(t, 'title_working')}")
    print(f"stage: {get_scalar(t, 'stage')}")
    print(f"next:  {get_scalar(t, 'next_action')}")
    print(f"concept: {get_scalar(t, 'packaging_concept') or '-'}")
    print("gates:")
    for g in GATES:
        print(f"  {g:28} {get_scalar(t, g, indent='  ')}")
    spent = sum(float(m) for m in re.findall(r'credits: ([0-9.]+)\}', t))
    print(f"credits spent: {spent:g}")
    print(f"media: {media_root(folder)}")


def cmd_stage(a) -> None:
    if a.stage not in STAGES:
        die("stage must be one of " + ", ".join(STAGES))
    folder = video_dir(a.id)
    t = set_scalar(read_status(folder), "stage", a.stage, quote=False)
    t = set_scalar(t, "next_action", a.next_action)
    write_status(folder, t)
    print(f"stage -> {a.stage}")


def cmd_gate(a) -> None:
    if a.gate not in GATES:
        hits = [g for g in GATES if g.startswith(a.gate)]
        if len(hits) != 1:
            die("gate must be one of " + ", ".join(GATES))
        a.gate = hits[0]
    if a.value not in GATE_VALUES:
        die("value must be one of " + ", ".join(sorted(GATE_VALUES)))
    folder = video_dir(a.id)
    t = set_scalar(read_status(folder), a.gate, a.value, indent="  ", quote=False)
    if a.value in ("APPROVED", "REJECTED"):
        t = append_list(t, "decisions", {"date": TODAY, "gate": a.gate, "decision": a.value, "note": a.note})
    write_status(folder, t)
    print(f"{a.gate} -> {a.value}")


def cmd_concept(a) -> None:
    folder = video_dir(a.id)
    write_status(folder, set_scalar(read_status(folder), "packaging_concept", a.text))
    print("packaging_concept set")


def cmd_hash(a) -> None:
    folder = video_dir(a.id)
    p = media_root(folder) / a.path
    if not p.is_file():
        die(f"not found: {p}")
    print(f"{sha256(p)}  {p.stat().st_size}  {a.path}")


def cmd_credit(a) -> None:
    folder = video_dir(a.id)
    t = append_list(read_status(folder), "credits",
                    {"date": TODAY, "provider": a.provider, "jobs": int(a.jobs),
                     "note": a.note, "credits": float(a.credits)})
    write_status(folder, t)
    print(f"logged {a.credits} credits ({a.provider}, {a.jobs} jobs)")


def run(cmd: list[str]) -> str:
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.stdout + r.stderr


def cmd_render_qc(a) -> None:
    folder = video_dir(a.id)
    p = media_root(folder) / a.path
    if not p.is_file():
        die(f"not found: {p}")
    probe = json.loads(run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(p)]))
    v = next((s for s in probe["streams"] if s["codec_type"] == "video"), {})
    au = next((s for s in probe["streams"] if s["codec_type"] == "audio"), {})
    dur = float(probe["format"]["duration"])
    loud = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(p), "-af", "ebur128=peak=true", "-f", "null", "-"])
    lufs = re.findall(r"I:\s+(-?[0-9.]+) LUFS", loud)
    peak = re.findall(r"Peak:\s+(-?[0-9.]+) dBFS", loud)
    black = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(p), "-vf", "blackdetect=d=0.3:pix_th=0.08",
                 "-an", "-f", "null", "-"])
    blacks = re.findall(r"black_start:([0-9.]+) black_end:([0-9.]+)", black)
    vertical = int(v.get("height", 0)) > int(v.get("width", 0))
    want = (1080, 1920) if vertical else (1920, 1080)
    checks = [
        ("resolution", f"{v.get('width')}x{v.get('height')}", (int(v.get("width", 0)), int(v.get("height", 0))) == want),
        ("fps", v.get("avg_frame_rate", "?"), v.get("avg_frame_rate") in ("25/1", "30/1", "24/1", "30000/1001")),
        ("video codec", v.get("codec_name", "?"), v.get("codec_name") == "h264"),
        ("audio", f"{au.get('codec_name', '-')} {au.get('sample_rate', '')}", bool(au)),
        ("duration", f"{dur:.3f} s", dur > 0),
        ("loudness", f"{lufs[-1] if lufs else '?'} LUFS", bool(lufs) and -17.0 <= float(lufs[-1]) <= -13.0),
        ("true peak", f"{peak[-1] if peak else '?'} dBFS", bool(peak) and float(peak[-1]) <= -1.0),
        ("black frames", f"{len(blacks)} segments", not [b for b in blacks if float(b[0]) > 0.5]),
    ]
    ok = all(c[2] for c in checks)
    lines = [f"# Render QC — {a.path} — {TODAY}", "", f"sha256: `{sha256(p)}`", "",
             "| Check | Value | Result |", "|---|---|---|"]
    lines += [f"| {n} | {val} | {'PASS' if good else 'FAIL'} |" for n, val, good in checks]
    if blacks:
        lines += ["", "Black segments: " + ", ".join(f"{float(s):.2f}–{float(e):.2f}" for s, e in blacks)]
    lines += ["", f"**Verdict: {'PASS' if ok else 'FAIL'}**", "",
              "Caption safe-zone and visual checks: see retention.md (manual)."]
    out = folder / "5_edit" / "render_qc.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


def cmd_check(a) -> None:
    folder = video_dir(a.id)
    t = read_status(folder)
    stage = get_scalar(t, "stage")
    upto = STAGES.index(stage) if stage in STAGES else 0
    errs: list[str] = []
    warns: list[str] = []

    def need(rel: str) -> None:
        p = folder / rel
        if not p.exists():
            errs.append(f"missing {rel}")
        elif p.suffix == ".csv" and not rows(p):
            errs.append(f"empty {rel}")
        elif p.suffix == ".md" and (TEMPLATE / rel).exists() and \
                (TEMPLATE / rel).read_text(encoding="utf-8") == p.read_text(encoding="utf-8"):
            errs.append(f"still template: {rel}")

    # gates must be approved before the stage that depends on them
    order = {"research": "g1_topic_go_and_concept", "voice": "g2_script_and_shorts_lock"}
    for st, g in order.items():
        if upto >= STAGES.index(st) and get_scalar(t, g, "  ") != "APPROVED":
            errs.append(f"stage {stage} but {g} is not APPROVED")

    if upto >= STAGES.index("qualification"):
        need("1_research/qualification.md")
    if upto >= STAGES.index("research") + 1 or (stage == "research" and a.strict):
        for f in ("research.md", "sources.csv", "claims.csv", "events.csv"):
            need(f"1_research/{f}")

    sources = {r["source_id"] for r in rows(folder / "1_research/sources.csv")}
    claims = rows(folder / "1_research/claims.csv")
    claim_ids = {c["claim_id"] for c in claims}
    for c in claims:
        if c.get("status") not in CLAIM_STATUSES:
            errs.append(f"claim {c['claim_id']}: bad status {c.get('status')!r}")
        if c.get("status") == "UNKNOWN":
            warns.append(f"claim {c['claim_id']} is UNKNOWN — must not be used in script")
        for s in filter(None, re.split(r"[;\s]+", c.get("source_ids", ""))):
            if s not in sources:
                errs.append(f"claim {c['claim_id']}: unknown source {s}")
        if not c.get("source_ids", "").strip():
            errs.append(f"claim {c['claim_id']}: no source")

    script = folder / "2_script/script.md"
    if upto >= STAGES.index("script") + 1:
        need("2_script/script.md")
        need("2_script/shorts.csv")
    if script.exists():
        s = script.read_text(encoding="utf-8")
        for tag in sorted(set(re.findall(r"\{(C[0-9]+)\}", s))):
            if tag not in claim_ids:
                errs.append(f"script tag {{{tag}}} not in claims.csv")
            else:
                st = next(c["status"] for c in claims if c["claim_id"] == tag)
                if st in ("UNKNOWN", "SUPERSEDED"):
                    errs.append(f"script uses {tag} with status {st}")
        if "{NEED:" in s:
            warns.append("script has open {NEED: …} flags")
        opens = set(re.findall(r"\[(SH[0-9]+)>\]", s))
        closes = set(re.findall(r"\[<(SH[0-9]+)\]", s))
        if opens != closes:
            errs.append(f"unbalanced Shorts markers: {sorted(opens ^ closes)}")

    if upto >= STAGES.index("voice") + 1:
        need("2_script/voice_script.md")
        if not get_scalar(t, "file", "  "):
            errs.append("voice.file not set in status.yaml")

    beats = rows(folder / "4_visual/beats.csv")
    if upto >= STAGES.index("visual") + 1 and not beats:
        errs.append("beats.csv empty")
    prev_end = 0.0
    fam_run: list[str] = []
    for b in beats:
        bid = b.get("beat_id", "?")
        try:
            st, en = float(b["start"]), float(b["end"])
        except (KeyError, ValueError):
            errs.append(f"{bid}: bad start/end")
            continue
        if st - prev_end > 0.5:
            warns.append(f"{bid}: gap {prev_end:.2f}–{st:.2f}")
        if en <= st:
            errs.append(f"{bid}: end <= start")
        prev_end = en
        if b.get("visual_type") not in VISUAL_TYPES:
            errs.append(f"{bid}: bad visual_type {b.get('visual_type')!r}")
        for cid in filter(None, re.split(r"[;\s]+", b.get("claim_ids", ""))):
            if cid not in claim_ids:
                errs.append(f"{bid}: unknown claim {cid}")
        fam_run = (fam_run + [b.get("family", "")])[-3:]
        if len(fam_run) == 3 and len(set(fam_run)) == 1 and fam_run[0]:
            warns.append(f"{bid}: family {fam_run[0]} three times in a row")
        if upto >= STAGES.index("edit") and b.get("status") != "ACCEPTED":
            warns.append(f"{bid}: asset not ACCEPTED ({b.get('status')})")

    mr = media_root(folder)
    for b in beats:
        f = b.get("asset_file", "").strip()
        if f and b.get("asset_sha256"):
            p = mr / f
            if not p.exists():
                errs.append(f"{b['beat_id']}: missing media {f}")
            elif a.hashes and sha256(p) != b["asset_sha256"]:
                errs.append(f"{b['beat_id']}: sha256 mismatch {f}")

    if upto >= STAGES.index("release"):
        rights = {r["asset_file"] for r in rows(folder / "6_release/rights.csv")}
        for b in beats:
            f = b.get("asset_file", "").strip()
            if f and f not in rights:
                errs.append(f"{b['beat_id']}: no rights row for {f}")

    print(f"{folder.name} — stage {stage}")
    for w in warns[:60]:
        print("WARN  " + w)
    for e in errs:
        print("FAIL  " + e)
    print("RESULT: " + ("FAIL" if errs else "PASS") + f" ({len(errs)} errors, {len(warns)} warnings)")
    sys.exit(1 if errs else 0)


# ---------- zero-token helpers that replace agent shell work ----------

def write_rows(path: Path, data: list[dict], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(data)


def csv_fields(path: Path) -> list[str]:
    with path.open(newline="", encoding="utf-8") as f:
        return next(csv.reader(f))


def slugify(text: str, n: int = 40) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", text).strip("_").upper()[:n] or "SOURCE"


def html_to_text(path: Path) -> Path:
    """Write readable text of an HTML file next to it (<name>.txt) so agents can read big pages."""
    from html.parser import HTMLParser

    class P(HTMLParser):
        skip = {"script", "style", "noscript", "svg", "nav", "footer", "header", "form"}

        def __init__(self):
            super().__init__()
            self.depth, self.out = 0, []

        def handle_starttag(self, tag, attrs):
            if tag in self.skip:
                self.depth += 1
            elif tag in ("p", "br", "h1", "h2", "h3", "li", "div", "tr", "blockquote"):
                self.out.append("\n")

        def handle_endtag(self, tag):
            if tag in self.skip and self.depth:
                self.depth -= 1

        def handle_data(self, data):
            if not self.depth and data.strip():
                self.out.append(data.strip() + " ")

    p = P()
    p.feed(path.read_text(encoding="utf-8", errors="replace"))
    text = re.sub(r"\n\s*\n+", "\n\n", "".join(p.out)).strip()
    out = path.with_suffix(".txt")
    out.write_text(text + "\n", encoding="utf-8")
    return out


def cmd_texts(a) -> None:
    """Extract .txt from every archived HTML source of a video."""
    folder = video_dir(a.id)
    for f in sorted((media_root(folder) / "sources").glob("*.html")):
        t = html_to_text(f)
        print(f"{f.name} -> {t.name} ({t.stat().st_size // 1024} KB)")


def cmd_fetch_sources(a) -> None:
    """Download tier-1/2 sources listed in sources.csv into media/sources and hash them."""
    import urllib.request
    folder = video_dir(a.id)
    path = folder / "1_research/sources.csv"
    data, fields = rows(path), csv_fields(path)
    out = media_root(folder) / "sources"
    out.mkdir(parents=True, exist_ok=True)
    ext_by_type = {"application/pdf": "pdf", "text/html": "html", "image/png": "png", "image/jpeg": "jpg"}
    ok = fail = 0
    for r in data:
        if r.get("media_file") or not r.get("url", "").startswith("http"):
            continue
        if r.get("tier", "").strip() not in ("1", "2") and not a.all:
            continue
        try:
            req = urllib.request.Request(r["url"], headers={"User-Agent": "Mozilla/5.0 (WhatItCost source archive)"})
            with urllib.request.urlopen(req, timeout=60) as resp:
                body = resp.read()
                ctype = resp.headers.get_content_type()
            ext = ext_by_type.get(ctype) or (r["url"].rsplit(".", 1)[-1].lower() if "." in r["url"][-6:] else "bin")
            name = f"{r['source_id']}_{slugify(r.get('title', ''))}.{ext}"
            (out / name).write_bytes(body)
            if ext == "html":
                html_to_text(out / name)
            r["media_file"] = f"sources/{name}"
            r["sha256"] = sha256(out / name)
            ok += 1
            print(f"OK    {r['source_id']}  {len(body)//1024} KB  {name}")
        except Exception as e:  # noqa: BLE001 — report and continue
            r["notes"] = (r.get("notes", "") + f" DOWNLOAD_FAILED: {e}").strip()
            fail += 1
            print(f"FAIL  {r['source_id']}  {e}")
    write_rows(path, data, fields)
    print(f"downloaded {ok}, failed {fail}")


def cmd_hash_beats(a) -> None:
    """Fill asset_sha256 in beats.csv for every row with an asset_file."""
    folder = video_dir(a.id)
    path = folder / "4_visual/beats.csv"
    data, fields = rows(path), csv_fields(path)
    mr, n, missing = media_root(folder), 0, []
    for r in data:
        f = r.get("asset_file", "").strip()
        if not f or (r.get("asset_sha256") and not a.all):
            continue
        p = mr / f
        if p.is_file():
            r["asset_sha256"] = sha256(p)
            n += 1
        else:
            missing.append(f"{r['beat_id']}: {f}")
    write_rows(path, data, fields)
    print(f"hashed {n}")
    for m in missing:
        print("MISSING " + m)


def cmd_words(a) -> None:
    """WeftCut transcribe_clip envelope (JSON file) -> 3_voice/words.json + captions.srt."""
    folder = video_dir(a.id)
    env = json.loads(Path(a.envelope).read_text(encoding="utf-8"))
    off = a.offset_us
    words, srt = [], []
    for i, seg in enumerate(env.get("segments", []), 1):
        for w in seg.get("words", []):
            words.append({"w": w["text"].strip(), "s": round((w["t_start_us"] - off) / 1e6, 3),
                          "e": round((w["t_end_us"] - off) / 1e6, 3)})

        def ts(us: int) -> str:
            ms = max(0, (us - off) // 1000)
            return f"{ms//3600000:02d}:{ms//60000%60:02d}:{ms//1000%60:02d},{ms%1000:03d}"
        srt.append(f"{i}\n{ts(seg['t_start_us'])} --> {ts(seg['t_end_us'])}\n{seg['text'].strip()}\n")
    (folder / "3_voice/words.json").write_text(json.dumps(words, ensure_ascii=False), encoding="utf-8")
    (folder / "3_voice/captions.srt").write_text("\n".join(srt), encoding="utf-8")
    print(f"{len(words)} words, {len(srt)} cues, word_timing={env.get('word_timing')}")


def norm_tokens(text: str) -> list[str]:
    return [t for t in re.sub(r"[^a-z0-9' ]+", " ", text.lower()).split() if t]


def cmd_audio_metrics(a) -> None:
    """Measure narration + diff transcript vs voice script -> 3_voice/audio_metrics.txt."""
    import difflib
    folder = video_dir(a.id)
    t = read_status(folder)
    rel = a.path or get_scalar(t, "file", "  ")
    if not rel:
        die("pass the audio path or set voice.file in status.yaml")
    p = media_root(folder) / rel
    if not p.is_file():
        die(f"not found: {p}")
    rep = [f"# Audio metrics — {rel} — {TODAY}", f"sha256 {sha256(p)}"]
    dur = float(json.loads(run(["ffprobe", "-v", "error", "-show_format", "-of", "json", str(p)]))["format"]["duration"])
    loud = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(p), "-af", "ebur128=peak=true", "-f", "null", "-"])
    I = re.findall(r"I:\s+(-?[0-9.]+) LUFS", loud)
    lra = re.findall(r"LRA:\s+(-?[0-9.]+) LU", loud)
    pk = re.findall(r"Peak:\s+(-?[0-9.]+) dBFS", loud)
    rep += [f"duration_sec {dur:.3f}", f"integrated_lufs {I[-1] if I else '?'} (target -16..-14)",
            f"loudness_range_lu {lra[-1] if lra else '?'}", f"true_peak_dbfs {pk[-1] if pk else '?'} (max -1.0)",
            f"clipping_risk {'YES' if pk and float(pk[-1]) > -0.3 else 'no'}"]
    sil = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(p), "-af", "silencedetect=noise=-45dB:d=1.5", "-f", "null", "-"])
    starts = re.findall(r"silence_start: ([0-9.]+)", sil)
    durs = re.findall(r"silence_duration: ([0-9.]+)", sil)
    rep.append(f"silences_over_1.5s {len(durs)}")
    rep += [f"  {float(s)//60:02.0f}:{float(s)%60:05.2f}  {float(d):.2f}s" for s, d in zip(starts, durs)]

    words_path, vs_path = folder / "3_voice/words.json", folder / "2_script/voice_script.md"
    if words_path.exists() and vs_path.exists():
        words = json.loads(words_path.read_text(encoding="utf-8"))
        script = "\n".join(l for l in vs_path.read_text(encoding="utf-8").splitlines() if not l.startswith("#"))
        exp = norm_tokens(script)
        heard_w = [(tok, w["s"]) for w in words for tok in norm_tokens(w["w"])]
        heard = [h[0] for h in heard_w]
        rep.append(f"words expected {len(exp)} / heard {len(heard)} / wpm {len(heard) / (dur / 60):.0f}")
        rep.append("mismatches (time — expected → heard):")
        sm = difflib.SequenceMatcher(a=exp, b=heard, autojunk=False)
        n = 0
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == "equal":
                continue
            at = heard_w[min(j1, len(heard_w) - 1)][1] if heard_w else 0
            has_digit = any(ch.isdigit() for ch in " ".join(exp[i1:i2] + heard[j1:j2]))
            flag = " [NUMBER]" if has_digit else ""
            rep.append(f"  {at//60:02.0f}:{at%60:05.2f}  {op}: \"{' '.join(exp[i1:i2])}\" → \"{' '.join(heard[j1:j2])}\"{flag}")
            n += 1
        rep.append(f"mismatch_count {n}")
    else:
        rep.append("transcript diff skipped: need 3_voice/words.json and 2_script/voice_script.md")
    out = folder / "3_voice/audio_metrics.txt"
    out.write_text("\n".join(rep) + "\n", encoding="utf-8")
    print("\n".join(rep[:12]))
    print(f"... written {out.relative_to(ROOT)}")


def cmd_frames(a) -> None:
    """Frames every N s + per-minute contact sheets + freeze/black report for a render."""
    folder = video_dir(a.id)
    p = media_root(folder) / a.path
    if not p.is_file():
        die(f"not found: {p}")
    base = media_root(folder) / "renders" / (p.stem + "_review")
    shutil.rmtree(base, ignore_errors=True)
    (base / "frames").mkdir(parents=True)
    fps = f"fps=1/{a.every}"
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(p), "-vf", f"{fps},scale=640:-2",
         str(base / "frames" / "f_%04d.jpg")])
    per_sheet = int(60 / a.every)
    cols = 6
    rows_n = -(-per_sheet // cols)
    run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(p), "-vf",
         f"{fps},scale=320:-2,tile={cols}x{rows_n}", str(base / "sheet_min%02d.jpg")])
    fr = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(p), "-vf",
              "freezedetect=n=0.003:d=8,blackdetect=d=0.3:pix_th=0.08", "-an", "-f", "null", "-"])
    freezes = re.findall(r"freeze_start: ([0-9.]+).*?freeze_duration: ([0-9.]+)", fr, re.S)
    blacks = re.findall(r"black_start:([0-9.]+) black_end:([0-9.]+)", fr)
    rep = [f"# Frames report — {a.path} — {TODAY}", f"frames: {base/'frames'} (every {a.every}s)",
           f"contact sheets: {base} (1 per minute, frame n = minute*60 + n*{a.every}s)",
           f"static stretches >8s: {len(freezes)}"]
    rep += [f"  {float(s)//60:02.0f}:{float(s)%60:05.2f}  {float(d):.1f}s" for s, d in freezes]
    rep.append(f"black segments: {len(blacks)}")
    rep += [f"  {float(s):.2f}–{float(e):.2f}" for s, e in blacks]
    out = folder / "5_edit/frames_report.txt"
    out.write_text("\n".join(rep) + "\n", encoding="utf-8")
    print("\n".join(rep))


def cmd_yt_search(a) -> None:
    """Real YouTube results (title, channel, subs, views, date, length) via yt-dlp — metadata only, no download."""
    import yt_dlp
    folder = video_dir(a.id)
    opts = {"quiet": True, "skip_download": True, "no_warnings": True, "extract_flat": False, "ignoreerrors": True}
    seen, found = set(), []
    with yt_dlp.YoutubeDL(opts) as ydl:
        for q in a.queries:
            res = ydl.extract_info(f"ytsearch{a.n}:{q}", download=False) or {}
            for e in res.get("entries") or []:
                if not e or e["id"] in seen:
                    continue
                seen.add(e["id"])
                d = e.get("upload_date") or ""
                found.append({"query": q, "title": e.get("title", ""), "channel": e.get("channel", ""),
                              "subs": e.get("channel_follower_count") or "", "views": e.get("view_count") or 0,
                              "date": f"{d[:4]}-{d[4:6]}-{d[6:]}" if d else "", "min": round((e.get("duration") or 0) / 60, 1),
                              "url": f"https://www.youtube.com/watch?v={e['id']}"})
    found.sort(key=lambda r: -int(r["views"] or 0))
    lines = [f"# YouTube search — captured {TODAY} (yt-dlp, metadata only)", "",
             "| Views | Published | Min | Channel (subs) | Title | URL | Query |", "|---|---|---|---|---|---|---|"]
    lines += [f"| {r['views']:,} | {r['date']} | {r['min']} | {r['channel']} ({r['subs']:,}) | {r['title'].replace('|', '/')} | {r['url']} | {r['query']} |"
              if isinstance(r['subs'], int) else
              f"| {r['views']:,} | {r['date']} | {r['min']} | {r['channel']} | {r['title'].replace('|', '/')} | {r['url']} | {r['query']} |"
              for r in found]
    out = folder / "1_research/yt_search.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:25]))
    print(f"{len(found)} videos -> {out.relative_to(ROOT)}")


def cmd_court(a) -> None:
    """CourtListener RECAP search (public API) -> dockets + downloadable PDF links -> 1_research/court_search.md."""
    import urllib.parse
    import urllib.request
    folder = video_dir(a.id)
    url = "https://www.courtlistener.com/api/rest/v4/search/?type=r&q=" + urllib.parse.quote(a.query)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (WhatItCost research)"})
    data = json.load(urllib.request.urlopen(req, timeout=60))
    lines = [f"# CourtListener search: {a.query} — {TODAY}", ""]
    for r in (data.get("results") or [])[:a.n]:
        lines.append(f"## {r.get('caseName')} — {r.get('docketNumber')} ({r.get('court_id')}), filed {r.get('dateFiled')}")
        lines.append(f"docket: https://www.courtlistener.com{r.get('docket_absolute_url', '')}")
        for d in r.get("recap_documents") or []:
            link = f"https://storage.courtlistener.com/{d['filepath_local']}" if d.get("is_available") and d.get("filepath_local") else "not in RECAP (PACER only)"
            lines.append(f"- #{d.get('document_number')} {d.get('entry_date_filed') or ''} {(d.get('description') or '').strip()[:110]} — {link}")
        lines.append("")
    out = folder / "1_research/court_search.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:30]))
    print(f"-> {out.relative_to(ROOT)}")


def cmd_pages(a) -> None:
    """Render PDF pages of archived sources to PNG (media/sources/pages/<source_id>_p<N>.png)."""
    import pymupdf
    folder = video_dir(a.id)
    mr = media_root(folder)
    wanted = set(a.sources.split(",")) if a.sources else None
    (mr / "sources/pages").mkdir(parents=True, exist_ok=True)
    for r in rows(folder / "1_research/sources.csv"):
        f = r.get("media_file", "")
        if not f.lower().endswith(".pdf") or (wanted and r["source_id"] not in wanted):
            continue
        doc = pymupdf.open(mr / f)
        pages = [int(x) for x in a.pages.split(",")] if a.pages else range(1, min(doc.page_count, a.max) + 1)
        for n in pages:
            if 1 <= n <= doc.page_count:
                doc[n - 1].get_pixmap(dpi=a.dpi).save(mr / f"sources/pages/{r['source_id']}_p{n}.png")
        print(f"{r['source_id']}: {len(list(pages))} of {doc.page_count} pages")


def ff_path(p: Path) -> str:
    return p.as_posix().replace(":", r"\:")


def cmd_doc_shots(a) -> None:
    """Render document shots from 4_visual/doc_shots.csv (page crop + red highlight + label) with ffmpeg."""
    folder = video_dir(a.id)
    spec = rows(folder / "4_visual/doc_shots.csv")
    if not spec:
        die("4_visual/doc_shots.csv is empty")
    mr = media_root(folder)
    font = FONTS_DIR / "ttf/Inter-Variable.ttf"
    if not font.is_file():
        die(f"font not found: {font}")
    (mr / "documents").mkdir(parents=True, exist_ok=True)
    tmp = mr / "documents" / "_label.txt"
    for r in spec:
        if a.only and r["beat_id"] not in a.only.split(","):
            continue
        src = mr / r["page_png"]
        if not src.is_file():
            print(f"MISSING {r['beat_id']}: {r['page_png']}")
            continue
        x, y, w, h = (int(float(r[k])) for k in ("crop_x", "crop_y", "crop_w", "crop_h"))
        s = min(1560 / w, 700 / h)
        W, H = int(w * s) // 2 * 2, int(h * s) // 2 * 2
        Y = max(120, 432 - H // 2)
        chain = [f"crop={w}:{h}:{x}:{y}"]
        if r.get("hl_w") and r.get("hl_h"):
            hx, hy, hw, hh = (int(float(r[k])) for k in ("hl_x", "hl_y", "hl_w", "hl_h"))
            chain.append(f"drawbox=x={hx - x}:y={hy - y}:w={hw}:h={hh}:color=0xD32222@0.22:t=fill")
            chain.append(f"drawbox=x={hx - x}:y={hy - y + hh}:w={hw}:h={max(3, int(4 / s))}:color=0xD32222@1:t=fill")
        chain.append(f"scale={W}:{H}")
        tmp.write_text(r.get("label", "").upper(), encoding="utf-8")
        X = (1920 - W) // 2
        fc = (f"color=c=0x1F1F1F:s=1920x1080:d=1[bg];[0:v]{','.join(chain)}[doc];"
              f"[bg]drawbox=x={X + 10}:y={Y + 12}:w={W}:h={H}:color=0x000000@0.55:t=fill[bg2];"
              f"[bg2][doc]overlay={X}:{Y},"
              f"drawbox=x={X}:y={Y - 52}:w=6:h=28:color=0xD32222@1:t=fill,"
              f"drawtext=fontfile='{ff_path(font)}':textfile='{ff_path(tmp)}':x={X + 20}:y={Y - 50}:"
              f"fontsize=24:fontcolor=0xEDEDED")
        out = mr / "documents" / f"{r['beat_id']}_{Path(r['page_png']).stem}.png"
        out.unlink(missing_ok=True)
        log = run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(src),
                   "-filter_complex", fc, "-frames:v", "1", str(out)])
        log = " ".join(l for l in log.splitlines() if "Fontconfig" not in l).strip()
        print(("OK    " if out.exists() else "FAIL  ") + f"{r['beat_id']} -> documents/{out.name} {log[:200]}")
    tmp.unlink(missing_ok=True)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("new"); s.add_argument("id"); s.add_argument("slug"); s.add_argument("title")
    s.add_argument("--topic", default=""); s.set_defaults(fn=cmd_new)
    s = sub.add_parser("status"); s.add_argument("id"); s.set_defaults(fn=cmd_status)
    s = sub.add_parser("check"); s.add_argument("id")
    s.add_argument("--hashes", action="store_true", help="re-hash media files")
    s.add_argument("--strict", action="store_true"); s.set_defaults(fn=cmd_check)
    s = sub.add_parser("stage"); s.add_argument("id"); s.add_argument("stage"); s.add_argument("next_action")
    s.set_defaults(fn=cmd_stage)
    s = sub.add_parser("gate"); s.add_argument("id"); s.add_argument("gate"); s.add_argument("value")
    s.add_argument("note", nargs="?", default=""); s.set_defaults(fn=cmd_gate)
    s = sub.add_parser("concept"); s.add_argument("id"); s.add_argument("text"); s.set_defaults(fn=cmd_concept)
    s = sub.add_parser("hash"); s.add_argument("id"); s.add_argument("path"); s.set_defaults(fn=cmd_hash)
    s = sub.add_parser("credit"); s.add_argument("id"); s.add_argument("provider"); s.add_argument("jobs")
    s.add_argument("credits"); s.add_argument("note", nargs="?", default=""); s.set_defaults(fn=cmd_credit)
    s = sub.add_parser("render-qc"); s.add_argument("id"); s.add_argument("path"); s.set_defaults(fn=cmd_render_qc)
    s = sub.add_parser("fetch-sources"); s.add_argument("id")
    s.add_argument("--all", action="store_true", help="also tier 3-4"); s.set_defaults(fn=cmd_fetch_sources)
    s = sub.add_parser("texts"); s.add_argument("id"); s.set_defaults(fn=cmd_texts)
    s = sub.add_parser("hash-beats"); s.add_argument("id")
    s.add_argument("--all", action="store_true", help="re-hash rows that already have sha"); s.set_defaults(fn=cmd_hash_beats)
    s = sub.add_parser("words"); s.add_argument("id"); s.add_argument("envelope", help="transcribe_clip JSON file")
    s.add_argument("--offset-us", type=int, default=0); s.set_defaults(fn=cmd_words)
    s = sub.add_parser("audio-metrics"); s.add_argument("id"); s.add_argument("path", nargs="?", default="")
    s.set_defaults(fn=cmd_audio_metrics)
    s = sub.add_parser("frames"); s.add_argument("id"); s.add_argument("path")
    s.add_argument("--every", type=int, default=2); s.set_defaults(fn=cmd_frames)
    s = sub.add_parser("yt-search"); s.add_argument("id"); s.add_argument("queries", nargs="+")
    s.add_argument("-n", type=int, default=10, help="results per query"); s.set_defaults(fn=cmd_yt_search)
    s = sub.add_parser("court"); s.add_argument("id"); s.add_argument("query")
    s.add_argument("-n", type=int, default=8); s.set_defaults(fn=cmd_court)
    s = sub.add_parser("pages"); s.add_argument("id"); s.add_argument("--sources", default="", help="S001,S004")
    s.add_argument("--pages", default="", help="1,3,7 (default: first --max pages)")
    s.add_argument("--max", type=int, default=30); s.add_argument("--dpi", type=int, default=200)
    s.set_defaults(fn=cmd_pages)
    s = sub.add_parser("doc-shots"); s.add_argument("id"); s.add_argument("--only", default="", help="B010,B011")
    s.set_defaults(fn=cmd_doc_shots)

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
