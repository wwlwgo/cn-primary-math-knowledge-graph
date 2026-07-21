# 人教版二年级下册跨版本对照

处理批次：阶段 5，批次 4。处理日期：2026-07-21。

教材 PDF 保持在私有目录 `人教版/`，本报告不复制教材原文、题目、答案、插图或完整目录。

## 输入与核验

- 输入文件：`人教版/人教版数学2下-新版.pdf`
- 文件页数：106 页；未加密。
- 目录关键定位（印刷页）：时间在哪里（1 起）、有余数的除法（10 起）、数量间的乘除关系（24 起）、万以内数的认识（40 起）、万以内的加法和减法（63 起）、数学连环画（83 起）。
- 视觉核验：目录页；报告只使用印刷页码。

## 节点对照

| 状态 | 现有候选（按主题分组） | 人教版定位与独立结论 |
|---|---|---|
| `supports` | `cn_math_g2_remainder_division_as_groups_and_leftover`; `cn_math_g2_calculate_division_with_remainder`; `cn_math_g2_remainder_less_than_divisor`; `cn_math_g2_find_largest_multiplier_under_limit`; `cn_math_g2_round_up_quotient_for_minimum_groups`; `cn_math_g2_round_down_quotient_for_maximum_groups`; `cn_math_g2_interpret_remainder_by_context` | 有余数的除法（10-23）和数量间的乘除关系（24-39）直接支持分组、余数、商的解释及情境化处理。具体策略粒度待关键页抽样。 |
| `supports` | `cn_math_g2_count_to_ten_thousand_by_units`; `cn_math_g2_place_value_within_ten_thousand`; `cn_math_g2_read_write_numbers_within_ten_thousand`; `cn_math_g2_compare_order_numbers_within_ten_thousand`; `cn_math_g2_locate_number_on_approximate_number_line`; `cn_math_g2_estimate_large_collections_using_benchmark` | 万以内数的认识（40-62）支持单位计数、位值、读写、比较及数量估计候选。数线和估计的具体表征需后续抽样。 |
| `supports` | `cn_math_g2_add_subtract_hundreds_tens_by_place_value`; `cn_math_g2_align_place_values_in_column_addition_subtraction`; `cn_math_g2_column_addition_with_regrouping`; `cn_math_g2_column_subtraction_with_regrouping`; `cn_math_g2_explain_alternative_compensation_for_subtraction`; `cn_math_g2_model_three_digit_add_subtract_word_problem` | 万以内加法和减法（63-82）支持位值对齐、竖式计算、策略解释和三位数情境建模。未将教材顺序转为 hard。 |
| `supports` | `cn_math_g2_convert_time_units_for_duration`; `cn_math_g2_record_and_compare_event_durations` | 时间在哪里（1-9）提供时间定位和时长比较的主题支持；单位换算的精确粒度待抽样。 |
| `not-located` | `cn_math_g2_sum_three_two_digit_numbers`; `cn_math_g2_compare_totals_in_three_round_context`; `cn_math_g2_subtract_two_parts_from_total`; `cn_math_g2_model_remaining_capacity`; `cn_math_g2_mixed_add_subtract_change`; `cn_math_g2_compare_opposite_changes_before_calculation` | 本册目录未单列这些具体情境目标，暂不确认独立映射；未定位不是反证。 |
| `not-located` | `cn_math_g2_construct_prism_or_cylinder_from_paper`; `cn_math_g2_identify_faces_of_simple_solids`; `cn_math_g2_control_cylinder_shape_with_paper_strip`; `cn_math_g2_recognize_solids_from_views`; `cn_math_g2_unfold_and_reconstruct_cuboid`; `cn_math_g2_predict_faces_when_cuboid_rolls` | 本册目录未单列简单立体和展开观察主题，暂不确认映射。 |
| `not-located` | `cn_math_g2_identify_parallelogram_by_features`; `cn_math_g2_construct_parallelogram_from_parts`; `cn_math_g2_recognize_parallelogram_invariance_under_shear`; `cn_math_g2_compose_target_shapes_with_tangram`; `cn_math_g2_decompose_tangram_by_adjacency_and_size` | 本册目录未单列平行四边形或拼图主题，暂不确认映射。 |
| `not-located` | `cn_math_g2_solve_logic_grid_by_constraints`; `cn_math_g2_classify_by_explicit_criterion`; `cn_math_g2_refine_classification_by_second_criterion`; `cn_math_g2_select_body_measure_for_length_estimation`; `cn_math_g2_measure_consistently_with_nonstandard_unit` | 本册目录未单列条件推理、分类或非标准测量主题，暂不确认映射。 |

## 统计

| 状态 | 数量 |
|---|---:|
| `supports` | 21 |
| `different-wording` | 0 |
| `different-granularity` | 0 |
| `not-located` | 22 |
| `conflicts` | 0 |

注：统计按现有 43 个二年级下册相关候选的登记结果核对；若候选清单后续发生拆分或合并，需同步修订本表。

## 依赖边影响

本批次未新增、删除或升级依赖边。所有现有关系继续保持 `soft`。

## 待处理

- 对有余数除法、万以内数和加减法补充关键页抽样。
- 将未定位项与三年级上册及其他版本继续追踪，不把未定位视为冲突。
- 下一批处理人教版三年级上册。
