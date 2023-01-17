number = int(input())

numbers = []
result = []
for i in range(number + 1):
    line = input()
    if line == 'even':
        for num in numbers:
            if num % 2 == 0:
                result.append(int(num))
    elif line == 'odd':
        for num in numbers:
            if num % 2 != 0:
                result.append(int(num))
    elif line == 'negative':
        for num in numbers:
            if num < 0:
                result.append(int(num))
    elif line == 'positive':
        for num in numbers:
            if num >= 0:
                result.append(int(num))
    else:
        numbers.append(int(line))

print(result)
# On the first line, you will receive a single number n. On the following n lines, you will receive integers.
# After that, you will be given one of the following commands:
#     • even
#     • odd
#     • negative
#     • positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.