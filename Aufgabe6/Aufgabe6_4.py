from numpy import array, double, zeros, eye
from numpy.linalg import qr


def SummeNeben(A):
    B = A.copy()
    for i in range(len(A)):
        B[i][i] = 0

    return sum(B.flatten() ** 2)


def QR(A, n):
    V = eye(len(A))
    while SummeNeben(A) > n * n:
        Q, R = qr(A)
        V = V.dot(Q)
        A = R.dot(Q)
    return A.diagonal(), V


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
    print("Eigenwerte:")
    print(QR(matrix, 1e-3)[0])
    print("Eigenvektoren:")
    print(QR(matrix, 1e-3)[1])
    print("+-------------------------------------------------------------------------------------+")

    print("Eigenwerte:")
    dim5 = dimensionsmatrix(5)
    print(QR(dim5, 1e-3)[0])
    print("Eigenvektoren:")
    print(QR(dim5, 1e-3)[1])
    print("+-------------------------------------------------------------------------------------+")
    print("Eigenwerte:")
    dim10 = dimensionsmatrix(10)
    print(QR(dim10, 1e-3)[0])
    print("Eigenvektoren:")
    print(QR(dim10, 1e-3)[1])
    print("+-------------------------------------------------------------------------------------+")
    print("Eigenwerte:")
    dim20 = dimensionsmatrix(20)
    print(QR(dim20, 1e-3)[0])
    print("Eigenvektoren:")
    print(QR(dim20, 1e-3)[1])