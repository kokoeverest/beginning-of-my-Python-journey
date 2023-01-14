array = input().split(',')
zeroes = []
others = []
for number in array:
    if number == '0':
        zeroes.append(number)
    else:
        others.append(number)
result = others + zeroes
final = ''
for num in result:
    final += str(num) + ','

print(final.removesuffix(','))
# Given an array integers, write a program that moves all of the zeroes to the end of it, \
# while maintaining the relative order of the non-zero elements.

# Input
# Read from the standard input:

# There is one line of input, containing N amount of integers, seperated by a comma (",")
# Output
# Print to the standard output:

# There is one line of outpit, containing the sorted integers, seperated by a comma (",")
# Constraints
# 5 <= N <= 1000
# Sample Tests
# Input
# 0,1,0,3,12
# Output
# 1,3,12,0,0
# Input
# 0,0,0,5,0,3,2,3
# Output
# 5,3,2,3,0,0,0,0