---
type: meta
tags:
  - "#layer/information"
  - "#status/stable"
  - "#function/definition"
---

# Note Types in Delta Theory
> Canonical type system for recursive structuring, propagation, and reflection

---

## Purpose

This note defines the **canonical set of note types** used across the Delta Theory repository.
Each type reflects a **specific modulation role** in the recursive system, grounded in the three structural layers:

- **Translation Layer** — defines and bridges structural primitives
- **Implementation Layer** — executes recursive dynamics
- **Informational Layer** — observes, traces, and maps the system itself

Additionally, two **Anchor Types** sit outside recursion, forming the ontological grounding.

---

## Type Index

### 1. Core

| Type     | Description |
|----------|-------------|
| `axiom`  | Foundational ontological truth (e.g., A1 — Irreducibility) |
| `theorem` | Derived truth proven from axioms (e.g., T1 — Asymmetry, T2 — Recursivity) |

---

### 2. Anchor Layer

| Type        | Description |
|-------------|-------------|
| `constant`  | Mathematical invariant (e.g., π, e, φ) — derived ratios and relationships |
| `boundary`  | Operational limits (e.g., ε, c, Cs) — system constraints and thresholds |
| `modulator` | Control parameters (SVA triad: ∇S, λV, ψA) — tuning anchors |

---

### 3. Translation Layer (Structure)

| Type        | Description |
|-------------|-------------|
| `primitive` | Core metaphysical distinction (e.g., Field, Closure, Delta) |
| `interface` | Functional link between primitives (e.g., PhaseLockLoop) |
| `bridge`    | Domain concept mapped into recursive structure (e.g., Force, Voltage) |

---

### 4. Implementation Layer (Void)

| Type         | Description |
|--------------|-------------|
| `module`     | Executable recursive unit (e.g., Construct, Identity Loop) |
| `stream`     | Directed difference propagation (stream construct) |
| `seed`       | Minimal recursive stabilizer (e.g., microkernel) |
| `protocol`   | Coordination logic across modules (e.g., Synchronization) |
| `controller` | Concrete mechanism that enacts modulation (implements ∇S/λV/ψA behavior) |

---

### 5. Informational Layer (Awareness)

| Type                 | Description |
|---------------------|-------------|
| `meta`              | System-level observation: structure, architecture, propagation logic |
| `glossary`          | Canonical concept definition with aliases |
| `index`             | Structural or conceptual folder map |
| `styleguide`        | Design, naming, and formatting rules |
| `speculative_note`  | Theoretical exploration and future scenario analysis grounded in ∆-Theory principles |
| `semantic`          | Metadata schema, tag definition, ontological markup |
| `ontological_metaphor` | Deep structural metaphor that reveals recursive patterns across domains |


## Usage Guidelines

- Every note **must** include a `type:` field in the YAML frontmatter.
- The type determines its **linking logic**, **graph visibility**, and **propagation role**.
- Stability is governed by tags: use `#status/seed`, `#status/unstable`, or `#status/stable` as appropriate.

### Filename Conventions
- Use **type-based naming** with the type in parentheses at the end of the filename
- Examples: `Delta (primitive).md`, `A1 — Irreducibility (axiom).md`, `Field (glossary).md`

### Examples by Type
```markdown
# Core types
A1 — Irreducibility (axiom).md                   # type: axiom
T1 — Asymmetry (theorem).md                      # type: theorem

# Anchor layer types
π — Closure Geometry Ratio (constant).md         # type: constant
c — Difference Propagation Limit (boundary).md   # type: boundary
∇S — Structure Gradient (modulator).md           # type: modulator

# Translation layer types
Delta (primitive).md                              # type: primitive
Gate (interface).md                               # type: interface
Force (bridge).md                                 # type: bridge

# Implementation layer types
Construct (module).md                             # type: module
DifferenceStream (stream).md                      # type: stream
Microkernel (seed).md                             # type: seed

# Informational layer types
Field (glossary).md                               # type: glossary
Translation Layer (index).md                     # type: index
Yin-Yang Metaphor (ontological_metaphor).md      # type: ontological_metaphor
```

---

## See Also

- [[VAULT_STRUCTURE]]
- [[TRANSLATION_GUIDELINES]]
- [[tags]]
