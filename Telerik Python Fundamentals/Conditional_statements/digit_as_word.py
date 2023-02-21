
# for i in range(9 + 1):  # without this for loop!
digit = input()

match digit:
    case "0":
        print("zero")
    case "1":
        print("one")
    case "2":
        print("two")
    case "3":
        print("three")
    case "4":
        print("four")
    case "5":
        print("five")
    case "6":
        print("six")
    case "7":
        print("seven")
    case "8":
        print("eight")
    case "9":
        print("nine")
    case _:
        print("not a digit")


    # if digit == '0':
    #     print('zero')
    # elif digit == '1':
    #     print('one')
    # elif digit == '2':
    #     print('two')
    # elif digit == '3':
    #     print('three')
    # elif digit == '4':
    #     print('four')
    # elif digit == '5':
    #     print('five')
    # elif digit == '6':
    #     print('six')
    # elif digit == '7':
    #     print('seven')
    # elif digit == '8':
    #     print('eight')
    # elif digit == '9':
    #     print('nine')
    # else:
    #     print('not a digit')

# Description
# Write a program that read a digit [0-9] from the console, and depending on the input, shows the digit as a word (in English).

# Print "not a digit" in case of invalid input.
# Use a switch statement.
# Input
# The input consists of one line only, which contains the digit.
# Output
# Output a single line - should the input be a valid digits, print the english word for the digits. Otherwise, print "not a digit".