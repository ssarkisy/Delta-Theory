---
type: glossary
tags:
  - "#layer/information"
  - "#status/seed"
  - "#function/observation"
---

# Buffer Allocation Policy (diagnostic)

> How capacity headroom is reserved and distributed to absorb variability without entering saturation.

---

## Invariants / Thresholds (anchors)

- c: total capacity; policy targets headroom ≥ H_min
- ε: minimal batch/granularity so buffering is effective
- e: refill/decay rates for buffers (leak/refresh)

---

## SVA Coupling

- λV tunes admission vs backlog; ∇S affects where buffers sit (per‑segment vs global);
- ψA influences smoothing windows and recovery cadence

---

## Failure Modes

- Starvation (buffers too strict); oscillation (too lax); head‑of‑line blocking; hidden hotspot

---

## Diagnostic Checklist

- [ ] Headroom targets defined and monitored per critical segment
- [ ] Admission control (λV) aligned with buffer sizes
- [ ] Refill/decay rates avoid oscillation

---

## Domain Mapping

- Physics: damping reservoirs; shock absorbers
- Chemistry: buffer solutions (pH), catalyst reserve
- Biology: glycogen stores; physiological reserves
- Social/Politics: contingency budgets; staffing buffers
- Economy: liquidity/capital reserves; inventory buffers
- Networks: queue sizing; congestion window policy
- Cognition: attention slack; recovery breaks

---

## See Also

- [[Capacity Margin (diagnostic)]] · [[Stability Margin (diagnostic)]] · [[Resilience (diagnostic)]]

