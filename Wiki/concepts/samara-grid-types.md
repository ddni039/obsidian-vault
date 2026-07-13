# Samara Grid Types — 四類編排網格

> 來源：*Making and Breaking the Grid* Ch.2，Timothy Samara（Rockport 2002/2023 3rd ed.）
> 免費章節摘要：https://www.bookey.app/book/making-and-breaking-the-grid
> 研究日期：2026-07-13

---

## 核心命題

Samara 將編排網格分為四大類：**Manuscript / Modular / Hierarchical / Radial**。掌握每類的「何時用 / 何時破」是 PDF 多欄佈局的基礎。

---

## 1. Manuscript Grid（手稿網格）

最傳統的單欄網格，常見於書籍、長篇文章。

### 結構
- 單一文字欄，寬度固定
- 左右留白均勻
- 行高（leading）決定縱向節奏

### 適用場景
PDF 報告內頁（論述型文字）
技術白皮書（純文字內容）
文學/書籍排版

### 破格信號
當需要插入側邊欄（sidebar）、圖表或 pull quote 時，Manuscript Grid 無法承載 → 升級到 Modular

---

## 2. Modular Grid（模組網格）

由縱列（columns）和橫列（rows）同時分割版面，形成「區塊矩陣」。

### 結構
- 欄數通常 3 / 4 / 6 / 9 / 12
- gutter（欄距）固定
- 每個交點 = 一個模組單元

### 欄數與用途對照（Samara 經驗值）

| 欄數 | 適用場景 | 說明 |
|------|---------|------|
| 3 | 簡報式雙語對照 | 左右文字 + 中心強調 |
| 4 | 商業報告內頁 | 圖文混排，經典型 |
| 6 | 雜誌/型錄 | 圖像密集，需多欄佈局 |
| 9 | 研究論文 | 3x3 可做層次分組 |
| 12 | 複雜儀表板 | 最高彈性，欄寬顆粒最小 |

### 黃金法則
**欄數越多 → 彈性越大 → gutter 必須足夠寬（≥0.5x 正文字大小）**
TRAP：gutter 太窄會讓跨欄元素黏在一起。

### ReportLab PLATYPUS 實作

```python
from reportlab.platypus import Frame, PageTemplate, BaseDocTemplate

# 三欄版（6 欄網格：左1右2合併=寬欄 / 中3=窄欄 / 右4右5合併=寬欄）
col_widths = [150, 150, 80, 150, 150, 80]
# 或者用百分比：
# PAGE_W = 595pt（A4），margin = 50pt
# content_w = 495pt，3欄等寬 = (495 - 2*10) / 3 ≈ 158pt
```

---

## 3. Hierarchical Grid（層次網格）

不同於 Modular 的「均勻矩陣」，Hierarchical 網格的欄寬和列高**根據內容重要性變化**。

### 結構特徵
- 主要欄（primary column）佔 50-60% 寬度
- 次要欄（secondary）佔 25-30%
- 輔助欄（tertiary）佔 10-15%
- 欄數不對稱：常見 2+1（左大右小）、3+1、1+2+1

### 適用場景
PDF 研究報告（摘要 + 正文 + 附錄）
商業提案（標題區 + 內容 + 側邊備註）
新聞通訊（主文 + 側邊引言）

### 與 Modular 的關鍵差異
| | Modular | Hierarchical |
|--|---------|--------------|
| 欄寬 | 全部相同 | 根據內容層次變化 |
| 適用 | 圖文均衡 | 文字導向，層次分明 |
| 破格難度 | 中等 | 高（需要先理解層次邏輯） |

---

## 4. Radial Grid（輻射網格）

從中央核心向外輻射，適合海報、資訊圖、視覺 Identity 系統。

### PDF 應用場景
- 視覺化信息圖（infographic）
- 目錄/手冊的封面佈局
- 圓形圖表包裝

### PDF 實作注意
Radial 佈局**不適合 PLATYPUS 處理**（PLATYPUS 專為直交矩形設計）。需要：
- ReportLab Canvas 直接繪製（`canvas.saveState()` / `canvas.restoreState()` 搭配 `rotate()`）
- 或用 SVG 轉 PDF（`svglib + reportlab.graphics`）

---

## 破格原則（Samara Ch.4）

「懂規則才能破規則」—— 破格不是隨機，是刻意。

### 破格技法清單

| 技法 | 說明 | PDF 適用性 |
|------|------|----------|
| **Asymmetry（不對稱）** | 故意不對齊，打破視覺均衡 | ✅ 直接適用 |
| **Overlap（重疊）** | 讓一個元素跨過欄邊界或進入 gutter | ⚠️ 需要精確座標計算 |
| **Scale Disruption（尺度破壞）** | 某元素刻意比網格大 1.5x 或 2x | ✅ 標題/引言適用 |
| **Rotation（旋轉）** | 非 0°/90° 放置元素 | ⚠️ 需要 Canvas 底層 |
| **Organic Shape（有機形狀）** | 圓形/曲線 vs 網格的矩形衝突 | ⚠️ SVG 轉換 |

---

## 與 Elam 3x3 網格的對應

Samara 的 4 類網格，Elam 的 3x3 網格（Law of Thirds）是**最小顆粒度的模組參考**：

```
┌─────┬─────┬─────┐
│  TL │  TC │  TR │  ← 三分法四焦點
│  ML │  MC │  MR │  ← PDF 欄距要塞在
│  BL │  BC │  BR │  ← gutter 位置而非疊加
└─────┴─────┴─────┘
```

**PDF 多欄應用**：
- 雙欄版：左欄 = 左1+左2，右欄 = 右1+右2
- 三欄版：各佔一個 column
- gutter 對齊三分線時視覺效果最佳（Elam 驗證）

---

## 與 pdf-design-spec 的整合

### 雙欄模板座標（SPEC-GEO 補充）

```python
# A4 雙欄版（PointDPI 系統，72dpi）
PAGE_W, PAGE_H = 595, 842
MARGIN = 50
GUTTER = 12  # pt

content_w = PAGE_W - 2 * MARGIN  # = 495
col_w = (content_w - GUTTER) / 2  # = 241.5pt ≈ 241pt

# 左欄 Frame
left_frame = Frame(
    MARGIN, MARGIN,
    col_w, PAGE_H - 2*MARGIN,
    leftPadding=0, rightPadding=0,
    topPadding=0, bottomPadding=0
)

# 右欄 Frame
right_frame = Frame(
    MARGIN + col_w + GUTTER, MARGIN,
    col_w, PAGE_H - 2*MARGIN,
    leftPadding=0, rightPadding=0,
    topPadding=0, bottomPadding=0
)
```

### 側邊欄（Sidebar）模式

```
┌──────────────────┬──────┬──────────────┐
│                  │ Side │              │
│   主欄（2/3寬）  │ bar  │  次欄（1/3）  │
│                  │ 1/3  │              │
└──────────────────┴──────┴──────────────┘
```

---

## 相關 wiki 頁面

- [[elam-grid-systems]] — 比例、分組、負空間、三分法
- [[muller-brockmann-grid-systems]] — 經典 8-32 格系統
- [[pdf-coordinate-layout-algorithms]] — Grid 佈局公式
- [[reportlab-platypus-multi-column]] — PLATYPUS 多欄實作（待建）
