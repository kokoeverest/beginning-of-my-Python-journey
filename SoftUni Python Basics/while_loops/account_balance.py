total_money = 0

while True:
    user_input = input()
    if user_input == 'NoMoreMoney':
        break
    increase = float(user_input)
    if increase < 0:
        print("Invalid operation!")
        break
    total_money += increase
    print(f"Increase: {increase:.2f}")

print(f"Total: {total_money:.2f}")
# Напишете програма, която пресмята колко общо пари има в сметката, след като направите определен брой вноски. /
# На всеки ред ще получавате сумата, която трябва да внесете в сметката, до получаване на команда  "NoMoreMoney "./
# При всяка получена сума на конзолата трябва да се извежда "Increase: " + сумата и тя да се прибавя в сметката. /
# Ако получите число по-малко от 0 на конзолата трябва да се изведе "Invalid operation!"  и програмата да приключи. /
# Когато програмата приключи трябва да се принтира "Total: " + общата сума в сметката форматирана до втория знак/
# след десетичната запетая.