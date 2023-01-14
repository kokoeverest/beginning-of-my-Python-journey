string_1 = input()
string_2 = input()

for letter1 in string_1:
    for letter2 in string_2:
        if letter1 != letter2:
            print(f'{string_2[0:1:]}{string_1[1::]}')
            continue
        break

# You will be given two strings. Transform the first string into the second one, letter by letter, starting from \
# the first one. After each interaction, print the resulting string only if it is unique.
# Note: the strings will have the same length.

# bubble gum
# turtle hum