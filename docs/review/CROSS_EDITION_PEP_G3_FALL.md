# 人教版三年级上册跨版本对照

处理批次：阶段 5，批次 5。处理日期：2026-07-21。

教材 PDF 保持在私有目录 `人教版/`，本报告不复制教材原文、题目、答案、插图或完整目录。

## 输入与核验

- 输入文件：`人教版/人教版数学3上-新版.pdf`
- 文件页数：109 页；未加密。
- 目录关键定位（印刷页）：观察物体（1 起）、混合运算（6 起）、毫米、分米和千米（20 起）、多位数乘一位数（39 起）、数字编码（57 起）、线和角（61 起）、分数的初步认识（73 起）。
- 视觉核验：目录页和混合运算主题起始页；报告只使用印刷页码。

## 节点对照

| 现有 topicId | 状态 | 人教版定位 | 独立比较结论 | 不确定性 |
|---|---|---|---|---|
| `cn_math_g3_model_mixed_operations_from_context` | supports | 三上，第 6-19 页范围 | 混合运算主题直接支持从情境建立混合算式的候选目标。 | 具体情境不公开复刻。 |
| `cn_math_g3_select_operation_order_in_mixed_expression` | supports | 三上，第 6-19 页范围 | 混合运算主题支持运算顺序判断。 | 不据教材顺序证明依赖强度。 |
| `cn_math_g3_convert_metric_length_units` | supports | 三上，第 20-38 页范围 | 毫米、分米和千米主题支持长度单位换算候选。 | 单位间换算的细粒度待抽样。 |
| `cn_math_g3_measure_and_estimate_length_with_precision` | supports | 三上，第 20-38 页范围 | 长度单位主题支持测量和估测精度的候选目标。 | 具体估测策略待关键页核验。 |
| `cn_math_g3_add_three_digit_numbers_with_regrouping` | not-located | 未在目录关键单元中定位 | 本册目录未单列三位数进位加法主题。 | 未定位不是反证。 |
| `cn_math_g3_subtract_three_digit_numbers_with_regrouping` | not-located | 未在目录关键单元中定位 | 本册目录未单列三位数退位减法主题。 | 未定位不是反证。 |
| `cn_math_g3_identify_angle_by_vertex_and_rays` | supports | 三上，第 61-72 页范围 | 线和角主题支持按顶点和边辨认角的候选目标。 | 具体角的分类粒度待抽样。 |
| `cn_math_g3_model_multiplication_division_applications` | different-granularity | 三上，第 39-56 页范围 | 多位数乘一位数支持乘法程序和应用，但与“多步乘除法应用”目标的应用层粒度不完全等同。 | 需补充应用页抽样后决定是否拆分。 |
| `cn_math_g3_interpret_decimal_as_yuan_jiao_fen` | not-located | 未在目录关键单元中定位 | 本册目录未单列元角分或小数主题。 | 未定位不是反证。 |
| `cn_math_g3_read_write_compare_simple_decimals` | not-located | 未在目录关键单元中定位 | 本册目录未单列小数读写比较主题。 | 未定位不是反证。 |
| `cn_math_g3_collect_record_and_classify_data` | not-located | 未在目录关键单元中定位 | 本册目录未单列数据收集与分类主题。 | 未定位不是反证。 |
| `cn_math_g3_interpret_calendar_dates_and_intervals` | not-located | 未在目录关键单元中定位 | 本册目录未单列日历日期和间隔主题。 | 未定位不是反证。 |

## 统计

| 状态 | 数量 |
|---|---:|
| `supports` | 6 |
| `different-wording` | 0 |
| `different-granularity` | 1 |
| `not-located` | 5 |
| `conflicts` | 0 |

## 依赖边影响

本批次未新增、删除或升级依赖边。所有现有关系继续保持 `soft`。

## 待处理

- 对混合运算、长度、角和多位数乘法补充关键页抽样。
- 将未定位的小数、数据、日历和三位数加减目标交给后续册次继续追踪。
- 进入阶段 5 全局汇总和完成审计。
