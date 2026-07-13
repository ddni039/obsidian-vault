---
title: Karpathy vs Hermes Tri-Role
created: 2026-06-11
updated: 2026-06-11
type: comparison
tags: [comparison, guideline, karpathy, hermes, tri-role]
sources: [raw/articles/karpathy-llm-wiki-2026.md]
---

# Karpathy vs Hermes Tri-Role

Karpathy LLM guidelines 與 Hermes 三角色（文謀/工匠/御史）的對齊分析。

## 對齊矩陣

| Karpathy Guideline | 對應 Hermes 角色 | 對齊程度 |
|-------------------|-----------------|---------|
| Think Before Coding | [[文謀]] | ★★★★★ 完全一致 |
| Simplicity First | [[文謀]] | ★★★★★ 完全一致 |
| Surgical Changes | [[工匠]] | ★★★★☆ 高度一致 |
| Goal-Driven Execution | [[御史]] | ★★★★★ 完全一致 |

## 詳細分析

### Think Before Coding ↔ 文謀

兩者核心都是「思」先於「行」：
- Karpathy：「不明確就停，命名困惑，提出來」
- 文謀：「先思後行，不明假設就提問、模糊就澄清」

Karpathy 偏向**懷疑主義**（懷疑自己的假設），文謀偏向**全局觀**（看大方向）。

### Simplicity First ↔ 文謀

兩者都強調最小化：
- Karpathy：「200行能做完就不要寫200行」「不提供未被要求的彈性」
- 文謀：「精簡結構，最小化，杜絕過度設計」

兩者完全一致，是同一原則的不同錶述。

### Surgical Changes ↔ 工匠

Karpathy 的「只碰必須碰的」對應工匠的「精準擊發」。但工匠多了一層紀律：
- 工匠有**反思迴圈**（目標→執行→反思→修正→驗證）
- Karpathy 沒有明確對應這層

### Goal-Driven Execution ↔ 御史

兩者都強調**可驗證的標準**：
- Karpathy：「強成功標準讓你獨立循環」
- 御史：「不接受差不多，需有可驗證通過標準」

兩者完全一致。

## 結論

Karpathy guidelines 與 Hermes 三角色的精神完全對齊，差異在於：
- Karpathy 偏向**個人工程師視角**（懷疑、收斂）
- Hermes 三角色偏向**協作治理視角**（分工、制衡）
