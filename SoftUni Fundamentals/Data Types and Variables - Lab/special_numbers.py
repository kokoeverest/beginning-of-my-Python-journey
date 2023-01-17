number = int(input())
for num in range(1, number + 1):
    sum_digits = 0
    digits = num
    while digits > 0:
        sum_digits += digits % 10
        digits = int(digits / 10)
    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')

# Write a program that reads an integer n. Then, for all numbers in the range [1, n], prints the number and if it
# is special or not (True / False). A number is special when the sum of its digits is 5, 7, or 11.
# Examples
# Input
# Output
# 15
# 1 -> False
# 2 -> False
# 3 -> False
# 4 -> False
# 5 -> True
# 6 -> False
# 7 -> True
# 8 -> False
# 9 -> False
# 10 -> False
# 11 -> False
# 12 -> False
# 13 -> False
# 14 -> True
# 15 -> False
# 6
# 1 -> False
# 2 -> False
# 3 -> False
# 4 -> False
# 5 -> True
# 6 -> False
