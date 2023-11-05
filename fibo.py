# Title: CS 2500 HW 1 - Fibbonacci
# Author: Will Weidler
# Date: 11/2/23

ArrayP = [[0, 1], [1, 1]]

def fibo(n, count=None):
    if count is None:
        count = [0] * (n + 1)

    if n <= 1:
        count[n] += 1
        return n

    count[n] += 1
    return fibo(n - 1, count) + fibo(n - 2, count)


def naive_matrix_mult(P, Q, count):
    a, b = len(P), len(P[0])
    g, h = a, b
    result = [[0 for _ in range(b)] for _ in range(a)]

    for m in range(a):
        for r in range(h):
            for k in range(g):
                result[m][r] += P[m][k] * Q[k][r]
                count += 1

    return result, count

def matrix_power(P, num):
    if num == 1:
        return P, 0

    result = P
    count = 0
    for _ in range(num - 1):
        result, count = naive_matrix_mult(P, result, count)

    return result, count



def main():
    FiboNum = int(input())
    count = [0] * (FiboNum + 1)
    result = fibo(FiboNum, count)
    print(count[1])
    for i in range(FiboNum + 1):
        print(f"fibo({i}) : {count[i]}")
    result, count = matrix_power(ArrayP, FiboNum)
    print(count)


if __name__ == "__main__":
    main()