import numpy as np


def pZerlegung(a):
    p = np.zeros(len(a) - 1, dtype=int)
    for i in range(len(a)):
        row = i
        for l in range(i, len(a)):
            if np.abs(a[l][i]) > np.abs(a[row][i]):
                row = l
        a[[i, row]] = a[[row, i]]
        if i < len(a) - 1:
            p[i] = row
        for k in range(i + 1, len(a)):
            factor = a[k][i] / a[i][i]
            for j in range(i, len(a)):
                a[k][j] -= factor * a[i][j]
                if j == i:
                    a[k][i] = factor
    return a, p

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


def dimensionsmatrix(n):
    matrix = np.zeros((n, n), dtype=float)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j and i < len(matrix) - 1:
                matrix[i][j] = 1
            if j == i - 1:
                matrix[i][j] = -10
            if j == len(matrix) - 1 and i == 0:
                matrix[i][j] = 10
    return matrix


def dimensionsvector(n):
    matrix = np.zeros(n, dtype=float)
    matrix.shape = n
    matrix[0] = 1 + 10
    for i in range(1, len(matrix) - 1):
        matrix[i] = 1 - 10
    matrix[n - 1] = -10
    return matrix


if __name__ == '__main__':
    dimM10 = dimensionsmatrix(10)
    dimV10 = dimensionsvector(10)
    dimM15 = dimensionsmatrix(15)
    dimV15 = dimensionsvector(15)
    dimM20 = dimensionsmatrix(20)
    dimV20 = dimensionsvector(20)
    lu, p = zerlegung(dimM10)
    bperm = permutation(p, dimV10)
    v = vorwaerts(lu, bperm)
    r = rueckwaerts(lu, v)
    print("Loesung mit dim = 10 ohne pivot:")
    print(r)
    lu, p = pZerlegung(dimM10)
    bperm = permutation(p, dimV10)
    v = vorwaerts(lu, bperm)
    r = rueckwaerts(lu, v)
    print("Loesung mit dim = 10 mit pivot:")
    print(r)
    lu, p = zerlegung(dimM15)
    bperm = permutation(p, dimV15)
    v = vorwaerts(lu, bperm)
    r = rueckwaerts(lu, v)
    print("Loesung mit dim = 15 ohne pivot:")
    print(r)
    lu, p = pZerlegung(dimM15)
    bperm = permutation(p, dimV15)
    v = vorwaerts(lu, bperm)
    r = rueckwaerts(lu, v)
    print("Loesung mit dim = 15 mit pivot:")
    print(r)
    lu, p = zerlegung(dimM20)
    bperm = permutation(p, dimV20)
    v = vorwaerts(lu, bperm)
    r = rueckwaerts(lu, v)
    print("Loesung mit dim = 20 ohne pivot:")
    print(r)
    lu, p = pZerlegung(dimM20)
    bperm = permutation(p, dimV20)
    v = vorwaerts(lu, bperm)
    r = rueckwaerts(lu, v)
    print("Loesung mit dim = 20 mit pivot:")
    print(r)

