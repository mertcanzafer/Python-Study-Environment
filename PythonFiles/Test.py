import math
import numpy as np
import sympy as sym

# Newton Raphson method


def f(x):
    return x*np.log(x) - 12


def df(x):
    return 3*x**2 + 7*np.sin(7*x)


x = 10
print(f(x))

# formula = 0.25 - (f(x) / df(x))
# print(formula)
