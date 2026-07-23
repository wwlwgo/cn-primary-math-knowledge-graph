# 中国小学数学知识图谱

> 面向中国义务教育阶段小学数学（1-6 年级）的、可追溯且可验证的微知识点依赖数据集。

本项目提供的是基础设施数据，不是教材、题库或教学应用。它回答的核心问题是：学习一个知识点之前，哪些能力是必要前提？数据可被诊断工具、学习路径规划器、教师工具和 AI 助教直接读取。

## 项目状态

项目处于 `0.x` 建设阶段。当前公开候选版本为 `candidate-0.3.0-cross-edition`，包含 95 个 `reviewed` 节点、18 条 `soft` 依赖、19 个课程标准能力锚点和 56 条课程标准登记。该候选层使用国内小学数学教材的私有核验材料与课程标准建立，仓库不包含教材原件、原文、OCR 或逐页复刻，也不代表任何教材出版方的官方数据。完整来源记录仅用于维护者内部审计；公开数据保留必要的可追溯定位。审计见 [三年级下册扩展审计](docs/review/PHASE_5_4_G3_SPRING_AUDIT.md)。

## 设计原则

- **学习目标优先**：节点表达可观察、可评估的学习目标，而不是教材标题或一道题。
- **证据可追溯**：每一个节点和边都必须可追溯到课程标准、教材活动、教辅材料或审核结论，并声明其证据层级。
- **区分必需与有益**：`hard` 表示学习所必需的前提，`soft` 表示显著有帮助但可替代的经验。
- **教材版本无关**：教材是重要证据来源，不是唯一真相；同一概念可映射到多个版本与学期。
- **数据先行**：核心数据为 JSON，验证工具只使用 Python 标准库，不要求运行服务。
- **应用契约优先**：应用只依赖稳定 ID、能力锚点和版本化关系，不依赖教材页码、单元或具体表述。

## 仓库结构

```text
data/                  已发布的数据集与版本清单
schemas/               机器可读的数据契约（JSON Schema）
scripts/               数据集校验器
docs/                  路线图、数据标准、来源与治理规则
```

## 快速开始

```bash
python3 scripts/validate_dataset.py
```

当前命令验证数据结构和图的完整性。数据集发布后，以下查询可以直接在任何语言中实现：

- 某知识点的直接或递归前置能力
- 已掌握知识点可解锁的后续目标
- 年级或课程标准范围内的学习目标
- 缺失 `hard` 前置能力导致的风险项

仓库内置了可复现的参考查询：

```bash
python3 scripts/query_dataset.py prerequisites cn_math_g2_model_three_digit_add_subtract_word_problem
python3 scripts/query_dataset.py unlocks cn_math_g2_identify_faces_of_simple_solids
python3 scripts/query_dataset.py grade G2
```

修改 `data/topics.json`、`data/dependencies.json` 或 `data/standards.json` 后，先运行 `python3 scripts/update_manifest.py`，再运行校验器。

## 首个里程碑

当前公开候选版本为 `candidate-0.3.0-cross-edition`：它覆盖一上至三下六册范围的自动化候选数据，并完成双版本私有核验范围内的课标能力锚点重算。该版本具有可追溯来源并通过自动校验，但仍待独立教育复核。该版本不依赖专家校审。首个 `expert-verified` 版本在此基础上逐批升级，全部 `hard` 边须完成双人领域审核。后续将在四年级新版教材或合法引用资源到位后继续扩展。

课程标准的规范性发布来源为教育部 `教材〔2022〕2号`，见中国政府网的[发布通知](https://www.gov.cn/zhengce/zhengceku/2022-04/21/content_5686535.htm)。项目内的稳定标识及来源记录见 [课标登记册](docs/STANDARDS_REGISTRY.md)。

## 参与方式

请先阅读 [数据标准](docs/DATA_STANDARD.md)、[质量与治理](docs/QUALITY_AND_GOVERNANCE.md) 和 [贡献指南](CONTRIBUTING.md)。欢迎提交教材映射、标准映射、边的审核意见和验证用例。

项目中的关键决策、验证结果、踩坑和待办持续记录在[开发日志](docs/DEVELOPMENT_LOG.md)。

从教材建立候选数据时遵循[教材抽取协议](docs/EXTRACTION_PROTOCOL.md)，确保候选推断与发布数据分离。

候选发布、跨教材交叉检验、社区复核和专家确认的边界见[证据与复核框架](docs/EVIDENCE_AND_REVIEW_FRAMEWORK.md)。

建设应用案例前请阅读[应用集成契约](docs/APPLICATION_INTEGRATION_CONTRACT.md)。

## 许可

代码采用 [MIT License](LICENSE)。公开数据将采用数据库与自有文字分层许可，第三方课程标准保留上游条款；详见 [数据许可策略](DATA_LICENSE.md)、[来源声明](PROVENANCE.md) 和 [版权风险审计](docs/IP_RISK_AUDIT.md)。教材原文、扫描页和未经授权的 OCR 文本不进入本仓库。

本项目借鉴了 [Marble Skill Taxonomy](https://github.com/withmarbleapp/os-taxonomy) 的数据发布与校验治理方式，但不复制其数据或内容；审读结论见 [参考项目审读记录](docs/REFERENCE_REVIEW_MARBLE.md)。

候选版本的范围、限制、许可和发布复现步骤见[发布说明](docs/releases/CANDIDATE_0.3.0_CROSS_EDITION.md)与[发布准备审计](docs/releases/CANDIDATE_0.3.0_CROSS_EDITION_RELEASE_AUDIT.md)。
