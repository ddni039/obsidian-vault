---
title: "Software Testing and Analysis — Pezzè & Young"
created: 2026-07-10
updated: 2026-07-10
uid: e-72cc5413219a
type: entity
subtype: book
author: Mauro Pezzè, Michal Young
year: "2008"
publisher: Wiley
isbn: "978-0471455924"
pages: ~450
tags: [software-testing, static-analysis, dynamic-analysis, test-planning, quality]
---

# Software Testing and Analysis — Pezzè & Young

## 核心定位

軟體測試與分析的系統性教科書，覆蓋從測試規劃到缺陷預防的完整光譜。與其他書籍的差異化：
- **與 Meszaros（xUnit Test Patterns）**：Pezzè/Young 側重測試策略與規劃，Meszaros 側重單元測試壞味道與重構
- **與 Kaner（測試定義）**：Pezzè/Young 提供結構化分析框架，Kaner 側重自由度與探索式測試
- **與 NIST 2002 研究**：引用國家標準與技術研究院的 Bug Cost 數據（見下）

## 測試分析層次

### 靜態分析（Static Analysis）
不執行程式的測試方法：
- **程式碼審查**（Code Review）：人工閱讀發現邏輯錯誤
- **語義分析**：型別檢查、指標操作、記憶體洩漏靜態規則
- **覆蓋率分析**：靜態推導哪些程式路徑可達

### 動態分析（Dynamic Analysis）
執行程式的測試方法：
- **黑盒測試**：基於規格輸入/輸出，不依賴實作
- **白盒測試**：基於程式結構（分支、路徑、覆蓋率）
- **灰盒測試**：結合兩者，部分了解內部結構

### 被動測試（Passive Testing）
監控系統運行而不注入測試案例：
- **軌跡驗證**：日誌模式識別異常行為
- **效能監控**：響應時間/吞吐量異常檢測
- **狀態機監控**：預期狀態轉換序列

## 測試策略框架

### 測試金字塔
Pezzè/Young 強調：
- 大量**單元測試**（快速、隔離、確定性）
- 適量**整合測試**（組件間介面）
- 少量**系統測試**（端到端行為）

### 測試優先順序
1. **安全關鍵**：生命攸關的程式碼（航空、醫療）
2. **業務關鍵**：核心營運邏輯
3. **常見路徑**：使用者最頻繁觸發的場景
4. **例外路徑**：錯誤處理、邊界條件

## 缺陷分類（Defect Taxonomy）

| 類別 | 說明 | 範例 |
|------|------|------|
| **邏輯錯誤** | 條件判斷錯誤 | `if (a > b)` 寫成 `if (a >= b)` |
| **介面錯誤** | 組件間契約破壞 | 參數型別不符、副作用未預期 |
| **遺漏錯誤** | 應有功能缺失 | 忘記處理空指標、邊界條件 |
| **計時錯誤** | 競爭條件、死結 | 併發存取共享資源 |
| **資料錯誤** | 狀態汙染 | 全域變數跨測試殘留 |

## Oracle Problem

「預言問題」：如何確認測試輸出是正確的？
- **顯式 Oracle**：測試斷言有明確預期值
- **隱式 Oracle**：差異測試（執行新舊版本比對輸出）
- **參考 Oracle**：golden file / snapshot 比對
- **暗示 Oracle**：不變量（invariants）如記憶體洩漏檢測

## NIST 2002 Bug Cost 研究（引用）

根據 NIST 2002 研究（參見 `concepts/software-testing-maintenance.md`）：
- 軟體缺陷在**開發階段**修復成本為 1x
- 在**測試階段**修復成本為 6x
- 在**發布後**修復成本為 15-100x

→ 強調**早期測試**與**預防勝於補救**的經濟學動機

## Hermes 應用

- **靜態分析**：Hermes `hermes logs` 結構化日誌相當於被動測試
- **動態分析**：`session_search` 提供對話軌跡挖掘，識別錯誤模式
- **測試策略**：`tri-role-pipeline` 的御史審計呼應「預防勝於補救」原則
- **Bug 分類**：`sop-design-maintenance-errors` 的 TRAP 陷阱表類似 Pezzè 缺陷分類

## 關聯

- [[software-testing-fundamentals]] — Wikipedia 軟體測試基礎
- [[software-testing-maintenance]] — 軟體測試維護概念
- [[xunit-test-patterns]] — Meszaros 單元測試壞味道
- [[debugging]] — 偵錯技術
