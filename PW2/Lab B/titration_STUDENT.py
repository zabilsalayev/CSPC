"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
The equivalence point is the volume where the pH changes fastest (the steep
jump). Numerically, that is where the SLOPE of the pH curve is largest.
Run:  python titration.py
"""
import numpy as np
import matplotlib.pyplot as plt

# TODO 1: read titration.csv (columns volume_base, pH) into arrays V, pH.
data = np.loadtxt("titration.csv", delimiter=",", skiprows=1)
V = data[:, 0]
pH = data[:, 1]

# TODO 2: compute the slope of the pH curve with np.gradient(pH, V), and find
#         the volume where that slope is largest (np.argmax). That is the
#         equivalence point. Print it.
slope = np.gradient(pH, V)
max_idx = np.argmax(slope)
equiv_V = V[max_idx]

print(f"Equivalence point volume = {equiv_V:.2f} mL (at max slope = {slope[max_idx]:.4f})")

# TODO 3: make two plots side by side: (left) pH vs volume with a line at the
#         equivalence point; (right) the slope vs volume, showing it peaks
#         at the equivalence point. Save as titration.png.
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Left plot: pH vs Volume
ax1.plot(V, pH, color="blue", label="pH Curve")
ax1.axvline(equiv_V, color="red", linestyle="--", label=f"Equiv Point ({equiv_V:.1f} mL)")
ax1.set_xlabel("Volume of Base Added (mL)")
ax1.set_ylabel("pH")
ax1.set_title("Titration Curve")
ax1.legend()
ax1.grid(True)

# Right plot: Slope vs Volume
ax2.plot(V, slope, color="green", label="dpH / dV")
ax2.axvline(equiv_V, color="red", linestyle="--", label=f"Peak at {equiv_V:.1f} mL")
ax2.set_xlabel("Volume of Base Added (mL)")
ax2.set_ylabel("Slope (dpH/dV)")
ax2.set_title("First Derivative (Slope)")
ax2.legend()
ax2.grid(True)

plt.xlabel("Time (t)")
plt.ylabel("Concentration (C)")
plt.title("Reaction Kinetics Fit")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("titration.png")
plt.show()