# 寫作風格研究日誌 | 2026-07-13

## 研究目標

提升自然語言寫作品質——覆盖：
- 古典漢語修辭學（文心雕龍）
- 現代漢語散文寫作技法
- 英文經典風格指南（Strunk & White / Williams）
- AI 風格寫作與 persona 引導

---

## 閱讀清單

### 古典修辭學（中文）

| 書名 | 作者 | 核心價值 |
|------|------|---------|
| 《文心雕龍》| 劉勰（南北朝）| 體大思精：文體論＋創作論＋批評論，涵蓋從字句到篇章的全部修辭規律 |
| 《說文解字》| 許慎（東漢）| 漢字形音義源流，寫作用字精準之根基 |
| 《修辭學》| 陳望道（1932）| 現代漢語修辭學奠基之作，系統化引進西方修辭學 |
| 《漢語修辭學》| 王希杰商務印書館 | 當代漢語修辭學權威教材 |

### 現代中文寫作（散文・商業）

| 書名 | 作者 | 核心價值 |
|------|------|---------|
| 《精準寫作》| 洪震宇 | 系統化中文寫作指南：標題、開場、內容結構、結論，在地化實戰 |
| 《素人也能寫出好文章》| （日） 文章の教室 | 從零建立寫作習慣 |
| 《大人的11堂寫作課》|  | 中文書寫實戰技法 |
| 《流量寫作密碼》| 竹村俊助 | 自媒體時代變現寫作 |
| 《文字變現！誠懇文案力》| 王繁捷 | 商業文案實戰，400萬業績驗證 |
| 《寫作，是最好的自我投資》| 陳立飛 | 自媒體商業寫作思維 |

### 英文經典（風格・修辭）

| 書名 | 作者 | 核心價值 |
|------|------|---------|
| *The Elements of Style* (Strunk & White) | William Strunk Jr. / E.B. White | 英語風格聖經，句構與用詞精準原則，Cited 6551+ |
| *Style: Toward Clarity and Grace* | Joseph M. Williams | 進階英文風格：清晰、連貫、簡潔 |
| *The Sense of Structure* |  | 句子與段落結構的認知原理 |
| *On Writing Well* | William Zinsser | 非虛構寫作（Non-fiction）經典 |

### AI 風格寫作研究

| 主題 | 來源 | 核心發現 |
|------|------|---------|
| LLM Style Transfer | arxiv.org/html/2507.22168v1 (EMNLP 2025) | Persona-based prompting 可模擬多樣寫作風格 |
| LLM as Writing Judge | MDPI Applied Sciences 2025 | LLM 評估創意寫作與人類評分高度相關 |
| AI vs Human Prose | PMC 13061212 (2026) | AI 生成的摘要詞彙密度顯著更高（Human 63.7% vs AI 66.3%）|
| Style Prompting | Medium @alishafique3 | 指令 LLM 生成特定文體/語氣的技法 |

---

## 研究發現摘要

### 《文心雕龍》核心框架（劉勰，約西元500年）

> 「文心」者，言為文之用心也；「雕龍」者，喻如雕鏤龍文般精雕細琢之功。

**全書結構：25篇（上）＋25篇（下）**

| 分部 | 篇數 | 核心命題 |
|------|------|---------|
| 文體論 | 20篇 | 各類文體之特質與規範（詩、賦、書、記、論、說…）|
| 創作論 | 19篇 | 構思、謀篇、條理、聲律、比興、風骨、情采 |
| 批評論 | 5篇 | 批評方法與文學史觀 |
| 總結 | 1篇 | 〈序志〉：全書宗旨與結構說明 |

**關鍵創作論命題：**

1. **情采**：「情者，文之經；辭者，理之緯」——情感與文采如經緯交織，反對空洞藻飾
2. **風骨**：「風清骨峻」，文章需有力度（骨）與感染力（風）
3. **比興**：「比則譴責以寓情，興則見今之失不嫌於同」——隱喻與象徵的運用
4. **隱秀**：「情在詞外曰隱，狀溢目前曰秀」——含蓄與鮮明的辯證
5. **通變**：「變則其久，通則不乏」——繼承與創新的平衡
6. **熔裁**：「規範本體謂之熔，剪裁浮詞謂之裁」——内容取捨的藝術

### AI 寫作風格核心技法

**1. Style Prompting（風格提示）**
```
System: 你是一位嚴肅的散文家，文字風格深受余秋雨影響。
User: [content]
```
關鍵維度：正式程度、句式長度、詞彙選擇、情感溫度

**2. Voice Preservation（人聲保留）**
- 提供 2-3 篇自己寫的文章作為風格樣本
- LLM 從樣本學習：節奏、感嘆詞頻率、主觀/客觀比例

**3. Multi-Draft Iteration（多輪迭代）**
- Draft 1：快速生成，捕捉核心內容
- Draft 2：風格潤飾，指定「換用更具體的動詞」
- Draft 3：節奏調整，長短句交替

### 英文風格核心原則（Strunk & White）

1. **Make the paragraph the unit** — 每段只說一件事
2. **Use active voice** — 主動語態優先（"Dumfound" vs "was dumfounded by"）
3. **Put statements in positive form** — 避免 "not…any" → "no"
4. **Use definite, specific, concrete language** — 抽象詞是萬惡之源
5. **Omit needless words** — 「這句話的風格是什麼？」→「它的風格就是省略」
6. **Keep related words together** — 修飾語與被修飾語不可被其他詞隔開
7. **Don't break the rules in the wrong direction** — 先懂規則，再談打破

---

## 待攝入計畫

- [ ] entities/wenxin-diaolong.md（文心雕龍實體）
- [ ] concepts/classical-chinese-rhetoric.md（古典修辭學概念）
- [ ] concepts/modern-chinese-prose-techniques.md（現代散文技法）
- [ ] concepts/english-style-guide.md（英文風格指南）
- [ ] concepts/ai-writing-style-transfer.md（AI風格遷移技法）
- [ ] entities/jiang-zhenyu-or-similar-modern-chinese-writing-master.md（如有合適實體）
