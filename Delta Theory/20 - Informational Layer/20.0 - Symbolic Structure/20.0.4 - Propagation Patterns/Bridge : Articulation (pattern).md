---
type: glossary
tags:
  - "#layer/information"
  - "#status/seed"
  - "#function/observation"
aliases:
  - Articulation Point
  - Bridge
---

# Bridge / Articulation (pattern)

> Critical connector whose failure isolates regions; key for both propagation and containment.

---

## Invariants / Thresholds (anchors)

- ε: minimum signal to traverse the bridge
- c: capacity limit determines bottleneck behavior

---

## SVA Coupling

- ∇S: defines partition boundaries that the bridge spans
- λV: gate can be tuned as circuit breaker
- ψA: synchronization across the bridge for stable interaction

---

## Failure Modes

- Partitioned network; amplification of bottlenecks; hotspot collapse

---

## Diagnostic Checklist

- [ ] Identify single points; add redundancy
- [ ] Gate tuning (λV) for safe operation
- [ ] Monitor load vs c and phase across sides

---

## See Also

- [[Multi‑path (redundant) (pattern)]] · [[Cascade (pattern)]] · [[Cycle (feedback loop) (pattern)]]


