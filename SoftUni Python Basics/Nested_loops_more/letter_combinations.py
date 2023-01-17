row_1 = input()
row_2 = input()
row_3 = input()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
counter = 0

for letter1 in range(97, 123): # instead of iterating throughout [letters]
    for letter2 in letters:
        for letter3 in letters:
            if chr(letter1) <= row_2 and chr(letter1) >= row_1 and chr(letter1) != row_3: #get the corresponding ASCII code for 'letter1'
                if letter2 <= row_2 and letter2 >= row_1 and letter2 != row_3:
                    if letter3 <= row_2 and letter3 >= row_1 and letter3 != row_3:
                        print(f'{letter1:c}{letter2}{letter3}', end=' ') # print the formatted 'letter1', according to its ASCII code
                        counter += 1

print(counter)

# Напишете програма, която да принтира на конзолата всички комбинации от 3 букви в зададен интервал, като се пропускат /
# комбинациите съдържащи зададена от конзолата буква. Накрая трябва да се изпринтира броят на отпечатаните комбинации.
# Вход
# Входът се чете от конзолата и съдържа точно 3 реда:
#     Ред 1. Малка буква от английската азбука за начало на интервала – от ‘a’ до ‚z’.
#     Ред 2. Малка буква от английската азбука за край на интервала  – от първата буква до ‚z’.
#     Ред 3. Малка буква от английската азбука – от ‘a’ до ‚z’ – като комбинациите съдържащи тази буквата се пропускат.
# Изход
# Да се отпечатат на един ред всички комбинации отговарящи на условието плюс броят им разделени с интервал.