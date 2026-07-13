---
title: Debug It! — Find, Repair, and Prevent Bugs
created: 2026-07-09
updated: 2026-07-09
uid: e-d698bfcd7bf7
type: entity
subtype: book
author: Paul Butcher
year: 2009
publisher: Pragmatic Bookshelf
pages: ~250
isbn: "978-1934356509"
tags: [debugging, troubleshooting, bug-prevention, software-quality]
confidence: high
status: wiki-entity-only
---

# Debug It! — Paul Butcher

## About the Author
Paul Butcher 是軟體工程師兼作家，專注於軟體品質與團隊協作。

## Core Philosophy
> Debugging is a **craft**, not just a technical task. It requires a systematic approach combined with deep understanding of the system.

## The Four-Phase Debugging Process

### Phase 1: Reproduce
確定你能穩定地再現問題。

步驟：
1. **隔離問題** — 找到觸發 bug 的最小輸入
2. **自動化** — 讓重現步驟可以腳本化
3. **隔離差異** — 什麼環境/輸入/操作序列導致失敗？

常見錯誤：
- 嘗試在完整系統上調試
- 沒有記錄重現步驟
- 假設 bug 隨機

### Phase 2: Identify the Source
確定問題的真正根源，不是表象。

技法：
- **假設-演繹法**（Hypothetico-deductive）：提出假設 → 設計實驗 → 驗證或否定
- **刪減法**（Divide and conquer）：在程式的一半插入斷點，看是否仍現
- **追蹤法**：追蹤數據流/控制流
- **日誌挖掘**：檢查應用/系統日誌

關鍵：問「為什麼這個看起來是這樣？」至少 5 次。

### Phase 3: Determine the Fix
確定怎麼修復。

選擇：
- **Hotfix**：最小改變，立即部署（應急）
- **Proper fix**：找到根本原因，全面修復
- **Test-first fix**：先寫測試重現 bug，再修復

準則：
- 修復代價 > bug 影響？→ 考慮不修
- 修復會引入新 bug？→ 評估風險
- 繞過 vs. 修復？→ 優先修復

### Phase 4: Fix and Validate
修復並確認有效。

步驟：
1. 寫測試捕獲這個 bug
2. 修復代碼
3. 運行測試確認通過
4. 確認修復沒有破壞其他功能

## Prevention: Beyond the Individual Bug

### 1. 缺陷根因分類（Bug Taxonomy）
常見根因模式：
- **需求層面**：誤解、不完整、變更
- **架構層面**：設計決策導致耦合/複雜性
- **實現層面**：邏輯錯誤、邊界條件
- **測試層面**：缺失測試、測試不穩定

### 2. 預防策略
- **代碼審查**（Code Review）
- **持續集成**（CI）
- **測試驅動開發**（TDD）
- **簡單設計**
- **頻繁提交**

### 3. Debugging vs. Testing
- **測試** = 預防：找出系統中的錯誤
- **Debugging** = 補救：修復已發現的錯誤
- 兩者都需要，但預防比補救便宜

## 与 Hermes 相关

Hermes 的 `systematic-debugging` skill（4-phase 流程）與 Butcher 的四階段高度一致：
1. Reproduce → 隔離最小可重現案例
2. Identify → 根因分析
3. Determine fix → 評估 hotfix vs. proper fix
4. Fix & Validate → 測試覆蓋 + 運行確認

`hermes logs` 命令類似於 Butcher 的日誌挖掘技法。

## See Also
- [[debugging]] — broader debugging techniques
- [[software-testing-maintenance]] — testing and prevention
- [[software-testing-fundamentals]] — testing fundamentals
- [[working-effectively-with-legacy-code]] — fixing untested code
