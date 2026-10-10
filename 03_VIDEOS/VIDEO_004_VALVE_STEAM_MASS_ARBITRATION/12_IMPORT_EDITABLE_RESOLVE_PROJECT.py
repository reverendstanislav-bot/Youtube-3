#!/usr/bin/env python3
"""Run inside DaVinci Resolve 19/20's Python console (or its scripting host).
Creates a NEW review project, never replaces or modifies owner's approved edit.
The Fusion .setting files are unverified until Resolve successfully loads them.
"""
import json, pathlib, os, sys, argparse, hashlib, shutil

def connect_resolve():
    try:import DaVinciResolveScript as dvr
    except ImportError:
        path = os.environ.get("RESOLVE_SCRIPT_API",
                r"C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting\Modules")
        sys.path.append(path)
        import DaVinciResolveScript as dvr
    app=dvr.scriptapp("Resolve")
    if not app:raise RuntimeError("DaVinci Resolve scripting service unavailable; open Resolve first")
    return app

def run(root,master,canary=8,all_shots=False):
    root=pathlib.Path(root).resolve()
    manifest=json.loads((root/"RESOLVE_SHOT_MANIFEST.json").read_text("utf8"))
    shots=manifest["shots"] if all_shots else manifest["shots"][:canary]
    assert len(manifest["shots"])==175
    assert pathlib.Path(master).is_file(), "Provide actual approved WAV master, no substitute audio"
    audio_hash=hashlib.sha256(pathlib.Path(master).read_bytes()).hexdigest()
    assert audio_hash==manifest["master_sha256"], "REFUSE wrong Harrison master WAV"
    resolve=connect_resolve()
    pm=resolve.GetProjectManager()
    name="VIDEO004_FUSION_EDIT_REVIEW_"+("FULL" if all_shots else "CANARY_%02d"%canary)
    existing=pm.GetProjectListInCurrentFolder() or []
    if name in existing:raise RuntimeError("Project already exists. No overwrite; choose a new name.")
    project=pm.CreateProject(name)
    if not project:raise RuntimeError("Cannot create Resolve project")
    for k,v in (("timelineFrameRate","25"),("timelineResolutionWidth","1920"),
                ("timelineResolutionHeight","1080")):
        if not project.SetSetting(k,v):raise RuntimeError("Could not lock project "+k)
    pool=project.GetMediaPool()
    media=pool.ImportMedia([str(root/"Media"/"EDIT_BASE.png"), str(pathlib.Path(master).resolve())])
    if not media or len(media)!=2:raise RuntimeError("Unable to import canvas media and Harrison WAV")
    base,wav=media
    timeline=pool.CreateEmptyTimeline(name+"_25FPS")
    if not timeline:raise RuntimeError("Could not create timeline")
    project.SetCurrentTimeline(timeline)
    result=[]
    for i,row in enumerate(shots):
        st=int(row["start_frame"])
        end=int(row["end_frame"])
        dur=end-st
        assert dur>0
        item=pool.AppendToTimeline([{"mediaPoolItem":base,"startFrame":0,"endFrame":dur,
                                     "recordFrame":st,"mediaType":1,"trackIndex":1}])
        if not item:raise RuntimeError("AppendToTimeline failed at "+row["shot_id"])
        ti=item[0]
        # Fail immediately on frame placement drift; do not continue a broken timeline.
        if round(ti.GetStart())!=st or round(ti.GetEnd())!=end:
            raise RuntimeError("Timeline frame mismatch at %s expected %d..%d got %s..%s"%(row["shot_id"],st,end,ti.GetStart(),ti.GetEnd()))
        contents=(root/row["editable_setting"]).read_text("utf8")
        contents=contents.replace("__PACK_ROOT__",str(root).replace("\\","/"))
        comp_path=root/"Resolved_Comps"/(row["shot_id"]+".setting")
        comp_path.parent.mkdir(parents=True,exist_ok=True)
        comp_path.write_text(contents,encoding="utf8")
        fc=ti.ImportFusionComp(str(comp_path))
        if not fc:raise RuntimeError("Resolve Fusion import rejected "+row["shot_id"]+" (no PASS recorded)")
        result.append({"shot":row["shot_id"],"in":st,"out":end,"fusion_imported":True})
    if all_shots:
        item=pool.AppendToTimeline([{"mediaPoolItem":wav,"startFrame":0,"endFrame":20200,
                                  "recordFrame":0,"mediaType":2,"trackIndex":1}])
        if not item:raise RuntimeError("Narration A1 import failed")
    report={"status":"RESOLVE_COMPS_IMPORTED__REAL_TIME_VISUAL_AND_AUDITORY_QC_PENDING",
            "project_name":name,"shots_imported":len(result),"expected_last_frame":shots[-1]["end_frame"],
            "result":result,"audio_added":all_shots,"audio_sha256":audio_hash}
    (root/"RESOLVE_IMPORT_REPORT.json").write_text(json.dumps(report,indent=2)+"\n")
    # Export only when every clip and Fusion comp has been imported and placement passed.
    pm.SaveProject()
    if not pm.ExportProject(name,str(root/(name+".drp"))):
        report["drp_export"]="FAILED"
    else:report["drp_export"]="OK"
    (root/"RESOLVE_IMPORT_REPORT.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({k:v for k,v in report.items() if k!="result"},indent=2))
if __name__=="__main__":
    arg=argparse.ArgumentParser()
    arg.add_argument("--pack",required=True)
    arg.add_argument("--master",required=True)
    arg.add_argument("--all",action="store_true")
    arg.add_argument("--canary",type=int,default=8)
    options=arg.parse_args()
    run(options.pack,options.master,options.canary,options.all)
