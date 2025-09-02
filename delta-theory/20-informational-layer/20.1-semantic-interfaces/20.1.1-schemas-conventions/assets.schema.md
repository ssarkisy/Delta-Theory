---
type: styleguide
tags:
  - "#layer/information"
  - "#status/stable"
  - "#function/observation"
aliases:
  - "Assets (conventions)"
---

# Assets (conventions)

> Conventions for images, diagrams, code snippets, and data attachments.

## Obsidian setting

- Settings → Files & Links → Default location for new attachments → "In subfolder next to current file"
- Subfolder name: `_assets`

## Placement

- Default: keep note‑specific assets in `./_assets/` beside the note (portable; safe on refactor/move)
- Shared/reusable: store in `Delta Theory/90 - Assets/` (logos, canonical diagrams, glyphs, shared data)

## Naming

- `<note-slug>-<asset-name>-v<version>.<ext>`
- Prefer kebab‑case; increment versions for material changes

## Diagrams: source + export

- Keep the diagram source (e.g., `.drawio`, `.svg`) together with the exported image (`.png`, `.webp`) if possible
- Prefer vector (`.svg`) for diagrams/glyphs; raster only when necessary

## Promotion rule

- If an asset is reused across notes, promote it from local `./_assets/` to `90 - Assets/` and update links

## Linking examples

Markdown image (local asset):

```markdown
![diagram](./_assets/delta-ontomolecule-diagram-v1.svg)
```

Wikilink to shared asset:

```markdown
![[Delta Theory/90 - Assets/delta-glyph.svg]]
```


