import numpy as np


def gradient_descent(x, y):
    mCurr = bCurr = 0
    iterations = 100000
    n = len(x)
    learningRate = 0.001
    for i in range(iterations):
        y_predicted = mCurr * x + bCurr
        cost = (1/n) * sum([val**2 for val in (y - y_predicted)])
        mD = -(2/n) * sum(x * (y - y_predicted))
        bD = -(2/n) * sum(y - y_predicted)
        mCurr = mCurr - learningRate * mD
        bCurr = bCurr - learningRate * bD
        print("m {}, b {},cost {}, iteration {}".format(mCurr, bCurr, cost, i))


x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])
gradient_descent(x, y)


# f(x) = y = mx + b
# Finding m and b using given x and y arrays
