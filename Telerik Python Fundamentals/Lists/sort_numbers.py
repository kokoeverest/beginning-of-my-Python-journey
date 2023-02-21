
n = input().split(', ')

new_nums = []

for element in n:
    new_nums.append(int(element))

final_nums = list(reversed(sorted(new_nums)))
final_list = ''

for i in final_nums:
    final_list = final_list + str(i) + ', ' 

print(final_list.removesuffix(', ')) 

# Write a program that reads a list of numbers separated by a comma and space.

# Arrange the numbers in descending order.

# Output all numbers on a single line, separated by a comma and a space.
# Input

#     On the only line you will receive all the numbers to be sorted.

# Output

#     On the only line of output, print all the numbers sorted in format n1, n2, n3, .. n
# 2, 3, 1, 5, 6    14, 5, 8, 5, 18, 5, 1