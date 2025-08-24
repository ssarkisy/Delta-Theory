# Mathematical Style Guide (Canonical Dialect)

Purpose: Define a single, canonical mathematical and geometrical dialect for the Geometrical Model of Nature. All technical documents should adhere to this guide.

---

## 1) Background spaces and sets

- Timespace:
  - M = ℝ × ℝ³ with coordinates (t, x, y, z).
  - Σ_t = {t} × ℝ³ are simultaneity slices (Euclidean 3-space snapshots).
- Vectors and norms:
  - Spatial vectors are bold: s, v, a.
  - Unit vectors carry hats: r̂.
  - Norms use double bars: ||·||.
- Indices:
  - Components indexed by i, j ∈ {1,2,3} with δ_ij.

Plain language: One global clock t and ordinary 3D space; we write vectors in bold, unit directions with hats, and lengths with double bars.

---

## 2) Kinematics (Newton–Cartan/Galilean background)

- Absolute time t is universal and oriented; durations are Δt = |t₂ − t₁|.
- Space is Euclidean with metric h_ij = δ_ij on each slice Σ_t.
- There is no 4D non-degenerate metric; we do not mix time and space into a single line element.
- Worldlines:
  - x: I ⊂ ℝ → ℝ³, t ↦ x(t), absolutely continuous; v = dx/dt, a = dv/dt.

Plain language: Objects move as dots in 3D through successive instants; speeds and distances are measured separately from time.

---

## 3) Propagation and causal set (retarded-only)

- Field speed is v; by default we non-dimensionalize to v = 1.
- Retarded-time condition (RT):
  - τ = t − t₀, r = ||s_o′(t) − s_j(t₀)||, and r = v τ.
- Causal set:
  - 𝒞_j(t) = { t₀ ≤ t | ||s_o′(t) − s_j(t₀)|| = v (t − t₀) }.
- Conventions:
  - H(0) = 0 (no instantaneous self-kick).
  - Exact center hits r = 0 with τ > 0 yield no directional acceleration (symmetry; measure zero).

Plain language: A push now only happens if a past sphere has had exactly enough time to reach you.

---

## 4) Distributions and regularization (spherical shells)

- Point emission at (t₀, s₀):
  - source = q δ(t − t₀) δ³(s − s₀).
- Expanding shell at speed v:
  - ρ(t, s) = (q/(4π r²)) δ(r − v τ) H(τ), r = ||s − s₀||, τ = t − t₀.
  - Equivalently with surface delta δ_S: ρ = (q/(4π r²)) δ_S_{vτ}(s − s₀) H(τ).
- Regularization:
  - δ(r − τ) → δ_ε(r − τ) = (1/(√(2π) ε)) exp(−(r − τ)²/(2 ε²)).
  - Use ε > 0 when differentiability is required; take ε → 0 limits in the weak/integrated sense.

Plain language: Each emission is a razor-thin spherical shell; when needed, we thicken it slightly so calculus works smoothly.

---

## 5) Master Equation of Motion (EOM; purely radial)

Given a receiver o′ at time t and a source j at retarded time t₀ ∈ 𝒞_j(t), let
- r = ||s_o′(t) − s_j(t₀)||,
- r̂ = (s_o′(t) − s_j(t₀)) / r,
- σ_{q_j q_{o′}} = sign(q_j q_{o′}) ∈ {+1, −1}.

Canonical per-hit acceleration:
a_{o′←j}(t; t₀) = κ σ_{q_j q_{o′}} |q_j q_{o′}| / ( r² (1 + |v_j(t₀)|)(1 + |v_{o′}(t)|) ) r̂.

Total acceleration:
a_o′(t) = Σ_j Σ_{t₀ ∈ 𝒞_j(t)} a_{o′←j}(t; t₀).

Notes:
- Emission cadence is constant; only per-wavefront amplitude and receiver response are speed-modulated.
- No cross products, no right-hand-rule magnetism; every per-hit action is along r̂.

Plain language: For each past emission that can reach you now, push along the line back to where it came from, weaken the push by both sides’ speeds and by 1/r², then add all pushes.

---

## 6) Energetics

- Potential (mollified):
  - Φ_ε is defined using δ_ε shells; U = q′ Φ_ε at a point.
- Force relation:
  - F = −∇U holds pointwise for Φ_ε; as ε → 0, interpret in the weak sense over resolved intervals.
- Work–energy:
  - ΔE_k = ∫ F · ds = −ΔU.

Plain language: With slightly thick shells, the usual “force is minus gradient of potential” works; in the razor-thin limit it works after integrating over small time windows.

---

## 7) Units and symbols

- v = 1 by default (dimensionless speed unit).
- ε = |e|/6 is the unit charge magnitude; Electrino q = −ε, Positrino q = +ε.
- κ > 0 universal coupling.
- q_eff(t₀) = q/(1 + |v_source(t₀)|) (per-wavefront amplitude); receiver modulation 1/(1 + |v_receiver(t)|).
- r, r̂ as above; H is the Heaviside step function with H(0) = 0.

Plain language: Fix units so the field speed is one; use ε as the basic charge; faster motion dims per-wavefront amplitude and response, not cadence.

---

## 8) Exclusions and scope

- No Lorentzian 4-vectors or Minkowski metric in the core specification.
- No v×B, no magnetic right-hand rule constructs; “magnetic-like” phenomena are emergent from retardation geometry.
- Keep alternate presentations (forms/differential geometry) in clearly marked appendices if needed.

---

## 9) Editorial micro-style

- After formal definitions, add a brief “Plain language” sentence.
- Use consistent symbol set: 𝒞_j(t), r, r̂, v, ε, κ.
- Equation tags (optional): (RT) retarded-time, (EOM) equation of motion, (REG) regularization, (ENER) energetics.
- Phrase velocity effects as “per-wavefront amplitude and receiver response modulation; emission cadence is constant.”
