"""Independent-model local recheck of eight low-confidence ASR regions."""
import argparse
import json
import subprocess
from pathlib import Path
from faster_whisper import WhisperModel

p=argparse.ArgumentParser()
p.add_argument("audio",type=Path)
p.add_argument("scratch",type=Path)
p.add_argument("--cache",type=Path,required=True)
a=p.parse_args()
a.scratch.mkdir(parents=True,exist_ok=True)
model=WhisperModel("medium.en",device="cpu",compute_type="int8",cpu_threads=6,download_root=str(a.cache))
regions=[(0,7),(138,149),(193,203),(221,230),(247,257),(423,433),(484,495),(730,741)]
out={"model":"medium.en","engine":"faster-whisper 1.2.1","status":"ASR_RECHECK_NOT_AUDITORY_REVIEW","regions":[]}
for i,(start,end) in enumerate(regions):
    clip=a.scratch/f"review_{i+1:02}.wav"
    subprocess.run(["ffmpeg","-v","error","-n","-ss",str(start),"-i",str(a.audio),"-t",str(end-start),"-ar","16000","-ac","1",str(clip)],check=True)
    segs,info=model.transcribe(str(clip),language="en",word_timestamps=True,beam_size=5,condition_on_previous_text=False)
    text=[]; words=[]
    for s in segs:
        text.append(s.text.strip())
        words.extend({"text":w.word.strip(),"start":round(w.start+start,3),"end":round(w.end+start,3),"probability":w.probability} for w in s.words or [])
    item={"region":i+1,"start_sec":start,"end_sec":end,"text":" ".join(text),"words":words}
    out["regions"].append(item)
    print(json.dumps(item,ensure_ascii=True),flush=True)
Path(__file__).with_name("11_ASR_MEDIUM_RECHECK.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
