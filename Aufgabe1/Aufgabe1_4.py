import numpy


def funkt1(x):
    return 1 / (x ** 2)


def funkt2(x):
    return numpy.log(x)


def trapez(f, a, b, n):
    i = 1
    arr = numpy.arange(1, n, 1, float)
    h = (b - a) / n
    while i < n:
        arr[i - 1] = a + i * h
        i += 1
    arr = f(arr)
    res = h / 2 * (f(a) + 2 * sum(arr) + f(b))
    print(f"Trapez: {res}")


if __name__ == '__main__':
    trapez(funkt1, 1 / 10, 10, 10000)
    trapez(funkt2, 1, 2, 10000)