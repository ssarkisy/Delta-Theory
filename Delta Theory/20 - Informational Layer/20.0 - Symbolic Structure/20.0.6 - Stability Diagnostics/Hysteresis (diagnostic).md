---
type: glossary
tags:
  - "#layer/information"
  - "#status/stable"
  - "#function/observation"
---

# Hysteresis (diagnostic)

> Different on/off thresholds to prevent thrash; path-dependent state.

---

## Definition

- Split threshold pattern
- State memory effect
- Path dependence
- Switch stability

---

## Dual‑register mapping

### Technical (network/computational)

| Diagnostic concept | Network construct | Test example |
|-------------------|------------------|--------------|
| Split level | Dual threshold | `Monitor`, `Split` |
| State memory | Path track | `Check`, `Path` |
| Switch hold | Gate lock | `Test`, `Hold` |

### Humane (biological/relational)

| Diagnostic concept | Humane construct | Example |
|-------------------|------------------|----------|
| Split level | Two points | "Different ways" |
| State memory | Remembers path | "Knows history" |
| Switch hold | Stays put | "Holds state" |

### Crosswalk (bridge)

| Technical term | Humane term | Ontological meaning |
|---------------|-------------|-------------------|
| Dual threshold | Two points | How splits work |
| Path track | Remembers path | How memory forms |
| Gate lock | Stays put | How hold works |

### Domain Examples

| Domain | Technical test | Humane test |
|--------|---------------|-------------|
| Physics | Switch gap | Energy hold |
| Networks | Gate split | Link memory |
| Cognition | Pattern hold | Mind path |
| Systems | State gap | Flow memory |

---

## Scale Effects

How Hysteresis manifests differently at various scales:

### Micro Scale (ε-bounded)

| Constant | Effect | Example |
|----------|--------|---------|
| ε | Quantum gap | Wave split |
| λV | Gate memory | State hold |

### Human Scale (ψA-bounded)

| Constant | Effect | Example |
|----------|--------|---------|
| ψA | Phase hold | Pattern memory |
| ∇S | Structure gap | Clear split |

### Cosmic Scale (c-bounded)

| Constant | Effect | Example |
|----------|--------|---------|
| c | Wave gap | Light split |
| λV | Field memory | Space hold |

Note: At extreme scales, hysteresis faces fundamental limits (e.g., quantum memory at ε, causal gaps at c).

---

## Invariants / Thresholds

Scale-dependent bounds:
- ε: gap resolution
- c: split capacity
- ψA: phase memory
- λV: gate split

---

## SVA Coupling

Scale-dependent modulator effects:

| Scale | Modulator | Technical effect | Humane effect |
|-------|-----------|-----------------|---------------|
| Micro | ∇S | Pattern gap | Wave split |
| Human | λV | Gate memory | Flow hold |
| Cosmic | ψA | Phase split | Field memory |

---

## Failure Modes

Scale-dependent failure patterns:

| Scale | Mode | Technical signature | Humane signature |
|-------|------|-------------------|------------------|
| Micro | Gap loss | Pattern flip | No memory |
| Human | Bad hold | State thrash | Won't stay |
| Cosmic | Split fail | Field flip | Lost hold |

---

## Diagnostic Checklist

Technical tests:
- [ ] Split levels set
- [ ] Path tracked
- [ ] Hold stable
- [ ] Gap sized

Humane tests:
- [ ] Points clear
- [ ] History kept
- [ ] State holds
- [ ] Space right

---

## Design rationale

This diagnostic must maintain dual-register intelligibility per governance (see [PRINCIPLES.md](../../../../PRINCIPLES.md)). Neither technical hysteresis nor experiential memory alone captures its full meaning.

---

## See Also

- [[Stability Margin (diagnostic)]]
- [[Metastability (diagnostic)]]
- [[Resilience (diagnostic)]]
- [[Form]]
- [[Field]]

---

## Dual‑register checklist

- [x] Technical mapping provided
- [x] Humane mapping provided
- [x] Crosswalk table included
- [x] Scale-aware tests documented