---
type: styleguide
tags:
  - "#layer/information"
  - "#status/stable"
  - "#function/observation"
---

# Primitive (template)

> Use this template for core primitives in the Translation Layer. Keep notes small, link-first, and versionable.

---

## Frontmatter

```
---
type: primitive
tags:
  - "#layer/translation"
  - "#status/seed"
  - "#function/definition"
polarity: P+|P-|P0  # Optional; set if axis-scoped (Structure=P+, Void=P-, Awareness=P0)
aliases:  # Optional
  - <ShortName>

---
```

---

## Title

`# <Name> (primitive)`

> One-sentence essence capturing the role of this primitive in recursion.

---

## Definition

2–4 sentences. Avoid domain-specific jargon; use vault-native terms (∆, R(·), ⊚, Field/Void/Awareness) where helpful.

---

## Formal identity (if applicable)

- Minimal relation(s) or operator identity, e.g.:
  - $F := ⊚(R(∆))$
  - $F_n := ⊚(R^n(∆_0))$

---

## Role in the loop

- Where it acts: Structure / Void / Awareness
- What it modulates or enables

---

## Conditions / Invariants

- Key invariants or thresholds
- Failure modes (if relevant)

---

## Network mapping

Map the primitive concept to concrete network constructs and (if available) interfaces/APIs.

| Primitive concept | Network construct (Target) | Interface/API example |
|-------------------|----------------------------|-----------------------|
| ∆                 | Divergent event on a stream | `ChangeDetector`, `EventSource` |
| R(·)              | Topology/context graph      | `ContextGraph`, `PathSelector` |
| ⊚                 | Control/feedback closure    | `SessionCloser`, `QuorumGate` |
| F                 | Stabilized session/identity | `Session`, `IdentityTracker` |

---

## Domain Mapping

Keep network as primary; add quick analogies in other domains. Suggested ordering: Physics, Chemistry, Biology, Social, Economy, Politics, Networks, Cognition.

---

## See Also

- [[Field]]
- [[Void]]
- [[Structure]]
- [[Awareness]]
- Closely related primitives/interfaces (inline links)
