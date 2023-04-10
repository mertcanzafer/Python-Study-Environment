import numpy as np
import math
import matplotlib.pyplot as plt


# Function def. for 2^(0.5) when F(x) = 0


def F(x): return x**2 - 2


def G(x):
    eqn = x - ((x**2 - 2) / 2*x)
    return eqn


def Fixed_point_method(x0, tol, N, counter):

    counter = 1
    condition = True
    while condition:
        x1 = G(x0)
        x0 = x1
        counter += 1
        if (counter > N):
            print("Divergent!!!")
            break
        condition = abs(F(x1)) > tol
    return x1, counter


counter_for_fixed = 0
N = 20
x0 = 1.5
tol = 10**(-4)

result, counter_for_fixed = Fixed_point_method(x0, tol, N, counter_for_fixed)

print("Your(Secant method) approximation is {}, {} many times iterated".format(
    result, counter_for_fixed))
