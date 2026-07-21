# candidate-0.2.0-vertical

## Candidate Data Release

This release contains a machine-validated candidate knowledge graph for BNU Press primary mathematics: Grade 1 fall/spring, Grade 2 fall/spring, and Grade 3 fall.

- 91 reviewed learning-goal nodes
- 19 soft, non-necessary dependency hypotheses
- 56 indexed entries from the 2022 curriculum standard

This is not an expert-verified educational standard. It contains no hard edges and no approved data. See `docs/releases/CANDIDATE_0.2.0_VERTICAL.md` for scope, limitations, license, provenance, and the cross-edition review queue.

## Reproduce

```bash
python3 scripts/validate_dataset.py
python3 scripts/check_release_tree.py
python3 scripts/query_dataset.py prerequisites cn_math_g3_model_mixed_operations_from_context --recursive
python3 scripts/query_dataset.py unlocks cn_math_g2_represent_equal_sharing_and_grouping_division --recursive
python3 scripts/query_dataset.py grade G3
```
