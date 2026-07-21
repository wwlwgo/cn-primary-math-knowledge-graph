# 北师大版纵向候选骨架审计

审计日期：2026-07-21。范围为北师大版一年级上、一下、二年级上、二年级下与三年级上候选能力骨架；不代表专家教育审核。

| 要求 | 证据 | 结论 |
| --- | --- | --- |
| 教材覆盖 | `docs/pilots/bnu-vertical-coverage.md` | 已覆盖目标五册及单元范围 |
| 结构化候选 | `data/topics.json`、转换状态表 | 91 个节点均为 `reviewed`，含必填字段 |
| 标准映射 | `data/standards.json` 与校验器 | 每个节点引用已登记课标 ID |
| 保守纵向关系 | `data/dependencies.json` | 19 条边均为 `soft`、`reviewed`，无 `hard` 边 |
| 自动校验 | `python3 scripts/update_manifest.py`、`python3 scripts/validate_dataset.py` | 通过；图无环、清单匹配 |
| 查询验收 | `scripts/query_dataset.py` | 已验证三上混合运算前置追溯、二上除法后续解锁、G3 年级范围查询 |
| 跨版本队列 | `docs/review/CROSS_EDITION_EVIDENCE_REGISTER.md`、发布说明 | 已登记，等待人教版输入 |
| 版权隔离 | `.gitignore`、来源政策、私有教材目录 | 无教材原件、OCR、题目或答案进入公开数据 |

## 结论

本轮纵向候选能力骨架满足本目标的候选数据、自动化、来源、保守依赖和审计要求。专家确认、`hard` 边和跨版本结论均明确保留在后续工作中。
