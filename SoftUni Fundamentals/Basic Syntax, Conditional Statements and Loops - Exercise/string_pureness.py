number = int(input())

for num in range(number):
    string = input()
    for letter in string:
        if letter == ',' or letter == '.' or letter == '_':
            print(f'{string} is not pure!')
            break
    else:
        print(f'{string} is pure.')

# You will be given number n. After that, you'll receive different strings n times. Your task is to check if the \
# given strings are pure, meaning that they do NOT consist of any of the characters: comma ",", period ".", \
# or underscore "_":
#     • If a string is pure, print "{string} is pure."
#     • Otherwise, print "{string} is not pure!"