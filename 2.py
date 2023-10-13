import math

# Function to calculate GCD using Euclidean algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to count pairs where GCD is not equal to 1
def count_pairs_with_non_gcd_one(N, A, B):
    count = 0

    for i in range(N):
        for j in range(N):
            if gcd(A[i], B[j]) != 1:
                count += 1

    return count

# Input
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Count pairs with GCD not equal to 1
result = count_pairs_with_non_gcd_one(N, A, B)
print(result)
