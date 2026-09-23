# Stage 12F-R5 — 115-Prompt Preflight QA

Status: **PASS FOR OWNER PROMPT REVIEW — GENERATION NOT AUTHORIZED**

- prompts built: **115 / 115**
- prompts with bound source attachments: **115 / 115**
- prompts with Higgsfield style media ID: **115 / 115**
- prompts with source-prep instruction: **115 / 115**
- prompts with subtitle-safe instruction: **115 / 115**
- prompts with forbidden-failure block: **115 / 115**
- prompt QA failures: **0**
- paid jobs submitted: **0**
- credits spent: **0**

## Key fixes versus rejected pipeline
- Each prompt now says exactly what to attach before the job.
- Text-heavy PDF/HTML sources are explicitly pre-cropped; raw dense pages are not fed blindly.
- Source material must already appear in the generated/final frame — no blank slots and no later material insertion pass.
- The owner-provided Evidence / Map / Dossier images are now stable Higgsfield style references with media IDs.
- Subtitle area is expanded from the minimum 20% lock to a target 22% visually quiet band.
- Variation is built into composition and thematic elements while palette/type/source grammar stay unified.
- No prompt is marked generation-authorized; owner review remains the gate.

## Prompt package
Canonical future prompt file: `12F_R5_HIGGSFIELD_PROMPTS.csv`.
R4 remains the semantic/source audit basis; R5 supersedes R4 only for prompt wording/execution.
