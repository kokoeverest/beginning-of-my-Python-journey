first_number = int(input())
second_number = int(input())

for i in range(first_number, second_number + 1):
    for j in range(first_number, second_number + 1):
        for k in range(first_number, second_number + 1):
            for m in range(first_number, second_number + 1):
                if i % 2 == 0 and m % 2 == 1:
                    if i > m and (j + k) % 2 == 0:
                        print(f'{i}{j}{k}{m}', end=' ')
                elif i % 2 == 1 and m % 2 == 0:
                    if i > m and (j + k) % 2 == 0:
                        print(f'{i}{j}{k}{m}', end=' ')



# Поздравления, поради вашите задълбочени знания в сферата на програмирането МВР реши да наеме точно вас за създаването /
# на новата им система за генериране на специални автомобилни номера. Всеки един специален автомобилен номер се състой /
# от четири числа. Условията, които разграничават специалните от обикновените номера са следните:
#     • Ако номерът започва с четна цифра, то той трябва да завършва на нечетна цифра и обратното – ако започва с /
#     нечетна,  завършва на четна
#     • Първата цифра от номера е по-голяма от последната
#     • Сумата от втората и третата цифра трябва да е четно число
# Входа се състой от две числа - начало и край на интервал, между които трябва да се генерира всяко едно число от номера.

# Вход
#     1. Първи ред - едноцифрено число - началото на интервала – цяло число в интервала [1…9]
#     2. Втори ред - едноцифрено число - края на интервала – цяло число в интервала [1…9]
# Изход
# На конзолата трябва да се отпечатат всички специални номера, разделени с интервал.