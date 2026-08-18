---
UID: 20260610-hermes-template
STATUS: Active
TYPE: Guide
---

# Hermes 5-Section 模板

## 1. Summary
> 新建知識庫模組時的標準起點。複製並填寫。

## 2. Assumptions & Invariants
* [ ] 目的地為 `~/.hermes/core/` 或 `~/Obsidian/Hermes Agent/Wiki/`
* [ ] UID 全域唯一（格式：`YYYYMMDD-slug`）
* [ ] 內容小於 500 字

## 3. Implementation

```markdown
---
UID: YYYYMMDD-模組slug
STATUS: Active
TYPE: [Logic|Tool|Data|Personality|Guide]
---

# 模組標題

## 1. Summary
> 一句話說明本模組的核心價值。

## 2. Assumptions & Invariants
* [ ] 前提條件 A
* [ ] 前提條件 B

## 3. Implementation
> 代碼或設定。原子化、單一職責。

```bash
# 程式碼
```

## 4. Verification
| 輸入 | 預期 | 驗證指令 |
|------|------|----------|
| ... | ... | `command` |

## 5. Changelog
* `YYYY-MM-DD`: 建立 — 初始版本
```

### TYPE 值（封閉枚舉）

| TYPE | 用途 |
|------|------|
| Logic | 業務邏輯、判斷規則、流程定義 |
| Tool | 工具規格、命令腳本、工具函式 |
| Data | 資料結構、資料庫、格式定義 |
| Personality | 身份定義、溝通風格、行為原則 |
| Guide | 指南、SOP、操作手冊、模板 |

## 4. Verification

| 檢查 | 指令 |
|------|------|
| 新模組符合 schema | 複製上方模板後： `grep "^## [0-9]" newfile.md \| wc -l`（期望 5）|
| TYPE 為封閉值 | `grep "^TYPE:" newfile.md \| grep -E "(Logic\|Tool\|Data\|Personality\|Guide)"` |

## 5. Changelog

* `2026-06-10`: 建立模板，枚舉 TYPE 值（Logic\|Tool\|Data\|Personality\|Guide）