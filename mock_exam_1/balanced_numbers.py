numbers = []
nums = []

for i in range(1001):
    number = int(input())
    numbers = [number]
    nums = list(enumerate(numbers))
    current_number = len(numbers)
    print(numbers)
    print(current_number)
    print(nums)
# A balanced number is a 3-digit number whose second digit is equal to the sum of the first and last digit.

# Write a program which reads and sums balanced numbers. You should stop when an unbalanced number is given.
# Input

# Input data is read from the standard input

#     Numbers will be given
#         Each one will be on a separate line

# Output

# Print to the standard output
# Constraints

#     No more than 1000 numbers will be given
