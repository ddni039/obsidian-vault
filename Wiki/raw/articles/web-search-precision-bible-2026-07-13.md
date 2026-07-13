---
title: Web Search 精準度聖經 — Learning to Rank 完整聖經（Microsoft + Stanford IR + Lucidworks）
created: 2026-07-13
updated: 2026-07-13
type: source-article
tags: [book-summary, learning-to-rank, ltr, lambdamart, lambdarank, ranknet, bm25, web-search-precision, web-search-quality, ndcg, microsoft-research, stanford-ir, hermes-search-precision, hermes-layer-4]
urls:
  - https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/MSR-TR-2010-82.pdf
  - https://cs.usm.maine.edu/~behrooz.mansouri/courses/Slides_IR_22/Introduction%20to%20Information%20Retrieval%20--%20Session%2015%20-%20Learning%20to%20Rank.pdf
  - https://lucidworks.com/blog/abcs-learning-to-rank
license: Microsoft Research Technical Report (公開) + Stanford IR Book (CC 公開在線版)
audience: Hermes Layer 4c Vector Search 精準度優化 / Web Search 排序學習設計者
---

# Web Search 精準度聖經 — Source Material

> 整合 3 個**完全開源**權威資源：
> - **Microsoft Research "From RankNet to LambdaRank to LambdaMART: An Overview"** (Burges 2010, MSR-TR-2010-82)
> - **Stanford NLP IR Book Session 15: Learning to Rank** (Manning 2008, Ch 15)
> - **Lucidworks ABCs of Learning to Rank** (Apache 2.0 開源工具)
>
> **無版權疑慮**。對應 Hermes **Layer 4c** = Web Search 精準度提升

## Part 1: Learning to Rank（LTR）完整概念

### 為什麼需要 LTR？

| 傳統 IR 限制 | LTR 解法 |
|------------|----------|
| BM25/TF-IDF 參數難調 | 自動學習 |
| 難以組合多模型 | 自動融合 |
| Overfitting 風險 | Regularization |
| 200+ features 難以手調 | ML 自動處理 |

> **Amit Singhal 2008**: Google 使用 200+ ranking signals/features — 手工 tune 不可能。

### LTR 3 大流派

| 流派 | Input | Output | 代表算法 |
|------|-------|--------|----------|
| **Pointwise** | 單文檔 | relevance score/label | 線性回歸、SVM |
| **Pairwise** | 文檔對 | 偏序偏好 | **RankNet, LambdaRank** |
| **Listwise** | 文檔列表 | 整體排序 | **LambdaMART, ListNet, AdaRank** |

### LambdaMART 簡史（Burges 2010）

```
RankNet (Burges 2005)
   ↓ 啟發式梯度
LambdaRank (Burges 2006)
   ↓ 用 MART 框架
LambdaMART (Burges 2007)
   ↓ Yahoo! 2010 LTR Challenge 冠軍
```

**LambdaMART = LambdaRank + MART（Multiple Additive Regression Trees）**

### RankNet 數學基礎

```python
# 兩文檔 Ui, Uj 的相關性機率
P_ij = 1 / (1 + exp(-σ(s_i - s_j)))

# Cross-entropy cost
C = -P̄_ij log P_ij - (1 - P̄_ij) log(1 - P_ij)

# λ_ij（gradient force）
λ_ij = ∂C/∂s_i = σ((1 - S_ij)/2 - 1/(1 + exp(σ(s_i - s_j))))
```

**直觀**：λ 是每個 URL 的「箭頭力」，方向=相關性提升，長度=力度。

### 4 大數學突破（Burges 2010）

1. **RankNet**：pairwise sigmoid + cross-entropy
2. **Factoring RankNet**：λ force 重構（速度↑ 100x）
3. **LambdaRank**：用 NDCG 增益直接定義 λ（理論保證 NDCG↑）
4. **LambdaMART**：用 MART 框架實作 LambdaRank

### Yahoo! 2010 LTR Challenge

- **Track 1 Winner**: LambdaMART ensemble
- 影響：微軟 Bing 採用 LambdaMART 作為 production ranker

## Part 2: 3 大 LTR 算法對比

### Pointwise（基於單文檔）

| 算法 | 損失函數 | 優點 | 缺點 |
|------|---------|------|------|
| Linear Regression | MSE | 簡單 | 忽略查詢內差異 |
| Logistic Regression | Log loss | 概率輸出 | 忽略排序位置 |
| PRank | Ordinal | 考慮有序 | 簡單模型 |

### Pairwise（基於文檔對）

| 算法 | 損失函數 | 代表 |
|------|---------|------|
| **RankNet** | Cross-entropy on pairs | Burges 2005 |
| **LambdaRank** | NDCG 增益直接定義 λ | Burges 2006 |
| RankSVM | Hinge loss on pairs | Joachims |
| RankBoost | Boosting | Freund |

### Listwise（基於列表）

| 算法 | 評估指標 | 特點 |
|------|---------|------|
| **LambdaMART** | NDCG/MRR | 最常用 |
| **ListNet** | Listwise CE | Top-1 優化 |
| **AdaRank** | NDCG 直接優化 | Boosting |
| **ListMLE** | Likelihood | 機率模型 |

## Part 3: Stanford IR Book LTR 重點（Manning 2008）

### LTR 問題定義

