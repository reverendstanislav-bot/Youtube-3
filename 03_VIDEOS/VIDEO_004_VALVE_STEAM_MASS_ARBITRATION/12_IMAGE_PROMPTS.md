# VIDEO004 — full-frame image specification routing

Current source of truth: `12_GENERATION_PLAN_V4.json`. This mandatory Stage12 entrypoint intentionally does not duplicate or silently rewrite the already reviewed frame specifications.

For a chosen GF-ID use **all** `common_direction` plus that asset's exact `visible_text`, `direction`, provenance label and constraints; use V5 `viewer_focus_ru`/`cut_reason_ru` only as editorial context, never as extra visible copy. The generation request must explicitly keep its English text inside the generated frame; no later text-overlay workaround.

Inventory:60 total image slots.51 are non-documentary compositions (50narrative +1endscreen);9documentary recreations use `12_RECONSTRUCTION_PROMPTS.md`. The count is not51+60. Each unique GF-ID is one required successful still; reuse does not create another request.

No provider/model request or job payload is prepared/submitted here. Provider requested by owner: Higgsfield. Exact model/capabilities/price and permitted job count still require preflight and explicit spend authorization. No optional variants, speculative tests or retry budget inferred.

For edit timing use `12_FILM_EDIT_MAP_V5.csv`; for actual generation status use `12_GENERATION_ASSET_MANIFEST_V4.csv` (NOT_SUBMITTED). English editorial labels are not burned narration captions. Lower20% remains free of essential content. All actual lettering, mobile readability and endscreen geometry await image/Studio QC.
