# VIDEO 002 — R11 Reject16 Hard Binary QC

Date: 2026-09-29

## Result
- Frames audited: **16 / 16**
- PASS: **11**
- REJECT: **5**
- Existing usable PASS before R11 retry: **94**
- Total usable PASS now: **105 / 110**
- Remaining without PASS: **5 / 110**
- Additional retry spend during QC: **0 credits**
- Automatic retries launched: **0**

## PASS
`F007, F011, F051, F053, F062, F063, F073, F093, F095, F100, F105`

## REJECT
- **F010** — SUBTITLE_SAFE_REJECT: the light Figma/Adobe UI evidence extends materially below the 85% line; source-native controls/text sit inside the bottom 15%, creating a real collision/readability problem for baked captions.
- **F054** — SUBTITLE_SAFE_REJECT: the second headline line PRODUCT-DESIGN CAPABILITIES sits inside the bottom 15%, causing a direct caption collision.
- **F059** — SUBTITLE_SAFE_REJECT: the EC document continues with source-native body text below the 85% line, so captions would cover evidence text.
- **F061** — SUBTITLE_SAFE_REJECT: the headline PRODUCTS WERE COMPLEMENTARY extends deep into the bottom 15%, causing a direct caption collision.
- **F104** — SUBTITLE_SAFE_REJECT: both bright CMA document sheets extend materially into the bottom 15%; white/orange captions would overlap bright paper and partially cover evidence.

## Notes
All five rejects are **composition / subtitle-safe failures**, not source-repair failures. Their repaired references are valid and should remain locked for any later retry.

No paid retry is authorized by this QC pass.
