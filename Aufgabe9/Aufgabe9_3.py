from math import sin, pi, cos

from numpy import zeros, ndarray
from numpy.linalg import solve


def x(t):
    return t + sin(2 * pi * t) / ((t ** 2) + 1)


def y(t):
    return cos(2 * pi * t) / (2 * (t ** 2) + 1)


def createPoints(m):
    tis = zeros(m)
    for i in range(m):
        tis[i] = 2 * (i - 1) / (m - 1)
    print("tis = ", tis)
    gamma = ndarray((2, len(tis)))
    for i in range(gamma.shape[1]):
        gamma[0][i] = x(tis[i])
        gamma[1][i] = y(tis[i])
    return tis, gamma


def splines(xis, yis, s):
    a = zeros((len(xis) - 2, len(xis) - 2))
    h_alt = xis[1] - xis[0]
    h_neu = xis[2] - xis[1]
    a[0][0] = 2 * (h_neu + h_alt)
    a[0][1] = h_neu
    for i in range(1, len(xis) - 3):
        h_alt = h_neu
        h_neu = xis[i + 1] - xis[i]
        a[i][i - 1] = h_alt
        a[i][i] = 2 * (h_neu + h_alt)
        a[i][i + 1] = h_neu
    # print(len(xis) - 2)
    a[len(xis) - 3][len(xis) - 4] = h_neu
    h_alt = h_neu
    h_neu = xis[-1] - xis[len(xis) - 2]
    a[-1][-1] = 2 * (h_neu + h_alt)
    gamma = zeros(len(yis) - 2)
    for i in range(len(yis) - 2):
        gamma[i] = 6 * ((yis[i + 1] - yis[i]) / (xis[i + 1] - xis[i]) - (yis[i] - yis[i - 2]) / (xis[i] - xis[i - 1]))
    # print("gamma = ", gamma)
    beta = zeros(len(gamma) + 2)
    beta[1:-1] = solve(a, gamma)
    # print("beta = ", beta)
    alpha = zeros(len(beta) - 1)
    for i in range(len(alpha)):
        alpha[i] = (yis[i + 1] - yis[i]) / (xis[i + 1] - xis[i]) - beta[i] * (xis[i + 1] - xis[i]) / 3 - beta[i + 1] * (
                xis[i + 1] - xis[i]) / 6
    # print("alpha = ", alpha)

    for i in range(len(xis) - 1):
        s3 = f'{yis[i]} + {alpha[i]}*(x - {xis[i]}) + {beta[i] / 2} * (x - {xis[i]})^2 + {(beta[i + 1] - beta[i]) / 6 * (xis[i + 1] - xis[i])} * (x - {xis[i]})^3'
        print(f'{s} auf dem Interval [{xis[i]}, {xis[i + 1]}] : {s3}.')
    return a


def main():
    tis, gamma = createPoints(5)
    print(gamma)
    print("sx")
    sx = splines(tis, gamma[0], "sx")
    print("sy")
    sy = splines(tis, gamma[1], "sy")


if __name__ == '__main__':
    main()
