# VIDEO005 — Stage11 Alignment / Timeline QA

**2026-10-14 | PASS_STRUCTURAL_FRAME_COVERAGE — ASR TIMING PROVISIONAL.**

**Source & master integrity:** Stage07 V4.4 55 unchanged spoken paragraphs and Stage08 2,627 normalized word tokens. Real Stage10 audio master SHA256 `0db92584d7eddd70914b800cb981250463d222cc4db1245444a8153c782847a0`, exactly 995.03s. Source chunk offsets from Stage10 build manifest 0.00 / 192.24 / 419.95 / 609.39 / 807.71sec, with 4 ×0.12s inter-chunk pauses.

**Transcript:** 2,627 word slots, 2,451 direct ASR anchors, 176 interpolated unmatched slots (6.7%). Word timing columns explicitly identify method; the unanchored rows do **NOT** pass exact timestamp QA. A sample word record includes spoken token, paragraph, chunk, start/end seconds and `ASR_EXACT_TOKEN_ANCHOR` or `ASR_INTERPOLATED_UNMATCHED_TOKEN`. Script order is unchanged. Five recognized audio chunks and all 55 parent speech paragraphs are present.

**Paragraph boundary review:** 48 paragraphs have both first and last word directly anchored with sufficient exact-match coverage. Seven need a timed listen: `A04-P01`, `A04-P03`, `A06-P03`, `A07-P02`, `A07-P05`, `A07-P06`, `A08-P06`. These are weak ASR boundary anchors, not established omissions/voice errors.

**Scene coverage:** 55 narrative cues, 110 proposed 25fps visuals; frame boundaries continuously partition frame indices 0..24,875. No gaps/overlaps. Frame-exact 995.04s visual canvas includes +0.01s harmless padding beyond 995.03s WAV; no hidden added speech.

**Shorts:** Exactly S01=A00-P01, S03=A02-P03, S05=A04-P03, S08=A08-P04; provisional source cut times and 3s end-card plan fit under 30s arithmetically. No Short exports generated. S05 word ending requires listen; all actual cuts/CTA duration still Stage15 QC.

**Visual and legal:** Provenance class is a proposal, not acquired rights or a real document. Do not invent court pages, money transfer screenshots, product-use verdicts, or disclosure of sealed payments. Stage12 must source/lock each visual. No burned automatic speech captions in visual assets.

**Acceptance boundary:** Stage11 evidence/structure/usable edit cues **PASS**. Subtitle word timings, final Short cuts, pronunciation and visuals remain **NOT LOCKED**. Stage12 can proceed with explicit caveats; Stage15 must recheck exact finished exports before publishing.

`11_ALIGNMENT_QC.json` is the machine-readable authoritative numeric QC ledger.