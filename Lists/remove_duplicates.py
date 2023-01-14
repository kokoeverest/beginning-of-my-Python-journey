elements = input().split(',')
no_duplicates = []

for i in elements:
    if i not in no_duplicates:
        no_duplicates.append(i)
final = ''

for element in no_duplicates:
    final += element + ','

print(final.removesuffix(','))

# Write a program that removes all duplicates from a list of elements.

# 1,2,2,2,4,7 -> 1,2,4,7.
# Maintain the relative order of the remaining items.

# Input
# On the only line of input, you will receive the elements, separated by a comma.
# Output
# Display the list with the duplicates removed, separated by a comma.
# Constraints
# 1 <= list.length <= 20