---
type: styleguide
tags:
  - "#layer/information"
  - "#status/stable"
  - "#function/observation"
---

# Constant (template)

> Use this template for conceptual invariants (anchors). Separate the conceptual role from domain instances; link instances for concrete values.

---

## Frontmatter

```
---
type: constant
tags:
  - "#layer/translation"   # authoring location; still an anchor type
  - "#status/seed"
  - "#function/definition"
polarity: P+|P-|P0  # Optional; set if this constant is axis-skewed (most are neutral)
aliases:  # Optional
  - <Symbol>

---
```

---

## Title

`# <Symbol> — <Conceptual name> (constant)`

> One‑line statement of the conceptual role. If numeric/dimensional, note that values live in instances.

---

## Definition (concept)

- Symbol: `<Symbol>`
- Conceptual name: `<Conceptual name>`
- Conceptual value: `conceptual` (domain instances carry numbers/units)
- Definition: minimal defining relation/limit/ratio (e.g., closure ratio; growth base)

---

## Derivation from Base Constants (if applicable)

*Include this section for constants that derive from more fundamental constants or emerge from specific primitive operations.*

**From Base Constants:** How this constant relates to fundamental constants
- Relationship to ε, π, e, φ, c or other base constants
- Mathematical derivation or operational emergence

**From Primitive Operations:** How this constant emerges from specific operations
- Connection to ∆ → R(·) → ⊚ → F flow in this domain
- Operational requirements that generate this constant

**From Domain Requirements:** What domain-specific needs generate this constant
- Domain constraints that necessitate this anchoring value
- Stability or coherence requirements that demand this constant

---

## Dual‑register mapping (concept)

Map the constant into both registers and show the bridge explicitly.

### Technical (network/computational)

| Constant concept | Network construct (Target) | Interface/API example |
|-----------------|---------------------------|----------------------|
| <concept>       | <technical target>        | `<API example>`     |

### Humane (biological/relational)

| Constant concept | Humane construct (Target) | Example |
|-----------------|---------------------------|---------|
| <concept>       | <felt experience>         | <lived example> |

### Crosswalk (bridge)

| Technical term | Humane term | Ontological meaning |
|---------------|-------------|-------------------|
| <tech term>   | <felt term> | <shared meaning>  |

---

## Domain Mapping

Brief examples across domains showing both technical and humane angles:

| Domain | Technical manifestation | Humane manifestation |
|--------|------------------------|---------------------|
| Physics | <technical example> | <experiential example> |
| Chemistry | <technical example> | <experiential example> |
| Biology | <technical example> | <experiential example> |
| Social | <technical example> | <experiential example> |
| Economy | <technical example> | <experiential example> |
| Politics | <technical example> | <experiential example> |
| Networks | <technical example> | <experiential example> |
| Cognition | <technical example> | <experiential example> |

---

## Formal identity (concept)

- Minimal defining relation(s) or limit/series, e.g.:
  - $\pi = \dfrac{C}{D}$
  - $e = \lim_{n\to\infty} \left(1 + \tfrac{1}{n}\right)^n$

---

## Anchor role

- What this constant stabilizes (geometry, growth, proportion, coherence, propagation)
- How it constrains or normalizes other quantities/flows

---

## Scope & invariance

- Domain(s) where it holds (cross‑domain vs domain‑specific)
- Known exceptions/edge interpretations (if any)
- Precision/tolerance guidance for instances

---

## Interplay with SVA (if relevant)

- How this constant interacts with ∇S / λV / ψA (if it does)

---

## Examples (concept)

- Brief, concept‑level examples (1–3 lines each) showing usage in different contexts

---

## Instances (domain bindings)

- Physics: `<link to physics instance>`
- Computing: `<link to computing instance>`
- Math/formalization: `<link to math instance>`

---

## See Also

- Related constants
- [[∇S — Structure Differentiation Gradient (Sarkisian)]]
- [[λV — Void Resonance Threshold (Volozhina)]]
- [[ψA — Awareness Phase Coherence Anchor (Aiza)]]

---

## Dual‑register checklist

- [ ] Technical mapping provided
- [ ] Humane mapping provided
- [ ] Crosswalk table included