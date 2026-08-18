# Hermes Constitution v2.0 — Graph Baseline v1.0

> 版本：Hermes Constitution v2.0 (CBHE + Graph-Aware)
> 基準：Graph Baseline v1.0
> 日期：2026-07-15
> 圖譜 commit：`912986c2`
> 工具：Graphify v0.9.16 + DeepSeek-v4-flash

---

## 一、圖譜 Zero-Point 基線

### 全域指標

| 指標 | Zero-Point 值 | 備註 |
|:---|:---:|:---|
| **總節點** | 1,648 | |
| **總邊緣** | 2,666 | |
| **總社區** | 126 | Louvain community detection |
| **Graph Density** | — | 待計算 |
| **B (wenmou) 出度** | 15 | 僅內部函數，**無跨角色輸出** |
| **b_role 節點出度** | 0 | 純文檔標記，無功能連接 |
| **E-code 節點出度** | 0 | 全部葉節點，純狀態標記 |
| **Super-node 數量（出度 > 20）** | 10 | |
| **PDF Auditor SV 出度** | 36 | 零消費者（in=0） |
| **Google Workspace API 出度** | 39 | 零消費者（in=0） |

### 10 大超級節點（出度 > 20）

| 節點 | 出度 | 入度 | 性質 |
|:---|:---:|:---:|:---|
| `red_teaming_godmode_scripts_parseltongue` | 41 | 0 | 純 producer |
| `productivity_google_workspace_scripts_google_api` | 39 | 0 | 純 producer |
| `pdf_edit_references_auditor_supervisor_verify` | 36 | 0 | 純 producer |
| `creative_comfyui_scripts_common` | 28 | 11 | 雙向連接 |
| `pdf_edit_references_auditor_supervisor_verify_audit` | 28 | 2 | 雙向 |
| `productivity_maps_scripts_maps_client` | 26 | 0 | 純 producer |
| `productivity_google_workspace_scripts_google_api_main` | 24 | 1 | 雙向 |
| `hermes_ctl` | 22 | 1 | **唯一有實際系統角色的節點** |
| `gen_gbrain_tutorial` | 21 | 0 | 純 producer |
| `pdf_design_spec_v1_0_0_gen` | 21 | 0 | 純 producer |

### Phase 覆蓋率

| Phase | 節點數 | 總 degree | 備註 |
|:---|:---:|:---:|:---|
| `PHASE_COMFY` | 355 | 1,366 | 最大子系統，實際已存在 |
| `PHASE_PDF` | 253 | 865 | 已結構化 |
| `PHASE_RESEARCH` | 42 | 134 | 已存在 |
| `PHASE_SYSTEM` | 33 | 67 | 覆蓋 cron/scripts |
| `PHASE_EVAL` | 1 | 1 | 極少節點 |

---

## 二、關鍵發現（御史 zero-point）

### 發現 1：wenmou (B Planner) 完全隔離

```
wenmou 輸出 15 條邊，全部指向 wenmou 內部函數：
  wenmou --> wenmou_analyze_strategy
  wenmou --> wenmou_check_alignment
  wenmou --> wenmou_check_lock
  wenmou --> wenmou_generate_plan
  ...（共15個內部目標）

wenmou 輸出 0 條邊指向 H、C、E 或其他角色節點。
b_role（概念角色標記）出度 = 0。
```

**含義：** `C→B→H→E→C` 流程在圖上只完成了第一步（C→B），B 之後的輸出沒有進入任何可追蹤的拓撲。

**v2 行動目標：** `deg(wenmou → [H,C,E]) ≥ 1`

---

### 發現 2：超級節點全部是純 Producer（無消費者）

10 個超級節點中，8 個 in=0。

這意味著：
- `parseltongue`（出度41）：輸出從未被圖中任何節點消費
- `google_api`（出度39）：API 呼叫結果從未被驗證
- `auditor_supervisor_verify`（出度36）：審計結果從未被任何人引用

**含義：** 這不是「超級節點」，這是「啞巴電線」——有能力，但輸出是懸在半空中的。

**v2 行動目標：** 每個出度 > 20 的節點，必須有至少 1 個 in-edge（消費者）。

---

### 發現 3：E-code 節點全部是葉節點

所有 `e_code_*` 節點：out=0。

這是**正確的**——E-code 是狀態標記，不是處理節點。這個狀態在 graph topology 層面是乾淨的。

**備註：** 圖譜中新 E-codes（`E-B-PLAN-UNREFERENCED` 等）尚未出現在圖中（因為是新規則，尚未被引用）。

---

### 發現 4：hermes_ctl 是唯一有實質系統角色的節點

`hermes_ctl`（出度22，入度1）：
- 唯一同時有「系統控制角色」和「被其他節點依賴」的節點
- 輸出覆蓋：版本檢查、PDF 結構檢查、distill、doctor

這是圖譜中**最接近 C (Master/Console) 概念實體**的節點。

**含義：** CBHE 架構中，C 的實體是 `hermes_ctl`，這與 SOUL/AGENTS 中「控制台唯一入口」的定義一致。

---

### 發現 5：Google Workspace 是啞巴電線的最典型案例

`productivity_google_workspace_scripts_google_api`（出度39，入度0）：
- 39 個 Google API 輸出函數
- 0 個消費者

**含義：** 每次執行 Gmail/Calendar/Docs API，輸出從未被圖譜追蹤。如果要滿足 `EXTERNAL-WRITE-AUDIT` 規則，這 39 個函數的輸出必須進入可追蹤的 graph edge。

**v2 行動目標：** 零啞巴電線——每個外部 API 輸出都必須有對應的驗證邊。

---

## 三、版本標記

```
Hermes Constitution v2.0 (CBHE + Graph-Aware)
Graph Baseline v1.0
Zero-Point Date: 2026-07-15
Graph Commit: 912986c2

Nodes: 1648 | Edges: 2666 | Communities: 126
B Connectivity: 0 (b_role out-deg=0, wenmou→[H,C,E]=0)
E-code Topology: CLEAN (all e_code_* are leaf nodes)
C实體: hermes_ctl (out=22, in=1) ✓
哑巴电线: 8/10 super-nodes have zero consumers
```

---

## 四、滾動目標（相對於 v1.0）

| 指標 | v1.0 基線 | v2.0 目標 |
|:---|:---:|:---:|
| `deg(wenmou → [H,C,E])` | 0 | ≥ 1 |
| Super-node 啞巴電線數 | 8 | ≤ 3 |
| `deg(b_role)` | 0 | ≥ 1 |
| `deg(hermes_ctl)` | 22 | ≥ 25 |
| PDF Auditor 有消費者 | 0 | ≥ 1 |
| Google Workspace 有驗證邊 | 0 | ≥ 1 |

---

## 五、附屬 artefact

| 檔案 | 說明 |
|:---|:---|
| `hermes-full-system-graph.html` | D3.js 全系統視覺化（可互動） |
| `hermes-core-files-graph.html` | 核心檔局部放大視覺化 |
| `hermes-full-system-knowledge-graph.md` | 語義層總覽與分析 |
| `hermes-constitution-v2-baseline.md` | 本文件，版本標記與 zero-point |
