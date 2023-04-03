import numpy as np
import math
import matplotlib.pyplot as plt

# Function def. for 2^(0.5) when F(x) = 0


def F(x): return x**2 - 2

# Bisection method function
# Having tolerance -> 10^(-4)
# Count all iterations until you reach a value that is bigger than given tol !!!!
# Send your interval values to the function such as " a and b" including ur tolerance


def BisectionFunc(a, b, tol, counter):
    # It is always needed to control signs in this alghorithm

    if (F(a) * F(b) >= 0):
        raise ("The signs are inaccurate!!!")
   # Then divide the interval by 2, and check if their signs are opposite do that again!!
   # Repeat until your absolute error becomes smaller than your tolerance

    while (abs(b - a) > tol):

        c = (a + b) / 2

        if (F(c) == 0):
            return c
        elif (F(a) * F(c) < 0):
            b = c
        else:
            a = c
        counter += 1
    return (a + b) / 2, counter


# Identify your initial values for a and b.
# If you don't know the excat interval. You must find out what values could fit with the soln.
# If 2^(0.5) is your root, then you can assume your interval values as 1 , 2.
# 1 < your root < 2 (Your root = 2^(0.5))
# Counter variable: It's going to count how many times loop is iterated
counter_for_Bis = 0

a = 1
b = 2

tol = 10**(-4)

# Here's the result

result, counter_for_Bis = BisectionFunc(a, b, tol, counter_for_Bis)

print("Your(Bisection method) approximation is {}, {} many times iterated".format(
    result, counter_for_Bis))


#####################################################################################

# Secant Method is one of the simplest method to understand and implement it on the computer.
# It's similar to Newton's approximation method, It's a variance of it in fact.
# In this method, You're going to use given formula  x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0)).
# By this formula, You can approximate the soln and return x2 after your loop condition terminates.
# The condution rule is similar to Bisection method used from above!!


# Send your first initial values as " x0 and x1 " with your tolerance and counter variable

def SecantFunc(x0, x1, tol, counter):

    while (abs(x1 - x0) >= tol):
        # Implement your formula. However, It's a good idea to make it a bit simpler than the current form
        # Numerator var: f(x1) * (x1 - x0)
        # Denumerator var: (f(x1) - f(x0)
        num = F(x1) * (x1 - x0)
        denum = F(x1) - F(x0)
        x2 = x1 - (num / denum)
        # Then your new x0 becomes x1 and x1 becomes x2
        x0 = x1
        x1 = x2
        counter += 1
    return x2, counter


# Counter variable for Secant Method...
counter_for_Sec = 0

# Initial values
x0 = 1
x1 = 2

Secant_result, counter_for_Sec = SecantFunc(x0, x1, tol, counter_for_Sec)

print("Your(Secant method) approximation is {}, {} many times iterated".format(
    Secant_result, counter_for_Sec))


#####################################################################################

# Fixed Point method Alghorithm
# First, find a G(x) function that satisfies x = G(x)
# If our function is given as x**(2) - 2
# Then G(x) can be rearranged as G(x) = x - (x^2 - 2) / 2x, it satisfies that x = sqrt(2)

def G(x):
    eqn = x - ((x**2 - 2) / 2*x)
    return eqn

# Your condition is abs(F(x1)) <= tol


def Fixed_point_method(x0, tol, N, counter):
    counter = 1
    condition = True

    while condition:
        # x1 value: fixed point at G(x)
        x1 = G(x0)
        x0 = x1
        counter += 1

        if (counter > N):
            print("Divergent!!!")
            break
        condition = abs(F(x1)) > tol
    return x1, counter


# Critical variables for fixed points.

N = 20
# We assume the initial value between 1 and 2
x0 = 1.5
# Counter var for Fixed Point method
counter_for_Fixed = 0

Fixed_result, counter_for_Fixed = Fixed_point_method(
    x0, tol, N, counter_for_Fixed)

print("Your(Fixed Method) approximation is {}, {} many times iterated".format(
    Fixed_result, counter_for_Fixed))


#############################################################################

# Newton's method Alghorithm.
# First use the formula as 𝑥𝑛+1 = 𝑥𝑛 −(𝑓(𝑥𝑛) / 𝑔(𝑥𝑛)).
# Where 𝑔(𝑥𝑛) = (𝑓(𝑥𝑛 + 𝑓(𝑥𝑛)) − 𝑓(𝑥𝑛)) / 𝑓(𝑥𝑛)
# Define an G(x) and apply the rule

def G1(x):
    return 2*x


def NewtonRaphsonFunc(x0, tol, N, counter):
    counter = 1
    condition = True
    while condition:
        if (G1(x0) == 0.0):
            raise ValueError("Divide by zero error!!!!")
        x1 = x0 - F(x0) / G1(x0)
        x0 = x1

        counter += 1
        if (counter > N):
            print("Divergent!!!")
        condition = abs(F(x1)) > tol
        return x1, counter


# Counter var for Newton's method
counter_for_Newton = 0

Newton_result, counter_for_Newton = NewtonRaphsonFunc(
    x0, tol, N, counter_for_Newton)

print("Your(Newton's Method) approximation is {}, {} many times iterated".format(
    Newton_result, counter_for_Newton))


print("Newton's method is the fastest method here!!!! by {} times iterated".format(
    counter_for_Newton))
