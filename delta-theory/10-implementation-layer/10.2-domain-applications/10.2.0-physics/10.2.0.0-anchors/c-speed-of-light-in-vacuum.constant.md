---
type: constant
tags:
  - "#layer/implementation"
  - "#status/stable"
  - "#function/definition"
aliases:
  - c
  - Speed of Light
  - Difference Propagation Limit (physics)
  - "c — Speed of Light in Vacuum (constant)"
---

# c — Speed of Light in Vacuum (constant)

> Physical implementation of difference propagation limit.
> See [[c-difference-propagation-limit.boundary\|c — Difference Propagation Limit (boundary)]] for core conceptual meaning.

---

## Definition

- Symbol: c
- Value: 299 792 458 m/s (exact, by SI definition)
- Primary: Maximum propagation speed in vacuum
- Units: Defines the meter via distance = c × time

---

## Dual‑register mapping

Map the implementation into both registers while preserving core meaning.

### Technical (physical)

| Implementation | Physical construct | Code example |
|----------------|-------------------|--------------|
| Value | Light speed | `c = 299792458` |
| Metric | Spacetime interval | `ds^2 = -c^2dt^2 + dx^2` |
| Energy | Mass relation | `E = mc^2` |

### Humane (experiential)

| Implementation | Natural example | Experience |
|----------------|----------------|------------|
| Value | Causal horizon | "Can't go faster" |
| Metric | Light cone | "Future vs past" |
| Energy | Mass-energy | "Matter is frozen light" |

### Crosswalk (bridge)

| Physics term | Natural term | Implementation meaning |
|-------------|-------------|----------------------|
| Speed limit | Causality | How fast difference moves |
| Interval | Time flow | How events connect |
| Mass-energy | Transformation | How forms change |

---

## Implementation Details

### Primary Relations

1. **Metric definition**
   $$ds^2 = -c^2dt^2 + dx^2 + dy^2 + dz^2$$

2. **Energy relation**
   $$E = mc^2$$
   $$E^2 = p^2c^2 + m^2c^4$$

3. **Wave equation**
   $$\nabla^2\phi = \frac{1}{c^2}\frac{\partial^2\phi}{\partial t^2}$$

### Usage Guidelines

1. **Units**
   - SI: meters per second
   - Natural: c = 1
   - Specify unit system clearly

2. **Precision**
   - Exact by SI definition
   - Media have v < c
   - Check unit consistency

3. **Validation**
   - Test relativistic formulas
   - Verify causal ordering
   - Check wave solutions

---

## Scope & Constraints

- Exact in vacuum
- Media have v < c
- Defines causality

---

## Design rationale

This implementation maintains dual-register intelligibility per governance (see [PRINCIPLES.md](../../../../../../PRINCIPLES.md)). Physical precision is balanced with natural understanding.

---

## See Also

- [[c-difference-propagation-limit.boundary\|c — Difference Propagation Limit (boundary)]] (core concept)
- [[alpha-fine-structure-constant.constant\|α — Fine-Structure Constant (constant)]]
- [[10.2.0-physics.index\|10.2.0 - Physics (index)]]
