#!/usr/bin/env python3
"""Validate the published JSON dataset without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from hashlib import sha256
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
TOPIC_ID = re.compile(r"^cn_math_g[1-6]_[a-z][a-z0-9_]{2,80}$")
TOPIC_TYPES = {"CONCEPTUAL", "PROCEDURAL", "REPRESENTATIONAL", "LANGUAGE", "STRATEGIC", "META"}
DOMAINS = {"数与代数", "图形与几何", "统计与概率", "综合与实践"}
REVIEW_STATUSES = {"draft", "reviewed", "approved"}
SOURCE_KINDS = {"curriculum_standard", "textbook", "teacher_guide", "expert_review", "research"}
GRADE_BANDS = {"G1", "G2", "G3", "G4", "G5", "G6"}
MODEL_LAYERS = {"diagnostic", "implementation_evidence"}


def load_json(path: Path, errors: list[str]):
    try:
        with path.open(encoding="utf-8") as file:
            return json.load(file)
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: 无法读取 JSON：{exc}")
        return None


def validate_manifest_files(manifest: object, errors: list[str]) -> None:
    if not isinstance(manifest, dict):
        return
    files = manifest.get("files")
    expected_files = {
        "topics.json", "dependencies.json", "standards.json", "capability_anchors.json",
        "cross_edition_anchor_evidence.json", "cross_edition_node_evidence.json",
        "review_queue.json",
    }
    if not isinstance(files, dict) or set(files) != expected_files:
        errors.append("data/manifest.json: files 必须列出 topics.json、dependencies.json、standards.json")
        return
    for filename, metadata in files.items():
        expected_hash = metadata.get("sha256") if isinstance(metadata, dict) else None
        actual_hash = sha256((DATA / filename).read_bytes()).hexdigest()
        if not isinstance(expected_hash, str) or not re.fullmatch(r"[0-9a-f]{64}", expected_hash):
            errors.append(f"data/manifest.json: {filename} 缺少有效 SHA-256")
        elif expected_hash != actual_hash:
            errors.append(f"data/manifest.json: {filename} 的 SHA-256 与文件内容不一致；运行 scripts/update_manifest.py")


def validate_sources(value: object, label: str, errors: list[str]) -> None:
    if not isinstance(value, list) or not value:
        errors.append(f"{label}: sources 至少需要一条来源")
        return
    required = {"kind", "citation", "locator"}
    allowed = required | {"edition", "url"}
    for index, source in enumerate(value):
        source_label = f"{label}.sources[{index}]"
        if not isinstance(source, dict):
            errors.append(f"{source_label}: 必须是对象")
            continue
        missing = required - source.keys()
        unknown = source.keys() - allowed
        if missing:
            errors.append(f"{source_label}: 缺少字段 {', '.join(sorted(missing))}")
        if unknown:
            errors.append(f"{source_label}: 存在未知字段 {', '.join(sorted(unknown))}")
        if source.get("kind") not in SOURCE_KINDS:
            errors.append(f"{source_label}: kind 无效")
        for field, minimum, maximum in (("citation", 5, 300), ("locator", 1, 120)):
            value_at_field = source.get(field)
            if not isinstance(value_at_field, str) or not minimum <= len(value_at_field) <= maximum:
                errors.append(f"{source_label}: {field} 长度无效")
        if "edition" in source and (not isinstance(source["edition"], str) or len(source["edition"]) > 100):
            errors.append(f"{source_label}: edition 长度无效")
        if "url" in source and (not isinstance(source["url"], str) or not re.match(r"^https?://", source["url"])):
            errors.append(f"{source_label}: url 必须是 http(s) URL")


def validate_anchors(anchors: object, standard_ids: set[str], errors: list[str]) -> set[str]:
    if not isinstance(anchors, list):
        errors.append("data/capability_anchors.json: 根元素必须是数组")
        return set()
    ids: set[str] = set()
    for index, anchor in enumerate(anchors):
        label = f"anchors[{index}]"
        if not isinstance(anchor, dict) or set(anchor) != {"id", "name", "standards", "scope"}:
            errors.append(f"{label}: 字段必须为 id、name、standards、scope")
            continue
        anchor_id = anchor["id"]
        if not isinstance(anchor_id, str) or not re.fullmatch(r"cn_math_anchor_[a-z0-9_]{3,120}", anchor_id):
            errors.append(f"{label}: id 格式无效")
        elif anchor_id in ids:
            errors.append(f"{label}: 重复 id {anchor_id}")
        else:
            ids.add(anchor_id)
        if not isinstance(anchor["name"], str) or not 4 <= len(anchor["name"]) <= 120:
            errors.append(f"{label}: name 长度无效")
        if anchor["scope"] != "curriculum-capability":
            errors.append(f"{label}: scope 无效")
        if not isinstance(anchor["standards"], list) or not anchor["standards"] or any(item not in standard_ids for item in anchor["standards"]):
            errors.append(f"{label}: standards 必须引用已登记课标")
    return ids


def validate_topics(topics: object, anchor_ids: set[str], errors: list[str]) -> dict[str, dict]:
    if not isinstance(topics, list):
        errors.append("data/topics.json: 根元素必须是数组")
        return {}

    by_id: dict[str, dict] = {}
    required = {
        "id", "type", "subject", "domain", "name", "description", "gradeBands",
        "evidence", "assessmentPrompt", "standards", "capabilityAnchor", "modelLayer", "sources", "reviewStatus",
    }
    allowed = required
    for index, topic in enumerate(topics):
        label = f"topics[{index}]"
        if not isinstance(topic, dict):
            errors.append(f"{label}: 必须是对象")
            continue
        missing = required - topic.keys()
        unknown = topic.keys() - allowed
        if missing:
            errors.append(f"{label}: 缺少字段 {', '.join(sorted(missing))}")
            continue
        if unknown:
            errors.append(f"{label}: 存在未知字段 {', '.join(sorted(unknown))}")
            continue
        topic_id = topic["id"]
        if not isinstance(topic_id, str) or not TOPIC_ID.fullmatch(topic_id):
            errors.append(f"{label}: id 格式无效")
            continue
        if topic_id in by_id:
            errors.append(f"{label}: 重复 id {topic_id}")
            continue
        by_id[topic_id] = topic
        if topic["type"] not in TOPIC_TYPES:
            errors.append(f"{label}: type 无效")
        if topic["subject"] != "数学":
            errors.append(f"{label}: subject 必须为 数学")
        if topic["domain"] not in DOMAINS:
            errors.append(f"{label}: domain 无效")
        if not isinstance(topic["name"], str) or not 2 <= len(topic["name"]) <= 80:
            errors.append(f"{label}: name 长度无效")
        if not isinstance(topic["description"], str) or not 10 <= len(topic["description"]) <= 300:
            errors.append(f"{label}: description 长度无效")
        if not isinstance(topic["gradeBands"], list) or not topic["gradeBands"] or len(set(topic["gradeBands"])) != len(topic["gradeBands"]) or any(grade not in GRADE_BANDS for grade in topic["gradeBands"]):
            errors.append(f"{label}: gradeBands 无效")
        if not isinstance(topic["evidence"], list) or len(topic["evidence"]) < 2 or any(not isinstance(item, str) or not 8 <= len(item) <= 240 for item in topic["evidence"]):
            errors.append(f"{label}: evidence 至少需要两条")
        if not isinstance(topic["assessmentPrompt"], str) or not 10 <= len(topic["assessmentPrompt"]) <= 400:
            errors.append(f"{label}: assessmentPrompt 长度无效")
        if not isinstance(topic["standards"], list) or not topic["standards"] or len(set(topic["standards"])) != len(topic["standards"]) or any(not isinstance(item, str) or not item.startswith("cn-math-2022:") for item in topic["standards"]):
            errors.append(f"{label}: standards 必须含有 cn-math-2022: 标识")
        if topic["capabilityAnchor"] not in anchor_ids:
            errors.append(f"{label}: capabilityAnchor 必须引用已登记锚点")
        if topic["modelLayer"] not in MODEL_LAYERS:
            errors.append(f"{label}: modelLayer 无效")
        validate_sources(topic["sources"], label, errors)
        if topic["reviewStatus"] not in REVIEW_STATUSES:
            errors.append(f"{label}: reviewStatus 无效")
    return by_id


def validate_standards(standards: object, errors: list[str]) -> set[str]:
    if not isinstance(standards, list):
        errors.append("data/standards.json: 根元素必须是数组")
        return set()

    ids: set[str] = set()
    required = {"id", "title", "authority", "documentNumber", "issuedAt", "sourceUrl", "sourceLocator", "status"}
    for index, standard in enumerate(standards):
        label = f"standards[{index}]"
        if not isinstance(standard, dict):
            errors.append(f"{label}: 必须是对象")
            continue
        missing = required - standard.keys()
        if missing:
            errors.append(f"{label}: 缺少字段 {', '.join(sorted(missing))}")
            continue
        standard_id = standard["id"]
        if not isinstance(standard_id, str) or not standard_id.startswith("cn-math-2022:"):
            errors.append(f"{label}: id 必须以 cn-math-2022: 开头")
        elif standard_id in ids:
            errors.append(f"{label}: 重复 id {standard_id}")
        else:
            ids.add(standard_id)
        if standard["authority"] != "教育部" or standard["documentNumber"] != "教材〔2022〕2号":
            errors.append(f"{label}: 必须关联教育部 教材〔2022〕2号")
        if standard["issuedAt"] != "2022-03-25":
            errors.append(f"{label}: issuedAt 必须为 2022-03-25")
        if standard["status"] not in {"authoritative-document", "indexed-section"}:
            errors.append(f"{label}: status 无效")
    return ids


def validate_dependencies(dependencies: object, topics: dict[str, dict], errors: list[str]) -> dict[str, set[str]]:
    if not isinstance(dependencies, list):
        errors.append("data/dependencies.json: 根元素必须是数组")
        return {}

    graph: dict[str, set[str]] = defaultdict(set)
    seen: set[tuple[str, str]] = set()
    required = {"topicId", "prerequisiteId", "strength", "reason", "sources", "reviewStatus"}
    allowed = required
    for index, dependency in enumerate(dependencies):
        label = f"dependencies[{index}]"
        if not isinstance(dependency, dict):
            errors.append(f"{label}: 必须是对象")
            continue
        missing = required - dependency.keys()
        unknown = dependency.keys() - allowed
        if missing:
            errors.append(f"{label}: 缺少字段 {', '.join(sorted(missing))}")
            continue
        if unknown:
            errors.append(f"{label}: 存在未知字段 {', '.join(sorted(unknown))}")
            continue
        topic_id, prerequisite_id = dependency["topicId"], dependency["prerequisiteId"]
        if topic_id not in topics or prerequisite_id not in topics:
            errors.append(f"{label}: 边端点必须引用已存在的节点")
            continue
        if topics[topic_id].get("modelLayer") != "diagnostic" or topics[prerequisite_id].get("modelLayer") != "diagnostic":
            errors.append(f"{label}: 依赖边端点必须为 diagnostic 节点")
        if topic_id == prerequisite_id:
            errors.append(f"{label}: 不允许自环")
        edge = (topic_id, prerequisite_id)
        if edge in seen:
            errors.append(f"{label}: 重复边 {topic_id} -> {prerequisite_id}")
        seen.add(edge)
        graph[topic_id].add(prerequisite_id)
        if dependency["strength"] not in {"hard", "soft"}:
            errors.append(f"{label}: strength 必须为 hard 或 soft")
        if not isinstance(dependency["reason"], str) or len(dependency["reason"].strip()) < 12:
            errors.append(f"{label}: reason 必须至少 12 个字符")
        validate_sources(dependency["sources"], label, errors)
        if dependency["reviewStatus"] not in REVIEW_STATUSES:
            errors.append(f"{label}: reviewStatus 无效")
        if dependency["strength"] == "hard" and dependency["reviewStatus"] != "approved":
            errors.append(f"{label}: hard 边只能进入 approved/expert-verified 数据")
        if dependency["strength"] == "hard" and sum(source.get("kind") == "expert_review" for source in dependency["sources"] if isinstance(source, dict)) < 2:
            errors.append(f"{label}: hard 边至少需要两条 expert_review 来源")
    return graph


def validate_acyclic(graph: dict[str, set[str]], errors: list[str]) -> None:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> None:
        if node in visiting:
            errors.append(f"依赖图存在环，涉及节点 {node}")
            return
        if node in visited:
            return
        visiting.add(node)
        for prerequisite in graph.get(node, set()):
            visit(prerequisite)
        visiting.remove(node)
        visited.add(node)

    for node in graph:
        visit(node)


def validate_candidate_policy(manifest: object, topics: dict[str, dict], dependencies: object, errors: list[str]) -> None:
    """Apply the additional safety contract for a candidate publication."""
    if not isinstance(manifest, dict) or manifest.get("status") not in {"candidate-preparation", "candidate", "candidate-release-prepared"}:
        return
    for topic_id, topic in topics.items():
        if topic.get("reviewStatus") != "reviewed":
            errors.append(f"candidate 数据集中的节点 {topic_id} 必须为 reviewed")
    if not isinstance(dependencies, list):
        return
    for index, dependency in enumerate(dependencies):
        if isinstance(dependency, dict) and dependency.get("strength") != "soft":
            errors.append(f"candidate 数据集中的 dependencies[{index}] 必须为 soft")
        if isinstance(dependency, dict) and dependency.get("reviewStatus") != "reviewed":
            errors.append(f"candidate 数据集中的 dependencies[{index}] 必须为 reviewed")


def main() -> int:
    errors: list[str] = []
    manifest = load_json(DATA / "manifest.json", errors)
    topics = load_json(DATA / "topics.json", errors)
    dependencies = load_json(DATA / "dependencies.json", errors)
    standards = load_json(DATA / "standards.json", errors)
    anchors = load_json(DATA / "capability_anchors.json", errors)
    if manifest is None or topics is None or dependencies is None or standards is None or anchors is None:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    standard_ids = validate_standards(standards, errors)
    anchor_ids = validate_anchors(anchors, standard_ids, errors)
    topics_by_id = validate_topics(topics, anchor_ids, errors)
    for topic_id, topic in topics_by_id.items():
        for standard_id in topic.get("standards", []):
            if standard_id not in standard_ids:
                errors.append(f"topic {topic_id}: 引用了未登记的课标 ID {standard_id}")
    graph = validate_dependencies(dependencies, topics_by_id, errors)
    validate_acyclic(graph, errors)
    validate_candidate_policy(manifest, topics_by_id, dependencies, errors)
    validate_manifest_files(manifest, errors)
    counts = manifest.get("counts") if isinstance(manifest, dict) else None
    if not isinstance(counts, dict) or counts.get("topics") != len(topics) or counts.get("dependencies") != len(dependencies) or counts.get("standards") != len(standards) or counts.get("capabilityAnchors") != len(anchors):
        errors.append("data/manifest.json: counts 与数据文件实际数量不一致")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"OK: {len(standards)} 条课标登记，{len(anchors)} 个能力锚点，{len(topics)} 个节点，{len(dependencies)} 条依赖，图无环。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
