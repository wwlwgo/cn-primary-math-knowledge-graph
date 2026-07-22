#!/usr/bin/env python3
"""Ensure every unresolved cross-edition diagnostic node has one review item."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def main() -> int:
    nodes = json.loads((DATA / "cross_edition_node_evidence.json").read_text(encoding="utf-8"))
    queue = json.loads((DATA / "review_queue.json").read_text(encoding="utf-8"))
    expected = {item["topicId"] for item in nodes if item["editionB"] != "located"}
    actual = [item.get("topicId") for item in queue]
    errors = []
    if len(actual) != len(set(actual)):
        errors.append("review_queue.json 包含重复 topicId")
    if set(actual) != expected:
        errors.append("review_queue.json 与节点证据中的未解决项目不一致")
    for item in queue:
        if item.get("reviewType") not in {"page-confirmation", "scope-expansion"}:
            errors.append(f"{item.get('topicId')}: reviewType 无效")
        if item.get("priority") not in {"high", "normal"}:
            errors.append(f"{item.get('topicId')}: priority 无效")
        if item.get("status") != "open":
            errors.append(f"{item.get('topicId')}: 初始状态必须为 open")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"OK: {len(queue)} 个待复核节点均已入队。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
