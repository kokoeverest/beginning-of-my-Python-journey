budget = float(input())
season = input()

destination = None
hotel_or_camping = None
total_price = 0

if budget <= 100:
    if season == "summer":
        destination = "Bulgaria"
        total_price = budget * 0.30
        hotel_or_camping = "Camp"
    else:
        destination = "Bulgaria"
        total_price = budget * 0.70
        hotel_or_camping = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        total_price = budget * 0.40
        hotel_or_camping = "Camp"
    else:
        destination = "Balkans"
        total_price = budget * 0.80
        hotel_or_camping = "Hotel"

elif budget > 1000:
    destination = "Europe"
    total_price = budget * 0.9
    hotel_or_camping = "Hotel"

print(f"Somewhere in {destination}")
print(f"{hotel_or_camping} - {total_price:.2f}")
