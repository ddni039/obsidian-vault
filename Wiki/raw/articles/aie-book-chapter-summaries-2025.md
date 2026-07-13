---
source_url: https://github.com/chiphuyen/aie-book
ingested: 2026-07-11
sha256: 69325c6464fb
---
# Chapter Summaries — AI Engineering (Chip Huyen, O'Reilly 2025)

## Ch1: Introduction to Building AI Applications with Foundation Models
Foundation models transformed AI from specialized discipline → general development tool.
- From LMs → LLMs (self-supervision) → Foundation Models (multimodal) → AI Engineering
- 8 use case categories: Coding, Image/Video, Writing, Education, Conversational Bots, Information Aggregation, Data Organization, Workflow Automation
- Key insight: Before building, ask "Should I build this?" — evaluation and maintenance matter
- AI Engineering Stack: 3 layers; differs from ML Engineering (tabular data, feature engineering) and Full-Stack Engineering

## Ch2: Understanding Foundation Models
Core design decisions for using foundation models (not training from scratch).
- Training data quality determines model behavior; multilingual/low-resource languages require curation
- Transformer architecture dominates; scaling laws (Chinchilla) determine optimal params vs tokens ratio
- Post-training: SFT → Preference Finetuning (RLHF/DPO)
- Sampling makes AI probabilistic — this is the root cause of hallucinations and inconsistency
- Probabilistic nature → must build workflows around it, not against it

## Ch3: Evaluation Methodology
Why foundation models are harder to evaluate than traditional ML.
- Language modeling metrics: perplexity, cross-entropy, bits-per-character
- Exact evaluation: functional correctness, similarity scores
- AI-as-a-Judge: subjective, dependent on judge model, should supplement with exact + human eval
- Comparative evaluation: preference signals, ranking models pairwise
- Preference models: specialized judges predicting user preference

## Ch4: Evaluate AI Systems
Practical evaluation pipeline design.
- Criteria: Domain-specific capability, generation capability, instruction-following, cost, latency
- Model selection: Build vs Buy (7 axes: privacy, lineage, performance, functionality, control, cost)
- Public benchmarks: useful to weed out bad models, not to find best for your app; contamination risk
- Evaluation pipeline: evaluate all components → create guidelines → define methods and data
- No single perfect method — combine approaches to mitigate biases

## Ch5: Prompt Engineering
- In-context learning: zero-shot (no examples) vs few-shot (examples in context)
- Prompt anatomy: system prompt + user prompt; context efficiency matters
- Best practices: clear instructions, sufficient context, break complex tasks, "give model time to think" (CoT)
- Defensive PE: prompt injection, jailbreaking, information extraction, defenses
- Security is cat-and-mouse; will remain roadblock for high-stakes environments

## Ch6: RAG and Agents
RAG emerged first; agents came later with more autonomy.
- RAG: 2-step (retrieve → generate); overcomes context window limitations
  - Retrievers: term-based (BM25, Elasticsearch) vs embedding-based (vector search)
  - Embedding-based powered by vector search (HNSW, FAISS, ScaNN)
- RAG can be seen as special case of agent where retriever = tool
- Agents: planner (model) + tools + environment; complex tasks require multi-step planning
- Agent augmentation: reflection + memory system
- Tool use → security risks; more automation → more catastrophic failures
- Memory system needed when information exceeds context length

## Ch7: Finetuning
When NOT to finetune: lack of data, resources, or when RAG suffices.
- Full finetuning impractical for large models → memory bottlenecks
- PEFT: LoRA, QLoRA — reduce trainable parameters
- Quantized training: reduce bits per value
- Model merging, multi-task finetuning
- Finetuning vs RAG: complementary, not mutually exclusive

## Ch8: Dataset Engineering
- Data curation: quality > coverage > quantity
- Synthetic data generation (AI-powered) for training data
- Model distillation: transfer knowledge from large to small model
- Data processing: inspect, deduplicate, clean/filter, format
- Dangers of data contamination in benchmarks

## Ch9: Inference Optimization
- Latency metrics: TTFT (time to first token), TPOT (time per output token)
- Tradeoff: latency vs throughput vs cost
- AI accelerators: GPU architecture, memory bandwidth
- Model-level: quantization, distillation, KV cache management, attention kernels
- Service-level: batching, parallelism (tensor, pipeline, replica), prompt caching
- Most impactful techniques: quantization, tensor parallelism, replica parallelism, attention optimization

## Ch10: AI Engineering Architecture and User Feedback
- Architecture steps: Enhance Context → Guardrails → Router/Gateway → Caches → Agent Patterns → Monitoring → Orchestration
- Components overlap in functionality; each adds capability but also complexity
- Observability: detecting and tracing failures; foundation models introduce new failure modes
- Conversational feedback: new type of feedback enabled by chat interface
- Data flywheel: user feedback → model improvement
- AI engineering is moving closer to product than traditional ML engineering

Source: https://github.com/chiphuyen/aie-book (MIT License)
Ingested: 2026-07-11
