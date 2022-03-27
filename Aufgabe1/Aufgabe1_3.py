from numpy import log


def linksseitig(f, a, b, n):
    h = (b - a) / n
    res = 0
    for i in range(n):
        res += f(a + i * h)

    return res * h


def rechtsseitig(f, a, b, n):
    h = (b - a) / n
    res = 0
    for i in range(1, n + 1):
        res += f(a + i * h)

    return res * h


def trapez(f, a, b, n):
    h = (b - a) / n
    res = 0
    for i in range(1, n):
        res += f(a + i * h)
    res *= 2
    res += f(a) + f(b)
    return h * res / 2


def funktion1(x):
    return 1 / pow(x, 2)


def funktion2(x):
    return log(x)


print("----- Funktion1 -------")
print("linksseitig:", linksseitig(funktion1, 1 / 10, 10, 10000))
print("trapez:", trapez(funktion1, 1 / 10, 10, 10000))
print("rechtsseitig:", rechtsseitig(funktion1, 1 / 10, 10, 10000))
print("Exakte Lösung: 9,9")
print("")
print("----- Funktion2 -------")
print("linksseitig:", linksseitig(funktion2, 1, 2, 10000))
print("trapez:", trapez(funktion2, 1, 2, 10000))
print("rechtsseitig:", rechtsseitig(funktion2, 1, 2, 10000))
print("Exakte Lösung: 0.3862943611198906")