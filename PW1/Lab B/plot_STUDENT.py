"""
PW1 Lab B -- read observed decay data and compare it to the analytical law.
Produce a 1x2 figure:  left = observed data,  right = analytical N0*exp(-lam*t),
with SHARED axes so the two shapes are directly comparable.

Complete the TODOs below. Run with:  python plot.py
"""

import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 0.3
t, observed = np.loadtxt('decay_observed.csv', delimiter=',', skiprows=1, unpack=True)
no=observed[0]
analytical = no * np.exp(-LAMBDA * t)
fig, (x1, x2) = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(10, 5))
x1.scatter(t, observed, color='blue', label='Observed Data')
x1.set_title('Observed Decay')
x1.set_xlabel('Time (t)')
x1.set_ylabel('Number of Nuclei (N)')
x2.plot(t, analytical, color='red', label='Analytical Model')
x2.set_title('Analytical Decay')
x2.set_xlabel('Time (t)')
x2.set_ylabel('Number of Nuclei (N)')
plt.tight_layout()
plt.savefig('figure.png')
plt.show()