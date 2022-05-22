import math

import numpy as np


def dividierteDifferenzen(x_werte, y_werte):
    counter = 1
    difs = np.zeros((len(x_werte), len(x_werte)))

    for i in range(len(y_werte)):
        difs[i][i] = y_werte[i]

    for i in range(len(x_werte)):
        for j in reversed(range(counter)):
            if i != j:
                difs[i][j] = (difs[i][j + 1] - difs[i - 1][j]) / (x_werte[i] - x_werte[j])
        counter = counter + 1
    res = np.zeros(len(x_werte))
    for i in range(len(x_werte)):
        res[i] = difs[i][0]
    return res


def hornerSchema(x_werte, dividierte, x):
    res = 0
    for i in reversed(range(1, len(x_werte))):
        res += dividierte[i]

        for j in range(len(x_werte) - 1):
            res *= (x - x_werte[j])
        res += dividierte[i - 1]
    return res


def hornerSchemaFunction(x_werte, dividierte):
    res = ""
    for i in reversed(range(1, len(x_werte))):
        res += f'{dividierte[i]}'

        for j in range(len(x_werte) - 1):
            if x_werte[j] > 0:
                res += f'*(x-{x_werte[j]})'
            elif x_werte[j] == 0:
                res += f'*x'
            else:
                res += f'*(x{x_werte[j]})'

        res += f'+{dividierte[i - 1]}'
    return res


def f(x):
    return 1 / (1 + x ** 2)


def createPoints_b(m):
    xis = np.zeros(m)
    for i in range(m):
        xis[i] = 10 * i / (m - 1) - 5
    yis = np.zeros(m)
    for x in range(len(xis)):
        yis[x] = f(xis[x])
    return xis, yis


def createPoints_c(m):
    xis = np.zeros(m)
    for i in range(m):
        xis[i] = -5 * math.cos(math.pi * (2 * i + 1) / 2 * m)
    yis = np.zeros(m)
    for x in range(len(xis)):
        yis[x] = f(xis[x])
    return xis, yis


def main():
    print("--------------- Aufgabenteil a ---------------")
    x_werte = np.array([0, 1, 3])
    y_werte = np.array([3, 2, 6])
    dividierte = dividierteDifferenzen(x_werte, y_werte)
    x = 2
    print(f'Das Interpolationspolynom an der Stelle x = {x} ist {hornerSchema(x_werte, dividierte, x)}.')

    print()
    print("--------------- Aufgabenteil b ---------------")

    liste = [3, 5, 7, 9, 11, 13]

    for i in liste:
        xis, yis = createPoints_b(i)
        dividierteDiag = dividierteDifferenzen(xis, yis)
        print(f'Das Interpolationspolynom mit {i} Schnittstellen ist {hornerSchemaFunction(xis, dividierteDiag)}.')
    # Je höher das m wird, desto stärker weicht das Interpolationspolynom von der eigentlichen Funktion außerhalb der Schnittstellen xi ab.

    print()
    print("--------------- Aufgabenteil c ---------------")
    liste = [9, 11, 13]

    for i in liste:
        xis, yis = createPoints_c(i)
        dividierteDiag = dividierteDifferenzen(xis, yis)
        print(f'Das Interpolationspolynom mit {i} Schnittstellen ist {hornerSchemaFunction(xis, dividierteDiag)}.')


if __name__ == '__main__':
    main()
