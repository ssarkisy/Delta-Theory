---
type: styleguide
tags:
  - "#layer/information"
  - "#status/stable"
  - "#function/observation"
aliases:
  - "Glossary (template)"
---

# Glossary (template)

> Streamlined template for glossary entries. Definition glossaries use core sections only; diagnostic glossaries include extended testing sections. Keep entries concise, link-first, and aligned with dual-register framing.

---

## LLM Usage Instructions

**CRITICAL:** This is template guidance - DO NOT copy instructional text into final files.

### Usage Instructions:
- **Definition glossaries** (Field, Void, Structure, Awareness): Use core sections only
- **Diagnostic glossaries** (Brittleness, Basin of Attraction, Resilience): Use core sections + diagnostic extensions
- Replace ALL `<placeholder>` text with actual content
- Remove unused sections completely rather than leaving empty
- Maintain mathematical notation and proper linking

### Section Selection by Class:
**Core Sections (All Glossaries):** Definition → Primitive Foundation → Dual-register mapping → Scale Effects → Ontological Role → Comparisons → See Also
**Diagnostic Extensions:** + Diagnostic Framework + Diagnostic Checklist

**AVOID REDUNDANCY:** Do not repeat the same concept across multiple sections. Consolidate overlapping content into unified sections.

### Current Delta Theory Glossaries:
**Definition (20.0.0):** Core terminology and foundational concepts
**Diagnostic (20.0.1-20.0.5):** Operational diagnostics with testing sections

### Header Instructions:
- **REMOVE** all parenthetical conditions like "(if derived concept)" or "(for diagnostic glossaries only)"
- **REMOVE** all italic guidance like "*DIAGNOSTIC GLOSSARIES ONLY - Remove this instruction*"
- **INCLUDE** only clean headers: "## Invariants/Thresholds" not "## Invariants/Thresholds (for diagnostic glossaries only)"

---

## Frontmatter

```
---
type: glossary
tags:
  - "#layer/information"
  - "#status/stable"
  - "#function/observation"
polarity: P+|P-|P0  # Optional
aliases:
  - <AltName>
---
```

---

## Title

`# <Term>`

> One-line definition of the concept.

---

## Definition

2-4 sentences clarifying the concept, its role in Delta Theory, and key characteristics.

---

## Primitive Foundation

*Use for terms derived from structural primitives - REMOVE this instruction in final files*

**Traceback:** How axioms, theorems, or [[delta.primitive|Delta (primitive)]] generate this concept
**Flow:** Connection to foundational operations
**Role:** What foundational elements require or generate this concept

---

## Dual-register mapping

Map the term into both registers and show the bridge explicitly.

### Technical (network/computational)

| Term concept | Network construct | Interface example |
|-------------|------------------|-------------------|
| <concept> | <technical target> | `<API example>` |

### Humane (biological/relational)

| Term concept | Humane construct | Example |
|-------------|------------------|----------|
| <concept> | <felt experience> | <lived example> |

### Crosswalk (bridge)

| Technical term | Humane term | Ontological meaning |
|---------------|-------------|-------------------|
| <tech term> | <felt term> | <shared meaning> |

---

## Scale Effects

How the term manifests differently at various scales:

### Micro Scale (ε-bounded)
- **Resolution effects:** How ε limits affect manifestation
- **Example:** <specific micro-scale behavior>

### Human Scale (ψA-bounded)
- **Coherence effects:** How ψA limits affect manifestation
- **Example:** <specific human-scale behavior>

### Cosmic Scale (c-bounded)
- **Causal effects:** How c limits affect manifestation
- **Example:** <specific cosmic-scale behavior>

**Scale transitions:** At extreme scales, terms may present as their polarity opposites due to fundamental limits.

---

## Ontological Role

| Domain | Role |
|--------|------|
| Structure | <structural role> |
| Void | <void role> |
| Awareness | <awareness role> |

Brief explanation of how the term functions within the SVA triad.

---

## Comparisons

Compare with related terms to clarify boundaries:

| This term | Related term | Key distinction |
|-----------|-------------|----------------|
| <this concept> | <other concept> | <difference> |

---

## Diagnostic Framework

*DIAGNOSTIC GLOSSARIES ONLY - Remove this instruction in final files*

**Core Detection Pattern:** <unified pattern that defines this diagnostic across all scales>

**Key Tests:**
- **<Test Type 1>:** <description of test approach>
- **<Test Type 2>:** <description of test approach>
- **<Test Type 3>:** <description of test approach>
- **<Test Type 4>:** <description of test approach>

*Note: This section consolidates what were previously separate Invariants/Thresholds, SVA Coupling, and Failure Modes sections to eliminate redundancy.*

---

## Diagnostic Checklist

*DIAGNOSTIC GLOSSARIES ONLY - Remove this instruction in final files*

**Technical tests:**
- [ ] <specific technical verification method>
- [ ] <specific technical verification method>
- [ ] <specific technical verification method>
- [ ] <specific technical verification method>

**Humane tests:**
- [ ] <specific experiential verification method>
- [ ] <specific experiential verification method>
- [ ] <specific experiential verification method>
- [ ] <specific experiential verification method>

---

## See Also

- [[flow.pattern|Flow (pattern)]] - Theoretical foundation from microkernel
- [[axiom.template|Axiom (template)]] - Axiomatic grounding
- [[delta.primitive|Delta (primitive)]] - Operational primitive connection
- [[20.0.0-glossary.index|20.0.0 - Glossary (index)]] · [[20.0.1-form-classifications.index|20.0.1 - Form Classifications (index)]] · [[20.0.2-field-classifications.index|20.0.2 - Field Classifications (index)]]
- [[20.1.0-templates.index|20.1.0 - Templates (index)]] - Parent module for navigation