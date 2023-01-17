# Да се напише програма, която чете текст (стринг), въведен от потребителя, и изчислява и отпечатва сумата от\
# стойностите на гласните букви според таблицата по-долу:

text = input()

result = 0

for i in range(0, len(text)):
    current_char = text[i]

    if current_char == "a":
        result += 1
    elif current_char == "e":
        result += 2
    elif current_char == "i":
        result += 3
    elif current_char == "o":
        result += 4
    elif current_char == "u":
        result += 5

print(result)
