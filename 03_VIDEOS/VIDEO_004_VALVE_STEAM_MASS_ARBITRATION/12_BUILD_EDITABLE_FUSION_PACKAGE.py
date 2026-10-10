#!/usr/bin/env python3
"""Build editable Fusion compositions for VIDEO004 from locked source/shot plans.
These are Resolve IMPORT CANDIDATES, not evidence of a successful Resolve render.
"""
import csv, json, pathlib, re, shutil, hashlib, zipfile
from PIL import Image
D=pathlib.Path(__file__).resolve().parent
OUT=D/"12_RESOLVE_EDITABLE_PACK_V1"
COMP=OUT/"Fusion_Comps"
MEDIA=OUT/"Media"
COMP.mkdir(parents=True,exist_ok=True)
MEDIA.mkdir(parents=True,exist_ok=True)
shotlist=list(csv.DictReader((D/"12_RESOLVE_COMPOSITIONS_V3.csv").open(encoding="utf8",newline="")))
scene_by_id={r["scene_id"]:r for r in csv.DictReader((D/"SCENE_TIMELINE.csv").open(encoding="utf8",newline=""))}
sync={r["shot_id"]:r for r in csv.DictReader((D/"12_RESOLVE_MARKER_WORD_SYNC_V3.csv").open(encoding="utf8",newline=""))}
asset_root=D/"12_VERIFIED_SOURCE_LAYERS"
source=json.loads((asset_root/"12_LAYER_ASSET_MANIFEST.json").read_text(encoding="utf8"))
assert len(shotlist)==175
def esc(s):
    return str(s).replace("\\","\\\\").replace('"','\\"').replace("\n"," ")
def node(name,ty,inputs):
    return f'    {name} = {ty} {{ Inputs = {{ {inputs} }}, ViewInfo = OperatorInfo {{ Pos = {{ 0, 0 }} }} }},\n'
def inp(name,val):
    return f'{name} = Input {{ Value = {val} }}, '
def link(name,src,output="Output"):
    return f'{name} = Input {{ SourceOp = "{src}", Source = "{output}" }}, '
def bg(name,hexcolor,alpha=1.0,mask=None):
    rr=[int(hexcolor[i:i+2],16)/255 for i in (1,3,5)]
    x=inp("Width",1920)+inp("Height",1080)+inp("TopLeftRed",round(rr[0],4))+inp("TopLeftGreen",round(rr[1],4))+inp("TopLeftBlue",round(rr[2],4))+inp("TopLeftAlpha",alpha)
    if mask:x+=link("EffectMask",mask,"Mask")
    return node(name,"Background",x)
def textbox(name,txt,x,y,size,font="Inter",color="#EDEDED"):
    rr=[int(color[i:i+2],16)/255 for i in (1,3,5)]
    ins=inp("StyledText",'"'+esc(txt)+'"')
    ins+=inp("Font",'"'+font+'"')+inp("Size",size)
    if font == "Bebas Neue": ins+=inp("Style",'"Regular"') # Installed family has no Bold face.
    ins+=inp("Center",'{ '+str(round(x,4))+', '+str(round(y,4))+' }')
    ins+=inp("Red1",round(rr[0],5))+inp("Green1",round(rr[1],5))+inp("Blue1",round(rr[2],5))
    return node(name,"TextPlus",ins)
def mask(name,x,y,w,h):
    return node(name,"RectangleMask",inp("Center","{ "+str(x)+", "+str(y)+" }")+inp("Width",w)+inp("Height",h))
def merge(name,base,top,blend=None):
    inputs=link("Background",base)+link("Foreground",top)
    if blend:inputs+=link("Blend",blend,"Value")
    return node(name,"Merge",inputs)
def fade(name,frames,fromvalue=0,to=1):
    f1=min(max(1,round(frames*.16)),15)
    return f'    {name} = BezierSpline {{ KeyFrames = {{ [0] = {{ {fromvalue}, Flags = {{ Linear = true }} }}, [{f1}] = {{ {to}, Flags = {{ Linear = true }} }} }} }},\n'
