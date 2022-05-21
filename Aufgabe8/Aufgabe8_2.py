import numpy as np
import sympy as sp


def f1(v):
    return np.sin(v[0]) - v[1]


def f2(v):
    return np.power(np.e, -v[1]) - v[0]


def f1x(v):
    return np.cos(v[0])


def f1y(v):
    return -1.


def f2x(v):
    return -1.


def f2y(v):
    return -np.power(np.e, -v[1])


def jm(v):
    return np.array([[f1x(v), f1y(v)], [f2x(v), f2y(v)]], dtype=float)


def f(v):
    return np.array([[f1(v)], [f2(v)]], dtype=float)


if __name__ == '__main__':
    x0 = 0.
    y0 = 0.
    x = np.array([x0, y0], dtype=float)

    for i in range(10):
        ft = f(x)
        x = x - np.linalg.solve(jm(x), f(x))[0]
        # x = [x[0] - (jmt[0][0] * ft[0] + jmt[0][1] * ft[1]), x[1] - (jmt[1][0] * ft[0] + jmt[1][1] * ft[1])]
        print("i = ", i + 1, "   xi = ", x)
