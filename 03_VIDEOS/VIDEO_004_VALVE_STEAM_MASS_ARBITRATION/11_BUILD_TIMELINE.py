"""Build provisional measured cues. ASR is evidence, not an auditory approval."""
import csv
import difflib
import hashlib
import json
import math
import re
from pathlib import Path

D = Path(__file__).resolve().parent
def read(name):
    return (D / name).read_text(encoding="utf-8").replace("\r\n", "\n")
def save(name, value):
    (D / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
def table(name, rows):
    with (D / name).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
def sha(name):
    return hashlib.sha256((D / name).read_bytes()).hexdigest()

# Explicit number spellings match the locked input. No invented word timing.
NUM = {"2021":"twenty twenty one", "2012":"twenty twelve", "997":"nine hundred ninety seven",
       "2026":"twenty twenty six", "4991":"four thousand nine hundred ninety one",
       "2023":"twenty twenty three", "2024":"twenty twenty four", "2025":"twenty twenty five",
       "454":"four hundred fifty four", "572":"five hundred seventy two",
       "118":"one hundred eighteen", "624":"six hundred twenty four",
       "400":"four hundred", "64":"sixty four", "4":"four", "20":"twenty",
       "3000":"three thousand", "26":"twenty six", "6269":"six two six nine",
       "27":"twenty seventh", "30":"thirtieth", "25":"twenty fifth",
       "18":"eighteenth", "21":"twenty first", "7":"seventh"}
def tokens(text):
    text = text.lower().replace("’", "'")
    text = re.sub(r"(?<=\d),(?=\d)", "", text)
    text = re.sub(r"(?<=\d)\.(?=\D|$)", "", text)
    text = re.sub(r"\b(\d+)(?:st|nd|rd|th)\b", r"\1", text)
    text = re.sub(r"\b\d+\b", lambda m:NUM.get(m[0], m[0]), text)
    return re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)*", text)

script = read("07_SCRIPT_FINAL.md")
sections = list(re.finditer(r"^## (S\d{2})[^\n]*\n\n([\s\S]*?)(?=\n## S\d{2}|\n---\n|\Z)", script, re.M))
voiceparts = list(re.finditer(r"^# PART ([A-C])[^\n]*\n\n([\s\S]*?)(?=\n---\n|\Z)", read("08_VOICE_SCRIPT.md"), re.M))
spoken = [p for m in voiceparts for p in m[2].strip().split("\n\n")]
paras = [{"section":m[1], "paragraph":i+1, "canonical_text":p}
         for m in sections for i,p in enumerate(m[2].strip().split("\n\n"))]
assert len(paras) == len(spoken) == 123
expected = []
for p, text in zip(paras, spoken):
    p["spoken_text"] = text; p["token_start"] = len(expected)
    expected.extend(tokens(text)); p["token_end"] = len(expected)
raw = json.loads(read("11_ASR_RAW.json"))
words = raw["words"]
actual, owners = [], []
for i,w in enumerate(words):
    ts = tokens(w["text"]); actual.extend(ts); owners.extend([i]*len(ts))
matcher = difflib.SequenceMatcher(None, expected, actual, autojunk=False)
aligned, differences = {}, []
equal_tokens = 0
for tag,a,b,c,d in matcher.get_opcodes():
    if tag == "equal":
        equal_tokens += b-a
        for k in range(b-a): aligned[a+k] = owners[c+k]
    else:
        near = words[owners[min(c,len(owners)-1)]]
        differences.append({"operation":tag, "expected":" ".join(expected[a:b]),
                            "recognized":" ".join(actual[c:d]), "near_sec":near["start"],
                            "canonical_token_start":a, "canonical_token_end":b,
                            "status":"REQUIRES_LISTEN_NOT_CONFIRMED_AUDIO_ERROR"})

