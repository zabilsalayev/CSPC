
## PW2 -- Lab A: Motion from Tracking Data
- **Measured mean acceleration:** `-8.58 m/s²` (std: `28.72 m/s²`).
- **Why acceleration was noisy:** Differentiating noisy position measurements twice divides small fluctuations by $\Delta t^2$, amplifying them into large swings in acceleration.
- **What integrating back showed:** Integrating acceleration twice with `cumulative_trapezoid` averaged out random noise and recovered the original position within `0.78 m`.
