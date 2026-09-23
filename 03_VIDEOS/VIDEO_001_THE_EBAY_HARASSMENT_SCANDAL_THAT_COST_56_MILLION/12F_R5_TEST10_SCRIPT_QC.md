# Stage 12F-R5 — Test10 Script QC

Status: **PARTIAL PASS — DO NOT SCALE YET**

Scope:
B001, B004, B006, B007, B008, B018, B024, B034, B041, B062

## Result
- PASS: **5**
- EDIT_FIX: **3**
- REGEN: **2**
- total checked: **10 / 10**
- additional generation during QC: **0**
- additional spend during QC: **0**

## Per-beat verdict

### B001 — PASS
**Script:** In August twenty nineteen, a couple in Massachusetts began receiving things that made no sense.

Massachusetts/location/date frame correctly establishes place and time before escalation.

**Visual:** Map + two real Massachusetts/Natick context images; headline matches beat; lower caption band is quiet.

**Action:** Keep as R5 reference-quality map/location frame.

### B004 — PASS
**Script:** A bloody pig mask.

Authentic DOJ/FBI pig-mask image is the dominant subject and directly matches narration.

**Visual:** Headline and evidence image are immediately readable; style matches owner-approved evidence reference; subtitle band stays clear.

**Action:** Keep.

### B006 — PASS
**Script:** They worked in, or with, the security organization of eBay.

Real eBay corporate/security context makes the corporate-origin reveal clear.

**Visual:** eBay HQ is visible; supporting interior image adds security/organization feel; clean caption band.

**Action:** Keep.

### B007 — EDIT_FIX
**Script:** All seven former employees and contractors who were federally prosecuted over the campaign later pleaded guilty.

Core message is correct, but the supporting source page is too text-dense for a montage-ready frame and risks generated/re-rendered microtext.

**Visual:** Headline is strong; source should be reduced to one authentic highlighted excerpt instead of a full dense page.

**Action:** Tighten prompt/source crop; do not use full-page body text in final frame.

### B008 — EDIT_FIX
**Script:** eBay entered a deferred prosecution agreement, admitted facts, paid a $3M criminal penalty, and accepted an independent compliance monitor.

Scene meaning is correct and the $3M/monitor hierarchy works, but the right-side DPA treatment still carries too much small legal text.

**Visual:** Good overall composition and eBay context; source panel should be one short authentic excerpt/label, not multiple tiny paragraphs.

**Action:** Keep layout; tighten source crop and legal microtext before scaling R5 money/DPA frames.

### B018 — REGEN
**Script:** His words were: “We are going to crush this lady.”

Wrong visual emphasis: pig-mask evidence dominates a beat that should be about the exact internal-message quote.

**Visual:** Style reference content contaminated the scene and introduced unrelated harassment imagery.

**Action:** Regenerate with quote/message source as hero; style reference must control look only and must not contribute pig-mask content.

### B024 — EDIT_FIX
**Script:** Another executive relationship was pulling the issue toward security too.

The eBay/security transition reads, but the clipped 'legal status' note is semantically weak and the frame does not visually communicate the executive-relationship aspect well enough.

**Visual:** HQ source is useful; side note feels inherited from style reference rather than this beat.

**Action:** Replace generic legal-status note with a scene-specific executive/security cue; preserve overall dossier layout.

### B034 — PASS
**Script:** The Steiners began receiving threatening online messages and disturbing deliveries. The admitted record includes live insects and a bloody pig mask.

The frame successfully combines the three required evidence categories without losing hierarchy.

**Visual:** Threatening-message excerpt, insects, and pig-mask source are all visible; clear headline stack; no horror over-stylization; caption area is clean.

**Action:** Keep as model for multi-source evidence composites.

### B041 — REGEN
**Script:** It had become a physical surveillance operation. And the next day, the Steiners went to the police.

Current frame reads mainly as GPS tracking/location and does not show the police/investigation pivot in the narration.

**Visual:** Tracker image repeats the preceding GPS idea; missing police/investigation cue makes the beat semantically late/early at once.

**Action:** Rebind to surveillance + Natick/police/investigation context; remove tracker as hero.

### B062 — PASS
**Script:** The company admitted a detailed factual account of the conduct. It agreed to pay a three-million-dollar criminal penalty.

The $3M consequence is clear and the eBay/DPA source context supports the narration.

**Visual:** Strong money hierarchy, source-backed company context, quiet subtitle band; no misleading 'conviction' claim.

**Action:** Keep; use as reference for later money/legal consequence frames, while keeping source excerpts short.

## System conclusions

### What R5 fixed
- Subtitle-safe lower area is materially better across the test set.
- Source-based composition is now visible in the finished frames instead of blank placeholder plates.
- The three approved channel style references create one recognizable visual family.
- B001, B004, B006, B034 and B062 show that the system can vary map, evidence, corporate, multi-source evidence and money frames without leaving the channel style.

### Remaining systemic problem
**Style-reference content leakage.**
A style reference must control composition/material language only. It must never donate its factual subject to another beat.

B018 is the clearest failure: the pig-mask subject from the evidence style family contaminated a quote scene whose script is only the internal message.

### Secondary problem
Some legal/accountability frames still carry too much small source text:
- B007
- B008

For those families, future prompts must require a **tight authentic excerpt crop** rather than an entire readable page/panel.

### Script/source problem
B041 demonstrates that correct style is not enough: the frame must follow the exact narration transition. A GPS-heavy image belongs to the preceding tracker beat; this beat needs physical surveillance + police/investigation pivot.

## Gate
R5 is **not yet cleared for 115-frame production**.

Before scaling:
1. fix the R5 prompt rules for style-reference content leakage;
2. tighten legal/document source cropping;
3. correct B041 source binding;
4. regenerate only the hard rejects after explicit owner approval.
