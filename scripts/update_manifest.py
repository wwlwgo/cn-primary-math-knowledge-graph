#!/usr/bin/env python3
"""Refresh dataset counts and SHA-256 checksums after a dataset edit."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
FILES = ("topics.json", "dependencies.json", "standards.json")


def load(name: str):
    with (DATA / name).open(encoding="utf-8") as file:
        return json.load(file)


def main() -> None:
    manifest_path = DATA / "manifest.json"
    manifest = load("manifest.json")
    topics = load("topics.json")
    dependencies = load("dependencies.json")
    standards = load("standards.json")
    manifest["counts"] = {
        "topics": len(topics),
        "dependencies": len(dependencies),
        "standards": len(standards),
    }
    manifest["files"] = {
        name: {"sha256": hashlib.sha256((DATA / name).read_bytes()).hexdigest()}
        for name in FILES
    }
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print("Updated data/manifest.json")


if __name__ == "__main__":
    main()
