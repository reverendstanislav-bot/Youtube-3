import pathlib,json,subprocess,hashlib,re
root=pathlib.Path(r'C:\Users\KK\channel-audit-20261010'); out=root/'06_ANALYTICS/CHANNEL_FORENSIC_AUDIT'; out.mkdir(parents=True,exist_ok=True)
files=[r'C:\YOUTUBE\Youtube 3\Video 1\VIDEO_001_UPLOAD_MASTER_1080P.mp4',r'C:\YOUTUBE\Youtube 3\Video 2\ADOBE FIGMA - FINAL WITH END SCREEN.mp4',r'C:\YOUTUBE\Youtube 3\Video 3\UMG DISTROKID - FINAL WITH END SCREEN.mp4']
res=[]
for i,f in enumerate(files,1):
 p=pathlib.Path(f); probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',f])); h=hashlib.file_digest(p.open('rb'),'sha256').hexdigest(); dur=float(probe['format']['duration']); row={'episode':i,'file':f,'sha256':h,'probe':probe};res.append(row)
 times=[0,2,5,10,15,20,30,45,60,90,180,300,450,600,750,dur-25,dur-5]
 for n,t in enumerate(times):
  subprocess.run(['ffmpeg','-v','error','-ss',str(t),'-i',f,'-frames:v','1','-vf','scale=480:-2,format=yuvj420p','-y',str(out/f'video_{i:03d}_frame_{n:02d}_{t:.1f}.jpg')],check=True)
 subprocess.run(['ffmpeg','-hide_banner','-i',f,'-vf','blackdetect=d=0.3:pix_th=0.1','-af','loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json','-f','null','-'],stdout=subprocess.DEVNULL,stderr=(out/f'video_{i:03d}_decode_loudness_black.log').open('w',encoding='utf8'))
(out/'video_media_probe.json').write_text(json.dumps(res,indent=2),encoding='utf8')
print(json.dumps([{'episode':r['episode'],'sha256':r['sha256'],'duration':r['probe']['format']['duration'],'bit_rate':r['probe']['format']['bit_rate'],'streams':[{k:s.get(k) for k in ['codec_type','codec_name','width','height','r_frame_rate','sample_rate','channels','bit_rate']} for s in r['probe']['streams']]} for r in res],indent=2))
