#!/usr/bin/env python3
import csv, os, subprocess, urllib.request, zipfile
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT=Path("/home/user/stage15a")
ROOT.mkdir(parents=True,exist_ok=True)
FRAMES=ROOT/"frames"; FRAMES.mkdir(exist_ok=True)
SRC=ROOT/"source"; SRC.mkdir(exist_ok=True)
GFX=ROOT/"gfx"; GFX.mkdir(exist_ok=True)
W,H=1920,1080
BG=(11,11,11); RED=(211,34,34); IV=(237,237,237); MUT=(170,166,158)
FONTB="/usr/share/fonts/truetype/higgsfield/Metropolis-ExtraBold.ttf"
FONTR="/usr/share/fonts/truetype/higgsfield/Montserrat-Regular.ttf"
if not Path(FONTB).exists(): FONTB="/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf"
if not Path(FONTR).exists(): FONTR="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
RAW="https://raw.githubusercontent.com/reverendstanislav-bot/Youtube-3/main/03_VIDEOS/VIDEO_001_THE_EBAY_HARASSMENT_SCANDAL_THAT_COST_56_MILLION/12B_SOURCE_ASSETS/"

def get(url,out):
    out=Path(out)
    if not out.exists():
        urllib.request.urlretrieve(url,out)
    return out

def font(path,size): return ImageFont.truetype(path,size)

def fit(im):
    im=im.convert("RGB")
    return ImageOps.fit(im,(W,H),method=Image.Resampling.LANCZOS,centering=(0.5,0.5))

def wrap(draw,text,f,maxw):
    words=text.split(); lines=[]; cur=""
    for w in words:
        t=w if not cur else cur+" "+w
        if draw.textbbox((0,0),t,font=f)[2] <= maxw: cur=t
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return "\n".join(lines)

EDITOR={
"B007":("SEVEN GUILTY PLEAS","ALL SEVEN FEDERALLY PROSECUTED PARTICIPANTS","DC011_SEVEN_GUILTY_DOJ.png"),
"B018":("“WE ARE GOING TO CRUSH THIS LADY.”","SOURCE: U.S. DISTRICT COURT • D. MASS.","DC001_CRUSH_THIS_LADY.png"),
"B048":("FEDERAL CASES BEGIN — 2020","INDIVIDUAL CRIMINAL ACCOUNTABILITY","DC011_SEVEN_GUILTY_DOJ.png"),
"B077":("NOT CRIMINALLY CHARGED","WENIG • JONES • WYMER — OVER THE CAMPAIGN","LIVE_DEVIN_WENIG_COMMONS.jpg"),
"B104":("NO JURY VERDICT ON SURVIVING CLAIMS","SURVIVING CLAIM ≠ LIABILITY","DC010_SUMMARY_JUDGMENT_ORDER.png"),
"B111":("$55.7M SETTLEMENT PACKAGE","CIVIL SETTLEMENT • NOT A JUDGMENT","EBAY_HQ_2018_CC_BY_SA.jpg"),
}

def editor_frame(beat):
    title,sub,srcname=EDITOR[beat]
    src=get(RAW+srcname,SRC/srcname)
    sim=Image.open(src).convert("RGB")
    im=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(im)
    # source panel, upper-left, never into subtitle-safe bottom 22%
    panel=ImageOps.fit(sim,(760,540),method=Image.Resampling.LANCZOS)
    panel=panel.point(lambda p:int(p*0.82))
    im.paste(panel,(90,250))
    d.rectangle((90,250,850,790),outline=(100,92,78),width=3)
    d.rectangle((90,92,355,101),fill=RED)
    d.text((90,115),"WHAT IT COST",font=font(FONTB,25),fill=MUT)
    tf=font(FONTB,68 if len(title)<30 else 56)
    txt=wrap(d,title,tf,850)
    d.multiline_text((930,270),txt,font=tf,fill=IV,spacing=3)
    bb=d.multiline_textbbox((930,270),txt,font=tf,spacing=3)
    d.rectangle((930,bb[3]+24,1190,bb[3]+34),fill=RED)
    sf=font(FONTB,25)
    d.multiline_text((930,bb[3]+68),wrap(d,sub,sf,760),font=sf,fill=MUT,spacing=5)
    d.rectangle((0,842,W,H),fill=BG)
    return im

with open(ROOT/"manifest.csv",newline="",encoding="utf-8") as f:
    rows=list(csv.DictReader(f))
assert len(rows)==115

# unpack final GFX
with zipfile.ZipFile(ROOT/"gfx.zip") as z: z.extractall(GFX)

for r in rows:
    beat=r["beat_id"]; route=r["route"]; out=FRAMES/f"{beat}.jpg"
    if route=="EDITOR_BUILD":
        im=editor_frame(beat)
    elif route=="FINAL_GFX":
        hits=list(GFX.rglob(r["canonical_asset"]))
        if not hits: raise FileNotFoundError(r["canonical_asset"])
        im=fit(Image.open(hits[0]))
    else:
        tmp=SRC/f"{beat}{Path(r['source']).suffix or '.img'}"
        get(r["source"],tmp)
        im=fit(Image.open(tmp))
    im.save(out,"JPEG",quality=93,optimize=True)

# validate images / create concat list
with open(ROOT/"concat.txt","w",encoding="utf-8") as f:
    for r in rows:
        p=FRAMES/f"{r['beat_id']}.jpg"
        Image.open(p).verify()
        f.write("file '"+str(p).replace("'","'\\''")+"'\n")
        f.write("duration "+r["duration_sec"]+"\n")
    p=FRAMES/f"{rows[-1]['beat_id']}.jpg"
    f.write("file '"+str(p).replace("'","'\\''")+"'\n")

cmd=[
"ffmpeg","-y","-loglevel","warning",
"-f","concat","-safe","0","-i",str(ROOT/"concat.txt"),
"-i",str(ROOT/"audio.mp3"),
"-vf","fps=25,format=yuv420p",
"-map","0:v:0","-map","1:a:0",
"-c:v","libx264","-preset","veryfast","-crf","20",
"-c:a","aac","-b:a","192k","-ar","44100","-ac","1",
"-t","957.414","-movflags","+faststart",
str(ROOT/"VIDEO_001_STAGE15A_PICTURE_ASSEMBLY_V1_1080P.mp4")
]
subprocess.run(cmd,check=True)
print("RENDER_OK")
