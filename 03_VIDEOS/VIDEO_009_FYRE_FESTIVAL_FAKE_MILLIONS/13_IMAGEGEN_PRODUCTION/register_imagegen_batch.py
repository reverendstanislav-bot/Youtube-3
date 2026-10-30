from pathlib import Path
import csv, hashlib, json, shutil, sys
import re
from PIL import Image

ROOT = Path(r'C:\Users\KK\VIDEO009_VISUAL_PRODUCTION')
EP = Path(r'C:\Users\KK\Youtube-3-video009-visual-v2\03_VIDEOS\VIDEO_009_FYRE_FESTIVAL_FAKE_MILLIONS')
OUT = EP/'13_IMAGEGEN_PRODUCTION'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
batch = Path(sys.argv[1])
rows = json.loads(batch.read_text(encoding='utf-8'))
(OUT/'OUTPUTS').mkdir(exist_ok=True)
(OUT/'RECEIPTS').mkdir(exist_ok=True)
for row in rows:
    aid, version = row['asset_id'], row['version']
    src = Path(row['source_file'])
    assert src.is_file(), src
    name = f'{aid}_IMAGEGEN_V{version}.png'
    local = ROOT/'IMAGEGEN/OUTPUTS'/name
    repo = OUT/'OUTPUTS'/name
    for dest in [local, repo]:
        if dest.exists(): assert sha(dest)==sha(src), str(dest)
        else: shutil.copy2(src,dest)
    with Image.open(repo) as im:
        im.verify()
    with Image.open(repo) as im:
        width,height=im.size
    assert width>=1500 and abs(width/height-16/9)<0.01
    row.update(local_file=str(local),repo_file='13_IMAGEGEN_PRODUCTION/OUTPUTS/'+name,sha256=sha(src),width=width,height=height,provider='built-in image_gen.imagegen',model='NOT_EXPOSED',numeric_cost='NOT_EXPOSED_NO_ZERO_COST_CLAIM')
    sidecar=EP/'12_VISUAL_V2/REFERENCES'/f'{aid}.json'
    row['fact_reference_sidecar']='12_VISUAL_V2/REFERENCES/'+sidecar.name
    row['fact_reference_sha256']=sha(sidecar)
    (OUT/'RECEIPTS'/f'{aid}_V{version}.json').write_text(json.dumps(row,ensure_ascii=False,indent=2),encoding='utf-8')
if '--save-only' in sys.argv:
    print(json.dumps({'durably_saved':len(rows),'shared_registries_updated':False}))
    sys.exit(0)
shutil.copy2(ROOT/'IMAGEGEN/OWNER_STYLE_APPROVAL.json',OUT/'OWNER_STYLE_APPROVAL.json')
queue=json.loads((OUT/'IMAGEGEN_QUEUE.json').read_text(encoding='utf-8'))
latest={}
for path in sorted((OUT/'RECEIPTS').glob('GF*_V*.json')):
    r=json.loads(path.read_text(encoding='utf-8'))
    if r['version']>=latest.get(r['asset_id'],{}).get('version',0):latest[r['asset_id']]=r
for r in queue:
    aid=r['asset_id']
    if aid=='GF003':
        r.update(status='OWNER_APPROVED_STYLE_BASELINE',selected_file='13_IMAGEGEN_PRODUCTION/GF003_IMAGEGEN_V2_STYLE_PROOF.png')
    elif aid in latest:
        s=latest[aid];r.update(status='GENERATED_LEAD_REVIEW_PENDING',selected_file=s['repo_file'],sha256=s['sha256'])
    else:r['status']='QUEUED_OWNER_APPROVED_STYLE'
