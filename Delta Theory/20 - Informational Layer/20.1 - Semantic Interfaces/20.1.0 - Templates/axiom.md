---
type: styleguide
tags:
  - "#layer/information"
  - "#status/stable"
  - "#function/observation"
---

# Axiom (template)

> Use for foundational ontological truths. Keep statements minimal and independent; move consequences to Implications.

---

## Frontmatter

```
---
type: axiom
tags:
  - "#layer/translation"
  - "#status/seed"
  - "#function/definition"
polarity: P+|P-|P0  # Optional; only if the axiom is framed from a specific axis perspective
aliases:  # Optional
  - <Short name>

---
```

---

## Title

`# A<n> — <Short name> (axiom)`

> One‑line canonical statement.

---

## Primitive Derivation (if derived axiom)

*Include this section only if this axiom derives from structural primitives or higher-level axioms. For foundational axioms (A1-A3), this section is not needed.*

Explain how this axiom emerges from the structural primitive flow (∆ → R(·) → ⊚ → F) when applied to the specific domain:

**From ∆ (Difference):** How difference detection applies in this domain
- $∆_{domain}$ = specific type of distinction relevant to this axiom
- What differences seed the axiom's requirements

**From R(·) (Relational Embedding):** How context shapes the axiom
- $R(∆_{domain})$ embeds differences in domain-specific relational context
- Context requirements that lead to the axiom

**From ⊚ (Stabilization):** How closure requirements generate the axiom
- $⊚(R(∆_{domain}))$ = stable pattern that must be maintained
- Closure conditions that necessitate the axiom

**From F (Form):** How stable forms require this axiom
- $F_{domain}$ = domain forms that depend on this axiom
- Form integrity requirements that mandate the axiom

---

## Statement

- Precise axiom wording (single bullet or short paragraph)

---

## Dual‑register mapping

Map the axiom into both registers and show the bridge explicitly.

### Technical (network/computational)

| Axiom concept | Network construct (Target) | Interface/API example |
|---------------|---------------------------|----------------------|
| <concept 1> | <technical target> | `<API example>` |
| <concept 2> | <technical target> | `<API example>` |
| <concept 3> | <technical target> | `<API example>` |

### Humane (biological/relational)

| Axiom concept | Humane construct (Target) | Example |
|---------------|---------------------------|---------|
| <concept 1> | <felt experience> | <lived example> |
| <concept 2> | <emotional resonance> | <embodied example> |
| <concept 3> | <intuitive knowing> | <heart-centered example> |

### Crosswalk (bridge)

| Technical term | Humane term | Ontological meaning |
|---------------|-------------|-------------------|
| <tech term> | <felt term> | <shared meaning> |
| <tech term> | <felt term> | <shared meaning> |
| <tech term> | <felt term> | <shared meaning> |

---

## Domain Mapping

Provide brief, concrete consequences (1 line each) across domains. Use the common order: Physics, Chemistry, Biology, Social, Economy, Politics, Networks, Cognition. Include both technical and humane angles where helpful, and link to domain examples when they exist.

---

## Register note (if governance)

- If this is a repository/theory governance principle (not kernel axiom), mark it as such and link from README/Onboarding.

---

## Rationale (context)

- Brief motivation and where it anchors in the theory (do not prove the axiom)

---

## Dependencies & scope

- Independent of: <list or "none">
- Applies to: primitives / embeddings / closure operations

---

## Implications / derivations (selected)

- Immediate consequences this axiom enables (list; keep concise)

---

## Related structures

- Primitives: [[Delta]] · [[RelationalEmbedding]] · [[Stabilization (Closure)]] · [[Form]]
- Constants: link to conceptual anchors if relevant (ε, π, e, φ, c)
- Modulators: ∇S / λV / ψA if influenced

---

## Dual‑register checklist

- [ ] Technical mapping provided
- [ ] Humane mapping provided
- [ ] Crosswalk table included

---

## See Also

- [[00.0.0.0 - Core Axioms (index)]]