number = input()

combination = reversed(sorted(number))
new_list = ''

for i in combination:
    new_list += str(i)

print(new_list)


# You will be given a number. Print the largest number that can be formed from the digits of the given number.