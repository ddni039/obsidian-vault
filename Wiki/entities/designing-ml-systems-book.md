---
title: "Designing Machine Learning Systems"
created: 2026-07-11
updated: 2026-07-11
uid: e-3951c2c69113
type: entity
tags: [book, mlops, ml-systems, data-engineering, training, deployment, monitoring, responsible-ai]
sources: [raw/articles/designing-ml-systems-summary-2026-07-11.md, raw/articles/designing-ml-systems-mlops-tools-2026-07-11.md, raw/articles/designing-ml-systems-resources-2026-07-11.md, raw/articles/designing-ml-systems-basic-ml-review-2026-07-11.md]
confidence: high
---

# Designing Machine Learning Systems (DMLS)

## Overview

*Designing Machine Learning Systems* by [[chip-huyen]] (O'Reilly, 2022) is a holistic ML systems design textbook aimed at ML engineers, data scientists, and engineering managers. Unlike tutorial books focused on algorithms, it focuses on **key design decisions** when developing and deploying ML systems in production.

> "Machine learning systems are both complex and unique. Complex because they consist of many different components and unique because they're data dependent." — Ch1

**Companion volume:** [[chip-huyen]]'s later book *AI Engineering* (2025) covers the foundation model era — DMLS covers traditional ML; AIE covers LLM-based applications.

## Book Structure (11 Chapters)

| Ch | Title | Core Content |
|----|-------|-------------|
| 1 | Overview of ML Systems | Research vs production ML, system approach |
| 2 | ML Systems Design | Business→ML objectives, reliability/scalability/maintainability/adaptability |
| 3 | Data Engineering Fundamentals | Formats, data models (relational/doc/graph), storage engines, batch vs stream |
| 4 | Training Data | Sampling, labeling (human/weak supervision), class imbalance, augmentation |
| 5 | Feature Engineering | Transforming raw data into features |
| 6 | Model Development & Offline Evaluation | Experiment tracking, AutoML, evaluation metrics |
| 7 | Model Deployment & Prediction Service | Shadow mode, canary, blue-green, microservices |
| 8 | Data Distribution Shifts & Monitoring | Covariate/label shift, monitoring, alert fatigue |
| 9 | Continual Learning & Test in Production | A/B testing, bandit, shadow deployment |
| 10 | Infrastructure & Tooling for MLOps | Model store, feature store, deployment tools |
| 11 | The Human Side of ML | User experience, team structure, responsible AI |

## Key Design Principles

### Four System Requirements (Ch2)
Every ML system must satisfy:
1. **Reliability** — system continues to perform correctly even when things go wrong
2. **Scalability** — growing demands can be handled gracefully
3. **Maintainability** — other teams can contribute and sustain the system
4. **Adaptability** — can evolve with changing requirements and data

### ML vs Traditional Software (Ch1)
| Aspect | Traditional Software | ML Systems |
|--------|---------------------|------------|
| Logic | Hand-coded | Learned from data |
| Behavior | Deterministic | Probabilistic |
| Correctness | provable | measurable |
| Debugging | formal methods | empirical |
| Failure mode | crashes | silent degradation |

### Iterative Development Process (Ch2)
```
Business Problem → ML Problem → Data Collection → Feature Engineering
→ Model Development → Deployment → Monitoring → ...
```
Never one-off; continuous feedback loop.

## Key Thematic Contributions

### Data is Central (Ch2)
The book argues data is the most important component:
- AlexNet (2012), BERT (2018), GPT (2018) — all leveraged large datasets
- "A nontrivial part of this book will be devoted to shedding light on various data questions"

### Data Engineering Fundamentals (Ch3)
- **Row vs Column formats:** Row (JSON/CSV) for writes; Column (Parquet/ORC) for analytics
- **Three data models:** Relational (SQL), Document (NoSQL), Graph (knowledge graphs)
- **Data passing modes:** Database → Services → Real-time transport (Kafka/RabbitMQ)
- **Batch vs Stream:** Batch produces static features; Stream produces dynamic features

### Training Data Lifecycle (Ch4)
- **Sampling:** Probability (random, stratified) vs non-probability (convenience, snowball)
- **Labels:** Natural labels (delayed feedback) vs human annotation (expensive/slow)
- **Alternatives:** Weak supervision (Snorkel), semi-supervised, transfer learning, active learning
- **Class Imbalance:** Resampling, cost-sensitive learning, threshold adjustment
- **Data Augmentation:** For CV (rotation, flip, crop) and NLP (synonym, back-translation)

### Monitoring: Distribution Shifts (Ch8)
- **Covariate shift:** P(X) changes, P(Y|X) unchanged
- **Label shift:** P(Y) changes, P(X|Y) unchanged
- **Concept drift:** P(Y|X) changes over time
- Monitoring pitfalls: alert fatigue, concept drift vs distribution shift

### Deployment Patterns (Ch7)
- Shadow mode: model runs parallel, no real decisions
- Canary: small % traffic to new model
- Blue-green: instant rollback capability
- A/B testing vs shadow mode vs canary

### Responsible AI (Ch11)
- Probabilistic → inconsistency in user experience
- Mostly correct → users need easy correction mechanisms
- Ethics frameworks, bias detection (AIF360), fairness audits

## MLOps Tool Ecosystem (Ch10 / mlops-tools.md)

DMLS intentionally avoids tool recommendations in the book text (tooling is ephemeral), but the repo catalogs:

| Category | Tools |
|----------|-------|
| Data & Features | ClickHouse, Druid, Great Expectations, DVC, Feast, Amundsen, DataHub |
| Experiment Tracking | MLflow, Aim |
| Model Optimization | TVM, TensorRT, Triton, DeepSpeed |
| Labeling | Snorkel, Label Studio, doccano |
| Interpretability | SHAP, LIME, Captum |
| Monitoring | Prometheus, Sentry, Grafana |
| Similarity Search | Faiss, Annoy, Milvus |

## Mathematical Foundations (basic-ml-review.md)

### Objective Functions
- **Scalar outputs:** RMSE (Euclidean), MAE (Manhattan)
- **Probability distributions:** Cross-entropy
- Regularizers: L1 (Lasso), L2 (Ridge) — encourage smaller parameters

### Learning Procedures
- **Exact:** Linear regression (closed-form solution)
- **Iterative:** Gradient descent — most popular
- **Optimizers:** Momentum, Adam, RMSProp — speed up convergence, improve generalization
- Key insight: minimizing training loss ≠ best test performance (generalization gap)

### Model Types
- **Parametric:** parameters fixed w.r.t. sample size (linear, neural network)
- **Non-parametric:** parameters grow with sample size (decision trees, k-means)

## Relationship to Other Entities

- [[chip-huyen]] — Author; also wrote *AI Engineering* (2025)
- [[llmops]] — DMLS planted seeds; Chip coined "LLMOps" in 2023 essay
- [[talk-to-your-data]] — RAG is a specific pattern; DMLS Ch6/Ch7 covers similar retrieval-grounded deployment
- [[anthropic-ai-agents-framework]] — AIE Ch6 builds on DMLS foundations
- [[martin-kleppmann-ddia]] — DMLS Ch3 references Kleppmann's *Designing Data-Intensive Applications*

## See Also
- [[llmops]] — The operational discipline around ML systems
- [[ai-engineering-framework]] — Chip's AIE framework for foundation model applications
- [[data-replication]] — DMLS Ch3 covers replication strategies
- [[data-partitioning]] — DMLS Ch3 covers data partitioning
- [[sql-execution-plan]] — DMLS Ch5/Ch6 touch on query optimization
- [[hermes-agent]] — Faces same ML systems design challenges (monitoring, deployment, reliability)
