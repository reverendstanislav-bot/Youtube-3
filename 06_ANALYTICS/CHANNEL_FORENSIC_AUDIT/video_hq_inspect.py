import pathlib,json,subprocess,hashlib
p=pathlib.Path(r'C:\Users\KK\Downloads\UMG_DISTROKID_FINAL_ENDSCREEN_YOUTUBE_FINAL_HQ.mp4');out=pathlib.Path(r'C:\Users\KK\channel-audit-20261010\06_ANALYTICS\CHANNEL_FORENSIC_AUDIT')
j=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(p)]));j['sha256']=hashlib.file_digest(p.open('rb'),'sha256').hexdigest();(out/'video_003_actual_hq_probe.json').write_text(json.dumps(j,indent=2),encoding='utf8');print(j['sha256'],j['format'])
for n,t in enumerate([0,5,15,30,60,300,600,750,983,1003]):
 subprocess.run(['ffmpeg','-v','error','-ss',str(t),'-i',str(p),'-frames:v','1','-vf','scale=480:-2','-y',str(out/f'video_003_hq_frame_{n:02d}_{t}.png')],check=True)
from PIL import Image,ImageDraw
fs=sorted(out.glob('video_003_hq_frame_*.png'));s=Image.new('RGB',(1440,((len(fs)+2)//3)*300),'#111');d=ImageDraw.Draw(s)
for n,f in enumerate(fs):s.paste(Image.open(f),(n%3*480,n//3*300));d.text((n%3*480+5,n//3*300+273),f.stem,fill='white')
s.save(out/'video_003_hq_contact.png')
r=subprocess.run(['ffmpeg','-hide_banner','-i',str(p),'-vf','blackdetect=d=0.3:pix_th=0.1','-af','loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json','-f','null','-'],stdout=subprocess.DEVNULL,stderr=(out/'video_003_actual_hq_decode.log').open('w',encoding='utf8'));print('decode_exit',r.returncode)
