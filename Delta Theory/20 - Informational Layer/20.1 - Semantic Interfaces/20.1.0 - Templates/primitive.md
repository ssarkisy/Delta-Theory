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

`# <n> (primitive)`

> One-sentence essence capturing the role of this primitive in recursion.

---

## Definition

2–4 sentences. Avoid domain-specific jargon; use vault-native terms (∆, R(·), ⊚, Field/Void/Awareness) where helpful.

---

## Dual-register mapping

Map the primitive into both registers and show the bridge explicitly.

### Technical (network/computational)

| Primitive concept | Network construct (Target) | Interface/API example |
|-------------------|----------------------------|-----------------------|
| ∆                 | Divergent event on a stream | `ChangeDetector`, `EventSource` |
| R(·)              | Topology/context graph      | `ContextGraph`, `PathSelector` |
| ⊚                 | Control/feedback closure    | `SessionCloser`, `QuorumGate` |
| F                 | Stabilized session/identity | `Session`, `IdentityTracker` |

### Humane (biological/relational)

| Primitive concept | Humane construct (Target)     | Example |
|-------------------|-------------------------------|---------|
| ∆                 | Perceptual moment (distinction)| Noticing a mismatch |
| R(·)              | Relationship/context           | Role, situation, setting |
| ⊚                 | Habit/rhythm (closure)         | Settling into a routine |
| F                 | Recognized form/identity       | "This is the pattern" |

### Crosswalk (bridge)

| Technical term  | Humane term          | Ontological meaning                    |
|-----------------|----------------------|----------------------------------------|
| Node/event      | Perceptual moment    | Distinct difference recognized         |
| Edge/topology   | Relationship/context | Difference embedded into larger whole  |
| Loop/closure    | Habit/rhythm         | Self-reinforcing stabilization         |
| Resonance       | Mutual attunement    | Stability via alignment of differences |

---

## Domain Mapping

Provide brief, concrete examples (1 line each) across domains. Use the common order: Physics, Chemistry, Biology, Social, Economy, Politics, Networks, Cognition. Include both technical and humane angles where helpful, and link to domain instances when they exist.

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

## See Also

- [[Field]]
- [[Void]]
- [[Structure]]
- [[Awareness]]
- Closely related primitives/interfaces (inline links)

---

## Dual‑register checklist

- [ ] Technical mapping provided
- [ ] Humane mapping provided
- [ ] Crosswalk table included