import csv,json,subprocess,hashlib,wave
import numpy as np
from pathlib import Path
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parent.parent
D=ROOT/'DELIVERY'; Q=D/'QC_V6';Q.mkdir(exist_ok=True)
MOV=D/'WHAT_IT_COST_VIDEO008_V6_SMALL_ENDSCREEN_1080P25.mov'
MP4=MOV.with_suffix('.mp4')
master=Path(r'C:\Users\KK\Youtube-3-video005-voice\03_VIDEOS\VIDEO_008_CLAUDE_80_7_BILLION_LOSS_IPO_FILING\10_AUDIO_MASTER\VIDEO008_HARRISON_V5_MASTER_24K_MONO_S16.wav')
def run(args):
    r=subprocess.run(args,capture_output=True,text=True)
    if r.returncode:raise RuntimeError(r.stderr[-3000:])
    return r
if not MP4.exists() or MP4.stat().st_mtime<MOV.stat().st_mtime:
    run(['ffmpeg','-v','error','-xerror','-y','-i',str(MOV),'-i',str(master),'-map','0:v:0','-map','1:a:0','-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-ac','1','-t','987.8','-movflags','+faststart',str(MP4)])
probe=json.loads(run(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(MP4)]).stdout)
v=next(s for s in probe['streams'] if s['codec_type']=='video');a=next(s for s in probe['streams'] if s['codec_type']=='audio')
assert (v['width'],v['height'],v['r_frame_rate'],int(v['nb_frames']))==(1920,1080,'25/1',24695),v
assert abs(float(probe['format']['duration'])-987.8)<.10,probe['format']
assert int(a['sample_rate'])==48000,a
with wave.open(str(master),'rb') as f:
    assert f.getframerate()==24000 and f.getnchannels()==1
    ref=np.frombuffer(f.readframes(f.getnframes()),dtype='<i2').astype(np.float32)/32768
decoded=subprocess.run(['ffmpeg','-v','error','-i',str(MP4),'-vn','-ac','1','-ar','24000','-f','f32le','pipe:1'],check=True,capture_output=True).stdout
got=np.frombuffer(decoded,dtype='<f4');n=min(len(ref),len(got))
corr=float(np.corrcoef(ref[:n:4],got[:n:4])[0,1]);gain=float(np.std(got[:n:4])/np.std(ref[:n:4]))
assert corr>.99 and .98<gain<1.02,(corr,gain)
audio_check={'locked_master':str(master),'comparison':'AAC delivery decoded to 24k mono compared against locked native master','correlation':corr,'rms_gain_ratio':gain,'master_samples':len(ref),'delivery_decoded_samples':len(got),'result':'PASS_NO_MISSING_REORDERED_OR_GAIN_CHANGED_NARRATION_DETECTED'}
repo=Path(r'C:\Users\KK\Youtube-3-video008-delivery\03_VIDEOS\VIDEO_008_CLAUDE_80_7_BILLION_LOSS_IPO_FILING')
rows=list(csv.DictReader((repo/'11_SCENE_TIMELINE.csv').open(encoding='utf-8-sig')))
frames=[(int(r['start_frame_25fps'])+int(r['end_frame_25fps_exclusive'])-1)//2 for r in rows]
terms=['eq(n\\,%d)'%n for n in frames]
while len(terms)>1:
    terms=['('+terms[i]+'+'+terms[i+1]+')' if i+1<len(terms) else terms[i] for i in range(0,len(terms),2)]
sel=terms[0]
# Full sequential decode with xerror; frame extraction doubles as scene coverage evidence.
run(['ffmpeg','-v','error','-xerror','-y','-threads','2','-filter_threads','1','-i',str(MP4),'-vf','select='+sel,'-fps_mode','vfr','-an','-threads','2','-q:v','3',str(Q/'SCENE_%03d.jpg')])
samples=sorted(Q.glob('SCENE_*.jpg'));assert len(samples)==110,len(samples)
for k in range(0,len(samples),16):
    im=Image.new('RGB',(1920,4*294),(22,22,22));draw=ImageDraw.Draw(im)
    for j,p in enumerate(samples[k:k+16]):
        x=(j%4)*480;y=(j//4)*294
        im.paste(Image.open(p).resize((480,270)),(x,y));draw.text((x+8,y+274),rows[k+j]['scene_id'],fill='white')
    im.save(Q/f'CONTACT_{k//16+1:02d}.jpg',quality=90)
files=[]
for p in [MP4,MOV,D/'VIDEO008_V6_SMALL_ENDSCREEN.drp']:
    h=hashlib.sha256()
    with p.open('rb') as f:
        while b:=f.read(8*1024*1024):h.update(b)
    files.append({'file':p.name,'bytes':p.stat().st_size,'sha256':h.hexdigest()})
out={'technical_qc':'PASS','container_operation':'Native DaVinci Resolve picture stream copied without video re-encoding; approved WAV directly encoded as AAC and muxed at time zero. No ffmpeg visual assembly. Native Resolve audio failed waveform check near 180-240s; native MOV is picture intermediate, not accepted sound master.','duration_sec':float(probe['format']['duration']),'frames':int(v['nb_frames']),'fps':v['r_frame_rate'],'resolution':[v['width'],v['height']],'video_codec':v['codec_name'],'audio_codec':a['codec_name'],'audio_sample_rate':a['sample_rate'],'audio_channels':a['channels'],'full_decode':'PASS_FFMPEG_XERROR','scene_samples':len(samples),'visual_sample_review':'PENDING','continuous_real_time_av_review':'NOT_CLAIMED','owner_visual_acceptance':'PENDING','files':files,'probe':probe}
out['audio_master_comparison']=audio_check
(D/'DELIVERY_QC_V6.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='probe'},indent=2))
