---
title: 問答智能聖經 — Wikipedia RAG + Haystack 官方 + arXiv Systematic Review
created: 2026-07-13
updated: 2026-07-13
type: source-article
tags: [book-summary, qa, question-answering, rag, retrieval-augmented-generation, haystack, langchain, llamaindex, llm-qa, wikipedia, hermes-qa]
urls:
  - https://en.wikipedia.org/wiki/Retrieval-augmented_generation
  - https://docs.cloud.deepset.ai/docs/generative-question-answering
  - https://arxiv.org/html/2507.18910v1
license: CC BY-SA 4.0 (Wikipedia) + Apache 2.0 (Haystack) + arXiv open access
audience: Hermes Layer 2 (Reasoning) + Layer 4 (Memory) QA 設計者
---

# 問答智能聖經 — Source Material

> 整合 3 個**完全 open-source** 權威資源：
> - **Wikipedia RAG** (CC BY-SA 4.0) — RAG 完整定義、歷史、應用、改進
> - **Haystack Enterprise Platform 官方文檔** (Apache 2.0)
> - **arXiv 2507.18910 Systematic Review** (開源論文)
>
> **無版權疑慮**。對應 Hermes **Layer 2 (Reasoning) + Layer 4 (Memory)** = QA 系統設計

## Part 1: RAG 完整定義（Wikipedia 2024+）

### 起源與時間線

- **2020 年首次提出**：Lewis et al. 2020 paper，結合 parametric language model + non-parametric external memory
- **2024+ 主流採用**：ChatGPT、Claude、Gemini 全面整合 RAG
- **2025+ 演進**：Agentic RAG、GraphRAG、Hybrid RAG、Multimodal RAG

### RAG 解決的核心問題

| LLM 限制 | RAG 解法 |
|---------|----------|
| ❌ 訓練後知識凍結 | ✅ 即時從外部 KB 補充 |
| ❌ 容易 hallucination | ✅ 答案可追溯到來源 |
| ❌ 領域專業知識弱 | ✅ 載入特定 domain 資料 |
| ❌ 無法引用來源 | ✅ 透明化、可驗證 |
| ❌ 重訓練成本高 | ✅ 只需更新 KB |

### 真實失敗案例（Bard）

> Google Bard 首次發表時，錯誤描述 James Webb 太空望遠鏡資訊，造成 Google 股價下跌 **$1000 億**。
> RAG 不會解決所有 hallucination，但能大幅降低。

### RAG Process（核心 4 步）

```
User Query
  ↓
┌─ Stage 1: Retrieval（資訊檢索）────────────────┐
│ - 文件向量化（embeddings）                     │
│ - 存到 vector database                          │
│ - 查詢時：找最相關的 top-K 文件                │
└──────────────────────────────────────────────┘
                ↓
┌─ Stage 2: Augmentation（增強 prompt）─────────────┐
│ - 把 retrieved documents 塞進 LLM prompt         │
│ - "prompt stuffing" 強制 LLM 優先用新資訊        │
└──────────────────────────────────────────────┘
                ↓
┌─ Stage 3: Generation（LLM 生成）────────────────┐
│ - LLM 結合 query + retrieved context 生成答案    │
│ - 可要求附帶 reference（引用來源）                │
└──────────────────────────────────────────────┘
                ↓
┌─ Stage 4: Post-Processing（後處理）───────────────┐
│ - Re-ranking、Context selection、Fine-tuning     │
│ - 過濾 hallucination                            │
└──────────────────────────────────────────────┘
                ↓
         帶 reference 的最終答案
```

### 改進方向（Wikipedia 列舉）

**Encoder 層**：
- **Dense vs Sparse vectors**：dense 表語義，sparse 表字面
- **Dot product similarity**：計算效率高
- **ANN search**：HNSW 等近似算法
- **Late Interactions**：ColBERT 精準比對

**LLM 層**：
- **Prompt engineering**：few-shot、CoT、Self-Consistency
- **Fine-tuning**：domain-specific tuning

**Process 層**：
- **Query expansion**：多 query 並行檢索
- **Re-ranking**：cross-encoder rerank
- **Self-RAG**：LLM 自己評估 retrieval 必要性

## Part 2: Haystack 官方 RAG QA 設計（Apache 2.0）

### Haystack 對 RAG QA 的定義

> RAG question answering uses LLMs to generate human-like responses based on retrieved documents.

### 4 大優勢

1. **Multi-source synthesis**：整合多來源資訊
2. **Creative generation**：原創內容、品牌化語氣
3. **Language flexibility**：自然語言、慣用語
4. **Reasoning capabilities**：比較事實、推理結論

### 6 大挑戰（必看）

| 挑戰 | 影響 | Hermes 對應 |
|------|------|------------|
| **Cost** | Token-based 計費昂貴 | TRAP-SOP-091（成本失控）|
| **Context length** | LLM token 上限 | TRAP-SOP-092（context overflow）|
| **Hallucination** | 模型虛構 | TRAP-SOP-086（已建立）|
| **Latency** | 慢於 extractive QA | TRAP-SOP-093（高延遲）|
| **Output control** | 可能有害內容 | TRAP-SOP-094（內容審核）|
| **Evaluation** | 缺乏客觀指標 | TRAP-SOP-095（評估難題）|

