"""Prepare/validate VIDEO004 prompts. No generation API. Default read-only; --patch prints patches."""
from __future__ import annotations
import argparse, csv, difflib, hashlib, io, json, sys
from pathlib import Path
from collections import Counter
BASE=Path(__file__).resolve().parent
ROOT=BASE.parent.parent
AUTHOR="12_PROMPT_PACKAGE_V6.json"
ADAPT="12_MONTAGE_ADAPTATION_V6.json"
def read_json(name):
    return json.loads((BASE/name).read_text(encoding="utf-8-sig"))
def csv_rows(name):
    with (BASE/name).open(encoding="utf-8-sig",newline="") as s:
        return list(csv.DictReader(s))
def sha_text(path):
    return hashlib.sha256(path.read_text(encoding="utf-8").encode()).hexdigest()
def csv_text(rows):
    out=io.StringIO(newline="")
    writer=csv.DictWriter(out,fieldnames=list(rows[0]),lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue()
def json_text(value):
    return json.dumps(value,ensure_ascii=False,indent=2)+"\n"
def build():
    author=read_json(AUTHOR)
    inventory=read_json(author["inventory_source"])
    film=read_json(author["film_map"])
    adapt=read_json(ADAPT)
    for receipt_name in ("12_GENERATION_COUNT_V4.json","12_FILM_VALIDATION_V5.json"):
        for name,expected in read_json(receipt_name)["input_sha256"].items():
            assert sha_text(BASE/name)==expected, f"Protected input changed: {name}"
    canon=ROOT/"00_FOUNDATION/EDITING_CANON.md"
    # The source and initial restoration were byte-identical. Validate canonical
    # UTF-8/LF content here so Git autocrlf checkouts do not create a false failure.
    assert sha_text(canon)==author["canon_restore"]["raw_sha256"], "Canon content differs from locked original"
    refs={r["reference_id"]:r for r in author["references"]}
    assert len(refs)==6
    for ref in refs.values():
        local=ROOT/ref["repo_path"]
        assert local.is_file(), f"Missing reference {local}"
        assert local.stat().st_size==ref["bytes"]
        assert hashlib.sha256(local.read_bytes()).hexdigest()==ref["sha256"]
        assert ref["role"]=="STYLE_ONLY" and ref["tool_role"]=="image"
        assert ref["url"].startswith("https://raw.githubusercontent.com/reverendstanislav-bot/Youtube-3/ba242a03")
        assert ref["url"].endswith(ref["repo_path"])
        assert ref["url_check"]=="FETCHED_BYTES_SHA256_MATCH_2026_10_11"
    assets={a["id"]:a for a in inventory["assets"]}
    bindings={b["asset_id"]:b for b in author["bindings"]}
    layouts={a["asset_id"]:a for a in adapt["assets"]}
    assert len(assets)==len(bindings)==len(layouts)==60
    assert set(assets)==set(bindings)==set(layouts)
    original_places=film["placements"]
    adapted_places=adapt["placements"]
    assert len(original_places)==len(adapted_places)==84
    for old,new in zip(original_places,adapted_places):
        for key in ("placement_id","asset_id","start_frame","end_frame","treatment"):
            assert old[key]==new[key], f"Placement drift: {old['placement_id']} {key}"
    params=author["request_parameters"]
    assert params["model"]==author["model"]["id"]=="gpt_image_2"
    assert params["aspect_ratio"] in author["model"]["aspect_ratios"]
    assert params["count"]==1
    for key in ("quality","resolution"):
        spec=next(p for p in author["model"]["parameters"] if p["name"]==key)
        assert params[key] in spec["options"]
    assert author["model"]["medias"][0]["roles"]==["image"]
    assert params=={"model":"gpt_image_2","resolution":"1k","quality":"low","aspect_ratio":"16:9","count":1}
    assert author["cost_preflight"]["submitted_jobs"]==0
    assert not author["cost_preflight"]["spend_authorized"]
    assert author["cost_preflight"]["one_attempt_each_estimated_credits"]==60*author["cost_preflight"]["cost_per_image_credits"]
    actual_assets={r["asset_id"]:r for r in csv_rows("12_GENERATION_ASSET_MANIFEST_V4.csv")}
    sources={r["source_id"]:r for r in csv_rows("SOURCE_INDEX.csv")}
    requests=[]
    reference_rows=[]
    contexts=[]
    human=["# VIDEO004 - 60 final Higgsfield prompts V6","",
        "Prepared text/reference packet only. No job is authorized or submitted. V4 owns the exact 60-slot inventory; V5 owns 84 placements; V6 prepares their requests.","",
        "Model: Higgsfield GPT Image 2 / 1k / low / 16:9 / count1; two STYLE_ONLY image-role inputs per request. Catalogue checked 2026-10-11; backend two-reference ingestion and generation output NOT TESTED.","",
        "Each image has two STYLE_ONLY inputs. Actual bytes and pinned URLs were verified; reference content is not Valve evidence. Factual URLs below are context records, not attached image pixels.","",
        "Readiness: PROMPTS_AND_LOCAL_REFERENCE_BINDINGS_PREPARED; AUDIO_FINAL_LOCK_AND_SPEND_APPROVAL_REQUIRED. Backend imports, accepted pixels, vertical adaptation and render QC are NOT_PERFORMED.","",
        "Live no-media estimate: 0.5 exact credit/image; 60 first attempts = 30.0 credits base. Full two-reference request price and image fidelity not validated. NOT AN AUTHORIZATION. No imports, jobs, retries, Shorts CTA or thumbnails.","",
        "The JSONL contains structured generate_image arguments for later authorized execution; it is not an executor. This script has no job submission path.","","## Every prompt",""]
    for aid,asset in assets.items():
        b=bindings[aid]
        assert b["primary"]!=b["secondary"]
        primary,secondary=refs[b["primary"]],refs[b["secondary"]]
        layout=layouts[aid]
        row=actual_assets[aid]
        sids=[s for s in row["source_ids"].split(";") if s]
        assert bool(sids)==(asset["type"]!="ENDSCREEN")
        for sid in sids:
            assert sid in sources and sources[sid]["url"].startswith("https://")
        label=row["mandatory_label"]
        assert layout["protected_content_en"]["exact_visible_text"]==asset["visible_text"]
        assert layout["protected_content_en"]["mandatory_provenance_label"]==label
        copy=list(asset["visible_text"])+([label] if label else [])
        assert (asset["type"]=="ENDSCREEN" and not label) or label==("RECREATION / NOT AN ORIGINAL DOCUMENT" if asset["type"]=="RECREATED_DOCUMENT" else "ILLUSTRATION")
        legal_context=b["factual_context_override"] or "Preserve the attributed, dated, scoped editorial meaning in the locked display copy and scene direction. No stronger claim, invented procedural outcome or extra numerical inference."
        factual=[{"source_id":sid,"url":sources[sid]["url"],"title":sources[sid]["title"],"source_type":sources[sid]["source_type"],"authority":sources[sid]["primary_or_secondary"],"scope_notes":sources[sid]["notes"]} for sid in sids]
        contexts.append({"asset_id":aid,"claim_ids":row["claim_ids"].split(";") if row["claim_ids"] else [],"source_ids":sids,"factual_context_mode":"TEXT_CONTEXT_NOT_IMAGE_ATTACHMENT_NOT_CURRENT_DOCKET_REFRESH","sources":factual,"bounded_interpretation":legal_context,"allowed_editorial_copy":asset["visible_text"],"provenance_label":label,"original_document_claim":False})
        parts=[
            f"Primary request: Generate one finished {aid} English-language full-frame documentary illustration. New composition, not an edit of either style image.",
            f"Input image 1: {primary['reference_id']} STYLE_ONLY. {primary['purpose']}",
            f"Input image 2: {secondary['reference_id']} STYLE_ONLY. {secondary['purpose']}",
            "Reference invariants: borrow only typography feel, hierarchy, tactile materials, controlled light and polish. Never copy any reference headline, company logo, face, source text, case fact, subject, layout or safe margin.",
            "Scene and subject: "+asset["direction"],
            "Composition for the edit: "+layout["layout_for_edit_en"],
            "Protected readable meaning: "+layout["protected_content_en"]["constraints_en"],
            "Layer and motion contract: "+layout["layer_policy_en"],
            "Potential attention target: "+layout["motion_target_en"],
            "Style: premium investigative editorial composition; charcoal #1F1F1F / deep black #0B0B0B / paper white #EDEDED; restrained semantic red #D32222, rare warm material gold #B69B68. Directional warm light, controlled cool shadows, matte tactile depth and fine grain. Crisp Bebas Neue-like condensed headline, Inter-like supporting copy. Do not add a decorative desk or a separate banner just to imitate the references.",
            "Text inside this generated image, VERBATIM and no other lettering:\n"+"\n".join(json.dumps(s,ensure_ascii=False) for s in copy),
            "Text hierarchy: every attribution, date, conditional and limitation remains readable with its proposition. Wrap long locked strings into legible lines without changing characters or wording. No tiny caveats, letter distortion, faux body copy or extra prose.",
            "Factual boundary (context only, not additional on-image text): "+legal_context]
        for key,value in inventory["common_direction"].items():
            # Historical V4 inventory remains immutable for source/beat hashes. Override only
            # the stale 4K sizing requirement for NEW V6 prepared requests.
            if key=="format":
                value="One complete generated 16:9 still per asset under Higgsfield gpt_image_2 / 1k / low. Keep text/logos/source labels readable at native 1k. Do not request 4K, fake 1080p/4K native resolution, or invent upscale detail. Any 1920x1080 edit delivery requires later separately QC-verified scaling. Exact English text must not be simplified or omitted to fit: REJECT if illegible."
            parts.append("Locked "+key+" requirement: "+value)
        parts.append("GPT Image 2 / 1k / low preflight: keep the already-locked copy exact; prioritize clear line breaks and readable attribution/caveats above decorative detail. If too much text to fit legibly at 1k, treat as a QC HOLD/REJECT, never remove words or silently shrink essential facts. Only reference images 1 and 2 are style sources.")
        if asset["type"]=="RECREATED_DOCUMENT":
            parts.append("Reconstruction: visibly editorial paraphrase only. The mandatory recreation label must be legible and integral. No original-looking page header, docket seal, signature, fake quote marks, fake body text or fabricated screenshot; do not re-create the authentic paper shown in style references.")
        if aid=="GF060":
            parts.append("Endscreen exception: no ILLUSTRATION label or extra copy. Translate the 1920x1080 design-space safe boxes to the actual native 1k 16:9 output by relative proportions only; DO NOT request 3840x2160 or claim exact pixel-safe geometry. Both native YouTube overlay areas must stay empty and require post-generation Studio-safe-area pixel QC. Do not inherit subjects, frames, logos or text from style images.")
        parts.append("Deliver one opaque 16:9 still with all permitted lettering already rendered. No storyboard, collage sheet, split deliverables, narration captions, black caption strip, motion blur, watermarks, random arrows, gavels or scales of justice. No generation of variations for later reuse.")
        prompt="\n\n".join(parts)
        for text in copy:
            assert json.dumps(text,ensure_ascii=False) in prompt
        args={"context":"Prepare one editorial documentary illustration with verified style references.","params":dict(params,prompt=prompt,medias=[{"role":"image","value":primary["url"]},{"role":"image","value":secondary["url"]}])}
        requests.append({"asset_id":aid,"status":"PREPARED_NOT_SUBMITTED","spend_authorized":False,"reference_ids":[b["primary"],b["secondary"]],"factual_context_source_ids":sids,"generate_image_arguments":args,"execution_gates":["GENUINE_AUDIO_ACCEPTANCE","FINAL_TIMELINE_LOCK","FRESH_EXACT_REQUEST_QUOTE","EXPLICIT_SPEND_APPROVAL"],"original_document_claim":False})
        reference_rows.append({"asset_id":aid,"primary_reference_id":primary["reference_id"],"primary_url":primary["url"],"primary_repo_path":primary["repo_path"],"primary_sha256":primary["sha256"],"secondary_reference_id":secondary["reference_id"],"secondary_url":secondary["url"],"secondary_repo_path":secondary["repo_path"],"secondary_sha256":secondary["sha256"],"input_role":"image","purpose":"STYLE_ONLY","asset_specific_purpose":b["purpose"],"factual_source_ids":";".join(sids),"factual_source_urls":";".join(sources[sid]["url"] for sid in sids),"attachment_state":"LOCAL_AND_HTTPS_BYTES_VERIFIED_NOT_IMPORTED_TO_HIGGSFIELD"})
        human += [f"### {aid} - {asset['type']}","",f"Image 1: [{primary['reference_id']}]({primary['url']}); image 2: [{secondary['reference_id']}]({secondary['url']}). Both STYLE_ONLY.","","Factual context: "+("; ".join(f"[{s['source_id']}]({s['url']})" for s in factual) or "None; native-overlay background.")+".","",chr(96)*3+"text",prompt,chr(96)*3,""]
    outputs={"12_HIGGSFIELD_REQUESTS_V6.jsonl":"".join(json.dumps(r,ensure_ascii=False,separators=(",",":"))+"\n" for r in requests),"12_HIGGSFIELD_PROMPTS_V6.md":"\n".join(human).rstrip()+"\n","12_REFERENCE_BINDINGS_V6.csv":csv_text(reference_rows),"12_FACTUAL_CONTEXT_V6.json":json_text(contexts)}
    report={"status":"STRUCTURAL_PROMPT_REFERENCE_MONTAGE_PASS_NOT_GENERATION_OR_MEDIA_QC","unique_longform_prompts":60,"unique_existing_style_files":6,"style_bindings":len(reference_rows),"image_inputs_per_request":2,"factual_context_rows":len(contexts),"story_frames_with_source_links":sum(bool(r["source_ids"]) for r in contexts),"document_recreations":sum(a["type"]=="RECREATED_DOCUMENT" for a in assets.values()),"placements":84,"placement_treatments":dict(Counter(p["treatment"] for p in adapted_places)),"runtime_sec":828,"canonical_voice_and_scene_inputs_unchanged":True,"paid_jobs":0,"new_raster_assets":0,"higgsfield_imports_performed":0,"spend_authorized":False,"stage_advanced":False,"input_sha256_scheme":"UTF8_LF_NORMALIZED","input_sha256":{n:sha_text(BASE/n) for n in (AUTHOR,ADAPT,"12_visual-style_V6.md","12_GENERATION_PLAN_V4.json","12_FILM_STRUCTURE_V5.json","SOURCE_INDEX.csv")},"editing_canon_sha256":sha_text(canon),"output_sha256":{n:hashlib.sha256(s.encode()).hexdigest() for n,s in outputs.items()},"remaining_gates":["AUDITORY_QC","FINAL_TIMELINE","ACTUAL_GENERATION_SPEND_APPROVAL","ACTUAL_IMAGE_QC","VERTICAL_AND_NATIVE_ENDSCREEN_QC","FULL_EDIT_AV_QC","STAGE16_REFRESH","RELEASE"]}
    outputs["12_PROMPT_VALIDATION_V6.json"]=json_text(report)
    return outputs
def emit_patch(name,content,max_lines):
    path=BASE/name
    old=path.read_text(encoding="utf-8") if path.exists() else ""
    if old==content:
        print("*** Begin Patch\n*** End Patch")
        return
    if max_lines and content.startswith(old):
        new=old+"".join(content[len(old):].splitlines(keepends=True)[:max_lines])
    else:
        new=content
    print("*** Begin Patch")
    if not path.exists():
        print(f"*** Add File: {path.as_posix()}")
        for line in new.splitlines():
            print("+"+line)
    else:
        print(f"*** Update File: {path.as_posix()}")
        context=90 if name.endswith(".md") else (100 if name=="12_FACTUAL_CONTEXT_V6.json" else 3)
        for line in list(difflib.unified_diff(old.splitlines(),new.splitlines(),lineterm="",n=context))[2:]:
            print("@@" if line.startswith("@@") else line)
    print("*** End Patch")
def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser=argparse.ArgumentParser()
    parser.add_argument("--patch",action="store_true")
    parser.add_argument("--write-derived",action="store_true",help="Write only derived V6 files. NEVER submits, imports or calls a paid API.")
    parser.add_argument("--name",choices=["12_HIGGSFIELD_REQUESTS_V6.jsonl","12_HIGGSFIELD_PROMPTS_V6.md","12_REFERENCE_BINDINGS_V6.csv","12_FACTUAL_CONTEXT_V6.json","12_PROMPT_VALIDATION_V6.json"])
    parser.add_argument("--max-lines",type=int,default=0)
    args=parser.parse_args()
    outputs=build()
    if args.write_derived:
        assert not args.patch, "Choose exactly one mode"
        for name,content in outputs.items():
            (BASE/name).write_text(content,encoding="utf-8",newline="\n")
        print(json.dumps({"status":"WRITTEN_NO_API_CALLS","files":list(outputs),"images":60,"reference_roles":2,"generation_jobs":0},indent=2))
    elif args.patch:
        assert args.name, "--name required: patch one derived file at a time"
        emit_patch(args.name,outputs[args.name],args.max_lines)
    else:
        for name,content in outputs.items():
            assert (BASE/name).read_text(encoding="utf-8")==content, f"Missing/stale {name}"
        print(outputs["12_PROMPT_VALIDATION_V6.json"])
if __name__=="__main__":
    main()
