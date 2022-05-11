import math as m

mg = 1.1 * 10 ** -16


def b(x):
    a = 9.8606
    c = -1.1085 * 10000000000000000000000000.0
    d = 0.029
    return a / (1 - c * m.pow(m.e, -d * x)) - 9


def bDerived(x):
    a = 9.8606
    c = -1.1085 * 10000000000000000000000000.0
    d = 0.029
    return (-1) * (a * c * d * m.pow(m.e, -d * x)) / m.pow((1 - c * m.pow(m.e, -d * x)), 2)


def newton(f, fderived, x):
    iteration = 0
    xtemp = x + mg + 1
    while abs(x - xtemp) > mg:
        iteration += 1
        xtemp = x
        x = x - f(x) / fderived(x)
    return x, 2 * iteration


def sekanten(f, x0, x1):
    iteration = 0
    while abs(x1 - x0) > mg:
        iteration += 1
        xtemp = x1
        x1 = x1 - (((x1 - x0) / (f(x1) - f(x0))) * f(x1))
        x0 = xtemp
    return x1, iteration


if __name__ == '__main__':
    print("Newton:")
    r, i = newton(b, bDerived, 1961)
    print("Ergebnis: ", r, "Iterationen: ", i)
    print("Sekanten:")
    r, i = sekanten(b, 1961, 2000)
    print("Ergebnis: ", r, "Iterationen: ", i)