def label(sec):
    return {"S01":"THE RULES CHANGED","S02":"THE AGREEMENT","S03":"THOUSANDS OF CLAIMS","S04":"UNVERIFIED COST","S05":"FOUR CLAIMANTS","S06":"A NEW CONTRACT","S07":"ACCESS VS LICENSE","S08":"PENDING CASES","S09":"VALVE SUES","S10":"WHICH AGREEMENT?","S11":"PRELIMINARY RULING","S12":"APPEAL AND STAY","S13":"WHAT REMAINS"}.get(sec,"WHAT IT COST")
def subtext(row):
    x=row["style"]
    if x=="TWO_POSITION_COMPARE":return ["CLAIMANTS' POSITION","VALVE'S POSITION"]
    if x=="MECHANISM_MAP":return ["ARBITRATION","COURT"]
    if x=="CHRONOLOGY":return ["BEFORE","AFTER"]
    if x=="NUMBER_CONTEXT":return ["DATE / COUNT","SOURCE REQUIRED"]
    if x=="EVIDENCE_STACK":return ["RECORD","RESPONSE"]
    if x=="EDITORIAL_QUESTION":return ["THE QUESTION","THE EVIDENCE"]
    return ["CLAIM","RESPONSE"]
BEAT_TITLES={
"B001":"ACCOUNT ACCESS","B002":"CLAIMANTS BECOME DEFENDANTS","B003":"THE ACCEPT BUTTON",
"B004":"TWO SEPARATE DISPUTES","B005":"TWO CONTRACTS","B006":"THE FIRST ALLEGATIONS",
"B007":"WHY ARBITRATION?","B008":"INDIVIDUAL-ONLY PROCEDURE","B009":"ONE FILE BECOMES MANY",
"B010":"DATED CLAIMANT COUNTS","B011":"FILINGS ARE NOT VICTORIES","B012":"THE COST OF REPETITION",
"B013":"THE MONEY QUESTION","B014":"$20M? UNVERIFIED","B015":"WHAT THE FEES COVER",
"B016":"THE PUBLISHED SCHEDULE","B017":"THE FOUR-CLAIMANT TURN","B018":"FOUR CLAIMANTS",
"B019":"CLAUSE CHALLENGED","B020":"DIFFERENT COHORTS","B021":"ALREADY IN PROCESS",
"B022":"THE CASES DID NOT VANISH","B023":"SEPTEMBER 2024","B024":"CAN NEW TERMS APPLY?",
"B025":"WHAT DID THEY ACCEPT?","B026":"ACCESS VERSUS LICENSE","B027":"LICENSES / ACCOUNT USE",
"B028":"ACCEPTANCE EVIDENCE","B029":"THE CLICK'S TWO SIDES","B030":"WHO DECIDES?",
"B031":"AAA DID NOT CLOSE THEM","B032":"THE LEGAL DECISION","B033":"SEPTEMBER / OCTOBER",
"B034":"VALVE REQUESTS A STOP","B035":"FIRST FILING STRUCK","B036":"LAWSUIT IS NOT RELIEF",
"B037":"COUNTS CHANGE","B038":"THE REVERSAL","B039":"AN EMERGENCY STANDARD",
"B040":"PRELIMINARY INJUNCTION","B041":"WORK ALREADY DONE","B042":"THE ACTIVE CASES",
"B043":"OLD TERMS / NEW TERMS","B044":"PRELIMINARY DENIAL","B045":"AS APPLIED","B046":"THE FAIRNESS QUESTION",
"B047":"EMERGENCY STANDARD","B048":"THE CLICK DID NOT SETTLE IT","B049":"CERTIFIED APPEAL",
"B050":"TWO DIFFERENT QUESTIONS","B051":"APPEAL IS NOT REVERSAL","B052":"A DOCKET SNAPSHOT",
"B053":"THE OPEN CONTRACT FIGHT","B054":"WHAT REMAINS OPEN"
}
info={"status":"175_EDITABLE_FUSION_COMPS_BUILT_NOT_RENDER_QC","frame_rate":25,"frame_width":1920,"frame_height":1080,
      "subtitle_safe_y_start":918,"source_artifact_run":38057742171,"master_sha256":"8c11be2619a6a84b7e1a6cbe0cb8c708d72dff556d1d737dd46f596ea21f65d7",
      "active_shorts":["SH01","SH02","SH04","SH08"],"shots":[],"source_assets":len(source["source_crops"])}
