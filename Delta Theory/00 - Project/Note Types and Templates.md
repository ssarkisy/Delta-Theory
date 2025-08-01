# Note Types and Templates

This file defines the core `type` and `domain` tags used in the ∆‑Theory project and provides templates or formatting guidance for each.

Each note should explicitly declare its `type` and `domain` in the YAML frontmatter:

```yaml
---
type: model
domain: 
 - physics
---
```

---

## Type System

The `type` describes the **structural role** a note plays in the theory.

|`type`|Meaning|Typical Location|
|---|---|---|
|`ontology`|Core conceptual entity (primitive or derived)|`00 – Ontology`|
|`spec`|Formal definition or logical rule (often mathematical)|`30 – Mathematics`|
|`model`|Domain-specific application or simulation|`50 – Physics`, `60 – Noetics`|
|`theorem`|Proven implication based on axioms and specs|`90 – Theorems`|
|`axiom`|Fundamental assumption, base-level principle|`00 – Ontology` or `90 – Theorems`|
|`meta`|Notes about system structure, templates, or organization|`00 – Project`|
|`glossary`|Plain-language or cross-cultural explanation of concepts|`Glossary`|
|`stub`|Placeholder for a note not yet written|Anywhere|

---

## Domain System

The `domain` defines the **context or area of application** of a note.

|`domain`|Meaning|
|---|---|
|`universal`|Applies across all domains|
|`ontology`|Resides in core ontological framework|
|`mathematics`|Pertains to formal and predicate-level structure|
|`physics`|Pertains to physical instantiations and emergent matter|
|`noetics`|Pertains to cognition, perception, mental structure|
|`meta`|Project-related, not theory content|

You may use lists for multi-domain notes:

```yaml
---
domain:
  - physics
  - noetics
---
```

---

## Templates

Each primary `type` has its own writing template:

### `ontology`

Use this for foundational concepts such as Form, Difference, Stabilization, etc.
See: [[Ontology Note Template]]

### `spec`

Use this to define operators, logical constructs, and formal conditions.
See: [[Spec Note Template]]

### `model`

Use this to describe physical, cognitive, or computational realizations.
See: [[Model Note Template]]

---

## Lightweight Types: Formatting Guidance

These types don’t require full templates but have suggested formats:

### `meta`

Used for indexes, summaries, project descriptions, roadmap notes, or file conventions.

**Recommended Structure:**
- Purpose of the note
- Scope or relevance
- Substructure summary
- Links to critical areas

### `glossary`

Used for accessible explanations of concepts or multi-language references.

**Recommended Structure:**

- Term (in original and translated form if needed)
- Concise definition
- Context of use (e.g., in a sentence)
- Optional diagram or analogy
    
### `stub`

No structure required. Should include `type: stub` and a single sentence defining the placeholder intent.

## Maintenance Notes

All notes should be classified with:

- `type` (exactly one)
- `domain` (one or more)
- `aliases` (if needed)
- `ontology` (one, for specs and models)
- `spec` (one, for ontology and models)
- `model` (one, for specs and ontology)
    
This ensures:
- Structural clarity
- Easier refactoring
- Scalable ToE-compatible mapping