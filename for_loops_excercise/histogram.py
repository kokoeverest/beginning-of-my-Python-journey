rows = int(input())


P_1 = 0
P_2 = 0
P_3 = 0
P_4 = 0
P_5 = 0

for i in range(rows):
    number = int(input())

    if number < 200:
        P_1 += 1 # because we have to add + 1, not to sum all numbers
    elif number <= 399:
        P_2 += 1
    elif number <= 599:
        P_3 += 1
    elif number <= 799:
        P_4 += 1
    else:
        P_5 += 1

total_numbers = P_1 + P_2 + P_3 + P_4 + P_5
P_1_percent = P_1 / total_numbers * 100
P_2_percent = P_2 / total_numbers * 100
P_3_percent = P_3 / total_numbers * 100
P_4_percent = P_4 / total_numbers * 100
P_5_percent = P_5 / total_numbers * 100

print(f'{P_1_percent:.2f}%')
print(f'{P_2_percent:.2f}%')
print(f'{P_3_percent:.2f}%')
print(f'{P_4_percent:.2f}%')
print(f'{P_5_percent:.2f}%')


# Дадени са n цели числа в интервала [1…1000]. От тях някакъв процент p1 са под 200, друг процент p2 са от 200 до 399,/
# друг процент p3 са от 400 до 599, друг процент p4 са от 600 до 799 и останалите p5 процента са от 800 нагоре. /
# Да се напише програма, която изчислява и отпечатва процентите p1, p2, p3, p4 и p5.
# Пример: имаме n = 20 числа: 53, 7, 56, 180, 450, 920, 12, 7, 150, 250, 680, 2, 600, 200, 800, 799, 199, 46, 128, 65. /
# Получаваме следното разпределение и визуализация:
# Изход
# Да се отпечата на конзолата хистограмата – 5 реда, всеки от които съдържа число между 0% и 100%, с точност две /
# цифри след десетичната точка, например 25.00%, 66.67%, 57.14%.
