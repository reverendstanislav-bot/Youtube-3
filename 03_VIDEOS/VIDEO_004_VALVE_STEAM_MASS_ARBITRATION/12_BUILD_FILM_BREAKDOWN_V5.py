"""Build/validate full-film chapter and placement maps without writing files.

Default checks committed derived outputs. --patch prints an apply_patch patch.
No network, paid jobs, voice edits, render or stage advancement.
"""
from __future__ import annotations

import argparse
import csv
import difflib
import hashlib
import io
import json
import re
import sys
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent
FPS = 25


def read_csv(name):
    with (BASE / name).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def hash_text(name):
    return hashlib.sha256((BASE / name).read_text(encoding="utf-8").encode("utf-8")).hexdigest()


def tc(frame):
    seconds, frame_part = divmod(int(frame), FPS)
    minutes, second_part = divmod(seconds, 60)
    hours, minute_part = divmod(minutes, 60)
    return f"{hours:02}:{minute_part:02}:{second_part:02}:{frame_part:02}"


def clock(frame):
    seconds = int(frame) / FPS
    minutes = int(seconds // 60)
    return f"{minutes:02}:{seconds-minutes*60:05.2f}"


def ids(rows, key):
    return ";".join(sorted({part for row in rows for part in row[key].split(";") if part}))


def csv_text(rows):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows({key:spaced(value) if isinstance(value,str) else value for key,value in row.items()} for row in rows)
    return stream.getvalue()


def spaced(text):
    text = re.sub(r"(?<=[А-Яа-яЁё])(?=[A-Za-z0-9])", " ", text)
    return re.sub(r"(?<=[A-Za-z0-9])(?=[А-Яа-яЁё])", " ", text)


def build():
    plan = json.loads((BASE / "12_FILM_STRUCTURE_V5.json").read_text(encoding="utf-8"))
    receipt = json.loads((BASE / "12_GENERATION_COUNT_V4.json").read_text(encoding="utf-8"))
    for name, expected in receipt["input_sha256"].items():
        assert hash_text(name) == expected, f"Upstream changed: {name}"
    cues = {row["scene_id"]: row for row in read_csv("SCENE_TIMELINE.csv")}
    mapped = read_csv(plan["source_cue_map"])
    assets = {row["asset_id"]: row for row in read_csv("12_GENERATION_ASSET_MANIFEST_V4.csv")}
    chapters = plan["chapters"]
    assert [c["id"] for c in chapters] == [f"S{i:02}" for i in range(1,14)] + ["ENDSCREEN"]
    assert plan["audio_master_sec"] == 808 and plan["planned_total_sec"] == 828
    assert plan["planned_end_screen_sec"] == 20 and plan["new_generation_jobs"] == 0
    chapter_for_scene = {}
    chapter_bounds = {}
    cursor = 0
    for chapter in chapters:
        names = [f"SC{i:03}" for i in range(int(chapter["first_scene"][2:]), int(chapter["last_scene"][2:])+1)]
        start = int(cues[names[0]]["start_frame"])
        end = int(cues[names[-1]]["end_frame"])
        assert start == cursor, f"Chapter gap/overlap {chapter['id']}"
        cursor = end
        for name in names:
            assert name not in chapter_for_scene
            chapter_for_scene[name] = chapter["id"]
            assert cues[name]["script_ref"].split(":")[0] == chapter["id"] or chapter["id"] == "ENDSCREEN"
        chapter_bounds[chapter["id"]] = (start, end)
    assert cursor == 20700 and set(chapter_for_scene) == set(cues)
    groups = []
    for row in mapped:
        if not groups or groups[-1]["asset_id"] != row["asset_id"]:
            groups.append({"asset_id":row["asset_id"],"rows":[]})
        groups[-1]["rows"].append(row)
    assert len(groups) == len(plan["placements"]) == receipt["continuous_image_placements_including_reuses"]
    seen = set()
    edit_rows = []
    for i, (group, direction) in enumerate(zip(groups, plan["placements"]),1):
        rows = group["rows"]
        start, end = int(rows[0]["start_frame"]), int(rows[-1]["end_frame"])
        assert direction["placement_id"] == f"PL{i:03}"
        assert direction["asset_id"] == group["asset_id"]
        assert (direction["start_frame"],direction["end_frame"]) == (start,end)
        assert direction["first_scene"] == rows[0]["scene_id"] and direction["last_scene"] == rows[-1]["scene_id"]
        assert direction["treatment"] in {"STATIC","CONDITIONAL_DETAIL"}
        assert direction["transition_in"] == ("START" if i == 1 else "MOTIVATED_STRAIGHT_CUT")
        assert direction["pixel_review"] == "NOT_PERFORMED" and direction["timing"] == "PROVISIONAL_ASR_GRID"
        asset = assets[group["asset_id"]]
        if asset["asset_type"] == "RECREATED_DOCUMENT":
            assert asset["mandatory_label"] == "RECREATION / NOT AN ORIGINAL DOCUMENT"
        use = "REUSE" if group["asset_id"] in seen else "FIRST_USE"
        seen.add(group["asset_id"])
        edit_rows.append({
            "placement_id":direction["placement_id"],"chapter_ids":";".join(dict.fromkeys(chapter_for_scene[r["scene_id"]] for r in rows)),
            "asset_id":group["asset_id"],"use_status":use,"start_frame":start,"end_frame":end,
            "in_tc_25fps":tc(start),"out_tc_25fps_exclusive":tc(end),"duration_sec":f"{(end-start)/FPS:.2f}",
            "scene_ids":";".join(dict.fromkeys(r["scene_id"] for r in rows)),"script_refs":";".join(dict.fromkeys(r["script_ref"] for r in rows)),
            "beat_ids":ids(rows,"beat_id"),"claim_ids":ids(rows,"claim_ids"),"source_ids":ids(rows,"source_ids"),"short_ids":ids(rows,"short_ids"),
            "asset_type":asset["asset_type"],"generated_display_text":asset["visible_text"],"mandatory_label":asset["mandatory_label"],
            "viewer_focus_ru":direction["viewer_focus_ru"],"cut_reason_ru":direction["cut_reason_ru"],"treatment":direction["treatment"],
            "transition_in":direction["transition_in"],"timing_status":direction["timing"],"pixel_qc":direction["pixel_review"],
            "execution_gate":"AUDIO_FINAL_LOCK_AND_ACTUAL_IMAGE_QC_REQUIRED"})
    assert len(seen) == len(assets) == receipt["unique_generated_frame_slots"]
    assert sum(r["use_status"] == "REUSE" for r in edit_rows) == receipt["repeat_placements_without_new_generation"]
    first_use = {r["asset_id"]:r["start_frame"] for r in edit_rows if r["use_status"] == "FIRST_USE"}
    chapter_rows = []
    for chapter in chapters:
        start,end = chapter_bounds[chapter["id"]]
        rows = [r for r in mapped if chapter_for_scene[r["scene_id"]] == chapter["id"]]
        touching = [r for r in edit_rows if int(r["start_frame"]) < end and int(r["end_frame"]) > start]
        chapter_rows.append({"chapter_id":chapter["id"],"act_id":chapter["act"],"title_ru":chapter["title_ru"],"start_frame":start,"end_frame":end,
            "in_tc_25fps":tc(start),"out_tc_25fps_exclusive":tc(end),"duration_sec":f"{(end-start)/FPS:.2f}","first_scene":chapter["first_scene"],"last_scene":chapter["last_scene"],
            "asset_ids":ids(rows,"asset_id"),"new_unique_images_first_used_here":sum(start <= frame < end for frame in first_use.values()),
            "placements_touching_chapter":len(touching),"placement_ids":";".join(r["placement_id"] for r in touching),"beat_ids":ids(rows,"beat_id"),"source_ids":ids(rows,"source_ids"),"short_ids":ids(rows,"short_ids"),
            "viewer_question_ru":chapter["question_ru"],"payoff_ru":chapter["payoff_ru"],"handoff_ru":chapter["handoff_ru"],"director_intent":chapter["director_intent"]})
    assert sum(r["new_unique_images_first_used_here"] for r in chapter_rows) == len(assets)
    short_rows = []
    for short in read_csv("11_SHORTS_CUT_MAP.csv"):
        sid = short["short_id"]
        if sid not in {"SH01","SH02","SH04","SH08"}:
            continue
        start_sec,end_sec = float(short["start_sec"]),float(short["end_sec"])
        touched = [r for r in edit_rows if int(r["start_frame"])/FPS < end_sec and int(r["end_frame"])/FPS > start_sec]
        final_sec = end_sec-start_sec+3
        assert final_sec <= 30
        short_rows.append({"short_id":sid,"source_start_sec":start_sec,"source_end_sec":end_sec,"planned_cta_sec":3,"planned_total_sec":round(final_sec,2),"placement_ids":";".join(r["placement_id"] for r in touched),"asset_sequence":";".join(r["asset_id"] for r in touched),"vertical_gate":"PLAN_REFRAME_PRESERVING_ALL_CAVEATS_OR_SEPARATELY_APPROVED_ALT_LAYOUT","pixel_review":"NOT_PERFORMED","extra_generated_assets_count":"NOT_ESTABLISHED_NOT_IN_LONGFORM_COUNT"})
    assert {r["short_id"] for r in short_rows} == {"SH01","SH02","SH04","SH08"}
    report = {"status":"WHOLE_FILM_PLAN_STRUCTURAL_PASS_NOT_RENDER_QC","voice_sec":808,"tail_no_voice_sec":20,"planned_film_sec":828,"planned_film_clock":"13:48","fps":FPS,"covered_frames":20700,"chapters_including_endscreen":len(chapters),"acts_excluding_tail":len(plan["acts"]),"placements":len(edit_rows),"unique_full_frame_images":len(assets),"repeat_placements":len(edit_rows)-len(assets),"cue_segments_preserved":len(mapped),"scene_cues_covered":len(cues),"narrative_beats":receipt["narrative_macro_beats_covered"],"treatments":dict(Counter(r["treatment"] for r in edit_rows)),"max_narration_placement_sec":max(float(r["duration_sec"]) for r in edit_rows[:-1]),"average_narration_placement_sec":round(808/(len(edit_rows)-1),3),"chapter_crossings_are_not_extra_cuts":[r["placement_id"] for r in edit_rows if ";" in r["chapter_ids"]],"short_count":len(short_rows),"paid_jobs":0,"audio_or_script_changed":False,"input_sha256_scheme":"UTF8_LF_NORMALIZED","input_sha256":{name:hash_text(name) for name in ("12_FILM_STRUCTURE_V5.json","12_GENERATION_PLAN_V4.json","12_GENERATION_CUE_MAP_V4.csv","07_SCRIPT_FINAL.md","SCENE_TIMELINE.csv","11_SHORTS_CUT_MAP.csv")}}
    lines = ["# VIDEO004 — полная режиссёрская разбивка V5", "", "**План фильма: 13:48 = 13:28 готовой озвучки под QC + 00:20 финального экрана без речи.** Это план будущего фильма, не проверенный готовый экспорт.", "", "5 актов → 13 глав истории + эндскрин → 84 монтажных появления → 60 уникальных полных изображений (59 сюжетных + 1 эндскрин). 24 возвращения используют прежнее изображение. Все 123 речевые реплики/54 смысловых бита и отдельный эндскрин покрыты. Сетка 25 fps: 0..20700 frames, границы справа исключены.", "", "Разбивка разворачивает весь сценарий, не заменяет его и не растягивает голос ради целевых 15–22 минут канала. Уже существующий master 808 с определяет длину этого V11. Аудио не замедлять, паузы не набивать, новые реплики не генерировать.", "", "## Пять актов", ""]
    for act in plan["acts"]:
        start = chapter_bounds[act["chapters"][0]][0]
        end = chapter_bounds[act["chapters"][-1]][1]
        lines.append(f"- {clock(start)}–{clock(end)} — {act['title_ru']} ({', '.join(act['chapters'])}).")
    lines += ["", "## Все главы", "", "Таймкоды здесь MM:SS.ss; точные HH:MM:SS:FF, 25 fps и frame-in/out — в CSV. «Новые» — первые появления уникальных изображений, не число jobs. Кадр может пересекать границу главы без дополнительного склеивания.", "", "| Глава | Время | Длина | Содержание | Новых изображений |", "|---|---|---:|---|---:|"]
    for chapter in chapter_rows:
        lines.append(f"| {chapter['chapter_id']} | {clock(chapter['start_frame'])}–{clock(chapter['end_frame'])} | {chapter['duration_sec']}с | {chapter['title_ru']} | {chapter['new_unique_images_first_used_here']} |")
    lines += ["", "## Драматургия каждой главы", ""]
    for chapter in chapter_rows:
        lines += [f"### {chapter['chapter_id']} — {chapter['title_ru']}", "", f"Вопрос: {chapter['viewer_question_ru']}", "", f"Ответ/граница: {chapter['payoff_ru']}", "", f"Переход: {chapter['handoff_ru']}", "", f"Монтажные блоки: {chapter['placement_ids']}. Кадры: {chapter['asset_ids']}. Реплики: {chapter['first_scene']}–{chapter['last_scene']}.", ""]
    lines += ["## Что делает монтаж, а что — генерация", "", "`12_FILM_EDIT_MAP_V5.csv` — 84 последовательных размещения PL001–PL084. У каждого есть точные границы, реплики, источники/claimID, текст уже внутри генерируемого изображения, цель внимания, причина склейки, повтор/первое использование и статус приёмки. Это не 175 старых Fusion-состояний и не список 60 длинных слайдов без режиссуры.", "", "77 размещений — стабильные планы; 7 — условный подход к конкретному смысловому объекту. Условность важна: пока изображения не созданы, геометрия crop/движения не проверена. Если теряются дата, оговорка или сторона спора — STATIC и повторное QC, не автоматический zoom и не новая платная вариация. Никаких универсальных дрейфов, скачков, тряски, текстовых подмен или вшитых речевых субтитров.", "", "Прямая смысловая склейка — базовый переход. Не накладывать два юридических текста друг на друга ради плавности. Речь остаётся единым источником 0..808 с, без аудиопорезки на границах глав. Картинка не должна показать FOUR раньше SC037, автоматическое незакрытие раньше SC050, отказ AAA раньше SC070 или судебный результат раньше SC100.", "", "Максимальное непрерывное речевое размещение 17 с; среднее 9.735 с. Это не гарантия темпа: проверить нормальным просмотром первые 60 с и длинные PL006/PL020/PL047/PL058. Плотные GF001/GF012/GF038/GF058/GF059 требуют настоящей проверки читаемости на телефоне.", "", "## Четыре Shorts в этой картине", "", "| Short | Озвучка из master | План с 3 с CTA | Кадры по порядку |", "|---|---|---:|---|"]
    for short in short_rows:
        lines.append(f"| {short['short_id']} | {short['source_start_sec']:.2f}–{short['source_end_sec']:.2f}с | {short['planned_total_sec']:.2f}с | {short['asset_sequence']} |")
    lines += ["", "Это непрерывные выдержки из основного голоса, не отдельная озвучка. V5 карта показывает нужные кадры, но не утверждает готовность 9:16. Вертикальные варианты/CTA и превью не скрыты внутри 60; дополнительные генерации отдельно перечисляются и согласуются при необходимости. Ни один горизонтальный crop не может отрезать attribution/date/legal caveat. Все четыре cut-edge требуют слухового QC.", "", "## Как это связано со всем производственным Git", "", "| Участок | Авторитетный вход / выход | Текущая граница |", "|---|---|---|", "| Stage02–07 | 02_STORY_MAP.md, ledgers, 07_SCRIPT_FINAL.md | V11 не переписан; 4 активных Shorts |", "| Stage08–10 | 08_VOICE_SCRIPT.md,10_AUDIO_MASTER.md | Master808с; full auditory QC open |", "| Stage11 | SCENE_TIMELINE.csv,11_WORD_LEVEL_TRANSCRIPT.json,11_SHORTS_CUT_MAP.csv |125 V4 сегментов покрывают 124 cue; финальная сетка provisional |", "| Stage12 кадры | 12_VISUAL_SOURCE_PLAN.md → 12_GENERATION_PLAN_V4.json/manifest | 60 полных изображений; 0 jobs |", "| Stage12 вся картина | 12_FILM_STRUCTURE_V5.json → chapters/edit/Shorts CSV + этот документ | 5 актов / 14 глав / 84 размещения; структурная проверка отдельно от media QC |", "| Stage12 спецификации | 12_IMAGE_PROMPTS.md,12_RECONSTRUCTION_PROMPTS.md | Входные маршруты к единому V4, не альтернативные Editor/Fusion-сборки |", "| Stage13 | Actual generation/source QC и ASSET_MANIFEST.csv | NOT_STARTED; плановые строки не выданы за файлы |", "| Stage14–15 | Ссылаться на PL/GF-ID этой карты при последующих graphics/sound/assembly | NOT_STARTED; код монтажа, музыка/SFX и рендер сейчас не создавались |", "| Stage16 | Final fact/legal refresh + provenance audit | NOT_RUN; апелляционный снимок не текущий официальный статус |", "| Stage17–19 | Packaging/upload/analytics | NOT_STARTED; не готово к выгрузке |", "", "Старые V2/V3, PDF-слои и Fusion-canary — история; не удалить и не запускать как действующую стратегию. `ASSET_MANIFEST.csv` хранит реальные аудиофайлы; плановые изображения — в 12_GENERATION_ASSET_MANIFEST_V4.csv, пока файлов нет.", "", "## Проверка и остановка", "", "```powershell", "python 03_VIDEOS/VIDEO_004_VALVE_STEAM_MASS_ARBITRATION/12_VALIDATE_GENERATION_PLAN_V4.py", "python 03_VIDEOS/VIDEO_004_VALVE_STEAM_MASS_ARBITRATION/12_BUILD_FILM_BREAKDOWN_V5.py", "```", "", "Проверяются согласованность V4/V5, каждый frame/ID/источник, структура глав, 125 сегментов, 60 уникальных кадров, 84 размещения и 4 Shorts. Команды не генерируют, не рендерят, не пишут файлы. `--patch` выводит patch производных файлов для apply_patch.", "", "Текущий этап остаётся 10_AUDIO_MASTER. Полное слушание, реальные буквы/мобильная читаемость, темп, эндскрин Studio и релиз не приняты. В рамках исторического V5 модель/стоимость Higgsfield не выбирались/не запрашивались; актуальная подготовка запросов — 12_IMAGE_PROMPTS.md (V6). 0 новых paid jobs; отдельное согласование расходов обязательно. V5 — полная подготовленная режиссёрская карта, не готовый фильм."]
    return {"12_FILM_CHAPTERS_V5.csv":csv_text(chapter_rows),"12_FILM_EDIT_MAP_V5.csv":csv_text(edit_rows),"12_FILM_SHORTS_MAP_V5.csv":csv_text(short_rows),"12_FILM_VALIDATION_V5.json":json.dumps(report,ensure_ascii=False,indent=2)+"\n","12_FILM_BREAKDOWN_V5.md":spaced("\n".join(lines))+"\n"}


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("--patch",action="store_true")
    args = parser.parse_args()
    outputs = build()
    if args.patch:
        print("*** Begin Patch")
        for name, content in outputs.items():
            path = BASE / name
            if path.exists():
                old = path.read_text(encoding="utf-8")
                if old == content:
                    continue
                print(f"*** Update File: {path.as_posix()}")
                for line in list(difflib.unified_diff(old.splitlines(),content.splitlines(),lineterm=""))[2:]:
                    print("@@" if line.startswith("@@") else line)
            else:
                print(f"*** Add File: {path.as_posix()}")
                for line in content.splitlines():
                    print("+"+line)
        print("*** End Patch")
    else:
        for name, content in outputs.items():
            assert (BASE / name).read_text(encoding="utf-8") == content, f"Stale output: {name}"
        print(outputs["12_FILM_VALIDATION_V5.json"])


if __name__ == "__main__":
    main()
