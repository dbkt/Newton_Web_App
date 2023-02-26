import numpy as np


def newton(f, x0, h=0.001, max_iter=1000, d=0.0001):
    count = 0
    x1 = x0
    sol = [x0]
    adj_list = []
    while (count < max_iter) & (abs(f(x0)) >= d):
        derivative = (f(x0 + h) - f(x0 - h)) / (2 * h)
        adj = - f(x0) / derivative
        adj_list.append(adj)
        x1 = x0 + adj
        count += 1
        x0 = x1
        sol.append(x0)
    return x1, count, np.array(sol), np.array(adj_list)
