---
type: glossary
tags:
  - "#layer/information"
  - "#status/stable"
  - "#function/observation"
---

# Phase Margin (diagnostic)

> ψA coherence reserve; how much phase error can be tolerated before losing lock.

---

## Definition

- Timing safety buffer
- Sync error tolerance
- Phase lock headroom
- Coherence reserve

---

## Dual‑register mapping

### Technical (network/computational)

| Diagnostic concept | Network construct | Test example |
|-------------------|------------------|--------------|
| Timing gap | Phase room | `Monitor`, `Phase` |
| Sync hold | Lock margin | `Check`, `Lock` |
| Error space | Jitter room | `Test`, `Error` |

### Humane (biological/relational)

| Diagnostic concept | Humane construct | Example |
|-------------------|------------------|----------|
| Timing gap | Rhythm space | "Stays in time" |
| Sync hold | Keeps together | "Holds sync" |
| Error space | Can slip some | "Room to drift" |

### Crosswalk (bridge)

| Technical term | Humane term | Ontological meaning |
|---------------|-------------|-------------------|
| Phase room | Rhythm space | How timing works |
| Lock margin | Keeps together | How sync holds |
| Jitter room | Can slip some | How error fits |

### Domain Examples

| Domain | Technical test | Humane test |
|--------|---------------|-------------|
| Physics | Phase lock | Time hold |
| Networks | Sync margin | Link time |
| Cognition | Mind sync | Think time |
| Systems | State time | Flow sync |

---

## Scale Effects

How Phase Margin manifests differently at various scales:

### Micro Scale (ε-bounded)

| Constant | Effect | Example |
|----------|--------|---------|
| ε | Quantum phase | Wave time |
| λV | Gate sync | State lock |

### Human Scale (ψA-bounded)

| Constant | Effect | Example |
|----------|--------|---------|
| ψA | Phase hold | Pattern time |
| ∇S | Structure sync | Clear lock |

### Cosmic Scale (c-bounded)

| Constant | Effect | Example |
|----------|--------|---------|
| c | Wave sync | Light time |
| λV | Field lock | Space phase |

Note: At extreme scales, phase margins face fundamental limits (e.g., quantum phase at ε, causal sync at c).

---

## Invariants / Thresholds

Scale-dependent bounds:
- ε: phase precision
- c: sync speed
- ψA: lock strength
- λV: gate timing

---

## SVA Coupling

Scale-dependent modulator effects:

| Scale | Modulator | Technical effect | Humane effect |
|-------|-----------|-----------------|---------------|
| Micro | ∇S | Pattern sync | Wave time |
| Human | λV | Gate phase | Flow lock |
| Cosmic | ψA | Phase hold | Field sync |

---

## Failure Modes

Scale-dependent failure patterns:

| Scale | Mode | Technical signature | Humane signature |
|-------|------|-------------------|------------------|
| Micro | Time loss | Pattern slip | Lost sync |
| Human | Lock break | Flow drift | Out of time |
| Cosmic | Phase fail | Field slip | Lost timing |

---

## Diagnostic Checklist

Technical tests:
- [ ] Phase tracked
- [ ] Lock held
- [ ] Error bounded
- [ ] Time kept

Humane tests:
- [ ] Rhythm good
- [ ] Stays together
- [ ] Can handle slip
- [ ] Time feels right

---

## Design rationale

This diagnostic must maintain dual-register intelligibility per governance (see [PRINCIPLES.md](../../../../PRINCIPLES.md)). Neither technical phase nor experiential timing alone captures its full meaning.

---

## See Also

- [[Stability Margin (diagnostic)]]
- [[Resolution Margin (diagnostic)]]
- [[Capacity Margin (diagnostic)]]
- [[Form]]
- [[Field]]

---

## Dual‑register checklist

- [x] Technical mapping provided
- [x] Humane mapping provided
- [x] Crosswalk table included
- [x] Scale-aware tests documented