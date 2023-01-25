numbers_list = input().split(' ')
numbers_to_remove = int(input())

digits = list(reversed(sorted([int(x) for x in numbers_list])))

for i in range(numbers_to_remove):
    if str(digits[-1]) in numbers_list:
        numbers_list.remove(str(digits[-1]))
    digits.pop()

result = ''
for n in numbers_list:
    result += n + ', '

print(result[:-2])

# Write a program that receives a list of integer numbers (separated by a single space) and a number n.
# The number n represents the count of numbers to remove from the list. You should remove the smallest ones,
# and then, you should print all the numbers that are left in the list, separated by a comma and a space ", ".
