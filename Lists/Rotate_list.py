numbers = input().split(',')
count = int(input())

for N in range(count):
    numbers.append(numbers[0])
    numbers.remove(numbers[0])
result = ''
for index in numbers:
    result += str(index)
    result += ','
print(result.removesuffix(','))
# Write a program that rotates a list several times (the first element becomes last).

# list = 1,2,3,4,5 and N = 2 -> result = 3,4,5,1,2
# Note that N could be larger than the length of the list.

# list = 1,2,3,4,5 and N = 6 -> result = 2,3,4,5,1
# Input
# On the first line you will receive the list of numbers.
# On the second line you will receive N
# Output
# On the only line of output, print the numbers separated by a comma.
