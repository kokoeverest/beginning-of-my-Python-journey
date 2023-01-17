from math import floor

ship_width = float(input())
ship_length = float(input())
ship_height = float(input())
astronauts_average_height = float(input())

spaceship_volume = ship_height * ship_length * ship_width
room_volume = (astronauts_average_height + 0.40) * 2 * 2

total_ship_capacity = spaceship_volume / room_volume

if total_ship_capacity > 10:
    print("The spacecraft is too big.")
elif total_ship_capacity < 3:
    print("The spacecraft is too small.")
else:
    print(f"The spacecraft holds {floor(total_ship_capacity)} astronauts.")

# Георги трябва да построи космически кораб, който да събира част от екипажа му. За целта, той трябва да го
# направи така, че да има място за поне трима астронавти, но за не повече от 10. Всеки астронавт се нуждае от
# малка стая, която да е с размери: 2 метра ширина, 2 метра дължина и с височина, която е с 40 см повече от
# средната височина на астронавтите.
# Напишете програма, която изчислява обема на кораба, колко астронавта ще събере и принтира на
# конзолата дали корабът е достатъчно голям.
# Вход:
# Входът се чете от конзолата и съдържа точно 4 реда:
#  На първия ред е широчината на кораба - реално число в интервала [1.00... 10.00]
#  На втория ред е дължината на кораба - реално число в интервала [1.00…10.00]
#  На третия ред е височината на кораба - реално число в интервала [1.00…20.00]
#  На четвъртия ред е средната височина на астронавтите - реално число в интервала [1.50 … 1.90]
# Изход:
# Да се отпечата на конзолата един ред:
#  Ако броят на астронавтите е между 3 (вкл.) и 10 (вкл.):
# "The spacecraft holds {броя на астронавтите} astronauts."
#  Ако броят на астронавтите е по-малък от 3:
# "The spacecraft is too small."
#  Ако броят на астронавтите е по-голям от 10:
# "The spacecraft is too big."