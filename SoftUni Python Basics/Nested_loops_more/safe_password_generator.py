number_a = int(input())
number_b = int(input())
max_passwords = int(input())

passwords = 0

while True:
    for A in range(35, 55):
        for B in range(64, 96):
            for x in range(1, number_a + 1):
                for y in range(1, number_b + 1):

                    if passwords == max_passwords:
                        raise SystemExit
                    print(f'{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}', end='|')
                    passwords += 1
                    A += 1
                    B += 1
                    if A == 56:
                        A = 35
                    if B == 97:
                        B = 64
                    if x == number_a and y == number_b:
                        raise SystemExit

# Ани се страхува от това, да не й бъде хакнат някой от профилите в социалните мрежи, затова решава да направи /
# генератор за пароли, които да бъдат достатъчно сигурни. Вашата задача е да й помогнете да напише програма, която/
# ще генерира тези пароли, разделени една от друга от знака "|".
# Да се напише програма, която генерира серия от символи като в шаблона:
# ABxyBA
# като при всяко генериране на нов код, стойностите на символите се увеличават с 1. Ако A надхвърли 55, се връща на 35./
# Ако B надхвърли 96, се връща на 64.
# Вход
# От конзолата се чете 1 ред:
#     • На първия ред a – цяло число в интервала [1 … 1000]
#     • На втория ред b – цяло число в интервала [1 … 1000]
#     • На третия ред максимален брой генерирани пароли – цяло число в интервала [1 … 1000000]
# Ограничения:
#     • A е символ с ASCII стойност в диапазона [35… 55]
#     • B е символ с ASCII стойност в диапазона [64 … 96]
#     • x e цяло число в диапазона [1… a]
#     • y e цяло число в диапазона [1… b]
# Изход:
# Да се отпечата на конзолата:
#     • Генерираният код. Ако броят на комбинациите е по-голям от максималния на кода, да се отпечата до подадената/
#     стойност, в противен случай да се отпечата до текущия брой на комбинациите.