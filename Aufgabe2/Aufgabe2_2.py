import numpy
import numpy as np


def gauss(a, b):
    x = 0

    print(a)
    print(b)
    print("-------------")
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i + 1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    b[i], b[j] = b[j], b[i]
                    print("hello")
                    break

        if a[i][i] != 1:
            b[i] = b[i] / a[i][i]
            a[i] = a[i] / a[i][i]

        for j in range(i + 1, len(a)):
            if a[j][i] != 0:
                b[j] -= a[j][i] * np.asarray(b[i])
                a[j] -= a[j][i] * np.asarray(a[i])
    print(a)
    print(b)

    return x


# def dimensionsmatrix(n):
#     matrix = np.zeros((n, n), dtype=float)
#     for i in range(1, len(matrix)):
#         for j in range(1, len(matrix)):
#             matrix[i][j] = 1 / i + j - 1
#     return matrix
#
#
# def dimensionsvector(n):
#     matrix = np.zeros(n, dtype=float)
#     matrix.shape = n
#     for i in range(1, len(matrix)):
#         matrix[i] = 1 / i + 1
#     return matrix


arr = np.array([[1, 3, 1, 1], [0, 1, 0, 2], [2, 1, 0, 0], [0, 4, 4, 0]], dtype=float)
vector = np.array([6, 2, 4, 12], dtype=float)
# print(gauss(arr, vector))
dimM5 = [[1, 1 / 2, 1 / 3, 1 / 4, 1 / 5], [1 / 2, 1 / 3, 1 / 4, 1 / 5, 1 / 6], [1 / 3, 1 / 4, 1 / 5, 1 / 6, 1 / 7],
         [1 / 4, 1 / 5, 1 / 6, 1 / 7, 1 / 8], [1 / 5, 1 / 6, 1 / 7, 1 / 8, 1 / 9]]
dimV5 = [1 / 2, 1 / 3, 1 / 4, 1 / 5, 1 / 6]
print(gauss(dimM5, dimV5))
