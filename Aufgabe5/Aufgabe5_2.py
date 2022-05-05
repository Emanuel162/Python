from numpy import zeros


def gs():
    n = 30
    iteration = 120
    f = -1.16
    d = 1.0
    e = 0.16
    x = zeros(n)
    for i in range(iteration):
        x[0] = -1*e - f
        for j in range(1, n - 1):
            x[j] = (0 - e * x[j - 1] - f * x[j + 1])
        x[-1] = (-f - e * x[-2])
    return x


if __name__ == '__main__':
    gs()
    print(gs())
