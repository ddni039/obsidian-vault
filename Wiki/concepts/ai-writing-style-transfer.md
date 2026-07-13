---
uid: 20260713-ai-writing-style-transfer
name: AI 風格寫作與 Persona 引導
aka: [style transfer, persona prompting, LLM writing style, AI voice]
type: concept
tags: [AI, LLM, writing, style, persona, prompt engineering, style transfer]
related_concepts:
  - concepts/classical-chinese-rhetoric.md
  - concepts/strunk-white-elements-of-style.md
  - concepts/prompt-engineering.md
  - concepts/llm-agent.md
trigger: |
  AI風格寫作、Persona引導、Voice Preservation、風格遷移、Style Transfer、LLM寫作、多輪迭代、Draft改稿、語氣控制、正式程度、句式長度、主觀客觀比例、AI寫作質量、AI口語化
source: |
  arxiv:2507.22168v1 — Persona-Augmented Benchmarking (EMNLP 2025, CMU + Amazon)
  MDPI Applied Sciences — Can LLMs Be Good Evaluators in Creative Writing Tasks? (2025)
  PMC 13061212 — Comparative analysis of text readability and writing styles in AI vs Human (2026)
  Medium @alishafique3 — LLM Prompt Engineering Techniques and Best Practices
---

# AI 風格寫作與 Persona 引導

## 核心研究發現

### 研究一：Persona-Augmented Benchmarking（CMU + Amazon, EMNLP 2025）

**核心發現**：寫作風格的細微變化（同一語義內容，不同表達方式）會顯著影響 LLM 的評估表現，且影響程度與模型家族、規模、年代無關。

| 發現 | 數據 |
|------|------|
| 相同語義，不同風格 | 可造成同一 LLM 回答準確率顯著差異 |
| 最差表現 persona | 64% 為「教育程度低於高中」，29% 為「老年人」|
| 跨模型一致性 | 無論 GPT-4 / Claude / Gemini，最差表現群體高度重疊 |
| 風格維度 | 句法（syntax）、詞彙（lexicon）、形態（morphology）、情感（sentiment）|

### 研究二：AI 生成文字的詞彙密度

| 指標 | 人類 | AI |
|------|------|----|
| 詞彙密度 | 63.7% | **66.3%**（p<0.001）|

AI 文字的詞彙密度顯著更高——意味著每句承載更多術語，信息量更大但節奏更密、閱讀負擔更高。

### 研究三：LLM 作為創意寫作評估者

LLM 作為創意寫作評估者，與人類專家評分高度相關——可用於協助風格審查。

---

## 風格維度模型

### 七維度寫作風格向量

```
風格向量 = {
  正式程度: [1=口語 ←→ 7=學術],
  句式長度: [1=短句 ←→ 7=超長複句],
  詞彙選擇: [1=日常 ←→ 7=專業術語],
  情感溫度: [1=冷靜客觀 ←→ 7=強烈主觀],
  主觀/客觀比例: [0% ←→ 100%],
  結構密度: [1=輕盈留白 ←→ 7=密集堆疊],
  節奏變化: [1=單一拍子 ←→ 7=起伏強烈]
}
```

### 風格Prompt框架

```python
STYLE_PROMPT_TEMPLATE = """
你是一位{profession}，寫作風格深受{influencer}影響。
文字特徵：
- 正式程度：{formality}/7
- 情感溫度：{emotion}/7
- 句式：{sentence_pattern}
- 典型用詞：{vocabulary_type}
- 節奏偏好：{rhythm_preference}

要求：{task_description}
"""
```

### Persona引導三層次

| 層次 | 方法 | 適用場景 |
|------|------|---------|
| L1: 簡單指定 | `你是一位XX領域專家` | 快速框架切換 |
| L2: 風格描述 | `用余秋雨的散文風格` | 需要具體調性 |
| L3: 樣本學習 | 提供2-3篇原文 | 精確模仿個人聲音 |

---

## 多輪迭代工作流

```
┌──────────────────────────────────────────────┐
│  Draft 1：捕捉內容                           │
│  → 快速生成，核心內容優先                      │
└──────────────────────────────────────────────┘
                 ↓
┌──────────────────────────────────────────────┐
│  Draft 2：風格校正                           │
│  → 「將結論段落的動詞換成更具體有力的動詞」       │
│  → 「減少被動語態，使用主動語態」               │
└──────────────────────────────────────────────┘
                 ↓
┌──────────────────────────────────────────────┐
│  Draft 3：節奏調整                           │
│  → 「每段不超過5句話」                        │
│  → 「加入一個具體數字或案例」                  │
└──────────────────────────────────────────────┘
                 ↓
┌──────────────────────────────────────────────┐
│  Draft 4：聲音一致性                          │
│  → 「全文是否保持同一敘事者聲音？」             │
│  → 「術語使用是否一致？」                      │
└──────────────────────────────────────────────┘
```

---

## Voice Preservation（人聲保留）技法

當需要讓 AI 模仿特定個人風格時：

1. **提供樣本**：2-3 篇該作者的文章（500-1000字）
2. **分析節奏**：句長分布、感嘆詞頻率、段落平均長度
3. **指定風格維度**：將該作者的風格翻譯為上述七維度向量
4. **迭代修正**：生成後對照原版，指出具體差異

```python
VOICE_ANALYSIS_PROMPT = """
分析以下文本的風格特征：
1. 句長分布（平均句長、句長範圍）
2. 詞彙層次（日常/書面/學術比例）
3. 情感溫度（主觀/客觀比例）
4. 段落結構（平均段落長度、組織模式）
5. 特色標記（重複詞、感嘆詞、口頭禪）

原文：
{text}
"""
```

---

## AI風格寫作TRAP（常犯錯誤）

| ID | 陷阱 | 正確做法 |
|----|------|---------|
| TRAP-AI-1 | 無限制使用被動語態 | 80% 主動語態，20% 被動語態（必要時）|
| TRAP-AI-2 | 詞彙密度過高（AI文字66% vs 人類64%）| 主動「稀釋」：每段加一句短過渡句 |
| TRAP-AI-3 | 缺少節奏變化 | 長段落後主動加一個短句或疑問句 |
| TRAP-AI-4 | 過度使用「首先、其次、最後」| 改用自然過渡，避免機械化連接詞 |
| TRAP-AI-5 | Persona描述模糊 | 具體化：「用余秋雨《千年一嘆》的史詩感」|

---

## 與古典修辭學的對話

| 古典原則 | AI 時代對應 |
|---------|------------|
| 劉勰「為情造文」| AI先確定核心情感，再潤飾文字 |
| 「風清骨峻」| AI需要「內容有力（骨）＋語氣有溫度（風）」|
| 「隱秀並存」| 重要結論直接說；次要議論含蓄帶過 |
| 體性八體 | 七維度風格向量可對應八體進行映射 |
