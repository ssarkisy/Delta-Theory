# Walkthrough Step 1 — Background and Simple Action

Existing text excerpt:
> The dynamics of an Architrino are governed by a simple action: an acceleration caused by the intersection of its path with a potential field.
>
> Geodesics and dynamics: The background is fixed (absolute time × Euclidean space); free paths are straight. Accelerations come only from delayed, purely radial hits from emitted shells—never from background curvature.

Detailed explanation (dynamical geometry):

- Background kinematics (Newton–Cartan/Galilean):
  - The arena is absolute time × Euclidean space, $\mathcal{M}=\mathbb{R}\times\mathbb{R}^3$, with simultaneity slices $\Sigma_t=\{t\}\times\mathbb{R}^3$ carrying the flat spatial metric $h_{ij}=\delta_{ij}$.
  - “Geodesics are straight” means: in the absence of any interaction, a worldline $\mathbf{s}(t)$ satisfies $\mathbf{a}(t)=d^2\mathbf{s}/dt^2=\mathbf{0}$; motion is uniform and rectilinear in each slice $\Sigma_t$. The background is fixed; there is no curvature to encode forces.

- Field geometry as expanding spherical shells:
  - Each Architrino emits potential on razor-thin spherical shells that expand at field speed $v$ (non-dimensionalized to $v=1$ elsewhere). The field is distribution-valued, supported on $r=v(t-t_0)$ around the historical emission point $\mathbf{s}(t_0)$, with surface density $\propto 1/r^2$.
  - “Potential field” here is not a static scalar on space; it is the collection of expanding spherical wavefronts from all sources at earlier times, summed at the receiver’s location and now.

- Intersection as the driver of acceleration:
  - The receiver’s worldline is $\mathbf{s}_{o'}(t)$. An intersection at time $t$ means some earlier emission time $t_0 < t$ satisfies the causal-distance condition
    $
    \|\mathbf{s}_{o'}(t) - \mathbf{s}_o(t_0)\| = v(t - t_0)
    $
    That event is a causal hit from source $o$’s past to the receiver’s present.
  - At a hit, the acceleration impulse is purely radial along
    $
    \hat{\mathbf{r}} = \frac{\mathbf{s}_{o'}(t) - \mathbf{s}_o(t_0)}{\|\mathbf{s}_{o'}(t) - \mathbf{s}_o(t_0)\|}.
    $
    No cross products or right-hand-rule terms appear; the action is collinear with $\hat{\mathbf{r}}$.

- “Simple action” in precise terms:
  - The law is event-driven: acceleration is a sum of per-hit radial contributions, each scaled by $1/r^2$. Between hits (as $\eta\to 0$) motion is inertial; with mollification ($\eta>0$) the impulses become short, smooth pushes.
  - The background adds no force; departures from straight motion arise only from these intersections with emitted fields (including self-hits when kinematics allow).

- Physical picture:
  - Picture many expanding spherical “skins.” A push occurs only when a skin arrives, directed straight along the radius back to its emission point, with strength falling as $1/r^2$.

If you’d like to continue, next up are “Units and constants” (the $v=1$ convention, coupling $\kappa$, regularization width $\eta$) and the formal definition of the causal interaction set $\mathcal{C}_o(t)$.
