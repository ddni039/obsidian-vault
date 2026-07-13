---
uid: 20260713-pdf-ua-standard
name: PDF/UA ISO 14289 標準
aka: [PDF/UA, PDF/UA-1, PDF/UA-2, ISO 14289, accessible PDF, universal accessibility]
type: concept
tags: [PDF, PDF/UA, ISO 14289, accessibility, tagged PDF, screen reader, Matterhorn, WCAG]
related_entities:
  - entities/matterhorn-protocol.md
  - entities/verapdf-validator.md
related_concepts:
  - concepts/pdf-a-standard.md
  - concepts/pdf-quality-gate-framework.md
  - concepts/pdf-tagged-structure.md
trigger: |
  PDF/UA, ISO 14289, 可及性, 無障礙, 螢幕閱讀器, 標籤PDF, 語義標記,
  Matterhorn Protocol, PAC, veraPDF, WCAG, PDF/UA-1, PDF/UA-2, 殘障通道,
  替代文字, Alt text, 閱讀順序, 表單無障礙
source: |
  Nutrient PDF/UA 完全指南：https://www.nutrient.io/blog/what-is-pdf-ua/
  PDF Association ISO 14289 資源：https://pdfa.org/resource/iso-14289-pdfua/
  Matterhorn Protocol：https://pdfa.org/resource/the-matterhorn-protocol/
  QualiBooth PDF Accessibility Guide：https://www.qualibooth.com/resources/pdf-accessibility-guide/
---

# PDF/UA ISO 14289 標準

## 定義

PDF/UA（PDF/Universal Accessibility，ISO 14289）是 PDF 可及性的國際標準，定義了 PDF 必須包含什麼內容才能讓螢幕閱讀器、放大鏡、點字顯示器、語音控制等輔助技術可靠地解讀文檔。

核心機制：**Tagged PDF**（標籤化 PDF）——在視覺內容之外，攜帶獨立的結構樹，描述每個內容片段的語義角色。

## 版本歷史

| 版本 | 發布 | 基於 | 狀態 |
|------|------|------|------|
| PDF/UA-1（ISO 14289-1:2014）| 2014 | PDF 1.7 | 目前主流驗證目標 |
| PDF/UA-2（ISO 14289-2:2024）| 2024 | PDF 2.0 | 最新版本，對齊現代 PDF 功能 |

## 核心要求

### 文檔級要求
- 必須是 Tagged PDF
- 必須聲明主要語言（如 `en-US`、`zh-TW`）
- 必須有標題 metadata
- 加密不得阻擋輔助技術讀取

### 內容結構
- 標題、段落、列表、表格、圖片必須有正確的結構標籤
- H1-H6 必須邏輯嵌套（不可跳級）
- 裝飾性元素標記為 artifacts（輔助技術跳過）

### 圖片替代文字
- 資訊性圖片：需要有意義的 Alt text（總結結論，非描述視覺）
- 複雜圖片：短 Alt + 長描述
- 裝飾性圖片：`/Alt=""`（標記為 artifact）

### 表格結構
- `<Table>` / `<TR>` / `<TH>`（標題格）/ `<TD>`（數據格）
- 標題行必須標記為 header cells
- 不得用 tab 或空格模擬表格

### 表單
- 每個欄位必須有標籤
- 必須有邏輯 tab 順序
- 必須支持鍵盤導航

## Tagged PDF 機制

```
普通 PDF：標記叢集 → 螢幕閱讀器猜測意義 → 不確定
Tagged PDF：結構樹 → 明確語義 → 可靠解讀
```

Tagged PDF 攜帶的結構信息：
- **邏輯閱讀順序**（獨立於視覺位置）
- **替代文字**（每個有意義的非文本元素）
- **語言 metadata**（文檔級 + span 級）
- **表格結構**（header vs data cells）
- **Unicode 映射**（選中文字 = 顯示 glyph）

## Matterhorn Protocol（PDF/UA 合規測試模型）

31 個檢查點 × 136 個失敗條件：
- **89 個**：可完全自動化驗證
- **47 個**：需要人工判斷

詳見：`entities/matterhorn-protocol.md`

## 主流工具

| 工具 | 類型 | 覆蓋 |
|------|------|------|
| **veraPDF** | 開源 CLI | PDF/A + PDF/UA 全覆蓋 |
| **PAC (PDF Accessibility Checker)** | 桌面工具 | PDF/UA 視覺化報告 |
| Adobe Acrobat Preflight | 商業 | PDF/UA + 自訂剖象 |
| PDFix SDK | 商業 API | PDF/UA + 批量修復 |

## PDF/UA vs WCAG

| 維度 | WCAG 2.2 | PDF/UA（ISO 14289）|
|------|---------|-------------------|
| 目標 | 網站 + 數位內容 | PDF 文檔專用 |
| 焦點 | 對比度、鍵盤導航、標題 | 標籤樹、語義結構、Alt text |
| 關係 | PDF 內嵌網頁內容參考 WCAG | PDF 自身結構參考 PDF/UA |

## Hermes 對接

現有 TRAP-TRAP 陷阱已覆蓋：

| TRAP | 對應 PDF/UA 約束 |
|------|-------------------|
| TRAP-TAG-1 | H1→H3 跳躍（PDF/UA 失敗）|
| TRAP-TAG-2 | 圖片無 Alt text（PDF/UA 失敗）|
| TRAP-TAG-3 | 表格無表頭（PDF/UA 失敗）|
| TRAP-TAG-4 | ReportLab 免費版 tagged 功能有限 |

