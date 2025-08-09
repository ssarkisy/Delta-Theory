---
type: styleguide
tags:
  - "#layer/information"
  - "#status/stable"
  - "#function/observation"
---

# Glossary (base template)

> Use for core terms (Field, Void, Structure, Awareness, Relation, Closure, etc.).
> Keep entries concise, link‑first, and aligned with dual‑register framing.

---

## Frontmatter

```
---
type: glossary
tags:
  - "#layer/information"
  - "#status/seed"
  - "#function/observation"
polarity: P+|P-|P0  # Optional
aliases:
  - <AltName>
---
```

---

## Title

`# <Term>`

> One‑line definition.

---

## Definition

- 2–4 sentences clarifying the concept
- If applicable, relate to primitives/modulators/constants

---

## Dual‑register mapping

Map the term into both registers and show the bridge explicitly.

### Technical (network/computational)

| Term concept | Network construct | Interface example |
|-------------|------------------|-------------------|
| <concept> | <technical target> | `<API example>` |

### Humane (biological/relational)

| Term concept | Humane construct | Example |
|-------------|------------------|----------|
| <concept> | <felt experience> | <lived example> |

### Crosswalk (bridge)

| Technical term | Humane term | Ontological meaning |
|---------------|-------------|-------------------|
| <tech term> | <felt term> | <shared meaning> |

### Domain Examples

| Domain | Technical manifestation | Humane manifestation |
|--------|------------------------|---------------------|
| Physics | <technical example> | <experiential example> |
| Networks | <technical example> | <experiential example> |
| Cognition | <technical example> | <experiential example> |
| Systems | <technical example> | <experiential example> |

---

## Scale Effects

How the term manifests differently at various scales:

### Micro Scale (ε-bounded)

| Constant | Effect | Example |
|----------|--------|---------|
| ε | <resolution limit> | <manifestation> |
| λV | <interface gate> | <manifestation> |

### Human Scale (ψA-bounded)

| Constant | Effect | Example |
|----------|--------|---------|
| ψA | <coherence window> | <manifestation> |
| ∇S | <structure gradient> | <manifestation> |

### Universe Scale (c-bounded)

| Constant | Effect | Example |
|----------|--------|---------|
| c | <causal horizon> | <manifestation> |
| λV | <opacity threshold> | <manifestation> |

Note: At extreme scales, terms may present as their polarity opposites due to fundamental limits (e.g., ultra-fine structure appearing void-like due to ε, or vast fields appearing structure-like due to c).

---

## Ontological Role

| Domain | Role |
|--------|------|
| Structure | <structural role> |
| Void | <void role> |
| Awareness | <awareness role> |

Brief explanation of how the term functions within SVA triad.

---

## Comparisons

Compare with related terms to clarify boundaries:

| Term | Distinction | Example |
|------|------------|---------|
| This term | <key aspect> | <example> |
| Other term | <difference> | <example> |

---

## Design rationale

This term must maintain dual-register intelligibility per governance (see [PRINCIPLES.md](../../../../PRINCIPLES.md)). Neither technical constructs nor experiential patterns alone captures its full meaning.

---

## See Also

- Related terms
- Primitives/modulators
- Diagnostics

---

## Dual‑register checklist

- [ ] Technical mapping provided
- [ ] Humane mapping provided
- [ ] Crosswalk table included
- [ ] Scale effects documented