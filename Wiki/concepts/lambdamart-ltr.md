---
title: LambdaMART Learning to Rank Algorithm
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [concept, lambdamart, lambdarank, ranknet, learning-to-rank, ltr, microsoft-research, burges-2010, ranking, hermes-search-precision, layer-4c]
sources:
  - raw/articles/web-search-precision-bible-2026-07-13.md
confidence: high
---

# LambdaMART Learning to Rank Algorithm

## 定義

**LambdaMART** = LambdaRank + MART（Multiple Additive Regression Trees）
= 現代 web search 排序學習的主流算法
= Microsoft Bing production ranker

起源：**Burges et al. 2006-2010**，Yahoo! 2010 LTR Challenge Track 1 冠軍

## 演進樹

```
RankNet (Burges 2005)
   ↓ 引入 pairwise sigmoid + cross-entropy
LambdaRank (Burges 2006)
   ↓ 用 NDCG 增益直接定義 λ gradient
LambdaMART (Burges 2007)
   ↓ 用 MART 框架實作
Yahoo! 2010 Challenge Winner
```

## LambdaMART vs LambdaRank vs RankNet

| 算法 | 框架 | 優化目標 | 速度 |
|------|------|---------|------|
| **RankNet** | Neural Net | Pairwise CE | ★★ |
| **LambdaRank** | 啟發式 | NDCG 增益 | ★★★ |
| **LambdaMART** | Gradient Boosted Trees | NDCG 增益 | ★★★★（生產級）|

## 4 大關鍵公式

### 1. RankNet Pairwise Probability

```
P_ij = 1 / (1 + exp(-σ(s_i - s_j)))
```

兩文檔 i, j 的相關性機率（sigmoid）。

### 2. Cross-Entropy Cost

```
C = -P̄_ij log P_ij - (1 - P̄_ij) log(1 - P_ij)
```

### 3. Lambda Force

```
λ_ij = ∂C/∂s_i = σ((1 - S_ij)/2 - 1/(1 + exp(σ(s_i - s_j))))
```

每個 URL 的「箭頭力」，決定排序方向。

### 4. NDCG Lambda（LambdaRank 關鍵）

```
λ_ij = -σ / (1 + exp(σ(s_i - s_j))) × |ΔNDCG|
```

直接以 NDCG 變化作為 gradient force（**理論保證 NDCG 提升**）。

## LambdaMART 訓練流程

```
1. 初始化：f_0(x) = arg min Σ L(y_i, f)
2. For t = 1 to T:
   a. 計算每對 (i, j) 的 λ_ij（用 NDCG 增益）
   b. 每個 URL i 累積 λ_i = Σ_{j} λ_ij - Σ_{k} λ_ki
   c. 用 regression tree 擬合 {x_i, λ_i}
   d. 更新：f_t(x) = f_{t-1}(x) + η × tree(x)
3. 輸出：F(x) = Σ_t α_t × tree_t(x)
```

## 4 大超參數

| 參數 | 預設 | 影響 |
|------|------|------|
| **num_leaves** | 64 | 樹葉數（複雜度）|
| **num_trees** | 500 | 樹數量（過多 overfitting）|
| **learning_rate** | 0.1 | 學習率 |
| **min_data_in_leaf** | 10 | 葉最少文檔數 |

## 6 大訓練特徵（Web Search）

| Feature | 計算 |
|---------|------|
| **TF-IDF cosine** | query-doc 向量相似度 |
| **BM25 score** | BM25(q, d) |
| **PageRank** | link analysis |
| **Domain authority** | inbound link count |
| **Freshness** | now - doc.mtime |
| **Click-through rate** | log(CTR) |

## LambdaMART vs BM25 對比

| 場景 | BM25 | LambdaMART |
|------|------|------------|
| 簡單 keyword search | ★★★★ | ★★★ |
| 多特徵融合 | ★ | ★★★★★ |
| 訓練成本 | 零 | 高（需 labeled data）|
| 可解釋性 | ★★★★★ | ★★ |
| NDCG@10 | 0.5-0.7 | 0.7-0.9 |
| 速度 | 極快 | 較慢 |

## 與 Hermes Layer 4c 對應

```
Layer 4c Vector Search:
  Qdrant Hybrid Search
            ↓
  Top-100 candidates
            ↓
  LambdaMART reranker ← ★ 新增
            ↓
  Top-10 final
```

### Hermes 升級路徑

```
v2.0（當前）：
  Qdrant → Hybrid Top-100 → MMR → Top-10

v3.0（升級）：
  Qdrant → Hybrid Top-100 → LambdaMART → MMR → Top-5
```

## 6 大應用場景

| 場景 | LambdaMART 適用 |
|------|-----------------|
| **Google Search** | ✅ Production |
| **Bing Search** | ✅ Production（微軟自研）|
| **Elasticsearch** | ✅ Plugin 支援 |
| **Solr** | ✅ Learning To Rank plugin |
| **Amazon Search** | ✅ Internal |
| **Personalized Feed** | ✅ 主流方法 |

## 何時不適用

| 不適用 | 替代 |
|--------|------|
| < 1K 文檔 | BM25 |
| 沒有訓練數據 | BM25 + 手調權重 |
| < 100 queries | Unsupervised fusion（CombSUM/RRF）|
| 即時 0 訓練 | Online bandit |

## 引用

- Burges, C. J. C. (2010). *From RankNet to LambdaRank to LambdaMART: An Overview*. MSR-TR-2010-82.
- Manning, C. D., Raghavan, P., & Schütze, H. (2008). *Introduction to Information Retrieval*. Ch 15.
- Lucidworks (2026). *The ABCs of Learning to Rank*.

## 版本

| 版本 | 日期 | 變更 |
|------|------|------|
| v1.0 | 2026-07-13 | 初版（基於 Microsoft Research + Stanford IR + Lucidworks）|