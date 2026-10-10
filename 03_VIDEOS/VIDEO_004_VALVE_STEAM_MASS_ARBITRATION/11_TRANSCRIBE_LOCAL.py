"""Local-only ASR evidence; never substitute the locked script for recognized speech.
Requires Python3.12, faster-whisper1.2.1 and av16.1.0 (av19 removed metadata_errors).
"""
import argparse
import json
from pathlib import Path
from faster_whisper import WhisperModel

p = argparse.ArgumentParser()
p.add_argument("audio", type=Path)
p.add_argument("output", type=Path)
p.add_argument("--cache", type=Path, required=True)
a = p.parse_args()
model = WhisperModel("small.en", device="cpu", compute_type="int8",
                     cpu_threads=6, download_root=str(a.cache))
segments, info = model.transcribe(str(a.audio), language="en", beam_size=5,
                                  word_timestamps=True, vad_filter=False,
                                  condition_on_previous_text=False)
out = {"engine": "faster-whisper 1.2.1", "model": "small.en",
       "language": info.language, "duration": info.duration,
       "audio_source": a.audio.name, "segments": [], "words": []}
for s in segments:
    out["segments"].append({"id": s.id, "start": s.start, "end": s.end,
                            "text": s.text, "avg_logprob": s.avg_logprob,
                            "no_speech_prob": s.no_speech_prob})
    for w in s.words or []:
        out["words"].append({"id": "w" + str(len(out["words"])),
                             "text": w.word.strip(), "start": w.start,
                             "end": w.end, "probability": w.probability})
    print(f"{s.start:.2f}-{s.end:.2f}: {s.text}", flush=True)
a.output.parent.mkdir(parents=True, exist_ok=True)
a.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"SAVED {len(out['words'])} ASR words to {a.output}", flush=True)
