# 人教版一年级下册跨版本对照

处理批次：阶段 5，批次 2。处理日期：2026-07-21。

本报告只记录独立撰写的跨版本观察，不复制教材原文、题目、答案、插图或完整目录。教材 PDF 保持在私有目录 `人教版/`，不进入 Git。

## 输入与核验

- 输入文件：`人教版/人教版数学1下-新版.pdf`
- 文件页数：93 页；未加密。
- 目录关键定位（印刷页）：认识平面图形（1 起）、20 以内的退位减法（8 起）、100 以内数的认识（23 起）、100 以内的口算加减法（43 起）、100 以内的笔算加减法（56 起）、数量间的加减关系（69 起）、欢乐购物街（77 起）。
- 视觉核验：目录页、平面图形关键页和退位减法单元起始页；PDF 页面序号与印刷页码存在偏移，报告只使用印刷页码。
- 来源限制：仅作私有交叉检验；不得将本报告解释为出版方授权或专家审核。

## 节点对照

| 现有 topicId | 状态 | 人教版定位 | 独立比较结论 | 不确定性 |
|---|---|---|---|---|
| `cn_math_g1_count_and_represent_numbers_within_twenty` | supports | 一下，第 23-42 页范围 | 100 以内数的认识覆盖 20 以内数量表征，支持现有目标。 | 具体表征活动尚未逐页登记。 |
| `cn_math_g1_compose_decompose_numbers_for_make_ten` | different-granularity | 一下，第 8-22 页范围 | 退位减法单元支持通过十的结构处理低数域计算，但其策略粒度与“用凑十进行组成分解”不完全等同。 | 需后续抽样区分凑十、破十及其他策略。 |
| `cn_math_g1_calculate_addition_within_twenty_by_make_ten` | different-granularity | 一下，第 8-22、43-55 页范围 | 本册有 20 以内计算和口算加减安排，但目录不能确认“凑十”是唯一或稳定的程序目标。 | 不据教材标题确认具体算法策略。 |
| `cn_math_g1_construct_plane_shapes_by_trace_or_compose` | supports | 一下，第 1-7 页范围 | 认识平面图形单元提供描画、辨认和组合平面图形的对应证据。 | 组合活动的粒度需后续抽样。 |
| `cn_math_g1_model_subtraction_within_twenty` | supports | 一下，第 8-22 页范围 | 20 以内退位减法单元支持低数域减法情境和数量关系建模。 | 不复制具体情境或题目。 |
| `cn_math_g1_calculate_subtraction_within_twenty_by_decomposition` | supports | 一下，第 8-22 页范围 | 退位减法主题与分解计算候选目标一致，支持程序层映射。 | 具体分解方式需逐页确认。 |
| `cn_math_g1_count_by_ones_tens_and_fives_within_hundred` | supports | 一下，第 23-42 页范围 | 100 以内数的认识支持按不同计数单位组织数量。 | 目录级证据不足以区分所有计数单位。 |
| `cn_math_g1_read_write_compare_numbers_within_hundred` | supports | 一下，第 23-42 页范围 | 100 以内数单元与读写、比较数的候选目标相符。 | 具体比较活动待抽样。 |
| `cn_math_g1_locate_numbers_on_hundred_number_line` | supports | 一下，第 23-42 页范围 | 100 以内数的认识提供数的顺序与位置表征的潜在支持。 | 目录未单独列出数线，暂按保守支持记录并列为待细化。 |
| `cn_math_g1_add_subtract_tens_within_hundred` | supports | 一下，第 43-55 页范围 | 100 以内口算加减法覆盖整十数加减的候选程序范围。 | 未据目录推断具体算法。 |
| `cn_math_g1_add_subtract_two_digit_numbers_without_regrouping` | supports | 一下，第 56-68 页范围 | 100 以内笔算加减法覆盖两位数加减的程序范围。 | 进退位边界需后续逐页抽样。 |
| `cn_math_g1_identify_and_compose_basic_plane_shapes` | supports | 一下，第 1-7 页范围 | 平面图形单元支持基本图形辨认及组合目标。 | 具体图形集合可能存在版本粒度差异。 |

## 统计

| 状态 | 数量 |
|---|---:|
| `supports` | 10 |
| `different-wording` | 0 |
| `different-granularity` | 2 |
| `not-located` | 0 |
| `conflicts` | 0 |

## 依赖边影响

本批次未新增、删除或升级依赖边。现有 19 条边继续保持 `soft`；教材章节标题和策略差异不能证明认知必要性。

## 待处理

- 对“凑十”“破十”和一般分解策略做关键页抽样，确认是否需要拆分或合并候选目标。
- 对 100 以内数线定位和笔算进退位边界补充视觉证据。
- 下一批处理人教版二年级上册。
