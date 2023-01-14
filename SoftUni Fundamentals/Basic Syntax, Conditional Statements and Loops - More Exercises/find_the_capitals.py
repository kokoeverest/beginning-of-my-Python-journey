text = input()

letters = []

for index in range(len(text)):
    if text[index].isupper():
        letters.append(index)

print(letters)

# Write a program that takes a single string and prints a list of all the capital letters indices.