---
type: constant
tags:
  - "#layer/implementation"
  - "#status/stable"
  - "#function/definition"
aliases:
  - k_B
  - Boltzmann Constant
  - Thermal Energy Scale
---

# k_B — Boltzmann Constant (constant)

> Physical implementation of thermal energy scale.
> Links temperature to energy and entropy.

---

## Definition

- Symbol: k_B
- Value: 1.380649... × 10⁻²³ J/K (exact by SI)
- Primary: Temperature-energy conversion
- Units: Energy per temperature

---

## Dual‑register mapping

Map the implementation into both registers while preserving core meaning.

### Technical (physical)

| Implementation | Physical construct | Code example |
|----------------|-------------------|--------------|
| Value | Energy scale | `k_B * T` |
| Distribution | Boltzmann factor | `exp(-E/k_B*T)` |
| Entropy | State counting | `S = k_B*ln(W)` |

### Humane (experiential)

| Implementation | Natural example | Experience |
|----------------|----------------|------------|
| Value | Heat measure | "How hot it feels" |
| Distribution | Natural spread | "Things mix" |
| Entropy | Disorder growth | "Things spread out" |

### Crosswalk (bridge)

| Physics term | Natural term | Implementation meaning |
|-------------|-------------|----------------------|
| Temperature | Heat | How energy flows |
| Distribution | Mixing | How states spread |
| Entropy | Disorder | How order decays |

---

## Implementation Details

### Primary Relations

1. **Energy scale**
   $$E = k_B T$$

2. **Boltzmann distribution**
   $$P(E) \propto e^{-E/k_B T}$$

3. **Entropy relation**
   $$S = k_B \ln W$$

### Usage Guidelines

1. **Units**
   - SI: joules per kelvin
   - Natural: k_B = 1
   - Specify unit system

2. **Precision**
   - Exact by SI definition
   - Check thermal limits
   - Note unit consistency

3. **Validation**
   - Test distributions
   - Verify entropy laws
   - Check energy scales

---

## Scope & Constraints

- Thermal systems only
- Statistical interpretation
- Macroscopic limit

---

## Design rationale

This implementation maintains dual-register intelligibility per governance (see [PRINCIPLES.md](../../../../../../PRINCIPLES.md)). Physical precision is balanced with natural understanding.

---

## See Also

- [[c — Speed of Light in Vacuum (constant)]]
- [[ħ — Reduced Planck Constant (constant)]]
- [[10.2.0 - Physics (index)]]

---

## Dual‑register checklist

- [x] Technical mapping provided
- [x] Humane mapping provided
- [x] Crosswalk table included