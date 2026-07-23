# candidate-0.3.0-cross-edition 发布准备审计

审计日期：2026-07-23。本审计证明本地发布准备完成；GitHub 推送、标签和 Release 创建需要单独执行并记录。

| 发布要求 | 工件/验证 | 结论 |
| --- | --- | --- |
| 版本一致性 | `data/manifest.json`、`CITATION.cff`、README、CHANGELOG、发布说明 | `0.3.0-candidate.cross-edition` / `candidate-0.3.0-cross-edition` 一致 |
| 覆盖与证据层级 | `docs/releases/CANDIDATE_0.3.0_CROSS_EDITION.md` | 95 reviewed 节点、18 soft 边、19 能力锚点、56 标准；非专家确认 |
| 跨版本复核 | `data/cross_edition_anchor_evidence.json`、`data/cross_edition_node_evidence.json`、`data/review_queue.json` | 锚点 18/19 支持，节点 79/87 直接确认，队列 0 个开放项 |
| 数据许可与来源 | `DATA_LICENSE.md`、`PROVENANCE.md`、`CITATION.cff`、`docs/IP_RISK_AUDIT.md` | 数据分层许可、上游权利边界和引用信息齐备 |
| 复现命令 | README、`docs/releases/GITHUB_RELEASE_BODY.md` | 数据校验、发布树检查、复核队列校验和示例查询可本地运行 |
| 公开边界 | `.gitignore`、`scripts/check_release_tree.py`、来源政策 | 教材、OCR、题目、答案、token 和私有输入不纳入发布数据 |

## 发布动作记录

1. 推送主分支到 GitHub。
2. 创建新标签 `candidate-0.3.0-cross-edition`，不得移动或覆盖 `candidate-0.2.0-vertical`。
3. 使用 `docs/releases/GITHUB_RELEASE_BODY.md` 创建新的 GitHub Release。

完成上述外部动作后，应在开发日志补充远端提交、标签和 Release 状态。
