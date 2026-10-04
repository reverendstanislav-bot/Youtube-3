# VIDEO 003 — Stage 11 Transcript + Visual Timeline

Status: **PASS / LOCKED**

Date: **2026-10-04**

## Audio authority

- Master: `VIDEO_003_HARRISON_AUDIO_MASTER.mp3`
- Media ID: `3927e3f3-6b64-4214-8bc0-144d59214b81`
- Runtime: **988.290612 sec / 16:28.291**
- Master SHA-256: `d6f149bc0d24be1f40c766ad3b68adfc94720ea67d547d22906cd963f2d551e8`

All Stage 11 timing derives from this locked master.

## Canonical word alignment

Canonical Stage 07 lexical tokens timed:
**2,392 / 2,392**

Alignment:
- **2,338 / 97.74% DIRECT**
- **54 / 2.26% ALIGNED**

`DIRECT` means the canonical token matched the master ASR token directly.
`ALIGNED` means timing was interpolated monotonically inside neighboring confirmed canonical/ASR anchors.

The ASR wording is never the text authority. The canonical text remains `07_SCRIPT_FINAL.md`.

### Stage 07 metadata reconciliation

Stage 07 R3 metadata previously recorded **2,391** words.
A fresh Stage 11 production-tokenizer pass on the unchanged canonical file returns **2,392 lexical tokens**.

This is an **off-by-one metadata correction only**:
- canonical script text changed: **NO**
- audio changed: **NO**
- legal/factual meaning changed: **NO**
- Shorts text changed: **NO**

Stage 11 downstream timing authority therefore uses **2,392 canonical tokens**.

## Transcript artifacts

Git authority:
- `11_WORD_TRANSCRIPT.csv.gz` — gzip-compressed canonical CSV
- `11_ALIGNMENT_QC.json`

Uncompressed durable mirror:
- `https://d2ol7oe51mr4n9.cloudfront.net/user_3J3zfwu7kpgllQvPySWoLtXHwdR/43d6ffa8-9c7e-4bb5-8e7e-06f8a539686d.csv`

Uncompressed CSV:
- size: **173,989 bytes**
- SHA-256: `7e9c9d3b7b31d5ec80f5b740ea3e643edfa694708ce93327e196e7fb2bfaa0b7`

Columns:
`word_id, section, paragraph, word, start_sec, end_sec, start_timecode, end_timecode, alignment, asr_probability`

## Visual timeline

Canonical timeline:
`11_VISUAL_TIMELINE.csv`

Exact visual beats:
**120**

Timeline SHA-256:
`70e1680bc731f9465119c0fff1e12ed6dc261f98ed1853d81d8bd95be30b8a46`

Timeline design:
- first minute deliberately denser to support R3 retention;
- B001–B010 cover the S01 cold open through **00:00:54.600**;
- B011 begins S02 at **00:00:55.460**;
- remaining beats maintain documentary cadence through the **16:28.291** master;
- nominal full-master cadence: **~8.24 sec per beat**;
- speech-bearing mean beat duration: **7.737 sec**;
- observed speech-bearing range: **3.920–11.020 sec**.

Every beat contains:
- exact master start/end;
- section/paragraph range;
- canonical word range;
- narration excerpt;
- visual objective;
- boundary type.

### Stage 12 boundary

Every beat currently has:
**`route_status = UNASSIGNED_STAGE12`**

Stage 11 does **not** decide:
- real-source assignment;
- document/UI assignment;
- reconstruction assignment;
- GFX assignment;
- image-generation count;
- paid generation spend.

Those belong to Stage 12.

## Shorts cut timing

Canonical timed map:
`11_SHORTS_CUT_MAP.csv`

| Short | Master range | Duration |
|---|---|---:|
| SH01 | 00:00:00.000 → 00:00:54.600 | **54.600 sec** |
| SH02 | 00:00:55.460 → 00:01:47.880 | **52.420 sec** |
| SH03 | 00:02:19.200 → 00:03:13.420 | **54.220 sec** |
| SH04 | 00:03:55.920 → 00:04:41.660 | **45.740 sec** |
| SH05 | 00:05:25.400 → 00:06:13.800 | **48.400 sec** |
| SH06 | 00:06:52.020 → 00:07:38.800 | **46.780 sec** |
| SH07 | 00:08:31.400 → 00:09:16.360 | **44.960 sec** |
| SH08 | 00:09:55.060 → 00:10:47.500 | **52.440 sec** |

Result:
**8 / 8 TIMED_LOCKED**

Rules preserved:
- contiguous master extraction only;
- no rewrite;
- no reorder;
- no stitching distant lines;
- same audio/story for 9:16 reframe;
- Stage 07 legal isolation remains authoritative.

## Stage 11 QA result

**PASS**

- master authority: PASS
- 2,392/2,392 canonical tokens timed
- monotonic word timing: PASS
- direct alignment: 97.74%
- 120/120 visual beats timed
- first-minute density lock: PASS
- 8/8 Shorts timed
- all Shorts < 60 sec
- Stage 12 routing not pre-empted
- paid generation: **0**
- new credits: **0**

## Stage boundary

**STOP.**

Next:
**Stage 12 — Visual Source / Generation Plan**, only on explicit owner instruction.
