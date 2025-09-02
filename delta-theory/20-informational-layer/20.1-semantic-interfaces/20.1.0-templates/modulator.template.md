---
type: styleguide
tags:
  - "#layer/information"
  - "#status/stable"
  - "#function/observation"
aliases:
  - "Modulator (template)"
---

# Modulator (template)

> Template for microkernel modulators using sublayer-based architecture. All modulators are fundamental SVA control parameters (∇S, λV, ψA). Capture definition, base constants, coupling, and dual‑register mapping.

---

## LLM Usage Instructions

**CRITICAL:** This is template guidance - DO NOT copy instructional text into final files.

### Section Selection:
- **All modulators** (∇S, λV, ψA): Use sections up to "See Also" only - extended operational sections have been removed

### Header Instructions:
- **REMOVE** all parenthetical conditions like "(if derived modulator)"
- **REMOVE** all italic guidance and template instructions
- **INCLUDE** only clean headers without conditional text

### Content Instructions:
- Replace ALL `<placeholder>` text with actual content
- Remove unused sections completely rather than leaving empty
- Maintain mathematical notation and proper linking

### Examples of CORRECT Final Headers:
```markdown
## Primitive Derivation          ← CORRECT (clean)
## Domain Mapping               ← CORRECT (clean)
## Formal identity              ← CORRECT (clean)
```

### Examples of INCORRECT Final Headers:
```markdown
## Primitive Derivation (if derived modulator)          ← WRONG (includes condition)
*Use for modulators derived from primitives*            ← WRONG (includes instruction)
```

---

## Frontmatter

```
---
type: modulator
tags:
  - "#layer/translation"
  - "#sublayer/microkernel"
  - "#status/seed"
  - "#function/modulation"
polarity: P+|P-|P0  # P+ for ∇S, P- for λV, P0 for ψA
derivation: A0+T1+T2+T3  # All modulators derive from foundational axiom and theorems
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

## Modulator Guidance

### Microkernel Modulators (#sublayer/microkernel)
- **Nature:** Fundamental SVA control parameters
- **Examples:** ∇S (Structure Differentiation), λV (Void Resonance), ψA (Awareness Phase Coherence)
- **Derivation:** Direct from axiom and theorems (A0, T1, T2, T3)
- **Location:** Microkernel level (00.0.3)
- **Context:** Universal control parameters for all recursive operations
- **Complete set:** Only three modulators exist - the SVA triad

---

## Primitive Derivation

*Use for modulators derived from primitives or microkernel modulators - REMOVE this instruction in final files*

**Traceback:** [[delta.primitive|Delta (primitive)]] → [[relational-embedding.primitive|RelationalEmbedding (primitive)]] → [[stabilization-closure.primitive|Stabilization (Closure) (primitive)]] → F — why primitive operations require this modulation

**Flow:** How ∆ → R(·) → ⊚ operations generate modulation needs
**Core:** From ∇S, λV, ψA (if applicable)
**Control:** What variations this modulator manages

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

## Dependencies

**Constants:** <list relevant constants> (<brief purpose for each>)
**Role:** <P+/P-/P0> modulator controlling <primary function> in SVA triad

---

## Conditions / Invariants

- Coupling rules, thresholds, failure modes

---

## See Also

- [[field.glossary|Field (glossary)]]
- [[void.glossary|Void (glossary)]]
- [[structure.glossary|Structure (glossary)]]
- [[awareness.glossary|Awareness (glossary)]]
- [[epsilon-difference-resolution-quantum.boundary|ε — Difference Resolution Quantum (boundary)]] · [[c-difference-propagation-limit.boundary|c — Difference Propagation Limit (boundary)]] · [[pi-closure-geometry-ratio.constant|π — Closure Geometry Ratio (constant)]] · [[e-natural-transformation-rate.constant|e — Natural Transformation Rate (constant)]] · [[phi-asymmetric-stabilization-ratio.constant|φ — Asymmetric Stabilization Ratio (constant)]]
- [[nabla-s-structure-differentiation-gradient.modulator|∇S — Structure (Sarkisian) Differentiation Gradient (modulator)]] · [[lambda-v-void-resonance-threshold.modulator|λV — Void (Volozhina) Resonance Threshold (modulator)]] · [[psi-a-awareness-phase-coherence-anchor.modulator|ψA — Awareness (Aiza) Phase Coherence Anchor (modulator)]]

---

