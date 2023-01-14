fruit = input()
day_of_week = input()
quantity = float(input())

price = 0

if day_of_week == "Saturday" or day_of_week == "Sunday":
    if fruit == "banana":
        price = quantity * 2.70
    elif fruit == "apple":
        price = quantity * 1.25
    elif fruit == "orange":
        price = quantity * 0.9
    elif fruit == "grapefruit":
        price = quantity * 1.6
    elif fruit == "kiwi":
        price = quantity * 3
    elif fruit == "pineapple":
        price = quantity * 5.60
    elif fruit == "grapes":
        price = quantity * 4.2
    #print(f'{price:.2f}')
if day_of_week == "Monday" \
        or day_of_week == "Tuesday" \
        or day_of_week == "Wednesday" \
        or day_of_week == "Thursday" \
        or day_of_week == "Friday":
    if fruit == "banana":
        price = quantity * 2.50
    elif fruit == "apple":
        price = quantity * 1.20
    elif fruit == "orange":
        price = quantity * 0.85
    elif fruit == "grapefruit":
        price = quantity * 1.45
    elif fruit == "kiwi":
        price = quantity * 2.70
    elif fruit == "pineapple":
        price = quantity * 5.50
    elif fruit == "grapes":
        price = quantity * 3.85


if price == 0:
    print('error')
else:
    print(f'{price:.2f}')


# Магазин за плодове през работните дни работи на следните цени:Напишете програма, която чете от конзолата /
# следните три променливи, въведени от потребителя, и пресмята цената според цените от таблиците по-горе:
#     • плод  - banana / apple / orange / grapefruit / kiwi / pineapple / grapes;
#     • ден от седмицата  - Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday;
#     • количество (реално число).
# Резултатът да се отпечата закръглен с 2 цифри след десетичната точка. При невалиден ден от седмицата или /
# невалидно име на плод да се отпечата "error".