"""Build native editable Fusion comps, extracting authentic pixels via ffmpeg."""
import csv,json,subprocess,math,re
from pathlib import Path
from PIL import Image
import numpy as np

ROOT=Path(__file__).resolve().parent
PACK=ROOT.parent/'VIDEO008_FINAL_VISUAL_PACK'
BASE=PACK/'IMAGEGEN_REPLACEMENTS'
REPO=Path(r'C:\Users\KK\Youtube-3-video008-assembly\03_VIDEOS\VIDEO_008_CLAUDE_80_7_BILLION_LOSS_IPO_FILING')
COMPS=ROOT/'COMPS'; EX=ROOT/'AUTHENTIC_EXCERPTS'
COMPS.mkdir(exist_ok=True);EX.mkdir(exist_ok=True)
scenes={r['scene_id']:r for r in csv.DictReader((REPO/'11_SCENE_TIMELINE.csv').open(encoding='utf-8-sig'))}
jobs=json.loads((BASE/'CLEAN_V3_PROMPTS.json').read_text())['jobs']
jobs.append({'id':'SC005','kind':'AUTHENTIC_EVIDENCE','refs':['',str(PACK/'DOCUMENTS/CROPS/SC005_SRC001_AUTHENTIC_CROP.png')],'source_ids':'SRC001'})
titles={
'SC002':('TWO DIFFERENT LOSSES','GAAP -$80.748B  |  OPERATING -$0.693B'),
'SC005':('THE ACCOUNTING REVALUATION','-$72.388B  |  H1 2026'),
'SC007':('ONE DAY. TWO EVENTS.','OCT 26, 2026  |  09:00 FILING  /  16:15 ANNOUNCEMENT'),
'SC010':('WHO BUYS THE MACHINES?','FINANCIERS  /  SPV  /  BROADCOM EQUIPMENT  /  ANTHROPIC'),
'SC013':('FIVE YEARS OF RENT','~$125.2B  |  EXCLUDING INTEREST'),
'SC015':('REVENUE SURGED','H1 2025: $1.163B  |  H1 2026: $16.286B'),
'SC018':('THE PHYSICAL COST OF GROWTH','$8.945B  |  COMPUTE + INFRASTRUCTURE  |  H1 2026'),
'SC020':('FINANCING THE MACHINES','$63B ANNOUNCED EQUIPMENT FINANCING'),
'SC025':('GROWTH DOES NOT REMOVE RISK','FORWARD-LOOKING STATEMENTS'),
'SC027':('RENT UNDER SPECIFIED TERMS','FIVE-YEAR ARRANGEMENT  |  EXCLUDING INTEREST'),
'SC029':('PAYMENTS FOLLOW READINESS','READY FOR SERVICE  /  QUARTERLY PAYMENTS'),
'SC031':('WHEN THE PAYMENTS START','EQUIPMENT READINESS  |  QUARTERLY INSTALMENTS'),
'SC034':('THE COST OF REVERSING COURSE','NON-CANCELLABILITY  |  CONTRACTUAL QUALIFIERS'),
'SC036':('DO NOT ADD THESE','$125.2B GROSS RENT  |  $63B FINANCING  |  OVERLAP UNRECONCILED'),
'SC038':('THE VEHICLE OWNS THE HARDWARE','SPV PURCHASE  |  LEASE TO ANTHROPIC'),
'SC040':('TWO FINANCING LAYERS','FIRST LIEN: BOFA / CITI / MS  |  SECOND-LIEN PORTION: BLACKSTONE'),
'SC043':('RESIDUAL-VALUE SUPPORT','TIED TO THE FIRST-LIEN PORTION  |  NO CASH PAYMENT PROVEN'),
'SC045':('ARRANGED BEFORE DELIVERY','2026 ANNOUNCEMENT  /  2027 EXPECTED DELIVERIES'),
'SC049':('UP TO IS THE CRUCIAL PHRASE','$42B POTENTIAL NOTES  |  SUBJECT TO CONDITIONS'),
'SC051':('A FORMULA IS NOT A RECEIPT','$30B NOTE-PURCHASE FORMULA  |  CONDITIONS APPLY'),
'SC053':('PRINCIPAL IS A DIFFERENT MEASURE','$6.2B AMAZON NOTE PRINCIPAL  |  JUNE 30, 2026'),
'SC055':('THREE DIFFERENT MEASURES','CONDITIONAL NOTES  |  EQUIPMENT RENT  |  CUSTOMER REVENUE'),
'SC057':('THE FAIR-VALUE LINE','-$72.388B  |  FINANCING INSTRUMENT REVALUATION'),
'SC059':('THE OPERATING CALCULATION','$16.286B - $16.979B = -$0.693B'),
'SC062':('BELOW THE OPERATING LINE','+$1.111B INTEREST  |  -$8.757B OTHER EXPENSE  |  -$21M TAX'),
'SC064':('TWO DIFFERENT RISKS','REPORTED ACCOUNTING CHARGE  |  FUTURE RENT EXPOSURE'),
'SC066':('THE HEADLINE EXPLAINED','GAAP -$80.748B  |  OPERATING -$0.693B  |  FV -$72.388B'),
'SC069':('CAPITAL AND CONTROL','ECONOMIC PARTICIPATION  |  GENERAL SHAREHOLDER VOTES'),
'SC071':('ONE SPECIAL CLASS F SHARE','50.1% OF GENERAL VOTING POWER  |  PROPOSED STRUCTURE'),
'SC073':('TWO GOVERNANCE MECHANISMS','CLASS F: GENERAL VOTES  |  CLASS T: DIRECTOR ELECTIONS'),
'SC076':('THE TRUST RIGHTS HAVE CONDITIONS','MAJORITY OF AUTHORIZED DIRECTORS  |  SPECIAL SEAT APPROVAL'),
'SC078':('IF THE OFFERING CLOSES','PROPOSED POST-OFFERING STRUCTURE  |  CONDITIONS APPLY'),
'SC080':('WHO EVALUATES THE DECISION?','GENERAL VOTES  |  BOARD OVERSIGHT  |  DIRECTOR ELECTIONS'),
'SC082':('UNUSUAL EVALUATION SETUPS','ANTHROPIC ACCOUNT  |  NOT NORMAL CUSTOMER USE'),
'SC084':('FOUR REPORTED INCIDENTS','ISSUER ASSESSMENT  |  INVESTIGATED + PARTIES NOTIFIED'),
'SC086':('A DEMAND FOR INFORMATION','ISSUER-REPORTED FTC INQUIRY  |  NO VIOLATION FINDING'),
'SC090':('WHAT THE EVIDENCE CAN SHOW','DOCUMENTED TERMS  |  FUTURE DEMAND + OUTCOME UNKNOWN'),
'SC092':('THE CASE FOR EXPANSION','$1.163B TO $16.286B  |  COMPARABLE HALF-YEARS'),
'SC094':('FUNDING CANNOT GUARANTEE SALES','$63B ANNOUNCED  /  EQUIPMENT EXPECTED FROM 2027'),
'SC098':('TWO DIFFERENT CLOCKS','PAST HALF-YEAR RESULT  |  FUTURE FIVE-YEAR RENT'),
'SC100':('BUYING STOCK AND BUYING CONTROL','VOTING RIGHTS  |  ECONOMIC RIGHTS  |  PROPOSED IPO'),
'SC102':('THE FILING WAS PRELIMINARY','OCT 26, 2026  |  OFFERING NOT YET COMPLETED'),
'SC104':('THREE ROWS. THREE MEANINGS.','ACCOUNTING MEASURES  |  NO INVENTED CASH-FLOW TOTAL'),
'SC106':('FUTURE EXPOSURE, DIFFERENT MEASURES','~$125.2B RENT  |  $63B ANNOUNCED FINANCING'),
'SC108':('THE VOTE IS A SEPARATE QUESTION','FOUNDER CLASS F  |  TRUST CLASS T  |  CONDITIONS APPLY')}

