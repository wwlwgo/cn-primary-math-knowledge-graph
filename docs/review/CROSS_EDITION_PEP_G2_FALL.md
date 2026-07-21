# 人教版二年级上册跨版本对照

处理批次：阶段 5，批次 3。处理日期：2026-07-21。

本报告只记录独立撰写的跨版本观察，不复制教材原文、题目、答案、插图或完整目录。教材 PDF 保持在私有目录 `人教版/`，不进入 Git。

## 输入与核验

- 输入文件：`人教版/人教版数学2上-新版.pdf`
- 文件页数：106 页；未加密。
- 目录关键定位（印刷页）：分类与整理（1 起）、1～6 的表内乘法（10 起）、1～6 的表内除法（30 起）、校园小导游（49 起）、厘米和米（55 起）、身体上的尺子（68 起）、7～9 的表内乘除法（73 起）。
- 视觉核验：导入页、目录页和乘法主题起始页；PDF 页面序号与印刷页码存在偏移，报告只使用印刷页码。
- 来源限制：仅作私有交叉检验；不得将本报告解释为出版方授权或专家审核。

## 节点对照

| 现有 topicId | 状态 | 人教版定位 | 独立比较结论 | 不确定性 |
|---|---|---|---|---|
| `cn_math_g2_add_two_digit_numbers_with_regrouping` | not-located | 未在本册目录主题中定位 | 本册目录重点为表内乘除法和测量，未确认两位数进位加法映射。 | 未定位不是反证，需考虑其他册次或版本位置。 |
| `cn_math_g2_subtract_two_digit_numbers_with_regrouping` | not-located | 未在本册目录主题中定位 | 未确认两位数退位减法在本册的独立单元映射。 | 未定位不是反证。 |
| `cn_math_g2_measure_length_with_standard_unit` | supports | 二上，第 55-67 页范围 | 厘米和米主题直接支持标准单位测量目标。 | 具体测量活动不公开复刻。 |
| `cn_math_g2_represent_equal_groups` | supports | 二上，第 10-29 页范围 | 表内乘法主题支持等量分组的数量表征。 | 主题级证据，待关键页抽样。 |
| `cn_math_g2_interpret_multiplication_as_equal_groups` | supports | 二上，第 10-29 页范围 | 1～6 表内乘法范围支持用乘法表示等量分组。 | 不据教材顺序证明前置关系。 |
| `cn_math_g2_use_multiplication_facts_within_nine` | supports | 二上，第 10-29、73-90 页范围 | 1～6 和 7～9 表内乘法覆盖 9 以内口诀候选目标。 | 口诀组织粒度需后续抽样。 |
| `cn_math_g2_represent_equal_sharing_and_grouping_division` | supports | 二上，第 30-48、73-90 页范围 | 表内除法主题支持平均分和按组分的表征。 | 具体表征方式待抽样。 |
| `cn_math_g2_interpret_division_using_multiplication_relation` | supports | 二上，第 30-48、73-90 页范围 | 表内除法与乘法关系共同出现，支持整除关系解释目标。 | 不将共同编排升级为 hard。 |
| `cn_math_g2_model_multiplication_division_word_problems` | supports | 二上，第 10-48、73-90 页范围 | 乘除法单元提供情境建模的候选支持。 | 目录不能证明应用题覆盖完整。 |
| `cn_math_g2_estimate_length_using_benchmark` | supports | 二上，第 55-72 页范围 | 厘米和米、身体上的尺子提供基准估测长度的主题支持。 | 估测策略需关键页抽样。 |
| `cn_math_g2_identify_reflection_symmetry_by_folding` | not-located | 未在目录关键单元中定位 | 当前目录未单独出现轴对称或折叠辨认主题。 | 未定位不是反证。 |
| `cn_math_g2_describe_simple_position_and_route` | supports | 二上，第 49-54 页范围 | 校园小导游与位置、方向和路线描述有直接主题对应。 | 具体方向语言待抽样。 |
| `cn_math_g2_model_amount_relationships_in_shopping` | not-located | 未在目录关键单元中定位 | 本册目录未单列购物数量关系主题。 | 未定位不是反证，可能在其他册次出现。 |

## 统计

| 状态 | 数量 |
|---|---:|
| `supports` | 9 |
| `different-wording` | 0 |
| `different-granularity` | 0 |
| `not-located` | 4 |
| `conflicts` | 0 |

## 依赖边影响

本批次未新增、删除或升级依赖边。现有 19 条边继续保持 `soft`；表内乘除法的编排不能单独证明认知必要性。

## 待处理

- 对乘除法、测量和路线主题补充关键页抽样，确认表征粒度。
- 在二年级下册和三年级上册批次中继续追踪未定位的计算、对称和购物目标。
- 下一批处理人教版二年级下册。
