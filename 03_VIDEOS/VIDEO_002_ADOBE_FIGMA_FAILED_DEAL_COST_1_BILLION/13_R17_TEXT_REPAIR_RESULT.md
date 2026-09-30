# VIDEO 002 — R17 Garbled-Text Repair + frame fixes

Date: 2026-09-30 · Owner: "делай" · Spend **7 × 0.5 = 3.5 credits**, 0 retries

Owner review found frames whose document text rendered as pseudo-text. Full audit of the 70 pre-R14 frames:

| Severity | Slots | Action |
|---|---|---|
| Heavy (unreadable) | F025, F094, F095 | R17 regenerated |
| Medium (several garbled lines) | F050, F096, F098, F106 | R17 regenerated |
| Header typo | F051 "Autbolity", F086 "paymet" | deterministic header re-render (Segoe UI Bold, sampled colours) |
| Minor (1–2 smudged words in dense body text) | F020, F089, F091, F108, F109 | **left as is** — not in headlines/quotes |

R17 root cause and fix: sources were long, small-type text dumps. Re-prepared 9 **short exact-quote renders** (same method as RV048 R15), uploaded to Higgsfield, frames regenerated. All 7 PASS (`13_R17_RESULTS.csv`); F094 bottom band darkened locally.

F059: the "FINAL" column was an empty dashed box (intended: no final decision exists). Added a "NO FINAL DECISION" label in the channel's Bebas style with red underline.

All swaps are in `15_FINAL_FRAMES_1080P/` + manifest (`r17-text-repair`, `+no-final-decision-label`).