def esc(x):return str(x).replace('\\','\\\\').replace('"','\\"').replace('\n','\\n')
def val(k,v):return f'{k} = Input {{ Value = {v} }}, '
def expr(k,v):return f'{k} = Input {{ Expression = "{esc(v)}" }}, '
def link(k,n,out='Output'):return f'{k} = Input {{ SourceOp = "{n}", Source = "{out}" }}, '
def node(n,t,ins):return f'{n} = {t} {{ Inputs = {{ {ins} }}, ViewInfo = OperatorInfo {{ Pos = {{ 0, 0 }} }} }},\n'
def loader(n,p,dur):return f'{n} = Loader {{ Clips = {{ Clip {{ ID = "Clip1", Filename = "{esc(p)}", FormatID = "PNGFormat", Length = 1, LengthSetManually = true, GlobalStart = 0, GlobalEnd = {dur-1}, TrimIn = 0, TrimOut = 0, ExtendFirst = 0, ExtendLast = {dur-1}, Loop = 1 }} }}, Inputs = {{ ["Gamut.SLogVersion"] = Input {{ Value = FuID {{ "SLog2" }} }} }} }},\n'
def color(n,r,g,b,a=1,mask=None):
    s=val('Width',1920)+val('Height',1080)+val('TopLeftRed',r)+val('TopLeftGreen',g)+val('TopLeftBlue',b)+val('TopLeftAlpha',a)
    if mask:s+=link('EffectMask',mask,'Mask')
    return node(n,'Background',s)
