"""Owner correction: remove obstructive editorial cards from every affected scene.
No image generation. Existing approved illustrative bases remain illustrations.
"""
from pathlib import Path
import json,hashlib

ROOT=Path(__file__).resolve().parent
ns={'__file__':str(ROOT/'build_fusion.py')}
exec((ROOT/'build_fusion.py').read_text(encoding='utf-8').split('records=[]')[0],ns)
for name in ('loader','node','val','expr','link','color','rect','fade','merge','text','comp'):globals()[name]=ns[name]
OUT=ROOT/'COMPS_V5_CLEAN';OUT.mkdir(exist_ok=True)
rows=json.loads((ROOT/'FUSION_BUILD_MANIFEST.json').read_text())
markers={
    # Native image pixels, measured on the accepted bases. No generic full-width marker.
    'SC002':[(490,741,770,20,-.4,45,69),(500,568,750,20,-.4,105,129)],
    'SC005':[(866,766,104,24,-2,50,74)],
    'SC015':[(826,332,115,23,-.5,45,69)],
    'SC071':[(1444,541,133,25,-5,45,69)]
}
manifest=[]
for r in rows:
    sid=r['scene_id'];dur=r['frames'];photo=Path(r['photo'])
    if sid=='SC064':photo=photo.with_name('SC098_CLEAN_V3.png')
    if sid=='SC090':
        # Do not reveal the previously rejected invented projection worksheet.
        photo=photo.with_name('SC100_CLEAN_V3.png')
    s=loader('CleanPhoto',photo,dur);last='CleanPhoto'
    for k,(x,y,w,h,angle,start,end) in enumerate(markers.get(sid,[])):
        mask=f'PaperMarkerMask{k}';ink=f'PaperMarkerInk{k}';reveal=f'PaperMarkerReveal{k}';mix=f'PaperMarkerMerge{k}'
        s+=node(mask,'RectangleMask',val('Center',f'{{{x/1672},{1-y/941}}}')+val('Width',w/1672)+val('Height',h/941)+val('Angle',angle))
        s+=node(ink,'Background',val('Width',1672)+val('Height',941)+val('TopLeftRed',.98)+val('TopLeftGreen',.80)+val('TopLeftBlue',.16)+val('TopLeftAlpha',.25)+link('EffectMask',mask,'Mask'))
        s+=fade(reveal,start,end)+merge(mix,last,ink,reveal,val('ApplyMode','FuID { "Multiply" }'));last=mix
    s+=color('Canvas',.035,.035,.035)
    s+=merge('CameraMove','Canvas',last,extra=expr('Size',f'{1920/1672}*(1+.012*min(time/{dur-1},1))'));last='CameraMove'
    if sid=='SC015':
        # Keep the requested chart entirely in the empty desk area; no backing rectangle.
        for name,x,value,h,year in [('Prior',.66,1.163,.02028,'H1 2025'),('Current',.83,16.286,.284,'H1 2026')]:
            s+=node(name+'BarMask','RectangleMask',expr('Height',f'{h}*min(max((time-35)/35,0),1)')+expr('Center',f'Point({x},.33+{h}/2*min(max((time-35)/35,0),1))')+val('Width',.06))
            s+=color(name+'Bar',.80,.055,.055,1,name+'BarMask')+merge(name+'BarMerge',last,name+'Bar');last=name+'BarMerge'
            s+=text(name+'Value',f'${value:.3f}B',x,.292,.027,'Inter')+merge(name+'ValueMerge',last,name+'Value');last=name+'ValueMerge'
            s+=text(name+'Year',year,x,.25,.020,'Inter')+merge(name+'YearMerge',last,name+'Year');last=name+'YearMerge'
    s+=node('MediaOut1','Saver',val('Index','"0"')+link('Input',last))
    path=OUT/(sid+'_CLEAN_V5.comp');body=comp(s,dur)
    forbidden=('SOURCE EXCERPT','ILLUSTRATIVE RECONSTRUCTION','SourcePaper','CreditPaper','ChartBacking','ResultPanel','Headline','Measure')
    assert not any(t in body for t in forbidden),sid
    path.write_text(body,encoding='utf-8')
    manifest.append({'scene_id':sid,'frames':dur,'timeline_start':r['timeline_start'],'photo':str(photo),'provenance':'ILLUSTRATIVE_GENERATED_BASE_NOT_AUTHENTIC_SCAN','comp_path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'removed':'All service labels, floating source strips, title/summary duplicates and opaque overlays','in_paper_markers':len(markers.get(sid,[])),'transparent_chart':sid=='SC015','status':'BUILT_NATIVE_RENDER_REVIEW_PENDING'})
(ROOT/'CLEAN_V5_MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps({'compositions':len(manifest),'service_labels':0,'floating_source_cards':0,'opaque_chart_backings':0,'new_generations':0}))
