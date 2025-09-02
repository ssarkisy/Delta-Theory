---
type: meta
tags:
  - "#layer/information"
  - "#status/stable"
  - "#function/definition"
aliases:
  - "Note Types in Delta Theory"
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
| `axiom`  | Foundational ontological truth (e.g., A0 — Existential Difference) |
| `theorem` | Derived truth proven from axioms (e.g., T1 — Asymmetry, T2 — Irreducibility, T3 — Recursivity) |

---

### 2. Anchor Layer

| Type        | Description |
|-------------|-------------|
| `constant`  | Mathematical invariant (e.g., π, e, φ) — derived ratios and relationships |
| `boundary`  | Operational limits (e.g., ε, c, Cs) — system constraints and thresholds |
| `modulator` | Control parameters (VSA triad: λV, ∇S, ψA) — tuning anchors |

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
| `controller` | Concrete mechanism that enacts modulation (implements λV/∇S/ψA behavior) |

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
- Examples: `Delta (primitive).md`, `A0 — Existential Difference (axiom).md`, `Field (glossary).md`

### Examples by Type
```markdown
# Core types
a0-existential-difference.axiom           # type: axiom
t1-the-axiom-of-difference-propagation.theorem                 # type: theorem

# Anchor layer types
pi-closure-geometry-ratio.constant         # type: constant
c-difference-propagation-limit.boundary   # type: boundary
nabla-s-structure-sarkisian-differentiation-gradient.modulator           # type: modulator

# Translation layer types
delta.primitive                              # type: primitive
gate.interface                               # type: interface
force.bridge                                 # type: bridge

# Implementation layer types
construct.module                             # type: module
difference-stream.stream                      # type: stream
microkernel.seed                             # type: seed

# Informational layer types
field.glossary                               # type: glossary
translation-layer.index                     # type: index
yin-yang-metaphor.ontological_metaphor      # type: ontological_metaphor
```

---

## See Also

- [[VAULT_STRUCTURE.md|VAULT STRUCTURE]]
- [[TRANSLATION_GUIDELINES.md|TRANSLATION GUIDELINES]]
- [[tags.schema|Tags (conventions)]]