```
Input:  X = {x_1, x_2, ..., x_n}  (query-doc pairs 帶 feature vectors)
Output: Y' = sorted list  (ranked by scoring function f)
Ground truth: Y = ideal ranking
Objective: maximize NDCG / MAP / MRR
```

### 5 大排名評估指標（必看）

| 指標 | 公式 | 評估對象 |
|------|------|---------|
| **NDCG** | DCG / IDCG | 排序品質（normalized）|
| **MAP** | mean(AP) | 整體精度 |
| **MRR** | mean(1/rank) | 第一個相關結果的排名 |
| **P@K** | precision at K | Top-K 精度 |
| **ERR** | Expected Reciprocal Rank | 用戶行為模擬 |

### 排序 4 大關鍵參數

| 參數 | 說明 | LambdaMART 預設 |
|------|------|-----------------|
| **Number of leaves** | 樹葉節點數 | 64 |
| **Number of trees** | 樹數量 | 100-1000 |
| **Learning rate** | 學習率 | 0.1 |
| **Min documents per leaf** | 葉最少文檔 | 10 |

## Part 4: 4 大 Unsupervised Fusion 方法

當沒訓練數據時，可使用：

| 方法 | 公式 | 強項 |
|------|------|------|
| **CombMAX** | max(s_0, ..., s_n) | 信心最大 |
| **CombMIN** | min(s_0, ..., s_n) | 嚴格標準 |
| **CombSUM** | sum(s_i) | 簡單平均 |
| **CombMNZ** | count × sum | 雙重加權 |
| **RRF** | sum(1/(k+r_i(d))) | **k=60 預設** |

### RRF（Reciprocal Rank Fusion）— 業界主流

```
RRF_score(d) = Σ 1/(k + rank_i(d))
```

**k=60 預設**（避免 top-1 過度加權），Google 搜尋結果融合也用 RRF。

## Part 5: 6 大新 TRAP-SOP 規劃

| TRAP | 主題 |
|------|------|
| **TRAP-SOP-092** | 用 BM25 不用 LTR（忽略特徵融合）|
| **TRAP-SOP-093** | LTR 訓練沒用 NDCG 評估（用錯指標）|
| **TRAP-SOP-094** | LambdaMART 樹數太多（overfitting）|
| **TRAP-SOP-095** | 沒做 feature normalization（不同尺度）|
| **TRAP-SOP-096** | Train/test 沒做 query-level split（leakage）|
| **TRAP-SOP-097** | 沒做 fusion（單一模型結果）|

## Part 6: Hermes Layer 4c Web Search 精準度升級路徑

### 現狀（v2.0）

```
wiki page → sentence-transformers → Qdrant (Hybrid) → Top-100
```

### 升級 v3.0（加 LTR）

```
                              ┌─ 雙編碼器分數
wiki page → Multi-Vector ──→ ├─ BM25 分數 ──→ LambdaMART ──→ Top-10
                              ├─ PageRank 分數
                              └─ Recency 分數
```

### LTR Features 清單（20+ 特徵）

| Feature | 計算 |
|---------|------|
| **Cosine sim** | dot(q_vec, d_vec) |
| **BM25 score** | BM25(q, d) |
| **Field-level sim** | title/body/heading 分別算 |
| **Document length** | len(d) |
| **Query length** | len(q) |
| **Term coverage** | |q ∩ d| / |q| |
| **Freshness** | now - d.modified_time |
| **PageRank** | graph-based |
| **Inbound link count** | inlinks(d) |
| **URL depth** | / 數量 |
| **Click-through rate** | log(CTR) |
| **Time spent** | avg dwell time |

## Part 7: Hermes Web Search 5 大場景決策表

| 場景 | 推薦方法 |
|------|---------|
| < 1K 文檔 | BM25 only |
| 1K-100K 文檔 | BM25 + LambdaMART |
| 100K-1M 文檔 | Hybrid + ColBERT + LambdaMART |
| 1M+ 文檔 | Hybrid + ColBERT + LambdaMART + 分片 |
| 即時 streaming | Online learning to rank |

## 引用

```bibtex
@techreport{burges2010lambdamart,
  author = {Christopher J.C. Burges},
  title = {From RankNet to LambdaRank to LambdaMART: An Overview},
  institution = {Microsoft Research},
  year = {2010},
  number = {MSR-TR-2010-82}
}

@book{manning2008ir,
  author = {Manning, Christopher D. and Raghavan, Prabhakar and Schütze, Hinrich},
  title = {Introduction to Information Retrieval},
  chapter = {15},
  year = {2008}
}

@article{lucidworks_ltr,
  title = {The ABCs of Learning to Rank},
  author = {{Lucidworks}},
  year = {2026},
  url = {https://lucidworks.com/blog/abcs-learning-to-rank}
}
```

## 對 Hermes 的啟示

| 維度 | 現狀 | 改善 |
|------|------|------|
| 搜尋方法 | Hybrid Search | + LambdaMART rerank |
| 評估指標 | Top-5 命中率 | + NDCG@10 / MAP / MRR |
| 特徵 | Embedding only | + 20+ LTR features |
| 工具 | Qdrant | + LightGBM/XGBoost LambdaMART |
| 訓練 | 無 | + LETOR dataset |

完整鏈路：3 大開源權威資源 → 3 大 LTR 流派 → LambdaMART 數學 → Hermes 5 大場景 → 6 大 TRAP（092~097）→ Layer 4c 升級 v3.0 🎯