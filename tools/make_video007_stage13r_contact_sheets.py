from __future__ import annotations

import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(r"C:\Users\KK\Youtube-3-video005-voice\.local_stage13r_build\VIDEO007_STAGE13R")
FFMPEG = Path(r"C:\Users\KK\VIDEO007_STAGE13R_TOOLS\ffmpeg\ffmpeg-9.0.2-essentials_build\bin\ffmpeg.exe")
QC = ROOT / "manifests" / "qc_contact_sheets"
THUMBS = QC / "_thumbs"


def font(size: int) -> ImageFont.FreeTypeFont:
    p = Path(r"C:\Windows\Fonts\arial.ttf")
    return ImageFont.truetype(str(p), size) if p.exists() else ImageFont.load_default()


def fit(im: Image.Image, size: tuple[int, int]) -> Image.Image:
    copy = im.convert("RGB")
    copy.thumbnail(size, Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", size, "#111111")
    canvas.paste(copy, ((size[0] - copy.width) // 2, (size[1] - copy.height) // 2))
    return canvas


def sheet(items: list[tuple[Path, Image.Image]], prefix: str) -> None:
    cols, rows = 4, 4
    cell_w, cell_h = 480, 270
    for page, start in enumerate(range(0, len(items), cols * rows), 1):
        canvas = Image.new("RGB", (1920, 1080), "#080808")
        d = ImageDraw.Draw(canvas)
        for n, (path, image) in enumerate(items[start:start + cols * rows]):
            x = (n % cols) * cell_w
            y = (n // cols) * cell_h
            tile = fit(image, (cell_w, cell_h - 34))
            canvas.paste(tile, (x, y))
            d.rectangle((x, y + cell_h - 34, x + cell_w, y + cell_h), fill="#111111")
            label = path.name[:55]
            d.text((x + 8, y + cell_h - 29), label, font=font(17), fill="#EDEDED")
        canvas.save(QC / f"{prefix}_{page:02d}.jpg", quality=90)


def main() -> None:
    QC.mkdir(parents=True, exist_ok=True)
    THUMBS.mkdir(parents=True, exist_ok=True)
    cut_items = []
    for i, path in enumerate(sorted((ROOT / "video_horizontal" / "cuts").rglob("*.mp4"))):
        thumb = THUMBS / f"cut_{i:03d}.jpg"
        subprocess.run([str(FFMPEG), "-hide_banner", "-loglevel", "error", "-y", "-ss", "2.5", "-i", str(path),
                        "-frames:v", "1", "-vf", "scale=480:270:force_original_aspect_ratio=decrease,pad=480:270:(ow-iw)/2:(oh-ih)/2:black",
                        str(thumb)], check=True)
        with Image.open(thumb) as im:
            cut_items.append((path, im.copy()))
    sheet(cut_items, "CUTS")

    for folder, prefix, patterns in [
        (ROOT / "stills", "STILLS", ("*.jpg", "*.jpeg", "*.png")),
        (ROOT / "documents" / "crops", "DOCUMENT_CROPS", ("*.png",)),
        (ROOT / "editor_gfx" / "png", "EDITOR_GFX", ("*.png",)),
    ]:
        paths = []
        for pattern in patterns:
            paths.extend(folder.rglob(pattern))
        items = []
        for path in sorted(set(paths)):
            with Image.open(path) as im:
                items.append((path, im.copy()))
        sheet(items, prefix)

    for path in THUMBS.glob("*.jpg"):
        path.unlink()
    THUMBS.rmdir()
    print(f"contact_sheets={len(list(QC.glob('*.jpg')))}")


if __name__ == "__main__":
    main()
