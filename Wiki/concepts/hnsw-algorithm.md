---
title: HNSW (Hierarchical Navigable Small World) Algorithm
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [concept, hnsw, ann, vector-search, graph-based-search, similarity-search, qdrant, milvus, weaviate, pinecone, intelligent-search]
sources:
  - raw/articles/intelligent-search-bible-2026-07-13.md
confidence: high
---

# HNSW (Hierarchical Navigable Small World)

## 定義

**HNSW** = Hierarchical Navigable Small World — 現代向量搜尋的主流 ANN（Approximate Nearest Neighbor）演算法。

```
核心概念：
- Small World：高 clustering coefficient + low average path length
- Hierarchical：多層 navigable graph
- 跳躍式搜尋：上層 sparse graph 快速縮小範圍 → 下層 dense graph 精確找鄰居
```

## 為什麼 HNSW 是主流？

| 演算法 | 速度 | 精度 | 記憶體 | 動態更新 | 主流度 |
|--------|------|------|--------|---------|--------|
| **HNSW** | ★★★★ | ★★★★ | ★★★ | ★★★★★ | ★★★★★ |
| IVF（Inverted File）| ★★★ | ★★★ | ★★★★ | ★★★ | ★★★ |
| PQ（Product Quantization）| ★★★★ | ★★ | ★★★★★ | ★★ | ★★★ |
| Annoy | ★★ | ★★★ | ★★★ | ★ | ★★ |
| FAISS flat | ★ | ★★★★★ | ★★ | ★ | ★ |

## 3 大關鍵參數

| 參數 | 意義 | 典型值 |
|------|------|--------|
| **M** | 每個 node 連接的最大邊數 | 16-64 |
| **ef_construction** | 建構時搜尋深度 | 100-200 |
| **ef** | 查詢時搜尋深度 | 50-200（越高 recall 越好）|

### 調優 trade-off

```
ef 越高 → recall 越高 + 延遲越高
M 越大 → 索引越大 + recall 越高
```

## 與 Hermes Layer 4c 對應

```
Layer 4c Vector Search:
  Embedding (sentence-transformers, 384d)
            ↓
  HNSW index (Qdrant / ChromaDB / Milvus)
            ↓
  ef = 50~100 (default)
            ↓
  Top-K retrieval + reranking
```

## 4 大 Vector DB 的 HNSW 實現

| DB | 語言 | HNSW 改進 |
|----|------|-----------|
| **Qdrant** | Rust | Filterable HNSW（filtering 階段一體化）|
| **Milvus** | C++/Go | Knowhere 框架（多演算法支援）|
| **Weaviate** | Go | HNSW + flat 混合 |
| **Pinecone** | 閉源 | proprietary index |

## Qdrant 的 Filterable HNSW 創新

```
傳統 HNSW：
  Search → Filter (post-filter，recall 降低)

Qdrant Filterable HNSW：
  Search + Filter (in-traversal，recall 維持)
```

效果：
- 過濾條件不影響 recall
- 延遲更低
- 支援複雜 nested filters

## 5 大常見錯誤（Hermes SOP 應用）

| # | 錯誤 | 後果 | 防護 |
|---|------|------|------|
| 1 | ef 設太低（< 32）| recall 太低 | 預設 ef ≥ 64 |
| 2 | M 設太大（> 128）| 記憶體爆炸 | M ≤ 64 |
| 3 | 沒做 quantization | 記憶體爆炸 | scalar quantization |
| 4 | ef_construction ≠ ef | 建構品質差 | ef_construction = 2 * ef |
| 5 | Index 不重建 | stale data | 定期 rebuild |

## 何時不適用 HNSW

| 場景 | 替代 |
|------|------|
| < 1K vectors | Flat search（無 ANN）|
| 需要 100% recall | Brute-force |
| 極低記憶體 | PQ + IVF |
| 即時 streaming | SCANN / Vamana |

## 引用

- Qdrant Filterable HNSW：https://qdrant.tech/articles/filterable-hnsw/
- Milvus HNSW：https://milvus.io/docs/index.md
- 原始論文：Malkov, Y. A., & Yashunin, D. A. (2018). *Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs*. TPAMI.

## 版本

| 版本 | 日期 | 變更 |
|------|------|------|
| v1.0 | 2026-07-13 | 初版（基於 Qdrant + Milvus 官方 + Stanford IR Book Ch 18）|