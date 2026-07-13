---
uid: 20260713-pdf-tagged-structure
name: Tagged PDF 語義結構
aka: [tagged PDF, structure tree, StructTreeRoot, logical structure, reading order, PDF tags]
type: concept
tags: [PDF, tagged PDF, structure tree, StructTreeRoot, reading order, PDF/UA, semantics, artifacts]
related_entities:
  - entities/matterhorn-protocol.md
  - entities/verapdf-validator.md
related_concepts:
  - concepts/pdf-ua-standard.md
  - concepts/pdf-quality-gate-framework.md
trigger: |
  tagged PDF, 標籤樹, 結構樹, 閱讀順序, StructTreeRoot, H1 H2 H3, 標題層次,
  PDF/UA, Artifacts, 裝飾性元素, 列表結構, 表格結構, 邏輯結構, 內容順序
source: |
  PDF Association Tagged PDF 資源：https://www.pdfa.org/tagged-pdf-related-projects/
  QualiBooth PDF Accessibility Guide：https://www.qualibooth.com/resources/pdf-accessibility-guide/
  Nutrient PDF/UA 完全指南：https://www.nutrient.io/blog/what-is-pdf-ua/
---

# Tagged PDF 語義結構

## 定義

Tagged PDF 是普通 PDF 添加了一個隱藏的**結構樹（Structure Tree）**——在視覺呈現之外，額外記錄每個內容片段的語義角色，使螢幕閱讀器、放大鏡等輔助技術能可靠解讀文檔。

```
普通 PDF：標記叢集（marks on a page）
Tagged PDF：標記叢集 + 結構樹（marks + meaning）
```

## 結構樹（StructTreeRoot）

PDF 文件的結構樹是一個樹狀層次結構，根節點為 `StructTreeRoot`，每個節點稱為 **Structure Element**（結構元素）。

### 標準結構標籤

| 標籤 | 語義 | 說明 |
|------|------|------|
| `<Document>` | 文檔根 | 結構樹根 |
| `<Part>` | 部分 | 大章節 |
| `<Artwork>` | 插圖 | 裝飾性藝術 |
| `<Sect>` | 章節 | 分組容器 |
| `<Div>` | 分組 | 無語義的通用分組 |
| `<H1>`–`<H6>` | 標題層次 | 1-6 級標題 |
| `<P>` | 段落 | 普通段落文本 |
| `<L>` | 列表 | 列表容器 |
| `<LI>` | 列表項 | 列表內的條目 |
| `<Lbl>` | 列表標籤 | 序號/項目符號 |
| `<LBody>` | 列表內容 | 列表項主體文本 |
| `<Table>` | 表格 | 表格容器 |
| `<TR>` | 表格行 | 行 |
| `<TH>` | 表格標題格 | 表頭（role="columnheader" 或 "rowheader"）|
| `<TD>` | 表格數據格 | 數據單元 |
| `<THead>` | 表頭區域 | 表頭行分組 |
| `<TBody>` | 表體區域 | 數據行分組 |
| `<Figure>` | 圖片 | 含 Alt text |
| `<Formula>` | 公式 | 數學公式 |
| `<Code>` | 代碼 | 程式碼塊 |
| `<Quote>` | 引用 | 引用文本 |
| `<Note>` | 註釋 | 腳註/尾註 |
| `<Reference>` | 引用 | 交叉引用 |
| `<BibEntry>` | 書目條目 | 參考文獻 |
| `<Figure>` | 圖形 | 含 Alt text |
| `<Link>` | 連結 | 超連結 |
| `<Annot>` | 註釋 | PDF 註釋 |

## 閱讀順序

**標籤定義"這是什麼"，閱讀順序定義"先讀什麼"。**

在單欄文檔中，視覺順序 = 邏輯順序。在複雜佈局中（雙欄、側邊欄、插圖包圍文字），兩者經常分歧。

正確的閱讀順序：標題 → 段落 → 側邊欄（標題之後、下一段落之前）→ 段落 → 插圖說明（插圖之後）

**常見錯誤**：
- 雙欄文檔，螢幕閱讀器從左上到右下逐行讀，導致「左欄第一段 → 右欄第一段 → 左欄第二段」
- 插圖說明在插圖之前讀出
- 頁腳/頁眉被當作正文讀出

## Artifacts（裝飾性元素）

Tagged PDF 可以將純裝飾性元素（背景、分隔線、頁碼裝飾）標記為 **Artifact**，使輔助技術跳過它們。

```
/Artifact
/Type /Pagination       ← 分頁相關裝飾（頁眉、頁腳、頁碼）
  /Type /Layout         ← 版面裝飾（分隔線、背景圖案）
  /Type /Page           ← 頁面級裝飾
```

ReporterLab 中實現：`from reportlab.pdfbase.pdfform import PDFAttributes` 或直接用 `canvas.doForm()` 配合 `/MCID` 映射。

## pikepdf 讀取結構樹

```python
import pikepdf

with pikepdf.open('document.pdf') as pdf:
    for page in pdf.pages:
        struct_tree = page.get('/StructTreeRoot')
        if struct_tree:
            # 遍歷結構樹
            def walk(node, depth=0):
                if isinstance(node, pikepdf.objects.Dictionary):
                    t = node.get('/Type')
                    s = node.get('/S')
                    print('  ' * depth + f'{t} / {s}')
                    for kid in node.get('/K', []):
                        walk(kid, depth+1)
            walk(struct_tree)
```

## 常見失敗模式

| 問題 | 描述 | PDF/UA 失敗條件 |
|------|------|----------------|
| 標題跳級 | H1 → H3（跳過 H2）| Matterhorn 7-002 |
| 偽裝標題 | 用大號粗體 `<P>` 而非 `<H*>` | Matterhorn 7-003 |
| 偽裝列表 | 用 `•` 字符的 `<P>` 而非 `<L>/<LI>` | Matterhorn 7-004 |
| 空 Alt text | `/Alt ""` 或完全缺失 | Matterhorn 10-001 |
| 閱讀順序錯誤 | 標籤順序與邏輯順序不一致 | Matterhorn 6-001 |
| 表格缺表頭 | 全部 `<TD>` 無 `<TH>` | Matterhorn 12-001 |

## Hermes 對接

`pdf-edit` TRAP-TRAP 已記錄：
- TRAP-TAG-1：H1→H3 跳躍
- TRAP-TAG-2：圖片無 Alt text
- TRAP-TAG-3：表格無表頭
- TRAP-TAG-4：ReportLab 免費版 tagged 功能有限

