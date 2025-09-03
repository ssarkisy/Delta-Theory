# Walkthrough Step 5 — Receiver velocity and work

Existing text excerpt:
> ### Receiver velocity: radial vs orthogonal components (instantaneous effect)
> Because $\mathbf{a}_{o'\leftarrow o}(t;t_0) \parallel \hat{\mathbf{r}}$, its instantaneous effect satisfies
> $$
> \frac{d}{dt}\mathbf{v}_\perp \;=\; \mathbf{0}\quad\text{from this hit}, 
> \qquad
> \frac{d}{dt}v_r \;=\; \mathbf{a}_{o'\leftarrow o}(t;t_0)\cdot \hat{\mathbf{r}}
> \;=\;
> \frac{\kappa\,\sigma_{q_o q_{o'}}\,|q_o q_{o'}|}{r^2}.
> $$

Detailed explanation (decomposition and energetics):

- Decomposition at a hit:
  - Write $\mathbf{v} = v_r\,\hat{\mathbf{r}} + \mathbf{v}_\perp$, where $v_r=\mathbf{v}\cdot\hat{\mathbf{r}}$ and $\mathbf{v}_\perp\cdot\hat{\mathbf{r}}=0$.
  - A single hit changes $v_r$ but not $\mathbf{v}_\perp$ instantaneously.

- Power and work:
  - Instantaneous power is $\mathbf{a}\cdot\mathbf{v} = |\mathbf{a}|\,v_r$.
  - Orthogonal motion does no instantaneous work; only radial motion exchanges kinetic and potential energy at a hit.

- Local trend via $1/r^2$:
  - If $v_r<0$ (moving inward), near-future hits tend to be stronger because $r$ shrinks between events; if $v_r>0$, they tend to weaken.

Plain language: Each hit only changes your along-the-line speed right then; sideways speed is untouched. Energy transfer happens only through the along-the-line part.
