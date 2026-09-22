# Stage 12F — GPT Prompt Pack QA

**PASS**

- Prompts: **115 / 115**
- Prompt uniqueness: **115 / 115**
- Selected physical reference assets missing: **0**
- Every prompt has a style-reference ID: **YES**
- Every prompt reserves bottom 20% for captions: **YES**
- Exact factual on-image text policy: **LOCKED**
- Real-person synthesis prohibition: **LOCKED**
- Fake-document prohibition: **LOCKED**
- Paid generation submitted: **0**
- Credits spent in Stage 12F: **0**
- First-pass budget if all 115 are later authorized: **57.5 credits**
- Stage 13 started: **NO**

## Important correction
Stage 12F does **not** blindly reuse the previous `hero_asset` field. It selects semantic references from the entire physical Stage 12C source pack. This prevents anti-repeat layout logic from assigning an irrelevant hero to a literal beat.

Examples:
- bloody pig mask → authentic `DOJ_FBI_PIG_MASK_AND_BOOK.jpg`
- threatening messages → `DC022_THREATENING_MESSAGES.png`
- Craigslist harassment → `DC021_CRAIGSLIST_HARASSMENT.png`
- obstruction/deletion → `DC023_OBSTRUCTION_DELETION.png`
- GPS attempt → `DC006/DC007` + generic tracker context where useful

## Gate
Stage 12F prompt preparation is complete.
No image generation is authorized by this file.
