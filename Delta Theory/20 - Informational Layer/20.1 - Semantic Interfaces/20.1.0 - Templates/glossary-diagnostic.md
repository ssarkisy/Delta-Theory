---
type: styleguide
tags:
  - "#layer/information"
  - "#status/stable"
  - "#function/observation"
---

# Glossary — Diagnostic (sub-template)

> Use this for glossary entries that define classes/diagnostics with operational tests. Keep it short, checkable, and tied to anchors/modulators.

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
aliases:  # Optional
  - <AltName>
---
```

---

## Title

`# <Name>`

> One‑line definition emphasizing the diagnostic criterion (what is tested and why it matters).

---

## Definition

- 2–4 sentences clarifying the concept
- State the observable condition(s) that distinguish this class/diagnostic

---

## Invariants / Thresholds (anchors)

- Tie explicitly to anchors where applicable (ε, π, e, φ, c)
- Specify quantitative/qualitative bounds (e.g., |∆| ≥ ε; phase jitter ≤ ε)

---

## SVA Coupling

- How ∇S (Structure), λV (Void), ψA (Awareness) modulate this diagnostic

---

## Failure Modes

- Collapse conditions, fragmentation, desynchronization, starvation, overload, etc.

---

## Diagnostic Checklist

- [ ] Gate condition(s) met?
- [ ] Stability/coherence window satisfied?
- [ ] Capacity constraints respected (ε, c, etc.)?
- [ ] Expected failure signatures absent?

---

## Application Diagnostics Mapping

- Physics: <observable tests>
- Networks/Control: <metrics, alarms>
- Cognition: <behavioral or timing tests>
- Economy/Other: <analogous signals>

---

## See Also

- Related glossary entries or classifications
- Core references: [[ε — Difference Resolution Quantum (constant)]], [[∇S — Structure Differentiation Gradient (Sarkisian)]], [[λV — Void Resonance Threshold (Volozhina)]], [[ψA — Awareness Phase Coherence Anchor (Aiza)]]


