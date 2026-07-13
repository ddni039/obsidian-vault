---
title: VCL - Varnish Configuration Language
created: 2026-07-13
updated: 2026-07-13
type: concept
tags: [concept, varnish, vinyl-cache, vcl, dsl, configuration-language, http, hot-reload]
sources:
  - raw/articles/vinyl-cache-official-2026-07-13.md
related:
  - "[[vinyl-cache]]"
  - "[[declarative-configuration-pattern]]"
confidence: high
---

# VCL - Varnish Configuration Language

## 定義

**VCL** = Domain-specific language（DSL）用於宣告 Vinly Cache 的 HTTP request/response policies。Vinyl Cache 的核心配置語言。

> VCL enables you to write policies on how incoming requests should be handled. In such a policy you can decide what content you want to serve, from where you want to get the content and how the request or response should be altered.

## 核心特徵

| 特徵 | 說明 |
|------|------|
| **語言類型** | Domain-specific language（DSL）|
| **目標** | 宣告 HTTP policies |
| **編譯流程** | VCL → C code → compiled .so → loaded into accelerator |
| **Hot reload** | 不需要重啟就能載入新配置 |
| **內建** | vcl_recv/vcl_hash/vcl_miss/vcl_hit/vcl_deliver 等 hooks |

## VCL 編譯流程

```
.vcl file
   ↓
   C compiler
   ↓
   shared object (.so)
   ↓
   loaded into Vinyl Cache accelerator
   ↓
   active without restart
```

**關鍵創新**：每次修改 VCL，Vinyl Cache 自動編譯成 C → 編譯成 .so → **runtime hot reload**。

## VCL 核心 Hooks（VCL Steps）

### Request Lifecycle

```
vcl_recv:
    收到請求，決定如何處理（cache / pass / pipe / synth）

vcl_hash:
    生成 cache key

vcl_miss:
    cache miss，決定是否 fetch from backend

vcl_hit:
    cache hit，可選擇 deliver 或 pass

vcl_hit_for_pass:
    決定多久後重新 fetch

vcl_backend_fetch:
    從 backend fetch

vcl_backend_response:
    backend 回應，可修改/判斷

vcl_deliver:
    回應 client 前最後 hook

vcl_synth:
    synthetic 錯誤回應
```

### Lifecycle Hooks

```
vcl_init:
    Startup（載入 VMODs）

vcl_fini:
    Shutdown
```

## VCL 語法範例

### Basic vcl_recv

```vcl
sub vcl_recv {
    if (req.url ~ "\.(jpg|png|gif)$") {
        # 圖片不用認證，直接 cache
        unset req.http.Authorization;
    }
    if (req.method == "PURGE") {
        # PURGE 方法用於 invalidation
        return (purge);
    }
}
```

### Backend Health Check

```vcl
probe health_check {
    .url = "/health";
    .timeout = 2s;
    .interval = 5s;
    .window = 5;
    .threshold = 3;
}

backend origin {
    .host = "127.0.0.1";
    .port = "8080";
    .probe = health_check;
}
```

### Grace Mode

```vcl
sub vcl_deliver {
    if (obj.ttl >= 0s) {
        # 正常 deliver
    }
    if (obj.ttl + obj.grace > 0s) {
        # 還在 grace 期間 serve stale content
        set resp.http.X-Cache = "HIT";
    } else {
        set resp.http.X-Cache = "MISS";
    }
}
```

## VMODs（擴展 VCL）

VMODs = C 擴展模組，擴展 VCL 功能。

### 內建 VMODs

| VMOD | 功能 |
|------|------|
| **std** | log/rollack/random/fnv32a 等工具 |
| **cookie** | Cookie 解析和操作 |
| **purge** | Cache purging |
| **directors** | 負載平衡 |
| **blob** | Binary data encoding/decoding |
| **h2** | HTTP/2 控制 |
| **proxy** | PROXYv2 TLV attributes |
| **unix** | Unix domain sockets |

### 第三方 VMODs

| VMOD | 用途 |
|------|------|
| **awsrest** | AWS Signature V4 |
| **blobdigest** | SHA256/HMAC |
| **cluster** | Cache clustering |
| **softpurge** | Soft cache invalidation |
| **statsd** | StatsD integration |

## 與 Hermes 的對應

| VCL 概念 | Hermes 對應 | 評估 |
|---------|------------|------|
| **Declarative DSL** | SOUL/AGENTS/RULES/CODEX 核心檔 | ✅ 直接對應 |
| **Hook-based lifecycle** | Phase（B→H→E）| ✅ 概念相似 |
| **VMOD plugin system** | Skill plugin 系統 | ✅ 直接對應 |
| **Hot reload .so** | `touch config.yaml` → reload | ✅ 直接對應 |
| **Backend health probe** | MCP heartbeat | ✅ 直接對應 |
| **Cache key (hash)** | E-code routing key | ✅ 概念相似 |

## 對 Hermes 的設計啟示

### 1. VCL 編譯流程

Vinyl Cache 的 VCL → C → .so → hot reload 是個很優雅的設計。

**Hermes 應用**：
```
SOUL.md / AGENTS.md / RULES.md / CODEX.md
   ↓
   Internal representation（JSON/YAML）
   ↓
   Hot reload without restart
```

### 2. Hook-based Lifecycle

VCL 的 lifecycle hooks（vcl_recv → vcl_hash → vcl_miss → ...）跟 Hermes 的 Phase routing（Plan → Build → Audit）概念相似。

**Hermes 應用**：Phase 鉤子可以更聲明式：
```yaml
hooks:
  on_plan_complete: check_preconditions
  on_build_start: inject_context
  on_audit_pass: update_metrics
```

### 3. VMOD Plugin 生態

Vinyl Cache 有 30+ VMODs 擴展生態。

**Hermes 應用**：Skill 系統 = Hermes 的「VMODs」，每個 Skill 是對核心功能的擴展。

## 為何 VCL 設計優秀？

| 設計優點 | 說明 |
|---------|------|
| **聲明式** | 不用寫 imperative 流程，聲明 policy 就好 |
| **安全** | 執行在 sandboxed C 環境 |
| **高效** | 編譯成 C → native code → 高效 |
| **可測試** | varnishtest 框架可 unit test |
| **可組合** | VMODs 可自由組合 |

## 參考資源

- [VCL Reference](https://varnish-cache.org/docs/reference/vcl/)
- [VCL Syntax](https://varnish-cache.org/docs/users-guide/vcl-syntax/)
- [VCL Design Patterns](https://varnish-cache.org/docs/vcl-design-patterns/)
- [VMOD Directory](https://vinyl-cache.org/vmods)