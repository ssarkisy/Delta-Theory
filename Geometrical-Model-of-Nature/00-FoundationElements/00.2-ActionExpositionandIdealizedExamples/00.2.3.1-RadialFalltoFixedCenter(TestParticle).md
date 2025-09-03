# 00.2.3.1 — Radial Fall to Fixed Center (Test Particle)

Setup:
- A test Architrino with charge q′ falls radially toward a fixed center with charge q.
- The interaction is delayed; the causal emission time exists uniquely for a fixed source, but the acceleration depends only on the current separation because the source position is time-independent.

Objectives:
- Closed-form relations for r(t), v(r), and time-to-fall from r0 to r.
- Energy balance and integral expressions suitable for comparison.

Delay differential equation and exact reduction:
- With field speed normalized to $v=1$ and a fixed source location $x_c$, the causal root satisfies $|x(t)-x_c|=t-t_0$ with $t_0<t$.
- The per-hit law yields a purely radial acceleration whose magnitude depends on the current separation $r(t)=|x(t)-x_c|$:
  $$
  \ddot{x}(t) \;=\; -\,\kappa\,\sigma_{q q'}\,\frac{|q q'|}{r(t)^2}\,\mathrm{sgn}\!\big(x(t)-x_c\big).
  $$
  Writing $K=\kappa\,|q q'|>0$ and $r=\lvert x-x_c\rvert$, the radial ODE is
  $$
  \ddot{r}(t) \;=\; -\,\frac{K}{r(t)^2}.
  $$

Exact solution (closed form):
- Energy integral: $\tfrac{1}{2}\dot{r}^2 - K/r = \text{const}$.
- For release from rest at $r(0)=r_0$ with $\dot{r}(0)=0$,
  $$
  r(t) \;=\; r_0 \cos^2 \eta,\qquad
  t \;=\; \sqrt{\frac{r_0^3}{2K}}\;\big(\,\eta + \sin\eta\cos\eta\,\big),\quad \eta\in[0,\tfrac{\pi}{2}],
  $$
  with fall time $T_{\mathrm{fall}}=\tfrac{\pi}{2}\sqrt{r_0^3/(2K)}$.

Notes:
- For a fixed source, the delayed formulation reduces exactly to the above ODE; the causal root determines only the emission time, not the instantaneous acceleration magnitude or direction.

Use:
- A ground-truth closed form against which delayed-law simulations can be benchmarked in the fixed-source case.

Plain language: With a stationary center, the delayed law simplifies to the familiar inverse-square fall, which has an exact, closed-form solution.
