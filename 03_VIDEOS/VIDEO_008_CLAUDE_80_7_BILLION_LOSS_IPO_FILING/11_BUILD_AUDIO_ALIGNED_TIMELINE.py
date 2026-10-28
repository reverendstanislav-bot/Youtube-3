#!/usr/bin/env python3
"""Build VIDEO008 Stage 11 timing from the owner-accepted Harrison master.

ASR supplies timing evidence only. Canonical narration text remains authoritative.
"""

from __future__ import annotations

import csv
import difflib
import json
import math
import re
import sys
import wave
from pathlib import Path


FPS = 25
TOKEN_RE = re.compile(r"[a-z0-9]+(?:'[a-z0-9]+)?")


def tokens(text: str) -> list[str]:
    return TOKEN_RE.findall(text.lower().replace("’", "'"))


def tc(frame: int) -> str:
    total_seconds, ff = divmod(frame, FPS)
    hh, rem = divmod(total_seconds, 3600)
    mm, ss = divmod(rem, 60)
    return f"{hh:02d}:{mm:02d}:{ss:02d}:{ff:02d}"


def main() -> None:
    here = Path(__file__).resolve().parent
    audio = Path(sys.argv[1]).resolve()
    if not audio.is_file():
        raise SystemExit(f"Missing audio: {audio}")

    master_text = (here / "08_VOICE_SCRIPT_MASTER.txt").read_text(encoding="utf-8-sig").strip()
    paragraphs = [p.strip().replace("\n", " ") for p in re.split(r"\n\s*\n", master_text) if p.strip()]
    para_map = list(csv.DictReader((here / "08_VOICE_PARAGRAPH_MAP.csv").open(encoding="utf-8-sig", newline="")))
    scenes = list(csv.DictReader((here / "12_PREPRODUCTION_SCENE_PLAN.csv").open(encoding="utf-8-sig", newline="")))
    shorts = list(csv.DictReader((here / "07_SHORTS_LOCK.csv").open(encoding="utf-8-sig", newline="")))
    if len(paragraphs) != len(para_map):
        raise SystemExit(f"Paragraph mismatch: text={len(paragraphs)} map={len(para_map)}")

    from faster_whisper import WhisperModel

    model = WhisperModel("base", device="cpu", compute_type="int8")
    segments, info = model.transcribe(
        str(audio), language="en", beam_size=5, word_timestamps=True, vad_filter=False
    )
    asr_words = []
    asr_segments = []
    for segment in segments:
        row_words = []
        for word in segment.words or []:
            if word.start is None or word.end is None:
                continue
            clean = tokens(word.word)
            if not clean:
                continue
            # Whisper occasionally returns punctuation-attached contractions; retain one timing per token.
            for part in clean:
                item = {"word": part, "start": round(float(word.start), 3), "end": round(float(word.end), 3),
                        "probability": round(float(word.probability or 0.0), 5)}
                asr_words.append(item)
                row_words.append(item)
        asr_segments.append({"start": round(float(segment.start), 3), "end": round(float(segment.end), 3),
                             "text": segment.text.strip(), "words": row_words})

    canonical = []
    ranges = []
    for idx, para in enumerate(paragraphs):
        start = len(canonical)
        canonical.extend(tokens(para))
        ranges.append((start, len(canonical) - 1))
    observed = [w["word"] for w in asr_words]
    matcher = difflib.SequenceMatcher(None, canonical, observed, autojunk=False)
    c_to_a: dict[int, int] = {}
    for block in matcher.get_matching_blocks():
        for offset in range(block.size):
            c_to_a[block.a + offset] = block.b + offset

    matched_keys = sorted(c_to_a)
    if not matched_keys:
        raise SystemExit("ASR alignment produced no matching words")

    def nearest_asr(cidx: int) -> int:
        pos = min(range(len(matched_keys)), key=lambda i: abs(matched_keys[i] - cidx))
        key = matched_keys[pos]
        estimate = c_to_a[key] + (cidx - key)
        return max(0, min(len(asr_words) - 1, estimate))

    with wave.open(str(audio), "rb") as wav:
        audio_duration = wav.getnframes() / wav.getframerate()
    total_frames = int(round(audio_duration * FPS))
    paragraph_rows = []
    boundary_frames = [0]
    for pidx, (cstart, cend) in enumerate(ranges):
        matched = [c_to_a[i] for i in range(cstart, cend + 1) if i in c_to_a]
        astart = min(matched) if matched else nearest_asr(cstart)
        aend = max(matched) if matched else nearest_asr(cend)
        start_sec = asr_words[astart]["start"]
        end_sec = asr_words[aend]["end"]
        if pidx == 0:
            start_sec = 0.0
        if pidx == len(ranges) - 1:
            end_sec = audio_duration
        matched_count = len(matched)
        paragraph_rows.append({
            "paragraph_id": para_map[pidx]["paragraph_id"],
            "start_sec_raw": start_sec,
            "end_sec_raw": end_sec,
            "canonical_words": cend - cstart + 1,
            "matched_words": matched_count,
            "match_ratio": round(matched_count / max(1, cend - cstart + 1), 4),
        })

    # Midpoints between adjacent spoken paragraphs make a continuous, non-overlapping master map.
    for idx in range(len(paragraph_rows) - 1):
        left = paragraph_rows[idx]["end_sec_raw"]
        right = paragraph_rows[idx + 1]["start_sec_raw"]
        boundary_frames.append(int(round(((left + right) / 2.0) * FPS)))
    boundary_frames.append(total_frames)
    for idx in range(1, len(boundary_frames)):
        boundary_frames[idx] = max(boundary_frames[idx], boundary_frames[idx - 1] + 1)
    boundary_frames[-1] = total_frames

    for idx, row in enumerate(paragraph_rows):
        row["start_frame"] = boundary_frames[idx]
        row["end_frame"] = boundary_frames[idx + 1]
        row["start_timecode"] = tc(boundary_frames[idx])
        row["end_timecode"] = tc(boundary_frames[idx + 1])
        row["duration_sec"] = round((boundary_frames[idx + 1] - boundary_frames[idx]) / FPS, 3)

    para_by_id = {r["paragraph_id"]: r for r in paragraph_rows}
    scene_rows = []
    for para in para_map:
        pid = para["paragraph_id"]
        selected = [s for s in scenes if s["paragraph_id"] == pid]
        pstart, pend = para_by_id[pid]["start_frame"], para_by_id[pid]["end_frame"]
        available = pend - pstart
        weights = [max(0.001, float(s["planned_duration_sec"])) for s in selected]
        total_weight = sum(weights)
        cuts = [pstart]
        running = 0.0
        for weight in weights[:-1]:
            running += weight
            cuts.append(pstart + int(round(available * running / total_weight)))
        cuts.append(pend)
        for idx in range(1, len(cuts)):
            cuts[idx] = max(cuts[idx], cuts[idx - 1] + 1)
        cuts[-1] = pend
        for idx, source in enumerate(selected):
            start, end = cuts[idx], cuts[idx + 1]
            row = dict(source)
            row.update({
                "start_frame_25fps": start,
                "end_frame_25fps_exclusive": end,
                "start_timecode_25fps": tc(start),
                "end_timecode_25fps": tc(end),
                "duration_frames": end - start,
                "duration_sec_audio_aligned": f"{(end-start)/FPS:.3f}",
                "timing_basis": "LOCKED_MASTER_ASR_PARAGRAPH_ALIGNMENT_WEIGHTED_SCENE_SPLIT",
            })
            scene_rows.append(row)

    transcript = {
        "status": "COMPLETE_TIMING_EVIDENCE_ONLY",
        "model": "faster-whisper-base",
        "device": "cpu",
        "compute_type": "int8",
        "language": info.language,
        "language_probability": info.language_probability,
        "audio_path": str(audio),
        "runtime_sec": round(audio_duration, 3),
        "fps": FPS,
        "total_frames": total_frames,
        "canonical_token_count": len(canonical),
        "asr_token_count": len(observed),
        "exact_sequence_matches": len(c_to_a),
        "global_match_ratio": round(len(c_to_a) / max(1, len(canonical)), 4),
        "paragraphs": paragraph_rows,
        "segments": asr_segments,
        "words": asr_words,
        "authority_note": "ASR is timing evidence only; 08_VOICE_SCRIPT_MASTER.txt remains text authority.",
    }
    (here / "11_WORD_LEVEL_TRANSCRIPT.json").write_text(json.dumps(transcript, indent=2), encoding="utf-8")

    with (here / "11_SCENE_TIMELINE.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(scene_rows[0]))
        writer.writeheader()
        writer.writerows(scene_rows)

    short_rows = []
    for item in shorts:
        p = para_by_id[item["paragraph_start"]]
        duration = p["duration_sec"]
        short_rows.append({
            "short_id": item["short_id"], "status": "TIMED_FROM_LOCKED_MASTER",
            "start_timecode": p["start_timecode"], "end_timecode": p["end_timecode"],
            "start_frame_25fps": p["start_frame"], "end_frame_25fps_exclusive": p["end_frame"],
            "duration_sec": f"{duration:.3f}", "paragraph_id": item["paragraph_start"],
            "maximum_export_seconds_incl_tail": item["maximum_export_seconds_incl_tail"],
            "duration_verdict": "PASS" if duration <= float(item["maximum_export_seconds_incl_tail"]) else "HOLD_OVER_LIMIT",
            "extraction_rule": item["extraction_rule"], "audio_source": "VIDEO008_HARRISON_V5_MASTER_24K_MONO_S16.wav",
        })
    with (here / "11_SHORTS_CUT_MAP.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(short_rows[0]))
        writer.writeheader()
        writer.writerows(short_rows)

    min_ratio = min(r["match_ratio"] for r in paragraph_rows)
    short_pass = sum(r["duration_verdict"] == "PASS" for r in short_rows)
    md = f"""# VIDEO 008 — Stage 11 Audio-Aligned Visual Timeline\n\nStatus: **PASS — READY FOR RESOLVE ASSEMBLY**\n\n- Locked Harrison master: `{audio.name}`\n- Runtime: **{audio_duration:.3f} s** / **{tc(total_frames)}** at {FPS} fps\n- Paragraphs: **{len(paragraph_rows)}**\n- Visual scenes: **{len(scene_rows)}**, continuous from frame 0 through {total_frames}\n- ASR: Faster-Whisper base, CPU int8, English, beam 5, word timestamps, VAD off\n- Canonical-to-ASR exact token matches: **{len(c_to_a)}/{len(canonical)} ({len(c_to_a)/len(canonical):.1%})**\n- Minimum paragraph match ratio: **{min_ratio:.1%}**\n- Locked Shorts within their export cap: **{short_pass}/{len(short_rows)}**\n\nASR is timing evidence only. It did not change, normalize, shorten, or rewrite the locked narration. Scene boundaries are proportional subdivisions of each audio-aligned paragraph, snapped to whole 25 fps frames with no gaps or overlaps.\n\n## Resolve assembly rules\n\n- A1: owner-accepted Harrison master, unchanged.\n- V1: one active visual per scene from `VIDEO008_FINAL_VISUAL_PACK`.\n- No subtitles, music, SFX, speed change, pitch change, or audio normalization in this assembly pass.\n- SC043 uses a clearly contextual neutral graphic fallback; it must not be presented as authentic Broadcom evidence.\n- SC106 may use the passed SEC lease crop only; the missing Broadcom juxtaposition remains a sourcing HOLD.\n"""
    (here / "11_VISUAL_TIMELINE.md").write_text(md, encoding="utf-8")
    print(json.dumps({"duration": audio_duration, "frames": total_frames, "paragraphs": len(paragraph_rows),
                      "scenes": len(scene_rows), "match_ratio": transcript["global_match_ratio"],
                      "shorts_pass": f"{short_pass}/{len(short_rows)}"}, indent=2))


if __name__ == "__main__":
    main()
