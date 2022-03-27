import numpy


def var1(p, q):
    x2 = -p + numpy.sqrt((p ** 2) + q)
    print("Variante 1:")
    print(f"x2: {x2}")


def var2(p, q):
    x3 = -p - numpy.sqrt((p ** 2) + q)
    x4 = -q / x3
    print("Variante 2:")
    print(f"x2: {x4}")


if __name__ == '__main__':
    print("p: 10^2")
    var1(10 ** 2, 1)
    var2(10 ** 2, 1)
    print("p: 10^4")
    var1(10 ** 4, 1)
    var2(10 ** 4, 1)
    print("p: 10^6")
    var1(10 ** 6, 1)
    var2(10 ** 6, 1)
    print("p: 10^7")
    var1(10 ** 7, 1)
    var2(10 ** 7, 1)
    print("p: 10^8")
    var1(10 ** 8, 1)
    var2(10 ** 8, 1)

    # Der Alternativalgorithmus ist damit genauer
