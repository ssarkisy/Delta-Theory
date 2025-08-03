---
type: meta
domain:
  - meta
aliases:
  - knowledge architecture
  - note types
  - file structure
  - naming convention
  - traceability rules
  - file taxonomy
---

# Knowledge Base Architecture — ∆‑Theory Structural Framework

This note defines the **core file types, naming conventions, domain tags, and traceability rules** that structure the ∆‑Theory Knowledge Base. Its purpose is to ensure **clarity, modularity, and scalable coherence** across Ontology, Property, Construct, Spec, Model, and Meta layers.


## 1. Core Note Types & Structural Roles

|Type|Purpose|Typical Location|
|---|---|---|
|`ontology`|Foundational primitives, recursive structures, functional configurations.|`10 – Ontology`|
|`property`|Qualifying attributes modulating Ontology structures.|Within `10.3 – Properties`|
|`construct`|Functional configurations synthesized from Properties.|`10.4 – Constructs`|
|`taxonomy`|Classification systems (Forms, Fields, Chains).|`10.5 – Diagnostic Classifications`|
|`spec`|Formal operators, predicates, rules, metrics, generators.|`30 – Mathematics`|
|`model`|Domain-specific realizations (physics, cognition, systems).|`50 – Physics`, `60 – Noetics`, `70 – Systems`|
|`axiom`|Irreducible theoretical principles.|`10 – Ontology` or `90 – Theorems`|
|`theorem`|Formal derivations from axioms and specs.|`90 – Theorems`|
|`meta`|Project-level architecture, organizational notes.|`00 – Project`|
|`glossary`|Plain-language explanations and cross-domain interpretations.|`Glossary`|
|`stub`|Placeholders for undeveloped notes.|Anywhere.|


## 2. Domain Tags

|Domain|Purpose|
|---|---|
|`ontology`|Foundational structures of difference propagation.|
|`mathematics`|Formal logic, structural operators, and evaluative predicates.|
|`physics`|Physical domain realizations (matter, energy fields).|
|`noetics`|Cognitive structures, self-referential loops, perception dynamics.|
|`systems`|Complex systems, feedback behaviors, networked structures.|
|`meta`|Organizational and architectural project notes.|

### Multi-Domain Notes Example:

```yaml
domain:
  - ontology
  - mathematics
  - physics
```


## 3. Filename Conventions

|Aspect|Rule|
|---|---|
|Spaces|Use PascalCase (FormStabilization.md) or Natural Case (Form Stabilization.md).|
|Type Suffix|Always in `(parentheses)` — e.g., `(spec)`, `(physics)`.|
|Domain Tags|Applied only in Model filenames to specify the realization domain.|
|Stub Suffix|Use `(stub)` to mark placeholders.|
|Naming Consistency|Filename stems remain identical across Ontology ↔ Spec ↔ Model chains.|



## 4. Frontmatter Structure by Note Type

### Universal Fields (All Notes)

```yaml
---
type: [ontology / property / construct / taxonomy / spec / model / axiom / theorem / meta / glossary / stub]
domain: [ontology / mathematics / physics / noetics / systems / meta]
aliases:
  - optional alias1
  - optional alias2
---
```

### Spec Notes

```yaml
---
type: spec
spec_type: operator / predicate / rule / metric / generator
ontology: "[[LinkedOntology]]"
model:
  - "[[LinkedModel]]"
---
```

### Model Notes

```yaml
---
type: model
ontology: "[[LinkedOntology]]"
spec: "[[LinkedSpec]]"
domain:
  - physics / noetics / systems
---
```

### Property Notes

```yaml
---
type: property
ontology: "[[LinkedOntology]]"
spec: "[[LinkedSpec]]"  # Optional if formalized
---
```

### Construct Notes

```yaml
---
type: construct
ontology: "[[LinkedOntology]]"
properties:
  - "[[LinkedProperty1]]"
  - "[[LinkedProperty2]]"
spec:
  - "[[LinkedSpec]]"  # Optional if formalized
---
```


## 5. Spec Suffixes & Functional Role Tags

|Spec Type|Suffix Example|Purpose|
|---|---|---|
|`operator`|`DifferencePropagationOperator (spec).md`|Structural transformation operator.|
|`predicate`|`FormStabilizationPredicate (spec).md`|Boolean evaluation condition.|
|`rule`|`CollapsePropagationRule (spec).md`|Declarative logic or inference rule.|
|`metric`|`StabilizationGradientMetric (spec).md`|Quantitative measurement or scalar output.|
|`generator`|`FormChainGenerator (spec).md`|Constructive process logic for structure creation.|


## 6. Traceability Link Rules

|From|Must Link To|Purpose|
|---|---|---|
|Ontology|Linked Specs, Derived Ontologies|Clarifies formal operational context.|
|Property|Linked Ontology, optional Spec|Defines qualification attributes and evaluation pathways.|
|Construct|Linked Ontology, enabling Properties, optional Spec|Defines functional synthesis configurations.|
|Spec|Linked Ontology, Linked Models|Defines operational scope and domain instantiation.|
|Model|Linked Ontology and Spec|Defines structural realization within a domain.|
|Taxonomy|Relevant Ontology layer|Contextual placement of classification system.|
|Axiom|Core Ontology and Derived Theorems|Traceability of foundational principles.|


## 7. Example Entity Chains (Triadic Traceability)

|Layer|File|Purpose|
|---|---|---|
|Ontology|`Persistence.md`|Defines stabilized functional structure of difference propagation.|
|Spec|`PersistenceEvaluationPredicate (spec).md`|Formal predicate evaluating Persistence conditions.|
|Model|`PersistentForm (physics).md`|Domain realization of Persistence in physical systems.|

## 8. Templates & Structural Patterns

|Type|Template|Purpose|
|---|---|---|
|Ontology|[[Ontology Note Template]]|Defines primitive structures and recursive configurations.|
|Spec|[[Spec Note Template]]|Formalizes structural operations (operators, predicates).|
|Model|[[Model Note Template]]|Instantiates Ontology ↔ Spec chains into domain-specific models.|
|Property|[[Property Note Template]]|Qualifying attributes modulating ontological structures.|
|Construct|[[Construct Note Template]]|Functional configurations emerging from Property compositions.|
|Axiom|Ontology Template (concise)|Irreducible principles of difference structuring.|
|Taxonomy|List/Table Structures|Classification schemas (Forms, Fields, Chains).|


## 9. Rationale for This Architecture

- Maintains **clear Ontology ↔ Spec ↔ Model traceability chains**.
    
- Keeps Ontology structurally minimal, ensuring **scalability through functional configurations, not entity proliferation**.
    
- Supports **recursive emergence of complexity** via Specs and Constructs, without bloating ontological layers.
    
- Designed for **graph-based visual navigation** and **diagnostic workflows**.
    
- Provides a solid, modular foundation for **theorem derivations, simulations, and domain-specific modeling**.
