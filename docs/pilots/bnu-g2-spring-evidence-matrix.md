# 北师大版二年级下册候选证据与诊断矩阵

状态：`draft`。本矩阵为候选层提供最小掌握证据和诊断提示；进入稳定数据时，每个节点仍须按其最终粒度写入独立 `evidence` 与 `assessmentPrompt`。

| 候选组 | 覆盖候选 | 最小掌握证据 | 诊断提示 |
| --- | --- | --- | --- |
| 位值与数表征 | `count_to_ten_thousand_by_units`、`place_value_within_ten_thousand`、`read_write_numbers_within_ten_thousand`、`compare_order_numbers_within_ten_thousand`、`locate_number_on_approximate_number_line` | 1. 在计数器/数位表上表示指定数并解释每位值。 2. 在符号、文字和数线三种表征之间转换或比较。 | “把 4,0,7,3 表示在数位表上，并说明两个 0 分别意味着什么；它在 4000 和 5000 之间的大致哪里？” |
| 加减计算与建模 | `sum_three_two_digit_numbers`、`subtract_two_parts_from_total`、`mixed_add_subtract_change`、`add_subtract_hundreds_tens_by_place_value`、`align_place_values_in_column_addition_subtraction`、`column_addition_with_regrouping`、`column_subtraction_with_regrouping`、`model_three_digit_add_subtract_word_problem` | 1. 正确计算陌生数值，过程中的数位对齐和进退位可解释。 2. 从新情境建立算式并以原情境检查结果合理性。 | “给出一个三位数量增减情境，请先画图或列式，再说明为什么此处要进位/退位。” |
| 有余数除法与约束决策 | `remainder_division_as_groups_and_leftover`、`calculate_division_with_remainder`、`remainder_less_than_divisor`、`find_largest_multiplier_under_limit`、`round_up_quotient_for_minimum_groups`、`round_down_quotient_for_maximum_groups`、`interpret_remainder_by_context` | 1. 用实物分组解释商和余数。 2. 面对“至少”和“最多”两种新问题，选择不同的商处理并说明余数去向。 | “23 人每车最多 5 人至少几车？23 元每件 5 元最多买几件？两题余数分别怎样处理，为什么？” |
| 立体与平面图形表征 | `construct_prism_or_cylinder_from_paper`、`identify_faces_of_simple_solids`、`control_cylinder_shape_with_paper_strip`、`recognize_solids_from_views`、`unfold_and_reconstruct_cuboid`、`predict_faces_when_cuboid_rolls`、`identify_parallelogram_by_features`、`construct_parallelogram_from_parts`、`recognize_parallelogram_invariance_under_shear`、`compose_target_shapes_with_tangram`、`decompose_tangram_by_adjacency_and_size` | 1. 在不同材料、方向或拼法中辨认目标图形。 2. 通过构造、展开或拼合解释平面与立体/组成部分的关系。 | “给出一个与教材不同的纸盒或拼图，要求说明它由哪些面组成、如何展开/拼回，并解释判断依据。” |
| 策略、推理、分类与测量 | `compare_totals_in_three_round_context`、`model_remaining_capacity`、`compare_opposite_changes_before_calculation`、`explain_alternative_compensation_for_subtraction`、`estimate_large_collections_using_benchmark`、`convert_time_units_for_duration`、`record_and_compare_event_durations`、`solve_logic_grid_by_constraints`、`classify_by_explicit_criterion`、`refine_classification_by_second_criterion`、`select_body_measure_for_length_estimation`、`measure_consistently_with_nonstandard_unit` | 1. 在未见过的材料中选择并说明策略。 2. 比较两种方案或结果，说明条件变化对答案的影响。 | “请选一种方法解决此问题，并说明另一种方法何时更合适；改变一个条件后，答案是否变化？” |

## 审查约束

- 同一候选至少须满足其组内两条证据，且不得只复述教材数值。
- “解释”必须能指向表征、数量关系、限制条件或验证方法之一。
- 若候选无法用独立提示诊断，应与相邻候选合并或降为掌握证据，而不是创建节点。
