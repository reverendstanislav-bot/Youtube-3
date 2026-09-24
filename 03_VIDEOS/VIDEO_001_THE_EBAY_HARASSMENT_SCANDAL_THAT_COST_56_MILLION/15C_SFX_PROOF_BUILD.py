#!/usr/bin/env python3
from __future__ import annotations
import csv, math, random, struct, subprocess, wave, hashlib
from pathlib import Path

BASE=Path(__file__).resolve().parent
SRC=BASE/"15B_OUTPUT"/"VIDEO_001_STAGE15B_REVIEW_V1_1080P.mp4"
ROOT=BASE/"15C_SFX_PROOF"
SFX=ROOT/"sfx"
OUT=ROOT/"out"
SFX.mkdir(parents=True,exist_ok=True)
OUT.mkdir(parents=True,exist_ok=True)
SR=44100
random.seed(15002)

def wav_write(path, samples, channels=1):
    with wave.open(str(path),"wb") as w:
        w.setnchannels(channels)
        w.setsampwidth(2)
        w.setframerate(SR)
        if channels==1:
            w.writeframes(b"".join(struct.pack("<h", max(-32768,min(32767,int(x)))) for x in samples))
        else:
            w.writeframes(b"".join(struct.pack("<hh", max(-32768,min(32767,int(l))), max(-32768,min(32767,int(r)))) for l,r in samples))

def envelope(i,n,attack=.02,release=.25):
    t=i/SR
    d=n/SR
    a=min(1.0,t/max(attack,1e-6))
    r=min(1.0,max(0.0,(d-t)/max(release,1e-6)))
    return min(a,r)

def noise_lp(n, amp=1200, smooth=.88):
    out=[]; y=0.0
    for i in range(n):
        x=(random.random()*2-1)*amp
        y=smooth*y+(1-smooth)*x
        out.append(y)
    return out

# paper tick
n=int(.18*SR); base=noise_lp(n,7800,.72)
paper=[base[i]*((1-i/n)**2.2) for i in range(n)]
wav_write(SFX/"02_paper_tick.wav",paper)

# page rustle
n=int(.52*SR); base=noise_lp(n,7200,.80)
page=[]
for i,x in enumerate(base):
    env=envelope(i,n,.06,.14)
    mod=.6+.4*math.sin(2*math.pi*3.2*i/SR)
    page.append(x*env*mod)
wav_write(SFX/"03_page_rustle.wav",page)

# keyboard cluster: 5 quiet clicks
n=int(.48*SR); key=[0.0]*n
for t in [0.00,.075,.16,.27,.38]:
    s=int(t*SR)
    for j in range(int(.018*SR)):
        if s+j>=n: break
        env=math.exp(-j/(SR*.004))
        key[s+j]+=6200*env*math.sin(2*math.pi*1350*j/SR)+(random.random()*2-1)*1600*env
wav_write(SFX/"04_keyboard_cluster.wav",key)

# dry click
n=int(.07*SR)
click=[]
for i in range(n):
    env=math.exp(-i/(SR*.010))
    click.append(10500*env*math.sin(2*math.pi*980*i/SR))
wav_write(SFX/"05_dry_click.wav",click)

# low transition
n=int(.45*SR)
low=[]
for i in range(n):
    env=math.exp(-i/(SR*.13))
    low.append(10800*env*(math.sin(2*math.pi*72*i/SR)+.35*math.sin(2*math.pi*144*i/SR)))
wav_write(SFX/"06_low_transition.wav",low)

