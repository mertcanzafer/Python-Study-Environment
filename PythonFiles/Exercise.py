import numpy as np
import matplotlib
from scipy import optimize
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True


def f(x): return np.cos(x) - x

# ----------------------------------------


def plot_Graph():
    x = np.linspace(-1, 1.5, 100)
    plt.plot(x, f(x), color='black')
    plt.show()


# -----------------------------------------
r = optimize.fsolve(f, -2)

print(" r = ", r)
# Verify the soln is a root or not

soln = f(r)

print("The result is ", soln)

plot_Graph()
