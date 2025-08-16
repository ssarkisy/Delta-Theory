---
type: styleguide
tags:
  - "#layer/information"
  - "#status/stable"
  - "#function/observation"
---

# Primitive (template)

> Unified template for all primitive types using sublayer-based architecture. Microkernel primitives use basic sections only; interface and coherence primitives include extended operational sections. Keep notes small, link-first, and versionable.

---

## LLM Usage Instructions

**CRITICAL:** This is template guidance - DO NOT copy instructional text into final files.

### Section Selection by Sublayer:
- **Microkernel primitives** (∆, R(·), ⊚): Use sections up to "See Also" only
- **Interface primitives** (Port, Gate, Surface): Use ALL sections including extended ones
- **Coherence primitives** (Memory, Phase, Recovery): Use ALL sections including extended ones

### Header Instructions:
- **REMOVE** all parenthetical conditions like "(if specialized primitive)" or "(for interface primitives only)"
- **REMOVE** all italic guidance like "*INTERFACE PRIMITIVES ONLY - Remove this instruction*"
- **INCLUDE** only the clean header: "## Interface Operations" not "## Interface Operations (for interface primitives only)"

### Content Instructions:
- Replace ALL `<placeholder>` text with actual content
- Remove unused sections completely rather than leaving empty
- For interface primitives, populate extended sections with actual interface-specific content
- For coherence primitives, populate extended sections with actual coherence-specific content
- Maintain mathematical notation and proper linking

### Examples of CORRECT Final Headers:
```markdown
## Primitive Derivation          ← CORRECT (clean)
## Interface Operations          ← CORRECT (clean)
## Modulator Effects            ← CORRECT (clean)
```

### Examples of INCORRECT Final Headers:
```markdown
## Primitive Derivation (if specialized primitive)     ← WRONG (includes condition)
## Interface Operations (for interface primitives only) ← WRONG (includes condition)
*Use this section only for class: interface primitives* ← WRONG (includes instruction)
```

---

## Frontmatter

