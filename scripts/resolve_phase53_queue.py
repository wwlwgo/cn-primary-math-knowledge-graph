#!/usr/bin/env python3
"""Apply private page-review conclusions to every phase 5.3 queue item."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

# Independent summaries only; never textbook text, questions, or images.
RESOLUTIONS = {
    "cn_math_g2_construct_prism_or_cylinder_from_paper": ("not-located-in-scope", "resolved", "G1 fall 67-72; G1 spring 1-7; G3 fall 1-5", "五册已核验图形范围未确认以纸张构造指定立体的独立目标。"),
    "cn_math_g2_identify_faces_of_simple_solids": ("located", "resolved", "G1 spring 1-7", "平面与立体表面关系的呈现支持该节点。"),
    "cn_math_g2_recognize_solids_from_views": ("located", "resolved", "G3 fall 1-5", "不同视角观察简单物体的呈现直接支持该节点。"),
    "cn_math_g2_unfold_and_reconstruct_cuboid": ("not-located-in-scope", "resolved", "G1 fall 67-72; G3 fall 1-5", "未确认展开与还原长方体的独立呈现。"),
    "cn_math_g2_predict_faces_when_cuboid_rolls": ("not-located-in-scope", "resolved", "G1 fall 67-72; G3 fall 1-5", "未确认滚动预测的独立呈现。"),
    "cn_math_g2_identify_parallelogram_by_features": ("located", "resolved", "G1 spring 1-7", "平面图形辨认范围支持按可见特征识别该图形。"),
    "cn_math_g2_construct_parallelogram_from_parts": ("located", "resolved", "G1 spring 1-7", "平面图形操作与构造范围支持该节点，但实现路径不同。"),
    "cn_math_g2_recognize_parallelogram_invariance_under_shear": ("not-located-in-scope", "resolved", "G1 spring 1-7", "未确认通过拉动保持特征的独立呈现。"),
    "cn_math_g2_compose_target_shapes_with_tangram": ("not-located-in-scope", "resolved", "G1 spring 1-7; G2 fall 1-9", "未确认特定拼图材料的独立呈现。"),
    "cn_math_g2_decompose_tangram_by_adjacency_and_size": ("not-located-in-scope", "resolved", "G1 spring 1-7; G2 fall 1-9", "未确认按相邻和大小分析特定拼图的独立呈现。"),
    "cn_math_g2_select_body_measure_for_length_estimation": ("located", "resolved", "G2 fall 55-72", "身体尺度作为长度估测基准的呈现支持该节点。"),
    "cn_math_g2_measure_consistently_with_nonstandard_unit": ("located", "resolved", "G2 fall 55-72", "测量活动支持以一致单位比较长度的节点。"),
    "cn_math_g1_compose_decompose_numbers_for_make_ten": ("located", "resolved", "G1 fall 88-102", "20以内进位计算范围支持十的组成分解策略。"),
    "cn_math_g2_identify_reflection_symmetry_by_folding": ("not-located-in-scope", "resolved", "G1 spring 1-7; G3 fall 61-72", "当前五册未确认折叠辨认轴对称的独立呈现。"),
    "cn_math_g3_model_multiplication_division_applications": ("located", "resolved", "G3 fall 39-56", "多位数乘一位数的应用范围支持乘除法建模，但粒度不同。"),
    "cn_math_g3_interpret_decimal_as_yuan_jiao_fen": ("needs-additional-input", "needs-additional-input", "G1 fall-G3 fall final scope check", "当前五册未包含可确认的小数/货币解释范围；需要后续册次或公开资源。"),
    "cn_math_g3_interpret_calendar_dates_and_intervals": ("needs-additional-input", "needs-additional-input", "G1 fall-G3 fall final scope check", "当前五册未包含可确认的日历间隔范围；需要后续册次或公开资源。"),
    "cn_math_g2_sum_three_two_digit_numbers": ("located", "resolved", "G2 spring 63-82", "万以内加减计算范围支持分步求和，教材实现不同。"),
    "cn_math_g2_subtract_two_parts_from_total": ("located", "resolved", "G2 spring 63-82", "加减数量关系范围支持从总量去除多个部分的建模。"),
    "cn_math_g2_mixed_add_subtract_change": ("located", "resolved", "G2 spring 63-82", "加减法应用范围支持连续变化表征，教材实现不同。"),
    "cn_math_g2_classify_by_explicit_criterion": ("located", "resolved", "G2 fall 1-9", "分类与整理范围直接支持明确标准分类。"),
    "cn_math_g2_refine_classification_by_second_criterion": ("located", "resolved", "G2 fall 1-9", "分类与整理范围支持按第二标准细分。"),
    "cn_math_g1_classify_objects_by_explicit_feature": ("located", "resolved", "G2 fall 1-9", "跨册分类与整理范围支持按明确特征分类。"),
    "cn_math_g1_calculate_addition_within_twenty_by_make_ten": ("located", "resolved", "G1 fall 88-102", "20以内进位计算范围支持该程序目标。"),
    "cn_math_g2_add_two_digit_numbers_with_regrouping": ("located", "resolved", "G1 spring 56-68", "100以内笔算加减范围支持进位加法节点。"),
    "cn_math_g2_subtract_two_digit_numbers_with_regrouping": ("located", "resolved", "G1 spring 56-68", "100以内笔算加减范围支持退位减法节点。"),
    "cn_math_g3_add_three_digit_numbers_with_regrouping": ("located", "resolved", "G2 spring 63-82", "万以内加减法范围支持三位数进位计算。"),
    "cn_math_g3_subtract_three_digit_numbers_with_regrouping": ("located", "resolved", "G2 spring 63-82", "万以内加减法范围支持三位数退位计算。"),
    "cn_math_g3_read_write_compare_simple_decimals": ("needs-additional-input", "needs-additional-input", "G1 fall-G3 fall final scope check", "当前五册未包含可确认的小数读写比较范围；需要后续册次或公开资源。"),
    "cn_math_g3_collect_record_and_classify_data": ("needs-additional-input", "needs-additional-input", "G1 fall-G3 fall final scope check", "当前五册未包含可确认的数据收集整理范围；需要后续册次或公开资源。"),
}


def main() -> None:
    nodes_path = DATA / "cross_edition_node_evidence.json"
    queue_path = DATA / "review_queue.json"
    nodes = json.loads(nodes_path.read_text(encoding="utf-8"))
    queue = json.loads(queue_path.read_text(encoding="utf-8"))
    selected = sys.argv[1] if len(sys.argv) > 1 else "all"
    queue_by_id = {item["topicId"]: item for item in queue}
    selected_ids = {
        item["topicId"] for item in queue
        if selected == "all"
        or selected == "high" and item["priority"] == "high"
        or selected == "normal" and item["reviewType"] == "page-confirmation" and item["priority"] == "normal"
        or selected == "scope" and item["reviewType"] == "scope-expansion"
    }
    for item in nodes:
        if item["topicId"] not in selected_ids:
            continue
        status, queue_status, locator, conclusion = RESOLUTIONS[item["topicId"]]
        item["editionB"] = status
        item["editionBLocator"] = locator
        item["comparison"] = "both-supported" if status == "located" else "one-sided-needs-review"
        item["note"] = conclusion
        item["uncertainty"] = "本结论限于五册私有输入范围，不构成专家审核。"
    for item in queue:
        if item["topicId"] not in selected_ids:
            continue
        status, queue_status, locator, conclusion = RESOLUTIONS[item["topicId"]]
        item["status"] = queue_status
        item["resolution"] = conclusion
        item["editionBLocator"] = locator
        item["communityState"] = "community-review-needed" if status == "not-located-in-scope" else "closed-with-maintainer-evidence"
    nodes_path.write_text(json.dumps(nodes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    queue_path.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Resolved {len(selected_ids)} queue items for {selected} batch.")


if __name__ == "__main__":
    main()
