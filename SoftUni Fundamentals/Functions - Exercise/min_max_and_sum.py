list_of_numbers = input().split(" ")


def min_max_sum(par):
    digits = []
    sum_result = 0
    for i in par:
        digits.append(int(i))
        sum_result += int(i)

    min_num = min(digits)
    max_num = max(digits)
    return f'The minimum number is {min_num}\
        \nThe maximum number is {max_num}\
        \nThe sum number is: {sum_result}'


print(min_max_sum(list_of_numbers))

# Write a program that receives a sequence of numbers (integers) separated by a single space. It should print the
# min and max values of the given numbers and the sum of all the numbers in the list. Use min(), max() and sum().
# The output should be as follows:
#     • On the first line: "The minimum number is {minimum number}"
#     • On the second line: "The maximum number is {maximum number}"
#     • On the third line: "The sum number is: {sum of all numbers}"
