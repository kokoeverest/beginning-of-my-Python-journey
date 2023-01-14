word = ''
c_count = 0
o_count = 0
n_count = 0
letters = ['a', 'd', 'g', 'j', 'm', 'p', 's', 'v', 'y', 'A', 'D', 'G', 'J', 'M', 'P', 'S', 'V', 'Y', 'b', 'C', 'F',
           'I', 'L', 'O', 'R', 'U', 'X', 'e', 'h', 'k', 'n', 'q', 't', 'w', 'z', 'B', 'E', 'H', 'K', 'N', 'Q', 'T',
           'W', 'Z', 'c', 'f', 'i', 'l', 'o', 'r', 'u', 'x']
while True:
    invalid_symbol = False
    letter = input()

    if letter == 'End':
        break

    if letter not in letters:
        invalid_symbol = True
        continue

    if letter == 'c':
        if c_count == 1:
            word += letter
            continue
        c_count += 1
    elif letter == 'o':
        if o_count == 1:
            word += letter
            continue
        o_count += 1
    elif letter == 'n':
        if n_count == 1:
            word += letter
            continue
        n_count += 1
    else:
        word += letter

    if c_count == 1 and o_count == 1 and n_count == 1:
        print(word, end=' ')
        c_count, o_count, n_count = 0, 0, 0
        word = ''
