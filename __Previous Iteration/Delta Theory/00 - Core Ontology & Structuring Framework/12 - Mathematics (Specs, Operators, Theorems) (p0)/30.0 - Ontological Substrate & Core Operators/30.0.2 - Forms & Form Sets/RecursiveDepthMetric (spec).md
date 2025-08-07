---
type: spec
spec_type: metric
domain:
  - mathematics
aliases:
  - Depth(Fₙ)
  - Recursive Form Depth
ontology: "[[RecursiveDepth]]"
model:
  - "[[FormDepth (physics) (stub)]]"
---

# RecursiveDepthMetric

## Definition

**`RecursiveDepthMetric`** is a formal **metric operator** that evaluates the **ontological depth** of a stabilized form $Fₙ = ⊚(Rⁿ(∆₀))$ by counting the number of **recursive relational embeddings (n)** required for its construction and coherence.

It measures **how many nested difference layers** are structurally active in sustaining the form’s persistence.

## Inputs

|Input|Type|Description|
|---|---|---|
|`∆₀`|∆|Initiating primitive difference|
|`Rⁿ(∆₀)`|R|n-depth recursive relational embedding|
|`Fₙ`|F|Target Form being evaluated for depth|

## Output

|Output|Type|Meaning|
|---|---|---|
|Result|Integer (n)|Returns the number of recursive embedding layers stabilized in the form|

## Formal Expression

Given:
$$
Fₙ = ⊚(Rⁿ(∆₀))
$$

The Recursive Depth is:
$$
Depth(Fₙ) = n
$$

|Symbol|Meaning|
|---|---|
|$∆₀$|Primitive initiating difference|
|$Rⁿ(∆₀)$|Recursive relational embedding chain of depth n|
|$⊚$|Stabilization operator applied at each embedding level|
|$Fₙ$|Resulting stabilized form|
|$Depth(Fₙ)$|Number of recursive embedding layers|

### Interpretive Pseudocode

```pseudo
function RecursiveDepth(Fₙ):
    depth = 0
    current = Fₙ
    while current traces back to R-layer:
        depth += 1
        current = previous R-layer
    return depth  // Depth(Fₙ) = n
````


## Preconditions

- `Fₙ` is a valid stabilized form constructed via recursive embedding.
    
- The embedding chain is traceable (no collapsed or singularities in R-path).
    
- Each embedding layer satisfies the stabilization condition (⊚).
    

## Postconditions

- Returns the **depth count (n)** indicating the number of stabilized recursive embeddings.
    
- Depth(Fₙ) informs system attributes like:
    
    - Structural inertia
        
    - Stored ∆‑tension (Potential Energy)
        
    - Restoration complexity in case of collapse.
        
- Failure to evaluate (broken embedding chain) indicates a **FormCollapse** or unstable structure.
    

## Role in ∆‑Theory

- **Metric Function**: Quantifies the ontological construction path from ∆₀ to Fₙ.
    
- **Structural Complexity Indicator**: Depth directly correlates to form inertia, resilience, and recovery cost.
    
- **Diagnostic Tool**: Used in analyzing systemic fragility, semantic density, and emergence layers.
    
- **Cross-Domain Scalability**: Applicable in physics (mass layers), cognition (belief depth), systems (nested structures).
    

## Example Usage

|Domain|Interpretation / Result| 
|---|---|
|Physics|Counting field interaction layers sustaining a proton (Depth = high)|
|Cognition|Evaluating belief systems built through recursive narrative loops|
|Systems|Measuring depth of feedback structures in recursive control loops|
|Software|Assessing architectural depth of nested abstractions|


## Related Constructs

|Type|Link|Purpose|
|---|---|---|
|Ontology|[[RecursiveDepth]]|Ontological concept of depth in form construction|
|Spec|[[RecursiveEmbedding (spec)]]|Operator defining recursive embedding chains|
|Spec|[[RecursiveClosure (spec)]]|Predicate for loop closure in recursive forms|
|Ontology|[[PotentialEnergy (physics)]]|Stored ∆-tension increases with Depth(Fₙ)|
|Ontology|[[StructuralInertia (spec)]]|Resistance to change based on depth layering|
|Model|[[FormDepth (physics) (stub)]]|Domain instantiation of recursive depth in physical systems|


## Notes

- Depth(Fₙ) is **structural**, not visual — surface simplicity can hide deep recursive construction.
    
- There may exist **fractal depths** — partial embeddings with recursive sub-structures.
    
- RecursiveDepth influences both **stability (persistence)** and **fragility (collapse cost)**.
    
- Depth dynamics interact with recursive closures — deeper forms are harder to destabilize but catastrophic upon collapse.
    

## TODO

- Define metrics for **fractional depth states** (meta-stabilized sub-structures).
    
- Formalize depth-related **fragility curves** — mapping depth to collapse cost.
    
- Visualize **RecursiveDepth trajectories** in ∆‑Field topologies.
    
- Model domain-specific **Depth-to-Inertia mappings** (e.g., mass, cognitive rigidity, systemic latency).
  