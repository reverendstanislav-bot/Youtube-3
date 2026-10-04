# VIDEO 003 — Stage 13K R6 Remaining-50 Hard Visual QC

Status: **QC COMPLETE / 44 PASS / 6 REJECT / NO FURTHER SPEND AUTHORIZED**
Date: **2026-10-04**

Wave:
- generated: **50 / 50**
- model/settings: **Higgsfield GPT Image 2 / 1k / low / 16:9**
- generation failures: **0**
- spend already incurred: **25.0 credits**
- automatic retries: **0**

## Hard visual QC
- **PASS: 44**
- **REJECT: 6**

PASS:
F033, F036, F039, F040, F041, F049, F050, F053, F055, F057, F058, F062, F063, F066, F067, F070, F071, F072, F075, F079, F080, F082, F083, F084, F087, F089, F090, F092, F093, F095, F097, F099, F100, F104, F105, F106, F108, F109, F112, F113, F114, F116, F117, F118

REJECT:
F044, F046, F051, F059, F102, F107

## Reject reasons
- **F044** — generated identifier/code-like copy outside the authentic source crop.
- **F046** — reconstructed synthetic metadata UI/field text.
- **F051** — fabricated code/identifier fragment; not reliably source-native.
- **F059** — synthetic error/status microcopy and pseudo-UI.
- **F102** — labeled three-node flow duplicates/generated node copy instead of unlabeled geometry.
- **F107** — notice/scale beat falls back into a fabricated notice/status card with extra copy.

## Result across the whole 120-frame film
Before this QC:
- PASS locked: **66**
- known rejects: **4**
- awaiting QC: **50**

After this QC:
- newly locked PASS: **44**
- new rejects: **6**
- total PASS locked: **110 / 120**
- total current rejects: **10 / 120**
- never-generated slots: **0**

Current reject set:
**F016, F044, F046, F051, F059, F060, F101, F102, F107, F110**

First-pass final-frame completion rate:
**110 / 120 = 91.7% PASS**

The remaining work is now reject-only repair. At the locked 0.5 credit/image rate, one single regeneration of all 10 rejects would be **5.0 credits**, but this is arithmetic only and **NOT AUTHORIZED**.

No retries or new generation were submitted by this QC.
