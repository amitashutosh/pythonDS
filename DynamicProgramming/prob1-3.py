"""
Problem:
    T(0) = T(1) = 2
    T(n) = Summation of (2 * T(i-1) * T(i -2)) from (i-1) to (n-1)
"""
def f(n):
    T = [0] * (n+1)
    T[0] = T[1] = 2
    T[2] = 2 * T[0] * T[1]
    for i in range(3, n + 1):
        T[i] = T[i - 1] + 2 * T[i - 1] * T[i - 2]
    print(T)
    return T[n]

print(f(5))
