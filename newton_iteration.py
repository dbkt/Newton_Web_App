import numpy as np


def newton(f, x0, h=0.001, max_iter=1000, d=0.0001):
    count = 0
    x1 = x0
    sol = [x0]
    while (count < max_iter) & (abs(f(x0)) >= d):
        derivative = (f(x0 + h) - f(x0 - h)) / (2 * h)
        if abs(derivative) <= 0.000000001:
            return x1, -1, f"extrem value in x = {x1} with derivate = {derivative}. "
        x1 = x0 - f(x0) / derivative
        count += 1
        x0 = x1
        sol.append(x0)
    return x1, count, np.array(sol)
