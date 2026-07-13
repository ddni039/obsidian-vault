# Wilke Figure Design — 圖表平衡與標題實踐

> 來源：*Fundamentals of Data Visualization* Ch.22 + Ch.23，Claus O. Wilke（O'Reilly 2019）
> 全書免費在線：https://clauswilke.com/dataviz/
> 研究日期：2026-07-13

---

## 一、標題與圖說（Ch.22 標題、圖說與表格）

### 核心原則：圖表不是藝術品，是資訊載體

> *"A data visualization is not a piece of art meant to be looked at only for its aesthetically pleasing features. Instead, its purpose is to convey information and make a point."* — Wilke

### 圖表標題的兩種放置方式

| 放置位置 | 適用場景 | PDF 應用 |
|---------|---------|---------|
| **嵌入圖表內（Infographic 樣式）** | 社群媒體、獨立海報、無伴隨說明 | PPT 轉 PDF、獨立資訊圖 |
| **置於圖說區塊第一行（Caption 樣式）** | 書籍、學術論文、正式商業文件 | **ReportLab PLATYPUS 預設** |

**ReportLab PLATYPUS 實踐**：
```python
# 正確：標題作為 caption 開頭，非獨立疊加在圖表上
 caption_text = "Corruption and human development: "
              "The most developed countries experience the least corruption."
# 錯誤：把標題繪製在 Drawing 內部（破壞了文圖分離原則）
```

### 標題寫作紀律

**錯誤示範**：
```
❌ "This figure shows how corruption is related to human development."
```

**正確示範**：
```
✅ "Corruption and human development."
✅ "The most developed countries are the least corrupt."
```

- 標題是**陳述句**（assertion），不是描述句
- 標題無需完整句子
- 標題是圖表的第一個聲音，必須直接表達核心發現

### 軸標題與圖例標題

| 元素 | 必要條件 |
|------|---------|
| 軸標題 | **必須標明單位**（如 "Body mass (grams)" 而非 "Body mass"） |
| 數值變數 | 全部需要單位 |
| 類別變數 | 不需要單位（如 "sex: female/male"） |
| 自解釋標籤 | 可省略標題（如 "2013, 2014, 2015" 已是年份標籤） |

### 表格設計（ReportLab TableStyle 直接相關）

**糟糕的表格設計（Fig 22.7a/b）**：
- ❌ 垂直分隔線
- ❌ 數據行之間隔線
- ❌ 居中數據列
- ❌ 深淺行交替過於強烈

**正確的表格設計（Fig 22.7c/d）**：
- ✅ 無垂直線
- ✅ 僅表頭底線（0.5pt）
- ✅ 數字右對齊 / 文字左對齊
- ✅ 表頭深色背景 + 淺色字（`TableStyle` header 區塊）
- ✅ 交替行時用**極淡灰**（`Color(0.95, 0.95, 0.95)`）而非深色

**ReportLab TableStyle 對應實作**：
```python
ts = TableStyle([
    # 表頭
    ('BACKGROUND', (0,0), (-1,0), Color(0.2, 0.2, 0.4)),  # 深藍灰
    ('TEXTCOLOR',  (0,0), (-1,0), Color(1,1,1)),            # 白字
    ('ALIGN',      (0,0), (-1,0), 'CENTER'),
    # 數據列：無垂直線
    ('VALIGN',     (0,1), (-1,-1), 'MIDDLE'),
    ('ALIGN',      (0,1), (0,-1), 'LEFT'),                  # 文字左對齊
    ('ALIGN',      (1,1), (-1,-1), 'RIGHT'),                # 數字右對齊
    # 交替行（淺灰）
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [Color(1,1,1), Color(0.97,0.97,0.97)]),
    # 僅表頭底線
    ('LINEBELOW',  (0,0), (-1,0), 0.5, Color(0.5,0.5,0.5)),
])
```

### 圖說 vs 表格標題位置
- **圖說**：置於**下方**（讀者先看圖、再讀說明）
- **表格標題**：置於**上方**（讀者從上往下閱讀，如同正文）

---

## 二、數據墨水與背景平衡（Ch.23）

