import numpy as np


def zerlegung(a):
    p = np.zeros(len(a) - 1, dtype=int)
    for i in range(len(a)):
        if a[i][i] == 0:
            found = False
            counter = 1
            while not found:
                if a[i + counter][i] != 0:
                    p[i] = i + counter
                    a[[i, i + counter]] = a[[i + counter, i]]
                    found = True
            counter += 1
        elif i < len(a) - 1:
            print(a)
            p[i] = i
        for k in range(i + 1, len(a)):
            factor = a[k][i] / a[i][i]
            for j in range(i, len(a)):
                a[k][j] -= factor * a[i][j]
                if j == i:
                    a[k][i] = factor
    return a, p


def permutation(p, x):
    for i in range(len(x) - 1):
        x[[i, p[i]]] = x[[p[i], i]]
    return x


def vorwaerts(a, x):
    y = x
    for i in range(len(a)):
        for j in range(i):
            y[i] -= a[i][j] * y[j]
    return y


def rueckwaerts(a, x):
    y = np.zeros(len(a), dtype=float)
    for i in range(len(a)):
        enumerator = x[len(a) - i - 1]
        for j in range(i):
            enumerator -= a[len(a) - i - 1][len(a) - j - 1] * y[len(a) - j - 1]
        y[len(a) - i - 1] = enumerator / a[len(a) - i - 1][len(a) - i - 1]
    return y


if __name__ == '__main__':
    arr = np.array([[0, 0, 0, 1], [2, 1, 2, 0], [4, 4, 0, 0], [2, 3, 1, 0]], dtype=float)
    print(arr)
    b = np.array([3, 5, 4, 5], dtype=float)
    lu, p = zerlegung(arr)
    print(lu)
    bperm = permutation(p, b)
    v = vorwaerts(lu, bperm)
    r = rueckwaerts(lu, v)
    print(r)
