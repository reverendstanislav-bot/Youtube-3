#!/usr/bin/env python3
"""VIDEO 002 — Stage 18: owner-facing channel folder, same format as the HIA packs
(Desktop/Новая папка (3)/Youtube 2/VIDEO N):

    <NAME> - ГОТОВОЕ ВИДЕО.mp4
    ОБЛОЖКА.png
    ДАННЫЕ ДЛЯ ЗАГРУЗКИ.txt          step-by-step upload sheet with paste-ready texts
    SHORTS/<ID> - <HOOK>.mp4 …       + КАК ЗАГРУЖАТЬ SHORTS.txt

Source: <media>/18_UPLOAD_PACK (DELIVERY / PUBLISHING / SHORTS). Texts come from 18_BUILD_PUBLISHING_TEXT.py.
Usage: python 18_BUILD_CHANNEL_FOLDER.py [media_root] [channel_video_folder]
"""
import importlib.util, shutil, sys
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parent
DEST = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("C:/Users/KK/Desktop/Новая папка (3)/Youtube 3/Video 2")
spec = importlib.util.spec_from_file_location("txt", HERE / "18_BUILD_PUBLISHING_TEXT.py")
txt = importlib.util.module_from_spec(spec)
argv, sys.argv = sys.argv, sys.argv[:2]
spec.loader.exec_module(txt)
sys.argv = argv
PACK = txt.PACK

VIDEO_NAME = "ADOBE FIGMA - ГОТОВОЕ ВИДЕО.mp4"
SHORT_FILES = {
    "SH01": "AF-S01 - 1 BILLION FOR A DEAL THAT NEVER CLOSED.mp4",
    "SH02": "AF-S02 - THE CLAUSE CAME BEFORE THE DEAL.mp4",
    "SH03": "AF-S03 - NOT A PENALTY.mp4",
    "SH04": "AF-S04 - NO FINAL NO YET.mp4",
    "SH05": "AF-S05 - HOW THE DEAL ACTUALLY ENDED.mp4",
    "SH06": "AF-S06 - 3 DAYS LATER 1 BILLION.mp4",
    "SH07": "AF-S07 - 20 BILLION IS NOT 1 BILLION.mp4",
    "SH08": "AF-S08 - FIGMA AFTER ADOBE.mp4",
}
LINE = "=" * 50

def section(title, body):
    return f"{title}\n{LINE}\n\n{body.strip()}\n\n\n"

DEST.mkdir(parents=True, exist_ok=True)
(DEST / "SHORTS").mkdir(exist_ok=True)
shutil.copy2(PACK / "DELIVERY" / "VIDEO_002_UPLOAD_MASTER_1080P.mp4", DEST / VIDEO_NAME)
Image.open(PACK / "PUBLISHING" / "VIDEO_002_THUMBNAIL_MASTER.png").convert("RGB").resize((1280, 720), Image.LANCZOS) \
    .save(DEST / "ОБЛОЖКА.png")
for sid, name in SHORT_FILES.items():
    shutil.copy2(PACK / "SHORTS" / f"VIDEO_002_{sid}.mp4", DEST / "SHORTS" / name)

