---
type: glossary
tags:
  - "#layer/information"
  - "#status/stable"
  - "#function/observation"
---

# Stability Margin (diagnostic)

> Combined reserve across ε/ψA/λV/c that prevents collapse under expected variability.

---

## Definition

- Aggregate stability buffer
- Multi-factor safety margin
- Combined threshold distance
- Integrated reserve capacity

---

## Dual‑register mapping

### Technical (network/computational)

| Diagnostic concept | Network construct | Test example |
|-------------------|------------------|--------------|
| Safety margin | Error budget | `Monitor`, `Margin` |
| Reserve capacity | Load headroom | `Check`, `Load` |
| Buffer level | Resource slack | `Test`, `Buffer` |

### Humane (biological/relational)

| Diagnostic concept | Humane construct | Example |
|-------------------|------------------|----------|
| Safety margin | Room for error | "Can recover" |
| Reserve capacity | Extra strength | "Has backup" |
| Buffer level | Breathing room | "Not too tight" |

### Crosswalk (bridge)

| Technical term | Humane term | Ontological meaning |
|---------------|-------------|-------------------|
| Error budget | Room for error | How safety works |
| Load headroom | Extra strength | How reserve builds |
| Resource slack | Breathing room | How buffer helps |

### Domain Examples

| Domain | Technical test | Humane test |
|--------|---------------|-------------|
| Physics | Safety factor | Natural margin |
| Networks | SLO budget | Living buffer |
| Cognition | Memory margin | Mind space |
| Systems | Load reserve | Flow room |

---

## Scale Effects

How Stability Margin manifests differently at various scales:

### Micro Scale (ε-bounded)

| Constant | Effect | Example |
|----------|--------|---------|
| ε | Resolution margin | Wave clarity |
| λV | Gate buffer | State room |

### Human Scale (ψA-bounded)

| Constant | Effect | Example |
|----------|--------|---------|
| ψA | Phase margin | Pattern space |
| ∇S | Structure buffer | Clear room |

### Cosmic Scale (c-bounded)

| Constant | Effect | Example |
|----------|--------|---------|
| c | Wave margin | Light room |
| λV | Field buffer | Space reserve |

Note: At extreme scales, stability margins face fundamental limits (e.g., quantum uncertainty at ε, causal buffers at c).

---

## Invariants / Thresholds

Scale-dependent bounds:
- ε: resolution headroom
- c: capacity headroom
- ψA: phase reserve
- λV: gate margin

---

## SVA Coupling

Scale-dependent modulator effects:

| Scale | Modulator | Technical effect | Humane effect |
|-------|-----------|-----------------|---------------|
| Micro | ∇S | Pattern margin | Wave room |
| Human | λV | Gate reserve | Flow space |
| Cosmic | ψA | Phase buffer | Field margin |

---

## Failure Modes

Scale-dependent failure patterns:

| Scale | Mode | Technical signature | Humane signature |
|-------|------|-------------------|------------------|
| Micro | Margin loss | Pattern break | No room left |
| Human | Buffer drain | Reserve gone | Too tight |
| Cosmic | Space loss | Field break | No space |

---

## Diagnostic Checklist

Technical tests:
- [ ] Error budget met
- [ ] Load headroom good
- [ ] Resource slack held
- [ ] Margins tracked

Humane tests:
- [ ] Recovery possible
- [ ] Strength in reserve
- [ ] Room to breathe
- [ ] Space to move

---

## Design rationale

This diagnostic must maintain dual-register intelligibility per governance (see [PRINCIPLES.md](../../../../PRINCIPLES.md)). Neither technical margins nor experiential space alone captures its full meaning.

---

## See Also

- [[Robustness (diagnostic)]]
- [[Resilience (diagnostic)]]
- [[Capacity Margin (diagnostic)]]
- [[Form]]
- [[Field]]

---

## Dual‑register checklist

- [x] Technical mapping provided
- [x] Humane mapping provided
- [x] Crosswalk table included
- [x] Scale-aware tests documented