input_numbers = input().split(',')

result = 0
counter = 0
avg = 0
below_avg = ''
above_avg = ''

for number in input_numbers:
    result += int(number)
    counter += 1
    
avg = result / counter
print(f'avg: {avg:.2f}')

for number in input_numbers:
    if int(number) < avg:
        below_avg += str(number) + ','
    elif int(number) > avg:
        above_avg += str(number) + ','

print(f'below: {below_avg}'.removesuffix(','))
print(f'above: {above_avg}'.removesuffix(','))


# Write a program that calculates the average of a list of numbers. Display the average, all the numbers below the average, \
# and all the numbers above the average. Maintain the relative order of numbers.

# Input
# On the only line of input, you will receive the numbers, separated by a comma.
# Output
# On the first line, print the average, with two digits after the decimal separator.
# On the second line, print all the numbers bellow the average
# On the third line, print all the numbers above the average
# Constraints
# 1 <= list.length <= 20
# Input
# 3,-12,0,0,13,5,1,0,-2
# Output
# avg: 0.89
# below: -12,0,0,0,-2
# above: 3,13,5,1
# Input
# 0,1,-1
# Output
# avg: 0.00
# below: -1
# above: 1