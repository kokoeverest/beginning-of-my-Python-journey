num_1 = int(input())
num_2 = int(input())
num_3 = int(input())


def sum_numbers(num1, num2):
    return num1 + num2


def subtract(n1, n3):
    return n1 - n3


def add_and_subtract(p1, p2, p3):
    sum_result = sum_numbers(p1, p2)
    subtract_result = subtract(sum_result, p3)

    return subtract_result


print(add_and_subtract(num_1, num_2, num_3))

# You will receive three integer numbers.
# Write functions named:
#     • sum_numbers() that returns the sum of the first two integers
#     • subtract() that returns the difference between the returned result of the first function and the third integer
# Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters.
# Print the result of the subtract() function on the console.
