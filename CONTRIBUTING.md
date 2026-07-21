# 贡献指南

贡献前请阅读 `docs/DATA_STANDARD.md` 和 `docs/SOURCE_POLICY.md`。

每个数据变更应说明：变更的节点或边、课程标准/教材/研究来源、教育判断理由、审核状态，以及对已有图的影响。请勿提交教材扫描页、OCR 全文、习题全文或其他未经授权材料。

提交前运行：

```bash
python3 scripts/update_manifest.py
python3 scripts/validate_dataset.py
```

候选数据可通过 Issue 或 PR 公开复核，但须标明不确定性与支持/冲突来源。涉及拟升级为 `hard` 的边、节点合并或标准标识规则的改动需要数学教育审核；所有进入 `expert-verified` 范围的 `hard` 边须完成双人独立复核。建议将候选数据与已批准数据分开提交，避免未审核推断被误表述为专家确认结论。
