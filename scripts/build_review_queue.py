#!/usr/bin/env python3
"""Build the phase 5.3 page-review and community-review queue."""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOCS = ROOT / "docs/review"


def main() -> None:
    nodes = json.loads((DATA / "cross_edition_node_evidence.json").read_text(encoding="utf-8"))
    topics = {item["id"]: item for item in json.loads((DATA / "topics.json").read_text(encoding="utf-8"))}
    queue = []
    for item in nodes:
        status = item["editionB"]
        if status == "located":
            continue
        topic = topics[item["topicId"]]
        review_type = "page-confirmation" if status == "likely-located-needs-page-check" else "scope-expansion"
        priority = "high" if topic["domain"] == "图形与几何" or topic["type"] in {"CONCEPTUAL", "REPRESENTATIONAL"} else "normal"
        queue.append({
            "topicId": topic["id"],
            "capabilityAnchor": topic["capabilityAnchor"],
            "reviewType": review_type,
            "priority": priority,
            "question": "在 edition-b 的五册私有范围内，是否存在可直接支持该可诊断目标的页面？" if review_type == "page-confirmation" else "在当前五册范围外是否需要继续检索，或该节点是否应保持为单方候选？",
            "allowedEvidence": "只记录独立结论、最小页码定位和不确定性；不得复制教材原文、题目、答案、图片或 OCR。",
            "status": "open",
        })
    (DATA / "review_queue.json").write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    by_anchor = defaultdict(list)
    for item in queue:
        by_anchor[item["capabilityAnchor"]].append(item)
    counts = Counter(item["reviewType"] for item in queue)
    lines = [
        "# 阶段 5.3 关键页复核队列", "",
        "本队列处理跨版本锚点已定位、但节点证据不足的项目。它不授权将教材内容提交到仓库；复核者只能提交独立判断、最小页码定位和不确定性。", "",
        "## 总览", "",
        f"- 开放项目：{len(queue)}。", f"- 关键页确认：{counts['page-confirmation']}。", f"- 范围扩展检索：{counts['scope-expansion']}。", "- 高优先级：空间表征、图形认识和概念边界项目。", "",
        "## 复核规则", "",
        "1. 先确认目标是否是稳定可诊断能力，而非教材特有活动。",
        "2. 仅登记版本代号、册次、页码/章节定位和独立结论。",
        "3. 结果只能是：直接支持、表述/粒度差异、当前范围未定位、冲突待裁决。",
        "4. 未定位不是反证；冲突不会自动改变节点或依赖强度。",
        "5. 拟议变更须使用社区复核模板，并由维护者记录采纳、拒绝或待定理由。", "",
        "## 项目", "",
        "| topicId | 锚点 | 类型 | 优先级 | 复核问题 |", "| --- | --- | --- | --- | --- |",
    ]
    for item in queue:
        lines.append(f"| `{item['topicId']}` | `{item['capabilityAnchor']}` | {item['reviewType']} | {item['priority']} | {item['question']} |")
    (DOCS / "PHASE_5_3_PAGE_REVIEW_QUEUE.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Built {len(queue)} review items.")


if __name__ == "__main__":
    main()
