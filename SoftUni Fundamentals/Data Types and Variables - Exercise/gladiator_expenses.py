lost_fights = int(input())
helmet_price, sword_price, shield_price, armor_price = float(input()), float(input()), float(input()), float(input())

total_expenses = 0
shield_breaks = 0

for fight in range(1, lost_fights + 1):
    day_expenses = 0
    if fight % 2 == 0 and fight % 3 == 0:
        day_expenses += helmet_price + sword_price + shield_price
        shield_breaks += 1
    elif fight % 2 == 0:
        day_expenses += helmet_price
    elif fight % 3 == 0:
        day_expenses += sword_price
    if shield_breaks == 2:
        day_expenses += armor_price
        shield_breaks = 0
    total_expenses += day_expenses

print(f'Gladiator expenses: {total_expenses:.2f} aureus')

# As a gladiator, Peter needs to repair his broken equipment when he loses a fight. His equipment consists of a
# helmet, a sword, a shield, and an armor.
# You will receive Peter's lost fights count.

# Every second lost game, his helmet is broken.

# Every third lost game, his sword is broken.

# When both his sword and helmet are broken in the same lost fight, his shield also breaks.

# Every second time his shield brakes, his armor also needs to be repaired.

# You will receive the price of each item in his equipment. Calculate his expenses for the year for renewing his
# equipment.
# Input / Constraints
# The input will consist of 5 lines:
#     • On the first line, you will receive the lost fights count – an integer in the range [0, 1000].
#     • On the second line, you will receive the helmet price - a floating-point number in the range [0, 1000].
#     • On the third line, you will receive the sword price - a floating-point number in the range [0, 1000].
#     • On the fourth line, you will receive the shield price - a floating-point number in the range [0, 1000].
#     • On the fifth line, you will receive the armor price - a floating-point number in the range [0, 1000].
# Output
#     • As output, you must print Peter`s total expenses for new equipment: "Gladiator expenses: {expenses} aureus"