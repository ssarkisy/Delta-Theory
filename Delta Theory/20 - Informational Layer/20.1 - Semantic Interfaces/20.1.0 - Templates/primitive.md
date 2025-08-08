---
type: styleguide
tags:
  - "#layer/information"
  - "#status/stable"
  - "#function/observation"
uid: ae9945a5-1814-4a69-8d88-e68715a3bd24
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
aliases:  # Optional
  - <ShortName>
uid: <do not add or change, governed by Obsidian>
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

## Cross-domain examples

Keep network as primary; add quick analogies in other domains.

- Human interactions / society:
  - ∆: first “hello” or unexpected message
  - R(·): mutual friends / shared group give context
  - ⊚: both confirm plan (time/place)
  - F: an ongoing chat or a friendship forms
- Money / economy:
  - ∆: you notice a cheaper price elsewhere
  - R(·): choose exchange/broker/payment rail
  - ⊚: payment/settlement is confirmed
  - F: balance/position/contract now exists
- Cognition:
  - ∆: a surprising sound grabs attention
  - R(·): you place it in context (where/when)
  - ⊚: you commit it to memory (rehearsal/sleep)
  - F: a concept/schema you can recall later

---

## See Also

- [[Field]]
- [[Void]]
- [[Structure]]
- [[Awareness]]
- Closely related primitives/interfaces (inline links)
