rows = int(input())

total_sum = 0
largest_number = 0

for i in range(0, rows):
    number = int(input())

    total_sum += number

    if number > largest_number:
        largest_number = number

total_sum -= largest_number

if largest_number == total_sum:
    print('Yes')
    print(f'Sum = {largest_number}')

else:
    print("No")
    print(f'Diff = {abs(largest_number - total_sum)}')



# Да се напише програма, която чете n-на брой цели числа, въведени от потребителя,и проверява дали сред тях съществува/
# число, което е равно на сумата на всички останали.
#     • Ако има такъв елемент печата "Yes" и на нов ред "Sum = "  + неговата стойност
#     • Ако няма такъв елемент печата "No" и на нов ред "Diff = " + разликата между най-големия елемент и сумата на останалите (по абсолютна стойност)