---
title: 智能搜尋聖經 — Vector DB 四強 + Stanford IR Book 21 章
created: 2026-07-13
updated: 2026-07-13
type: source-article
tags: [book-summary, intelligent-search, vector-search, semantic-search, information-retrieval, qdrant, milvus, weaviate, pinecone, ir-book, stanford, hnsw, hybrid-search, rag, faiss, hermes-memory, layer-4]
urls:
  - https://qdrant.tech/
  - https://milvus.io/ai-quick-reference/what-vector-databases-are-best-for-semantic-search-applications
  - https://nlp.stanford.edu/IR-book/
license: Open source (Qdrant + Milvus 官方) + Stanford IR Book 免費在線版
audience: Hermes Layer 4 Memory Architecture / Vector Search 設計者
---

# 智能搜尋聖經 — Source Material

> 整合 3 個**完全 open-source** 的權威資源：
> - **Stanford NLP IR Book**（Manning et al. 2008，21 章免費在線版）
> - **Qdrant 官方文檔**（MIT License，30k+ stars）
> - **Milvus AI Quick Reference**（Apache 2.0，Zilliz 維護）
> 
> **無版權疑慮**。對應 Hermes **Layer 4 Memory** = Vector Search Layer 4c。

## 與 Hermes Layer 4 對應

```
Hermes Memory 4 層：
  4a. Short-term (in-session)        — 已有（context）
  4b. Long-term Structured (fact_store) — 已有
  4c. Long-term Semantic (vector search) — ★ 本研究重點
  4d. Graph (wiki links)            — 已有
```

## 書 1: Stanford NLP IR Book（Manning et al. 2008）

### 簡介

**Introduction to Information Retrieval** — Christopher D. Manning, Prabhakar Raghavan, Hinrich Schütze。Cambridge University Press 2008 出版。

### 21 章目錄（合規來源：nlp.stanford.edu/IR-book/）

| Ch | 主題 | 與 Vector Search 關係 |
|----|------|---------------------|
| 01 | Boolean retrieval | keyword search 基礎 |
| 02 | Term vocabulary & postings lists | inverted index 經典 |
| 03 | Dictionaries & tolerant retrieval | 拼字校正 |
| 04 | Index construction | 大規模索引建構 |
| 05 | Index compression | 儲存優化 |
| 06 | **Scoring, term weighting & the vector space model** | ★ Vector Space Model（向量搜尋基礎）|
| 07 | Computing scores in a complete search system | TF-IDF 評分 |
| 08 | Evaluation in information retrieval | 評估指標（P/R/F1） |
| 09 | Relevance feedback & query expansion | RRF, query reformulation |
| 10 | XML retrieval | 結構化檢索 |
| 11 | Probabilistic information retrieval | BM25 |
| 12 | Language models for information retrieval | LM-based retrieval |
| 13 | Text classification & Naive Bayes | 分類 |
| 14 | **Vector space classification** | ★ 現代 dense vector 基礎 |
| 15 | Support vector machines & ML on documents | ML 分類 |
| 16 | Flat clustering | k-means |
| 17 | Hierarchical clustering | 階層式 |
| 18 | **Matrix decompositions & LSI** | ★ Latent Semantic Indexing（向量降維）|
| 19 | Web search basics | PageRank |
| 20 | Web crawling and indexes | crawler |
| 21 | Link analysis | HITS, PageRank |

### 5 大經典公式（Hermes Vector Search 應用）

| 公式 | 出處 | 應用 |
|------|------|------|
| **TF-IDF** | Ch 6 | 傳統 sparse vector |
| **Vector Space Model** | Ch 6 | cosine similarity 基礎 |
| **BM25** | Ch 11 | keyword + vector hybrid |
| **Latent Semantic Indexing (LSI)** | Ch 18 | SVD 降維（dense vector 雛形）|
| **PageRank** | Ch 21 | link-based ranking |

## 書 2: Vector DB 四強官方整合

