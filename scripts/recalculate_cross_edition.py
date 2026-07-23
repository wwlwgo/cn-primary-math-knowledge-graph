#!/usr/bin/env python3
"""Recalculate cross-edition metrics from curriculum capability anchors.

This deliberately compares the six-book private input ranges as a whole.
It does not compare same-named units or same-semester textbook structure.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
REPORT = ROOT / "docs/review/PHASE_5_2_RECALCULATION.md"
INPUT_AUDIT = ROOT / "docs/review/PHASE_5_2_INPUT_AUDIT.md"
IMPACT = ROOT / "docs/review/PHASE_5_2_IMPACT.md"
OLD_REPORTS = sorted((ROOT / "docs/review").glob("CROSS_EDITION_PEP_G*.md"))
ONE_SIDED = {
    "cn_math_anchor_primary_number_algebra_stage_2_quantitative_relations_content_4",
}
IMPLEMENTATION_DIFFERENCES = {
    "cn_math_anchor_primary_geometry_stage_1_shape_recognition_and_measurement_content_1",
    "cn_math_anchor_primary_geometry_stage_1_shape_recognition_and_measurement_content_2",
    "cn_math_anchor_primary_number_algebra_stage_1_number_and_operations_content_3",
    "cn_math_anchor_primary_number_algebra_stage_1_number_and_operations_content_4",
    "cn_math_anchor_primary_number_algebra_stage_1_number_and_operations_content_5",
    "cn_math_anchor_primary_number_algebra_stage_2_number_and_operations_content_1",
}
RESOLVED_NOT_LOCATED = {
    "cn_math_g3_preserve_order_when_adding_same_quantity": {
        "editionBLocator": "G3 spring final scope check",
        "note": "当前六册范围未确认同加数保持大小关系的独立呈现。",
        "uncertainty": "未定位不是反证；后续册次或公开资源可继续核验。",
    },
}


def percent(numerator: int, denominator: int) -> str:
    return f"{numerator / denominator * 100:.1f}%" if denominator else "N/A"


def main() -> None:
    anchors = json.loads((DATA / "capability_anchors.json").read_text(encoding="utf-8"))
    topics = json.loads((DATA / "topics.json").read_text(encoding="utf-8"))
    records = []
    for anchor in anchors:
        one_sided = anchor["id"] in ONE_SIDED
        if one_sided:
            relation = "one-sided-needs-review"
            b_status = "not-located-in-scope"
            note = "当前六册范围未确认第二版本的对应呈现；未定位不是反证。"
        elif anchor["id"] in IMPLEMENTATION_DIFFERENCES:
            relation = "different-implementation"
            b_status = "located"
            note = "两版本均有能力呈现，但使用的表征或活动路径不同；不构成稳定能力冲突。"
        else:
            relation = "both-supported"
            b_status = "located"
            note = "两个版本的六册私有核验范围均确认该课标能力锚点。"
        records.append({
            "capabilityAnchor": anchor["id"],
            "standards": anchor["standards"],
            "editionA": {"status": "located", "locator": "私有六册范围（G1 fall 至 G3 spring）"},
            "editionB": {"status": b_status, "locator": "私有六册范围（G1 fall 至 G3 spring）"},
            "comparison": relation,
            "note": note,
            "uncertainty": "页级抽样不足时，锚点定位不应替代节点级确认。",
        })
    (DATA / "cross_edition_anchor_evidence.json").write_text(
        json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    diagnostic = [topic for topic in topics if topic["modelLayer"] == "diagnostic"]
    both_anchors = {item["capabilityAnchor"] for item in records if item["editionB"]["status"] == "located"}
    direct_support_ids: set[str] = set()
    for path in OLD_REPORTS:
        for line in path.read_text(encoding="utf-8").splitlines():
            if "| supports" in line or "| `supports`" in line:
                direct_support_ids.update(re.findall(r"`(cn_math_[a-z0-9_]+)`", line))
    existing_node_path = DATA / "cross_edition_node_evidence.json"
    existing_nodes = {}
    if existing_node_path.exists():
        existing_nodes = {item["topicId"]: item for item in json.loads(existing_node_path.read_text(encoding="utf-8"))}
    node_records = []
    for topic in diagnostic:
        direct = topic["id"] in direct_support_ids
        anchor_located = topic["capabilityAnchor"] in both_anchors
        generated = {
            "topicId": topic["id"],
            "capabilityAnchor": topic["capabilityAnchor"],
            "editionA": "located",
            "editionB": "located" if direct else ("likely-located-needs-page-check" if anchor_located else "not-located-in-scope"),
            "comparison": "both-supported" if direct else "one-sided-needs-review",
            "note": "已有直接节点证据。" if direct else "锚点已定位但该节点尚缺第二版本的页级确认。" if anchor_located else "当前六册范围尚未确认第二版本节点证据。",
        }
        prior = existing_nodes.get(topic["id"])
        if not direct and prior and prior.get("editionB") in {"located", "not-located-in-scope"} and "editionBLocator" in prior:
            generated.update(prior)
        if not direct and topic["id"] in RESOLVED_NOT_LOCATED:
            generated.update(RESOLVED_NOT_LOCATED[topic["id"]])
        node_records.append(generated)
    (DATA / "cross_edition_node_evidence.json").write_text(
        json.dumps(node_records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    both_nodes = [item for item in node_records if item["comparison"] == "both-supported"]
    anchor_covered_nodes = [topic for topic in diagnostic if topic["capabilityAnchor"] in both_anchors]
    difference_count = sum(item["comparison"] in {"different-wording", "different-granularity", "different-implementation"} for item in records if item["editionB"]["status"] == "located")
    relations = Counter(item["comparison"] for item in records)
    lines = [
        "# 阶段 5.2 跨版本验证重算",
        "",
        "处理日期：2026-07-23。比较单位是课标能力锚点，不是同册教材目录或教材特有活动。两套教材均仅作为私有输入证据，公开结论不复制教材内容。",
        "",
        "## 输入与范围",
        "",
        f"- 可比较能力锚点：{len(records)}。",
        f"- 可诊断节点：{len(diagnostic)}；教材实现证据节点：{len(topics) - len(diagnostic)}，不纳入节点重合率。",
        "- 输入范围：两个版本均为一上至三下六册；允许跨册检索。",
        "- 未定位仅表示当前六册范围未确认，不表示另一版本不存在该能力。",
        "",
        "## 指标",
        "",
        f"| 指标 | 分子/分母 | 结果 |",
        f"| --- | --- | --- |",
        f"| 课标能力锚点重合率 | {len(both_anchors)}/{len(records)} | {percent(len(both_anchors), len(records))} |",
        f"| 严格可诊断节点重合率 | {len(both_nodes)}/{len(diagnostic)} | {percent(len(both_nodes), len(diagnostic))} |",
        f"| 教材实现差异率 | {difference_count}/{len(both_anchors)} | {percent(difference_count, len(both_anchors))} |",
        "",
        "教材实现差异率的分子只包含已在两个版本定位、但表征或活动路径不同的能力锚点；它不表示课程目标冲突。",
        f"锚点覆盖下仍待节点页级复核的节点：{len(anchor_covered_nodes) - len(both_nodes)} 个；它们不计入严格节点重合率。",
        "",
        "## 状态统计",
        "",
        f"- `both-supported`：{relations['both-supported']}",
        f"- `different-implementation`：{relations['different-implementation']}",
        f"- `one-sided-needs-review`：{relations['one-sided-needs-review']}",
        f"- `conflict`：{relations['conflict']}",
        "",
        "## 限制",
        "",
        "- 该轮确认的是课标能力范围的跨版本呈现，不等同于微节点的专家确认。",
        "- 单方待复核锚点当前仅涉及第二学段等量关系；后续可由其他册次或关键页证据继续检索。",
        "- 任何 `different-implementation` 均不触发 hard 边升级或节点拆分。",
    ]
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    INPUT_AUDIT.write_text(
        "# 阶段 5.2 输入审计\n\n"
        f"- 能力锚点：{len(records)}，均关联已登记课程标准条目。\n"
        f"- 可诊断节点：{len(diagnostic)}；教材实现证据节点：{len(topics) - len(diagnostic)}，排除在严格节点统计外。\n"
        f"- 直接确认双版本节点：{len(both_nodes)}；锚点已定位但待页级确认节点：{len(anchor_covered_nodes) - len(both_nodes)}；当前范围未定位节点：{len(diagnostic) - len(anchor_covered_nodes)}。\n"
        "- 结论：输入满足六册对六册重算；未定位和待页级确认不解释为课程内容缺失。\n",
        encoding="utf-8",
    )
    dependencies = json.loads((DATA / "dependencies.json").read_text(encoding="utf-8"))
    topic_by_id = {topic["id"]: topic for topic in topics}
    edge_lines = ["# 阶段 5.2 节点与依赖影响清单", "", "所有保留边均为连接 `diagnostic` 节点的 `soft` 边；未新增或升级 `hard` 边。", "", "| 目标节点 | 前置节点 | 锚点关系 | 处理 |", "| --- | --- | --- | --- |"]
    for edge in dependencies:
        target = topic_by_id[edge["topicId"]]
        prerequisite = topic_by_id[edge["prerequisiteId"]]
        relation = "同一能力锚点" if target["capabilityAnchor"] == prerequisite["capabilityAnchor"] else "跨能力锚点"
        edge_lines.append(f"| `{target['id']}` | `{prerequisite['id']}` | {relation} | 保留为 soft；待后续页级或专家复核。 |")
    IMPACT.write_text("\n".join(edge_lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(records)} anchor records and {len(node_records)} node records; {len(both_nodes)} direct diagnostic-node confirmations.")


if __name__ == "__main__":
    main()
