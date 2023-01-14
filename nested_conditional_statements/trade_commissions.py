city = input()
sales = float(input())

commission = 0
is_invalid_input = False

if city == "Sofia":
    if 0 <= sales <= 500:
        commission = sales * 0.05
    elif 500 <= sales <= 1000:
        commission = sales * 0.07
    elif 1000 <= sales <= 10000:
        commission = sales * 0.08
    elif sales > 10000:
        commission = sales * 0.12
    else:
        is_invalid_input = True
elif city == "Varna":
    if 0 <= sales <= 500:
        commission = sales * 0.045
    elif 500 <= sales <= 1000:
        commission = sales * 0.075
    elif 1000 <= sales <= 10000:
        commission = sales * 0.1
    elif sales > 10000:
        commission = sales * 0.13
    else:
        is_invalid_input = True
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commission = sales * 0.055
    elif 500 <= sales <= 1000:
        commission = sales * 0.08
    elif 1000 <= sales <= 10000:
        commission = sales * 0.12
    elif sales > 10000:
        commission = sales * 0.145
    else:
        is_invalid_input = True
else:
    is_invalid_input = True

if is_invalid_input: #or sales < 0:
    print("error")
else:
    print(f'{commission:.2f}')

# Фирма дава следните комисионни на търговците си според града, в който работят и обема на продажбите:\
# Напишете конзолна програма, която чете име на град (текст) и обем на продажби (реално число), въведени \
# от потребителя, и изчислява и извежда размера на търговската комисионна според горната таблица. \
# Резултатът да се изведе форматиран до 2 цифри след десетичната точка. При невалиден град или обем на \
# продажбите (отрицателно число) да се отпечата "error".