Image.new("RGB",(1920,1080),(31,31,31)).save(MEDIA/"EDIT_BASE.png")
for row in shotlist:
    sid=row["shot_id"];frames=int(row["duration_frames"])
    assert int(row["end_frame"])-int(row["start_frame"])==frames and frames>0
    section=row["scene_id"]
    chapter=scene_by_id.get(row["scene_id"],{}).get("script_ref","").split(":")[0]
    # Actual section comes from canonical scene map, not a guessed court claim.
    scene_id=row["scene_id"]
    isdoc=row["style"].startswith("DOCUMENT")
    isend=row["style"]=="NATIVE_END_SCREEN"
    nodes=""
    nodes+=bg("Backdrop","#1F1F1F")
    last="Backdrop"
    if isdoc and sid in source["shots"]:
        item=source["shots"][sid]
        f=item["document_layer"]
        nodes+=node("AuthenticPDF","Loader",inp("Clip",'"__PACK_ROOT__/Media/'+esc(f)+'"'))
        nodes+=merge("MergeEvidence",last,"AuthenticPDF")
        last="MergeEvidence"
    if isdoc and sid not in source["shots"]:
        # No fake PDF: retain neutral source-index treatment.
        nodes+=textbox("SourceHold","SOURCE CAPTURE PENDING",.50,.46,.07,color="#B69B68")
        nodes+=merge("MergeEvidence",last,"SourceHold")
        last="MergeEvidence"
    if not isend:
        nodes+=textbox("TopBrand","WHAT IT COST",.12,.09,.028,"Bebas Neue")
        nodes+=merge("BrandMerge",last,"TopBrand")
        last="BrandMerge"
        section_id=chapter
        # Avoid unsourced quotations. Editor-native story labels are not narration captions.
        title=BEAT_TITLES.get(row["beat_id"],label(chapter))
        # The source shot table omits script_ref; refer to canonical mapping in shot metadata below.
        if title=="WHAT IT COST":title="VALVE / STEAM"
        if not isdoc:
            nodes+=textbox("ChapterLabel",title,.46,.22,.075,"Bebas Neue")
            nodes+=fade("ChapterIn",frames)
            nodes+=merge("MergeHeading",last,"ChapterLabel","ChapterIn")
            last="MergeHeading"
            style=row["style"]
            if style in ("TWO_POSITION_COMPARE","MECHANISM_MAP","CHRONOLOGY","EVIDENCE_INSERT_OR_COMPARE","EVIDENCE_STACK"):
                nodes+=mask("BoxLeftMask",.275,.50,.39,.43)
                nodes+=bg("PanelLeft","#3A3A3A",.72,"BoxLeftMask")
                nodes+=merge("MergeLeft",last,"PanelLeft")
                last="MergeLeft"
                nodes+=mask("BoxRightMask",.725,.50,.39,.43)
                nodes+=bg("PanelRight","#0B0B0B",.90,"BoxRightMask")
                nodes+=fade("CounterpositionIn",frames)
                nodes+=merge("MergeRight",last,"PanelRight","CounterpositionIn")
                last="MergeRight"
                left,right=subtext(row)
                if chapter=="S03":left,right="DATED DEMANDS","DATED CLAIMANTS"
                elif chapter=="S04":left,right="$20M? UNVERIFIED","VERIFIED FEE SCHEDULE"
                elif chapter=="S06":left,right="OLDER TERMS","UPDATED TERMS"
                elif chapter=="S07":left,right="ACCESS CONCERN","VALVE RESPONSE"
                elif chapter=="S08":left,right="AAA REQUEST","AAA RESPONSE"
                elif chapter=="S09":left,right="VALVE FILING","COURT PROCESS"
                elif chapter=="S11":left,right="PRELIMINARY","AS APPLIED"
                elif chapter=="S12":left,right="CERTIFIED ISSUE","DISTRICT STAY"
                nodes+=textbox("LeftLabel",left,.275,.48,.037)
                nodes+=merge("MergeLeftLabel",last,"LeftLabel")
                last="MergeLeftLabel"
                nodes+=textbox("RightLabel",right,.725,.48,.037)
                nodes+=merge("MergeRightLabel",last,"RightLabel","CounterpositionIn")
                last="MergeRightLabel"
            elif style=="NUMBER_CONTEXT":
                nodes+=textbox("NumberLabel","COUNTS REQUIRE DATES",.47,.50,.046,color="#EDEDED")
                nodes+=merge("MergeNumber",last,"NumberLabel")
                last="MergeNumber"
            else:
                nodes+=textbox("IndexLabel","EVIDENCE / CONSEQUENCE",.50,.50,.047)
                nodes+=merge("MergeQuestion",last,"IndexLabel")
                last="MergeQuestion"
        else:
            nodes+=textbox("SourceLabel","COURT RECORD / SOURCE DETAIL",.78,.13,.028,"Inter")
            nodes+=merge("MergeSourceLabel",last,"SourceLabel")
            last="MergeSourceLabel"
        notes=row["source_ids"].replace(";"," / ")
        nodes+=textbox("CitedSource","SOURCES: "+notes,.30,.81,.021,"Inter",color="#B69B68")
        nodes+=merge("MergeCite",last,"CitedSource")
        last="MergeCite"
    else:
        nodes+=textbox("EndWordmark","WHAT IT COST",.50,.32,.13,"Bebas Neue")
        nodes+=merge("MergeEnd",last,"EndWordmark")
        last="MergeEnd"
    # Marker source is an independently editable transparent PNG, never baked into PDF.
    marker=source["shots"].get(sid,{}).get("marker_layer")
    if marker and sync.get(sid,{}).get("status","").startswith("ASR_WORD_ANCHORED"):
        nodes+=node("VerifiedLineMask","Loader",inp("Clip",'"__PACK_ROOT__/Media/'+esc(marker)+'"'))
        # Gate entire marker OFF by default until independent listening approval.
        nodes+=node("MarkerGate","Merge",link("Background",last)+link("Foreground","VerifiedLineMask")+inp("Blend",0))
        last="MarkerGate"
    nodes+=node("MediaOut1","MediaOut",link("Input",last))
    contents="{\n  Tools = ordered() {\n"+nodes+"  },\n  ActiveTool = \"MediaOut1\"\n}\n"
    (COMP/(sid+".setting")).write_text(contents,encoding="utf8")
    info["shots"].append({"shot_id":sid,"start_frame":int(row["start_frame"]),"end_frame":int(row["end_frame"]),
        "duration_frames":frames,"composition":row["style"],"source_ids":row["source_ids"],"claim_ids":scene_by_id.get(row["scene_id"],{}).get("claim_ids",""), "editable_setting":"Fusion_Comps/"+sid+".setting",
        "authentic_doc":isdoc and sid in source["shots"],"marker_active_after_listen":bool(marker)})
for name in sorted(set(v["document_layer"] for v in source["shots"].values())|set(v["marker_layer"] for v in source["shots"].values() if v["marker_layer"])):
    shutil.copy2(asset_root/name,MEDIA/name)
assert info["shots"][-1]["end_frame"]==20700
assert all(a["end_frame"]==b["start_frame"] for a,b in zip(info["shots"],info["shots"][1:]))
(OUT/"RESOLVE_SHOT_MANIFEST.json").write_text(json.dumps(info,indent=2)+"\n",encoding="utf8")
print(json.dumps({"settings":len(info["shots"]),"source_png_copied":len(list(MEDIA.glob("*.png"))),"last_frame":info["shots"][-1]["end_frame"],"size_mb":sum(p.stat().st_size for p in OUT.rglob("*") if p.is_file())/1e6}))
