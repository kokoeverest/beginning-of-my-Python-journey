character_1 = input()
character_2 = input()


def chr_range(chr1, chr2):
    characters = ""
    for char in range(ord(chr1) + 1, ord(chr2)):
        characters += (chr(char)) + " "

    return characters[:-1]


print(chr_range(character_1, character_2))

# Write a function that receives two characters and returns a single string with all the characters in between them
# (according to the ASCII code), separated by a single space. Print the result on the console.
