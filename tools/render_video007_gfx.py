#!/usr/bin/env python3
"""Render the 143 WHAT IT COST editable Stage13 SVGs to PNGs for Resolve.
No external requests, no generation credits. Takes only checked-out GitHub assets.
Example: python tools/render_video007_gfx.py --root . --dest /tmp/video007_editor_png --check-only
Example: python tools/render_video007_gfx.py --root . --dest /tmp/video007_editor_png
"""
import argparse, csv, subprocess, sys, xml.etree.ElementTree as ET
from pathlib import Path

ROOT_PART = Path("03_VIDEOS/VIDEO_007_APPLE_OPENAI_THE_TRADE_SECRET_WAR")
def run():
    p=argparse.ArgumentParser()
    p.add_argument("--root",default=".")
    p.add_argument("--dest",default="/tmp/video007_editor_png")
    p.add_argument("--check-only",action="store_true")
    args=p.parse_args()
    root=Path(args.root).resolve()
    base=root/ROOT_PART
    with (base/"13_ASSET_MANIFEST.csv").open(encoding="utf8",newline="") as f:
        rows=list(csv.DictReader(f))
    gfx=[r for r in rows if r["type"]=="EDITOR_FACT_GFX"]
    assert len(gfx)==143, len(gfx)
    out=Path(args.dest);out.mkdir(parents=True,exist_ok=True)
    reports=[]
    for r in gfx:
        sf=base/r["asset_file_in_repository"]
        assert sf.is_file(),f"Missing {sf}"
        raw=sf.read_text(encoding="utf8")
        doc=ET.fromstring(raw)
        assert doc.attrib.get("viewBox")=="0 0 1920 1080",sf
        assert doc.attrib.get("width")=="1920" and doc.attrib.get("height")=="1080",sf
        assert "NOT SOURCE PIXELS" in raw,f"Misleading source semantics {sf}"
        pf=out/(sf.stem+".png")
        if not args.check_only:
            cmd=["inkscape",str(sf),"--export-filename="+str(pf),"--export-width=1920","--export-height=1080"]
            subprocess.run(cmd,check=True,stdout=subprocess.DEVNULL)
            assert pf.exists() and pf.stat().st_size>10000,pf
        reports.append((r["shot_id"],str(sf),str(pf),"STATIC_XML_PASS" if args.check_only else "PNG_RENDER_DONE_MANUAL_QC_PENDING"))
    with (out/"render_receipt.csv").open("w",encoding="utf8",newline="") as f:
        w=csv.writer(f);w.writerow(("shot_id","source_svg","render_png","status"));w.writerows(reports)
    print(f"{len(reports)} editable graphics checked. PNG render {'SKIPPED' if args.check_only else 'DONE'}; manual visual, factual and timing QA still mandatory.")
if __name__=="__main__":run()
