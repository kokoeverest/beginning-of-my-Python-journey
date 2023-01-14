from math import ceil, floor

days_missing = int(input())
food_in_kilos = int(input())
food_deer_one = float(input())
food_deer_two = float(input())
food_deer_three = float(input())

deer_one_total = food_deer_one * days_missing
deer_two_total = food_deer_two * days_missing
deer_three_total = food_deer_three * days_missing

total_food = deer_one_total + deer_two_total + deer_three_total

if food_in_kilos >= total_food:
    print(f'{floor(food_in_kilos - total_food)} kilos of food left.')
else:
    print(f'{ceil(total_food - food_in_kilos)} more kilos of food are needed.')

# Дядо Коледа много обича да пътешества, но за съжаление се случило, така че точно преди да замине на
# почивка три от елените му се разболяли и трябва да ги остави. Когато заминава, той трябва да съобрази колко
# храна да остави на всеки един от елените, за да не останат гладни. Напишете програма, която пресмята дали
# оставената от Дядо Коледа храна ще е достатъчна за времето, в което него няма да го има. Всеки елен изяжда
# определено количество храна на ден.

# Вход:
# От конзолата се четат пет реда:
#  Първи ред – брой дни, в които Дядо Коледа отсъства – цяло число в интервала [1...5000]
#  Втори ред – оставена храна в килограми – цяло число в интервала [0...100000]
#  Трети ред – храна на ден за първия елен в килограми – реално число в интервала [0.00...100.00]
#  Четвърти ред – храна на ден за втория елен в килограми– реално число в интервала [0.00...100.00]
#  Пети ред – храна на ден за третия елен в килограми – реално число в интервала [0.00...100.00]

# Изход:
# На конзолата трябва да се отпечата на един ред:
#  Ако оставената храна Е достатъчна:
# o “{килограми, които остават} kilos of food left.”
#  Резултатът трябва да е закръглен към ПО-МАЛКОТО цяло число
#  Ако оставената храна НЕ Е достатъчна:
# o “{килограми, които не недостигат} more kilos of food are needed.”
#  Резултатът трябва да е закръглен към ПО-ГОЛЯМОТО цяло число