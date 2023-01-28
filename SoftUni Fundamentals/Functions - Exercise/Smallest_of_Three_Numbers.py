number_1 = int(input())
number_2 = int(input())
number_3 = int(input())


def smallest_number(num1, num2, num3):
    result = [num1, num2, num3]
    smallest = min(result)
    return smallest


final_result = smallest_number(number_1, number_2, number_3)
print(final_result)


# Write a function that receives three integer numbers and returns the smallest. Print the result on the console.
# Use an appropriate name for the function.
