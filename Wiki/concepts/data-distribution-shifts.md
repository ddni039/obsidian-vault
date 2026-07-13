---
title: "Data Distribution Shifts"
created: 2026-07-11
updated: 2026-07-11
type: concept
tags: [mlops, monitoring, data-quality, ml-systems]
sources: [raw/articles/designing-ml-systems-summary-2026-07-11.md]
confidence: high
---

# Data Distribution Shifts

## Definition

Data distribution shifts occur when the statistical properties of data change between training and production, causing model performance to degrade. This is one of the core challenges in deploying ML systems. From [[designing-ml-systems-book]] Ch8.

## Types of Distribution Shifts

### Covariate Shift
- **What changes:** P(X) — the input distribution changes
- **What stays:** P(Y|X) — the relationship between input and label remains the same
- **Example:** Training on summer images, deploying in winter

### Prior Probability Shift (Label Shift)
- **What changes:** P(Y) — the overall label distribution changes
- **What stays:** P(X|Y) — the relationship between label and input remains the same
- **Example:** Training on balanced classes, deploying where one class dominates

### Concept Drift
- **What changes:** P(Y|X) — the relationship between input and label changes over time
- **What stays:** P(X) — the input distribution stays roughly the same
- **Example:** Fraud patterns evolve as attackers adapt

## Monitoring Pitfalls

1. **Alert Fatigue** — too many alerts for minor fluctuations
2. **Distribution shift vs Concept drift** — require different remediation strategies
3. **Silent Failures** — model continues to serve predictions with degraded quality

## Detection Techniques

- Population Stability Index (PSI)
- Feature distribution monitoring
- Label quality monitoring
- User feedback signals

## Remediation Strategies

- Retraining with fresh data
- Online learning / continual learning
- Ensemble models for robustness
- Monitoring-driven alerts for human review

## Relationship to Other Concepts

- [[designing-ml-systems-book]] — Ch8 covers distribution shifts in depth
- [[inference-optimization]] — Monitoring is part of inference operations
- [[llmops]] — Distribution shift monitoring is a core MLOps concern

## See Also
- [[designing-ml-systems-book]]
- [[inference-optimization]]
