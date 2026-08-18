---
source_url: https://github.com/NousResearch/hermes-agent/blob/main/plugins/memory/hindsight/README.md
ingested: 2026-07-11
sha256: <computed-on-ingest>
---

# Hindsight Memory Provider

Long-term memory plugin with knowledge graph, entity resolution, and multi-strategy retrieval. Supports cloud, local embedded, and local external modes.

## Requirements

- **Cloud:** API key from ui.hindsight.vectorize.io
- **Local Embedded:** API key for a supported LLM provider (OpenAI, Anthropic, Gemini, Groq, OpenRouter, MiniMax, Ollama, or any OpenAI-compatible endpoint). Embeddings and reranking run locally.
- **Local External:** A running Hindsight instance (Docker or self-hosted) reachable over HTTP.

## Setup

```bash
hermes memory setup    # select "hindsight"
```

## Deployment Modes

### Cloud
Connects to Hindsight Cloud API at `https://api.hindsight.vectorize.io`.

### Local Embedded
- Spins up local Hindsight daemon with built-in PostgreSQL
- Daemon starts automatically on first use, stops after 5 minutes of inactivity
- Supports any OpenAI-compatible endpoint (llama.cpp, vLLM, LM Studio, etc.)

### Local External
Points to existing Hindsight instance (Docker, self-hosted). No daemon management.

## Config

Config file: `~/.hermes/hindsight/config.json`

Key settings:
- `mode`: `cloud`, `local_embedded`, or `local_external`
- `bank_id_template`: Dynamic bank naming with `{profile}`, `{workspace}`, `{platform}`, `{user}`, `{session}`
- `recall_budget`: `low` / `mid` / `high`
- `recall_types`: `observation` (default, consolidated beliefs) / `world` / `experience` (raw facts)
- `auto_recall`: Automatically recall memories before each turn
- `auto_retain`: Automatically retain conversation turns
- `memory_mode`: `hybrid` (auto injection + tools) / `context` (auto only) / `tools` (tools only)

## Tools

| Tool | Description |
|------|-------------|
| `hindsight_retain` | Store information with auto entity extraction |
| `hindsight_recall` | Multi-strategy search (semantic + entity graph) |
| `hindsight_reflect` | Cross-memory synthesis (LLM-powered) |

## Client Version

Requires `hindsight-client >= 0.6.1`.