sheet = "ИНСТРУКЦИЯ ПО ЗАГРУЗКЕ ВИДЕО НА YOUTUBE\n" + LINE + "\n\n"
sheet += f"""В этой папке находятся:

1. {VIDEO_NAME} — готовый мастер 1920×1080.
2. ОБЛОЖКА.png — обложка 1280×720.
3. ДАННЫЕ ДЛЯ ЗАГРУЗКИ.txt — инструкция и готовые тексты.
4. SHORTS — восемь готовых вертикальных роликов и инструкция к ним.


"""
sheet += section("ШАГ 1. ЗАГРУЗИТЬ ВИДЕО", f"""В YouTube Studio нажмите «Создать» → «Добавить видео» и выберите:
{VIDEO_NAME}

Сначала установите «Ограниченный доступ» или «Доступ по ссылке».
Не публикуйте ролик, пока YouTube полностью не обработает 1080p.""")
sheet += section("ШАГ 2. НАЗВАНИЕ", txt.TITLE)
sheet += section("ШАГ 3. ОПИСАНИЕ", f"""Скопируйте английский текст между линиями:

---------------- НАЧАЛО ОПИСАНИЯ ----------------

{txt.DESCRIPTION.strip()}

---------------- КОНЕЦ ОПИСАНИЯ ----------------""")
sheet += section("ШАГ 4. ОБЛОЖКА", """Загрузите файл ОБЛОЖКА.png.
Перед публикацией проверьте его отображение в YouTube Studio.""")
sheet += section("ШАГ 5. НАСТРОЙКИ", """Язык видео: английский
Язык названия и описания: английский
Категория: Образование / Education
Для детей: Нет
Платная реклама: Нет
Изменённый или синтетический контент: Да
Музыка: отсутствует (голос и собственный звуковой дизайн)""")
sheet += section("ШАГ 6. ТЕГИ", ", ".join(txt.TAGS))
sheet += section("ШАГ 7. КОНЕЧНАЯ ЗАСТАВКА", """Отдельной конечной заставки в ролике нет: рассказ идёт до последних секунд.
Если нужны элементы конечной заставки, поставьте их на последние 5–10 секунд:
слева одно рекомендуемое видео канала, справа кнопку подписки.
Не закрывайте ими субтитры внизу кадра.""")
sheet += section("ШАГ 8. ЗАКРЕПЛЁННЫЙ КОММЕНТАРИЙ", txt.PINNED)
sheet += section("ВАЖНО ПО ФОРМУЛИРОВКАМ", """1. Не пишите, что Adobe «оштрафовали»: 1 млрд долларов — выплата по договору, а не штраф.
2. Не пишите, что сделку «запретили»: финального запрета регуляторов не было, сделку расторгли по взаимному согласию.
3. Не удаляйте блок CREDITS из описания: его требуют лицензии OGL v3.0 и CC BY 4.0.""")
sheet += section("ПРОВЕРКА ПЕРЕД ПУБЛИКАЦИЕЙ", """1. Дождитесь обработки 1080p.
2. Проверьте звук и встроенные английские субтитры.
3. Проверьте главы в описании.
4. Проверьте отображение обложки.
5. После проверки публикуйте или планируйте выпуск.""")
(DEST / "ДАННЫЕ ДЛЯ ЗАГРУЗКИ.txt").write_text(sheet, encoding="utf-8-sig")

shorts = "ИНСТРУКЦИЯ ПО ЗАГРУЗКЕ ВОСЬМИ ADOBE / FIGMA SHORTS\n" + LINE + "\n\n"
shorts += """Все ролики готовы в формате 1080×1920, 25 fps. В них используется утверждённый голос и звук из основного фильма, встроенные английские субтитры, музыки нет.

Загружайте Shorts по одному. Сначала используйте «Ограниченный доступ» или «Доступ по ссылке», дождитесь обработки HD и проверьте звук и кадрирование.


"""
for n, (sid, title, desc, tags) in enumerate(txt.SHORT_TEXT, 1):
    shorts += section(f"SHORT {n}", f"""Файл: {SHORT_FILES[sid]}
Название: {title} #Shorts
Описание:
{desc}

Watch the full documentary on What It Cost.

{tags}""")
shorts += section("НАСТРОЙКИ ДЛЯ КАЖДОГО SHORT", """Для детей: Нет
Изменённый или синтетический контент: Да
Музыка: отсутствует
После публикации основного ролика укажите его в каждом Short как связанное видео.""")
shorts += section("РЕКОМЕНДУЕМЫЙ ПОРЯДОК", """Short 1 → Short 2 → Short 3 → Short 4 → Short 5 → Short 6 → Short 7 → Short 8.
Не публикуйте все восемь одновременно. Оставляйте отдельное временное окно между публикациями.""")
(DEST / "SHORTS" / "КАК ЗАГРУЖАТЬ SHORTS.txt").write_text(shorts, encoding="utf-8-sig")

for p in sorted(DEST.rglob("*")):
    if p.is_file():
        print(f"{p.stat().st_size:>13,}  {p.relative_to(DEST)}")
