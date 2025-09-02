---
type: meta
tags:
  - "#status/stable"
  - "#layer/information"
  - "#function/observation"
aliases:
  - "Tags (conventions)"
---

# Tags (conventions)
> Tags as recursive diagnostics — seeing ∆ through structure, phase, and role

---

## Why Tags Exist

In Delta Theory, **tags are not cosmetic**.
They serve as **recursive overlays** for:

- Navigating the vault via Obsidian’s graph view
- Diagnosing propagation status of each note
- Categorizing notes by their recursive **layer**, **phase**, and **function**
- Enabling future indexing, search, and filtering via tools like Dataview

Tags are **the visible echo of the invisible structure**.

---

## Four Axes of Tags

Delta Theory uses **tags** distributed across **4 dimensions**:

| Axis      | Tag Prefix     | VSA Alignment | Answers...                |
|-----------|----------------|----------------|----------------------------|
| Status    | `#status/…`     | Structure       | How stable is this note?   |
| Layer     | `#layer/…`      | Void            | Where is this note located? |
| Sublayer  | `#sublayer/…`   | Void (refined)  | Which specific sublayer?   |
| Function  | `#function/…`   | Awareness       | What is this note doing?   |

---

## Canonical Tag Set

### Status Tags (`#status/…`)
> Represent a note’s **temporal phase** in recursive stabilization

| Tag                  | Description |
|----------------------|-------------|
| `#status/seed`       | Note has just been created or drafted |
| `#status/unstable`   | Actively evolving; major ideas or structures still changing |
| `#status/stable`     | Recursive modulation has slowed below threshold `ε_note` (see below) |

> Stability is not finality.
> A note is stable when its change rate is low enough to be self-sustaining.

**By default**, a note becomes `stable` if:
- It hasn’t been modified for **21+ days**,
- AND no active issues or open questions remain.

This reflects recursive **damping**: when external difference has been absorbed into internal coherence.

---

### Layer Tags (`#layer/…`)
> Represent the structural position of a note within the recursive architecture

| Tag                      | Meaning |
|--------------------------|---------|
| `#layer/translation`     | Defines structural primitives and abstractions |
| `#layer/implementation`  | Executes recursive difference via folding and modulation |
| `#layer/information`     | Observes, documents, or reflects recursive processes |

---

### Sublayer Tags (`#sublayer/…`)
> Represent the specific sublayer within each major layer

**Translation Layer Sublayers:**
| Tag                      | Meaning |
|--------------------------|---------|
| `#sublayer/microkernel`  | Pure mathematical foundations (axioms, constants, primitives, patterns) |
| `#sublayer/interface`    | Environment interfaces (theorems, primitives, operational patterns) |
| `#sublayer/coherence`    | Coherence orchestration (temporal coordination, stability management) |

**Implementation Layer Sublayers:**
| Tag                      | Meaning |
|--------------------------|---------|
| `#sublayer/kernel`       | Delta kernel implementation (recursive execution logic) |
| `#sublayer/formalization`| Mathematical formalization (mathematical encoding of recursion) |
| `#sublayer/application`  | Domain applications (use in real systems and sciences) |

**Informational Layer Sublayers:**
| Tag                      | Meaning |
|--------------------------|---------|
| `#sublayer/symbolic`     | Symbolic structure (glossary, constants, naming systems) |
| `#sublayer/semantic`     | Semantic interfaces (contributor docs, access maps, metadata) |
| `#sublayer/trace`        | Recursive trace (changelog, epistemology, memory scaffolds) |

---

### Function Tags (`#function/…`)
> Represent what kind of recursive action this note performs

| Tag                        | Meaning |
|----------------------------|---------|
| `#function/definition`     | Introduces a core concept or structural primitive |
| `#function/modulation`     | Describes recursive dynamics or operational mechanisms |
| `#function/observation`    | Reflects on structure, documents feedback, or maps relationships |

---

## Usage Guidelines

- Apply **4 tags** per note
- Use one tag from each axis (`status/`, `layer/`, `sublayer/`, `function/`)
- Do not duplicate YAML fields (`type:`, `domain:`) as tags
- Use tags for **graph clarity** and **system-level diagnostics**

---

## Example Tag Quadruplets

| Note                         | Tags |
|------------------------------|------|
| `pi-closure-geometry-ratio.constant` | `#status/stable`, `#layer/translation`, `#sublayer/microkernel`, `#function/definition` |
| `gate.primitive`        | `#status/stable`, `#layer/translation`, `#sublayer/interface`, `#function/definition` |
| `README.md`                  | `#status/stable`, `#layer/information`, `#sublayer/semantic`, `#function/observation` |
| `memory.primitive`      | `#status/seed`, `#layer/translation`, `#sublayer/coherence`, `#function/definition` |

---

## Tags vs YAML Fields

- YAML contains **full structured metadata**
- Tags are **graph-exposed signals**
- Tags may **subset** fields (e.g. type, status, layer) for graph clarity

> **All tags are fields, but not all fields are tags.**

---

## Future Tag Dimensions (Experimental)

As the system evolves, new recursive axes may be added. Polarity is now standardized as a YAML field with optional tags:

- YAML field (canonical): `polarity: P+|P-|P0` (Void=P-, Structure=P+, Awareness=P0)
- Optional tags (for graph filters): `#polarity/P+`, `#polarity/P-`, `#polarity/P0`
- `#anchor/root`, `#anchor/link`, `#anchor/interface`
- `#subsystem/physics`, `#subsystem/ontology`, etc.

---

## Summary

Tags in Delta Theory serve as **recursive overlays**, aligning:

- **Structure**: `#status/…`
- **Void**: `#layer/…` + `#sublayer/…`
- **Awareness**: `#function/…`

They let the system visualize its own propagation state.  They are not just labels.
