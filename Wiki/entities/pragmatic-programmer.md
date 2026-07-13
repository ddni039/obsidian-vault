---
title: The Pragmatic Programmer
created: 2026-07-09
updated: 2026-07-09
uid: e-4a05da22f9eb
type: entity
subtype: book
author: Andrew Hunt, David Thomas
year: "1999 (1st), 2019 (20th Anniversary)"
publisher: Addison-Wesley
pages: ~350 (1st), ~500 (20th)
isbn: "978-0135957059"
tags: [software-craftsmanship, best-practices, maintenance, career, craftsmanship]
confidence: high
status: wiki-entity-only
---

# The Pragmatic Programmer — Andrew Hunt & David Thomas

## About the Authors
- **Andrew Hunt**：Agile manifesto 共同作者，Pragmatic Programmer 系列創始人
- **David Thomas**：Programming 實踐家，Unix 專家
- 共同創辦 Pragmatic Bookshelf 出版社

## Core Philosophy
"**程序员不应局限于任何一种技术，而应注重软件开发的基本原则。**"

## Key Concepts

### 1. The Pragmatic Philosophy
- **Cat Cat's Law**：当存在两种做法且差不多時，選擇較難的那個（短期較難但長期更好）
- **Stone Soup and Boiled Frogs**：用石頭湯故事推動改變，但要防止舒適區慢慢腐蝕
- **Good Enough Software**：不必追求完美，但要知道何時「足夠好」
- **知識組合**：投資你的知識組合（代碼、工具、經驗）——定期、多樣化、刻意

### 2. Debugging
- 心理學比工具有效
- 永遠假設不是你預期的錯
- `printf` 是最被低估的調試工具
- bug 回歸：修復後寫測試，防止復發

### 3. Code Smells（代碼壞味道）
- **重复代码** (Duplicated Code)
- **過長函數** (Long Method)
- **過大類** (Large Class)
- **switch 陳述式** (Switch Statements)
- **temp 變數濫用** (Temporary Field)
- **過度耦合** (Inappropriate Intimacy)

### 4. Refactoring 原則
- 每次小改變 → 測試驗證 → 下一個改變
- 隨時可重構，但先確保有測試覆蓋
- 不在重構同時添加功能

### 5. Testing
- **Test While You Code**：邊寫邊測，不要最後補
- **Property-Based Testing 思維**（現代理解）：測試屬性不只測點值
- **殺蟲程序測試法**：記錄 bug，確保每次重現，最後寫測試

### 6. Build戒律（特別適用於 Hermes 這類多模組專案）

```
Tip 17: Distinguish Business Rules from GUI
Tip 18: Don't Use Magic Numbers
Tip 24: Use Version Control
Tip 25: Fix, Don't Work-Around
Tip 27: Minimize Coupling
Tip 32: Make It Right Before You Make It Fast
```

## 與 Hermes 相關的 Tips

| Tip | Hermes 應用 |
|-----|-----------|
| Tip 24: 修復，不要 workaround | Hermes 的 TRAP 陷阱表機制，固化教訓不重蹈覆轍 |
| Tip 27: 最小化耦合 | hermes-agent 的 plugin ABC 架構 |
| Tip 32: 先求正確，再求快 | `scripts/run_tests.sh` 的 CI-parity 隔離測試 |
| Tip 17: 業務邏輯與 GUI 分離 | TUI (`ui-tui/`) + Gateway (`gateway/`) + Core (`hermes-agent/`) 分離 |
| Tip 36: 文檔化你的弱假設 | `AGENTS.md` 和 skill frontmatter 為假設文檔化 |

## 20th Anniversary Edition 新增內容
- DevOps 與持續交付
- 單元測試工具進化
- 響應式編程
- 自動化基礎設施
- 更多關於合約設計的內容

## See Also
- [[software-testing-maintenance]] — testing and maintenance concepts
- [[software-testing-fundamentals]] — testing fundamentals
- [[debugging]] — debugging techniques
- [[working-effectively-with-legacy-code]] — legacy code refactoring
