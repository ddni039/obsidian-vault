---
tags: [writing, clarity, precision, anti-fluff, zinsser, strunk, leguin, books]
date: 2026-07-16
related_skills: [anti-fluff]
---

# 精準寫作書籍研究：降低廢話能力的核心讀物

## 概述

針對「降低 Agent 廢話輸出能力」這一目標，從 Writing Clarity / Anti-Fluff 領域，識別出三本最具實證價值的經典著作，均從 Internet Archive 免費下載。

---

## 圖書清單

### 1. On Writing Well (William Zinsser, 1976)

| 欄位 | 值 |
|:---|:---|
| **作者** | William Knowlton Zinsser（耶魯寫作教授）|
| **出版** | HarperCollins，30th Anniversary Edition |
| **頁數** | 322 頁 |
| **大小** | 4.5 MB |
| **下載來源** | archive.org / dn790000.ca.archive.org |
| **ISBN** | 978-0060891541 |
| **核心定位** | 非虛構寫作的「聖經」，聚焦clarity、simplicity、brevity、humanity |

**對 anti-fluff 的關鍵貢獻：**

Zinsser 的核心原則：「The secret of good writing is to strip every sentence to its cleanest components.」

直接相關的章節：
- **Chapter 3: Clutter** — 系統性分析廢話來源（官僚語言、被動語態、無意義形容詞）
- **Chapter 4: Style** — 人聲（human voice）的建立
- **Chapter 5: Words** — 精確用詞，反對模糊修飾

**可提取為 anti-fluff 約束的具體規則：**
```
1. 刪除所有可以刪除的詞（而不損失意義）
2. 每個形容詞都必須有存在的理由
3. 被動語態一律禁止
4. 先濃縮，再擴展
```

**對 Hermes 的具體應用：**
- Phase 1（寫作前約束）可直接引用 Zinsser 的 Clutter 檢測清單
- Signal Density 計算的理論基礎：Zinsser 的「每句話負擔信息量」原則

---

### 2. The Elements of Style (Strunk & White, 1920/1979)

| 欄位 | 值 |
|:---|:---|
| **作者** | William Strunk Jr. + E. B. White |
| **出版** | Macmillan，4th Edition |
| **頁數** | 82 頁 |
| **大小** | 243 KB |
| **下載來源** | archive.org（PDFy mirror）|
| **地位** | 全球最暢銷的寫作指南之一（超過1000萬冊）|

**對 anti-fluff 的關鍵貢獻：**

最著名的三條規則：
```
1. Omit needless words.（刪除冗詞 — 英文写作金律）
2. Use the active voice.（使用主動語態）
3. Put the emphatic words of a sentence at the end.（重點放句尾）
```

第八章「An Approach to Style」提出：
- 使用強動詞替代「weak verbs + adverb」模式
- 避免形容詞數量詞（many、few、several）混用
- 文章的節奏感來自句式變化，而非填充詞

**與 anti-fluff skill 的整合點：**
- `E-OUTPUT-FLUFF` 的觸發條件可直接參照 Strunk 的「needless words」定義
- 「句尾重點」原則可內化為「第一句話不要下結論」

---

### 3. Steering the Craft (Ursula K. Le Guin, 1998)

| 欄位 | 值 |
|:---|:---|
| **作者** | Ursula K. Le Guin（科幻/奇幻文學大師）|
| **出版** | The Eighth Mountain Press，修訂版2015 |
| **頁數** | 105 頁 |
| **大小** | 789 KB |
| **下載來源** | archive.org |
| **核心定位** | 21世紀敘事寫作指南，聚焦句式節奏與故事聲音 |

**對 anti-fluff 的關鍵貢獻：**

Le Guin 在 Chapter 1 提出的「Sentence Sound」概念，直接對應廢話檢測：

> 「If the reader's mind slides off the sentence into some drowsy reflex, the sentence isn't doing its job.」

核心技法：
- **Severe Cutting**（嚴酷刪減）：將一段文字強制刪減一半，測試核心信息是否還在
- **句式長度分布**：長短句交替，杜絕「機器人節奏」的單一長句
- **聲音與停頓**：用句號控制節奏，而非用「然而」、「但是」連接

**與 anti-fluff skill 的整合點：**
- Phase 2 自檢階段可使用「Severe Cutting」技法
- 廢話的另一個維度：節奏單一（所有句子同長度），而不僅是詞彙冗餘

---

## 三本書的互補結構

| 維度 | On Writing Well | Elements of Style | Steering the Craft |
|:---|:---|:---|:---|
| **聚焦** | 非虛構寫作 | 英語風格基礎 | 敘事/創意寫作 |
| **核心武器** | Clutter 識別 | Needlessly words | Severe Cutting |
| **主要受眾** | 記者、知識工作者 | 所有英語寫作者 | 小說/故事作者 |
| **對 AI 的價值** | 系統性反廢話框架 | 最小化精確度原則 | 節奏/聲音檢測 |
| **可操作性** | 高（清單式）| 極高（20條規則）| 中（需主觀判斷）|

---

## 對 anti-fluff Skill 的強化建議

結合三本書的精華，anti-fluff 可升級為：

```
Phase 1+（寫作前約束）：
  → Zinsser Clutter 清單（被動語態、官僚詞彙、無謂形容詞）
  → Strunk Rule 1：刪除所有可以刪除的詞

Phase 2+（自檢）：
  → Le Guin Severe Cutting：強制刪減50%文字，核心信息還在嗎？
  → Strunk Rule 3：重點放句尾（結論不開頭）

Phase 3+（審計）：
  → Zinsser Signal Density（事實/數字密度）
  → Le Guin 節奏檢測（句長分布是否單一）
  → Strunk 被動語態檢測（0次被動）
```

---

## 下載狀態

| 書名 | 檔案路徑 | 頁數 | 格式 | 狀態 |
|:---|:---|---:|:---:|:---:|
| On Writing Well | `~/books/zinsser_on_writing_well.pdf` | 322 | PDF（可全文檢索）| ✅ 已下載 |
| The Elements of Style | `~/books/strunk_white_elements_of_style.pdf` | 82 | PDF（可全文檢索）| ✅ 已下載 |
| Steering the Craft | `~/books/leguin_steering_the_craft.pdf` | 105 | PDF（可全文檢索）| ✅ 已下載 |

---

## 參考來源

- Zinsser, W.K. (2006). *On Writing Well: The Classic Guide to Writing Nonfiction* (30th ed.). HarperCollins.
- Strunk, W. Jr. & White, E.B. (1979). *The Elements of Style* (4th ed.). Macmillan.
- Le Guin, U.K. (2015). *Steering the Craft: A Twenty-First-Century Guide to Sailing the Sea of Story* (rev. ed.). Mariner Books.
