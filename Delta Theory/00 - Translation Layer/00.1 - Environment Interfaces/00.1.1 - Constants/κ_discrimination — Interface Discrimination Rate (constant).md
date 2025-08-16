---
type: constant
tags:
  - "#layer/translation"
  - "#sublayer/interface"
  - "#status/stable"
  - "#function/definition"
polarity: P+
derivation: T3
aliases:
  - κ_discrimination
  - Interface Discrimination Rate
  - Selective Permeability Constant
---

# κ_discrimination — Interface Discrimination Rate (constant)

> **Mathematical invariant for interface discrimination operations** — the fundamental rate at which interfaces can make stable discrimination decisions while maintaining selective permeability coherence.

---

## Definition

- Symbol: `κ_discrimination`
- Conceptual name: `Interface Discrimination Rate`
- Conceptual value: `conceptual` (domain instances carry numbers/units)
- Definition: minimal stable interval between discrimination decisions required for selective permeability coherence

---

## Primitive Derivation

**Theorem Source:** T3 (Interface Discrimination) — "Interfaces must discriminate between flows"

**Derivation Logic:**
1. **T3 Requirement:** Discrimination must be consistent across similar contexts
2. **Temporal Implication:** Consistent discrimination requires minimum decision interval
3. **Mathematical Necessity:** κ_discrimination emerges as this minimal stable interval
4. **Invariant Nature:** Represents fundamental timing constraint for discrimination coherence

**Traceback:** `A1 → T1 → T3 → κ_discrimination` — why discrimination requires this rate invariant

**Flow:** T3 demands consistent selective permeability → requires stable discrimination timing → κ_discrimination emerges as timing invariant for discrimination coherence

---

## Dual‑register mapping

### Technical (network/computational)

| Constant concept | Network construct | Interface example |
|------------------|------------------|-------------------|
| Discrimination interval | Decision latency | `FilterLatency`, `ACLProcessTime` |
| Selectivity rate | Throughput control | `SelectionRate`, `PermissionHz` |
| Coherence timing | Consistency window | `DecisionWindow`, `StableInterval` |

### Humane (biological/relational)

| Constant concept | Humane construct | Example |
|------------------|------------------|---------|
| Discrimination interval | Decision pause | "Time needed to choose wisely" |
| Selectivity rate | Thoughtful filtering | "How quickly I can discern quality" |
| Coherence timing | Consistent judgment | "Maintaining fairness in decisions" |

### Crosswalk (bridge)

| Technical term | Humane term | Ontological meaning |
|---------------|-------------|-------------------|
| Decision latency | Decision pause | Time required for stable discrimination |
| Throughput control | Thoughtful filtering | Rate of selective permeability |
| Consistency window | Consistent judgment | Prevention of discrimination conflicts |

---

## Domain Mapping

| Domain | Technical manifestation | Humane manifestation |
|--------|------------------------|---------------------|
| Physics | Molecular selectivity timing | Natural filtering processes |
| Chemistry | Catalytic discrimination rates | Chemical selection processes |
| Biology | Ion channel selectivity timing | Cellular discrimination processes |
| Social | Group admission decisions | Community boundary maintenance |
| Economy | Market access control | Economic filtering mechanisms |
| Politics | Policy discrimination timing | Institutional selection processes |
| Networks | Packet filtering latency | System access control |
| Cognition | Attention filtering rates | Conscious discrimination processes |

---

## Formal identity

$$κ_{discrimination} = δt_{min}(discrimination\_decision)$$

where $δt_{min}$ ensures discrimination decision coherence

---

## Anchor role

- **Discrimination Stabilization:** Anchors the temporal scale for selective permeability decisions
- **Consistency Constraint:** Ensures discrimination decisions remain coherent across contexts
- **Coherence Normalization:** Provides consistent timing reference for filtering operations

---

## Scope & invariance

- **Domain:** Cross-domain constant applicable wherever interface discrimination must be stable
- **Invariance:** Conceptual ratio holds across all discrimination implementations
- **Precision:** Domain instances determine specific timing values and decision latencies
- **Scaling:** Rate may scale with discrimination complexity and accuracy requirements

