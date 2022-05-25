import numpy as np
from numpy.linalg import solve


def createPointsAndA():
    length = 7
    xis = np.zeros(length, dtype=float)
    yis = np.zeros(length, dtype=float)
    for i in range(length):
        xis[i] = 10 ** (i + 1 - 7)
        yis[i] = xis[i] + 1
    grad = 6
    a = np.zeros((len(xis), grad), dtype=float)
    for i in range(len(xis)):
        for j in range(grad):
            a[i][j] = xis[i] ** j
    return xis, yis, a


def normalgleichung(yis, a):
    at = a.transpose()
    ata = np.matmul(at, a)
    atb = np.matmul(at, yis)
    res = solve(ata, atb)
    return res


def getFunction(function):
    func = ""
    for i in range(len(function)):
        func += f'{function[i]} * x**{i}'
        if i < len(function) - 1:
            func += " + "
    return func


def householder(yis, a):
    q, r = np.linalg.qr(a)
    b = np.asarray(yis)
    qtb = np.dot(q.T, b)
    x = solve(r, qtb[:len(yis)])
    return x


def cglsVerfahren(yis, a):
    x = np.zeros(a.shape[1])
    s = yis - a.dot(x)
    r = np.matmul(a.T, s)
    p = r
    n = 1
    while n <= a.shape[0]:
        n = n + 1
        alpha = np.matmul(r, r) / np.matmul(np.matmul(a, p), np.matmul(a, p))
        x = x + alpha * p
        s = s - alpha * np.matmul(a, p)
        r_alt = r
        r = np.matmul(a.T, s)
        beta = np.matmul(r, r) / np.matmul(r_alt, r_alt)
        p = r + beta * p
    return x


def main():
    xis, yis, a = createPointsAndA()

    print()
    print("Normalgleichung:")
    normal = normalgleichung(yis, a)
    print(f' Array = {normal}')
    print(f'f(x) = {getFunction(normal)}')

    print()
    print("Householder-Verfahren")
    hhg = householder(yis, a)
    print(f'x = {hhg}')
    print(f'f(x) = {getFunction(hhg)}')

    print()
    print("CGLS-Verfahren")
    cgls = cglsVerfahren(yis, a)
    print(f'x = {cgls}')
    print(f'f(x) = {getFunction(cgls)}')

    print()
    print("Ergebnis:")
    print(
        "Mit Abstand am besten war Householder, gefolgt vom CGLS-Verfahren. Zuletzt kommt das Verfahren für vorhandene Standardlöser in numpy.")


if __name__ == "__main__":
    main()
