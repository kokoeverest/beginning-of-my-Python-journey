sum_prime = 0
sum_non_prime = 0

while True:
    user_input = input()

    if user_input == "stop":
        break

    current_number = int(user_input)
    is_prime = True

    if current_number < 0:
        print("Number is negative.")
        continue

    for number in range(2, current_number):
        if current_number % number == 0:
            is_prime = False
            break

    if is_prime:
        sum_prime += current_number
    else:
        sum_non_prime += current_number


print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_non_prime}')

# Напишете програма, която чете от конзолата цели числа, докато не се получи команда "stop". Да се намери сумата на /
# всички въведени прости и сумата на всички въведени непрости числа. Тъй като по дефиниция от математиката /
# отрицателните числа не могат да бъдат прости, ако на входа се подаде отрицателно число, да се изведе следното /
# съобщение "Number is negative.". В този случай въведено число се игнорира и не се прибавя към нито една от двете суми, /
# а програмата продължава своето изпълнение, очаквайки въвеждане на следващо число.
# На изхода да се отпечатат на два реда двете намерени суми в следния формат:
#     • "Sum of all prime numbers is: {prime numbers sum}"
#     • "Sum of all non prime numbers is: {nonprime numbers sum}"