for p in paras:
    ix = [aligned[i] for i in range(p["token_start"],p["token_end"]) if i in aligned]
    assert ix, p
    p["first_word_id"],p["last_word_id"] = words[min(ix)]["id"],words[max(ix)]["id"]
    p["speech_start"],p["speech_end"] = words[min(ix)]["start"],words[max(ix)]["end"]
    p["boundary_tokens_matched"] = p["token_start"] in aligned and p["token_end"]-1 in aligned
    p["unmatched_expected_tokens"] = sum(i not in aligned for i in range(p["token_start"],p["token_end"]))
    p["status"] = "PROVISIONAL_ASR_ANCHORED_NOT_AUDIO_LOCKED"

beats = json.loads(read("11_BEAT_INTENTS.json"))
claims = {r["claim_id"]:r for r in csv.DictReader(read("CLAIMS_LEDGER.csv").splitlines())}
def intent(p):
    hit = [b for b in beats if b["section"]==p["section"] and b["paragraph_start"]<=p["paragraph"]<=b["paragraph_end"]]
    assert len(hit)==1, p
    return hit[0]
def frame(t): return round(t*25)
boundaries = [0] + [frame((a["speech_end"]+b["speech_start"])/2) for a,b in zip(paras,paras[1:])] + [20200]
assert all(a<b for a,b in zip(boundaries,boundaries[1:]))
rows = []
for i,p in enumerate(paras):
    b=intent(p)
    sources=sorted({s for c in b["claim_ids"].split(";") for s in claims[c]["source_ids"].split(";")})
    rows.append({"scene_id":f"SC{i+1:03}","start_sec":round(boundaries[i]/25,6),
                 "end_sec":round(boundaries[i+1]/25,6),"script_ref":f"{p['section']}:p{p['paragraph']}",
                 "purpose":b["purpose"],"entity_or_event":p["canonical_text"],
                 "evidence_class":b["evidence_class"],"visual_plan":b["visual_plan"],
                 "source_ids":";".join(sources),"notes":"Cue boundary, not a mandatory picture cut; ASR only; rights/crop verification Stage12/16.",
                 "beat_id":b["beat_id"],"claim_ids":b["claim_ids"],"start_frame":boundaries[i],"end_frame":boundaries[i+1],
                 "first_word_id":p["first_word_id"],"last_word_id":p["last_word_id"],"short_ids":""})

def tc(t):
    ms=round(t*1000); h,ms=divmod(ms,3600000); m,ms=divmod(ms,60000); s,ms=divmod(ms,1000)
    return f"{h:02}:{m:02}:{s:02}.{ms:03}"
shorts=[]
for lock in csv.DictReader(read("07_SHORTS_LOCK.csv").splitlines()):
    selected=[(i,p) for i,p in enumerate(paras) if p["section"]==lock["section_start"] and int(lock["paragraph_start"])<=p["paragraph"]<=int(lock["paragraph_end"])]
    a,b=selected[0][1],selected[-1][1]
    assert a["boundary_tokens_matched"] and b["boundary_tokens_matched"], lock["short_id"]
    first=int(a["first_word_id"][1:]); last=int(b["last_word_id"][1:])
    start=max(0,a["speech_start"]-0.12)
    end=b["speech_end"]+0.18
    # Do not borrow preceding or following narration as padding.
    if first: start=max(start,words[first-1]["end"])
    if last+1<len(words): end=min(end,words[last+1]["start"])
    assert start<=a["speech_start"] and end>=b["speech_end"]
    duration=round(end-start,6); total=round(duration+3,6)
    assert total<=30, (lock["short_id"],total)
    ids=[]
    for i,p in selected:
        rows[i]["short_ids"]=lock["short_id"]; ids.append(rows[i]["scene_id"])
    shorts.append({"short_id":lock["short_id"],"status":"PROVISIONAL_ASR_CUT_AUDITION_PENDING",
                   "working_title":lock["hook"],"start_timecode":tc(start),"end_timecode":tc(end),
                   "duration_sec":duration,"section_range":f"{a['section']}:p{a['paragraph']}-p{b['paragraph']}",
                   "beat_ids":";".join(dict.fromkeys(intent(p)["beat_id"] for _,p in selected)),"gfx_ids":"",
                   "claim_ids":lock["claim_ids"],"hook":lock["hook"],"payoff":lock["payoff"],
                   "first_line":a["canonical_text"],"last_line":b["canonical_text"],
                   "extraction_rule":"CONTIGUOUS_NO_REWRITE_NO_REORDER", "audio_source":"VIDEO004_HARRISON_V11_MASTER.wav",
                   "vertical_rule":"ALT_LAYOUT_SAME_EVIDENCE_AND_AUDIO_NO_SHAKE_NO_BURNED_CAPTIONS",
                   "legal_review":"TEXT_LOCK_PRESERVED_AUDIO_QUALIFICATIONS_REQUIRE_LISTEN",
                   "start_sec":round(start,6),"end_sec":round(end,6),"speech_start_sec":a["speech_start"],
                   "speech_end_sec":b["speech_end"],"cta_sec":3,"planned_total_sec":total,
                   "scene_ids":";".join(ids),"export_measured":False})

