# 阶段 5.1 输入审计

审计日期：2026-07-22。范围为当前 91 个候选节点、19 条初始 `soft` 依赖和 2022 年课程标准登记册。

## 前置条件结论

开始审计时，仓库缺少能力锚点表、节点层级、迁移记录和相应机器校验，因此不具备重算跨版本交集的条件。该缺口已作为阶段 5.1 的输入问题处理，而非继续沿用同册教材统计。

## 校准产物

| 项目 | 结果 |
| --- | --- |
| 课程标准条目到能力锚点 | `data/capability_anchors.json`，17 个锚点；均由已登记的具体课程标准条目生成 |
| 节点锚定 | 91/91 节点具有 `capabilityAnchor` 和至少一个具体课程标准 ID |
| 节点层级 | 83 个 `diagnostic` 节点；8 个 `implementation_evidence` 节点 |
| 数据契约 | `schemas/capability-anchor.schema.json`、`schemas/topic.schema.json` 和校验器已增加锚点及层级门禁 |
| 依赖审查 | 1 条指向教材实现证据的边移出公开依赖图；保留 18 条 `soft` 边，端点均为 `diagnostic` 节点 |

## 不纳入跨版本节点重合率的实现证据

下列 ID 保留用于历史追溯和私有教材证据，但不作为稳定能力节点参与阶段 5.2 的节点交集分母：

| 旧 ID | 处理决定 | 原因 |
| --- | --- | --- |
| `cn_math_g1_order_events_within_a_day` | 降为实现证据 | 日内事件排序是综合活动中的局部呈现，不作为本轮数学校准范围的稳定微能力。 |
| `cn_math_g2_compare_totals_in_three_round_context` | 降为实现证据 | 特定轮次总量情境应归入一般数量关系建模证据。 |
| `cn_math_g2_model_remaining_capacity` | 降为实现证据 | 容量情境是加减数量关系的教材实现。 |
| `cn_math_g2_compare_opposite_changes_before_calculation` | 降为实现证据 | 计算前预测策略是特定教学路径，不独立定义稳定能力边界。 |
| `cn_math_g2_control_cylinder_shape_with_paper_strip` | 降为实现证据 | 材料操作的特定方式不应等同于空间观念节点。 |
| `cn_math_g2_explain_alternative_compensation_for_subtraction` | 降为实现证据 | 补偿算法是算法偏好，不能作为跨版本核心节点。 |
| `cn_math_g2_solve_logic_grid_by_constraints` | 降为实现证据 | 特定条件表格活动需更强的课标和跨版本证据后才可进入稳定图。 |
| `cn_math_g2_model_amount_relationships_in_shopping` | 降为实现证据 | 购物是数量关系建模的情境，不单独构成稳定节点。 |

## 依赖迁移

`cn_math_g2_compare_opposite_changes_before_calculation <- cn_math_g2_mixed_add_subtract_change` 已从 `data/dependencies.json` 移出，因为目标节点现为 `implementation_evidence`。该判断保留在开发日志和本审计中；未改变其他已发布 ID。

## 结论

阶段 5.1 的前置结构已满足阶段 5.2 的最低输入要求：可比较单位是课标锚定的能力，而不是教材目录或单个活动。课程标准锚点仍较宽，阶段 5.2 必须把其结果明确标注为候选验证，不得解释为专家确认。
