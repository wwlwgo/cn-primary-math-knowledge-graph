#!/usr/bin/env python3
"""Reject private textbook material from a candidate release tree."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
# Private textbook inputs are intentionally present in a maintainer worktree
# but must be excluded from the public release-tree scan.
EXCLUDED_DIRS = {".git", "教材", "人教版", "__pycache__"}
FORBIDDEN_SUFFIXES = {".pdf", ".epub", ".mobi"}
FORBIDDEN_PATH_PARTS = {"ocr", "private"}


def main() -> int:
    violations: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        parts = set(relative.parts)
        if parts & EXCLUDED_DIRS:
            continue
        if path.suffix.lower() in FORBIDDEN_SUFFIXES or parts & FORBIDDEN_PATH_PARTS:
            violations.append(str(relative))
    if violations:
        print("ERROR: 发布树包含受限文件：")
        for item in violations:
            print(f"- {item}")
        return 1
    print("OK: 发布树未发现教材、OCR 或私有输入文件。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
