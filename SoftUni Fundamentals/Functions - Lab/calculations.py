def calculator(operator, num1, num2):
    if operator == "multiply":
        return num1 * num2
    elif operator == "divide":
        return int(num1 / num2)
    elif operator == "add":
        return num1 + num2
    elif operator == "subtract":
        return num1 - num2


action = input()
number_1 = int(input())
number_2 = int(input())

print(calculator(action, number_1, number_2))

# Create a function that receives three parameters, calculates a result depending on the given operator, and returns it.
# Print the result of the function.
# The input comes as three parameters – an operator as a string and two integer numbers.
# The operator can be one of the following:  "multiply", "divide", "add", "subtract".
