---
UID: 20260610-hermes-index
STATUS: Active
TYPE: Data
---

# Hermes INDEX

## 1. Summary
> 核心檔案頂層導航。閱讀此檔優先。

## 2. Assumptions & Invariants
* [ ] 核心檔案位於 `~/.hermes/core/`
* [ ] 每檔有前置matter：`UID`、`STATUS`、`TYPE`
* [ ] 所有檔案遵循 5-section Karpathy 模板

## 3. Implementation

### 檔案地圖

```
~/.hermes/
├── core/
│   ├── SPEC.md      # Schema 規範（本文）
│   ├── SOUL.md      # 身份與風格
│   ├── CODEX.md     # API 標準
│   ├── RULES.md     # 安全規則
│   ├── INDEX.md     # 本檔
│   └── AGENTS.md    # 開發指南
├── playbooks/       # 任務 SOP
├── skills/          # 程序知識
├── memories/        # 跨 session 持久記憶
└── auth.json        # SSOT（credentials 專用）
```

### 閱讀順序

```
1. INDEX.md   → 找到需求
2. SOUL.md    → 理解身份
3. CODEX.md   → 掌握 API 操作
4. RULES.md   → 知道紅線
5. AGENTS.md  → 開發細節
```

### STATUS 狀態碼

| Status | 意義 |
|--------|------|
| Draft | 開發中，可能變動 |
| Active | 生產就緒，當前版本 |
| Deprecated | 已廢棄，勿用 |

## 4. Verification

| 檢查 | 指令 |
|------|------|
| 檔案齊全 | `ls ~/.hermes/core/` |
| 全部 Active | `grep "STATUS: Active" ~/.hermes/core/*.md | wc -l`（期望 6）|
| 格式合規 | `grep "^## [0-9]" ~/.hermes/core/*.md | wc -l`（期望 30）|

## 5. Changelog

* `2026-06-10`: 初始版本 — 檔案地圖、閱讀順序、狀態碼