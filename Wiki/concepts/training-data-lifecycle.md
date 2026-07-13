---
title: "Training Data Lifecycle"
created: 2026-07-11
updated: 2026-07-11
type: concept
tags: [mlops, training-data, labeling, data-quality, ml-systems]
sources: [raw/articles/designing-ml-systems-summary-2026-07-11.md]
confidence: high
---

# Training Data Lifecycle

## Definition

Training data forms the foundation of modern ML algorithms. No matter how clever the algorithms, bad training data produces bad models. From [[designing-ml-systems-book]] Ch4.

## Sampling Methods

### Probability Sampling
- **Random sampling** — each sample has equal probability of selection
- **Stratified sampling** — ensures proportional representation of subgroups

### Non-Probability Sampling
- **Convenience sampling** — use available data (common, biased)
- **Snowball sampling** — existing subjects recruit future subjects
- Risk of systematic bias

## Labeling Strategies

### Natural Labels
Labels that arise naturally from user behavior:
- Click-through rates
- Purchase decisions
- Time spent
- Feedback loop length is the time between prediction and label availability

### Human Annotation
- **Pros:** High quality, controlled
- **Cons:** Expensive, slow, subject to annotator bias

### Alternatives to Human Labels

| Method | Description | Tools |
|--------|-------------|-------|
| **Weak Supervision** | Programmatic labels via heuristics/rules | Snorkel |
| **Semi-supervised** | Leverage unlabeled data with few labels | SSL techniques |
| **Transfer Learning** | Pre-trained models + fine-tune | Hugging Face |
| **Active Learning** | Iteratively label most informative samples | Custom |

## Class Imbalance

Class imbalance is the norm in real-world ML problems:
- Rare disease detection: 0.1% positive cases
- Fraud detection: 0.01% fraudulent transactions

### Handling Techniques

1. **Choose the right metric** — Accuracy is useless; use Precision/Recall/F1/AUC
2. **Resampling** — Oversample minority class (SMOTE) or undersample majority
3. **Cost-sensitive learning** — Modify loss function to penalize minority errors more
4. **Threshold adjustment** — Lower decision threshold for minority class

## Data Augmentation

### Computer Vision
- Geometric: rotation, flip, crop, scaling
- Color: brightness, contrast, saturation
- Mixup, CutMix, CutOut

### NLP
- Synonym replacement
- Back-translation
- Random insertion/deletion/swap
- LLM-based paraphrasing

## Data Quality Dimensions

- **Completeness** — no missing values
- **Consistency** — no contradictory records
- **Timeliness** — data reflects current reality
- **Accuracy** — data matches ground truth
- **Representativeness** — training data matches production distribution

## See Also
- [[designing-ml-systems-book]]
- [[data-distribution-shifts]] — Training/serving skew
- [[software-testing-fundamentals]] — Testing ML systems (oracle problem)