def text(n,t,x,y,size,font='Bebas Neue',rgb=(.93,.93,.91)):
    def glyph(name,px,py,c):
        return node(name,'TextPlus',val('Width',1920)+val('Height',1080)+val('UseFrameFormatSettings',1)+val('StyledText','"'+esc(t)+'"')+val('Font','"'+font+'"')+val('Style','"Regular"')+val('Size',size)+val('Center',f'{{ {px}, {py} }}')+val('Red1',c[0])+val('Green1',c[1])+val('Blue1',c[2]))
    if max(rgb)<.2:return glyph(n,x,y,rgb)
    s=glyph(n+'Shadow',x+.0013,y-.0022,(.025,.025,.025))+glyph(n+'Face',x,y,rgb)
    return s+merge(n,n+'Shadow',n+'Face')
def merge(n,b,f,blend=None,extra=''):
    return node(n,'Merge',link('Background',b)+link('Foreground',f)+(link('Blend',blend,'Value') if blend else '')+extra)
def fade(n,start,end):return f'{n} = BezierSpline {{ KeyFrames = {{ [{start}] = {{ 0, RH = {{ {start+(end-start)*.4}, 0 }} }}, [{end}] = {{ 1, LH = {{ {end-(end-start)*.4}, 1 }} }} }} }},\n'
def rect(n,x,y,w,h):return node(n,'RectangleMask',val('Center',f'{{{x},{y}}}')+val('Width',w)+val('Height',h))
def comp(nodes,dur):return 'Composition { CurrentTime = 70, GlobalRange = {0,'+str(dur-1)+'}, RenderRange = {0,'+str(dur-1)+'}, HiQ = true, Tools = {\n'+nodes+'}, Prefs = { Comp = { FrameFormat = { Width = 1920, Height = 1080, Rate = 25 }, Unsorted = { GlobalEnd = '+str(dur-1)+' } } } }'

