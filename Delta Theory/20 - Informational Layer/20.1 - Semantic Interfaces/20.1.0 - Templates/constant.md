---
type: styleguide
tags:
  - "#layer/information"
  - "#status/stable"
  - "#function/observation"
uid: c5a3a2c1-2d8d-4d04-9c7a-8b6a21e1d9f0
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
aliases:  # Optional
  - <Symbol>
uid: <uuid>
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

## References

- Source(s) or canonical definitions (brief links or citations)

---

## Instances (domain bindings)

- Physics: `<link to physics instance>`
- Computing: `<link to computing instance>`
- Math/formalization: `<link to math instance>`

---

## See Also

- Related constants
- [[∇S — Sarkisian Differentiation Gradient (Structure)]]
- [[λV — Volozhina Resonance Threshold (Void)]]
- [[ψA — Aiza Phase Coherence Anchor (Awareness)]]
