---
type: styleguide
tags:
  - "#layer/information"
  - "#status/stable"
  - "#function/observation"
---

# Glossary — Diagnostic (sub-template)

> Use this for glossary entries that define classes/diagnostics with operational tests.
> Keep it short, checkable, and tied to anchors/modulators.
> Maintain dual-register mapping to show both technical and humane manifestations.

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
- Link to relevant anchors and modulators

---

## Dual‑register mapping

Map the diagnostic into both registers and show the bridge explicitly.

### Technical (network/computational)

| Diagnostic concept | Network construct | Test example |
|-------------------|------------------|--------------|
| <concept> | <technical target> | `<Test>` |
| <measure> | <metric> | `<Metric>` |
| <threshold> | <bound> | `<Check>` |

### Humane (biological/relational)

| Diagnostic concept | Humane construct | Example |
|-------------------|------------------|----------|
| <concept> | <felt experience> | <lived test> |
| <measure> | <quality> | <felt measure> |
| <threshold> | <boundary> | <natural limit> |

### Crosswalk (bridge)

| Technical term | Humane term | Diagnostic meaning |
|---------------|-------------|-------------------|
| <tech term> | <felt term> | <shared test> |
| <metric> | <quality> | <shared measure> |
| <bound> | <limit> | <shared threshold> |

### Domain Examples

| Domain | Technical test | Humane test |
|--------|---------------|-------------|
| Physics | <measurement> | <observation> |
| Networks | <metric> | <experience> |
| Cognition | <signal> | <behavior> |
| Systems | <indicator> | <pattern> |

---

## Invariants / Thresholds

Scale-dependent bounds:

### Micro Scale (ε-bounded)

| Constant | Threshold | Test |
|----------|-----------|------|
| ε | <quantum limit> | <quantum test> |
| λV | <gate threshold> | <gate test> |

### Human Scale (ψA-bounded)

| Constant | Threshold | Test |
|----------|-----------|------|
| ψA | <coherence window> | <coherence test> |
| ∇S | <structure bound> | <structure test> |

### Cosmic Scale (c-bounded)

| Constant | Threshold | Test |
|----------|-----------|------|
| c | <causal limit> | <causal test> |
| λV | <horizon bound> | <horizon test> |

---

## SVA Coupling

Scale-dependent modulator effects:

| Scale | Modulator | Technical effect | Humane effect |
|-------|-----------|-----------------|---------------|
| Micro | ∇S | <quantum structure> | <felt quantum> |
| Human | λV | <gate effect> | <felt gate> |
| Cosmic | ψA | <causal bind> | <felt bind> |

---

## Failure Modes

Scale-dependent failure patterns:

| Scale | Mode | Technical signature | Humane signature |
|-------|------|-------------------|------------------|
| Micro | Quantum | <tech failure> | <felt failure> |
| Human | System | <tech failure> | <felt failure> |
| Cosmic | Causal | <tech failure> | <felt failure> |

---

## Diagnostic Checklist

Technical tests:
- [ ] Gate conditions met at each scale
- [ ] Stability windows satisfied
- [ ] Capacity constraints respected
- [ ] Error signatures absent

Humane tests:
- [ ] Feels coherent/stable across scales
- [ ] Natural rhythm maintained
- [ ] Within comfortable bounds
- [ ] No distress signals

---

## Design rationale

This diagnostic must maintain dual-register intelligibility per governance (see [PRINCIPLES.md](../../../../PRINCIPLES.md)). Neither technical metrics nor experiential qualities alone captures its full meaning.

---

## See Also

- Related diagnostics
- Core references:
  - [[ε — Difference Resolution Quantum (constant)]]
  - [[∇S — Structure Differentiation Gradient (Sarkisian)]]
  - [[λV — Void Resonance Threshold (Volozhina)]]
  - [[ψA — Awareness Phase Coherence Anchor (Aiza)]]

---

## Dual‑register checklist

- [ ] Technical mapping provided
- [ ] Humane mapping provided
- [ ] Crosswalk table included
- [ ] Scale-aware tests documented