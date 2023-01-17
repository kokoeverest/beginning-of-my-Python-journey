start_first_pair = int(input())
start_second_pair = int(input())
end_first_pair = int(input())
end_second_pair = int(input())

is_first_pair_prime = False
is_second_pair_prime = False

for first in range(start_first_pair, (start_first_pair + end_first_pair) + 1):

    for second in range(start_second_pair, (start_second_pair + end_second_pair) + 1):

        is_first_pair_prime = True

        for i in range(2, first):
            if first % i == 0:
                is_first_pair_prime = False
                break

        if is_first_pair_prime:
            is_second_pair_prime = True

            for k in range(2, second):
                if second % k == 0:
                    is_second_pair_prime = False
                    break

            if is_first_pair_prime and is_second_pair_prime:
                print(f'{first}{second}')


# Напишете програма, която генерира и принтира на конзолата четирицифрени числа, в които първата и втората двойка /
# цифри образуват двуцифрени прости числа (пример за такова число 1723). Крайната стойност до която трябва да се /
# генерират двойките се определя от други 2 цифри, подадени като вход, които определят с колко крайната стойност /
# е по-голяма от началната.
# Вход
# От конзолата се четат четири реда:
#     • На първия ред – началната стойност на първите първата двойка числа – цяло положително число в диапазона [10… 90]
#     • На втория ред – началната стойност на втората двойка числа – цяло положително число в диапазона [10… 90]
#     • На третия ред – разликата между началната и крайната стойност на  първата двойка числа – цяло положително число в диапазона [1… 9]
#     • На четвъртия ред – разликата между началната и крайната стойност на  втората двойка числа – цяло положително число в диапазона [1… 9]
# Изход:
# Да се отпечатат на конзолата четирицифрените числа, в които първите две и вторите две цифри са прости двуцифрени числа.
