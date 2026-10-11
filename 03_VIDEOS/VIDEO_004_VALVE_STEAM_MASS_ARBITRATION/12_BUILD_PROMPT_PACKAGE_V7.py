"""VIDEO004 V7: deterministic prompt/ref compiler and hard textual preflight. No media calls, imports or spend."""
from __future__ import annotations
import argparse,csv,hashlib,io,json,re
from collections import Counter
from pathlib import Path
BASE=Path(__file__).resolve().parent
ROOT=BASE.parent.parent
V7="12_PASS_REPAIR_RULES_V7.json"
def read_json(path):return json.loads((BASE/path).read_text(encoding="utf-8-sig"))
def csv_rows(path):
    with (BASE/path).open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f))
def sha(data):return hashlib.sha256(data).hexdigest()
def hash_file(p):return sha((BASE/p).read_bytes())
def json_out(obj):return json.dumps(obj,ensure_ascii=False,indent=2)+"\n"
def csv_out(rows):
    f=io.StringIO(newline="")
    writer=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator="\n")
    writer.writeheader();writer.writerows(rows);return f.getvalue()
def main_build():
    rules=read_json(V7)
    inv=read_json("12_GENERATION_PLAN_V4.json")
    author=read_json("12_PROMPT_PACKAGE_V6.json")
    montage=read_json("12_MONTAGE_ADAPTATION_V6.json")
    assert rules["scope"].startswith("60 pre-existing")
    params=rules["output_contract"]
    assert {k:params[k] for k in ("model","resolution","quality","aspect_ratio","count")}=={"model":"gpt_image_2","resolution":"1k","quality":"low","aspect_ratio":"16:9","count":1}
    assert params["style_reference_count"]==2 and params["ready_to_spend"] is False
    assets=inv["assets"]
    assert len(assets)==len(author["bindings"])==len(montage["assets"])==len(rules["frame_specific_policies"])==60
    assert len(montage["placements"])==84
    assert len({a["id"] for a in assets})==60
    refs={r["reference_id"]:r for r in author["references"]}
    assert len(refs)==len(rules["reference_policies"])==6
    bindings={b["asset_id"]:b for b in author["bindings"]}
    layouts={v["asset_id"]:v for v in montage["assets"]}
    manifest={r["asset_id"]:r for r in csv_rows("12_GENERATION_ASSET_MANIFEST_V4.csv")}
    assert len(manifest)==60
    for key,ref in refs.items():
        file=ROOT/ref["repo_path"]
        assert file.is_file(),f"Reference missing: {key}"
        data=file.read_bytes()
        assert sha(data)==ref["sha256"],f"Reference byte hash failure {key}"
        assert len(data)==ref["bytes"] and ref["tool_role"]=="image" and ref["role"]=="STYLE_ONLY"
        assert ref["url"].endswith(ref["repo_path"]) and "ba242a03" in ref["url"]
    reqs=[];rows=[];checks=[];human=["# VIDEO004 — V7 PASS-ORIENTED 60 full-frame generation prompts","",
      "V7 replaces V6 as GENERATION PROMPT authority, NOT as proof of actual generated-image QC. V4 visible_text and legal facts and V5 84 placements remain immutable.","",
      "Each prompt is short, scene-specific, and has an EXACT PRINT-ONLY whitelist before any visual direction. Reference URLs are original byte-verified approved Video002 images; style-only; source images are never evidence for Video004.","",
      "No WHAT IT COST logo except where GF060 endscreen exact copy requires it. No SOURCES footer, ILLUSTRATION stamps, signatures, fake body legal text, legible lettering on props, synthetic UI messages or substituted synonyms.","",
      "Configuration: GPT Image 2 / 1k / low / 16:9; 2 reference images per asset. 0 jobs launched by this compiler; no spending. Images still require manual pixel QC and cannot be guaranteed PASS by prompting.","",
      "## 60 independently constrained frames",""]
    unique_pairs=Counter();types=Counter();exceptions=[]
    source_ix={r["source_id"]:r for r in csv_rows("SOURCE_INDEX.csv")}
    for a in assets:
        aid=a["id"];type_=a["type"];types[type_]+=1
        assert aid in bindings and aid in layouts and aid in manifest and aid in rules["frame_specific_policies"]
        rule=rules["frame_specific_policies"][aid]
        old=bindings[aid]
        pair=rule.get("ref_pair",[old["primary"],old["secondary"]])
        assert len(pair)==2 and pair[0]!=pair[1] and all(k in refs for k in pair),(aid,pair)
        unique_pairs[tuple(pair)]+=1
        if "ref_pair" in rule: exceptions.append(aid)
        for key in pair:assert key in rules["reference_policies"]
        p1,p2=refs[pair[0]],refs[pair[1]]
        context=layouts[aid]["protected_content_en"]
        assert context["exact_visible_text"]==a["visible_text"]
        expected_label="RECREATION / NOT AN ORIGINAL DOCUMENT" if type_=="RECREATED_DOCUMENT" else ""
        assert context["mandatory_provenance_label"]==expected_label,(aid,context["mandatory_provenance_label"])
        locked=list(a["visible_text"])+([expected_label] if expected_label else [])
        assert len(locked)>=1 and len(set(locked))==len(locked),(aid,locked)
        assert all(x and x==x.strip() and "\n" not in x for x in locked)
        sources=[sid for sid in manifest[aid]["source_ids"].split(";") if sid]
        assert all(sid in source_ix for sid in sources)
        if type_=="ENDSCREEN":assert not sources
        else:assert len(sources)>0
        exact="\n".join(f" {i}. {json.dumps(text,ensure_ascii=False)}" for i,text in enumerate(locked,1))
        per1=rules["reference_policies"][pair[0]]
        per2=rules["reference_policies"][pair[1]]
        length=max(len(t) for t in locked)
        qa_tier="DENSE_EXACT_LETTERING_HIGH_RISK" if sum(map(len,locked))>95 or length>49 else ("EXACT_LETTERING_NORMAL_RISK" if max(map(len,locked))>28 else "EXACT_LETTERING_COMPACT")
        # Frontload deterministic visible lettering instructions; avoid describing forbidden words as possible render copy.
        sections=[
          f"{aid} — ONE FINISHED 16:9 ENGLISH INVESTIGATIVE DOCUMENTARY STILL. ONE COMPOSITION ONLY. NO VARIANTS.",
          "PRINT EXACTLY THESE "+str(len(locked))+" ENGLISH STRINGS — THIS IS THE COMPLETE LETTERING WHITELIST (punctuation, plurality, apostrophes, case and dates must be identical):\n"+exact,
          "TYPESETTING CONTRACT: each quoted item must be legible in full and appear ONCE, as a designed editorial text group, in the same numbered order. Different font color/line wraps are OK, but no omission, paraphrase, word substitution, extra caption, object sticker, icon text, label, book spine or date. Print no other legible letters ANYWHERE. Avoid extra lettering on all props. If a phrase is long, split only at SPACE boundaries; preserve its exact characters and its distinct attribution/qualification. Use large condensed ivory text, restrained red for semantic emphasis, simple backing and ample line spacing; NEVER shrink into tiny type.",
          f"SCENE (VISUAL FACTS, NOT ADDITIONAL ON-IMAGE WORDS): {rule['visual_anchor']}",
          "LOCKED NARRATIVE BOUNDARY: "+context["constraints_en"],
          "EDITORIAL COMPOSITION: "+layouts[aid]["layout_for_edit_en"],
          ("This is a DOCUMENT RECREATION, NOT A REAL SOURCE PAGE. Display the exact warning from the whitelist. The document has no readable body paragraphs, real letterhead, citations, signatures, seals or authentic-looking UI." if type_=="RECREATED_DOCUMENT" else "This is a NEW AUTHOR-CREATED EDITORIAL IMAGE, not a screenshot, official document or photograph of identified litigants. Avoid any fake legal prose."),
          "SPACE & SIZE: final image opaque 16:9. All allowed essential lettering and qualifiers well inside 8–92% horizontal and 9–76% vertical. Bottom 20% uncluttered, reserved for external narration subtitles. Prefer stable complete-frame reading at phone size. If 1k cannot legibly fit exact copy, output requires QC REJECT, not guessed abbreviation.",
          f"REFERENCE IMAGE 1 ({pair[0]}) STYLE ONLY — borrow {per1['use']}. IGNORE {per1['ignore']}.",
          f"REFERENCE IMAGE 2 ({pair[1]}) STYLE ONLY — borrow {per2['use']}. IGNORE {per2['ignore']}.",
          "COLOR/CRAFT: premium matte evidence-photo/editorial illustration; charcoal #1F1F1F, near-black #0B0B0B, warm ivory #EDEDED, rare red #D32222 and quiet warm gold #B69B68. Tangible paper/metal/glass, controlled low-key studio light, mild grain, coherent single hero scene. No excessive collage, stock icons, courtroom clichés, sensational fires, celebrity faces, logos copied from references, or repetitive generic split-screen headline templates.",
          "FINAL CHECK BEFORE DELIVERING: visually verify every EXACT quoted string is fully present and no other characters appear; protected propositions and parties remain together, prop surfaces blank, good spacing above subtitle safe zone. Never invent outcomes, totals, legal citations or source text. This is an illustration, but do NOT print ILLUSTRATION. Do NOT print the channel name except the locked GF060 endscreen string. Do NOT print SOURCES or source IDs."
        ]
        if type_=="ENDSCREEN":
            sections[7]="ENDSCREEN SPACE: Video-overlay areas must remain COMPLETELY BLANK per montage placement; keep exactly the three allowed endscreen strings, no supplementary copy. Studio overlay and 1080p placement require later QC. Do not put a faux subscribe button into a clickable overlay slot."
            sections[-1]="FINAL CHECK: exact three endscreen strings only; video link and subscribe overlay boxes remain unobstructed and unlettered. No illustration stamp or SOURCES footer."
        prompt="\n\n".join(sections)
        # Whitelist literal equality is the only positive text cue in the brief.
        extracted=prompt.split("PRINT EXACTLY THESE ",1)[1].split("\n\nTYPESETTING CONTRACT:",1)[0].split("\n",1)[1].split("\n")
        assert len(extracted)==len(locked)
        for n,(line,x) in enumerate(zip(extracted,locked),1):
            assert line==f" {n}. {json.dumps(x,ensure_ascii=False)}",(aid,line,x)
        assert '"ILLUSTRATION"' not in prompt and '"SOURCES"' not in prompt
        assert '"RECREATION / NOT AN ORIGINAL DOCUMENT"' in prompt if type_=="RECREATED_DOCUMENT" else '"RECREATION / NOT AN ORIGINAL DOCUMENT"' not in prompt
        assert "GF"+aid[2:] in prompt and len(prompt)<5900,(aid,len(prompt))
        req={"asset_id":aid,"version":"V7_PASS_REPAIR","status":"PREPARED_NOT_SUBMITTED","spend_authorized":False,
             "reference_ids":pair,"reference_mode":"STYLE_ONLY","factual_context_source_ids":sources,
             "generate_image_arguments":{"context":f"{aid}: full-frame editorial image; 2 style-only byte-verified reference images; exact editorial copy whitelist.",
             "params":{**{k:params[k] for k in ("model","resolution","quality","aspect_ratio","count")},
                       "prompt":prompt,"medias":[{"role":"image","value":p1["url"]},{"role":"image","value":p2["url"]}]}},
             "preflight":"STRUCTURAL_PASS_GENERATED_PIXEL_QC_PENDING","real_output_qc":"NOT_RUN"}
        reqs.append(req)
        rows.append({"asset_id":aid,"asset_type":type_,"ref_1":pair[0],"ref_1_sha256":p1["sha256"],"ref_1_url":p1["url"],
                     "ref_2":pair[1],"ref_2_sha256":p2["sha256"],"ref_2_url":p2["url"],
                     "references_distinct":"PASS","reference_risk_repair_reason":rule.get("reason","Both original byte-verified style-only references retained; contamination cues explicitly excluded."),
                     "exact_copy_count":len(locked),"locked_visible_text_json":json.dumps(locked,ensure_ascii=False),
                     "copy_density_risk":qa_tier,"text_qa":"NOT_VERIFIED_PIXEL","rendering_jobs":"0"})
        checks.append({"asset_id":aid,"hard_preflight":"PASS","frame_type":type_,"allowed_visible_text":locked,"allowed_copy_count":len(locked),"qa_risk":qa_tier,
                       "reference_ids":pair,"all_physical_props_blank":True,"subtitle_safe_percent":20,
                       "disallowed_other_onscreen_text":True,"after_image_generation_require":"HUMAN_PIXEL_TEXT_MATCH_PLUS_SUBJECT_AND_SUBTITLE_ZONE","visual_pass":"NOT_TESTED"})
        human.extend([f"### {aid} — {type_}",f"Style refs: [{pair[0]}]({p1['url']}) + [{pair[1]}]({p2['url']}); no evidence from ref images. Original fact refs: {', '.join(sources) if sources else 'none'}",
          f"Lettering risk: **{qa_tier}**; protected exact copy: {json.dumps(locked,ensure_ascii=False)}",
          "```text",prompt,"```",""])
    assert len(reqs)==len(rows)==len(checks)==60
    assert types["RECREATED_DOCUMENT"]==9 and types["ENDSCREEN"]==1
    assert all(len(x["generate_image_arguments"]["params"]["medias"])==2 for x in reqs)
    assert sum("RECREATION / NOT AN ORIGINAL DOCUMENT" in x["allowed_visible_text"] for x in checks)==9
    output={
      "12_HIGGSFIELD_REQUESTS_V7.jsonl":"".join(json.dumps(x,ensure_ascii=False,separators=(",",":"))+"\n" for x in reqs),
      "12_HIGGSFIELD_PROMPTS_V7.md":"\n".join(human).rstrip()+"\n",
      "12_REFERENCE_BINDINGS_V7.csv":csv_out(rows),
      "12_QC_PREFLIGHT_60_V7.csv":csv_out([{
        "asset_id":x["asset_id"],"preflight":x["hard_preflight"],"frame_type":x["frame_type"],"locked_copy_count":x["allowed_copy_count"],
        "risk":x["qa_risk"],"reference_1":x["reference_ids"][0],"reference_2":x["reference_ids"][1],
        "input_style_refs":2,"text_on_generated_pixels":"NOT_TESTED","image_generated_by_compiler":"NO",
        "nontext_geometry_qc":"NOT_TESTED","bottom_safe_area_qc":"NOT_TESTED","result":"READY_FOR_TEST_GENERATION_SUBJECT_TO_OWNER_APPROVAL"} for x in checks]),
    }
    receipt={"version":"V7_PASS_ORIENTED_60","status":"ALL_60_STRUCTURAL_PREFLIGHT_PASS_PIXEL_OUTPUT_NOT_GUARANTEED",
         "image_count":60,"montage_placements_unchanged":84,"document_recreation_count":9,
         "end_screen_count":1,"unique_reference_pair_count":len(unique_pairs),
         "reference_pairs_repaired_assets":exceptions,"repaired_pair_count":len(exceptions),
         "all_60_exact_original_visible_text":True,"all_60_two_byte_verified_style_references":True,
         "all_60_reference_image_sources_same_previously_approved_6":True,
         "all_60_onscreen_copy_whitelist_qa":"PASS_PREGEN_ONLY",
         "all_60_extra_word_prevention":"STRONG_PROMPT_INSTRUCTION_NOT_COMPUTER_VISION_GUARANTEE",
         "no_illustration_stamp_for_50_narrative_frames":True,
         "reconstruction_warning_for_all_9":True,
         "GF007_three_blank_folders_and_exact_party_copy_enforced":True,
         "GF006_blank_contract_text_and_update_glyph_enforced":True,
         "GF008_subordinate_courthouse_enforced":True,
         "GF009_exact_forum_wording_and_safe_area_enforced":True,
         "GF010_warning_slash_and_blank_tabs_enforced":True,
         "model_profile":"gpt_image_2 / 1k / low / 16:9",
         "configuration_only_cost_credits_each":0.5,"theoretical_60_first_attempt_base_credits":30.0,
         "paid_jobs_launched_by_v7":0,"media_imports_by_v7":0,"full_generation_approval_required":True,
         "next_qc":"ACTUAL_GENERATED_PIXELS_EXACT_WORD_BY_WORD_PLUS_SCENE_CROP_CHECK",
         "input_sha256":{n:hash_file(n) for n in (V7,"12_PROMPT_PACKAGE_V6.json","12_GENERATION_PLAN_V4.json","12_MONTAGE_ADAPTATION_V6.json","12_FILM_STRUCTURE_V5.json")},
         "output_sha256":{n:sha(s.encode()) for n,s in output.items()},
         "frame_reviews":checks,
         "notes":["No prompt design can guarantee 60/60 final PASS at model 1k low; prevent automatic acceptance or retries.","Do not edit 60 V4 source texts, original 84 placement timeline, or historical Higgsfield job ledger.","No subtitle/video/native 1920x1080 QC has been done."]}
    output["12_PASS_VALIDATION_V7.json"]=json_out(receipt)
    return output
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--write-derived",action="store_true")
    ap.add_argument("--print-qc",action="store_true")
    args=ap.parse_args()
    files=main_build()
    if args.write_derived:
        for name,content in files.items():(BASE/name).write_text(content,encoding="utf-8",newline="\n")
        print("WRITTEN 5 FILES: 60 images, 120 ref bindings, no API/generation")
    else:
        for name,content in files.items():
            assert (BASE/name).read_text(encoding="utf-8")==content,f"Stale derived file: {name}"
        print(json.dumps({"status":"V7 PASS preflight only, not pixels","image_count":60,"output_files":list(files),"spend":0},indent=2))
if __name__=="__main__":main()
