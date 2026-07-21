# 北师大版二年级下册候选依赖总表

状态：`draft`。本表是阶段 2 的候选边，不进入 `data/dependencies.json`；每条 `hard` 边必须在阶段 3 由独立教育审核者复核。

| 目标 | 前置 | 强度 | 理由 |
| --- | --- | --- | --- |
| `compare_totals_in_three_round_context` | `sum_three_two_digit_numbers` | hard | 必须先获得三轮总分，才能按总分比较结果。 |
| `model_remaining_capacity` | `subtract_two_parts_from_total` | hard | 模型求解的核心计算是从总量中连续移除两部分。 |
| `compare_opposite_changes_before_calculation` | `mixed_add_subtract_change` | soft | 可先比较增减量预测方向，但也可直接计算后判断。 |
| `calculate_division_with_remainder` | `remainder_division_as_groups_and_leftover` | hard | 计算符号需建立在商和余数的分组含义上。 |
| `remainder_less_than_divisor` | `calculate_division_with_remainder` | hard | 需通过分组结果理解余数不能再组成完整一组。 |
| `find_largest_multiplier_under_limit` | `calculate_division_with_remainder` | hard | 寻找最大可行乘数依赖有余数分组计算。 |
| `round_up_quotient_for_minimum_groups` | `interpret_remainder_by_context` | hard | 是否增加一组由余数在容量情境中的含义决定。 |
| `round_down_quotient_for_maximum_groups` | `interpret_remainder_by_context` | hard | 是否舍去余数由资源限额情境决定。 |
| `place_value_within_ten_thousand` | `count_to_ten_thousand_by_units` | hard | 各位值建立在十进制单位递进上。 |
| `read_write_numbers_within_ten_thousand` | `place_value_within_ten_thousand` | hard | 读写数字需能解释各数位的值。 |
| `compare_order_numbers_within_ten_thousand` | `place_value_within_ten_thousand` | hard | 比较大小依赖最高不同数位的位值。 |
| `locate_number_on_approximate_number_line` | `compare_order_numbers_within_ten_thousand` | soft | 比较大小有助于定位，但可借刻度和估算策略直接完成。 |
| `column_addition_with_regrouping` | `align_place_values_in_column_addition_subtraction` | hard | 进位竖式必须在相同数位上相加。 |
| `column_subtraction_with_regrouping` | `align_place_values_in_column_addition_subtraction` | hard | 退位竖式必须在相同数位上相减。 |
| `model_three_digit_add_subtract_word_problem` | `column_addition_with_regrouping` | soft | 建模可使用其他算法，竖式是常见而非唯一计算路径。 |
| `unfold_and_reconstruct_cuboid` | `identify_faces_of_simple_solids` | hard | 展开和还原要辨识立体的面及其相邻关系。 |
| `predict_faces_when_cuboid_rolls` | `identify_faces_of_simple_solids` | soft | 可通过实物操作预测，不必先掌握抽象面关系。 |
| `construct_parallelogram_from_parts` | `identify_parallelogram_by_features` | soft | 可尝试拼搭再归纳特征，先验辨认会提高成功率。 |
| `refine_classification_by_second_criterion` | `classify_by_explicit_criterion` | hard | 分层分类先要能依据一条标准完成初次分类。 |
| `measure_consistently_with_nonstandard_unit` | `select_body_measure_for_length_estimation` | hard | 一致测量必须先选定合适且可重复使用的单位。 |
| `record_and_compare_event_durations` | `convert_time_units_for_duration` | hard | 汇总或比较以时、分、秒表示的时长需能统一单位。 |

## 外部前置缺口

其余候选主要依赖一年级或上册已学的基本加减、表内乘除、平面图形、长度单位等能力。阶段 2 只记录缺口，不凭常识补造正式跨年级节点；这些节点将在后续教材输入到位后建立。
