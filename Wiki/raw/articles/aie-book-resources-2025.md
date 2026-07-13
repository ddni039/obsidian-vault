---
source_url: https://github.com/chiphuyen/aie-book
ingested: 2026-07-11
sha256: 8e8d71209929
---
# Key Resources — AI Engineering (Chip Huyen, 2025)

## ML Theory Fundamentals
- Stanford CS231N (http://cs231n.github.io/) — neural networks fundamentals
- Andrej Karpathy's Neural Networks: Zero to Hero (YouTube playlist)
- Kevin P Murphy: Machine Learning: A Probabilistic Perspective

## Ch1 — Planning Applications
- OpenAI (2023): GPTs are GPTs — labor market impact, 100% exposed: interpreters, tax preparers, web designers, writers
- Applied LLMs (Yan et al., 2024) — Eugene Yan's deployment learnings
- Musings on Building a Generative AI Product (LinkedIn, Juan Pablo Bottaro)
- Apple Human Interface Guidelines for ML apps

## Ch2 — Understanding Foundation Models
- Key papers: InstructGPT, GPT-2/3, Gopher, Chinchilla, Llama 1/2/3, Constitutional AI, Qwen
- Scaling laws: GPT (Kaplan), Chinchilla (Hoffman et al.), Beyond Chinchilla-Optimal (Sardana et al.)
- Post-training: RLHF, DPO, Constitutional AI
- RoPE positional encoding (Su et al., 2021)

## Ch3+4 — Evaluation
- Anthropic: Challenges in Evaluating AI Systems
- HELM (Stanford, 2022), BIG-bench (Google, 2022)
- MT-Bench + Chatbot Arena (Zheng et al., 2023) — LLM-as-a-Judge
- Eugene Yan: LLM Task-Specific Evals
- Hamel Hussain: Your AI Product Needs Evals

## Ch5 — Prompt Engineering
- Anthropic Interactive Prompt Tutorial (Google Sheets)
- Brex's Prompt Engineering Guide (GitHub)
- dair-ai/Prompt-Engineering-Guide
- Defensive: Instruction Hierarchy (OpenAI 2024), Prompt Injection (Greshake et al.)
- Tools: PyRIT, Garak, GPTFUZZER, MasterKey

## Ch6 — RAG and Agents
- RAG: Lewis et al. (2020), Gao et al. (2023 survey), Anthropic Contextual Retrieval (2024)
- Chunking: Pinecone, LangChain tutorials, Greg Kamradt 5 Levels
- Agents: Chameleon (2023), Toolformer (Schick et al.), Generative Agents (Park et al.)
- Function calling: Berkeley Function Calling Leaderboard, Gorilla paper

## Ch7 — Finetuning
- LoRA (Hu et al.), QLoRA (Dettmers et al.)
- Model merging: Wortsman et al., ILDB, Steerable KL
- Multi-task finetuning, instruction tuning (Chung et al.)
- Memory calculation: Chinchilla's training compute formula

## Ch8 — Dataset Engineering
- Synthetic data: Beyond Chinchilla-Optimal
- Data filtering: LaBSE, academic citations
- Model distillation: MoE, Switch Transformer

## Ch9 — Inference Optimization
- NVIDIA: Mastering LLM Inference Optimization
- Character.AI: Optimizing Inference at Character.AI
- Speculative Sampling (DeepMind, 2023)
- DistServe (Zhong et al., 2024): Prefill/Decoding Decoupling
- KV Cache optimization: Omri Mallis blog
- Tim Dettmers: Best GPUs for Deep Learning

## Ch10 — Architecture & Feedback
- Google SRE: Monitoring Chapter
- Microsoft: Guidelines for Human-AI Interaction (18 principles)
- Amazon: Feedback-Based Self-Learning in Conversational AI

## Engineering Blogs
LinkedIn, DoorDash, Uber, Netflix, LMSYS, Anyscale, Databricks, Together, Duolingo

Source: https://github.com/chiphuyen/aie-book (MIT License)
