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
  - constants layer
---

# Knowledge Base Architecture — ∆‑Theory Structural Framework

This note defines the **core file types, naming conventions, domain tags, and traceability rules** that structure the ∆‑Theory Knowledge Base. Its purpose is to ensure **clarity, modularity, and scalable coherence** across Ontology, Property, Construct, Spec, Model, Constants, and Recursive Dynamics layers.


## 1. Core Note Types & Structural Roles

|Type|Purpose|Typical Location|
|---|---|---|
|`ontology`|Foundational primitives, recursive structures, functional configurations.|`10 – Ontology`|
|`property`|Qualifying attributes modulating Ontology structures.|Within `10.3 – Properties`|
|`construct`|Functional configurations synthesized from Properties.|`10.4 – Constructs`|
|`recursive_construct`|Self-referential constructs that modulate themselves via recursive feedback dynamics.|`10.4 – Constructs` or `95 – Meta-Ontology`|
|`taxonomy`|Classification systems (Forms, Fields, Chains).|`10.5 – Diagnostic Classifications`|
|`spec`|Formal operators, predicates, rules, metrics, feedback loops.|`30 – Mathematics`|
|`constant`|Universal structural ratios and stabilization anchors for recursive propagation.|`20 – Constants`|
|`model`|Domain-specific realizations (physics, cognition, systems, ethics, etc.).|`50 – Physics`, `60 – Noetics`, `70 – Systems`, `91 – Ethics`|
|`axiom`|Irreducible theoretical principles.|`10 – Ontology` or `90 – Theorems`|
|`theorem`|Formal derivations from axioms and specs.|`90 – Theorems`|
|`meta`|Project-level architecture, organizational notes.|`00 – Project`|
|`glossary`|Plain-language explanations and cross-domain interpretations.|`Glossary`|
|`stub`|Placeholders for undeveloped notes.|Anywhere.|


## 2. Domain Tags

|Domain|Purpose|
|---|---|
|`ontology`|Foundational structures of difference propagation.|
|`mathematics`|Formal logic, structural operators, evaluative predicates, feedback mechanisms.|
|`physics`|Physical domain realizations (matter, energy fields).|
|`noetics`|Cognitive structures, self-referential loops, perception dynamics.|
|`systems`|Complex systems, feedback behaviors, networked structures.|
|`eth`|Ethical constructs and dynamics of difference responsibility.|
|`meta`|Organizational and architectural project notes.|

### Multi-Domain Notes Example:

```yaml
domain:
  - ontology
  - mathematics
  - ethics
```


## 3. Filename Conventions

|Aspect|Rule|
|---|---|
|Spaces|Use PascalCase (FormStabilization.md) or Natural Case (Form Stabilization.md).|
|Type Suffix|Always in `(parentheses)` — e.g., `(spec)`, `(physics)`, `(constant)`, `(recursive_construct)`.|
|Domain Tags|Applied in filenames only where realization context is specified (Models, Domain-Specific Constructs).|
|Stub Suffix|Use `(stub)` to mark placeholders.|
|Naming Consistency|Filename stems remain identical across Ontology ↔ Spec ↔ Model ↔ Constant chains.|


## 4. Frontmatter Structure by Note Type

### Universal Fields (All Notes)

```yaml
---
type: [ontology / property / construct / recursive_construct / taxonomy / spec / constant / model / axiom / theorem / meta / glossary / stub]
domain: [ontology / mathematics / physics / noetics / systems / ethics / meta]
aliases:
  - optional alias1
  - optional alias2
---
```

### Constant Notes

```yaml
---
type: constant
domain:
  - mathematics
  - ontology
aliases:
  - Recursive Stabilization Constant
  - Structural Ratio
ontology:
  - [[LinkedOntology]]
specs:
  - [[LinkedSpec]]   # Optional, if defined operationally
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
|`feedback_operator`|`EthicalFeedbackLoop (spec).md`|Recursive operator that modulates constructs based on domain feedback.|

## 6. Traceability Link Rules

|From|Must Link To|Purpose|
|---|---|---|
|Ontology|Linked Specs, Derived Ontologies|Clarifies formal operational context.|
|Property|Linked Ontology, optional Spec|Defines qualification attributes and evaluation pathways.|
|Construct|Linked Ontology, enabling Properties, optional Spec|Defines functional synthesis configurations.|
|Recursive Construct|Enabling Constructs, Linked Specs, Feedback Operators|Ensures recursive loop closure and feedback dynamics.|
|Spec|Linked Ontology, Linked Models|Defines operational scope and domain instantiation.|
|Constant|Linked Ontology, optional Spec|Anchors structural invariants within difference propagation chains.|
|Model|Linked Ontology, Construct, Spec, Constants|Defines structural realization within a domain.|
|Taxonomy|Relevant Ontology layer|Contextual placement of classification system.|
|Axiom|Core Ontology and Derived Theorems|Traceability of foundational principles.|


## 7. Recursive Dynamics Layer — Ethical and Systemic Feedback Loops

|Element|Description|
|---|---|
|Recursive Construct|A construct that not only configures properties but also modulates its own structure via feedback loops.|
|Feedback Operator Spec|Formal operator defining how domain feedback (from Models) influences Construct parameters.|
|Domain Feedback|Real-world or simulated difference interactions (e.g., system collapse, identity shifts) that trigger construct adjustments.|
|Recursive Loop Closure|Ensures that ethical or systemic constructs are not statically defined but dynamically re-embedded through recursive feedback mechanisms.|


## 8. Rationale for Constants Layer Integration

- Constants represent **universal structural invariants** (recursive stabilization ratios, closure thresholds, asymmetry ratios).
    
- They provide **anchoring conditions for recursive propagation**, ensuring difference loops stabilize coherently.
    
- Unlike Ontologies or Constructs, Constants do not propagate — they **modulate propagation behaviors** by defining systemic invariants.
    
- Constants must remain explicitly traceable across **Ontology ↔ Spec ↔ Model chains**, acting as foundational stabilizers of recursive difference flows.


## 9. Templates & Structural Patterns

|Type|Template|Purpose|
|---|---|---|
|Ontology|[[Ontology Note Template]]|Defines primitive structures and recursive configurations.|
|Property|[[Property Note Template]]|Qualifying attributes modulating ontological structures.|
|Construct|[[Construct Note Template]]|Functional configurations emerging from property compositions.|
|Recursive Construct|[[Recursive Construct Note Template]]|Defines self-referential structuring loops with feedback integration.|
|Spec|[[Spec Note Template]]|Formalizes structural operations (operators, predicates, feedback operators).|
|Constant|[[Constant Note Template]]|Defines structural invariants and recursive stabilization ratios.|
|Model|[[Model Note Template]]|Instantiates Ontology ↔ Construct ↔ Spec ↔ Constant chains into domain-specific models.|
|Axiom|Ontology Template (concise)|Irreducible principles of difference structuring.|
|Taxonomy|List/Table Structures|Classification schemas (Forms, Fields, Chains).|
