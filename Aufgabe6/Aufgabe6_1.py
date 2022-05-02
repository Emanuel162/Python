import numpy as np


def vektoriteration(a, x, n):
    for i in range(1, n+1):
        x0 = x
        y = np.matmul(a, x)
        x = y / np.linalg.norm(y)
        z = np.dot(x0, y)
        print(f'------ {i}te Wiederholung ------')
        print(f'y = {y}')
        print(f'x = {x}')
        print(f'z(müh) = {z}')
        print()


def main():
    arr = np.array([[4, 2, 1], [2, 4, 2], [1, 2, 4]])
    x = np.array([1, 0, 0])
    vektoriteration(arr, x, 5)


if __name__ == '__main__':
    main()
