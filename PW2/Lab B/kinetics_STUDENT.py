"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

A first-order reaction decays as  C(t) = C0 * exp(-k*t).  You have noisy
concentration-vs-time measurements; find the k that best matches them.
Complete the TODOs. Run:  python kinetics.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# TODO 1: 
data = np.loadtxt("kinetics.csv", delimiter=",", skiprows=1)
t = data[:, 0]
C = data[:, 1]
C0 = C[0]

# TODO 2: 
def total_error(k):
  
    k_val = k[0] if isinstance(k, (list, np.ndarray)) else k
    model = C0 * np.exp(-k_val * t)
    return np.sum((C - model)**2)

# TODO 3: 
res = minimize(total_error, x0=[0.5], method="SLSQP", bounds=[(0, 5)])
fitted_k = res.x[0]
print(f"Fitted rate constant k = {fitted_k:.6f}")

# TODO 4: 
plt.figure(figsize=(8, 5))
plt.scatter(t, C, color="red", label="Measured Data")

t_dense = np.linspace(t.min(), t.max(), 200)
C_fitted = C0 * np.exp(-fitted_k * t_dense)
plt.plot(t_dense, C_fitted, color="blue", label=f"Fitted Curve (k = {fitted_k:.4f})")

plt.xlabel("Time (t)")
plt.ylabel("Concentration (C)")
plt.title("Reaction Kinetics Fit")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("kinetics.png")
plt.show()