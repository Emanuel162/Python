import numpy as np


def gauss(a, b):
    print(a)
    print(b)
    print("-------------")

    l = np.zeros(len(a) - 1, dtype=float)
    u = np.zeros(len(a) - 1, dtype=float)
    d = np.zeros(len(a), dtype=float)
    l.shape = len(a) - 1
    u.shape = len(a) - 1
    d.shape = len(a)
    for i in range(len(a) - 1):
        d[i] = a[i][i]
        l[i] = a[i + 1][i]
        u[i] = a[i][i + 1]
    d[len(a) - 1] = a[len(a) - 1][len(a) - 1]

    for i in range(len(d)):
        if d[i] != 1:
            b[i] = b[i] / d[i]
            if i < len(d) - 1:
                u[i] = u[i] / d[i]
            d[i] = 1

        if i < len(d) - 1:
            if l[i] != 0:
                b[i + 1] -= l[i] * np.asarray(b[i])
                d[i + 1] -= l[i] * np.asarray(u[i])
                l[i] -= l[i] * np.asarray(d[i])

    for i in range(len(u)):
        if u[len(u) - 1 - i] != 0:
            b[len(u) - 1 - i] -= u[len(u) - 1 - i] * np.asarray(b[len(u) - i])
            u[len(u) - 1 - i] = 0
    print(u)
    print(d)
    print(l)
    return b


def dimensionsmatrix(n):
    m = np.zeros((n, n), dtype=float)
    for i in range(len(m) - 1):
        m[i][i] = -2
        m[i + 1][i] = 1
        m[i][i + 1] = 1
    m[n - 1][n - 1] = -2
    return m


def dimensionsvector(n):
    v = np.zeros(n, dtype=float)
    v.shape = n
    for i in range(len(v)):
        v[i] = 1 / (n + 1) ** 2
    return v


if __name__ == '__main__':
    arr = dimensionsmatrix(100)
    vector = dimensionsvector(100)
    print(gauss(arr, vector))
    arr = dimensionsmatrix(1000)
    vector = dimensionsvector(1000)
    print(gauss(arr, vector))
    arr = dimensionsmatrix(10000)
    vector = dimensionsvector(10000)
    print(gauss(arr, vector))
