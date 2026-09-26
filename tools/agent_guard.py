#!/usr/bin/env python3
"""PreToolUse guard for subagents: allow Write/Edit only to the given path globs.

Used from agent frontmatter:
  python "$CLAUDE_PROJECT_DIR/tools/agent_guard.py" "videos/*/2_script/review_critic.md" ...
Globs are relative to the repo root; `*` also matches `/`.
"""
from __future__ import annotations

import fnmatch
import json
import os
import sys
from pathlib import Path


def deny(reason: str) -> None:
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": reason}}))
    sys.exit(0)


def main() -> None:
    allowed = sys.argv[1:]
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        deny("guard: unreadable hook input")
    path = (data.get("tool_input") or {}).get("file_path") or (data.get("tool_input") or {}).get("notebook_path")
    if not path:
        return
    root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or ".").resolve()
    target = Path(path)
    if not target.is_absolute():
        target = Path(data.get("cwd") or root) / target
    try:
        rel = target.resolve().relative_to(root).as_posix()
    except ValueError:
        deny(f"guard: {path} is outside the repository. Allowed: {', '.join(allowed)}")
    if any(fnmatch.fnmatch(rel, g) for g in allowed):
        return
    deny(f"guard: this agent may only write {', '.join(allowed)} — not {rel}. Stay in your task.")


if __name__ == "__main__":
    main()
