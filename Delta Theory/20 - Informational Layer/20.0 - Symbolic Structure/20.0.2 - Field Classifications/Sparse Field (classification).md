---
type: glossary
tags:
  - "#layer/information"
  - "#status/seed"
  - "#function/observation"
---

# Sparse Field (classification)

> Under‑sampled or under‑resolved regime in which differences fall below ε and fail to register.

---

## Definition

- Sampling/resolution too low; many signals are sub‑ε
- Interfaces present but cannot accumulate enough evidence for closure

---

## Invariants / Thresholds (anchors)

- ε: resolution below phenomenon scale
- λV: gating too strict; drops marginal but informative signals

---

## SVA Coupling

- ∇S too low → boundaries blur; too high → misses global context
- ψA windows too short to bind sparse events

---

## Failure Modes

- False negatives; misclassification as “Zero”; inability to stabilize

---

## Diagnostic Checklist

- [ ] Increase resolution/sampling; do forms emerge?
- [ ] Relax λV briefly; does signal appear?
- [ ] Extend observation window (ψA); does identity bind?

---

## See Also

- [[Transparent Field (classification)]] · [[Masked Field (classification)]] · [[Saturated Field (classification)]]
- [[Field]] · [[Void]]
- [[Resolution Margin (diagnostic)]]

