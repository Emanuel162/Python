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
                # print(f'difs[{i}][{j}] = {difs[i][j]}')

        counter = counter + 1
    res = np.zeros(len(x_werte))
    for i in range(len(x_werte)):
        res[i] = difs[i][0]
    # print(f'div. Differenzen Diagonale: {res}')
    return res


def hornerSchema(x_werte, dividierte, x):
    res = 0
    for i in reversed(range(1, len(x_werte))):
        res += dividierte[i]

        for j in x_werte-1:
            res *= (x-x_werte[j])
        print(res)
    return res


def main():
    x_werte = np.array([0, 1, 3])
    y_werte = np.array([3, 2, 6])
    dividierte = dividierteDifferenzen(x_werte, y_werte)
    x = 2
    print(f'Das Interpolationspolynom an der Stelle x = {x} ist {hornerSchema(x_werte, dividierte, x)}.')


if __name__ == '__main__':
    main()
