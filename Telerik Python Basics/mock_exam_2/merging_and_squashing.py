N = int(input())
counter = 0

for i in range(N):
    number = input()
    digit_1 = number[0]
    digit_2 = number[1]
    if counter == 0:
        print(digit_2, end=(''))
    else:
        print(digit_1,digit_2, end=(''))
    counter += 1
    if range == N - 1:
        print(end=())
    # for j in range(N):
    #     print(digit_1, (int(digit_2) + int(digit_1)))
# We have the following operations defined for two-digit numbers. There are two possible ways of merging them:

# Merging ab and cd produces bc
# 42 merged with 17 produces 21
# 17 merged with 42 produces 74
# Squashing ab and cd produces a(b+c)d - the middle digit is the sum of b and c
# 42 squashed with 17 produces 437
# 39 squashed with 57 produces 347 (9 + 5 = 14, we use only the 4)
# You have a sequence of N two-digit numbers. Your task is to merge and squash each pair of adjacent numbers.

# Input
# All input data is read from the standard input

# On the first line, you will receive an integer N
# On the next N lines you will receive N two-digit numbers
# Each number will be on a separate line
# Output
# The output data is printed on the standard output

# On the first output line print the merged numbers

# There should be N - 1 of them
# Separate them by spaces
# On the second output line print the squashed numbers

# There should be N - 1 of them
# Separate them by spaces
# Constraints
# 2 <= N <= 1000
# Numbers will consist of two non-zero digits
# The input data will always be correct and there is no need to check it explicitly