---
type: meta
tags:
  - "#layer/information"
  - "#status/stable"
  - "#function/definition"
uid: 66d38e20-f21a-4285-953d-c6d7a407585f
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
| `axiom`  | Foundational ontological truth (e.g., Difference precedes Form) |

---

### 2. Anchor Layer

| Type        | Description |
|-------------|-------------|
| `constant`  | Numeric/ratio invariant (e.g., π, e, φ) — not modulators |
| `modulator` | Canonical modulation anchors (SVA triad: ∇S, λV, ψA) |

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

| Type         | Description |
|--------------|-------------|
| `meta`       | System-level observation: structure, architecture, propagation logic |
| `glossary`   | Canonical concept definition with aliases |
| `index`      | Structural or conceptual folder map |
| `log`        | Change trace or history |
| `styleguide` | Design, naming, and formatting rules |
| `access`     | Query or link aggregation interface |
| `semantic`   | Metadata schema, tag definition, ontological markup |

---

## Structural Pattern

The type system follows a recursive prime-sequence:

- 1 core axiom type
- 2 anchor types
- 3 translation types
- 5 implementation types
- 7 informational types

This enables **minimal complexity with maximal propagation coherence** — a principle echoed across Delta Theory.

---

## Usage Guidelines

- Every note **must** include a `type:` field in the YAML frontmatter.
- The type determines its **linking logic**, **graph visibility**, and **propagation role**.
- Stability is governed by tags: use `#status/seed`, `#status/unstable`, or `#status/stable` as appropriate.

---

## See Also

- [[VAULT_STRUCTURE]]
- [[TRANSLATION_GUIDELINES]]
- [[tags]]
