# Да се напише програма, която чете 2 * n-на брой цели числа, подадени от потребителя, и проверява дали сумата на /
# първите n числа (лява сума) е равна на сумата на вторите n числа (дясна сума). При равенство печата/
# " Yes, sum = " + сумата; иначе печата " No, diff = " + разликата. Разликата се изчислява като положително число /
# (по абсолютна стойност).
number = int(input())

left_number = 0
right_number = 0

for i in range(0, number):
    num = int(input())
    left_number += num

for i in range(0, number):
    num = int(input())
    right_number += num

if left_number == right_number:
    print(f'Yes, sum = {left_number}')
else:
    print(f'No, diff = {abs(left_number - right_number)}')
