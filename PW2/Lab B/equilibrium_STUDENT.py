"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: 
def k_imbalance(x):
    return ((2*x)**2) / ((a - x) * (b - x)) - K

# TODO 2 
x_newton = newton(k_imbalance, x0=0.5)

# TODO 3 
def objective(x):
    return k_imbalance(x[0])**2

res_minimize = minimize(objective, x0=[0.5], method="SLSQP", bounds=[(0, 0.999)])
x_slsqp = res_minimize.x[0]

print(f"Extent x via Newton's method: {x_newton:.6f}")
print(f"Extent x via SLSQP minimize:  {x_slsqp:.6f}")

# TODO 4: 
x_eq = x_newton
H2_eq = a - x_eq
I2_eq = b - x_eq
HI_eq = 2 * x_eq

print("\n--- Equilibrium Amounts ---")
print(f"H2: {H2_eq:.4f} mol")
print(f"I2: {I2_eq:.4f} mol")
print(f"HI: {HI_eq:.4f} mol")

x_vals = np.linspace(0, 0.99, 200)
H2_vals = a - x_vals
I2_vals = b - x_vals
HI_vals = 2 * x_vals

plt.figure(figsize=(8, 5))
plt.plot(x_vals, H2_vals, label="H2 (1-x)", color="blue")
plt.plot(x_vals, I2_vals, label="I2 (1-x)", color="green", linestyle="--")
plt.plot(x_vals, HI_vals, label="HI (2x)", color="red")

plt.axvline(x_eq, color="black", linestyle=":", label=f"Equilibrium x = {x_eq:.4f}")
plt.scatter([x_eq]*3, [H2_eq, I2_eq, HI_eq], color="black", zorder=5)

plt.xlabel("Extent of Reaction (x)")
plt.ylabel("Amount (mol)")
plt.title("Chemical Equilibrium Composition")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("equilibrium.png")
plt.show()