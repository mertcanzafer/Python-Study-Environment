import numpy as np
import matplotlib.pyplot as plt
import math

# Defining the function


def F(x):
    return x ** 2 - 3


def BisectionFunc(F, tol, a, b):
    # In bisection method, First control that f(a) . f(b) < 0 or not

    if F(a) * F(b) >= 0:
        raise ValueError("The signs must be opposite to each other!!!!")

    while (abs(b - a) > tol):

        mid = (a + b) / 2

        if (F(mid) == 0):
            return mid
        elif (F(a) * F(mid) < 0):
            b = mid
        else:
            a = mid

    return (a + b) / 2

# Let's define the interval at [1, 2]


a = 1
b = 2

# abs(b - a) < tol
tolerance = 10**(-4)

# Calling the function and finding the root

soln = BisectionFunc(F, tolerance, a, b)

print("The square root of 3 is approximately: ", soln)


def Plot_A_Graph(F):
    x = np.linspace(0, 3, 100)

    # Plot the function

    plt.plot(x, F(x), 'b-', label='F(x)')

    # Plot the root found using the Bisection method

    plt.plot(soln, 0, 'ro', label='Root')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()

    # Show the plot

    plt.plot(x, F(x), color='blue')
    plt.show()


Plot_A_Graph(F)
