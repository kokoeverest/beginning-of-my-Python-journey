month = input()
nights = int(input())

apartment_price = 0
studio_price = 0

if month == "May":
    apartment_price = 65 * nights
    studio_price = 50 * nights
    if nights > 14:
        studio_price *= 0.70
    elif nights > 7:
        studio_price *= 0.95
    # elif nights < 7:
    #     apartment_price = nights * 65
    #     studio_price = nights * 50
elif month == "June":
    apartment_price = nights * 68.70
    studio_price = nights * 75.20
    if nights > 14:
        studio_price *= 0.80
elif month == "July":
    apartment_price = nights * 77
    studio_price = nights * 76
elif month == "August":
    apartment_price = nights * 77
    studio_price = nights * 76
elif month == "September":
    apartment_price = nights * 68.70
    studio_price = nights * 75.20
    if nights > 14:
        studio_price *= 0.80
elif month == "October":
    apartment_price = nights * 65
    studio_price = nights * 50
    if nights > 14:
        studio_price *= 0.70
    elif nights > 7:
        studio_price *= 0.95

if nights > 14:
    apartment_price *= 0.90

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")

# Хотел предлага 2 вида стаи: студио и апартамент. Напишете програма, която изчислява цената за целия престой /
# за студио и апартамент. Цените зависят от месеца на престоя:Предлагат се и следните отстъпки:
#     • За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
#     • За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
#     • За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
#     • За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.

'''
# Вход
# Входът се чете от конзолата и съдържа точно 2 реда, въведени от потребителя:
#     • На първия ред е месецът - May, June, July, August, September или October;
#     • На втория ред е броят на нощувките - цяло число.
'''
# Изход
# Да се отпечатат на конзолата 2 реда:
#     • На първия ред: "Apartment: {цена за целият престой} lv."
# На втория ред: "Studio: {цена за целият престой} lv."Цената за целия престой да е форматирана с точност до два знака след десетичната запетая.