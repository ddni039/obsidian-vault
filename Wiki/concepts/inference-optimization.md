---
title: Inference Optimization
created: 2026-07-11
updated: 2026-07-11
type: concept
tags: [ai-engineering, inference, optimization, latency, throughput, llm]
sources: [raw/articles/aie-book-chapter-summaries-2025.md, raw/articles/aie-book-resources-2025.md]
confidence: high
---

# Inference Optimization

## Overview
Making LLM inference cheaper and faster. *AIE* Ch9 covers the full stack: from model-level techniques to service-level optimizations. Fundamental tradeoff: **latency vs throughput vs cost**.

## Key Metrics

### Time to First Token (TTFT)
How long before the model starts generating. Dominated by **prefilling** phase (processing input + KV cache computation).

### Time Per Output Token (TPOT)
How long each subsequent token takes. Dominated by **decoding** phase (autoregressive generation).

### Latency vs Throughput
| | Latency | Throughput |
|---|---|---|
| **Measures** | Time per request | Tokens per second |
| **Use case** | User-facing (chat, real-time) | Batch processing |
| **Optimize for** | Response speed | Cost efficiency |

### GPU Utilization
Percentage of GPU compute actually used. Low utilization = wasted resources.

## AI Accelerators

GPUs (NVIDIA H100, A100) dominate. Key specs:
- **Memory bandwidth**: how fast data moves in/out of GPU
- **FLOPs**: raw compute capacity
- **Memory size**: limits batch size and model size

## Optimization Techniques

### Model-Level (Changes the Model)

**Quantization**
- Reduce weight precision: FP16 → INT8 → INT4
- PTQ (Post-Training Quantization): quantize after training
- QAT (Quantization-Aware Training): train with quantization in mind
- Impact: 2-4x memory reduction, minimal quality loss with proper calibration

**Knowledge Distillation**
- Train small model to mimic large model
- "I think so" → soft labels from teacher model

**KV Cache Optimization**
- Cache key-value activations from previous tokens
- Reduces redundant computation in autoregressive decoding
- Bottleneck: memory-bound, not compute-bound

**Attention Kernels**
- FlashAttention: IO-aware exact attention
- Approximate attention: sparse attention, linear attention

### Service-Level (Keeps Model Intact)

**Batching**
- Static batching: group multiple requests, process together (wastes GPU on short requests)
- Dynamic batching: adaptively group requests by length

**Parallelism**
- **Tensor parallelism**: split model weights across GPUs (for large models)
- **Pipeline parallelism**: split model layers across GPUs
- **Data parallelism**: replicate model, process different batches

**Prefill/Decoding Decoupling**
- Separate prefill and decode onto different hardware (prefill = compute-bound, decode = memory-bound)

**Prompt Caching**
- Cache KV of system prompts and shared prefixes
- Reuse for multi-turn conversations with overlapping context

## Most Impactful Techniques (per *AIE* Ch9)

1. **Quantization** — generally works well across models
2. **Tensor parallelism** — reduces latency AND enables larger models
3. **Replica parallelism** — relatively straightforward, reduces latency
4. **Attention optimization** — significantly accelerates transformers

## Inference Optimization vs Training Optimization

| | Training | Inference |
|---|---|---|
| **Goal** | Improve model quality | Reduce cost/latency |
| **Frequency** | One-time (or periodic) | Every request |
| **Constraints** | GPU memory, time | GPU memory, latency |
| **Key techniques** | Distributed training, gradient checkpointing | Quantization, batching, caching |

## LLM Inference Companies & Tools

- **vLLM**: PagedAttention, high-throughput inference
- **TensorRT-LLM**: NVIDIA's optimized inference engine
- **Ollama**: local inference
- **LM Studio**: local model serving
- **Character.AI**: published their optimization techniques (2024)

## See Also
- [[ai-engineering-framework]] — The framework this fits into
- [[finetuning-vs-prompting]] — Training vs inference tradeoff
- [[embedding-vector-database]] — Vector search inference
