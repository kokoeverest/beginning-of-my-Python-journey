from math import factorial

N = int(input())
x = float(input())

for i in range(1, N + 1):
    if N == 3:
        sum = 1 + factorial(1)/x + factorial(2)/x**2 + factorial(N)/x**N
    elif N == 4:
        sum =1 + factorial(1)/x + factorial(2)/x**2 + factorial(3)/x**3 + factorial(N)/x**N
    elif N == 5:
        sum = 1 + factorial(1)/x + factorial(2)/x**2 + factorial(3)/x**3 + factorial(4)/x**4 + factorial(N)/x**N
print(f'{sum:.5f}')

# Description

# Write a program that, for a given two numbers N and x, calculates the sum S = 1 + 1!/x + 2!/x2 + … + N!/xN.

#     Use only one loop. Print the result with 5 digits after the decimal point.

# Input

#     On the first line you will receive one number - N.
#     On the second line you will receive another number - x.

# Output

#     Output only one number - the sum of the sequence for the given N and x.

# Constraints

#     N will always be a valid integer between 2 and 10, inclusive.
#     X will always be a valid floating-point number between 0.5 and 100
