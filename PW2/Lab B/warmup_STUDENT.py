"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize

# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

# TODO 2A: minimise f three ways from x0=0 and print each result:
#   (1) gradient descent by hand (loop x = x - lr*df(x) until the step is tiny)
#   (2) scipy.optimize.newton(df, x0, fprime=d2f)
#   (3) scipy.optimize.minimize(f, x0, method="SLSQP")

print("--- 2A: Minimizing f(x) ---")
# (1) Gradient Descent by Hand
x = 0.0
lr = 0.1
tol = 1e-7
max_iter = 10000

for _ in range(max_iter):
    grad = df(x)
    step = lr * grad
    x = x - step
    if abs(step) < tol:
        break
print(f"Gradient Descent result: x = {x:.6f}")

# (2) Newton's Method
res_newton_f = newton(df, x0=0.0, fprime=d2f)
print(f"Newton method result:    x = {res_newton_f:.6f}")

# (3) SLSQP Optimization
res_slsqp_f = minimize(f, x0=0.0, method="SLSQP")
print(f"SLSQP method result:     x = {res_slsqp_f.x[0]:.6f}")


# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

# TODO 2B: run the same three methods on g, from x0=0 AND from x0=2.
#   For Newton (which solves dg(x)=0), also check the sign of d2g at the answer:
#   d2g > 0 means a minimum, d2g < 0 means a maximum.
#   In your README note: do the methods agree? did Newton find a minimum or
#   another stationary point? how did the starting point change the result?

def run_2b(x0):
    print(f"\n--- 2B: Minimizing g(x) from x0 = {x0} ---")
    
    # (1) Gradient Descent
    x = float(x0)
    lr = 0.01
    for _ in range(10000):
        grad = dg(x)
        step = lr * grad
        x = x - step
        if abs(step) < 1e-7:
            break
    print(f"Gradient Descent result: x = {x:.6f}")
    
    # (2) Newton
    res_newton = newton(dg, x0=x0, fprime=d2g)
    sign_str = "minimum (d2g > 0)" if d2g(res_newton) > 0 else "maximum (d2g < 0)"
    print(f"Newton method result:    x = {res_newton:.6f} -> Classification: {sign_str}")
    
    # (3) SLSQP
    res_slsqp = minimize(g, x0=x0, method="SLSQP")
    print(f"SLSQP method result:     x = {res_slsqp.x[0]:.6f}")

run_2b(0)
run_2b(2)