# abstract digital-delete texture
n=int(.30*SR); digital=[]
for i in range(n):
    t=i/SR
    env=math.exp(-t/.10)
    freq=1500-800*(i/n)
    gate=1.0 if (i//80)%3 else .25
    digital.append(7600*env*gate*math.sin(2*math.pi*freq*t))
wav_write(SFX/"07_digital_delete.wav",digital)

# soft whoosh
n=int(.55*SR); raw=noise_lp(n,7200,.70)
who=[]
for i,x in enumerate(raw):
    env=max(0.0,math.sin(math.pi*i/max(n-1,1)))**1.7
    who.append(x*env)
wav_write(SFX/"08_soft_whoosh.wav",who)

README=SFX/"README.txt"
README.write_text("""VIDEO_001 — EDITOR-NATIVE SFX PACK

All files in this folder were procedurally synthesized for WHAT IT COST / VIDEO_001.
No third-party recording, stock library, copyrighted sample, model generation, or paid asset is used.
Project use: unrestricted.

02_paper_tick.wav — tiny paper/object touch
03_page_rustle.wav — restrained document movement
04_keyboard_cluster.wav — abstract quiet keyboard cluster
05_dry_click.wav — dry editorial click
06_low_transition.wav — restrained low transition pulse
07_digital_delete.wav — abstract digital deletion texture
08_soft_whoosh.wav — very soft transition air movement

HARD RULES:
- Never imply a factual event that is not established.
- No sirens, gavel, pig/insect foley, cash register, coins, alarms, gunshots, horror stings, or trailer impacts.
- No SFX after B111 in the final film.
""",encoding="utf-8")

# Beat starts
beats={}
with (BASE/"11_VISUAL_TIMELINE.csv").open(encoding="utf-8-sig",newline="") as f:
    for r in csv.DictReader(f):
        beats[r["beat_id"]]=float(r["start"])

# Proof windows from real film.
windows=[
    ("opening",0.0,34.0),
    ("messages",164.0,36.0),
    ("operation",284.0,38.0),
    ("money",758.0,42.0),
    ("ending",858.0,40.0),
]

# beat -> sfx file + gain dB
events={
"B002":("02_paper_tick.wav",-18),
"B003":("03_page_rustle.wav",-22),
"B008":("05_dry_click.wav",-23),
"B018":("04_keyboard_cluster.wav",-21),
"B019":("05_dry_click.wav",-24),
"B020":("05_dry_click.wav",-24),
"B023":("07_digital_delete.wav",-24),
"B025":("03_page_rustle.wav",-23),
"B034":("03_page_rustle.wav",-22),
"B037":("08_soft_whoosh.wav",-26),
"B042":("06_low_transition.wav",-23),
"B044":("07_digital_delete.wav",-22),
"B083":("06_low_transition.wav",-25),
"B088":("05_dry_click.wav",-24),
"B091":("05_dry_click.wav",-25),
"B093":("05_dry_click.wav",-25),
"B097":("05_dry_click.wav",-24),
"B104":("03_page_rustle.wav",-25),
"B108":("05_dry_click.wav",-26),
"B111":("03_page_rustle.wav",-26),
}

def sh(cmd):
    print("RUN"," ".join(map(str,cmd)))
    subprocess.run(cmd,check=True)

clips=[]
for idx,(name,start,dur) in enumerate(windows,1):
    clip=OUT/f"{idx:02d}_{name}.mp4"
    # Build SFX filter inputs relative to this excerpt.
    inputs=["-i",str(SRC)]
    af=[]
    labels=[]
    # V2: no room tone. Only clearly audible, sparse editorial events.
    in_idx=1
    for bid,(fn,gain) in events.items():
        t=beats.get(bid)
        if t is None or not (start <= t < start+dur):
            continue
        rel=t-start
        inputs += ["-i",str(SFX/fn)]
        ms=int(round(rel*1000))
        lab=f"e{in_idx}"
        af.append(f"[{in_idx}:a]volume={gain}dB,adelay={ms}|{ms}[{lab}]")
        labels.append(f"[{lab}]")
        in_idx+=1
    if labels:
        af.append("".join(labels)+f"amix=inputs={len(labels)}:duration=longest:normalize=0[sfx]")
    else:
        af.append(f"anullsrc=r={SR}:cl=mono,atrim=0:{dur:.3f}[sfx]")
    af.append("[0:a]volume=1.0[vo]")
    af.append("[vo][sfx]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[a]")
    label=f"SFX PROOF • {idx}/5"
    vf=f"drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf:text='{label}':x=55:y=45:fontsize=30:fontcolor=white@0.82:box=1:boxcolor=black@0.38:boxborderw=12"
    cmd=["ffmpeg","-y","-loglevel","error","-ss",str(start),"-t",str(dur),*inputs,
         "-filter_complex",";".join(af),"-map","0:v:0","-map","[a]","-vf",vf,
         "-c:v","libx264","-preset","veryfast","-crf","26","-pix_fmt","yuv420p",
         "-c:a","aac","-b:a","160k","-ar","44100","-ac","2","-t",str(dur),str(clip)]
    sh(cmd)
    clips.append(clip)

lst=OUT/"concat.txt"
lst.write_text("\n".join("file '"+str(x.resolve()).replace("'","'\\''")+"'" for x in clips)+"\n")
final=OUT/"VIDEO_001_SFX_ONLY_PROOF_V2_AUDIBLE.mp4"
sh(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",str(lst),
    "-c","copy","-movflags","+faststart",str(final)])

# Package SFX
import zipfile
z=SFX/"VIDEO_001_EDITOR_NATIVE_SFX_PACK.zip"
with zipfile.ZipFile(z,"w",zipfile.ZIP_DEFLATED) as zz:
    for p in sorted(SFX.glob("*.wav")):
        zz.write(p,p.name)
    zz.write(README,README.name)

def sha(p):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for c in iter(lambda:f.read(1024*1024),b""): h.update(c)
    return h.hexdigest()

report=OUT/"VIDEO_001_SFX_PROOF_REPORT.txt"
report.write_text(f"""VIDEO_001 — SFX-ONLY PROOF V2 / AUDIBLE

Purpose:
Test the film without music. Harrison + original picture/captions + restrained editor-native SFX only.

Proof windows:
1 opening 00:00–00:34
2 messages 02:44–03:20
3 operation 04:44–05:22
4 money 12:38–13:20
5 ending 14:18–14:58

Music: NONE
SFX source: 100% editor-native procedural synthesis
Third-party SFX: NONE
Model generation: NONE
Paid credits: 0

Proof SHA-256: {sha(final)}
SFX pack SHA-256: {sha(z)}

Proof-local audible SFX checkpoints:
- 00:06.340 paper tick
- 00:07.760 page rustle
- 00:16.260 keyboard cluster
- 00:16.950 dry click
- 00:25.800 digital-delete texture
- 00:30.950 page rustle
- 01:10.180 page rustle
- 01:35.400 soft whoosh
- 01:52.080 dry click
- 02:08.640 dry click
- 02:18.540 dry click
- 02:34.240 page rustle
- 03:09.900 dry click

Editorial intent:
- narration and silence carry tension;
- room tone removed completely;
- working SFX raised roughly +10 dB from V1 event-gain settings;
- source SFX amplitudes rebuilt so accents are actually audible under narration;
- SFX still remain sparse and non-TikTok/non-trailer;
- no cliché / horror / event-implying design;
- no music decision is made by this proof.
""",encoding="utf-8")
print(report.read_text())
