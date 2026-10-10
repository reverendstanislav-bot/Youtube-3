import pathlib,json,subprocess,hashlib
from PIL import Image,ImageDraw
out=pathlib.Path(r"C:\Users\KK\channel-audit-20261010\06_ANALYTICS\CHANNEL_FORENSIC_AUDIT");rows=[]
for ep in [1,2,3]:
 fs=sorted(pathlib.Path(fr"C:\YOUTUBE\Youtube 3\Video {ep}\SHORTS").glob("*.mp4"));sheet=Image.new("RGB",(720,len(fs)*390),"#111");d=ImageDraw.Draw(sheet)
 for n,f in enumerate(fs):
  j=json.loads(subprocess.check_output(["ffprobe","-v","error","-show_streams","-show_format","-of","json",str(f)]));dur=float(j["format"]["duration"]);rows.append({"episode":ep,"filename":f.name,"duration":dur,"sha256":hashlib.file_digest(f.open("rb"),"sha256").hexdigest(),"streams":[{k:s.get(k) for k in ["codec_type","width","height","codec_name","r_frame_rate"]} for s in j["streams"]]})
  for c,t in enumerate([0,3,max(0,dur-1.5)]):
   fp=out/f"video_short_{ep}_{n+1:02d}_{c}.png";subprocess.run(["ffmpeg","-v","error","-ss",str(t),"-i",str(f),"-frames:v","1","-vf","scale=240:-2","-y",str(fp)],check=True);im=Image.open(fp);sheet.paste(im,(c*240,n*390));d.text((c*240+3,n*390+360),f"S{n+1:02d} {t:.1f}s",fill="white")
 sheet.save(out/f"video_shorts_{ep:03d}_contact.png")
(out/"video_shorts_probe.json").write_text(json.dumps(rows,indent=2),encoding="utf8");print(len(rows),"Shorts sampled")
