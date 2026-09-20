# Status Schema

`manifest.yaml` is authoritative. `VIDEO_INDEX.csv` mirrors status/current_stage and CI treats drift as an error.

## Portfolio statuses
- CANDIDATE
- QUALIFIED
- BACKLOG_APPROVED
- READY_FOR_RESEARCH
- IN_PREPARATION
- PREP_COMPLETE
- ASSEMBLY_IN_PROGRESS
- RELEASE_QA
- RELEASE_READY
- SCHEDULED
- PUBLISHED
- ON_HOLD
- CANCELLED
- ARCHIVED

## Stages
- BRIEF
- 00_TOPIC_QUALIFICATION
- 01_EVIDENCE_RESEARCH
- 02_CASE_STORY_MAP
- 03_SCRIPT_V1
- 04_FACT_LEGAL_REVIEW
- 05_SCRIPT_REVISION
- 06_PERFORMANCE_REVIEW
- 07_SCRIPT_LOCK
- 08_VOICE_SCRIPT
- 09_VOICE_QA_LOCK
- 10_AUDIO_MASTER
- 11_TRANSCRIPT_VISUAL_TIMELINE
- 12_VISUAL_SOURCE_GENERATION_PLAN
- 13_VISUAL_ASSET_QC
- 14_GRAPHICS_DOCUMENTS_MUSIC_SFX
- 15_ASSEMBLY_EDIT
- 16_FINAL_FACT_LEGAL_REFRESH
- 17_PACKAGING
- 18_UPLOAD_PREPUBLICATION
- 19_POST_PUBLISH_ANALYTICS

## Transition rule
Only the lead changes status/current_stage. FAIL blocks advancement. A transition requires updated state files and passing audit.

## Cancellation
Cancelled topics keep their folder and video ID. IDs are never recycled.
