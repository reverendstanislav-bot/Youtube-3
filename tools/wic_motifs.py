#!/usr/bin/env python3
"""Brand fonts for WeftCut motifs.

Motifs render offline, so fonts must be embedded as data: URIs. Motif HTML is
authored with placeholders (e.g. __WIC_BEBAS__) and this tool swaps them for
base64 fonts inside WeftCut's draft folder, or back again for the repo copy.

  python tools/wic_motifs.py inject <draft_id>        # placeholders -> fonts (before preview/install)
  python tools/wic_motifs.py export <motif_id> <name> # draft/installed -> weftcut/motifs/<name>.html (fonts -> placeholders)
"""
from __future__ import annotations

import base64
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = Path(os.environ.get("WIC_MEDIA", "C:/Users/KK/Documents/WhatItCost_media")) / "_fonts" / "woff2"
DRAFTS = Path(os.environ["APPDATA"]) / "WeftCut" / "data" / "motifs" / "drafts"
FONTS = {
    "__WIC_BEBAS__": "bebas-neue-400.woff2",
    "__WIC_INTER500__": "inter-500.woff2",
    "__WIC_INTER700__": "inter-700.woff2",
    "__WIC_MONT800__": "montserrat-800.woff2",
    "__WIC_GARAMOND_I__": "eb-garamond-400-italic.woff2",
}


def b64(name: str) -> str:
    return base64.b64encode((FONT_DIR / name).read_bytes()).decode()


def draft_html(motif_id: str) -> Path:
    """Draft folder first; installed motifs live one level up."""
    for p in (DRAFTS / motif_id / "index.html", DRAFTS.parent / motif_id / "index.html"):
        if p.is_file():
            return p
    sys.exit(f"no draft or installed motif {motif_id}")


def inject(draft_id: str) -> None:
    p = draft_html(draft_id)
    s = p.read_text(encoding="utf-8")
    used = [k for k in FONTS if k in s]
    for k in used:
        s = s.replace(k, b64(FONTS[k]))
    p.write_text(s, encoding="utf-8")
    print(f"{draft_id}: embedded {', '.join(used) or 'nothing'}")


def export(draft_id: str, name: str) -> None:
    s = draft_html(draft_id).read_text(encoding="utf-8")
    for k, f in FONTS.items():
        s = s.replace(b64(f), k)
    out = ROOT / "weftcut" / "motifs" / f"{name}.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(s, encoding="utf-8")
    print(f"saved {out.relative_to(ROOT)}")


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "inject":
        inject(sys.argv[2])
    elif len(sys.argv) == 4 and sys.argv[1] == "export":
        export(sys.argv[2], sys.argv[3])
    else:
        sys.exit(__doc__)
