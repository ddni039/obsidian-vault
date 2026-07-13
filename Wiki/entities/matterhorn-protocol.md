---
uid: 20260713-matterhorn-protocol
name: Matterhorn Protocol
aka: [Matterhorn, PDF/UA Conformance Testing Model, ISO 14289 test model]
type: entity
tags: [PDF/UA, ISO 14289, accessibility, conformance testing, 31 checkpoints, 136 failure conditions]
related_entities:
  - entities/verapdf-validator.md
related_concepts:
  - concepts/pdf-ua-standard.md
  - concepts/pdf-quality-gate-framework.md
source: |
  PDF Association Matterhorn Protocol：https://pdfa.org/resource/the-matterhorn-protocol/
  Quadient 說明：https://www.quadient.com/en-us/blog/matterhorn-protocol-pdf-accessibility-made-easier
  Matterhorn Protocol 1.0 規範（PDF Association 可免費獲取）
---

# Matterhorn Protocol

## 概述

Matterhorn Protocol 是 ISO 14289（PDF/UA）標準的**可測試合規模型**，由 PDF Association 發布。將抽象的 PDF/UA 標準翻譯成 31 個檢查點、136 個具體失敗條件的清單。

**命名由来**：2013 年發布，代號取自瑞士阿爾卑斯山馬特洪峰——象徵「標準高聳，但可征服」。

## 核心數據

| 指標 | 數值 |
|------|------|
| 檢查點（Checkpoints）| 31 |
| 失敗條件（Failure conditions）| 136 |
| 可自動化驗證 | 89 個 |
| 需人工判斷 | 47 個 |

## 檢查點類別

### 1. 文檔要求（約 5 個檢查點）
- Tagged PDF 存在
- 語言聲明（`/Lang`）
- 標題 metadata（`/Title`）
- 未加密或加密不阻擋 AT

### 2. 結構標籤（約 15 個檢查點）
- 標題層次（H1-H6 不跳級）
- 段落標籤（`<P>` 而非 `<H*>` 偽裝）
- 列表結構（`<L>/<LI>` 而非 `P + •`）
- Artifacts（裝飾性內容標記）

### 3. 非文本內容（約 10 個檢查點）
- Alt text 存在（每個有意義的圖片）
- Alt text 非空（不能是空白或純裝飾）
- 複雜圖片的長描述

### 4. 表格（約 8 個檢查點）
- 表頭行（`<TH>` 而非 `<TD>`）
- 表頭/數據 cell 區分
- 表佈局合理性

### 5. 表單（約 8 個檢查點）
- 欄位標籤（`/T` 和 `/TU`）
- Tab 順序邏輯
- 鍵盤可訪問性

### 6. 導航（約 10 個檢查點）
- 書籤有意義（不是「第 1 頁」）
- 標籤順序與邏輯順序一致
- 內容不被遮擋

## 工具支持

PAC（PDF Accessibility Checker）免費桌面工具，實現了 Matterhorn Protocol 的視覺化呈現，直接展示每個檢查點 Pass/Warn/Fail 狀態。

veraPDF 是最完整的開源實現，覆蓋所有 136 個失敗條件。

## 在 Hermes 的定位

Matterhorn Protocol 是 PDF 審查 L4 層（PDF/UA 合規層）的**行業標準測試基準**。Hermes `pdf-edit` skill 的御史（E）角色執行 PDF 審查時，Matterhorn 31 檢查點提供結構化的審查框架。

與現有 `pdf-edit` TRAP-TRAP 的對應：
- TRAP-TAG-1~4 → 結構標籤類別
- PDF/UA 八步驟清單（Deque）→ 文檔+內容+替代文字+表格+表單+導航

