# solved with zip function.

from itertools import zip_longest

line_1 = input().split(' ')
line_2 = input().split(' ')

# no need to create new_list_1 and new_list_2 (lists with integers of the input)/
#  when using the zip_longest function
# new_line_1 = []
# new_line_2 = []
# for i in line_1:
#     new_line_1.append(int(i))
# for k in line_2:
#     new_line_2.append(int(k))

zipped = list(zip_longest(line_1, line_2, fillvalue='x'))
for l, j in zipped:
    if l == j:
        print('+', l, j)   
    else:
        print('-', l, j)

# Diff Checker
# Git stopped working because the diffing algorithm is buggy so guess who will have to re-implement it?

# To start with something simpler, you will need to compare two arrays, and display a + if there's a match between /
# a pair of elements or a - if there is none. If there are more numbers in one of the arrays, display a 'x' for the missing /
# number in the other array.

# Study the examples below to get a clearer understanding.

# Input
# There are two lines of input, each one containing numbers, separated by a space.

# Output
# For each pair of elements, print a new line in the format:
# + {firstArrElement} {secondArrElement} - if equal
# - {firstArrElement} {secondArrElement} - if different
# Replace a missing element with 'x', if necessary.
# Sample Tests
# Input
# 1 2 3 4 5 7
# 1 2 4 4 5 6
# Output
# + 1 1
# + 2 2
# - 3 4
# + 4 4
# + 5 5
# - 7 6
# Input
# 1 2 3 4 5 6
# 1 2 3 4
# Output
# + 1 1
# + 2 2
# + 3 3
# + 4 4
# - 5 x
# - 6 x

# 1 2 9 6 3 5 4 4 6 5 8
# 5 4 8 6 3 4 4 6 8