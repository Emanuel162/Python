import numpy as np
from numpy.linalg import solve


def f(x):
    return 1 / (1 + x ** 2)


def createPoints(m):
    xis = np.zeros(m)
    for i in range(m):
        xis[i] = 10 * i / (m - 1) - 5
    yis = np.zeros(m)
    for x in range(len(xis)):
        yis[x] = f(xis[x])
    return xis, yis


def splines(xis, yis):
    a = np.zeros((len(xis) - 2, len(xis) - 2))
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
    a[len(xis) - 3][len(xis) - 4] = h_neu
    h_alt = h_neu
    h_neu = xis[-1] - xis[len(xis) - 2]
    a[-1][-1] = 2 * (h_neu + h_alt)
    gamma = np.zeros(len(yis) - 2)
    for i in range(len(yis) - 2):
        gamma[i] = 6 * ((yis[i + 1] - yis[i]) / (xis[i + 1] - xis[i]) - (yis[i] - yis[i - 2]) / (xis[i] - xis[i - 1]))
    # print("gamma = ", gamma)
    beta = np.zeros(len(gamma) + 2)
    beta[1:-1] = solve(a, gamma)
    # print("beta = ", beta)
    alpha = np.zeros(len(beta) - 1)
    for i in range(len(alpha)):
        alpha[i] = (yis[i + 1] - yis[i]) / (xis[i + 1] - xis[i]) - beta[i] * (xis[i + 1] - xis[i]) / 3 - beta[i + 1] * (
                xis[i + 1] - xis[i]) / 6
    # print("alpha = ", alpha)

    for i in range(len(xis) - 1):
        s3 = f'{yis[i]} + {alpha[i]}*(x - {xis[i]}) + {beta[i] / 2} * (x - {xis[i]})^2 + {(beta[i + 1] - beta[i]) / 6 * (xis[i + 1] - xis[i])} * (x - {xis[i]})^3'
        print(f's3 auf dem Interval [{xis[i]}, {xis[i+1]}] : {s3}.')
    return a


def main():
    ms = [5, 7, 9, 11, 17]
    for m in ms:
        print()
        print(f'm = {m}')
        xis, yis = createPoints(m)
        splines(xis, yis)


if __name__ == "__main__":
    main()
