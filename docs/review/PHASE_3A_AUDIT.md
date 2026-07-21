# 阶段 3a 完整性审计

审计日期：2026-07-20。范围为北师大版《义务教育教科书 数学 二年级下册》2024 版的 `candidate-0.1.0` 发布准备，不代表专家教育审核或 GitHub Release 已完成。

| 阶段 3a 要求 | 证据 | 结论 |
| --- | --- | --- |
| 候选节点结构化 | `data/topics.json`；43 个节点均含 ID、类型、描述、两条证据、诊断提示、课标 ID、教材定位与 `reviewed` 状态 | 已完成 |
| 保守依赖转换 | `data/dependencies.json`；5 条教材内 `soft` 边，无 `hard` 边 | 已完成 |
| 自动门禁 | `scripts/validate_dataset.py` 检查字段边界、诊断提示、来源结构、课标引用、候选发布策略、端点、重复、自环、环路与 manifest | 已完成 |
| 可复现查询 | `scripts/query_dataset.py` 提供前置追溯、后续解锁与年级范围查询 | 已完成 |
| 跨版本/教辅登记 | `docs/review/CROSS_EDITION_EVIDENCE_REGISTER.md` | 已完成登记；目前仅有北师大版基线，待接收人教版、低年级教材和教辅材料 |
| 公开复核入口 | `docs/review/COMMUNITY_REVIEW_TEMPLATE.md` 和 `docs/review/CANDIDATE_RELEASE_CHECKLIST.md` | 已完成 |
| 版权隔离 | `docs/SOURCE_POLICY.md`、`.gitignore` 与节点来源记录 | 已完成；未纳入教材、教辅或 OCR 原文 |

## 查询验收

| 场景 | 命令 | 预期结果 |
| --- | --- | --- |
| 前置追溯 | `python3 scripts/query_dataset.py prerequisites cn_math_g2_model_three_digit_add_subtract_word_problem` | 返回“三位数进位竖式加法”这一条 `soft` 关系 |
| 后续解锁 | `python3 scripts/query_dataset.py unlocks cn_math_g2_identify_faces_of_simple_solids` | 返回“预测长方体滚动后的面”这一条 `soft` 关系 |
| 年级范围 | `python3 scripts/query_dataset.py grade G2` | 返回 43 个二年级候选节点 |

## 阶段结论

阶段 3a 的退出条件已满足：候选数据、自动门禁、跨版本证据登记和公开复核队列均已具备。阶段 4 可以在许可文本、GitHub 仓库与发布说明准备完成后发布 `candidate-0.1.0`。人教版和教辅材料尚未提供，不构成候选首发阻塞项；收到后应按登记册补充支持、差异或冲突记录。

不得将本审计解释为阶段 3b 的专家校审通过。所有 `hard` 边和 `approved` 数据仍为空。
