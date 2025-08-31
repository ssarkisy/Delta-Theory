# Walkthrough Step 10 — Numerical recipe and stability

Event-aware integration (practical algorithm):

1. Root finding:
   - For each source $o$ (including $o'=o$ for potential self-hits), solve $F(t_0;t)=\|\mathbf{s}_{o'}(t)-\mathbf{s}_o(t_0)\|-(t-t_0)=0$ for $t_0< t$.
   - Discard non-physical roots by convention $H(0)=0$ (exclude $\tau=0$); note $r=0$ occurs only at $\tau=0$ and is thus excluded.

2. Per-hit accumulation:
   - For each accepted root, compute $r$, $\hat{\mathbf{r}}$, and
     $$
     \mathbf{a}_{o'\leftarrow o}(t;t_0)=\kappa\,\sigma_{q_o q_{o'}}\,\frac{|q_o q_{o'}|}{r^2}\,\hat{\mathbf{r}}.
     $$
   - Sum over all sources and all roots (superposition).

3. Time stepping:
   - Impulsive mode: advance velocities with jumps at hit times (measure-driven ODE with velocity of bounded variation).
   - Mollified mode: replace $\delta(\cdot)$ by $\delta_\eta(\cdot)$ and integrate with a standard ODE solver; choose $\eta$ small relative to local geometric scales.

4. Stability tips:
   - Use event bracketing or root trackers for continuity of $t'(t)$ across steps.
   - Limit step size so that at most one (or a controlled number of) mollified shells overlap significantly per step.
   - Monitor invariants over resolved windows (work–energy balance with $\Phi_\eta$) to validate settings.

5. Units:
   - Use $v=1$ nondimensionalization throughout. Remember: emission cadence and per-wavefront amplitude are constant; receiver speed influences only power via $v_r$.

Plain language: At each time, find which past emissions can reach you now, sum their radial pushes with 1/r² falloff, and step forward—either with sharp kicks at exact hit times or with tiny-thick shells for smooth integration.
