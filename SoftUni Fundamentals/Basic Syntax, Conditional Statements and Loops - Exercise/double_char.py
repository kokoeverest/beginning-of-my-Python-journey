while True:
    string = input()
    if string == 'End':
        break
    elif string == 'SoftUni':
        continue
    else:
        for letter in string:
            print(letter * 2, end='')
    print()
# You will be given strings until you receive the command "End". For each string given, you should print a string \
# in which each character (case-sensitive) is repeated twice. Note that if you receive the string "SoftUni",\
# you should NOT print it!