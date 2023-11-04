# Title: CS 2500 HW 1 - Fibbonacci
# Author: Will Weidler
# Date: 11/2/23


def fibo(n, count=None):
    if count is None:
        count = [0] * (n + 1)

    if n <= 1:
        count[n] += 1
        return n

    count[n] += 1
    return fibo(n - 1, count) + fibo(n - 2, count)


def naive_matrix_mult(P, num):
    a, b = len(P), len(P[0])
    g, h = a, b
    c = 0

    Q = [[0 for _ in range(h)] for _ in range(a)]

    while num > 0:
        for m in range(a):
            for r in range(h):
                for k in range(g):
                    Q[m][r] += P[m][k] * P[k][r]
                    c += 1
        num -= 1

    return c


def main():
    FiboNum = int(input())
    count = [0] * (FiboNum + 1)
    result = fibo(FiboNum, count)
    print(count[1])
    for i in range(FiboNum + 1):
        print(f"fibo({i}) : {count[i]}")
    ArrayS = [[fibo(FiboNum - 1), fibo(FiboNum)], [fibo(FiboNum), fibo(FiboNum + 1)]]
    ArrayP = [[0, 1], [1, 1]]
    print(naive_matrix_mult(ArrayP, FiboNum))


if __name__ == "__main__":
    main()