### 來源
- Qdrant 官方 (https://qdrant.tech/) — MIT License
- Milvus AI Quick Reference (https://milvus.io/...)

### 4 大主流 Vector DB 對比

| DB | 部署 | 開源 | 強項 | 適合 |
|----|------|------|------|------|
| **Pinecone** | 託管 | 閉源 | 生產級、易用 | 大規模商用 |
| **Weaviate** | 自託管/雲 | BSD-3 | **Hybrid search 最佳** | RAG + keyword |
| **Milvus** | 自託管/雲 | Apache 2.0 | 大規模、億級 vectors | 圖像檢索 |
| **Qdrant** | 自託管/雲 | Apache 2.0 | Rust + 靈活 filtering | 地理空間 + 客製化 |

### 共同技術基礎

| 技術 | 描述 |
|------|------|
| **HNSW**（Hierarchical Navigable Small World）| 主流 ANN（Approximate Nearest Neighbor）算法 |
| **Filterable HNSW** | Qdrant 創新：filtering 在 HNSW traversal 階段（不需 pre/post-filter）|
| **Hybrid Search** | Dense + Sparse + BM25/SPLADE++/miniCOIL |
| **Quantization** | Scalar / Binary / Product quantization（減少 64x 記憶體）|
| **Multivector** | 每個 object 多個 vectors（支援 ColBERT late interaction）|

## 書 3: Qdrant 進階功能（官方）

### 5 大核心功能

1. **Expansive Metadata Filters**：JSON 儲存 metadata + nested/text/geo/has_vector filters
2. **Native Hybrid Search**（Dense + Sparse）：BM25、SPLADE++、miniCOIL 整合
3. **Built-in Multivector**：多向量 = 更高表達力
4. **One-stage Filtering**：HNSW 階段過濾 = 高 recall + 低 latency
5. **Full-spectrum Reranking**：MMR、score boosting、late interaction（ColBERT）

### 4 大部署模式

| 模式 | 描述 |
|------|------|
| **Qdrant Cloud** | AWS/GCP/Azure 全託管 |
| **Qdrant Hybrid Cloud** | 自帶 K8s + 分離 control/data planes |
| **Qdrant Private Cloud** | Air-gapped 企業部署 |
| **Qdrant Edge** | 邊緣低延遲部署（beta）|

### 5 大應用場景

- RAG & GenAI
- AI Agents
- Semantic Search
- Recommendation Systems
- Data Analysis & Anomaly Detection

## 對 Hermes Layer 4c 的啟示

### Hermes 應用架構

```
wiki page ──> Embedding Model ──> Qdrant/Milvus ──> Semantic Search
                ↓
        sentence-transformers (all-MiniLM-L6-v2, 384 dims)
                ↓
        ChromaDB / Pinecone / local HNSW
                ↓
        4-stage pipeline:
          1. Query expansion (Stanford IR Ch 9)
          2. Embedding (sentence-transformers)
          3. ANN search (HNSW via Qdrant)
          4. Reranking (BM25 + dense)
```

### 5 大設計原則

| 原則 | 來源 | 應用 |
|------|------|------|
| **Hybrid search 預設** | Milvus 建議 | 結合 keyword + vector |
| **Filterable HNSW** | Qdrant 專利 | 過濾在檢索階段 |
| **即時索引** | Qdrant 設計 | 新增資料立即可搜 |
| **量化降低記憶體** | 4 大共通 | 64x 壓縮比 |
| **Multivector** | Qdrant 創新 | ColBERT 整合 |

## 5 大工具決策表

| 場景 | 推薦 | 理由 |
|------|------|------|
| 個人筆記 < 100 萬 vectors | **ChromaDB + sentence-transformers** | 簡單、本地、零成本 |
| 中型專案 < 1000 萬 | **Qdrant** | 開源 + Rust 性能 + hybrid search |
| 大型商用無運維 | **Pinecone** | 全託管 |
| 已有 Elasticsearch | **Elasticsearch vector plugin** | 不另起爐灶 |
| 多語言 + 結構化 | **Weaviate** | 內建 BM25 + vectorization |

## 對 Hermes SOP 的擴展

| 新 TRAP | 主題 |
|---------|------|
| TRAP-SOP-081 | Vector Search 沒做 Hybrid（只用 dense 或只用 sparse）|
| TRAP-SOP-082 | Embedding 模型版本不一致（每次重建會變化）|
| TRAP-SOP-083 | ANN 參數（ef, m）沒調優，recall 太低 |
| TRAP-SOP-084 | 沒做 Reranking，Top-K 精確率差 |
| TRAP-SOP-085 | Index 沒做 Quantization，記憶體爆炸 |

## 引用

```bibtex
@book{manning2008ir,
  author = {Manning, Christopher D. and Raghavan, Prabhakar and Schütze, Hinrich},
  title = {Introduction to Information Retrieval},
  publisher = {Cambridge University Press},
  year = {2008},
  note = {Online edition available at \url{https://nlp.stanford.edu/IR-book/}}
}

@software{qdrant,
  title = {Qdrant - Vector Search Engine},
  author = {{Qdrant Team}},
  year = {2026},
  url = {https://qdrant.tech/},
  license = {Apache 2.0}
}
```

## 資源

- Stanford IR Book：https://nlp.stanford.edu/IR-book/
- Qdrant 官方：https://qdrant.tech/
- Milvus Quick Reference：https://milvus.io/ai-quick-reference/
- ChromaDB（建議給 Hermes）：https://www.trychroma.com/

## 對現有 Hermes Memory SOP 的啟示

| 現有 SOP | 改善建議 |
|---------|----------|
| `vector-search-memory-design.md` v1.0 | 升級加入 hybrid search + Qdrant 評估 |
| `mcp-health-probe-sliding-window.md` | 加入 vector DB 監控（Qdrant metrics）|

完整鏈路：3 個 open-source 資源 → 21 章 IR + 4 大 Vector DB → Hermes Layer 4c 設計 → 5 大新 TRAP-SOP 🎯