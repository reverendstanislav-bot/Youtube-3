# Legal Status Schema

Allowed `legal_status` values for material claims/events:
- ALLEGATION
- COMPLAINT
- CLAIM
- CHARGE
- RULING
- VERDICT
- SETTLEMENT
- DISMISSAL
- CONVICTION
- ADMISSION
- DENIAL
- UNDISPUTED_FACT
- REPORTED_FACT
- OPINION
- ANALYSIS
- UNKNOWN_REQUIRES_REVIEW

## Invariants
1. COMPLAINT/ALLEGATION/CLAIM/CHARGE never equal established guilt/liability.
2. SETTLEMENT never equals admission unless explicitly supported.
3. DISMISSAL records scope, prejudice status when material, and procedural basis when known.
4. RULING/VERDICT records exactly what issue/count was resolved and later appeal/post-trial status when material.
5. CONVICTION records plea/verdict and current procedural posture.
6. UNKNOWN_REQUIRES_REVIEW is blocking for material script claims.

## Promotion
A claim may move to a stronger status only when a new source/event justifies it. Preserve the historical event in CASE_EVENT_LEDGER rather than rewriting chronology.
