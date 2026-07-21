# candidate-0.2.0-vertical 发布准备审计

审计日期：2026-07-21。本审计证明本地发布准备完成，不表示 GitHub Release 已创建。

| 发布要求 | 工件/验证 | 结论 |
| --- | --- | --- |
| 版本一致性 | `data/manifest.json`、`CITATION.cff`、README、CHANGELOG、发布说明 | `0.2.0-candidate.vertical` / `candidate-0.2.0-vertical` 一致 |
| 覆盖与证据层级 | `docs/releases/CANDIDATE_0.2.0_VERTICAL.md` | 91 reviewed 节点、19 soft 边、56 标准；非专家确认 |
| 数据许可与来源 | `DATA_LICENSE.md`、`PROVENANCE.md`、`CITATION.cff` | 数据分层许可、上游权利边界和引用信息齐备 |
| 复现命令 | README、`docs/releases/GITHUB_RELEASE_BODY.md` | 校验与三类查询均可本地运行 |
| 公开边界 | `.gitignore`、来源政策、工作树检查 | 教材、OCR、题目和答案不纳入发布数据 |
| GitHub 工件 | `CHANGELOG.md`、Release Body、社区复核模板 | 本地准备完成；首次提交、仓库 URL、标签和 Release 创建为外部动作 |

## 未完成的外部动作

1. 创建或指定 GitHub 仓库 URL，并将该 URL 写入 `CITATION.cff`。
2. 创建首次 Git 提交、推送仓库，创建标签 `candidate-0.2.0-vertical`。
3. 使用 `docs/releases/GITHUB_RELEASE_BODY.md` 创建 GitHub Release。

上述动作需要维护者的 GitHub 归属与发布授权；在完成前不得声称已创建公开 Release 或已有可克隆的 GitHub 仓库。
