# VIDEO 005 — Five owner-approved GENERATED_ILLUSTRATION stills

**Visual approval 5/5; 2026-10-16. Technical/final Stage13 QC is separate.**

These five specific full-frame images are owner-approved visual choices. VP100 specifically selects the **original** `late_night_financial_desk.png` shown again by the user; the later receipt-roll versions were rejected. The reattached VP100 has identical RGB pixels to the approved original.

- V005-VP043 (SC022): `macro_circuit_board_glow.png`, SHA256 `a6c259033414a1e7e5ca163921187017dadae94e924da074bedc10ddb3bd91ea`, 1672×941, **OWNER VISUAL PASS**.
- V005-VP046 (SC023): `cinematic_electronics_workshop_bench.png`, SHA256 `21af5b709713876cb1f91a5363dd11db65eaf9a582beccaa41d4abaf557d64f9`, 1672×941, **OWNER VISUAL PASS**.
- V005-VP076 (SC038): `glass_and_steel_under_tension.png`, SHA256 `a0dbd3e8d1b53e4ae88ac29eb0fbc22dfdc42e2375c0f67774daae1b427657ff`, 1672×941, **OWNER VISUAL PASS**.
- V005-VP090 (SC045): `sunset_boardroom_negotiations.png`, SHA256 `ad3f2f4fe1368294bce8d37c2288134051b59800ed43d91e70c9856087184422`, 1672×941, **OWNER VISUAL PASS**.
- V005-VP100 (SC050): `late_night_financial_desk.png`, SHA256 `98f84c6681c5cc889d2345f64b85f8972dc06d97c3d8870e35632ee57eb84551`, 1672×941, **OWNER VISUAL PASS**.

## Binary handoff

**The GitHub repository does not yet contain these PNG files**. The manifest and Stage13 visual QC now record their approval and full SHA256, but the actual image file bytes still need committing. Do not treat GitHub metadata alone as image upload.

User-facing package: `VIDEO005_AI_STILL_LAST5_OWNER_PASS_ORIGINALS.zip` SHA256 `d84a805099add887b4e5a48aa6dcf159bc4e6971f91afb98e31493e3dea2ac67`. Contains the five exact originals in `originals/` named by asset ID. In Codex: unpack, verify each checksum above, `git add` the original PNGs under `13_AI_STILL_APPROVED_ORIGINALS/`, commit, and update `ASSET_MANIFEST.csv` storage_uri only once GitHub truly contains the images. No image modifications in the source archive.

Master requirement remains 1920×1080, with no invented source documentation, no fake numerical totals, with visual QC and final source/technical gates before overall Stage13 PASS. The separate 60 EDITOR GFX pipeline is not affected.
