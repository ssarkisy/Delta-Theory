# Walkthrough Step 7 — Superposition and locality

Existing text excerpt:
> -   **Superposition:** The potential fields from all sources superpose linearly. The net potential at any point is the sum of the individual potentials:
>     $$
>     \Phi_{\text{net}} = \sum_{i} \Phi_i
>     $$
>     The total acceleration on a particle at any instant is the vector sum of the accelerations from all intersecting expanding spherical shells. Operationally, every Architrino is continuously immersed in the superposed sphere streams of all others (and, when kinematics permit, its own); tractability comes from treating each causal hit independently with $1/r^2$ distance weighting, which makes local sources dominate.

Detailed explanation (why near fields dominate):

- Linear addition at the shell level:
  - Because each source contributes a distribution supported on its causal sphere(s), the total field is a sum of these measures; the acceleration law is linear in the summed contributions.

- Locality from $1/r^2$:
  - The surface density on a sphere scales as $1/r^2$, so nearby hits contribute disproportionately compared to distant ones. Random phases and geometries of distant sources enhance cancellation.

- Practical consequence:
  - Simulations can prioritize nearby sources and recent roots, using multipole or sampling approximations for far-field backgrounds.

Plain language: Add all the pushes; the closest ones matter most because each hit falls off like one over distance squared, and distant pushes mostly cancel out.
