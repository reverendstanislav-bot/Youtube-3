# VIDEO006 — Voicebox Harrison generation plan

**Plan only. No TTS job submitted and no audio created.**

## Proposed local configuration

- Application: Voicebox 0.5.0 local API on Windows.
- Model: Qwen3-TTS 0.6B Base using CUDA on the installed NVIDIA RTX 3050 6 GB setup.
- Voice candidate: existing local `Harrison` clone profile `228d3d8a-096f-461b-bf11-4f9415e2dafc`, created from the approved Harrison reference workflow. It remains a candidate implementation of the channel-locked Higgsfield Harrison identity and requires Stage09 listening comparison.
- Input: five files `08_HARRISON_TTS_CHUNK_01.txt` through `05.txt`, submitted in numeric order.
- Proposed jobs: **5 sequential local generation jobs**, one per file; no speculative retries.
- Proposed seed: `20261021` for reproducibility.
- Proposed instruction: “Controlled, curious, factual US investigative documentary narration; precise business and legal language; medium cadence; restrained reveals; no trailer voice, melodrama or sarcasm.”
- Proposed internal maximum text segment: 800 characters; 50 ms crossfade; output normalization enabled.
- Proposed output: mono PCM WAV, retaining the model's native sample rate for lossless Stage09 QC.

## Preliminary cost

Provider/API credits: **$0 / 0 credits** because generation is local in Voicebox. Local GPU time and electricity are not metered as provider credits. The plan is five jobs; any failed-span retry would be a separate owner decision even though local credit cost is zero.

## Required approval and QA boundary

The current request authorizes Stage08 preparation only. Stage09 generation must not start until the owner explicitly authorizes these five local jobs. After generation: decode/hash each WAV, compare ASR/order to all 51 paragraphs, listen for the pronunciation checklist, compare timbre to canonical Harrison, inspect joins/artifacts, and time S01/S04/S05/S07. Stage10 master assembly remains a separate stage.
