# candidate-0.3.0-cross-edition

## Candidate Data Release

This release contains a machine-validated candidate knowledge graph for Chinese primary mathematics, expanded through Grade 3 spring and recalculated across two private textbook-edition evidence ranges.

- 95 reviewed learning-goal nodes
- 18 soft, non-necessary dependency hypotheses
- 19 curriculum capability anchors
- 56 indexed entries from the 2022 curriculum standard
- 18/19 capability anchors supported across the current two-edition private evidence range
- 79/87 diagnostic nodes directly confirmed across the current two-edition private evidence range
- 0 open review-queue items in the current Grade 1 fall to Grade 3 spring scope

This is not an expert-verified educational standard. It contains no hard edges and no approved data. The repository does not include textbook scans, OCR, exercises, answers, or private input files. See `docs/releases/CANDIDATE_0.3.0_CROSS_EDITION.md` for scope, limitations, license, provenance, and the cross-edition review queue.

## Reproduce

```bash
python3 scripts/validate_dataset.py
python3 scripts/check_release_tree.py
python3 scripts/query_dataset.py prerequisites cn_math_g3_model_mixed_operations_from_context --recursive
python3 scripts/query_dataset.py unlocks cn_math_g2_represent_equal_sharing_and_grouping_division --recursive
python3 scripts/query_dataset.py grade G3
```
