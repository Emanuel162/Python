import math

import numpy as np


def var1(x, n):
    i = 0
    res = 0
    while i <= n:
        res += (x ** i) / math.factorial(i)
        i += 1
    print(f"Var1: {res}")


def var2(x, n):
    i = 1
    res = 0
    while i <= n:
        res += (x ** (n - i)) / math.factorial(n - i)
        i += 1
    print(f"Var2: {res}")


if __name__ == '__main__':
    xarray = np.array([1, 5, 7, 10])
    narray = np.array([10, 100, 1000])
    for xwert in xarray:
        for nwert in narray:
            print("------ x:", xwert, "-- n:", nwert, "------")
            print("Unterschied:", var1(xwert, nwert))
            print("Unterschied:", var2(xwert, nwert))
