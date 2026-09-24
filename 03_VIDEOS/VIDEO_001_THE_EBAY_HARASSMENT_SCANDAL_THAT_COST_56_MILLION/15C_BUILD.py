#!/usr/bin/env python3
from __future__ import annotations
import csv, hashlib, json, math, random, struct, subprocess, urllib.request, wave
from array import array
from pathlib import Path

BASE=Path(__file__).resolve().parent
IN15B=BASE/"15B_OUTPUT"/"VIDEO_001_STAGE15B_REVIEW_V1_1080P.mp4"
OUT=BASE/"15C_OUTPUT"
OUT.mkdir(exist_ok=True)

RUNTIME=957.414
SR=44100

TRACKS={
"A":("Resonance","Scott Buckley","https://d2ol7oe51mr4n9.cloudfront.net/user_3J3zfwu7kpgllQvPySWoLtXHwdR/fceba555-a9bd-488b-82fc-6fa81e022073.mp3"),
"B":("Intervention","Scott Buckley","https://d2ol7oe51mr4n9.cloudfront.net/user_3J3zfwu7kpgllQvPySWoLtXHwdR/c03fb370-6d8b-41c4-80af-53d8efe9be0c.mp3"),
"C":("Chronicle","Scott Buckley","https://d2ol7oe51mr4n9.cloudfront.net/user_3J3zfwu7kpgllQvPySWoLtXHwdR/d01ee201-5c0b-4ad2-81c6-e6bad207b766.mp3"),
"D":("Life Is","Scott Buckley","https://d2ol7oe51mr4n9.cloudfront.net/user_3J3zfwu7kpgllQvPySWoLtXHwdR/9c6fe426-6ed1-40bc-9402-001a772bf453.mp3"),
}

# cue_id, start, end, family, source offset, gain dB
CUES=[
("M14-01",0.000,73.980,"A",6.0,-10.0),
("M14-02",74.680,130.260,"B",10.0,-12.0),
("M14-03",131.060,218.300,"A",78.0,-10.0),
("M14-04",219.200,283.080,"A",168.0,-10.5),
("M14-05",284.180,355.800,"A",14.0,-9.0),
("M14-06",356.860,415.800,"A",98.0,-11.0),
("M14-07",416.540,476.000,"B",82.0,-12.5),
("M14-08",477.340,569.300,"B",145.0,-14.0),
("M14-09",570.640,709.000,"B",16.0,-16.0),
("M14-10",710.380,757.000,"C",24.0,-12.0),
("M14-11",757.980,843.700,"C",93.0,-11.0),
("M14-12",844.600,957.414,"D",34.0,-12.0),
]

def dl(url: str, p: Path):
    if p.exists() and p.stat().st_size>0: return
    urllib.request.urlretrieve(url,p)

def sh(cmd):
    print("RUN", " ".join(map(str,cmd)))
    subprocess.run(cmd,check=True)

def probe(path: Path):
    return json.loads(subprocess.check_output([
        "ffprobe","-v","error","-show_entries","format=duration,size",
        "-show_entries","stream=index,codec_type,codec_name,width,height,r_frame_rate,avg_frame_rate,sample_rate,channels",
        "-of","json",str(path)
    ],text=True))

