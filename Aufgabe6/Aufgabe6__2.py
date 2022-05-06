from numpy import unravel_index, argmax, array, eye, zeros, double


def SummeNeben(A):
    B = A.copy()
    for i in range(len(A)):
        B[i][i] = 0

    return sum(B.flatten() ** 2)


def MaximumNeben(A):
    B = A.copy()
    for i in range(len(A)):
        B[i][i] = 0

    i, j = unravel_index(argmax(abs(B)), B.shape)
    return min(i, j), max(i, j)


def Vor(x):
    if x < 0:
        return -1
    else:
        return 1


def Jacobi(A, n):
    dim = len(A)
    print(A)
    while SummeNeben(A) > n * n:
        [i, j] = MaximumNeben(A)
        a = (A[j, j] - A[i, i]) / (2.0 * A[i, j])
        c = ((1.0 + (a ** 2 / (1.0 + a ** 2)) ** 0.5) / 2.0) ** 0.5
        s = Vor(a) / (2.0 * c * (1.0 + a ** 2) ** 0.5)
        Q = eye(dim)
        Q[i, i] = c
        Q[j, j] = c
        Q[i, j] = s
        Q[j, i] = -s
        A = Q.T.dot(A).dot(Q)
    return A.diagonal()


def dimensionsmatrix(n):
    m = zeros((n, n), dtype=double)
    for i in range(len(m)):
        m[i][i] = 2
        for j in range(len(m)):
            if abs(i - j) == 1:
                m[i][j] = -1
    return m


if __name__ == '__main__':
    matrix = array([[1, 2, 3], [2, 3, 2], [3, 2, 1]], dtype=double)
    print(Jacobi(matrix, 1e-3))

    dim5 = dimensionsmatrix(5)
    print(Jacobi(dim5, 1e-3))
    dim10 = dimensionsmatrix(10)
    print(Jacobi(dim10, 1e-3))
    dim20 = dimensionsmatrix(20)
    print(Jacobi(dim20, 1e-3))
