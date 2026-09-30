# VIDEO 002 — R15 Reject-7 Retry: Results + Hard QC

Date: 2026-09-30 · Owner approval: **YES — 3.5 credits** · Spend: **7 × 0.5 = 3.5 credits** · Automatic retries: 0

Source repair: `RV048_8K_MERGER_AGREEMENT_CROP_R15.png` — deterministic exact-text render of the 8-K Merger Consideration sentence (1600×772, sha256 `6dc71a3bdad0d50405a31f90417165e7ced6171187674a707a9ef1332f04e5e7`), Higgsfield `804a54b8-c960-4cd5-a96c-7cb186097955`. Local file in `WhatItCost_media/002-adobe-figma/12_SOURCE_PREP/`.

- **PASS: 5** — `F013 F033 F043 F048 F074`
- **REJECT: 2**
  - `F012` — paper and last text lines still in the caption band (layout override not followed).
  - `F037` — quote legible but misspelled ("Coprpany Shares").

Cumulative R14 + R15: **38 / 40 PASS**. Preview-backed slots remaining: **2** (F012, F037 keep their locked previews).

Next retry (2 × 0.5 = 1.0 credit): **NOT AUTHORIZED**. Suggested: F012 — shrink the document to the right half with top edge at 8%; F037 — same prompt, one more seed.