### Tufte Data-Ink Ratio 的 Wilke 修正

| 立場 | 人物 | 觀點 |
|------|------|------|
| 極端 minimalist | Tufte（在 Ch.23 被批評）| 移除所有 non-data ink |
| **Wilke 中道** | 本章 | "within reason"：適當非數據元素是必要的 |
| 極端裝飾 | 大多數商業圖表 | 太多 frame/grid/3D效果 |

### 適量的重要性：背景格線的價值

**背景格線的兩個功能**（Fig 23.2 示範）：
1. **錨定數據點**：點不漂浮在空白中，有明確空間參照
2. **區隔圖例與繪圖區**：視覺邊界

### 三個極端與正確地帶

```
極端過多                    適量地帶                    極端過少
═══════════════            ════════════════            ════════════
- Frame 包圍整圖            - 開放格線                   - 軸標籤太淡
- Frame 包圍繪圖區          - 淺灰主格線                 - 數據點漂浮
- Frame 包圍圖例            - 中間對齊                   - 圖例點被誤認為數據
- 密集背景網格             - 無frame 或輕frame           - 無格線
（Fig 23.1）                                          （Fig 23.3）
```

### 小多倍（Small Multiples）背景設計

**問題（Fig 23.5）**：每面無框架、柱無基準線 → 像現代藝術

**正確做法（Fig 23.6）**：
- 淺灰背景（每 facet 相同）
- 極淡水平格線（統一 Y軸 範圍）
- facet 間無需明確邊界（共享軸刻度隱含邊界）

### ReportLab PLATYPUS 實踐：圖表周圍格線

```python
# Fig 23.2 等效：開放格線，白色背景
d = Drawing(width, height)
# 主格線（淺灰 0.5pt）
grid_color = Color(0.85, 0.85, 0.85)
# Y軸格線（每主要刻度）
for y in range(0, 100, 10):
    y_pos = y * height / 100
    d.add(Line(0, y_pos, width, y_pos, strokeColor=grid_color, strokeWidth=0.5))
# X軸格線（極淡）
minor_grid = Color(0.93, 0.93, 0.93)
# 數據線（主要顏色，不被格線喧賓奪主）
d.add(PolyLine(x_data, y_data, strokeColor=Color(0.12, 0.12, 0.44), strokeWidth=1.5))
```

---

## 三、Wilke 對 Tufte 的關鍵修正

| Tufte 原文（過度極簡） | Wilke 修正 |
|----------------------|-----------|
| 「最大化 data-ink ratio」 | 「within reason」——非數據墨水承載結構功能 |
| 「移除所有 frame」 | 「可選：frame 幫助區隔圖例與繪圖區」 |
| 「軸線不必要」 | 「軸線提供空間參照，促進閱讀」 |
| 「格線是 chartjunk」 | 「淺灰主格線是有用背景，不是干擾」 |

---

## 四、與現有 PDF 技法約束的整合

### 圖表核查清單（Wilke + Tufte 整合版）

```
交付前核查：
□ 標題是 assertion 而非 description
□ 標題位於 caption 第一行（PLATYPUS flowable caption）
□ 軸標題包含單位
□ 數字軸使用右對齊
□ 格線：主格線 0.5pt 淺灰，副格線 0.25pt 極淡
□ 無垂直分隔線（表格）
□ 表頭底線 0.5pt
□ 交替行使用 Color(0.97,0.97,0.97)
□ 小多倍 facets Y軸範圍一致
□ 強調色不與基線顏色競爭（GrayLine 廢除原則）
□ 色盲安全：類別標籤使用 Okabe-Ito 而非 ColorBrewer Set1
□ 無 3D 效果
□ 無 粗黑 frame 包圍整圖
□ 圖例點有足夠視覺距離，不被誤認為數據點
□ 圖例與繪圖區有明確邊界（或留白分隔）
```

---

## 參考文獻
- Wilke, C. O. (2019). *Fundamentals of Data Visualization*, Ch.22+23. O'Reilly.
  - Ch.22 在線：https://clauswilke.com/dataviz/figure-titles-captions.html
  - Ch.23 在線：https://clauswilke.com/dataviz/balance-data-context.html
