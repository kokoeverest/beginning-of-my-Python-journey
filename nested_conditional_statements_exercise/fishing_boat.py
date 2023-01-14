budget = int(input())
season = input()
fisherman_count = int(input())

total_price = 0
boat_price = 0

if season == "Spring":
    boat_price = 3000
elif season == "Summer" or season == "Autumn":
    boat_price = 4200
elif season == "Winter":
    boat_price = 2600

if fisherman_count <= 6:
    boat_price *= 0.9
elif 7 < fisherman_count <= 11:
    boat_price *= 0.85
elif fisherman_count > 12:
    boat_price *= 0.75

if fisherman_count % 2 == 0 and season != "Autumn":
    boat_price *= 0.95

if budget >= boat_price:
    print(f"Yes! You have {budget - boat_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {boat_price - budget:.2f} leva.")