```
---
type: primitive
tags:
  - "#layer/translation"
  - "#sublayer/microkernel"  # or "#sublayer/interface" or "#sublayer/coherence"
  - "#status/seed"
  - "#function/definition"
polarity: P+|P-|P0  # Required for interface/coherence primitives; optional for microkernel primitives
derivation: A1|T1|T2|T3|T4|T5|T6|T7|T8  # Source axiom or theorem
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

## Sublayer-Specific Guidance

### For Microkernel Primitives (#sublayer/microkernel)
- **Nature:** Foundational mathematical operations
- **Examples:** ∆ (Difference), R(·) (Relational Embedding), ⊚ (Stabilization)
- **Derivation:** Direct from axioms and theorems (A1, T1, T2)
- **Location:** Microkernel level (00.0.4)
- **No operational context:** Pure mathematical relationships

### For Interface Primitives (#sublayer/interface)
- **Nature:** Applied operational capabilities for field interaction
- **Examples:** Port (flow control), Gate (threshold evaluation), Surface (boundary adjustment)
- **Derivation:** From interface theorems applied to microkernel primitives
- **Location:** Interface level (00.1.2)
- **Operational context:** Include Interface Operations, Modulator Effects, Implementation Guidelines

### For Coherence Primitives (#sublayer/coherence)
- **Nature:** Applied operational capabilities for temporal/informational coherence
- **Examples:** Memory (information preservation), Phase (temporal synchronization), Recovery (stability restoration)
- **Derivation:** From coherence theorems applied to microkernel primitives
- **Location:** Coherence level (00.2.4)
- **Operational context:** Include Interface Operations, Modulator Effects, Implementation Guidelines

---

## Primitive Derivation

*Use for primitives derived from microkernel ∆, R(·), ⊚ operations - REMOVE this instruction in final files*

**Traceback:** `∆ → R(·) → ⊚ → F` — how this specializes the core flow

**Core:** Which primitive (∆, R(·), ⊚) this extends
**Domain:** What functional needs require this specialization
**Interface:** How this addresses coordination requirements

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

## Dependencies

**Derivation:** <Source axiom/theorem> - <brief explanation>
**Role:** Operates in <Structure/Void/Awareness> aspect of SVA triad

---

## Conditions / Invariants

- Key invariants or thresholds
- Failure modes (if relevant)

---

---

## Interface Operations

*INTERFACE AND COHERENCE PRIMITIVES ONLY - Remove this instruction in final files*

### Core Functions

| Operation | Technical Implementation | Humane Implementation |
|-----------|------------------------|---------------------|
| <Operation 1> | `primitive.<method>(params)` | <humane description> |
| <Operation 2> | `primitive.<method>(params)` | <humane description> |
| <Operation 3> | `primitive.<method>(params)` | <humane description> |
| <Operation 4> | `primitive.<method>(params)` | <humane description> |

### Control Parameters

| Parameter | Technical Control | Humane Control | <Primary Modulator> Effect |
|-----------|------------------|---------------|---------------------------|
| <Parameter 1> | <technical aspect> | <humane aspect> | <modulator effect description> |
| <Parameter 2> | <technical aspect> | <humane aspect> | <modulator effect description> |
| <Parameter 3> | <technical aspect> | <humane aspect> | <modulator effect description> |
| <Parameter 4> | <technical aspect> | <humane aspect> | <modulator effect description> |

---

## Domain Manifestations

*INTERFACE AND COHERENCE PRIMITIVES ONLY - Remove this instruction in final files*

| Domain | Technical manifestation | Humane manifestation |
|--------|------------------------|---------------------|
| Physics | <technical example> | <experiential example> |
| Chemistry | <technical example> | <experiential example> |
| Biology | <technical example> | <experiential example> |
| Social | <technical example> | <experiential example> |
| Economy | <technical example> | <experiential example> |
| Politics | <technical example> | <experiential example> |
| Networks | <technical example> | <experiential example> |
| Cognition | <technical example> | <experiential example> |

---

## Stability Conditions

*INTERFACE AND COHERENCE PRIMITIVES ONLY - Remove this instruction in final files*

- **<Condition 1>:** <Description of what must remain stable>
- **<Condition 2>:** <Description of what must remain stable>
- **<Condition 3>:** <Description of what must remain stable>
- **<Condition 4>:** <Description of what must remain stable>

---

## Modulator Effects

*INTERFACE AND COHERENCE PRIMITIVES ONLY - Remove this instruction in final files*

### <Primary Modulator Symbol> (<Primary Modulator Full Name>)
- **High <symbol>:** <Effect description for high values>
- **Low <symbol>:** <Effect description for low values>

### <Secondary Modulator Symbol> (<Secondary Modulator Full Name>)
- <Effect description and control mechanism>

### <Tertiary Modulator Symbol> (<Tertiary Modulator Full Name>)
- <Effect description and influence on primitive>

---

## Implementation Guidelines

*INTERFACE AND COHERENCE PRIMITIVES ONLY - Remove this instruction in final files*

```
<PrimitiveName> Interface:
- <operation_1>(parameters) → <return_type>
- <operation_2>(parameters) → <return_type>
- <operation_3>(parameters) → <return_type>
- configure(<config_params>)
```

### Error Conditions
- **<Error Type 1>:** <Description and cause>
- **<Error Type 2>:** <Description and cause>
- **<Error Type 3>:** <Description and cause>
- **<Error Type 4>:** <Description and cause>

---

## Related Primitives

*INTERFACE AND COHERENCE PRIMITIVES ONLY - Remove this instruction in final files*

- **Sequence:** <Interface/Coherence primitive sequence description>
- **Controls:** <How this primitive affects others>
- **Dependencies:** <What this primitive depends on>

---

## Constants Integration

*INTERFACE AND COHERENCE PRIMITIVES ONLY - Remove this instruction in final files*

### For Interface Primitives:
- **Primary constant:** <κ_discrimination/ι_identity/σ_conservation> - <timing constraint description>
- **Supporting constants:** <Other interface constants> - <coordination description>
- **Implementation requirement:** <Timing bounds and operational constraints>

### For Coherence Primitives:
- **Primary constants:** <r_temporal/r_memory/r_stability/γ_retention/δ_recovery> - <timing/efficiency constraint description>
- **Supporting constants:** <Other coherence constants> - <coordination description>
- **Implementation requirement:** <Timing bounds and operational constraints>

---

## See Also

- [[Field (glossary)]]
- [[Void (glossary)]]
- [[Structure (glossary)]]
- [[Awareness (glossary)]]
- Closely related primitives/interfaces (inline links)

---

