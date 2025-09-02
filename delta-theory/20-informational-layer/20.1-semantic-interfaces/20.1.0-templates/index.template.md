---
type: styleguide
tags:
  - "#layer/information"
  - "#status/stable"
  - "#function/observation"
aliases:
  - "Index (template)"
---

# Index (template)

> Use this template for module index files that provide overview and navigation for collections of related content.

---

## LLM Usage Instructions

**CRITICAL:** This is template guidance - DO NOT copy instructional text into final files.

### Usage Instructions:
- Replace ALL `<placeholder>` text with actual content
- Remove unused sections completely rather than leaving empty
- Keep overview concise and focused on module purpose
- Include clear navigation links to module contents
- Avoid duplicating content that exists in individual files

### Section Requirements:
**Core Sections (All Index Files):** Module Overview → Content Structure → Core References → See Also
**Optional Extensions:** Key Principles (for foundational modules), Implementation Notes (for practical modules)

### Template vs Final File Example:

**IN TEMPLATE:**
```markdown
## Module Overview

<Brief description of what this module contains and its role in the larger system>
```

**IN FINAL FILE:**
```markdown
## Module Overview

Constants represent the mathematical relationships that emerge necessarily from the foundational axioms and theorems.
```

---

## Frontmatter

```
---
type: meta
tags:
  - "#layer/translation"   # or appropriate layer
  - "#sublayer/microkernel"  # or appropriate sublayer
  - "#status/stable"
  - "#function/observation"
---
```

---

## Title

`# <Module Number> - <Module Name> (index)`

> One-line description of module purpose and scope.

**Derivation Trace:** (if applicable) [[delta.primitive|Delta (primitive)]] → [[axiom.template|Axiom (template)]] → [[t1-asymmetry.theorem|T1 — Asymmetry (theorem)]]/[[t2-irreducibility.theorem|T2 — Irreducibility (theorem)]]/[[t3-recursivity.theorem|T3 — Recursivity (theorem)]] → <module contents>

---

## Module Overview

<Brief description of what this module contains and its role in the larger system>

<Description of what each item in the module provides>:
- **<Property 1>** description
- **<Property 2>** description
- **<Property 3>** description
- **<Property 4>** description

---

## Content Structure

| <Item> | <Classification> | <Role> | <Key Property> |
|--------|-----------------|--------|----------------|
| [[axiom.template\|Axiom (template)]] | <type/derivation> | <purpose> | <distinguishing feature> |
| [[theorem.template\|Theorem (template)]] | <type/derivation> | <purpose> | <distinguishing feature> |
| [[primitive.template\|Primitive (template)]] | <type/derivation> | <purpose> | <distinguishing feature> |

<Additional explanatory text if needed about classification or patterns>

---

## Core References

<Category>:
- [[<Item 1>]]
- [[<Item 2>]]
- [[<Item 3>]]

<Related Category> (if applicable):
- [[<Related Item 1>]]
- [[<Related Item 2>]]

Related Modules:
- [[<Related Module 1>]]
- [[<Related Module 2>]]
- [[<Related Module 3>]]

---

## Key Principles

*Optional section for foundational modules with important conceptual insights*

1. **<Principle 1>**
   - <Key point 1>
   - <Key point 2>
   - <Key point 3>

2. **<Principle 2>**
   - <Key point 1>
   - <Key point 2>

3. **<Principle 3>**
   - <Key point 1>
   - <Key point 2>

<Link to additional guidance if needed>

---

## Implementation Notes

*Optional section for practical/operational modules*

Brief notes on:
- How the module is used
- Key dependencies
- Important constraints
- Special considerations

---

## See Also

- [[20.1.0-templates.index|20.1.0 - Templates (index)]]
- [[axiom.template|Axiom (template)]]
- [[theorem.template|Theorem (template)]]
- [[primitive.template|Primitive (template)]] · [[pattern.template|Pattern (template)]] · [[glossary.template|Glossary (template)]]