---

## Mathematical Properties

### Expression
```
κ_discrimination ∈ ℝ⁺
κ_discrimination > 0 (positive definite)
∂κ_discrimination/∂t = 0 (time-invariant)
```

### Relationships
- **Lower bound:** Must allow discrimination completion
- **Upper bound:** Must maintain interface responsiveness
- **Stability:** Constant across discrimination contexts

### Operational Constraints
- **Primitive operations** must respect κ_discrimination timing
- **Pattern operations** aggregate within κ_discrimination bounds
- **Modulator effects** cannot violate κ_discrimination requirements

---

## Implementation Notes

### Usage in Interface Operations
- **Port operations:** Flow admission decisions must respect κ_discrimination
- **Gate operations:** Threshold evaluations must respect κ_discrimination
- **Surface operations:** Boundary adjustments must respect κ_discrimination

### Relationship to Other Constants
- **Microkernel foundation:** Built upon difference propagation timing (related to c)
- **Coherence extension:** Extended by coherence constants for temporal operations
- **Pattern constraints:** Provides timing foundation for pattern operations

### Violation Consequences
- **Too fast:** Discrimination decisions become incoherent/conflicting
- **Too slow:** Interface becomes unresponsive/non-functional
- **Variable:** Interface behavior becomes unpredictable

---

## Relationship to Other Principles

### Foundation Theorems
- **T3 (Discrimination):** Direct source - provides mathematical expression of discrimination requirement
- **T1 (Asymmetry):** Provides foundation for discrimination necessity
- **A1 (Irreducibility):** Ensures discrimination cannot be eliminated

### Supporting Principles
- **T4 (Identity):** Discrimination timing affects identity maintenance
- **T5 (Conservation):** Discrimination decisions must preserve flow conservation

### Higher-Level Extensions
- **T6 (Temporal Continuity):** Extends discrimination into temporal coherence
- **Interface Primitives:** Use κ_discrimination as timing foundation
- **Interface Patterns:** Aggregate discrimination operations within this constraint

---

## Instances (domain bindings)

*Placeholder for future domain-specific implementations with concrete values*

- Physics: [Future: molecular discrimination timing values]
- Computing: [Future: packet filtering and access control rates]
- Biology: [Future: cellular selectivity intervals]

---

## Architecture Examples

**Real-world interfaces where κ_discrimination defines discrimination decision timing:**

### **Network Security**
- **Firewalls:** Packet classification and filtering decisions (typically 1-10 milliseconds)
- **Identity:** Protocol analysis, threat detection, access rule evaluation

### **Access Control Systems**
- **API Gateways:** Request authentication and authorization (typically 10-100 milliseconds)
- **Identity:** User credentials, permission evaluation, rate limiting decisions

### **Load Balancing**
- **Traffic Distribution:** Server selection and routing decisions (typically 1-5 milliseconds)
- **Identity:** Health checks, capacity assessment, routing algorithm evaluation

### **Data Processing**
- **Stream Processing:** Event filtering and classification (typically 0.1-1 milliseconds)
- **Identity:** Data quality assessment, schema validation, routing decisions

### **Quality Control**
- **Content Moderation:** Message/content filtering decisions (typically 50-500 milliseconds)
- **Identity:** Content analysis, policy compliance, safety assessment

### **Resource Management**
- **CPU Schedulers:** Process priority and resource allocation (typically 0.01-1 milliseconds)
- **Identity:** Process characteristics, resource requirements, priority assessment

**κ_discrimination Application:** Defines the minimum time required between discrimination decisions to maintain coherent selectivity. Faster decisions → inconsistent filtering. Slower decisions → system unresponsiveness.

---

## See Also

- [[T3 — Interface Discrimination (theorem)]] (source theorem)
- [[ι_identity — Interface Identity Rate (constant)]] (complementary interface constant)
- [[σ_conservation — Interface Conservation Rate (constant)]] (complementary interface constant)
- [[00.1.2 - Interface Primitives (index)]] (implementation consumers)