def sha(path: Path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for c in iter(lambda:f.read(1024*1024),b""): h.update(c)
    return h.hexdigest()

if not IN15B.exists():
    raise SystemExit("Stage 15B review master missing; run 15B_BUILD.py first.")

# Download approved music only.
for fam,(title,artist,url) in TRACKS.items():
    dl(url,OUT/f"{fam}_{title.replace(' ','_')}.mp3")

# Beat times for restrained SFX and automation.
beats={}
with (BASE/"11_VISUAL_TIMELINE.csv").open(encoding="utf-8-sig",newline="") as f:
    for r in csv.DictReader(f):
        beats[r["beat_id"]]=(float(r["start"]),float(r["end"]))

# Build 12 normalized cue segments.
cue_files=[]
for cue,start,end,fam,offset,gain in CUES:
    title=TRACKS[fam][0]
    src=OUT/f"{fam}_{title.replace(' ','_')}.mp3"
    dur=end-start
    fout=OUT/f"{cue}_{fam}.wav"
    fade_out=max(0.0,dur-1.4)
    af=f"loudnorm=I=-18:LRA=10:TP=-1.5,volume={gain}dB,afade=t=in:st=0:d=0.65,afade=t=out:st={fade_out:.3f}:d=1.4"
    sh(["ffmpeg","-y","-loglevel","error","-ss",f"{offset:.3f}","-i",str(src),"-t",f"{dur:.3f}",
        "-af",af,"-ar",str(SR),"-ac","2",str(fout)])
    cue_files.append((cue,start,end,fout))

# Mix cues into full music stem with exact cue starts.
inputs=[]
filters=[]
labels=[]
for i,(cue,start,end,p) in enumerate(cue_files):
    inputs+=["-i",str(p)]
    ms=int(round(start*1000))
    labels.append(f"m{i}")
    filters.append(f"[{i}:a]adelay={ms}|{ms}[m{i}]")
mixins="".join(f"[{x}]" for x in labels)
filters.append(f"{mixins}amix=inputs={len(labels)}:duration=longest:normalize=0[music0]")

# Manual reductions called out by the locked cue sheet.
duck_windows=[]
for beat_id,factor in [
    ("B008",0.62),("B018",0.68),("B019",0.68),("B020",0.68),("B023",0.68),("B025",0.68),
    ("B040",0.65),("B059",0.55),("B060",0.55),
    ("B069",0.55),("B070",0.55),("B071",0.55),("B072",0.55),("B073",0.55),("B074",0.55),
    ("B075",0.55),("B076",0.55),("B077",0.55),("B078",0.55),
    ("B083",0.36),("B097",0.58),("B098",0.58),("B099",0.16),("B100",0.58),("B101",0.58),
    ("B104",0.38),("B115",0.55)
]:
    if beat_id in beats:
        a,b=beats[beat_id]; duck_windows.append((a,b,factor))
current="music0"
for n,(a,b,factor) in enumerate(duck_windows):
    nxt=f"mv{n}"
    filters.append(f"[{current}]volume=volume={factor}:enable='between(t,{a:.3f},{b:.3f})'[{nxt}]")
    current=nxt
# final 3 sec almost tail/room
filters.append(f"[{current}]afade=t=out:st=954.2:d=3.0,atrim=0:{RUNTIME:.3f}[music]")
music=OUT/"VIDEO_001_STAGE15C_MUSIC_BED.flac"
sh(["ffmpeg","-y","-loglevel","error",*inputs,"-filter_complex",";".join(filters),"-map","[music]",
    "-ar",str(SR),"-c:a","flac",str(music)])

# Restrained editor-native SFX. No factual event is implied.
events=[
("paper","B003",-31),("paper","B018",-30),("paper","B023",-31),("paper","B028",-32),
("paper","B034",-31),("paper","B055",-31),("paper","B068",-32),
("low","B032",-29),("low","B049",-30),("low","B083",-30),
("click","B042",-31),("click","B057",-32),("click","B062",-32),
("digital","B044",-32),
("tone","B088",-31),("tone","B091",-32),("tone","B093",-32),("tone","B097",-32),
("tone","B108",-33),("tone","B111",-33),
]
N=int(math.ceil(RUNTIME*SR))
buf=array('h',[0])*N
random.seed(15001)

def add_sample(t,kind,db):
    start=int(t*SR)
    amp=32767*(10**(db/20))
    if kind=="paper":
        dur=.075
        for i in range(int(dur*SR)):
            env=(1-i/(dur*SR))**3
            x=(random.random()*2-1)*env
            idx=start+i
            if idx<N: buf[idx]=max(-32768,min(32767,buf[idx]+int(x*amp)))
    elif kind=="click":
        dur=.045
        for i in range(int(dur*SR)):
            env=math.exp(-i/(SR*.009))
            x=math.sin(2*math.pi*1100*i/SR)*env
            idx=start+i
            if idx<N: buf[idx]=max(-32768,min(32767,buf[idx]+int(x*amp)))
    elif kind=="low":
        dur=.28
        for i in range(int(dur*SR)):
            env=math.exp(-i/(SR*.10))
            x=math.sin(2*math.pi*82*i/SR)*env
            idx=start+i
            if idx<N: buf[idx]=max(-32768,min(32767,buf[idx]+int(x*amp)))
    elif kind=="tone":
        dur=.11
        for i in range(int(dur*SR)):
            env=math.exp(-i/(SR*.03))
            x=math.sin(2*math.pi*760*i/SR)*env
            idx=start+i
            if idx<N: buf[idx]=max(-32768,min(32767,buf[idx]+int(x*amp)))
    elif kind=="digital":
        dur=.16
        for i in range(int(dur*SR)):
            env=(1-i/(dur*SR))**2
            freq=1350-650*(i/(dur*SR))
            x=math.sin(2*math.pi*freq*i/SR)*env*(1 if (i//70)%2==0 else .45)
            idx=start+i
            if idx<N: buf[idx]=max(-32768,min(32767,buf[idx]+int(x*amp)))

for kind,bid,db in events:
    if bid in beats:
        add_sample(beats[bid][0],kind,db)

sfxwav=OUT/"sfx_tmp.wav"
with wave.open(str(sfxwav),"wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(buf.tobytes())
sfx=OUT/"VIDEO_001_STAGE15C_SFX_STEM.flac"
sh(["ffmpeg","-y","-loglevel","error","-i",str(sfxwav),"-c:a","flac",str(sfx)])
sfxwav.unlink()

# Original Harrison master is the sidechain key and primary mix source.
voice=OUT/"harrison_master.mp3"
dl("https://d2ol7oe51mr4n9.cloudfront.net/user_3J3zfwu7kpgllQvPySWoLtXHwdR/4c1aa66b-440d-4fc7-ae95-78e60845ae5f.mp3",voice)

mixed=OUT/"VIDEO_001_STAGE15C_AUDIO_MIX.wav"
fc=(
    "[1:a]aformat=sample_rates=44100:channel_layouts=stereo[m];"
    "[0:a]aformat=sample_rates=44100:channel_layouts=mono,asplit=2[vo][key];"
    "[m][key]sidechaincompress=threshold=0.035:ratio=2.2:attack=18:release=280:makeup=1[md];"
    "[2:a]aformat=sample_rates=44100:channel_layouts=mono,volume=1.0[sfx];"
    "[vo][md][sfx]amix=inputs=3:duration=first:normalize=0,"
    "loudnorm=I=-14:LRA=9:TP=-1.0[aout]"
)
sh(["ffmpeg","-y","-loglevel","error","-i",str(voice),"-i",str(music),"-i",str(sfx),
    "-filter_complex",fc,"-map","[aout]","-t",f"{RUNTIME:.3f}","-ar",str(SR),"-c:a","pcm_s24le",str(mixed)])

# Final 15C review: copy Stage15B video bitstream; replace audio only.
review=OUT/"VIDEO_001_STAGE15C_REVIEW_V1_1080P.mp4"
sh(["ffmpeg","-y","-loglevel","error","-i",str(IN15B),"-i",str(mixed),
    "-map","0:v:0","-map","1:a:0","-c:v","copy","-c:a","aac","-b:a","256k","-ar",str(SR),"-ac","2",
    "-t",f"{RUNTIME:.3f}","-movflags","+faststart",str(review)])

# Lightweight review file for easy download.
lite=OUT/"VIDEO_001_STAGE15C_REVIEW_LITE_1080P.mp4"
sh(["ffmpeg","-y","-loglevel","error","-i",str(review),"-c:v","libx264","-preset","veryfast","-crf","29",
    "-pix_fmt","yuv420p","-c:a","aac","-b:a","128k","-ar",str(SR),"-ac","2","-movflags","+faststart",str(lite)])

p=probe(review)
v=next(x for x in p["streams"] if x["codec_type"]=="video")
a=next(x for x in p["streams"] if x["codec_type"]=="audio")
dur=float(p["format"]["duration"])
assert v["width"]==1920 and v["height"]==1080
assert v["r_frame_rate"]=="25/1" and v["avg_frame_rate"]=="25/1"
assert a["sample_rate"]=="44100"
assert abs(dur-RUNTIME)<0.08

credits=OUT/"VIDEO_001_STAGE15C_MUSIC_CREDITS.txt"
credits.write_text("""VIDEO_001 — MUSIC CREDITS

'Resonance' by Scott Buckley - released under CC-BY 4.0. www.scottbuckley.com.au
'Intervention' by Scott Buckley - released under CC-BY 4.0. www.scottbuckley.com.au
'Chronicle' by Scott Buckley - released under CC-BY 4.0. www.scottbuckley.com.au
'Life Is' by Scott Buckley - released under CC-BY 4.0. www.scottbuckley.com.au

SFX: editor-native synthesized micro-accents only; no external SFX library and no model generation.
""",encoding="utf-8")

report=OUT/"VIDEO_001_STAGE15C_MIX_REPORT.txt"
report.write_text(f"""VIDEO_001 — STAGE 15C AUDIO MIX REPORT
STATUS: TECHNICAL PASS / OWNER LISTEN REVIEW PENDING

VIDEO
- {review.name}
- 1920x1080 / H.264 video copied from approved Stage15B render
- CFR 25 fps
- audio: AAC 44.1 kHz stereo
- runtime: {dur:.3f} sec
- target: {RUNTIME:.3f} sec
- video SHA-256: {sha(review)}
- lite SHA-256: {sha(lite)}

MUSIC
- 12 cue windows from locked Stage14 cue sheet
- A Resonance: M14-01/03/04/05/06
- B Intervention: M14-02/07/08/09
- C Chronicle: M14-10/11
- D Life Is: M14-12
- cue-local gain + manual legal/number dips + VO-keyed sidechain compression
- final 3 sec music fade to near-room/tail
- music bed stem: {music.name} / SHA-256 {sha(music)}

SFX
- {len(events)} restrained editor-native micro-accents
- paper / dry click / low hit / abstract digital / tonal tick only
- no sirens, pig squeals, insect foley, cash-register, coins, gunshots, gavel, jump-scare or horror SFX
- no SFX after B111
- stem: {sfx.name} / SHA-256 {sha(sfx)}

MIX
- Harrison remains primary source
- music sidechain ducked under VO
- additional manual reductions for exact quotes / legal nuance / money arithmetic
- final mix target: -14 LUFS / <= -1.0 dBTP
- master WAV: {mixed.name} / SHA-256 {sha(mixed)}

SPEND
- paid/model generation: 0
- external SFX acquisition: 0

NEXT GATE
- owner listen review
- do not start final master/QC stage automatically
""",encoding="utf-8")

print(report.read_text())
