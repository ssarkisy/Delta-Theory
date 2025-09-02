---
type: constant
tags:
  - "#layer/implementation"
  - "#status/stable"
  - "#function/definition"
aliases:
  - α
  - Alpha
  - Fine Structure Constant
  - "α — Fine-Structure Constant (constant)"
---

# α — Fine Structure Constant (constant)

> Physical implementation of electromagnetic coupling.
> Dimensionless measure of interaction strength.

---

## Definition

- Symbol: α
- Value: 1/137.035999084... (dimensionless)
- Primary: Electromagnetic coupling strength
- Units: None (pure number)

---

## Dual‑register mapping

Map the implementation into both registers while preserving core meaning.

### Technical (physical)

| Implementation | Physical construct | Code example |
|----------------|-------------------|--------------|
| Value | Coupling strength | `e^2/(ħ*c)` |
| Structure | Energy levels | `E_n ∝ α^2` |
| Interaction | QED vertex | `√α` per vertex |

### Humane (experiential)

| Implementation | Natural example | Experience |
|----------------|----------------|------------|
| Value | Connection strength | "How strongly linked" |
| Structure | Pattern detail | "Fine features" |
| Interaction | Influence reach | "Effect strength" |

### Crosswalk (bridge)

| Physics term | Natural term | Implementation meaning |
|-------------|-------------|----------------------|
| Coupling | Connection | How things affect each other |
| Structure | Pattern | How details emerge |
| Vertex | Meeting | How influences combine |

---

## Implementation Details

### Primary Relations

1. **Definition**
   $$\alpha = \frac{e^2}{\hbar c} \approx \frac{1}{137}$$

2. **Energy levels**
   $$E_n = -mc^2\frac{\alpha^2}{2n^2}$$

3. **QED expansion**
   $$\text{amplitude} \propto \sum (\sqrt{\alpha})^n$$

### Usage Guidelines

1. **Value**
   - Use measured value
   - Note uncertainty
   - Check unit cancellation

2. **Precision**
   - Known to ~10⁻¹⁰
   - May vary with energy
   - Test convergence

3. **Validation**
   - Check spectral lines
   - Verify QED series
   - Test running coupling

---

## Scope & Constraints

- Electromagnetic only
- Energy dependent
- Perturbative regime

---

## Design rationale

This implementation maintains dual-register intelligibility per governance (see [PRINCIPLES.md](../../../../../../PRINCIPLES.md)). Physical precision is balanced with natural understanding.

---

## See Also

- [[c-speed-of-light-in-vacuum.constant\|c — Speed of Light in Vacuum (constant)]]
- [[h-reduced-planck-constant.constant\|ħ — Reduced Planck Constant (constant)]]
- [[10.2.0-physics.index\|10.2.0 - Physics (index)]]
