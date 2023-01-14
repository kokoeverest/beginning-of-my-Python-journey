sector = input()
rows = int(input())
odd_row_seats = int(input())

all_seats = 0
seats = 0
current_sector = ''
initial_odd_row_seats = odd_row_seats

for s in range(65, 91): # ASCII codes for letters A-Z
    current_sector = chr(s)
    for row in range(1, rows + 1):
        if row % 2 == 0:
            odd_row_seats += 2
        for t in range(97, 123): # ASCII codes for letters a-z
            seats += 1
            print(f'{s:c}{row}{t:c}') # format the iterator to letter, according to the ASCII code
            all_seats += 1
            if seats >= odd_row_seats:
                seats = 0
                odd_row_seats = initial_odd_row_seats
                break
    rows += 1
    if current_sector == sector:
        break
print(all_seats)


# Младоженците искат да направят списък кой на кое място ще седи на сватбената церемония. Местата са разделени на /
# различни сектори. Секторите са главните латински букви като започват от A. Във всеки сектор има определен брой редове./
# От конзолата се чете броят на редовете в първия сектор (A), като във всеки следващ сектор редовете се увеличават с 1./
# На всеки ред има определен брой места - тяхната номерация е представена с малките латински букви. /
# Броя на местата на нечетните редове се прочита от конзолата, а на четните редове местата са с 2 повече.
# Вход
# От конзолата се четaт 3 реда:
#     • Последния сектор от секторите - символ (B-Z)
#     • Броят на редовете в първия сектор - цяло число (1-100)
#     • Броят на местата на нечетен ред - цяло число (1-24)
# Изход
# Да се отпечата на конзолата всяко място на отделен ред по следния формат:
# {сектор}{ред}{място}
# Накрая трябва да отпечата броя на всички места.