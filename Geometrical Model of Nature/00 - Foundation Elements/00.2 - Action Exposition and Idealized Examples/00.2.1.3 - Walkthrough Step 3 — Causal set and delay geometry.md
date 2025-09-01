# Walkthrough Step 3 — Causal set and delay geometry

Existing text excerpt:
> -   **Causal Interaction Set:** The receiver $o'$ at time $t$ interacts with a source $o$ through the (possibly multi-valued) set of causal emission times
>     $$
>     \mathcal{C}_o(t) = \big\{\, t_0 < t \;\big|\; \|\mathbf{s}_{o'}(t) - \mathbf{s}_o(t_0)\| = (t - t_0) \,\big\}.
>     $$
>     For $|\mathbf{v}_o(t_0)| < 1$ locally, $\mathcal{C}_o(t)$ is generically a singleton; for $|\mathbf{v}_o|> 1$ it may contain multiple solutions (including self-hits when $o'=o$).

Clarification: “Multi-valued” means that, for a fixed observation time $t$, there can be more than one emission time $t_0$ that satisfies the causal-distance condition; i.e., $\mathcal{C}_o(t)$ may contain multiple causal roots (e.g., when $|\mathbf{v}_o|> 1$ or for self-hits when $o'=o$). This multiplicity can occur only if the transmitter/source has exceeded field speed at least once; if $|\mathbf{v}_o|<1$ everywhere, $F(t_0;t)$ is strictly increasing in $t_0$ and the causal root is unique.

Detailed explanation (geometry of delay and roots):

- Root condition as an expanding spherical shell intersection:
  - Define $F(t_0; t) \equiv \|\mathbf{s}_{o'}(t) - \mathbf{s}_o(t_0)\| - (t - t_0)$ (with $v=1$ units). Causal roots satisfy $F(t_0; t)=0$ with $t_0 < t$ and $H(t-t_0)$.
  - Geometrically: the source point $\mathbf{s}_o(t_0)$ must lie on the sphere of radius $\tau = t - t_0$ centered at the receiver’s current position $\mathbf{s}_{o'}(t)$.

- Local uniqueness (sub-field-speed, transverse crossing):
  - If the source speed is locally sub-field-speed ($\|\mathbf{v}_o(t_0)\|<1$) and the derivative $\partial_{t_0}F(t_0;t) = -\hat{\mathbf{r}}\!\cdot\!\mathbf{v}_o(t_0) + 1$ is nonzero at the root, then the implicit function theorem guarantees a unique, smooth root branch near $t$.
  - Intuition: the expanding spherical shell intersects the moving source path transversely.

- Multiple roots (require super-field-speed):
  - When $\|\mathbf{v}_o\|> 1$ at some emission times, the source can outpace recent shells, allowing several distinct historical points to satisfy the same distance–time constraint (multi-hit regime). If $\|\mathbf{v}_o\|<1$ everywhere, $F(t_0;t)$ is strictly increasing in $t_0$, so at most one causal root exists.

- Conventions at singular cases:
  - We adopt $H(0)=0$ so the instantaneous emission at $t_0=t$ does not produce an immediate self-kick.
  - No $r=0$ causal roots beyond $\tau=0$: because $r = v(t - t_0)$, $r=0$ implies $\tau=0$; the $\tau=0$ case is excluded by $H(0)=0$. Under mollification, the symmetric limit as $r\to 0$ yields zero net push.

Plain language: You only feel pushes from those earlier moments of a source that lie exactly on the “now-sphere” around you. Usually there’s just one such moment; if the source is very fast or its path loops around, there can be several.

Non-technical visualization — outrunning your own wake (speedboat analogy):
- Picture a speedboat continuously laying down circular wake ridges that spread outward across the water at a fixed wave speed $c_w$ (analogy variable: wake ridge expansion speed). If the boat stays slower than $c_w$, it remains inside its newest ridge and will never meet it again—no self-hits. Once the boat exceeds $c_w$, it moves ahead of its freshest ridge. Later, if it curves or slows, it can run into older ridges it created earlier. Each crossing delivers a brief shove normal to the ridge (straight outward from the ridge’s center), mirroring the model’s purely radial push. The ridge “drop rate” never changes; each ridge has the same strength regardless of the boat’s speed when it was made. This is an analogy: real Kelvin wakes are dispersive; we idealize to circular ridges expanding at one speed to match the model’s fixed-speed shells.

Four self-hits in one maneuver (storyboard):
1) Sprint phase (exceed the field speed): The boat accelerates to a speed strictly greater than $c_w$ and holds it for several ticks. During this super-speed run it lays down several concentric ridges that it immediately outruns.
2) Set up spacing: Maintain the super-speed for long enough to create at least four successive ridges with noticeable gaps (their radii grow at $c_w\cdot \Delta t$ while the boat advances faster than $c_w$).
3) Curving return: Bank into a broad, smooth turn (a teardrop/U-turn or a gentle outward spiral) that arcs back toward the track laid moments earlier.
4) Crossings: As the boat’s curved path cuts across the expanding circles, it re-enters first the outermost of those recent ridges, then the next three in sequence. With a steady arc and timing, four distinct ridge crossings occur in quick succession—four self-hits. The shove at each crossing points straight away from the center of that ring (the boat’s earlier position).
5) Tuning intuition: To make four hits likely, think “fast straight run” $(\lvert v\rvert>c_w)$ to lay multiple rings, then a wide-radius turn whose chord length is comparable to the ring spacing. Tighter loops and longer super-speed runs increase the chance of multiple crossings; if you never exceed $c_w$, you cannot produce this multi-hit pattern at all.
