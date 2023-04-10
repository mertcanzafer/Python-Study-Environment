import numpy as np
import math
import matplotlib.pyplot as plt

# Function def. for 2^(0.5) when F(x) = 0


def F(x): return x**2 - 2


def SecantFunc(x0, x1, tol):

    while (abs(x1 - x0) >= tol):
        num = F(x1) * (x1 - x0)
        denum = F(x1) - F(x0)
        x2 = x1 - (num / denum)
        x0 = x1
        x1 = x2
    return x2


x0 = 1
x1 = 2
tol = 10**(-4)

print("Approximation of square root of 2:", SecantFunc(x0, x1, tol))