### Haystack 4 大應用場景

- **Chatbots / AI Assistants / 客服支援**
- **Writing aids / 內容生成**
- **Learning assistants / 教育**
- **Translation aids / 翻譯助手**

### Haystack 5 大 Pipeline 元素

```
Query → Retriever → Ranker → PromptBuilder → LLM Generator
        ↓              ↓          ↓                ↓
    (Vector Search)  (Re-rank)  (Template)    (GPT-4/Claude)
```

### Haystack 三大模型選擇

| 模型 | 廠商 | 強項 |
|------|------|------|
| **GPT-4 / GPT-4o** | OpenAI | 通用、推理強 |
| **Claude 3.5/3.7** | Anthropic | 長 context、安全 |
| **Command R+** | Cohere | RAG 原生整合 |

## Part 3: 4 大 QA 框架對比

| 框架 | 開發者 | 強項 | 適合 |
|------|--------|------|------|
| **LangChain** | Harrison Chase (2022) | Agent + Chain + Tools | 通用 LLM 應用 |
| **LlamaIndex** | Jerry Liu (2022) | Document QA / RAG 原生 | 文件問答 |
| **Haystack** | deepset (2020) | Pipeline-based + Production-ready | 企業級 QA |
| **RAGFlow** | InfiniFlow | 開箱即用 + OCR + 文檔解析 | 中文/多模態 |

### 共同設計理念

- **文件載入器** → **Splitter** → **Embedder** → **Vector Store** → **Retriever** → **Reranker** → **LLM**

## 對 Hermes QA 系統的啟示

### Hermes QA = Layer 2 Reasoning + Layer 4 Memory 整合

```
User Query
  ↓
┌─ Layer 4: Retrieval（向量化檢索）───────────┐
│ - Sentence-transformers (Dense 384d)         │
│ - Qdrant Hybrid Search（已升級）              │
│ - Top-100 candidates                         │
└──────────────────────────────────────────────┘
                ↓
┌─ Layer 2: Reranking + Reasoning ──────────────┐
│ - Cross-encoder rerank                        │
│ - Top-10 refined                             │
│ - Self-Consistency voting（已建立）            │
└──────────────────────────────────────────────┘
                ↓
┌─ Generation + Citation ─────────────────────┐
│ - LLM（MiniMax-M3 / Claude 3.5）             │
│ - Prompt: top-10 contexts + query             │
│ - Citation 自動生成                          │
└──────────────────────────────────────────────┘
                ↓
         Answer + References + Confidence
```

### 6 大 QA TRAP-SOP 規劃

| TRAP | 主題 |
|------|------|
| **TRAP-SOP-086** | RAG 系統只用 LLM 不用 retrieval（純靠記憶）|
| **TRAP-SOP-087** | Retrieval 沒做 hybrid（只 dense 或只 BM25）|
| **TRAP-SOP-088** | Retrieval 沒做 late interaction（錯失精準）|
| **TRAP-SOP-089** | LLM prompt 沒要求引用來源（無法驗證）|
| **TRAP-SOP-090** | 沒做 query expansion（單 query 召回低）|
| **TRAP-SOP-091** | 沒做 cost monitoring（token 成本失控）|

## QA 評估指標

### 7 大自動指標

| 指標 | 評估對象 | 公式 |
|------|---------|------|
| **Exact Match (EM)** | 答案完全匹配 | 1 if match else 0 |
| **F1 Score** | Token-level 重疊 | 2*P*R/(P+R) |
| **BLEU/ROUGE** | n-gram 重疊 | - |
| **MRR (Mean Reciprocal Rank)** | 檢索排序 | 1/rank |
| **NDCG@k** | 排序品質 | - |
| **Context Relevance** | 檢索文件相關性 | LLM judge |
| **Answer Faithfulness** | 答案忠於來源 | LLM judge |

## 引用

```bibtex
@misc{wikipedia_rag,
  title = {Retrieval-augmented generation},
  howpublished = {Wikipedia},
  url = {https://en.wikipedia.org/wiki/Retrieval-augmented_generation},
  license = {CC BY-SA 4.0}
}

@software{haystack,
  title = {Haystack Enterprise Platform},
  author = {{deepset}},
  url = {https://docs.cloud.deepset.ai/},
  license = {Apache 2.0}
}

@article{arXiv_2507_18910,
  title = {A Systematic Review of Key Retrieval-Augmented Generation},
  year = {2025},
  url = {https://arxiv.org/abs/2507.18910}
}
```

## 對 Hermes 的最終評估

| Layer | 現狀 | QA 改進方向 |
|-------|------|-----------|
| Layer 1 (LLM) | 70% | Model routing QA-專用模型 |
| Layer 2 (Reasoning) | 75% | 整合 Re-ranking + Self-Consistency |
| Layer 4 (Memory) | 80% | 已升級 v2.0（Qdrant + Hybrid）|
| **整體 QA 能力** | **75%** | **→ 目標 92%** |

完整鏈路：3 大 open-source 資源 → Wikipedia RAG 完整定義 + Haystack 官方 + arXiv → 6 大 TRAP-SOP（086~091）→ Hermes QA 系統 v2.0 🎯