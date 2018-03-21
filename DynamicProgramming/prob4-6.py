"""
    Maximum value contiguous subsequence:
        Given an array of n numbers, give an algorithm for finding a contiguous subsequence A(i)....A(j)
        for which the sum of elements is maximum.
"""

#1 Brute force solution
def MaxContiguousSumBF(A):
    maxSum = 0
    n = len(A)
    for i in range(1, n):
        for j in range(i, n):
            currentSum = 0
            for k in range(i, j+1):
                currentSum += A[k]
                if(currentSum > maxSum):
                    maxSum = currentSum
    return maxSum
A = [-2, 3, -16, 100, -4, 5]
print(MaxContiguousSumBF(A))

#2 Time Complexity: O(n) and Space complexity: O(n)
def MaxContiguousSum2(A):
    maxSum = 0
    n = len(A)
    M = [0] * (n+1)
    if (A[0] > 0):
        M[0] = A[0]
    else: M[0] = 0
    for i in range(1, n):
        if (M[i-1] + A[i] > 0):
            M[i] = M[i-1] + A[i]
        else: M[i] = 0
    for i in range(0, n):
        if (M[i] > maxSum):
            maxSum = M[i]
    return maxSum
A = [-2, 3, -16, 100, -4, 5]
print(MaxContiguousSum2(A))

#3 Time Complexity: O(n) and Space complexity: O(1)
def MaxContiguousSum(A):
    sumSoFar = sumEndingHere = 0
    n = len(A)
    for i in range(0, n):
        sumEndingHere = sumEndingHere + A[i]
        if (sumEndingHere < 0):
            sumEndingHere = 0
            continue
        if (sumSoFar < sumEndingHere):
            sumSoFar = sumEndingHere
    return sumSoFar
A = [-2, 3, -16, 100, -4, 5]
print(MaxContiguousSum(A))
