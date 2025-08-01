---
aliases:
  - Operator Index
  - ∆‑Math Signature Table
  - Core FRONT Operators
  - Operator Specification Map
tags:
  - #∆‑Mathematics
  - #Operators
  - #Spec
---

# MetaOperators — Core Signatures of ∆‑Mathematics

This table defines the **core operators of FRONT** as **functional mappings** — from difference to form, from instability to stabilization, from recursion to collapse. Each entry provides:

- A symbolic **signature**
- A **description** of what the operator does
- A reference to the **canonical definition**
- Space for specifying **preconditions** and **exceptions** (expandable)

This meta-layer helps unify all symbolic reasoning in ∆‑Mathematics and prepares the system for simulation, validation, or logic modeling.

---

## 🧮 Operator Table

| Operator         | Signature                                 | Meaning                                              | Definition Note |
|------------------|-------------------------------------------|------------------------------------------------------|-----------------|
| `∆`              | —                                         | Primitive unit of **ontological distinction**         | [[PrimitiveDifference]] |
| `R`              | `∆ → R(∆)`                                | **Embeds** a difference into a relational context     | [[RelationalEmbedding]] |
| `⊚`              | `R(∆) → F` (if stable)                    | **Stabilizes** a relational difference                | [[StabilizationOperator]] |
| `F := ⊚(R(∆))`   | `∆ → F`                                   | **Form as stabilized relation**                      | [[Form]] |
| `Rⁿ(∆₀)`         | `∆₀ → Fₙ` via recursive embedding         | **Recursive structuring** of difference               | [[RecursiveEmbedding]] |
| `Loop(Fₙ)`       | `Fₙ → F₀` (if closure holds)              | **Recursive cycle** — returns to prior difference     | [[RecursiveClosure]] |
| `Collapse(Fₙ)`   | `Fₙ → ∅` (if stability fails)             | **Breakdown** of stabilized form                      | [[FormCollapse]] |
| `PhaseLock(Fₙ)`  | `Fₙ × τ → Loop(Fₙ)`                       | **Synchronization** that sustains recursive loop      | *To create: `PhaseLock.md`* |
| `restore(∆ⱼ)`    | `∆ⱼ → ∆ᵢ` (via memory)                    | **Reconstructs** past difference in current context   | [[Restore]] |

---

## 🧩 Operator Roles by Type

### Ontological Primitives
- `∆` — irreducible difference
- `R` — embedding into context
- `⊚` — condition for persistence
- `F` — realization of stable difference

### Recursive Mechanics
- `Rⁿ(∆₀)` — structuring across depth
- `Loop(Fₙ)` — recursive return
- `PhaseLock` — phase alignment to sustain structure
- `restore(∆)` — memory-based restoration

### Collapse & Transition
- `Collapse(Fₙ)` — destabilization / boundary crossing
- `⊚Field(x)` (in calculus) — extrinsic modulator of stabilization

---

## 🔗 See Also

- [[30.0 – Core Operators & Axioms]]
- [[30.1 – Structural Constructs]]
- [[30.2 – ∆‑Field Calculus]]
- [[30.3 – Delta Topology]]
- [[StabilityConditions]]
- [[StructuralMemory]]
