import numpy as np
import math
import matplotlib.pyplot as plt


def F(x): return (3*x + 3) * (x - 0.5) * (x - 1)


def Bisection_Function(a, b, F):
    # In bisection method, First control that f(a) . f(b) < 0 or not
    start = 1
    end = 4

    if (F(a) * F(b) >= 0):
        raise ValueError("The signs must be opposite to each other!!!!")

    while (start < end):

        c = (a + b) / 2

        if F(c) == 0:
            return c
        elif (F(a) * F(c) < 0):
            b = c
        else:
            a = c
        start += 1

    return (a + b) / 2

# Define the interval


a = -2
b = 1.5


result = Bisection_Function(a, b, F)

print("The root is approximately: ", result)


def Plot_A_Graph(F):
    x = np.linspace(-2, 2, 100)

    # Plot the function

    plt.plot(x, F(x), 'b-', label='F(x)')

    # Plot the root found using the Bisection method

    plt.plot(result, 0, 'ro', label='Root')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()

    # Show the plot

    plt.plot(x, F(x), color='black')

    plt.show()


Plot_A_Graph(F)