rows.append({"scene_id":"SC124","start_sec":808,"end_sec":828,"script_ref":"NO_NARRATION_ENDSCREEN",
             "purpose":"20-second native YouTube end screen after narration ends.","entity_or_event":"WHAT IT COST",
             "evidence_class":"EDITOR_GRAPHIC","visual_plan":"Stable 16:9 design with empty space for one native video element and Subscribe; verify sizes in Studio, no painted fake buttons.",
             "source_ids":"","notes":"PLANNED_ONLY; silence after master; not present in current808s WAV; no stretching narration.",
             "beat_id":"ENDSCREEN","claim_ids":"","start_frame":20200,"end_frame":20700,
             "first_word_id":"","last_word_id":"","short_ids":""})
table("SCENE_TIMELINE.csv", rows)
table("11_SHORTS_CUT_MAP.csv", shorts)
save("11_WORD_LEVEL_TRANSCRIPT.json", {"status":"PROVISIONAL_ASR_NOT_HUMAN_VERIFIED", "runtime_sec":808,
     "planned_video_runtime_sec":828,"source_sha256":"8c11be2619a6a84b7e1a6cbe0cb8c708d72dff556d1d737dd46f596ea21f65d7",
     "engine":raw["engine"],"model":raw["model"],"words":words})
save("11_PARAGRAPH_ALIGNMENT.json",paras)
save("11_ALIGNMENT_QC.json", {"status":"PROVISIONAL_NOT_STAGE10_OR_STAGE11_PASS",
     "expected_tokens":len(expected),"asr_normalized_tokens":len(actual),"equal_tokens":equal_tokens,
     "exact_token_coverage":equal_tokens/len(expected),"differences":differences,
     "word_count":len(words),"short_word_spans":[w for w in words if w["end"]-w["start"]<0.05],
     "low_confidence_words":[w for w in words if w["probability"]<0.6],
     "paragraphs":len(paras),"paragraph_boundary_mismatches":[p["section"]+":p"+str(p["paragraph"]) for p in paras if not p["boundary_tokens_matched"]],
     "scene_rows":len(rows),"authored_macro_beats":len(beats),"coverage_frames":20700,
     "audio_locked":False,"auditory_review":"NOT_PERFORMED", "short_exports_measured":False,
     "input_hashes":{n:sha(n) for n in ["07_SCRIPT_FINAL.md","08_VOICE_SCRIPT.md","07_SHORTS_LOCK.csv","11_ASR_RAW.json","11_BEAT_INTENTS.json"]}})
print(json.dumps({"words":len(words),"match":equal_tokens/len(expected),"differences":len(differences),
                  "scenes":len(rows),"shorts":[[s["short_id"],s["start_sec"],s["end_sec"],s["planned_total_sec"]] for s in shorts]},indent=2))
