dancers = int(input())
points = float(input())
season = input()
country = input()

money_prize = 0

if country == 'Bulgaria':
    money_prize = points * dancers
    if season == 'summer':
        money_prize = money_prize - (money_prize * 0.05)
    elif season == 'winter':
        money_prize = money_prize - (money_prize * 0.08)
elif country == 'Abroad':
    money_prize = (points * dancers) + (points * dancers * 0.50)
    if season == 'summer':
        money_prize = money_prize - (money_prize * 0.10)
    elif season == 'winter':
        money_prize = money_prize - (money_prize * 0.15)

money_for_charity = money_prize * 0.75
money_left = money_prize - money_for_charity

print(f'Charity - {money_for_charity:.2f}')
print(f'Money per dancer - {money_left / dancers:.2f}')




# След успешно класиране, група заминава за финалното състезание. След представянето си всяка група
# получава парична награда. Тя зависи от: държавата, в която се е провело състезанието; броя точки, които
# журито е дало и сезонът, през който се е провело състезанието.
#  Ако състезанието се е провело в България паричната награда се изчислява като се умножат точките
# по броя участниците.
#  Ако се е провело в чужбина – се умножават броя участници по броя точки и към тях се добавя 50% от
# получената сума.
# От получената сума се изваждат разходите посочени в проценти спрямо сезона, през който се е провел:
# След завръщането си групата дарява 75% от сумата, след приспаднатите разходи, за благотворителност.
# Останалата сума се разпределя между членовете на групата.
# Да се напише програма, която изчислява колко пари са дадени за благотворителност и колко е получил
# всеки един член на групата.
'''
# Вход:
# От конзолата се четат 4 реда:
# 1. Брой танцьори – цяло число в интервала [1 ... 10]
# 2. Брой точки – реално число в интервала [1.00 ... 10000.00]
# 3. Сезон – текст със следните възможности - "summer" или "winter"
# 4. Място – текст със следните възможности - "Bulgaria" или "Abroad"
'''
# Изход:
# На конзолата се отпечатват 2 реда:
#  Сумата, която са дали за благотворителност
# "Charity - {сума за благотворителност}"
#  Сумата, която е получил всеки танцьор
# "Money per dancer - {сума за танцьор}"
# Сумите да бъдат форматирани до втория знак след десетичната запетая.