# Storage Policy

Git is the control plane, not the raw-media warehouse.

Store in Git:
- Markdown/CSV/YAML/JSON production truth;
- source metadata and links;
- scripts, timelines, claims, QA and manifests;
- prompts and packaging specs;
- small approved reference artifacts when practical;
- storage URIs/checksums for heavy assets.

Do not store in ordinary Git:
- bulk image/video generations;
- long audio/video masters;
- edit caches/projects;
- production archives unless intentionally managed with suitable artifact/LFS storage.

Every heavy episode asset must be represented in `ASSET_MANIFEST.csv`.
