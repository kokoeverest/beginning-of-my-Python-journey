N = int(input())

for i in range(1, N + 1):
    while i % 3 != 0 and i % 7 != 0:

        print(i, end=' ')
        break

# Description

# Write a program that reads from the console a positive integer N and prints all the numbers /
# from 1 to N not divisible by 3 or 7, on a single line, separated by a space.
# Input

#     Will always consists of one valid integer number - the number N.

# Output

#     Should always consists of the numbers from 1 to N, which are not divisible by 3 or 7,/
#  separated by a whitespace.

# Constraints

#     1 < N < 1500
