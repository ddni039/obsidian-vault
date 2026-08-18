---
name: Playwright MCP
slug: playwright-mcp
version: 1.0.0
description: "瀏覽器自動化 via Microsoft Playwright MCP。提供無頭瀏覽器控制，支援開頁、點擊、填表、截圖、快照抓取。適合 JS 渲染頁面、多步驟表單、截圖证据擷取。"
changelog: "2026-04-03 初版安裝"
metadata: {"emoji":"🎭","requires":{"bins":["node","npx","playwright"]},"os":["darwin","linux","win32"]}
---

## 安全評估

| 項目 | 狀態 | 說明 |
|------|------|------|
| 發布者 | ✅ Microsoft 官方 | microsoft/playwright-mcp |
| 數據收集 | ✅ 無外部收集 | 純本地執行 |
| 瀏覽器隔離 | ✅ Playwright managed | 不綁定真實 Chrome profile |
| 隱私風險 | ✅ 低 | 無須擔心 |

## 安裝狀態

```bash
npm install -g @playwright/mcp    # ✅ 已安裝 (v0.0.70)
```

## 啟動方式

### 方式一：直接 npx（臨時）
```bash
npx @playwright/mcp --headless
```

### 方式二：全局指令（推薦）
```bash
playwright-mcp --headless
```

## 常用工具動作

| 動作 | 用途 |
|------|------|
| `browser_navigate` | 開啟指定 URL |
| `browser_snapshot` | 取得頁面結構快照（無截圖） |
| `browser_screenshot` | 截圖（像素級） |
| `browser_click` | 點擊頁面元素 |
| `browser_type` | 輸入文字 |
| `browser_select_option` | 選擇下拉選項 |
| `browser_evaluate` | 執行 JavaScript |
| `browser_download` | 下載檔案 |

## 使用時機

- ✅ JS 渲染頁面（SPA、React、Vue）抓取
- ✅ 需要登入但不希望綁定真實 Chrome
- ✅ 自動化填表、多步驟操作
- ✅ 截圖存據、PDF 生成
- ❌ 不需要：已經有 OpenClaw 內建 browser profile（兩者功能重疊）

## OpenClaw 整合方式

OpenClaw 沒有原生 MCP 客戶端，此 Skill 需透過 Claude Code / Codex 等 Coding Agent 呼叫：

```bash
# 在 Claude Code 中啟動
claude mcp add playwright npx @playwright/mcp@latest
```

## 卸載

```bash
npm uninstall -g @playwright/mcp
```
