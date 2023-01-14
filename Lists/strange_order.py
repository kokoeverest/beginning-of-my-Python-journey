numbers = input().split(',')
final = ''
negative = []
zero = []
positive = []

for number in numbers:
    if int(number) < 0:
        negative.append(number)
    elif int(number) == 0:
        zero.append(number)
    else:
        positive.append(number)

result = negative + zero + positive

for num in result:
    final += str(num) + ','

print(final.removesuffix(','))


# logic: from the input list, place the negative numbers first (from left to right), then 0 (zero) then the positive numbers

# Write a program that orders a list of numbers in the following way:

# 3,-2,1,0,-1,0,-2,1 -> -2,-1,-2,0,0,3,1,1
# You need to find out the criteria for yourself by looking at the example. You can also check the example below.

# Input
# On the only line of input, you will receive the numbers, separated by a comma.
# Output
# Display the list with the mysterious ordering applied removed, separated by a comma.
# Constraints
# 1 <= list.length <= 20
# Input
# 3,-12,0,0,13,5,1,0,-2
# Output
# -12,-2,0,0,0,3,13,5,1
# Input
# 0,1,-1