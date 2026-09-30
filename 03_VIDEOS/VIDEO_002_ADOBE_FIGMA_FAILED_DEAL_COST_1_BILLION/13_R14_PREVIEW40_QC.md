# VIDEO 002 — R14 Preview-40 Regeneration: Results + Hard QC

Date: 2026-09-30
Owner approval: **YES — regenerate the 40 preview-only slots in Higgsfield at 1k**

- Submitted / completed: **40 / 40**, 0 failures
- Model: **Higgsfield GPT Image 2 / 1k / low / 16:9** — output **1344×752**
- Higgsfield project: `9bad6370-d0ed-4bbd-94f5-29a9786baedb`
- Spend: **40 × 0.5 = 20.0 credits**
- Automatic retries: **0**
- Local copies: `WhatItCost_media/002-adobe-figma/13_R14_RESULTS/F###.png`
- Results: `13_R14_PREVIEW40_RESULTS.csv` · QC ledger: `13_R14_PREVIEW40_QC.csv`

## Hard QC

- **PASS: 33**
- **REJECT: 7** — `F012 F013 F033 F037 F043 F048 F074`

| Slot | Failure | Fix for a retry |
|---|---|---|
| F012, F074 | Document text / paper enters the bottom 15% caption band | Layout-only retry (R12/R13 pattern) |
| F013, F033, F037, F048 | 8-K body text garbled into pseudo-text | Root cause is the R14 source prep: `RV048_8K_MERGER_AGREEMENT_CROP.png` is 2200×630 with small type. Re-crop to the Merger Consideration paragraph only, larger type (like the deterministic RV049/RV050 renders), re-upload, then retry |
| F043 | Model added a CMA logo absent from the crop | Retry with explicit "no logo, no emblem" line |

Notes: F021 PASS but the RV012 portrait is not shown — the canonical R9 prompt's SOURCE ROLE says "none", so this is a prompt conflict, not a model failure. F016 paper edge dips marginally below the 85% line with no text in the band (PASS, practically clear).

## Effect on the frame set

For the 33 PASS slots the new 1344×752 frame replaces the 960×540 recovery preview. For the 7 REJECT slots the existing locked preview remains the fallback. Preview-backed slots: **40 → 7**.

Retry cost if approved: 7 × 0.5 = **3.5 credits**. **Not authorized.**
