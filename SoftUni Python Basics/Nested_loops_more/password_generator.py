number = int(input())
letter = int(input())

current_number1 = 0
current_number2 = 0
current_letter1 = 0
current_letter2 = 0
current_number3 = 0

for num1 in range(1, number + 1):
    current_number1 += 1
    if current_number1 == number:
        raise SystemExit
    for num2 in range(1, number + 1):
        current_number2 += 1
        if current_number2 == number:
            current_number2 = 0
            break
        for ltr1 in range(97, 123):
            current_letter1 += 1
            if current_letter1 == letter + 1:
                current_letter1 = 0
                break
            for ltr2 in range(97, 123):
                current_letter2 += 1
                if current_letter2 == letter + 1:
                    current_letter2 = 0
                    break
                for num3 in range(1, number + 1):
                    if num3 >= num1:
                        if num3 <= num2:
                            print(f'{num1}{num2}{chr(ltr1)}{chr(ltr2)}{num2 + 1}', end=' ')
                    elif num3 >= num2:
                        if num3 <= num1:
                            print(f'{num1}{num2}{chr(ltr1)}{chr(ltr2)}{num1 + 1}', end=' ')











# Да се напише програма, която чете две цели числа n и l, въведени от потребителя, и генерира по азбучен ред всички /
# възможни  пароли, които се състоят от следните 5 символа:
#     • Символ 1: цифра от 1 до n.
#     • Символ 2: цифра от 1 до n.
#     • Символ 3: малка буква измежду първите l букви на латинската азбука.
#     • Символ 4: малка буква измежду първите l букви на латинската азбука.
#     • Символ 5: цифра от 1 до n, по-голяма от първите 2 цифри.
# Вход
# Входът се чете от конзолата и се състои от две цели числа n и l в интервала [1…9], по едно на ред.
# Изход
# На конзолата трябва да се отпечатат всички пароли по азбучен ред, разделени с интервал.