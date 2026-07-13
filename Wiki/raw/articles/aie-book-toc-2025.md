---
source_url: https://github.com/chiphuyen/aie-book
ingested: 2026-07-11
sha256: 202981f90008
---
# Table of Contents — AI Engineering (Chip Huyen, O'Reilly 2025)

## Full Chapter Outline

| Chapter | Title | Pages |
|---------|-------|-------|
| Preface | | ix |
| Ch1 | Introduction to Building AI Applications with Foundation Models | 1 |
| Ch2 | Understanding Foundation Models | 49 |
| Ch3 | Evaluation Methodology | 113 |
| Ch4 | Evaluate AI Systems | 159 |
| Ch5 | Prompt Engineering | 211 |
| Ch6 | RAG and Agents | 253 |
| Ch7 | Finetuning | 307 |
| Ch8 | Dataset Engineering | 363 |
| Ch9 | Inference Optimization | 405 |
| Ch10 | AI Engineering Architecture and User Feedback | 449 |
| Epilogue | | 495 |
| Index | | 497 |

## Chapter 1: Introduction
- From Language Models → LLMs → Foundation Models → AI Engineering
- Foundation Model Use Cases: Coding, Image/Video, Writing, Education, Conversational Bots, Information Aggregation, Data Organization, Workflow Automation
- Planning AI Applications: Use Case Evaluation, Setting Expectations, Milestone Planning, Maintenance
- AI Engineering Stack: Three Layers, vs ML Engineering, vs Full-Stack Engineering

## Chapter 2: Understanding Foundation Models
- Training Data: Multilingual Models, Domain-Specific Models
- Modeling: Model Architecture (Transformer), Model Size
- Post-Training: Supervised Finetuning (SFT), Preference Finetuning (RLHF, DPO)
- Sampling: Fundamentals, Strategies, Test Time Compute, Structured Outputs
- Probabilistic Nature of AI

## Chapter 3: Evaluation Methodology
- Challenges of Evaluating Foundation Models
- Language Modeling Metrics: Entropy, Cross Entropy, Bits-per-Character, Perplexity
- Exact Evaluation: Functional Correctness, Similarity Measurements, Embedding
- AI as a Judge: Why, How, Limitations, What Models Can Judge
- Ranking Models with Comparative Evaluation

## Chapter 4: Evaluate AI Systems
- Evaluation Criteria: Domain-Specific Capability, Generation Capability, Instruction-Following, Cost and Latency
- Model Selection: Workflow, Build vs Buy, Navigate Public Benchmarks
- Design Your Evaluation Pipeline: Evaluate Components, Create Guidelines, Define Methods and Data

## Chapter 5: Prompt Engineering
- In-Context Learning: Zero-Shot and Few-Shot
- System Prompt and User Prompt
- Context Length and Context Efficiency
- Best Practices: Clear Instructions, Sufficient Context, Break into Subtasks, Give Model Time to Think
- Defensive Prompt Engineering: Proprietary Prompts, Jailbreaking, Prompt Injection, Information Extraction, Defenses

## Chapter 6: RAG and Agents
- RAG: Architecture, Retrieval Algorithms, Retrieval Optimization, RAG Beyond Texts
- Agents: Overview, Tools, Planning, Agent Failure Modes and Evaluation
- Memory

## Chapter 7: Finetuning
- When to Finetune (reasons for and against)
- Finetuning and RAG
- Memory Bottlenecks: Backpropagation, Memory Math, Numerical Representations, Quantization
- Finetuning Techniques: PEFT (LoRA, QLoRA), Model Merging, Multi-Task Finetuning
- Finetuning Tactics

## Chapter 8: Dataset Engineering
- Data Curation: Quality, Coverage, Quantity, Acquisition and Annotation
- Data Augmentation and Synthesis: Why, Traditional Techniques, AI-Powered, Model Distillation
- Data Processing: Inspect, Deduplicate, Clean and Filter, Format

## Chapter 9: Inference Optimization
- Understanding: Inference Overview, Performance Metrics, AI Accelerators
- Optimization: Model Optimization (Quantization, Distillation, KV Cache, Attention Kernels), Inference Service Optimization (Batching, Parallelism, Prefill/Decoding Decoupling, Prompt Caching)

## Chapter 10: AI Engineering Architecture and User Feedback
- Architecture: Enhance Context, Guardrails, Model Router/Gateway, Caches, Agent Patterns, Monitoring, AI Pipeline Orchestration
- User Feedback: Extracting Conversational Feedback, Feedback Design, Feedback Limitations

Source: https://github.com/chiphuyen/aie-book (MIT License)
