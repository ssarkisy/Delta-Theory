---
type: styleguide
tags:
  - "#layer/information"
  - "#status/stable"
  - "#function/observation"
---

# Meta / Index (template)

> Use for folder/module index notes. Keep it brief, focused on organization, and clear about module purpose.

---

## Frontmatter

```
---
type: meta
tags:
  - "#layer/<translation|information|implementation>"
  - "#status/seed"
  - "#function/observation"
---
```

---

## Title

`# <code> - <Module name> (index)`

> One‑line intent of the module in the system.

---

## Module Overview

Brief explanation of:
- What this module contains
- How it fits into the larger system
- Key organizing principles

---

## Content Structure

| Category | Description | Key Elements |
|----------|-------------|--------------|
| <Category1> | <Purpose> | <Key files/concepts> |
| <Category2> | <Purpose> | <Key files/concepts> |
| <Category3> | <Purpose> | <Key files/concepts> |

Each entry should provide:
- Clear categorization
- Purpose/role in module
- Key files or concepts

---

## Core References

Primitives:
- <relevant primitives>

Anchors:
- <relevant constants>
- <relevant modulators>

Related Modules:
- <neighboring modules>
- <dependent modules>

---

## Implementation Notes

Brief notes on:
- How the module is used
- Key dependencies
- Important constraints
- Special considerations

---

## See Also

- Related modules
- Key references
- External links (if any)