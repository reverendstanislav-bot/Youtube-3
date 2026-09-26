# WeftCut brand motifs — WHAT IT COST

Installed in WeftCut as motifs (`add_motif_layer`). Sources here use font placeholders; fonts live in
`C:/Users/KK/Documents/WhatItCost_media/_fonts/` (not in git, OFL licensed).

| Motif id | Use | Key props |
|---|---|---|
| `wic-captions-16-9` | long-form captions, active word red; ONE layer spanning the whole video | `words_json` = `[{"w","s","e"}]` seconds relative to layer start, `offset_s`, `font_size` 46, `max_chars` 53, `bottom_px` 46 |
| `wic-captions-9-16` | Shorts captions (1080×1920) | same; defaults 64 px, 24 chars, `bottom_px` 440 |
| `wic-headline` | frame headline + red underline + support line | `headline` (`*word*` = red), `support`, `align`, `v_pos` top/middle, `size` |
| `wic-source-label` | small source tag with red tab | `text` e.g. `COURT RECORD · D. MASS. · 2020`, `corner` |
| `wic-status-tag` | legal status box (NOT A JUDGMENT, ALLEGED, CHARGED…) | `text`, `x_pct`, `y_pct`, `size`, `tone` red/white |
| `wic-money` | count-up amount + label + caveat | `amount`, `decimals`, `prefix`, `suffix`, `label`, `caveat`, `count_up`, `align`, `amount_color` |
| `wic-lower-third` | person name / role / legal status, above subtitle zone | `name`, `role`, `status`, `side` |
| `wic-card` | chapter or date card, solid dark or transparent | `kicker`, `title`, `sub`, `background`, `align` |
| `wic-quote` | verified quote in EB Garamond italic | `quote` (`*words*` = red), `attribution`, `background`, `size` |

All 16:9 motifs keep the bottom 20% (Y 864–1080) free.

## Edit a motif
1. `get_motif_source <id>` → change HTML keeping `__WIC_*__` placeholders → `write_motif_draft { from: <id> }`.
2. `python tools/wic_motifs.py inject <draft_id>` (embeds fonts on disk).
3. `preview_motif_draft` → `install_motif { mode: "update" }`.
4. `python tools/wic_motifs.py export <id> <id>` → commit `weftcut/motifs/<id>.html`.

## Assembly
`python tools/yt.py weftcut-plan <id>` turns `beats.csv` (`asset_file`, `motion`, `motif`, `motif_props`) + narration + `words.json` into `5_edit/weftcut_plan.json`; the `assembler` agent executes it (tracks: A NARRATION, V1 PICTURE, V2 GRAPHICS, captions on top). The owner exports the mp4 from WeftCut.

## Captions from a transcript
`transcribe_clip` on the narration → convert words to `[{"w","s","e"}]` (seconds, relative to the caption layer start) → one `wic-captions-16-9` layer over the full runtime. Shorts: slice the same words for the Short's range, `offset_s` = range start.
