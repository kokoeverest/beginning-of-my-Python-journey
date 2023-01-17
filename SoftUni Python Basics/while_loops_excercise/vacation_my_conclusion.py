days = 0
days_spending = 0

money_needed = float(input())
available_money = float(input())

while days_spending < 5:
    text = input()
    amount = float(input())
    days += 1

    if text == "spend":
        available_money -= amount

        if available_money < 0:
            available_money = 0
        if days >= 5:
            print("You can't save the money.")
            print(f'{days}')
            break

        days_spending += 1
    elif text == "save":
        available_money += amount
        days_spending = 0
        if available_money >= money_needed:
            print(f'You saved the money for {days} days.')
            break
# Джеси е решила да събира пари за екскурзия и иска от вас да ѝ помогнете да разбере дали ще успее да събере /
# необходимата сума. Тя спестява или харчи част от парите си всеки ден. Ако иска да похарчи повече от наличните/
# си пари, то тя ще похарчи колкото има и ще ѝ останат 0 лева.
# Вход
# От конзолата се четат:
#     • Пари, нужни за екскурзията - реално число;
#     • Налични пари - реално число.
# След това многократно се четат по два реда:
#     • Вид действие – текст с две възможности: "spend" или "save";
#         ◦ Сумата, която ще спести/похарчи - реално число.
# Изход
# Програмата трябва да приключи при следните случаи:
#     • Ако 5 последователни дни Джеси само харчи, на конзолата да се изпише:
#     • "You can't save the money."
#     • "{Общ брой изминали дни}"
#     • Ако Джеси събере парите за почивката, на конзолата се изписва:
#     • "You saved the money for {общ брой изминали дни} days."