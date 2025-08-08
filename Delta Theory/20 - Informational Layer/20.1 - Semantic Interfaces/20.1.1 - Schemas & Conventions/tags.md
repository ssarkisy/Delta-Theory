---
type: meta
tags:
  - "#status/stable"
  - "#layer/information"
  - "#function/observation"
uid: 4ff94bbc-7697-4281-85ce-5de4ad2683c4
---

# Tag Guidelines for Delta Theory  
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

## Three Axes of Tags

Delta Theory uses **9 core tags**, distributed across **3 dimensions**:

| Axis      | Tag Prefix     | SVA Alignment | Answers...                |
|-----------|----------------|----------------|----------------------------|
| Status    | `#status/…`     | Structure       | How stable is this note?   |
| Layer     | `#layer/…`      | Void            | Where is this note located? |
| Function  | `#function/…`   | Awareness       | What is this note doing?   |

---

## Canonical Tag Set (3 × 3)

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

### Function Tags (`#function/…`)  
> Represent what kind of recursive action this note performs

| Tag                        | Meaning |
|----------------------------|---------|
| `#function/definition`     | Introduces a core concept or structural primitive |
| `#function/modulation`     | Describes recursive dynamics or operational mechanisms |
| `#function/observation`    | Reflects on structure, documents feedback, or maps relationships |

---

## Usage Guidelines

- Apply **3 tags** per note  
- Use one tag from each axis (`status/`, `layer/`, `function/`)  
- Do not duplicate YAML fields (`type:`, `domain:`) as tags  
- Use tags for **graph clarity** and **system-level diagnostics**

---

## Example Tag Triplets

| Note                         | Tags |
|------------------------------|------|
| `Electron.md`                | `#status/stable`, `#layer/implementation`, `#function/modulation` |
| `README.md`                  | `#status/stable`, `#layer/information`, `#function/observation` |
| `Closure.md` (concept note)  | `#status/unstable`, `#layer/translation`, `#function/definition` |

---

## Tags vs YAML Fields

- YAML contains **full structured metadata**  
- Tags are **graph-exposed signals**  
- Tags may **subset** fields (e.g. type, status, layer) for graph clarity  

> **All tags are fields, but not all fields are tags.**

---

## Future Tag Dimensions (Experimental)

As the system evolves, new recursive axes may be added:

- `#polarity/+`, `#polarity/–`, `#polarity/0`  
- `#anchor/root`, `#anchor/link`, `#anchor/interface`  
- `#subsystem/physics`, `#subsystem/ontology`, etc.

---

## Summary

Tags in Delta Theory serve as **recursive overlays**, aligning:

- **Structure**: `#status/…`  
- **Void**: `#layer/…`  
- **Awareness**: `#function/…`  

They let the system visualize its own propagation state.  They are not just labels. 
