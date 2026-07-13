---
title: PDF PLATYPUS Page Layout Architecture
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [concept, platypus, reportlab, pdfgen, flowable, document-template, frame, table-style, pdf-architecture, generator-renderer-separation, hermes-pdf-production, layer-1]
sources:
  - raw/articles/pdf-production-bible-2026-07-13.md
confidence: high
---

# PDF PLATYPUS Page Layout Architecture

## 定義

**PLATYPUS**（Page Layout And Typography Using Scripts）= ReportLab 的高階頁面佈局系統
官方全稱：*"Page Layout And Typography Using Scripts"*

對立於低階 `pdfgen`（直接操 Canvas），PLATYPUS 提供 Flowable 抽象，讓 PDF 生成更聲明式、更易維護。

## 為何需要 PLATYPUS

| 低階 pdfgen | PLATYPUS |
|------------|----------|
| 手動管理座標 | 自動佈局流動 |
| 硬編碼位置 | Flowable 抽象 |
| 難處理分頁 | 自動分頁 |
| 難統一樣式 | StyleSheet 統一 |
| 內容與呈現耦合 | 內容與呈現分離 |

## 兩層架構

```
User Content (Python data structures)
    ↓
PLATYPUS Flowables
    ├─ Paragraph
    ├─ Table
    ├─ Image
    ├─ Spacer
    └─ ... (25+ flowables)
    ↓
pdfgen Canvas API
    ↓
PDF File
```

## 5 大核心 Flowable

| Flowable | 用途 | 關鍵參數 |
|----------|------|---------|
| `Paragraph` | 文字段落 | `text`, `style` |
| `Table` | 表格 | `data`, `style` |
| `Image` | 圖片 | `filename`, `width`, `height` |
| `Spacer` | 空白 | `width`, `height` |
| `PageBreak` | 換頁 | — |

## 4 大 Flowable 進階

| Flowable | 用途 | 使用時機 |
|----------|------|---------|
| `CondPageBreak` | 條件換頁 | 避免孤立的表頭 |
| `KeepTogether` | 保持群組 | 標題和首段不分離 |
| `TableOfContents` | 目錄 | 自動生成目錄 |
| `SimpleIndex` | 索引 | 自動生成索引 |

## Document Template 架構

```python
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame

class MyDocument(BaseDocTemplate):
    def __init__(self, filename, **kwargs):
        BaseDocTemplate.__init__(self, filename, **kwargs)
        
        # Frame = 頁面內的內容區域
        frame = Frame(
            x1=leftMargin,
            y1=bottomMargin,
            width=width,
            height=height,
            id='main'
        )
        
        # PageTemplate = 頁面配置（可有多個：首頁/內頁/空白頁）
        self.addPageTemplates([
            PageTemplate(id='Main', frames=[frame], onPage=self.header_footer)
        ])
    
    def header_footer(self, canvas, doc):
        canvas.saveState()
        # 頁眉
        canvas.setFont('Helvetica', 9)
        canvas.drawString(72, 780, "Header Text")
        # 頁腳
        canvas.drawRightString(523, 30, f"Page {doc.page}")
        canvas.restoreState()
```

## Generator-Renderer 分離模式

**這是避免邏輯錯誤的核心模式（來源：StackExchange Kilian Foth）**

```
┌─────────────────────────────────────────┐
│  Generator（內容生成器）                 │
│  - 決定「印什麼內容」                   │
│  - 決定「按什麼順序」                   │
│  - 不關心 PDF/HTML/Text                 │
└──────────────────┬──────────────────────┘
                   │ Flowable[]
                   ▼
┌─────────────────────────────────────────┐
│  Renderer（渲染器）                      │
│  - PDFRenderer: Canvas 操作              │
│  - HTMLRenderer: HTML 標記              │
│  - TextRenderer: 純文字                 │
└─────────────────────────────────────────┘
```

**好處**：
- 報告內容變了 → 只改 Generator
- 樣式要求變了 → 只改 Renderer
- 需要新輸出格式 → 只加新的 Renderer

## Programming Flowables（邏輯控制）

```python
from reportlab.platypus import DocAssign, DocExec, DocIf, DocWhile, DocAssert

# DocAssert = 防止邏輯矛盾的斷言
DocAssert(condition='len(items) > 0',
          format="Table must have at least 1 row")

# DocIf = 條件內容
DocIf("x > 5",
      [Paragraph("x > 5", styles['Normal'])],
      [Paragraph("x <= 5", styles['Normal'])])

# DocWhile = 迴圈
DocWhile("i < 10",
         [DocExec("i = i + 1"),
          Paragraph("i = %(i)d" % locals(), styles['Normal'])])
```

## TableStyle 5 大常見錯誤

| 錯誤 | 正確 |
|------|------|
| `(0,0), (0,0)` 只覆蓋一格 | `(-1,0)` = 整行 |
| 不宣告 SPAN | `('SPAN', (0,0), (1,1))` |
| 全表同一字體大小 | 表頭用 `FONTNAME='Helvetica-Bold', FONTSIZE=14` |
| 不設定交替行顏色 | `('ROWBACKGROUNDS', (0,0), (-1,-1), [colors.white, colors.lightgrey])` |
| 硬編碼顏色 | 用顏色變數 |

## Hermes PDF 架構改進

```
Layer 1: pdf-design-spec (技法規範 SSOT)
  └─ SPEC-CLR/FNT/GEO 集中定義

Layer 2: pdf Skill (PLATYPUS + Generator-Renderer)
  └─ 統一 StyleSheet
  └─ Document Template
  └─ Programming Flowables

Layer 3: pdf-edit / chinese-pdf-gen (應用)
  └─ 依賴 Layer 1 + Layer 2
  └─ 不內聯 SPEC 值
```

## 版本

| 版本 | 日期 | 變更 |
|------|------|------|
| v1.0 | 2026-07-13 | 初版（基於 ReportLab v5.0.0 官方文檔 + StackExchange）|