---
type: glossary
tags:
  - "#layer/information"
  - "#status/seed"
  - "#function/observation"
---

# Stability Margin (diagnostic)

> Combined reserve across ε/ψA/λV/c that prevents collapse under expected variability.

---

## Definition

- Aggregate buffer indicating how far the system is from critical thresholds

---

## Invariants / Thresholds (anchors)

- ε: resolution headroom
- c: capacity headroom
- λV: gating headroom (noise vs starvation)
- ψA: coherence reserve (phase/memory)

---

## SVA Coupling

- ∇S affects needed reserves (higher differentiation may require more ψA/λV margin)

---

## Failure Modes

- Narrow margin → sensitivity to noise/jitter → collapse

---

## Diagnostic Checklist

- [ ] ε/c headroom quantified and sufficient
- [ ] λV hysteresis configured to prevent thrash
- [ ] ψA reserve covers recurrence intervals

---

## Dual‑register tests

- Technical: error budget (ε) and capacity (c) headroom ≥ target SLO; λV hysteresis configured; ψA covers recurrence interval
- Humane: “can we miss and recover?” tolerance present; shared rhythm holds under typical gaps; smallest meaningful issues still noticed

Depends on: [[ε — Difference Resolution Quantum (constant)]], [[c — Difference Propagation Limit (constant)]], [[λV — Void Resonance Threshold (Volozhina)]], [[ψA — Awareness Phase Coherence Anchor (Aiza)]], [[∇S — Structure Differentiation Gradient (Sarkisian)]].

## Domain Mapping

- Physics: control stability margins; safety factors
- Chemistry: tolerance to concentration/temperature variance
- Biology: homeostatic reserve; buffering capacity
- Social/Politics: institutional slack; redundancy
- Economy: capital/liquidity buffers
- Networks: SLO error budgets
- Cognition: attention/memory reserve


