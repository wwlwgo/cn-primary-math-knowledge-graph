# candidate-0.3.0-cross-edition 发布说明

## 覆盖范围

本候选版本覆盖一上至三下六册范围的自动化候选数据：95 个 `reviewed` 学习目标、18 条 `soft` 依赖、19 个课程标准能力锚点和 56 条课程标准登记。

本版本新增三年级下册双版本私有核验范围结论，并按课程标准能力锚点重新计算跨版本支持情况。公开仓库只保存独立撰写的能力目标、最小定位、状态和不确定性，不包含教材扫描件、原文、OCR、题目、答案或图片。

## 跨版本结果

- 课标能力锚点重合率：18/19。
- 严格可诊断节点直接确认数：79/87。
- 当前复核队列：27 项全部闭环，0 个开放项。
- 当前范围未定位项不解释为课程缺失或版本冲突。
- 未新增、删除或升级依赖边。

## 证据层级

这是 `candidate` 数据，不是专家确认版：

- 所有边均为 `soft`，表示有帮助但存在替代学习路径。
- 未发布 `hard` 边，未存在 `approved` 节点或边。
- 双版本共同呈现只支持“候选目标可被重复观察”，不证明认知必要性。
- 教材顺序、页码和单元不构成应用层接口。

## 已知限制

- 四年级新版教材输入尚未到位，因此本版本不继续外推四年级范围。
- 版本 B 仍作为私有交叉检验材料；公开结论不得复刻其受保护表达。
- 课程标准能力锚点不是官方微知识点划分，而是项目内稳定比较单位。
- 诊断提示是检查入口，不是正式试题或标准化测验。

## 复现

```bash
python3 scripts/validate_dataset.py
python3 scripts/check_release_tree.py
python3 scripts/validate_review_queue.py
python3 scripts/query_dataset.py prerequisites cn_math_g2_remainder_division_as_groups_and_leftover --recursive
python3 scripts/query_dataset.py unlocks cn_math_g2_represent_equal_sharing_and_grouping_division --recursive
python3 scripts/query_dataset.py grade G3
```
