vacation_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

puzzle_price = 2.60
doll_price = 3
bear_price = 4.10
minion_price = 8.20
truck_price = 2

total_toys_price = \
    (puzzles * puzzle_price) + \
    (dolls * doll_price) + \
    (bears * bear_price) + \
    (minions * minion_price) + \
    (trucks * truck_price)
total_toys = puzzles + dolls + bears + minions + trucks

if total_toys >= 50:
    total_toys_price *= 0.75

loan = total_toys_price - (total_toys_price * 0.90)
money_left = total_toys_price - loan

if total_toys_price >= vacation_price:
    print(f"Yes! {money_left - vacation_price:.2f} lv left.")
else:
    print(f"Not enough money! {vacation_price - money_left:.2f} lv needed.")

# 90/100 points in judge!
