number = int(input())

for i in range(number):
    list = input().split(',')
   
    if i == str(chr):
        break
    elif 1 <= number <= 10:
        if 1 <= len(list) <= 20:
            if list == ['']:
                continue
            elif list == sorted(list):
                print('true')
            else:
                print('false')

# Write a program that checks if a list is already sorted. For a list to be sorted, the next element must NOT be smaller than the previous one.

# Input
# On the first line - you will receive a number N.
# On the next N lines, you will receive a list of numbers, separated by a comma
# Output
# There are N lines of output
# for each list you receive, print 'true' if sorted or 'false' otherwise.
# Constraints
# 1 <= N <= 10
# 1 <= list.length <= 20