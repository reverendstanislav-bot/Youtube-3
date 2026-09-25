# VIDEO 002 — Stage 12A-R2 Prompt Rules (VIDEO 001 R7 style parity)

Status: **LOCKED / NO SPEND**
Date: 2026-09-25
Supersedes: `12A_PROMPT_RULES.md` and `12A_HIGGSFIELD_PROMPTS_001_030/031_060/061_085.csv` (kept as history).

## Why R2 exists
Owner instruction: VIDEO 002 generated frames must look like VIDEO 001. The v17 pack diverged from the VIDEO 001 final (R7) grammar in three ways:
1. **No in-frame headline.** v17 forbade all generated text; VIDEO 001 R7 frames carry the locked headline inside the frame (off-white distressed condensed headline + restrained red underline). R7 result: 61/61 final jobs QC PASS with in-frame headlines.
2. **Section-level families.** v17 applied one family per section, producing 43 three-in-a-row family runs. R7 assigns a family per beat by content.
3. **Abstract inputs.** v17 attached source files to only 26/85 frames; 59 were abstract folder/tab compositions — the pattern that caused VIDEO 001 R7 `HOLD_SOURCE_MISMATCH` rejects.

## R2 production model
- Provider/model: **Higgsfield GPT Image 2 — 1k, low quality, 16:9, 0.5 credit/job** (VIDEO 001 R7 settings).
- Prompt structure: VIDEO 001 R7 one-pass standard, verbatim blocks — STYLE, LAYOUT (T01/T02/T03/T04/T06/T07), SOURCE FIDELITY, SUBTITLE SAFE, ONE-PASS RULES — plus a beat-specific SCENE line.
- Generated text: **exactly one block per frame = the locked v17 editor-overlay headline, unchanged**. No other readable words. R2 did not rewrite any headline.
- Inputs: 81/85 frames attach prepared files from `12A_R2_SOURCE_PREP_QUEUE.csv` (41 prep items / 40 Stage01B assets). 4 frames (G013, G018, G020, G064) are deliberately input-free conceptual beats built from blank paper objects only.
- Documents enter only as tight authentic crops rendered from the official source (`12_SOURCE_PREP/`); raw PDF/HTML is never attached.
- Real-person photos (8 frames) carry a PERSON PHOTO LOCK; no likeness synthesis.
- HOLD_RIGHTS assets used: **0**.

## Adjacency rules applied
- No three consecutive generated timeline beats share a family (authentic/GFX beats counted as their own route).
- No identical document crop on two consecutive timeline beats (incl. adjacent 12B/12C authentic beats).

## Stage 13 QC additions (inherited from VIDEO 001)
- Headline spelling must match `exact_text` exactly; a misspelled headline is **EDIT_FIX** (deterministic Bebas Neue cover, VIDEO 001 B104 precedent), not an automatic regen.
- Any attached document crop whose text the model altered = **EDIT_FIX** (composite the authentic crop) or REGEN on owner approval.
- Any altered face in a person-lock frame = EDIT_FIX (composite the unchanged photo) or REGEN on owner approval.

## Spend
85 jobs × 0.5 = **42.5 credits** (unchanged). R2 authorizes **0 jobs, 0 retries, 0 credits**. Source prep (`12_SOURCE_PREP/`) must be completed before generation.
