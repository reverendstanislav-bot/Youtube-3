from pathlib import Path
import json,zipfile,hashlib
ROOT=Path(__file__).resolve().parent;PROD=ROOT.parent;D=PROD/'DELIVERY'
rows=json.loads((ROOT/'CLEAN_V5_MANIFEST.json').read_text())
files=[ROOT/n for n in ('build_clean_v5.py','build_fusion.py','CLEAN_V5_MANIFEST.json','FUSION_BUILD_MANIFEST.json','verify_delivery_v5_final.py','CLEAN_SOURCE_PLATES_V5.json','LEGACY_SOURCE_REPLACEMENT_V5.json','replace_legacy_files_with_backup.py')]
files+=[D/'VIDEO008_V6_SMALL_ENDSCREEN.drp']
files+=list((PROD/'ENDSCREEN').glob('*'))
files+=list((ROOT/'COMPS_V5_CLEAN').glob('*.comp'))
files+=[Path(r['photo']) for r in rows]
pack=PROD/'VIDEO008_FINAL_VISUAL_PACK'
files+=[pack/'RESOLVE_PLATES'/(r['scene_id']+'_PLATE_25FPS.mp4') for r in rows]
files+=[pack/'RESOLVE_PLATES_V5_CLEAN'/(sid+'_CLEAN_SOURCE_V5.mp4') for sid in ('SC064','SC071','SC076')]
files+=[pack/'IMAGEGEN_REPLACEMENTS'/n for n in ('CLEAN_V3_PROMPTS.json','CLEAN_V3_GENERATION_RECEIPT.json')]
out=D/'VIDEO008_V6_SMALL_ENDSCREEN_EDIT_ASSETS.zip';manifest=[]
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=1) as z:
    for f in dict.fromkeys(files):
        assert f.is_file(),str(f)
        rel=f.relative_to(PROD).as_posix();z.write(f,rel)
        manifest.append({'path':rel,'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
    z.writestr('MANIFEST_SHA256.json',json.dumps(manifest,indent=2))
    z.writestr('README.txt','VIDEO008 V6 small endscreen. Current timeline VIDEO008_V6_SMALL_ENDSCREEN_25FPS. Last20seconds use the existing owner-approved WHAT IT COST artwork with720x405video window and260pxcircle; body structure and locked audio preserved. All45 unwanted overlay groups removed. No service labels/floating source strips/opaque chart backings/duplicate headers. A single transparent revenue chart occupies empty desk space. Four scenes have measured highlights on printed figures. All45 legacy source-card MP4 files are replaced by clean scene bases with matching frames/fps; originals backed up outside this archive. Generated documents remain illustrative, not authentic scans. No new images/TTS generated. This archive includes45 clean source plates plus direct-source files for items70/77/83 and the post-restart DRP. Original stock media and approved WAV remain required. Extract under C:/Users/KK/VIDEO008_PRODUCTION or relink. V4 and earlier V5 precheck exports are rejected/superseded. Use WHAT_IT_COST_VIDEO008_V6_SMALL_ENDSCREEN_1080P25.mp4. The native MOV is silent picture; final MP4 copies its video and encodes the locked WAV at time zero. Continuous AV review and owner acceptance are separate, not claimed.')
with zipfile.ZipFile(out) as z:assert z.testzip() is None
q={'path':str(out),'files':len(manifest),'clean_comps':45,'legacy_source_plates_replaced':45,'distinct_selected_illustrative_bases':len({r['photo'] for r in rows}),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'bytes':out.stat().st_size,'zip_integrity':'PASS','new_generations':0}
(D/'EDIT_ASSETS_QC_V6.json').write_text(json.dumps(q,indent=2),encoding='utf-8');print(json.dumps(q))
