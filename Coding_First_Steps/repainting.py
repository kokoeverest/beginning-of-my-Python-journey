nylon = int(input())
paint = int(input())
thinner = int(input())
work_hours = int(input())

nylon_price = 1.50
paint_price = 14.50
thinner_price = 5.0
bags_price = 0.40

nylon += 2
paint += paint * 0.10

materials_price = (nylon * nylon_price) + (paint * paint_price) + (thinner * thinner_price) + (bags_price * 1)
price_for_one_working_hour = materials_price * 0.30

total_price = materials_price + (price_for_one_working_hour * work_hours)

print(total_price)
