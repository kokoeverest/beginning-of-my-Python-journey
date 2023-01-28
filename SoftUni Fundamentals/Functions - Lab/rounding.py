nums = input().split(" ")


def rounder(numbers_list):
    result = []
    for number in numbers_list:
        result.append(round(float(number)))

    return result


print(rounder(nums))
# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list.
# Use round().
