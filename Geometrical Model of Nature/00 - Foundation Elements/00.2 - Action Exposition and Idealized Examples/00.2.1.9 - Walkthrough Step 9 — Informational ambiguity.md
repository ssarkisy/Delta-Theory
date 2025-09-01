# Walkthrough Step 9 — Informational ambiguity

Existing text excerpt:
> ### **Informational Ambiguity at the Receiver**
> From the perspective of the receiving Architrino, the information carried by an intersecting expanding spherical shell is limited. The receiver only knows two things:
> 1.  The net strength of the potential at the point of intersection.
> 2.  The unoriented line of action through its current position (i.e., one of the two open rays on that line; orientation along the line is ambiguous).

Detailed explanation (degeneracies and inference limits):

- Many-to-one mapping:
  - Different combinations of source identity, charge magnitudes, distances, and emission timings/geometry can yield the same instantaneous hit magnitude and direction at the receiver.

- Sign ambiguity across a line:
  - Attraction from a positive charge on one side is indistinguishable, at an instant, from repulsion by a negative charge located at the diametrically opposite point along the same line.

- Consequence for reconstruction:
  - Instantaneous local data at the receiver are insufficient to invert for sources; this remains true even for an absolute observer who knows the universal clock $t$ and the Euclidean rest frame. The absolute observer can eliminate coordinate uncertainty (perfect synchronization and alignment) but not the physical ambiguities below.
  - Irreducible ambiguities at an instant:
    - Sign/side ambiguity: attraction from a positive source on one side is indistinguishable from repulsion by a negative source on the diametrically opposite side along the same line.
    - Superposition along a line: multiple sources aligned on the same unoriented line of action can sum to the same net magnitude and direction at one instant.
    - Self-hit confound: a self-interaction and an external source can yield identical instantaneous data if they lie on the same line with compensating magnitudes.
    - Continuum of surrogate locations: for any instantaneous hit there exists a continuum of stationary surrogate source positions along the same unoriented line of action, each with a correspondingly adjusted emission time $t_0$, that reproduces the same instantaneous data; hence instantaneous inversion is severely underdetermined.

  - What helps (over time or with more views):
    - Track the time series of the line of action $\hat{\mathbf{r}}(t)$ and separation proxy $r(t)$ inferred from timing and geometry; curvature and rotation of $\hat{\mathbf{r}}$ constrain source trajectories.
    - Use multiple receivers (an array) to triangulate unoriented lines at the same $t$; intersecting rays narrow candidate locations (two-sided).
    - Actively vary the receiver path to sample different directions and ranges, turning the inverse problem into a controlled experiment.
    - Impose priors: charge inventories, speed bounds, and assembly templates reduce degeneracy space.
    - Use surrogate-location recasts: for instantaneous hits, place a stationary surrogate source somewhere along the same unoriented line of action and adjust only the emission time; this simplifies hypothesis testing without altering per-wavefront amplitude.
  - Absolute-observer note: Access to absolute time and a common Euclidean frame enables global correlation of events across receivers, but unique inversion at an instant would require hidden information (the full emission ledger $\{(t_0,\mathbf{s}_j(t_0),q_j,\mathbf{v}_j(t_0))\}_j$). Practical reconstruction is therefore necessarily temporal, statistical, and multi-view.

Plain language: A hit tells you how hard and from which direction you’re being pushed—but not who pushed you or how far away they are. Many different source stories can fit the same momentary shove. A null action at an instant conveys no information about sources; superposition can cancel perfectly even in a non-empty universe.
