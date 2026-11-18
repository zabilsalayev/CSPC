# pytest cache directory #

This directory contains data from the pytest's cache plugin,
which provides the `--lf` and `--ff` options, as well as the `cache` fixture.

**Do not** commit this to version control.

See [the docs](https://docs.pytest.org/en/stable/how-to/cache.html) for more information.


## PW1 Lab B

**Data Observation:** The observed data showed the count of radioactive nuclei exponentially decreasing over time. 

**Analytical Match:** Based on the generated figure, the scatter plot of the observed data clearly matched the smooth curve predicted by the analytical decay law[cite: 3].

**Snakemake Pipeline:** The Snakemake pipeline automates the generation of the plot, ensuring the figure is only rebuilt when the input data or Python script changes[cite: 3].

## PW3

Data Distributions: The Shapiro-Wilk test showed that the maximum heart rate (thalach) is not normally distributed. Because of this, we used non-parametric statistical tests for the rest of the analysis.

Heart Rate and Disease: Using the Mann-Whitney U test, we found a clear difference between the two groups. Patients with heart disease have a significantly lower maximum heart rate on average compared to healthy people.

Age and Heart Rate: The Spearman correlation showed a negative relationship between age and maximum heart rate. This means that as people get older, their maximum heart rate tends to decrease.

The Chemical Mystery: At first glance, cadmium seemed to be the main cause of malignancy. However, when we filtered the data to account for the area pollution index, cadmium's correlation dropped heavily while benzene's stayed strong. This proves that benzene is the real cause of the cancer, and cadmium only looked guilty because it is common in highly polluted areas.

## PW2 -- Lab A: Motion from Tracking Data
Measured mean acceleration: -8.58 m/s² (standard deviation: 28.72 m/s²).
Why acceleration was noisy: The time step is very small ($\Delta t = 0.1\text{ s}$). When I take the derivative of position two times, I divide by $\Delta t^2 = 0.01$. So small errors in the data become big errors in acceleration. This is why the acceleration jumps up and down a lot.
What integrating back showed: I integrated the noisy acceleration two times with cumulative_trapezoid. The noise goes up and down randomly, so it mostly cancels out. I got the original position back with a maximum error of 0.78 m.

## PW2 -- Lab B: Optimization in Chemistry
Part 2: Comparing Optimization Methods
Convex function $f(x) = (x-3)^2 + 1$ ($x_0 = 0$): All three methods (Gradient Descent, Newton’s method, SLSQP) agree. They all reach the global minimum at $x = 3.0000$.
Non-convex function $g(x) = x^4 - 3x^2 + x + 5$: The methods do not always agree. The starting point changes the result.
From $x_0 = 0$: Gradient Descent ($x \approx -1.3008$) and SLSQP ($x \approx -1.3009$) find the global minimum. Newton’s method goes to $x \approx 0.1699$, where $g''(0.1699) = -5.65 < 0$. This is a local maximum. Newton only looks for $g'(x) = 0$, so it can stop at a maximum.
From $x_0 = 2$: Gradient Descent and Newton’s method both stop at the nearby local minimum ($x \approx 1.1309$, $g'' = +9.35 > 0$). SLSQP jumps over the barrier to the global minimum ($x \approx -1.3006$).
Part 3: First-Order Reaction Kinetics
Fitted rate constant: $k = \text{<paste your printed k value>}$. I used SLSQP to minimize the squared residuals.
Part 4: Chemical Equilibrium ($\text{H}_2 + \text{I}_2 \rightleftharpoons 2\,\text{HI}$, $K = 15.6$)
Equilibrium extent of reaction: $x = 0.6638\text{ mol}$ (Newton and SLSQP give the same value).
Equilibrium composition: $\text{H}_2 = 0.3362\text{ mol}$, $\text{I}_2 = 0.3362\text{ mol}$, $\text{HI} = 1.3277\text{ mol}$.
Part 5 (Bonus): Titration Equivalence Point
Equivalence point volume: $\text{<paste your printed volume>}\text{ mL}$. I found it where $\frac{d\text{pH}}{dV}$ is maximum, because pH changes fastest there.



