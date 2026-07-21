# 人教版一年级上册跨版本对照

处理批次：阶段 5，批次 1。处理日期：2026-07-21。

本报告只记录维护者独立撰写的跨版本观察，不复制教材原文、题目、答案、插图或完整目录。教材 PDF 保持在私有目录 `人教版/`，不进入 Git。

## 输入与核验

- 输入文件：`人教版/人教版数学1上-新版.pdf`
- 文件页数：118 页；未加密。
- 目录关键定位（印刷页）：5 以内数的认识和加减法（12 起）、6～10 的认识和加减法（34 起）、认识立体图形（67 起）、11～20 的认识（73 起）、20 以内的进位加法（88 起）。
- 视觉核验：目录页及 5 以内数单元关键页；PDF 页面序号与印刷页码存在偏移，报告只使用印刷页码。
- 来源限制：仅作私有交叉检验；不得将本报告解释为出版方授权或专家审核。

## 节点对照

| 现有 topicId | 状态 | 人教版定位 | 独立比较结论 | 不确定性 |
|---|---|---|---|---|
| `cn_math_g1_count_and_represent_quantities_within_ten` | supports | 一上，第 12-66 页范围 | 以数量、数词和数的书写建立 1-10 的数量表征，能力范围与现有目标一致。 | 目录级和关键页核验，未逐页建立活动清单。 |
| `cn_math_g1_compare_quantities_within_ten` | supports | 一上，第 12-66 页范围 | 同一低数域内的数量比较属于该册数概念学习范围，支持现有目标。 | 具体比较活动页待后续抽样复核。 |
| `cn_math_g1_compose_decompose_numbers_within_five` | supports | 一上，第 12-33 页范围 | 5 以内数的认识和加减法为分解、合成及数量关系提供对应范围。 | 未将教材练习结构作为依赖证据。 |
| `cn_math_g1_model_addition_as_combining_within_five` | supports | 一上，第 12-33 页范围 | 低数域加法单元支持将合并变化表征为加法的候选目标。 | 具体情境表达不公开复刻。 |
| `cn_math_g1_model_subtraction_as_removal_within_five` | supports | 一上，第 12-33 页范围 | 同一单元覆盖去除变化与减法表征，支持现有目标。 | 具体活动页待抽样复核。 |
| `cn_math_g1_calculate_add_subtract_within_five` | supports | 一上，第 12-33 页范围 | 5 以内数的加减法提供对应程序能力证据。 | 不据教材顺序推断 hard 关系。 |
| `cn_math_g1_compose_decompose_numbers_within_ten` | supports | 一上，第 34-66 页范围 | 6～10 的认识和加减法扩展了数的组成与分解范围，支持现有目标。 | 具体组成表征的页码需后续抽样。 |
| `cn_math_g1_calculate_add_subtract_within_ten` | supports | 一上，第 34-66 页范围 | 6～10 的认识和加减法与 10 以内加减计算目标相符。 | 20 以内进位加法另列为后续范围。 |
| `cn_math_g1_classify_objects_by_explicit_feature` | not-located | 未在目录关键单元中定位 | 当前目录与抽样页未提供足够证据确认该目标在本册的独立教学映射。 | 未定位不是反证；需后续逐页或补充版本核验。 |
| `cn_math_g1_identify_simple_solids_by_observable_features` | supports | 一上，第 67-72 页范围 | “认识立体图形”提供简单立体按可观察特征辨认的跨版本支持。 | 目录不能证明所有形状粒度完全一致。 |
| `cn_math_g1_order_events_within_a_day` | not-located | 未在目录关键单元中定位 | 本册目录未出现时间/日内顺序主题，暂不确认对应目标。 | 未定位不是反证，也不修改现有节点。 |

## 统计

| 状态 | 数量 |
|---|---:|
| `supports` | 9 |
| `different-wording` | 0 |
| `different-granularity` | 0 |
| `not-located` | 2 |
| `conflicts` | 0 |

## 依赖边影响

本批次未新增、删除或升级依赖边。现有 19 条边继续保持 `soft`；本册的目录级一致性不能证明认知必要性。

## 待处理

- 对两个 `not-located` 目标进行后续逐页抽样，不将“未定位”解释为教材缺失。
- 对 `supports` 目标补充少量关键页视觉核验，确认粒度和表征差异。
- 下一批处理人教版一年级下册。