def extract(sid,source):
    a=np.array(Image.open(source).convert('RGB'));r,g,b=[a[:,:,i].astype(float) for i in range(3)]
    mask=(r>180)&(g>130)&(g<205)&(b<95)
    dense=mask.sum(axis=1)>200
    yy,xx=np.where(mask & dense[:,None])
    if len(xx)>20:
        x0,x1,y0,y1=int(xx.min()),int(xx.max()),int(yy.min()),int(yy.max())
        # Remove the existing editorial outline, keeping original source pixels inside.
        x=x0+7;y=y0+7;w=x1-x0-13;h=y1-y0-13
        if w<70 or h<8:raise ValueError((sid,x,y,w,h))
    else:
        x,y,w,h=480,310,640,210
        if a.shape[1]<1200:x,y,w,h=10,150,a.shape[1]-20,min(240,a.shape[0]-160)
    if sid in ('SC013','SC106'):x,y,w,h=488,443,624,14
    if sid in ('SC027','SC029','SC031'):x,y,w,h=488,465,624,47
    if sid=='SC034':x,y,w,h=488,473,624,181
    if sid in ('SC073','SC076','SC108'):x,y,w,h=8,531,1584,36
    if sid=='SC053':x,y,w,h=701,443,65,14
    if sid in ('SC082','SC084'):x,y,w,h=440,365,710,225
    target=EX/(sid+'_SOURCE_PIXELS.png')
    subprocess.run(['ffmpeg','-v','error','-y','-i',str(source),'-vf',f'crop={w}:{h}:{x}:{y}','-frames:v','1',str(target)],check=True)
    return target,w,h,{'source':str(source),'crop_xywh':[x,y,w,h]}

