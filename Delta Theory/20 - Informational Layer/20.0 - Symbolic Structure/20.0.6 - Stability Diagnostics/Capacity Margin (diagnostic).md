---
type: glossary
tags:
  - "#layer/information"
  - "#status/seed"
  - "#function/observation"
---

# Capacity Margin (diagnostic)

> Distance to saturation (c); headroom before throughput/latency degrade into opacity.

---

## Invariants / Thresholds (anchors)

- c: ceiling on propagation/processing
- ε: effective resolution degrades near saturation

---

## SVA Coupling

- λV can throttle to preserve margin; ψA may degrade under load; ∇S increases path load

---

## Failure Modes

- Saturation → indistinguishability; collapse of diagnostics

---

## Diagnostic Checklist

- [ ] Headroom quantified; autoscaling/circuit breaking configured
- [ ] Graceful degradation paths present

---

## Domain Mapping

- Physics: speed/throughput limits; shock capacity
- Chemistry: catalyst/enzyme turnover limits
- Biology: metabolic/throughput ceilings
- Social/Politics: administrative bandwidth; queue backlogs
- Economy: liquidity/credit capacity
- Networks: bandwidth/CPU/IO headroom
- Cognition: attention/working‑memory limits

---

## See Also

- [[Saturated Field (classification)]]


