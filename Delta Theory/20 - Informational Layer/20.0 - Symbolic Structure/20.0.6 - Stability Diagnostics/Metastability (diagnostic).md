---
type: glossary
tags:
  - "#layer/information"
  - "#status/stable"
  - "#function/observation"
---

# Metastability (diagnostic)

> Stable within a window; under small drift or perturbation it transitions to a different Form.

---

## Definition

- Temporary stability state
- Bounded window hold
- Transition potential
- Drift sensitivity

---

## Dual‑register mapping

### Technical (network/computational)

| Diagnostic concept | Network construct | Test example |
|-------------------|------------------|--------------|
| Window hold | State trap | `Monitor`, `Hold` |
| Drift risk | Change build | `Check`, `Drift` |
| Transition | State flip | `Test`, `Flip` |

### Humane (biological/relational)

| Diagnostic concept | Humane construct | Example |
|-------------------|------------------|----------|
| Window hold | Brief balance | "Holds for now" |
| Drift risk | Slow change | "Building up" |
| Transition | Sudden shift | "Tips over" |

### Crosswalk (bridge)

| Technical term | Humane term | Ontological meaning |
|---------------|-------------|-------------------|
| State trap | Brief balance | How hold works |
| Change build | Slow change | How drift grows |
| State flip | Sudden shift | How change tips |

### Domain Examples

| Domain | Technical test | Humane test |
|--------|---------------|-------------|
| Physics | Phase trap | Energy hold |
| Networks | State hold | Link pause |
| Cognition | Pattern trap | Mind pause |
| Systems | Flow hold | Balance point |

---

## Scale Effects

How Metastability manifests differently at various scales:

### Micro Scale (ε-bounded)

| Constant | Effect | Example |
|----------|--------|---------|
| ε | Quantum trap | Wave hold |
| λV | Gate pause | State trap |

### Human Scale (ψA-bounded)

| Constant | Effect | Example |
|----------|--------|---------|
| ψA | Phase hold | Pattern pause |
| ∇S | Structure trap | Clear hold |

### Cosmic Scale (c-bounded)

| Constant | Effect | Example |
|----------|--------|---------|
| c | Wave trap | Light hold |
| λV | Field pause | Space trap |

Note: At extreme scales, metastability faces fundamental limits (e.g., quantum tunneling at ε, causal traps at c).

---

## Invariants / Thresholds

Scale-dependent bounds:
- ε: drift tolerance
- c: hold capacity
- ψA: phase window
- λV: gate threshold

---

## SVA Coupling

Scale-dependent modulator effects:

| Scale | Modulator | Technical effect | Humane effect |
|-------|-----------|-----------------|---------------|
| Micro | ∇S | Pattern trap | Wave hold |
| Human | λV | Gate pause | Flow trap |
| Cosmic | ψA | Phase hold | Field pause |

---

## Failure Modes

Scale-dependent failure patterns:

| Scale | Mode | Technical signature | Humane signature |
|-------|------|-------------------|------------------|
| Micro | Early flip | Pattern break | Too soon |
| Human | Late hold | Stuck state | Won't change |
| Cosmic | Bad trap | Field lock | Wrong pause |

---

## Diagnostic Checklist

Technical tests:
- [ ] Window measured
- [ ] Drift tracked
- [ ] Flip predicted
- [ ] Hold timed

Humane tests:
- [ ] Balance felt
- [ ] Change sensed
- [ ] Shift ready
- [ ] Time known

---

## Design rationale

This diagnostic must maintain dual-register intelligibility per governance (see [PRINCIPLES.md](../../../../PRINCIPLES.md)). Neither technical metastability nor experiential pause alone captures its full meaning.

---

## See Also

- [[Stability Margin (diagnostic)]]
- [[Resilience (diagnostic)]]
- [[Hysteresis (diagnostic)]]
- [[Form]]
- [[Field]]

---

## Dual‑register checklist

- [x] Technical mapping provided
- [x] Humane mapping provided
- [x] Crosswalk table included
- [x] Scale-aware tests documented