string_1 = input()
string_2 = input()

result = string_1
for letter in range(len(string_1)):
    if string_1[letter] == string_2[letter]:
        continue
    result = string_2[:letter + 1] + string_1[letter + 1:]

    print(result)
# You will be given two strings. Transform the first string into the second one, letter by letter, starting from \
# the first one. After each interaction, print the resulting string only if it is unique.
# Note: the strings will have the same length.

# bubble gum
# turtle hum