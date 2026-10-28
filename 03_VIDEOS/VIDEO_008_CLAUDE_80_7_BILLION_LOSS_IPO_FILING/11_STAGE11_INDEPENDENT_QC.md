# VIDEO008 Stage11 independent timing audit - 2026-10-28

Reviewer: review_stage11, independent read-only technical critic.

**PASS - timing audit with documented ASR warnings; no unresolved HIGH/BLOCKER.**

- Actual master SHA256: 5cf8cf37bb728e8a50456b08240824eca4a8d03583626519396eca0258a7ad72; PCM16 mono 24000Hz; 23707200 samples; 987.800 seconds.
- 2576 ASR word timestamps within runtime, ordered without overlaps. Two zero-duration points are explicitly retained and flagged.
- 50 canonical paragraphs / 2548 whitespace words; 110 scenes continuously cover frames0-24695 at25fps. Existing scene allocations were preserved.
- Lexical-match score independently recomputed:2463/2695 normalized tokens =91.391%. This is not a semantic correctness score.
- HIGH fixed: SH01 previous133.76s onset clipped first word Four (ASR digit4 at133.66-133.96s). Corrected cut133.36s includes the complete word; its word row is assigned to P008.
- SH04 cut632.48s provides lead-in before the first word at632.80s. All four cut/sample offsets and durations independently verified.
- Planned3s canonical CTA gives total durations20.16 /20.60 /22.76 /22.88s; all below30s. Final exports remain NOT_RENDERED; no rendered-duration certification is claimed.

Ten paragraphs below85% exact lexical matching, two ASR point timestamps (306.10s and484.86s), and P008/P049 visual-boundary caveats are retained. They are ASR/planning limitations, not proof of an audio error. Accepted audio and canonical V5 wording were not altered. Semantic/pronunciation acceptance remains owner listening; this review did not invent a new independent listening or semantic-ASR PASS.

No Resolve calls, new generation, render, scene-boundary changes or downstream stage advancement were performed by this audit. Existing downstream Resolve state remains preserved.
