
number = int(input())

while True:
    user_input = input()
    if user_input == "Stop":
        break
    new_input = int(user_input)
    if new_input < number:
        number = new_input
print(number)


# Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени от потребителя, намира /
# най-малкото измежду тях и го принтира. Въвежда се по едно число на ред.