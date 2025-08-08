---
type: glossary
tags:
  - "#layer/information"
  - "#status/seed"
  - "#function/observation"
aliases:
  - Chain
---

# Path (chain) (pattern)

> Single‑route propagation along a sequence of interfaces.

---

## Invariants / Thresholds (anchors)

- ε: signal must exceed threshold at each hop
- c: latency/throughput within propagation ceilings

---

## SVA Coupling

- ∇S defines partitioning; path specificity increases with ∇S
- λV gates each hop; compounded gating risk
- ψA must span the end‑to‑end recurrence interval

---

## Failure Modes

- Single‑point failure; accumulated jitter; attenuation below ε

---

## Diagnostic Checklist

- [ ] Per‑hop ε/λV satisfied
- [ ] End‑to‑end ψA window adequate
- [ ] No segment exceeds c

---

## See Also

- [[Multi‑path (redundant) (pattern)]] · [[Cycle (feedback loop) (pattern)]] · [[Cascade (pattern)]] · [[Bridge / Articulation (pattern)]]

