numbers = []

for opr in range(4):
    number = int(input())
    numbers.append(number)

result = int((numbers[0] + numbers[1]) / numbers[2]) * numbers[3]

print(f'{result:.0f}')
# Write a program that reads four integer numbers. It should add the first to the second number,
# integer divide the sum by the third number, and multiply the result by the fourth number. Print the final result.
# Examples
# Input
# Output
#
# Input  Output
# 10
# 20
# 3
# 3       30
#
# 15
# 14
# 2
# 3       42