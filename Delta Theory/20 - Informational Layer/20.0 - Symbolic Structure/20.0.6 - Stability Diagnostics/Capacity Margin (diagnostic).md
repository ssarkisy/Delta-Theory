---
type: glossary
tags:
  - "#layer/information"
  - "#status/stable"
  - "#function/observation"
---

# Capacity Margin (diagnostic)

> Distance to saturation (c); headroom before throughput/latency degrade into opacity.

---

## Definition

- Load headroom measure
- Saturation distance
- Throughput reserve
- Processing margin

---

## Dual‑register mapping

### Technical (network/computational)

| Diagnostic concept | Network construct | Test example |
|-------------------|------------------|--------------|
| Load room | Usage gap | `Monitor`, `Load` |
| Peak handle | Max capacity | `Check`, `Peak` |
| Flow space | Rate margin | `Test`, `Flow` |

### Humane (biological/relational)

| Diagnostic concept | Humane construct | Example |
|-------------------|------------------|----------|
| Load room | Space left | "Room to grow" |
| Peak handle | Can handle | "Takes more" |
| Flow space | Easy move | "Flows free" |

### Crosswalk (bridge)

| Technical term | Humane term | Ontological meaning |
|---------------|-------------|-------------------|
| Usage gap | Space left | How room works |
| Max capacity | Can handle | How peaks work |
| Rate margin | Easy move | How flow works |

### Domain Examples

| Domain | Technical test | Humane test |
|--------|---------------|-------------|
| Physics | Speed limit | Force room |
| Networks | Load cap | Link space |
| Cognition | Mind space | Think room |
| Systems | Flow cap | Move space |

---

## Scale Effects

How Capacity Margin manifests differently at various scales:

### Micro Scale (ε-bounded)

| Constant | Effect | Example |
|----------|--------|---------|
| ε | Quantum room | Wave space |
| λV | Gate cap | State room |

### Human Scale (ψA-bounded)

| Constant | Effect | Example |
|----------|--------|---------|
| ψA | Phase space | Pattern room |
| ∇S | Structure cap | Clear space |

### Cosmic Scale (c-bounded)

| Constant | Effect | Example |
|----------|--------|---------|
| c | Wave cap | Light room |
| λV | Field space | Space cap |

Note: At extreme scales, capacity faces fundamental limits (e.g., quantum capacity at ε, causal limits at c).

---

## Invariants / Thresholds

Scale-dependent bounds:
- ε: resolution room
- c: speed margin
- ψA: phase space
- λV: gate capacity

---

## SVA Coupling

Scale-dependent modulator effects:

| Scale | Modulator | Technical effect | Humane effect |
|-------|-----------|-----------------|---------------|
| Micro | ∇S | Pattern room | Wave space |
| Human | λV | Gate margin | Flow cap |
| Cosmic | ψA | Phase cap | Field room |

---

## Failure Modes

Scale-dependent failure patterns:

| Scale | Mode | Technical signature | Humane signature |
|-------|------|-------------------|------------------|
| Micro | Space loss | Pattern full | No room |
| Human | Cap hit | Flow block | Too much |
| Cosmic | Room gone | Field full | No space |

---

## Diagnostic Checklist

Technical tests:
- [ ] Load tracked
- [ ] Peaks handled
- [ ] Flow smooth
- [ ] Space kept

Humane tests:
- [ ] Room feels good
- [ ] Can take more
- [ ] Moves easy
- [ ] Space clear

---

## Design rationale

This diagnostic must maintain dual-register intelligibility per governance (see [PRINCIPLES.md](../../../../PRINCIPLES.md)). Neither technical capacity nor experiential space alone captures its full meaning.

---

## See Also

- [[Stability Margin (diagnostic)]]
- [[Resolution Margin (diagnostic)]]
- [[Phase Margin (diagnostic)]]
- [[Form]]
- [[Field]]

---

## Dual‑register checklist

- [x] Technical mapping provided
- [x] Humane mapping provided
- [x] Crosswalk table included
- [x] Scale-aware tests documented