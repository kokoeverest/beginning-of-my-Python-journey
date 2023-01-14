array_input = input().split(' ')
numbers = 0

new_numbers = []
for i in array_input:
    if int(i) % 3 == 0 and int(i) % 7 == 0:
        new_numbers.append(i)
magic_number = 0
for k in new_numbers:
    magic_number += int(k)

magic_number = str(magic_number)
final_number = 0

for n in magic_number:
    final_number += int(n)

print(final_number)

# Magic Numbers
# Given an array of exactly 5 numbers, find those that can be divided both to 3 and 7. Then, sum them all up and find the number /
# that will be the result of the sum of the number’s digits.


# ###Example:

# Numbers: '21 42 50 126 300'
# Numbers that can be divided both to 3 and 7: '21 42 126'
# Sum: '21 + 42 + 126 = 189'
# Digits' sum: '1 + 8 + 9 = 18'
# Input
# Read from the standard input

# Exactly 5 numbers.
# Output
# Print on the standard output

# The result of the calculated sum.
# Sample tests
# Input
# 21 42 50 126 300
# Output
# 18