start_number = int(input())
end_number = int(input())
magical_number = int(input())

combination_count = 0
is_found = False

for a in range(start_number, end_number + 1):
    if is_found:
        break
    for b in range(start_number, end_number + 1):
        combination_count += 1
        if a + b == magical_number:
            print(f'Combination N:{combination_count} ({a} + {b} = {magical_number})')
            is_found = True
            break
if not is_found:
    print(f'{combination_count} combinations - neither equals {magical_number}')
# Напишете програма която проверява всички възможни комбинации от двойка числа в интервала от две дадени числа./
# На изхода се отпечатва, коя поред е комбинацията чиито сбор от числата е равен на дадено магическо число. /
# Ако няма нито една комбинация отговаряща на условието се отпечатва съобщение, че не е намерено.
# Вход
# Входът се чете от конзолата и се състои от три реда:
#     • Първи ред – начало на интервала – цяло число в интервала [1...999]
#     • Втори ред – край на интервала – цяло число в интервала [по-голямо от първото число...1000]
#     • Трети ред – магическото число – цяло число в интервала [1...10000]
# Изход
# На конзолата трябва да се отпечата един ред, според резултата:
#     • Ако е намерена комбинация чиито сбор на числата е равен на магическото число
#         ◦ "Combination N:{пореден номер} ({първото число} + {второ число} = {магическото число})"
#     • Ако не е намерена комбинация отговаряща на условието
#         ◦ "{броят на всички комбинации} combinations - neither equals {магическото число}"