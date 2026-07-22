#!/usr/bin/env python3
"""Create curriculum capability anchors and attach every topic to one anchor."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
IMPLEMENTATION_EVIDENCE = {
    "cn_math_g1_order_events_within_a_day",
    "cn_math_g2_compare_totals_in_three_round_context",
    "cn_math_g2_model_remaining_capacity",
    "cn_math_g2_compare_opposite_changes_before_calculation",
    "cn_math_g2_control_cylinder_shape_with_paper_strip",
    "cn_math_g2_explain_alternative_compensation_for_subtraction",
    "cn_math_g2_solve_logic_grid_by_constraints",
    "cn_math_g2_model_amount_relationships_in_shopping",
}


def anchor_id(standard_id: str) -> str:
    suffix = standard_id.removeprefix("cn-math-2022:")
    return "cn_math_anchor_" + re.sub(r"[^a-z0-9]+", "_", suffix).strip("_")


def main() -> None:
    topics_path = DATA / "topics.json"
    standards = json.loads((DATA / "standards.json").read_text(encoding="utf-8"))
    standard_titles = {item["id"]: item["title"] for item in standards}
    topics = json.loads(topics_path.read_text(encoding="utf-8"))
    used_standards = sorted({topic["standards"][0] for topic in topics})
    anchors = [
        {
            "id": anchor_id(standard_id),
            "name": standard_titles[standard_id],
            "standards": [standard_id],
            "scope": "curriculum-capability",
        }
        for standard_id in used_standards
    ]
    for topic in topics:
        topic["capabilityAnchor"] = anchor_id(topic["standards"][0])
        topic["modelLayer"] = "implementation_evidence" if topic["id"] in IMPLEMENTATION_EVIDENCE else "diagnostic"
    (DATA / "capability_anchors.json").write_text(
        json.dumps(anchors, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    topics_path.write_text(json.dumps(topics, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Built {len(anchors)} anchors and classified {len(topics)} topics.")


if __name__ == "__main__":
    main()
