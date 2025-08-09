---
type: styleguide
tags:
  - "#layer/information"
  - "#status/stable"
  - "#function/observation"
---

# Modulator (template)

> Use for SVA modulators (∇S, λV, ψA). Capture definition, base constants, coupling, and dual‑register mapping.

---

## Frontmatter

```
---
type: modulator
tags:
  - "#layer/translation"
  - "#status/seed"
  - "#function/modulation"
polarity: P+|P-|P0
aliases:
  - <ShortName>
---
```

---

## Title

`# <Symbol> — <n> (<Eponym>)`

> One‑line function: what it modulates and why it matters.

---

## Definition

- Core modulation behavior (2–4 sentences)
- How it shifts thresholds/phase/depth

---

## Dual‑register mapping

### Technical (network/computational)

| Modulator (axis) | Network construct (Target) | Interface/API example |
|------------------|----------------------------|-----------------------|
| <symbol> (S/V/A) | …                          | …                     |

### Humane (biological/relational)

| Modulator (axis) | Humane construct (Target) | Example |
|------------------|---------------------------|---------|
| <symbol> (S/V/A) | …                         | …       |

### Crosswalk (bridge)

| Technical term | Humane term | Ontological meaning |
|----------------|-------------|---------------------|
| <tech term>    | <felt term> | <shared meaning>   |

---

## Domain Mapping

Provide brief, concrete examples (1 line each) across domains. Use the common order: Physics, Chemistry, Biology, Social, Economy, Politics, Networks, Cognition. Include both technical and humane angles where helpful, and link to domain instances when they exist.

- Physics: <short, concrete>
- Chemistry: <short, concrete>
- Biology: <short, concrete>
- Social: <short, concrete>
- Economy: <short, concrete>
- Politics: <short, concrete>
- Networks: <short, concrete>
- Cognition: <short, concrete>

---

## Formal identity

- Global modulation line and any specific relations

---

## Base constants (core dependencies)

- ε / π / e / φ / c — specify which and how

---

## Role in the loop

- Where (S/V/A) and what it enables

---

## Conditions / Invariants

- Coupling rules, thresholds, failure modes

---

## See Also

- [[Field]]
- [[Void]]
- [[Structure]]
- [[Awareness]]
- Related constants and modulators
- Related primitives or interfaces

---

## Dual‑register checklist

- [ ] Technical mapping provided
- [ ] Humane mapping provided
- [ ] Crosswalk table included