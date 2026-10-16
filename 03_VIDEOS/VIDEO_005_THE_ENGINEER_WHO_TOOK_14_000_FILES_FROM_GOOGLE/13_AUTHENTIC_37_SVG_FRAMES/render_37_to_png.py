#!/usr/bin/env python3
"""Render VIDEO005 authentic-source 1920x1080 SVG masters to individual PNGs; no Codex/AI."""
from __future__ import annotations
from pathlib import Path
import sys, subprocess, shutil, json, hashlib, re
ROOT=Path(__file__).resolve().parent
FRAMES=ROOT/"frames"
OUT=ROOT/"PNGS_1920x1080"
OUT.mkdir(parents=True,exist_ok=True)
svgs=sorted(FRAMES.glob("V005-VP*.svg"))
if len(svgs)!=37: sys.exit(f"ERROR: expected exactly 37 SVG frames, found {len(svgs)}")
try: import cairosvg
except ImportError: cairosvg=None
inkscape=shutil.which("inkscape")
if cairosvg is None and not inkscape: sys.exit("Need CairoSVG (pip install cairosvg) OR Inkscape")
from PIL import Image
report=[]
for i,src in enumerate(svgs,1):
    data=src.read_text(encoding="utf-8")
    if not ('width="1920" height="1080"' in data and 'data:image/png;base64,' in data):
        sys.exit(f"Malformed/un-sourced frame: {src.name}")
    target=OUT/(src.stem+".png")
    if cairosvg:
        cairosvg.svg2png(url=str(src),write_to=str(target),output_width=1920,output_height=1080)
    else:
        subprocess.run([inkscape,str(src),"--export-type=png",f"--export-filename={target}","--export-width=1920","--export-height=1080"],check=True,capture_output=True)
    with Image.open(target) as im:
        if im.size!=(1920,1080):sys.exit(f"SIZE ERROR {src.name}: {im.size}")
    sha=hashlib.sha256(target.read_bytes()).hexdigest()
    original_count=data.count('href="data:image/png;base64,')
    report.append({"asset_id":src.stem,"file":target.name,"sha256":sha,"original_source_excerpts_embedded":original_count,"dimensions":[1920,1080],"release":"PENDING_HUMAN_VISUAL_LEGAL_RIGHTS_QC"})
    print(f"{i:02d}/37 {target.name}: OK, native sources {original_count}")
(OUT/"RENDER_QC_PENDING_OWNER.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
print(f"Output: {OUT}")
print("Important: technical export verified. Editorial, source-context, legal rights and owner acceptance are still HOLD.")
