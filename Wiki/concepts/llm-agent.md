---
title: LLM-Powered Autonomous Agents
source: https://lilianweng.github.io/posts/2023-06-23-agent/
author: Lilian Weng
date: 2023-06
type: concept
tags: [llm, agent, planning, memory, tool-use, reflection, react, reflexion, mips, rag]
summary: Building autonomous agents with LLM as core controller — Planning (CoT, ToT, ReAct), Memory (STM/LTM/MIPS), Tool Use (MRKL, Toolformer, HuggingGPT), and case studies (ChemCrow, Generative Agents, AutoGPT)
related:
  - prompt-engineering
  - chain-of-thought
  - toolformer
  - react
  - memory-systems
---

# LLM-Powered Autonomous Agents

> Source: [Lilian Weng — LLM-Powered Autonomous Agents (Jun 2023)](https://lilianweng.github.io/posts/2023-06-23-agent/)

## Agent System Overview

LLM as the **brain**, complemented by three key components:

| Component | Capability | Human Analogy |
|----------|-----------|---------------|
| **Planning** | Subgoal decomposition + self-reflection | Prefrontal cortex |
| **Memory** | Short-term (in-context) + Long-term (vector store) | Hippocampus |
| **Tool Use** | External APIs, code execution, information retrieval | Hands / sensory tools |

## Component One: Planning

### Task Decomposition
Break down complex tasks into manageable subgoals.

Methods:
1. **LLM with simple prompting** — `"Steps for XYZ.\n1."` or `"What are the subgoals?"`
2. **Task-specific instructions** — e.g. `"Write a story outline"`
3. **Human inputs**

**Chain of Thought** (CoT): instruct model to "think step by step" to decompose hard tasks. (Wei et al. 2022)

**Tree of Thoughts** (Yao et al. 2023): extend CoT by exploring multiple reasoning branches at each step — creates a tree structure. Search via BFS or DFS.

**LLM+P** (Liu et al. 2023): outsource planning to external classical planner via PDDL (Planning Domain Definition Language).

### Self-Reflection

**ReAct** (Yao et al. 2023): integrates reasoning and acting. Format:
```
Thought: ...
Action: ...
Observation: ...
```
Combines LLM reasoning traces with task-specific discrete actions (e.g. Wikipedia search).

**Reflexion** (Shinn & Labash 2023): dynamic memory + self-reflection to improve reasoning. Two failure modes:
- **Inefficient planning**: trajectory too long without success
- **Hallucination**: consecutive identical actions leading to same observation

Heuristic `h_t` determines when to reset environment.

**Chain of Hindsight** (CoH; Liu et al. 2023): supervised fine-tuning on sequence of past outputs annotated with human feedback. ranked by reward. Model learns to produce better outputs based on feedback history.

**Algorithm Distillation** (AD; Laskin et al. 2023): distill RL algorithm into neural network via behavioral cloning over multi-episode learning histories. Requires 2-4 episodes to learn near-optimal in-context RL.

## Component Two: Memory

### Types of Memory (Human → Agent Mapping)

| Human Memory | Duration | Agent Equivalent |
|-------------|----------|----------------|
| Sensory | ms–sec | Raw input embedding |
| Short-Term (STM) | ~30 sec | In-context learning (finite context window) |
| Long-Term (LTM) | days–decades | External vector store + fast retrieval |

### Maximum Inner Product Search (MIPS)

External memory enables finite context window to access larger knowledge pool.

ANN algorithms for fast MIPS:

| Algorithm | Key Idea |
|----------|---------|
| **LSH** | Similar items → same hash buckets (locality-sensitive) |
| **ANNOY** | Random projection trees / binary trees |
| **HNSW** | Hierarchical navigable small world graphs |
| **FAISS** | Clustering + coarse-to-fine quantization |
| **ScaNN** | Anisotropic vector quantization |

## Component Three: Tool Use

### MRKL (Modular Reasoning, Knowledge and Language)
(Karpas et al. 2022) — LLM as **router** to expert modules (neural or symbolic).

### TALM / Toolformer
- **TALM**: self-play bootstrapping of tool-use examples
- **Toolformer**: self-supervised LM learns to call APIs (calculator, search, Q&A, translation, calendar)

Toolformer format:
```
<API>calculator(2+2)</API>
<API>calculator(2+2) → 4</API>
```

### ChatGPT Plugins / Function Calling
Practical deployment of tool-augmented LLMs.

### HuggingGPT (Shen et al. 2023)
LLM as **task planner** over HuggingFace model hub. 4 stages:
1. Task planning (LLM parses user request into task graph)
2. Model selection (LLM picks best model per task)
3. Task execution (expert models run)
4. Response generation (LLM summarizes results)

### API-Bank Benchmark
Evaluates tool-augmented LLMs at 3 levels:
- **Level 1**: Call API correctly
- **Level 2**: Retrieve and use API from documentation
- **Level 3**: Plan beyond retrieve + call (multi-step workflows)

## Case Studies

### ChemCrow (Bran et al. 2023)
Domain-specific agent for organic synthesis, drug discovery, materials design. 13 expert tools via LangChain. Uses ReAct format (Thought → Action → Observation).

**Finding**: GPT-4 self-evaluation said it matched ChemCrow; **human expert evaluation showed ChemCrow significantly outperformed** — reveals LLM cannot reliably judge its own performance in expert domains.

### Generative Agents (Park et al. 2023)
25 LLM-powered virtual characters living in a sandbox (Sims-like). Architecture:
- **Memory stream**: comprehensive natural language record of experiences
- **Retrieval model**: surfaces context by relevance + recency + importance
- **Reflection**: synthesizes memories into higher-level inferences
- **Planning**: optimizes for believability in the moment

Emergent social behaviors: information diffusion, relationship memory, coordination of social events (e.g. party invitation).

### AutoGPT / GPT-Engineer
Proof-of-concept autonomous agents with LLM as controller. AutoGPT uses ~20 fixed commands (Google Search, browse website, write/read files, etc.) in JSON format. Reliability issues due to natural language interface parsing.

## Challenges

1. **Finite context length** — limits historical information, instructions, API call context
2. **Long-term planning** — LLMs struggle to adjust plans when facing unexpected errors
3. **Natural language interface reliability** — formatting errors and rebellious behavior; much agent code focuses on **parsing LLM output**

## Key Papers

| Paper | Year | Contribution |
|-------|------|-------------|
| Wei et al. — CoT | 2022 | Chain-of-thought prompting |
| Yao et al. — ReAct | 2023 | Reasoning + acting with external tools |
| Shinn & Labash — Reflexion | 2023 | Dynamic memory + self-reflection |
| Liu et al. — CoH | 2023 | Chain of Hindsight fine-tuning |
| Laskin et al. — AD | 2023 | Algorithm Distillation |
| Karpas et al. — MRKL | 2022 | Modular neuro-symbolic agents |
| Schick et al. — Toolformer | 2023 | Self-supervised tool learning |
| Shen et al. — HuggingGPT | 2023 | LLM as task planner |
| Li et al. — API-Bank | 2023 | Tool-augmented LLM benchmark |
| Park et al. — Generative Agents | 2023 | Interactive simulacra of human behavior |
| Bran et al. — ChemCrow | 2023 | Domain-specific agent for chemistry |

## Citation

```
@article{weng2023agent,
  title   = "LLM-Powered Autonomous Agents",
  author  = "Weng, Lilian",
  journal = "lilianweng.github.io",
  year    = 2023,
  month   = "Jun",
  url     = "https://lilianweng.github.io/posts/2023-06-23-agent/"
}
```
