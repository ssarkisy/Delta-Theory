# TRANSLATION_GUIDELINES
> Ensuring semantic fidelity across languages in Delta Theory

---

## Purpose

This document outlines how to responsibly translate Delta Theory into other languages while preserving its recursive structure, symbolic consistency, and ontological clarity.

Translations are welcome and encouraged — but they must maintain **semantic coherence** with the canonical English vault.

---

## Core Principles

### 1. Direct Translation from English Source

The **English-language vault is the canonical origin** for all theory content. Always translate directly from English to your target language to:
- Prevent amplification of distortions through translation chains
- Maintain consistent interpretation from the source
- Preserve precise meaning of technical terms
- Ensure reliable semantic anchoring

Translations should mirror the English source structurally and semantically — they are interpretive renderings, not independent forks of meaning.

### 2. Note Stability Awareness

Only translate notes marked as `#status/stable`. Unstable notes:
- May change significantly during development
- Create unnecessary maintenance burden
- Risk propagating outdated concepts
- Make it harder to maintain translation accuracy

Wait for notes to stabilize before investing in translation work.

### 3. Structural Fidelity Over Literal Equivalence

Do **not** aim for literal translations.
Aim for **recursive functional equivalence** — choose terms that preserve:

- Recursive structure
- Modulation meaning
- Ontological anchoring (Structure, Void/Cosmos, Awareness)

Example:
```markdown
English: "Void as receptive field of potential"
Russian: "Космос как принимающее поле потенциала"
```
The Russian translation uses "космос" instead of literal "пустота" to better capture the generative aspect while preserving the structural meaning.

---

## What Must Not Be Translated

| Element | Treatment |
|--------|-----------|
| **Modulator symbols** (`∇S`, `λV`, `ψA`) | Always preserve — these are canonical |
| **Term “Delta Theory”** | Do not translate — always “Delta Theory” |
| **Mathematical expressions** | Never alter formulas, variables, or notation |
| **Folder / File Names** | Use canonical English names in vault structure |
| **Primitive terms** (e.g. `Difference`, `Closure`, `Propagation`) | Use dual-language aliases with original in parentheses, e.g., "Различие (Difference)" |

---

## What Can Be Translated

| Element | Notes |
|--------|-------|
| **Body text** | Translate with care — match rhythm and recursion |
| **Quotes / examples** | May be culturally adapted if structure remains intact |
| **Glossary entries** | Use dual-language format (see below) |
| **Meta-notes** | Can include cultural reflections unique to each language |
| **README.md (localized)** | Recommended for each translation fork |
| **Interface Notes** | Serve as bridges — see below |

---

## Interface Notes (Recommended Pattern)

To aid bilingual readers and cross-referencing, create **dual-language interface notes** like this:

```markdown
---
aliases:
  - Difference
  - Различие
tags:
  - "#dual_language"
  - "#link"
  - "#russian"
  - "#status/stable"  # Only translate stable notes
version_en: "0.2.4"   # Version of English source
---

# Различие (Difference)

🇷🇺 **[[Различие]]** — это базовая единица различения в Теории Дельты...
> Примечание: В русском языке "различие" подчёркивает как сам факт отличия, так и процесс различения.

🇬🇧 **[[Difference]]** is the fundamental unit of distinction in Delta Theory...
> Note: Original English term emphasizes the state of being different.

## Cultural Bridge
- Russian: Focuses on both state and process of differentiation
- English: Emphasizes the state of distinctness
- Common Ground: Both capture the essential nature of detectable variation
````

---

## Translation Structure

Place all translated READMEs in the `README (International)` folder:

```
Delta Theory/
├── README (International)/
│   ├── README.ru.md
│   ├── README.es.md
│   └── ... (other languages)
├── README.md (English source)
└── TRANSLATION_GUIDELINES.md

Delta Theory/           (main project structure)
├── 00 - Translation Layer/
├── 10 - Implementation Layer/
└── 20 - Informational Layer/
```

Always translate directly from the English README.md. This prevents distortion chains and maintains semantic clarity.

---

## Collaborating on Translations

1. Fork the repository or create a new language folder

2. Add yourself to `CONTRIBUTORS.md` with your language

3. Join discussion threads to resolve translation ambiguity

4. Use pull requests to propose new translations


---

## Suggested Tags for Translated Notes

| Tag                        | Purpose                                   |
| -------------------------- | ----------------------------------------- |
| `#translated`              | Marks all translated notes                |
| `#dual_language`           | Notes with side-by-side bilingual content |
| `#translation_in_progress` | For draft or partially translated notes   |
| `#link`                    | For interface or glossary bridge notes    |
| `#<language>`                           | Might be useful for future repository merge                                        |

---

## License Reminder

Delta Theory is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You may freely translate and redistribute, but please:

- Credit the original author(s)

- Link to the original repository

- Preserve recursive structure


---

## Managing Changes

### Stability and Updates

1. **Check Status Tags**
   - Only translate notes marked `#status/stable`
   - Watch for status changes in English source
   - Prioritize core concepts and stable documentation
   - If a stable note becomes unstable, mark translation as needing review

2. **Version Tracking**
   - Add version number of English source to translation frontmatter:
     ```yaml
     version_en: "0.2.4"   # Version when translated
     last_sync: "2024-03-15"  # Date of last sync check
     ```
   - Update when source changes significantly
   - Add sync status to note metadata

3. **Change Management**
   - Subscribe to repository updates
   - Focus on stable core concepts first
   - Build translation gradually as content stabilizes
   - Document cultural adaptations in "Cultural Bridge" sections
   - Maintain a translation glossary for consistent term usage

## Open Translations

If you're considering starting a translation, check or open an issue:

- `delta-theory/issues#translations`

Let's stabilize difference — in every language.