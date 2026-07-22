# 阶段 5.1 节点与依赖迁移说明

本迁移不删除历史 ID。每个既有节点新增两个字段：

- `capabilityAnchor`：链接至 `data/capability_anchors.json` 中由课程标准内容要求定义的稳定能力锚点。
- `modelLayer`：`diagnostic` 表示参与候选图谱和跨版本节点比较；`implementation_evidence` 表示保留为私有教材实现或策略证据，不参与节点交集统计。

已发布的节点 ID 不复用。处于 `implementation_evidence` 的 ID 不再接受新的依赖边，也不应被后续公开查询作为稳定能力结论。

依赖迁移：初始 19 条 `soft` 边中 1 条因端点降层而移出，当前保留 18 条 `soft` 边。没有新增 `hard` 边，没有 `approved` 数据。
