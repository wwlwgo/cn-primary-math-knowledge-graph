#!/usr/bin/env python3
"""Run simple reproducible queries against the published knowledge graph."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def load(name: str):
    with (DATA / name).open(encoding="utf-8") as file:
        return json.load(file)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for command in ("prerequisites", "unlocks"):
        subparser = commands.add_parser(command)
        subparser.add_argument("topic_id")
        subparser.add_argument("--recursive", action="store_true")
    grade = commands.add_parser("grade")
    grade.add_argument("grade_band", choices=["G1", "G2", "G3", "G4", "G5", "G6"])
    args = parser.parse_args()

    topics = {topic["id"]: topic for topic in load("topics.json")}
    dependencies = load("dependencies.json")
    if args.command == "grade":
        result = [topic for topic in topics.values() if args.grade_band in topic["gradeBands"]]
    else:
        relation = defaultdict(list)
        for dependency in dependencies:
            key = dependency["topicId"] if args.command == "prerequisites" else dependency["prerequisiteId"]
            value = dependency["prerequisiteId"] if args.command == "prerequisites" else dependency["topicId"]
            relation[key].append((value, dependency["strength"]))
        if args.topic_id not in topics:
            parser.error(f"未知 topic_id: {args.topic_id}")
        pending = list(relation[args.topic_id])
        seen = set()
        result = []
        while pending:
            topic_id, strength = pending.pop(0)
            if topic_id in seen:
                continue
            seen.add(topic_id)
            result.append({"id": topic_id, "name": topics[topic_id]["name"], "strength": strength})
            if args.recursive:
                pending.extend(relation[topic_id])

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
