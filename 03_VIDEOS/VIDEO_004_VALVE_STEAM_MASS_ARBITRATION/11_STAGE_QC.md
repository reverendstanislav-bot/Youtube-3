# VIDEO004 — Stage10/11 bounded independent review

2026-10-10. No audio listening claimed.

## Independent reviewers

v08_precision: PASS_PROVENANCE; PASS_ASR_COVERAGE_WITH_REVIEW_FLAGS. Checked all3source hashes, master hash/runtime, nearly identical decoded source/master signal, unchanged exact TTS payload hashes, full recognized text and8Short ranges. Substantive dates/counts/negations/attribution/preliminary-as-applied and conditional appeal recognized. Eight candidate lexical anomalies identified, not classified as TTS errors.

review_correction: PASS_PROVISIONAL_STAGE11_PREPARATION; NOT_STAGE11_LOCK / NOT_AUDIO_PASS. Checked123narrationcue spans plus20splannedend screen,54authoredbeats, all8Shorts in isolation, every timeline frame boundary, source classes, all5input hashes, cut lengths18.18–21.66s with3sCTA. No proved creative/legal/text-extract defect.

Reviewed structural hashes:
-11_ALIGNMENT_QC.json:c1fe0eadc895384db9b48f170f446fec22b0f8d04941d0911f5d182fd2597189
-SCENE_TIMELINE.csv:32174510dc3795529fbc147f2efa6d0d81ddb1b05619c5bce474c0d9379872ae
-11_SHORTS_CUT_MAP.csv:5656d4b22e428324d06cf9721e54e81d941008e4ac1fcd68e701d936448e5856

## Supplementary medium.en recheck

Eight original small.en anomaly windows were re-recognized locally with medium.en; full results retained in11_ASR_MEDIUM_RECHECK.json. It recognizes purchased and question, omits the five phantom extra words, and recognizes stop at734.880–735.120s with0.99894modelprobability. All8candidate locations support the locked source wording in the second model. Clip edges contain incomplete outside-context words and are not canonical narration. No hidden raw transcript rewriting or invented timing. Neither model establishes genuine hearing or phonetic certainty.

20literal alignment differences include formatting/tokenization differences (counts split across ASR words, dollar notation, possessives, hyphens, date ordinal, vs/dash) and the8lexical flags. Do not turn the literal token-match rate98.7587% into a semantic accuracy score. The44sub-50ms word spans and44low-confidence rows remain visible; this provisional word stream is not approved for captions.

## Open acceptance issues

HIGH | AUDIO_GATE | Full808smaster | No genuine auditory review of pronunciation, timbre, cadence or join noise | Listen full hashed master; record actual reviewer and verdict. No newgeneration authorized.

HIGH | ANCHORS | S05:p9 around271.24–273.76s and all meaningful ASR discrepancies | The initial Valve's token is unmatched in first-model alignment | Confirm audible paragraph start and classification; revise anchor from evidence, not equal-time interpolation.

MEDIUM | SHORT_EDGES | SH05out359.960; SH06in415.300; SH07in467.600; SH08in627.640 | No ASR silence budget at adjacent-word edge | Audition all8fullcuts plus3sCTA; avoid clipped syllables/borrowed adjacent speech; revise within natural silence and recheck. No speedup/rewrite.

No Stage10audio lock, Stage11lock, Stage12asset/provenance PASS, export-duration PASS, picture/edit QC or release PASS. Lead accepts only the provisional preparation verdict and retains bothlocksfalse.
