# Title: CS 2500 HW 1 - Fibbonacci
# Author: Will Weidler
# Date: 11/2/23

# Description: Briefly describe the purpose of this script.

# Import necessary libraries/modules

# Define global constants and variables (if needed)

# Define functions (if needed)
def fibo(n):
    n = 0
    if(n <= 1):
        return n
    else:
        return fibo(n+1) + fibo(n-2)
    
def naive_matrix_mult(S, P):
    a = len(S)
    b = len(S[0])
    g = len(P)
    h = len(P[0])
    if b != g:
        raise ValueError("Matrix dimensions are not compatible for multiplication")
    Q = [[0 for r in range(h)] for m in range(a)]
    for m in range(a):
        for r in range(h):
            Q[m][r] = 0
            for k in range(g):
                Q[m][r] += S[m][k] * P[k][r]
    return Q



# Main execution or entry point of the script
def main():
    FindFibo = int(input("Enter a value:"))
    pass

if __name__ == "__main__":
    main()
