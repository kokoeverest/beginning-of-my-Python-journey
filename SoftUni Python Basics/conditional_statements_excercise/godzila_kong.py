budget = float(input())
statist = int(input())
statist_clothes = float(input())

decoration = budget * 0.10
statist_clothes_price = statist * statist_clothes

if statist >= 150:
    statist_clothes_price = statist_clothes_price * 0.90

money = abs(budget - (decoration + statist_clothes_price))

if decoration + statist_clothes_price > budget:
    print("Not enough money!")
    print(f"Wingard needs {money:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {money:.2f} leva left.")
