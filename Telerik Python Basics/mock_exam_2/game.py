user_input = input()

number_one = user_input[0]
number_two = user_input[1]
number_three = user_input[2]

result_1 = int(number_one) + int(number_three) * int(number_two)
result_2 = int(number_one) + int(number_two) * int(number_three)
result_3 = int(number_one) * int(number_two) + int(number_three)
result_4 = int(number_one) * int(number_three) + int(number_two)

if result_1 >= result_2 and result_1 >= result_3 and result_1 >= result_4:
    print(result_1)
elif result_2 >= result_1 and result_2 >= result_3 and result_2 >= result_4:
    print(result_2)
elif result_4 >= result_1 and result_4 >= result_2 and result_4 >= result_3:
    print(result_4)
else:
    print(result_3)
# Three friends came up with a game for having fun in the break between the classes. One of them says a three-digit number /
# and the others use it to form a mathematical expressions by using operators for sum and multiplication between the digits.

# The winner is the first one who founds the biggest number that is a result of the above mentioned rules.

# Write a program 'game', which prints out that biggest number.

# Input
# Read from the standard input

# The first line of the input will be positive three-digit number N.
# Output
# Print on the standard output

# The result should be the calculated biggest number.
# The calculation order