records=[]
for j in sorted(jobs,key=lambda j:j['id']):
    sid=j['id']; row=scenes[sid]; dur=int(row['duration_frames']);title,sub=titles[sid]
    photo=BASE/('SC005_COMPOSITION_CLEAN_PROPS_V2.png' if sid=='SC005' else sid+'_CLEAN_V3.png')
    nodes=loader('CleanPhoto',photo,dur)
    # Resolve's MediaOut fits the native Loader. Use a 1920 background to anchor overlays.
    nodes+=color('Canvas',.043,.043,.043)
    nodes+=merge('PhotoMerge','Canvas','CleanPhoto',extra=expr('Size',f'{1920/1672}*(1+.018*min(time/{dur-1},1))'))
    last='PhotoMerge'
    if sid=='SC090':
        # Conceal the generated worksheet; no projected financial series is evidence.
        nodes+=rect('UncertaintyCoverMask',.5,.48,.92,.57)+color('UncertaintyCover',.035,.035,.035,1,'UncertaintyCoverMask')
        nodes+=merge('UncertaintyCoverMerge',last,'UncertaintyCover');last='UncertaintyCoverMerge'
    nodes+=text('Headline',title,.5,.914,min(.072,1.75/max(len(title),1)))+fade('HeadlineReveal',3,17)
    nodes+=merge('HeadlineMerge',last,'Headline','HeadlineReveal');last='HeadlineMerge'
    nodes+=text('Measure',sub,.5,.825,min(.032,1.60/max(len(sub),1)),'Inter')+fade('MeasureReveal',20,34)
    nodes+=merge('MeasureMerge',last,'Measure','MeasureReveal');last='MeasureMerge'
    source=Path(j['refs'][1])
    if sid in ('SC031','SC034'):source=PACK/'DOCUMENTS/CROPS/SC013_SRC001_AUTHENTIC_CROP.png'
    if sid=='SC043':source=PACK/'DOCUMENTS/CROPS/SC038_SRC017_AUTHENTIC_CROP.png'
    excerpt,w,h,provenance=extract(sid,source)
    # Source-native excerpt replaces generated factual detail in a clear editable insert.
    chart=sid in ('SC015','SC092')
    scale=min((700 if chart else 1370)/w,340/h); panelh=h*scale/1080
    cy=.46 if chart or panelh>.20 else [.43,.50,.55][int(sid[2:])%3]
    cx=.28 if chart else .5
    merge_scale=scale
    if sid in ('SC034','SC053','SC073','SC076','SC108'):
        # Conform extreme aspect-ratio crops before Fusion to avoid Loader cache/large-scale GPU errors.
        # A new filename also prevents stale source dimensions from the earlier version.
        targetw=1700 if sid in ('SC073','SC076','SC108') else min(1370,round(w*scale))
        targeth=max(2,round(h*targetw/w));panelh=targeth/1080
        safe=EX/(sid+'_CONFORMED_RGBA_FINAL.png')
        subprocess.run(['ffmpeg','-v','error','-y','-i',str(excerpt),'-vf',f'scale={targetw}:{targeth}:flags=lanczos,format=rgba,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=0x00000000','-frames:v','1',str(safe)],check=True)
        excerpt=safe;merge_scale=1
    if sid=='SC053':panelh=.13
    nodes+=loader('AuthenticSource',excerpt,dur)
    nodes+=rect('PaperMask',cx,cy,.93 if sid in ('SC073','SC076','SC108') else (.395 if chart else .75),panelh+.045)+color('SourcePaper',.95,.94,.90,1,'PaperMask')
    nodes+=fade('EvidenceReveal',40,58)
    nodes+=merge('PaperMerge',last,'SourcePaper','EvidenceReveal');last='PaperMerge'
    if sid=='SC053':
        nodes+=text('TypesetFigure','$6.2 billion',cx,cy,.11,'Inter',(.045,.045,.045))
        nodes+=merge('SourceMerge',last,'TypesetFigure','EvidenceReveal');last='SourceMerge'
    else:
        nodes+=merge('SourceMerge',last,'AuthenticSource','EvidenceReveal',val('Center',f'{{{cx},{cy}}}')+val('Size',merge_scale));last='SourceMerge'
    # A restrained translucent yellow marker travels across the exact source-pixel strip.
    if sid not in ('SC007','SC015','SC045','SC078','SC090','SC092','SC094','SC098','SC104'):
        markh=min(.035,panelh*.72)
        nodes+=node('MarkerMask','RectangleMask',expr('Center',f'Point(.145+.355*min(max((time-72)/28,0),1),{cy})')+expr('Width','.71*min(max((time-72)/28,0),1)')+val('Height',markh))
        nodes+=color('YellowMarker',.94,.77,.25,.32,'MarkerMask')+fade('MarkerReveal',72,100)
        nodes+=merge('MarkerMerge',last,'YellowMarker','MarkerReveal',val('ApplyMode','FuID { "Multiply" }'));last='MarkerMerge'
    label='SOURCE EXCERPT  |  '+re.search(r'SRC\d+',source.name).group()
    if sid=='SC053':label='FILING FIGURE (TYPESET)  |  SRC001'
    if sid in ('SC073','SC076','SC108'):label+='  |  AFTER CLASS F SUNSET'
    if sid=='SC043':label='BOFA PARTNER ANNOUNCEMENT EXCERPT  |  SRC017'
    credity=max(.27,cy-panelh/2-.055)
    nodes+=rect('CreditPaperMask',cx,credity,.40 if chart else .61,.035)+color('CreditPaper',.95,.94,.90,1,'CreditPaperMask')
    nodes+=merge('CreditPaperMerge',last,'CreditPaper','EvidenceReveal');last='CreditPaperMerge'
    nodes+=text('SourceCredit',label,cx,credity,.016 if chart else .018,'Inter',(.05,.05,.05))+fade('CreditReveal',40,58)
    nodes+=merge('CreditMerge',last,'SourceCredit','CreditReveal');last='CreditMerge'
    nodes+=rect('ReconstructionPaperMask',.5,.225,.46,.034)+color('ReconstructionPaper',.95,.94,.90,1,'ReconstructionPaperMask')
    nodes+=merge('ReconstructionPaperMerge',last,'ReconstructionPaper');last='ReconstructionPaperMerge'
    nodes+=text('ReconstructionCredit','BACKGROUND: ILLUSTRATIVE RECONSTRUCTION',.5,.225,.016,'Inter',(.05,.05,.05))
    nodes+=merge('ReconstructionCreditMerge',last,'ReconstructionCredit');last='ReconstructionCreditMerge'
    if sid=='SC106':
        extra,ew,eh,_=extract('SC106_FINANCING',PACK/'DOCUMENTS/CROPS/SC038_SRC017_AUTHENTIC_CROP.png')
        nodes+=loader('FinancingSource',extra,dur)+rect('FinancingPaperMask',.5,.64,.75,.10)+color('FinancingPaper',.95,.94,.90,1,'FinancingPaperMask')+fade('FinancingReveal',90,105)
        nodes+=merge('FinancingPaperMerge',last,'FinancingPaper','FinancingReveal');last='FinancingPaperMerge'
        nodes+=merge('FinancingSourceMerge',last,'FinancingSource','FinancingReveal',val('Size',1370/ew)+val('Center','{.5,.64}'));last='FinancingSourceMerge'
        nodes+=text('FinancingCredit','SEPARATE PARTNER ANNOUNCEMENT  |  SRC017',.5,.565,.018,'Inter')
        nodes+=merge('FinancingCreditMerge',last,'FinancingCredit','FinancingReveal');last='FinancingCreditMerge'
    if sid in ('SC015','SC092'):
        # Accurate chart: zero-based heights, 1.163/16.286 ratio; independent masked bars.
        nodes+=rect('ChartBackingMask',.74,.50,.35,.43)+color('ChartBacking',.035,.035,.035,.94,'ChartBackingMask')
        nodes+=merge('ChartBackingMerge',last,'ChartBacking');last='ChartBackingMerge'
        for n,x,num,maxh in [('Prior',.66,1.163,.0214),('Current',.83,16.286,.30)]:
            nodes+=node(n+'BarMask','RectangleMask',expr('Height',f'{maxh}*min(max((time-55)/35,0),1)')+expr('Center',f'Point({x},.35+{maxh}/2*min(max((time-55)/35,0),1))')+val('Width',.065))
            nodes+=color(n+'Bar',.82,.13,.13,1,n+'BarMask')
            nodes+=merge(n+'BarMerge',last,n+'Bar');last=n+'BarMerge'
            nodes+=text(n+'Value',f'${num:.3f}B',x,.31,.028,'Inter')
            nodes+=merge(n+'LabelMerge',last,n+'Value');last=n+'LabelMerge'
            nodes+=text(n+'Year','H1 2025' if n=='Prior' else 'H1 2026',x,.265,.020,'Inter')
            nodes+=merge(n+'YearMerge',last,n+'Year');last=n+'YearMerge'
    if sid=='SC104':
        for k,t in enumerate(['GAAP NET LOSS   -$80.748B','OPERATING LOSS   -$0.693B','FAIR-VALUE CHARGE   -$72.388B']):
            nodes+=rect('ResultMask'+str(k),.5,.63-k*.14,.82,.12)+color('ResultPanel'+str(k),.035,.035,.035,.95,'ResultMask'+str(k))
            nodes+=fade('ResultReveal'+str(k),30+k*20,44+k*20)
            nodes+=merge('ResultPanelMerge'+str(k),last,'ResultPanel'+str(k),'ResultReveal'+str(k));last='ResultPanelMerge'+str(k)
            nodes+=text('ResultText'+str(k),t,.5,.63-k*.14,.046)
            nodes+=merge('ResultTextMerge'+str(k),last,'ResultText'+str(k),'ResultReveal'+str(k));last='ResultTextMerge'+str(k)
    nodes+=node('MediaOut1','Saver',val('Index','"0"')+link('Input',last))
    path=COMPS/(sid+'_EDITABLE.comp');path.write_text(comp(nodes,dur),encoding='utf-8')
    records.append({'scene_id':sid,'comp_path':str(path),'frames':dur,'timeline_start':int(row['start_frame_25fps']),'photo':str(photo),'headline':title,'summary':sub,'source_excerpt':str(excerpt),'source_pixels':provenance,'source_text_qc':'SOURCE_PIXEL_EXTRACTION_NOT_GENERATED','status':'BUILT_IMPORT_AND_RENDER_QC_PENDING'})
(ROOT/'FUSION_BUILD_MANIFEST.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
print(json.dumps({'compositions':len(records),'authentic_source_excerpts':len(records),'output':str(COMPS)}))
