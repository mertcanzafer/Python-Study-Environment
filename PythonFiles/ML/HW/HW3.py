import pandas as pd
import numpy as np
import math

# Read the data from the CSV file
df = pd.read_csv("test_scores.csv")

# Convert columns to NumPy arrays
x = np.array(df['math'])
y = np.array(df['cs'])


def gradient_descent(x, y):
    mCurr = bCurr = 0
    tol = 1e-09
    n = len(x)
    learningRate = 0.01
    curCost = prevCost = 0
    iterationCount = 0

    while True:
        y_predicted = mCurr * x + bCurr  # Element-wise multiplication and addition
        prevCost = curCost
        # Compute cost
        curCost = (1/n) * sum([val**2 for val in (y - y_predicted)])

        # Compute gradients
        mD = -(2/n) * sum(x * (y - y_predicted))
        bD = -(2/n) * sum(y - y_predicted)

        # Update parameters
        mCurr -= learningRate * mD
        bCurr -= learningRate * bD
        iterationCount += 1

        if math.isclose(prevCost, curCost, rel_tol=tol):  # Ensure correct tolerance checking
            break

    print(
        f"Iterations: {iterationCount}, m: {mCurr}, b: {bCurr}, Cost: {curCost}")


gradient_descent(x, y)
