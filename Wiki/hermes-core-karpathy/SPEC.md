---
UID: 20260610-hermes-spec
STATUS: Active
TYPE: Guide
---

# Hermes 原子化編輯準則

## 1. Summary
> 所有知識庫檔案的綁定結構規範。定義 5-section 模板與 Logic Audit 流程。

## 2. Assumptions & Invariants
* [ ] 檔案位於 `~/.hermes/core/` 或 `~/Obsidian/Hermes Agent/Wiki/`
* [ ] 每檔有前置matter：`UID`、`STATUS`、`TYPE`
* [ ] 每檔 5 區塊結構（H2 為最深標題）
* [ ] 編輯完成前執行 Logic Audit
* [ ] TYPE 值為封閉枚舉：Logic | Tool | Data | Personality | Guide

## 3. Implementation

### 3.1 預設結構（5-Section）

新建模組時，複製 TEMPLATE.md 並填寫。**所有模組章節使用 H2。**

嵌入式範例（如 SPEC.md 3.1 中的模板）可使用 H3+，但**不計入模組本體的 5-section 結構**。

```markdown
---
UID: YYYYMMDD-slug
STATUS: [Draft|Active|Deprecated]
TYPE: [Logic|Tool|Data|Personality|Guide]
---

# 模組標題

## 1. Summary
> 一句話說明。

## 2. Assumptions & Invariants
* [ ] 前提 A

## 3. Implementation
> 代碼或設定。原子化、單一職責。

```bash
# 程式碼
```

## 4. Verification
| 輸入 | 預期 | 驗證 |
|------|------|------|
| ... | ... | `command` |

## 5. Changelog
* `YYYY-MM-DD`: 事件 — 效果
```

### 3.2 Logic Audit（10 項檢查）

編輯完成前必做：

```
[ ] 1. 前置matter齊全（UID/STATUS/TYPE）
[ ] 2. 恰好 5 區塊（Summary/Assumptions/Implementation/Verification/Changelog）
[ ] 3. 無硬編碼密鑰（API key、token、secret）
[ ] 4. 檔案 < 500 字 / ~3000 chars
[ ] 5. Verification 至少一項
[ ] 6. Changelog 有本次編輯記錄
[ ] 7. TYPE 為封閉枚舉值（Logic|Tool|Data|Personality|Guide）
[ ] 8. H3 僅限 Implementation 區段內；嚴禁 H4+
[ ] 9. 程式碼區塊標明語言
[ ] 10. 引用 SPEC.md 為 schema 依據
```

**任一失敗 → 先修復，再提交。**

### 3.3 TYPE 封閉枚舉

| TYPE | 用途 | 範例 |
|------|------|------|
| Logic | 業務邏輯、判斷規則 | CODEX.md、RULES.md |
| Tool | 工具規格、命令腳本 | playbooks/*.md |
| Data | 資料結構、格式定義 | INDEX.md |
| Personality | 身份定義、溝通風格 | SOUL.md |
| Guide | 指南、SOP、操作手冊 | SPEC.md、TEMPLATE.md |

### 3.4 System Prompt 整合

每個檔案為**獨立模組**，LLM 可一次解析：
1. 立即上下文（Summary）
2. 前置條件（Assumptions）
3. 實作細節（Implementation）
4. 驗證方法（Verification）
5. 歷史變更（Changelog）

## 4. Verification

| 檢查 | 指令 |
|------|------|
| 全域合規 | `find ~/.hermes/core ~/Obsidian/Hermes\ Agent/Wiki -name "*.md" -exec grep -L "^UID:" {} \;` |
| 全部 H2 最深 | `find ~/.hermes/core -name "*.md" -exec grep -c "^### " {} \;`（期望 0）|
| TYPE 封閉 | `grep "^TYPE:" ~/.hermes/core/*.md \| grep -Ev "^(Logic\|Tool\|Data\|Personality\|Guide):" \| grep -v "^\s*#"` |
| Schema 版本 | `grep "^UID:" ~/.hermes/core/SPEC.md \| head -1` |

## 5. Changelog

* `2026-06-10`: 初始版本 + TYPE 封閉枚舉對齊 + Audit #8 H3 範例例外說明