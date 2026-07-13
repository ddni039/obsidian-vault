---
title: PDF Rendering — 4-Way Architecture (PyMuPDF vs PDF.js vs PDFium vs Native)
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [concept, pdf-rendering, pymupdf, pdfjs, pdfium, browser-pdf, server-side-rendering, image-rasterization, wasm, pdf-quality, pdf-performance, hermes-pdf-rendering, layer-1]
sources:
  - raw/articles/pdf-rendering-bible-2026-07-13.md
confidence: high
---

# PDF Rendering — 4-Way Architecture

## 定義

**PDF 渲染** ≠ PDF 製作：
- **PDF 製作（Generation）**：從零建立 PDF（ReportLab、WeasyPrint、Playwright）
- **PDF 渲染（Rendering）**：將現有 PDF 轉換成可視形式（顯示、轉圖片、預覽）

---

## 4-Way 渲染架構

```
┌──────────────────────────────────────────────────────┐
│  1. Browser Native（HTML5 embed / iframe）           │
│     - <embed src="file.pdf">                        │
│     - 依賴瀏覽器內建 PDF 檢視器                      │
│     - 速度最快，質量取決於瀏覽器                      │
└──────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────┐
│  2. PDF.js（JavaScript Canvas）                     │
│     - Mozilla 開源（Apache 2.0）                    │
│     - 全 JavaScript，無需服務端                      │
│     - 質量中等，Web 標準                              │
│     ⚠️ PDF.js v4 有 WASM CSP 問題                    │
└──────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────┐
│  3. PDFium（Chromium 內核 WASM）                    │
│     - Google 維護（BSD）                             │
│     - 渲染質量 = Chrome 瀏覽器                       │
│     - EmbedPDF 2026 新開源方案                       │
└──────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────┐
│  4. Server-Side Rasterization（Python/Rust/Go）     │
│     - PyMuPDF（Python，無外部依賴）⭐                │
│     - pdf2image（Python，需 Poppler）               │
│     - pdfium-render（Rust）                         │
│     - 輸出：PNG/JPEG/WebP                            │
└──────────────────────────────────────────────────────┘
```

---

## PyMuPDF 渲染（原創精華）

### 核心 API

```python
import fitz

doc = fitz.open("document.pdf")
page = doc[0]

# 三級 DPI
mat_72   = fitz.Matrix(1.0, 1.0)   # 72dpi = 螢幕
mat_144  = fitz.Matrix(2.0, 2.0)   # 144dpi = 預覽
mat_300  = fitz.Matrix(4.167, 4.167)  # 300dpi = 印刷

pix = page.get_pixmap(matrix=mat_144, alpha=False)
pix.save("output.png")
```

### 渲染參數

| 參數 | 值 | 說明 |
|------|-----|------|
| `matrix` | `Matrix(dpi/72, dpi/72)` | 縮放矩陣 |
| `alpha` | `False` | 無透明度（更快）|
| `annots` | `True` | 包含註釋 |
| `clip` | `Rect` | 只渲染區域 |

---

## 性能優化

### 五大策略

| 策略 | 實現 |
|------|------|
| **DPI 控制** | 預覽 144dpi，列印 300dpi |
| **虛擬滾動** | 只渲染視口內頁面 |
| **CDN 緩存** | 渲染結果緩存 |
| **並發渲染** | 多線程渲染不同頁面 |
| **漸進式** | 先低 DPI → 再高 DPI |

---

## PDF.js vs PDFium 對比

| 維度 | PDF.js | PDFium |
|------|--------|--------|
| **質量** | 中等（Canvas 2D）| 高（Chromium 內核）|
| **速度** | 中等 | 快 |
| **大小** | ~800KB | ~20MB |
| **依賴** | 無 | Chromium |
| **WASM** | 原生 JS | 需要 |

---

## 版本

| 版本 | 日期 | 變更 |
|------|------|------|
| v1.0 | 2026-07-13 | 初版（基於 PyMuPDF/PDF.js/PDFium 資源）|