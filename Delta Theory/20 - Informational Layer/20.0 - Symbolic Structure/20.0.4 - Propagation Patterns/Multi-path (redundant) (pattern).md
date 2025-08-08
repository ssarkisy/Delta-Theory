---
type: glossary
tags:
  - "#layer/information"
  - "#status/seed"
  - "#function/observation"
---

# Multi‑path (redundant) (pattern)

> Parallel routes provide redundancy and higher resilience.

---

## Invariants / Thresholds (anchors)

- ε: aggregate signal above threshold despite individual path variance
- c: load sharing keeps each path within capacity

---

## SVA Coupling

- ∇S enables parallelization (partitioning)
- λV per path; diversity reduces gating risk
- ψA aligns merged results; requires reconciliation window

---

## Failure Modes

- Correlated failures; merge conflicts; hidden single points (shared bridges)

---

## Diagnostic Checklist

- [ ] Paths are independent enough (low correlation)
- [ ] Load balancing avoids saturation
- [ ] Merge phase window sufficient

---

## See Also

- [[Path (chain) (pattern)]] · [[Cycle (feedback loop) (pattern)]] · [[Bridge / Articulation (pattern)]]


