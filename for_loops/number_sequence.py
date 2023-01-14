# Напишете програма, която чете n на брой цели числа. Принтирайте най-голямото и най-малкото число сред въведените.

numbers = int(input())

min_number = 0
max_number = 0

for i in range(0, numbers):
    num = int(input())
    if i == 0:
        min_number = num
        max_number = num
    else:
        if num < min_number:
            min_number = num
        elif num > max_number:
            max_number = num

print(f'Max number: {max_number}')

print(f'Min number: {min_number}')

