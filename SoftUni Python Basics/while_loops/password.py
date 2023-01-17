name = input()
password = input()

correct_pass = ''

while correct_pass != password:
    correct_pass = input()
    if correct_pass == password:
        print(f"Welcome {name}!")

# Напишете програма, която първоначално прочита име и парола на потребителски профил. След това чете парола за вход.
#     • при въвеждане на грешна парола: потребителя да се подкани да въведе нова парола.
#     • при въвеждане на правилна парола: отпечатваме "Welcome {username}!".