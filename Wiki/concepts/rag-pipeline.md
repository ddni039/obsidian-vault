---
title: RAG (Retrieval-Augmented Generation) Pipeline
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [concept, rag, retrieval-augmented-generation, llm, qa, hybrid-search, hermes-qa, wikipedia, haystack]
sources:
  - raw/articles/qa-intelligence-bible-2026-07-13.md
  - en.wikipedia.org/wiki/Retrieval-augmented_generation
confidence: high
---

# RAG (Retrieval-Augmented Generation) Pipeline

## 定義

**RAG** = Retrieval-Augmented Generation
= 一種讓 LLM 結合**外部知識庫**生成答案的技術

```
RAG = LLM + Vector Search + Prompt Engineering
```

起源：**Lewis et al. 2020 paper**

## 為什麼需要 RAG？

| 純 LLM 問題 | RAG 解法 |
|------------|----------|
| 訓練後知識凍結 | 即時從 KB 補充 |
| Hallucination 高 | 答案可追溯到來源 |
| 無法引用來源 | 透明化 |
| 重訓練成本高 | 只需更新 KB |
| 領域專業弱 | 載入 domain 資料 |

## 4-Stage RAG Pipeline

```
┌─ Stage 1: Retrieval ─────────────────┐
│ User Query → Embedding → Vector Search│
│ → Top-K Documents                     │
└──────────────────────────────────────┘
                ↓
┌─ Stage 2: Augmentation ───────────────┐
│ Prompt = Query + Retrieved Context     │
│ ("prompt stuffing" 強制優先用新資訊)  │
└──────────────────────────────────────┘
                ↓
┌─ Stage 3: Generation ─────────────────┐
│ LLM(Prompt) → Answer                  │
└──────────────────────────────────────┘
                ↓
┌─ Stage 4: Post-Processing ────────────┐
│ Re-rank, Cite sources, Filter         │
└──────────────────────────────────────┘
                ↓
       Answer + References
```

## RAG 演進樹（2020-2026）

```
2020: 原始 RAG（Lewis et al.）
       ↓
2021: Real-time RAG（streaming）
       ↓
2022: Hybrid RAG（dense + sparse）
       ↓
2023: Self-RAG（LLM 自我評估 retrieval）
       ↓
2024: Agentic RAG（LLM 主動 multi-step 檢索）
       ↓
2025: GraphRAG（知識圖譜 + RAG）
       ↓
2026: Multimodal RAG（text + image + audio）
```

## 4 大 RAG 框架對比

| 框架 | 開發者 | 強項 |
|------|--------|------|
| **LangChain** | Harrison Chase | 通用 + Agent |
| **LlamaIndex** | Jerry Liu | RAG 原生 + 文件處理 |
| **Haystack** | deepset | Pipeline + 企業級 |
| **RAGFlow** | InfiniFlow | 開箱即用 + OCR + 中文 |

## Hermes 4-Stage QA Pipeline

```
User Query (中文/英文)
   ↓
Layer 4: Qdrant Hybrid Search
   - Dense: sentence-transformers (384d)
   - Sparse: BM25
   - Top-100 candidates
   ↓
Layer 2: Re-ranking + Reasoning
   - Cross-encoder rerank → Top-10
   - Self-Consistency voting
   ↓
Generation: LLM(MiniMax-M3)
   - Prompt: query + top-10 contexts
   - Output: answer + citations
   ↓
Output + Confidence Score
```

## 7 大 QA 評估指標

| 指標 | 用途 | 公式 |
|------|------|------|
| **EM** (Exact Match) | 答案完全匹配 | 1 if match else 0 |
| **F1** | Token 重疊 | 2*P*R/(P+R) |
| **BLEU** | n-gram 翻譯品質 | - |
| **ROUGE** | n-gram 摘要品質 | - |
| **MRR** | 排序評估 | 1/rank |
| **NDCG@k** | 排序品質 | - |
| **Faithfulness** | 忠於來源 | LLM judge |

## 6 大常見失敗（將成為 TRAP-SOP-086~091）

| # | 失敗 | 後果 |
|---|------|------|
| 1 | 純 LLM 不用 retrieval | 領域知識弱 |
| 2 | 只用 dense 或只 BM25 | 召回率低 30-50% |
| 3 | 沒做 late interaction | 精準度差 |
| 4 | 沒要求引用來源 | 無法驗證 |
| 5 | 沒做 query expansion | 召回低 |
| 6 | 沒做 cost monitoring | 成本失控 |

## 何時 RAG 不適用

| 不適用 | 替代 |
|--------|------|
| 完全 general 知識 | 純 LLM |
| < 100 docs | 純 LLM + fine-tuning |
| 即時性要求極高 | 純 LLM |
| 隱私敏感 | 純 LLM（local model）|

## 引用

- Wikipedia RAG：https://en.wikipedia.org/wiki/Retrieval-augmented_generation
- Haystack Docs：https://docs.cloud.deepset.ai/docs/generative-question-answering
- arXiv Systematic Review：https://arxiv.org/abs/2507.18910

## 版本

| 版本 | 日期 | 變更 |
|------|------|------|
| v1.0 | 2026-07-13 | 初版（基於 Wikipedia + Haystack + arXiv）|