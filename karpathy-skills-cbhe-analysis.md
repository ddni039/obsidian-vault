# karpathy-skills: CBHE 映射研究

## 源頭
- **Repo**: [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) (194k stars, 19.9k forks)
- ** Fork 自**: Andrej Karpathy [原始推文](https://x.com/karpathy/status/2015883857489522876)
- **攝入日期**: 2026-07-18
- **原始檔案**: CLAUDE.md, EXAMPLES.md

---

## 核心內容：四原則

| 原則 | 核心主張 | 對應 CBHE 角色 |
|---|---|---|
| **Think Before Coding** | 不假設、不隐藏困惑、主動呈現取捨 | C（路由評估）+ B（規劃） |
| **Simplicity First** | 最小代碼解決當下問題，拒絕 speculative complexity | H（工匠執行） |
| **Surgical Changes** | 只動該動的，不做 drive-by refactoring | H（領域守門）|
| **Goal-Driven Execution** | 將任務轉為可驗證目標，loop 直到確認 | E（御史核查）|

---

## 與 CBHE 的對應分析

### 1. Think Before Coding ↔ C + B 層

Karpathy 指出：
> "The models make wrong assumptions on your behalf and just run along with them without checking. They don't manage their confusion, don't seek clarifications."

這正是 C-ROUTING-CHECK 要處理的場景。C 在 routing 前必須：
- 列出假設（assumptions）
- 若有多種解釋，呈現後讓用戶選擇
- 遇到不清楚時，`workflow_mode` 應該是 `sequential`（不可並行）

**CBHE 缺口**：目前 C-ROUTING-CHECK 專注於「複雜度矩陣」，但沒有要求 C 主動列舉假設清單。

**建議更新**：`C-ROUTING-ENTRY` 或 `C-ROUTING-CHECK` 加入：
```
C 在 routing 時若偵測到 ambiguity，應輸出：
  - list_of_assumptions: [...]
  - ambiguity_flag: true/false
```
相當於 Karpathy 的 "Surface tradeoffs" 原則。

### 2. Simplicity First ↔ H 層

Karpathy 指出：
> "They really like to overcomplicate code and APIs, bloat abstractions... implement a bloated construction over 1000 lines when 100 would do."

H（工匠）的核心紀律：
- 收到 B 的 plan + NFR 後，只實作 plan 範圍內的最小代碼
- 杜絕 speculative features（"add later if needed"）

**CBHE 缺口**：
- `H-DOMAIN` 有 `h_no_speculative_code` 約束，但從未出現在 TRAP 列表
- 沒有 TRAP 對應「over-abstraction / speculative features」

**建議更新**：`sop-design-maintenance-errors` 新增 TRAP：
```
KARPATHY-OVER-ABSTRACT-001
  Condition: 新增 class/interface/abstract 層級，但使用處只有 1 處
  Fix: 收斂成普通函式，直到出現第 2 個使用處
```

### 3. Surgical Changes ↔ H 層（進階）

Karpathy 指出：
> "They still sometimes change/remove comments and code they don't sufficiently understand as side effects, even if orthogonal to the task."

這與 CBHE `H-DOMAIN` 的 `h_surgical_edits` 完全對齊：
```
H-DOMAIN 約束：
  h_surgical_edits: 只改與用戶請求直接相關的代碼
  h_drive_by_forbidden: 嚴禁 drive-by refactoring（改不相關的格式、注釋、import）
```

**CBHE 缺口**：
- `h_drive_by_forbidden` 沒有 TRAP 對應
- 也沒有對應的 E-code（如 `E-H-DRIVE-BY`）

**建議更新**：`H-DOMAIN` 新增 E-code：
```
E-H-DRIVE-BY
  Condition: PR diff 中，出現非用戶請求範圍內的變更（格式化、注釋、dead code 刪除）
  Action: 阻斷交付，要求 H 重做 surgical scope
```

### 4. Goal-Driven Execution ↔ E 層

Karpathy 指出：
> "Goal-Driven Execution" — transform imperative instructions into declarative goals with verification loops.

CBHE E（御史）的核心職責：
- 接收 H 的實作，核查是否與 B 的 NFR 匹配
- 使用 B 的「可驗收標準」作為布林 gate

**CBHE 缺口**：
- 目前 `E-PDF-DELIVERY-GATE` 只有 6 項，都是 PDF-specific
- 沒有通用的「Goal-Driven Execution」E-gate 清單

**建議更新**：在 RULES 新增 `E-GOAL-DRIVEN-GATE`（通用 E-gate）：
```
E-GOAL-DRIVEN-GATE
  所有交付必須滿足：
    1. success_criteria_defined: B 的 NFR 中有明確可測量標準
    2. test_reproducible: 關鍵行為有可重複驗證的測試
    3. no_regression: 現有測試全部綠燈
    4. scope_respected: diff 中無超出用戶請求的變更
```

---

## Anti-Pattern 與現有 TRAP 的映射

| karpathy anti-pattern | 現有 CBHE TRAP | 狀態 |
|---|---|---|
| Hidden assumption → wrong implementation | （無完全對應 TRAP） | 待新增 |
| Over-abstraction (Strategy for single use) | `PDF-PT-DOUBLE-WRAP-001`（部分重疊：過度包裝） | 已有 |
| Drive-by refactoring | `E-H-DRIVE-BY` | **待新增** |
| Vague goal (no verification) | `E-PIPELINE-BYPASS`（部分對應） | 部分覆蓋 |
| Speculative features | `KARPATHY-OVER-ABSTRACT-001` | **待新增** |
| No clarification asked | `C-ROUTING-CHECK` ambiguity flag | 部分覆蓋 |

---

## EXAMPLES.md 的具體案例與 CBHE 應用

### 案例 1：Hidden Assumptions（Think Before Coding）

> "Add a feature to export user data"
→ LLM 直接假設：所有用戶、無分頁、檔案位置、欄位

**CBHE 應用**：
- C 收到請求時，偵測到「export user data」語義模糊
- 輸出 `ambiguity_flag: true`，要求 B 補詳細規格後才 routing
- 對應 Karpathy 的 "present multiple interpretations"

### 案例 2：Over-abstraction（Simplicity First）

> 30+ 行 Strategy pattern 用於簡單折扣計算

**CBHE 應用**：
- H 實作前，先問：「這個 abstraction 有幾個使用處？」
- 1 處 → 直接寫函式，不建 class
- TRAP `KARPATHY-OVER-ABSTRACT-001` 在此觸發

### 案例 3：Drive-by（ Surgical Changes）

> 修復一個 bug，卻改了格式化、風格、原本正常的程式碼

**CBHE 應用**：
- H 的 `h_surgical_edits` 約束：每個變更必須 trace 到用戶原始請求
- E 在核查時若發現 scope 外變更，觸發 `E-H-DRIVE-BY`

### 案例 4：No verification loop（Goal-Driven）

> "Fix the authentication system" → 沒有成功標準，直接改 code

**CBHE 應用**：
- B 的 NFR-VIDEO-001 定義了具體可測量標準（時長 ±5%、音訊存在等）
- E 依據 NFR 的布林條件核查，不接受「看起來 OK」
- E 的 6 項 `E-PDF-DELIVERY-GATE` 是此原則的具體實例

---

## 建議的核心文件更新

### 1. RULES.md 新增

```
### E-H-DRIVE-BY（CBHE H 層 drive-by 違規）
  Condition: diff 中出現非用戶請求範圍內的變更
  Action: 阻斷交付，觸發 incident log

### KARPATHY-OVER-ABSTRACT-001（CBHE TRAP）
  Condition: 新增 class/interface/protocol，但使用處 ≤ 1
  Fix: 收斂成普通函式，直到出現第 2 個使用處

### E-GOAL-DRIVEN-GATE（通用 E-gate）
  1. success_criteria_defined: B 的 NFR 有可測量標準
  2. test_reproducible: 關鍵行為可重複驗證
  3. no_regression: 現有測試綠燈
  4. scope_respected: diff 無超出請求的變更
```

### 2. H-DOMAIN 新增約束

```
h_no_speculative_code: H 不得實作「用戶未明確要求」的功能
h_assumption_check: H 若發現新假設，必須停止並回報 C
```

### 3. C-ROUTING-CHECK 新增輸出

```
ambiguity_flag: true/false — 若任務語義模糊
list_of_assumptions: [...] — C 列出已識別的假設
```

---

## 總結：karpathy-skills 對 CBHE 的價值

| CBHE 缺口 | karpathy 填補 |
|---|---|
| C 不主動呈現取捨 | 四原則第一條：Think Before Coding |
| H 容易 over-abstract | 四原則第二條：Simplicity First |
| H 容易 drive-by editing | 四原則第三條：Surgical Changes |
| E 沒有通用 goal-driven gate | 四原則第四條：Goal-Driven Execution |

karpathy-skills 的價值不是新原則，而是**具體的 anti-pattern 清單 + 對照案例**，讓 CBHE 的抽象原則有可操作的著力點。

---

## 標籤
#research #cbhe #karpathy #coding-standards #h-domain #c-routing #e-gate #anti-patterns
