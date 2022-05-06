from numpy import array, double, zeros
from numpy.linalg import qr

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
    print(qr(matrix))
