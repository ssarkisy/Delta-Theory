---
type: constant
tags:
  - "#layer/implementation"
  - "#status/stable"
  - "#function/definition"
aliases:
  - ħ
  - h-bar
  - Reduced Planck Constant
  - "ħ — Reduced Planck Constant (constant)"
---

# ħ — Reduced Planck Constant (constant)

> Physical implementation of quantum of action.
> Fundamental scale of quantum phenomena.

---

## Definition

- Symbol: ħ
- Value: 1.054571817... × 10⁻³⁴ J⋅s (exact by SI)
- Primary: Quantum of action (h/2π)
- Units: Energy × time

---

## Dual‑register mapping

Map the implementation into both registers while preserving core meaning.

### Technical (physical)

| Implementation | Physical construct | Code example |
|----------------|-------------------|--------------|
| Value | Action quantum | `h/(2*pi)` |
| Phase | Wave function | `exp(iE*t/ħ)` |
| Uncertainty | Conjugate pairs | `Δx*Δp ≥ ħ/2` |

### Humane (experiential)

| Implementation | Natural example | Experience |
|----------------|----------------|------------|
| Value | Smallest change | "Can't be smaller" |
| Phase | Quantum rhythm | "Discrete beats" |
| Uncertainty | Trade-offs | "Can't know both" |

### Crosswalk (bridge)

| Physics term | Natural term | Implementation meaning |
|-------------|-------------|----------------------|
| Quantum | Step | How small changes can be |
| Phase | Rhythm | How cycles unfold |
| Uncertainty | Trade-off | How choices limit |

---

## Implementation Details

### Primary Relations

1. **Wave function**
   $$\psi(x,t) = e^{i(px - Et)/\hbar}$$

2. **Uncertainty relations**
   $$\Delta x \Delta p \geq \frac{\hbar}{2}$$
   $$\Delta E \Delta t \geq \frac{\hbar}{2}$$

3. **Commutators**
   $$[x,p] = i\hbar$$

### Usage Guidelines

1. **Units**
   - SI: joule-seconds
   - Natural: ħ = 1
   - Specify unit system

2. **Precision**
   - Exact by SI definition
   - Check quantum limits
   - Note unit consistency

3. **Validation**
   - Test uncertainty bounds
   - Verify phase relations
   - Check commutators

---

## Scope & Constraints

- Quantum scale only
- Defines measurement limits
- Sets phase quantization

---

## Design rationale

This implementation maintains dual-register intelligibility per governance (see [PRINCIPLES.md](../../../../../../PRINCIPLES.md)). Physical precision is balanced with natural understanding.

---

## See Also

- [[c-speed-of-light-in-vacuum.constant|c — Speed of Light in Vacuum (constant)]]
- [[alpha-fine-structure-constant.constant|α — Fine-Structure Constant (constant)]]
- [[10.2.0-physics.index|10.2.0 - Physics (index)]]

---

## Dual‑register checklist

- [x] Technical mapping provided
- [x] Humane mapping provided
- [x] Crosswalk table included