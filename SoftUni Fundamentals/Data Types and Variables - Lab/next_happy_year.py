year = int(input())
next_year = year
counter = 0
digits = []
while True:
    year += 1
    for digit in str(year):
        if digit not in digits:
            digits.append(digit)
            counter += 1
    if counter == len(str(year)):
        print(year)
        exit()
    digits = []
    counter = 0


# You are saying goodbye to your best friend: "See you next happy year". Happy Year is the year with only
# distinct digits, for example, 2018. Write a program that receives an integer number and finds the next happy year.
# Examples
# Input  Output
# 8989    9012
# 1001    1023