(OUT/'IMAGEGEN_QUEUE.json').write_text(json.dumps(queue,ensure_ascii=False,indent=2),encoding='utf-8')
review_file=ROOT/'IMAGEGEN/LEAD_VISUAL_QC.json'
reviews=json.loads(review_file.read_text(encoding='utf-8')) if review_file.exists() else {'reviews':{}}
if review_file.exists():shutil.copy2(review_file,OUT/'LEAD_VISUAL_QC.json')
for reg in [OUT/'QC_REGISTRY.csv',EP/'ASSET_MANIFEST.csv']:
    with reg.open(encoding='utf-8-sig',newline='') as f:
        reader=csv.DictReader(f);fields=reader.fieldnames;data=list(reader)
    for r in data:
        aid=r['asset_id']
        if aid=='GF003':
            p=OUT/'GF003_IMAGEGEN_V2_STYLE_PROOF.png'
            r.update(type='IMAGEGEN_EDITORIAL_GRAPHIC',download_status='GENERATED_OWNER_STYLE_APPROVED',local_asset_path='13_IMAGEGEN_PRODUCTION/'+p.name,sha256=sha(p),hash_kind='ACTUAL_FILE',qc='HOLD_INDEPENDENT_RELEASE_QC',usage_note='Owner approved GF003 V2 as production style baseline. Original editorial metaphor, not an authentic device. No baked colored outlines. Final assembly/release QC pending.')
        elif aid in latest:
            s=latest[aid]
            r.update(type='IMAGEGEN_EDITORIAL_GRAPHIC',download_status='GENERATED',local_asset_path=s['repo_file'],sha256=s['sha256'],hash_kind='ACTUAL_FILE',qc='HOLD_LEAD_VISUAL_REVIEW',usage_note='Generated through built-in ImageGen using approved VIDEO005/GF003 references. Original editorial graphic, not authentic evidence. Receipt preserves prompt and facts. Native size '+str(s['width'])+'x'+str(s['height'])+'; final Fusion placement and release QC pending.')
    with reg.open('w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader();writer.writerows(data)
total=len(set(latest)|{'GF003'})
submissions=4+len(list((OUT/'RECEIPTS').glob('GF*_V*.json')))
for r in queue:
    aid=r['asset_id'];q=reviews['reviews'].get(aid,{})
    if aid in latest and q.get('version')==latest[aid]['version']:
        r['status']='GENERATED_'+q['result']
(OUT/'IMAGEGEN_QUEUE.json').write_text(json.dumps(queue,ensure_ascii=False,indent=2),encoding='utf-8')
summary={'requested_asset_identities':52,'generated_asset_identities':total,'remaining_asset_identities':52-total,'submissions_total':submissions,'owner_rejected_initial_style_images':3,'owner_approved_style_baseline':'GF003_V2','owner_asset_approval_count':1,'independent_release_qc':'PENDING','cost':'NOT_EXPOSED_NO_ZERO_COST_CLAIM','audio_status_queried':False}
(OUT/'PRODUCTION_STATUS.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
(OUT/'OWNER_ROUTE_OVERRIDE.md').write_text(f'''# Owner-approved ImageGen production

Owner explicitly replaced the SVG route with built-in ImageGen and approved GF003 V2: "Да, продолжай в этой подаче". Direct approved VIDEO005 master frames and GF003 V2 define the visual language. Compositions must vary by subject; this is not permission to repeat the counter for every scene.

Current inventory: {total}/52 asset identities have real PNGs; {submissions} total submissions include three rejected initial-style images. Per-image lead reviews and correction holds are in LEAD_VISUAL_QC.json. A generated file is not independent/release PASS. Only GF003 V2 has individual owner style approval. Underlying model and numeric cost are not exposed by this tool; no zero-cost ImageGen claim is made.

No baked yellow/red outlines, source banners or motion. Official documents are never regenerated; the14 genuine source crops remain unchanged. ImageGen illustrations are editorial explanatory visuals, not authentic historical evidence. Later Fusion motion/compositing and montage have not been performed or authorized here. The local Harrison audio queue remains unmonitored.
''',encoding='utf-8')
(EP/'STATE.md').write_text(f'''# VIDEO009 - ImageGen production in owner-approved style

Current stage:13_VISUAL_ASSET_PRODUCTION. Owner approved GF003 V2 on2026-10-30 and authorized continuation in that presentation. Actual PNG inventory: {total}/52 asset identities; total ImageGen submissions: {submissions}, including3 rejected initial-style attempts. See13_IMAGEGEN_PRODUCTION/IMAGEGEN_QUEUE.json, OUTPUTS, RECEIPTS and LEAD_VISUAL_QC.json. Correction holds and pending reviews remain explicit. No full52-frame or independent release PASS is claimed.

No SVG production, no baked yellow/red outlines, no fake official source documents. Genuine14 document crops and all locked script/voice text remain unchanged. Native ImageGen dimensions are recorded per receipt; final1080p Fusion placement and visual review remain for later authorized assembly.

Five-part local Harrison queue was previously launched and remains deliberately unmonitored. No audio completion, listening PASS, Stage10 assembly or montage is claimed. Stock/context holds and independent review remain open.
''',encoding='utf-8')
p=EP/'manifest.yaml';text=p.read_text(encoding='utf-8')
text=text.replace('IN_PROGRESS_IMAGEGEN_STYLE_HOLD_14DOC_PASS_38STOCK_PASS_36HOLD_2REJECT','IN_PROGRESS_OWNER_STYLE_APPROVED_IMAGEGEN_BATCHES_QC_PENDING_14DOC_PASS')
text=re.sub(r'(?m)^  style_approval: .*$', '  style_approval: "OWNER_APPROVED_GF003_V2_20261030"',text)
text=re.sub(r'(?m)^  submissions: \d+$',f'  submissions: {submissions}',text)
text=re.sub(r'(?m)^  approved_production_images: \d+$','  approved_production_images: 1',text)
text=re.sub(r'(?m)^(\s*next_action:) .*$',r'\1 "Continue authorized ImageGen assets in approved GF003 V2 style and correct QC defects. Leave Voicebox unmonitored. No montage."',text)
p.write_text(text,encoding='utf-8')
direction_file=ROOT/'IMAGEGEN/STYLE_DIRECTION_VIDEO008.json'
if direction_file.exists():
    shutil.copy2(direction_file,OUT/'STYLE_DIRECTION_VIDEO008.json')
    natural={aid:r for aid,r in latest.items() if r.get('current_style_reassessment')=='PASS_VIDEO008_NATURAL_BACKGROUND' or any('VIDEO008_PRODUCTION' in ref for ref in r.get('input',{}).get('referenced_image_paths',[]))}
    for r in queue:
        aid=r['asset_id']
        r['status']='GENERATED_VIDEO008_DIRECTION_REVIEW_PENDING' if aid in natural else ('HOLD_STYLE_REVISION_VIDEO008' if aid in latest or aid=='GF003' else 'QUEUED_VIDEO008_DIRECTION')
        if aid in natural:r.update(selected_file=natural[aid]['repo_file'],sha256=natural[aid]['sha256'])
    (OUT/'IMAGEGEN_QUEUE.json').write_text(json.dumps(queue,ensure_ascii=False,indent=2),encoding='utf-8')
    for reg in [OUT/'QC_REGISTRY.csv',EP/'ASSET_MANIFEST.csv']:
        with reg.open(encoding='utf-8-sig',newline='') as f:
            reader=csv.DictReader(f);fields=reader.fieldnames;data=list(reader)
        for r in data:
            aid=r['asset_id']
            if not aid.startswith('GF'):continue
            if aid in natural:
                s=natural[aid]
                r.update(type='IMAGEGEN_EDITORIAL_ANALYSIS',download_status='GENERATED_VIDEO008_DIRECTION',local_asset_path=s['repo_file'],sha256=s['sha256'],hash_kind='ACTUAL_FILE')
                r['qc']='HOLD_VIDEO008_STYLE_REVIEW'
                r['usage_note']='New owner-requested natural VIDEO008 direction. Actual PNG preserved; exact prompt/style references in receipt. Not an authentic source document. Lead and independent/owner review remain separate.'
            elif aid in latest or aid=='GF003':
                r['qc']='HOLD_OWNER_STYLE_REVISION'
                r['download_status']='AUDIT_ONLY_NOT_PRODUCTION_SELECTED'
                r['usage_note']='Owner rejected the artificial direction and requested VIDEO008. Preserve prior output as audit only; do not use in production without reassessment.'
                if aid in latest:r['local_asset_path']=latest[aid]['local_file']
        with reg.open('w',encoding='utf-8',newline='') as f:
            writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader();writer.writerows(data)
    summary.update(current_style='OWNER_REQUEST_VIDEO008_NATURAL_DOCUMENTARY',current_style_png_count=len(natural),previous_direction_asset_approval_is_historical=True,owner_asset_approval_count=0)
    approved_file=ROOT/'IMAGEGEN/OWNER_STYLE_APPROVAL_VIDEO008.json'
    if approved_file.exists():
        approved=json.loads(approved_file.read_text(encoding='utf-8'))
        shutil.copy2(approved_file,OUT/'OWNER_STYLE_APPROVAL_VIDEO008.json')
        summary.update(owner_approved_style_baseline='VIDEO008_NATURAL_DOCUMENTARY_FIVE_ACCEPTED_FRAMES',owner_asset_approval_count=len(approved['approved_candidates']))
    (OUT/'PRODUCTION_STATUS.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    (OUT/'.gitignore').write_text('OUTPUTS/*.png\n'+''.join('!OUTPUTS/'+Path(r['repo_file']).name+'\n' for r in natural.values()),encoding='utf-8')
    (EP/'STATE.md').write_text(f'''# VIDEO009 - Owner correction: natural VIDEO008 documentary style

Current stage:13_VISUAL_ASSET_PRODUCTION. Latest owner instruction2026-10-30: the mechanical/signboard direction is too AI; match VIDEO008. This supersedes the earlier GF003 approval as the production direction. Prior versions are preserved for audit, not silently accepted for use.

Actual PNGs exist for{total}/52 identities. Current VIDEO008-style candidates:{len(natural)}/52; per-image fact/style/owner/independent QC remain separate. See13_IMAGEGEN_PRODUCTION/STYLE_DIRECTION_VIDEO008.json, OUTPUTS and RECEIPTS. No completed52-frame package or release PASS is claimed. Built-in ImageGen model/numeric cost are not exposed;{submissions} submissions recorded including rejected/superseded versions.

Use natural paper/files/stationery and neutral light. No rusty mechanisms, giant signs, baked red/yellow emphasis, source banners or generated official evidence. Genuine14 source crops and locked narration remain unchanged. Official passages stay authentic and separate for later authorized Fusion compositing.

Previously launched Harrison queue remains deliberately unmonitored. Audio completion/listening/Stage10 assembly are not claimed. No montage or Resolve work has been started. Stock/context and independent review holds remain open.
''',encoding='utf-8')
    (OUT/'OWNER_ROUTE_OVERRIDE.md').write_text('''# Latest owner direction: VIDEO008

The owner rejected the artificial mechanism/signboard treatment and requested the natural documentary presentation used in VIDEO008. Actual VIDEO008 scene066 and034 frames were inspected and used as direct style references. Earlier GF003 approval is historical; it does not override the newer correction. All earlier versions remain audit evidence and are not silently selected for production.

ImageGen remains the explicitly requested provider. No SVG substitute. Paper-based illustrations are clearly original editorial analysis, never authentic company or official government documents. The14 genuine source crops are unchanged. No baked red/yellow emphasis, source banners or motion; later Fusion composition/montage remains separate. Costs/model are not exposed by the built-in tool. See current PRODUCTION_STATUS.json and per-image receipts; no full-package PASS is claimed.
''',encoding='utf-8')
    p=EP/'manifest.yaml';text=p.read_text(encoding='utf-8')
    text=re.sub(r'(?m)^  style_approval: .*$', '  style_approval: "LATEST_OWNER_REQUEST_VIDEO008_DIRECTION_ASSET_REVIEW_PENDING"',text)
    text=re.sub(r'(?m)^  approved_production_images: \d+$','  approved_production_images: 0',text)
    if approved_file.exists():
        text=text.replace('LATEST_OWNER_REQUEST_VIDEO008_DIRECTION_ASSET_REVIEW_PENDING','OWNER_APPROVED_VIDEO008_NATURAL_DIRECTION_FIVE_ACCEPTED_FRAMES')
        text=text.replace('  approved_production_images: 0','  approved_production_images: 5')
    text=text.replace('IN_PROGRESS_OWNER_STYLE_APPROVED_IMAGEGEN_BATCHES_QC_PENDING_14DOC_PASS','IN_PROGRESS_OWNER_VIDEO008_STYLE_CORRECTION_QC_PENDING_14DOC_PASS')
    text=re.sub(r'(?m)^(\s*next_action:) .*$',r'\1 "Match actual VIDEO008 natural documentary style using inspected direct frames. No mechanical signboards. Leave Voicebox unmonitored. No montage."',text)
    p.write_text(text,encoding='utf-8')
print(json.dumps({'saved_in_batch':len(rows),'generated_asset_identities':total,'remaining_without_any_png':52-total,'actual_png_hashes_verified':True,'audio_status_queried':False}))
