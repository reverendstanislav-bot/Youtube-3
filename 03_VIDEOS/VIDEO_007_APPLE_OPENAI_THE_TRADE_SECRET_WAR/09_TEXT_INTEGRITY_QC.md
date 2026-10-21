# VIDEO007 — Stage09 independent text integrity QC

**Verdict: PASS_INPUT_INTEGRITY — text only. No generation submitted.**

An independent UTF-8 parser extracted the 60 spoken paragraphs from `07_SCRIPT_FINAL.md`, excluding headers, IDs, source notes and Short labels. It then compared those paragraphs with the Stage08 master and five segments.

| Check | Result |
|---|---|
| Canonical spoken paragraphs | 60 |
| Stage08 master paragraphs | 60 |
| Combined segment paragraphs | 60 |
| Canonical vs master text mismatches | 0 |
| Master vs combined-segment mismatches | 0 |
| Missing / duplicated / reordered paragraphs | 0 / 0 / 0 |
| Narration-only source vs master bytes | IDENTICAL |
| Lexical word count | 2,517 |
| Standalone em-dash tokens excluded by locked counting convention | 7 |
| Locked Shorts | exactly 4; IDs and paragraph locations match |

## Segment locks

| Job | File | Paragraphs | Words | Characters | SHA-256 |
|---:|---|---:|---:|---:|---|
| 01 | `08_VOICE_SEGMENT_01.txt` | 9 | 382 | 2,493 | `B81ABA431BFDC15BB1AB91F7F8CFE20BB5725C702B6AF9F5AC470253EE3E4CB8` |
| 02 | `08_VOICE_SEGMENT_02.txt` | 12 | 508 | 3,285 | `C1831CE6985A634575CFFB80E6A6AEF9C0C5F1517B3B386835CA03DA41C67490` |
| 03 | `08_VOICE_SEGMENT_03.txt` | 12 | 506 | 3,411 | `F67BDEEF564594D449E90780C472834627DE7C19C367A0003E382532BCADABE5` |
| 04 | `08_VOICE_SEGMENT_04.txt` | 15 | 585 | 3,946 | `BEEC734EB475E3E758ED3AA173BFBD061580A2764ABE31F5AE8F3BCF1135A4FB` |
| 05 | `08_VOICE_SEGMENT_05.txt` | 12 | 536 | 3,559 | `15FA0F58F39B5B07F6DD916E1E2AF6ED40CE1E09596864AA8A8E277B265DAC4D` |

Each input is under Voicebox's 5,000-character API limit. No locked text file was edited by Stage09 preparation.

## Shorts text check

SH01/A00-P01 = 59 words; SH02/A05-P03 = 63; SH03/A07-P03 = 64; SH04/A09-P03 = 61. Counts match `07_SHORTS_LOCK.csv` when standalone em-dash separator tokens are excluded. Each is one complete source paragraph inside one long-form segment.
