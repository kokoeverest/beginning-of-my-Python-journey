items = int(input())
days = int(input())

total_days = 0
total_price = 0
total_spirit = 0
while True:

    for day in range(1, days + 1):

        # check every second day
        if day % 2 == 0:
            if day % 10 == 0:  # possible days are 10; 20; 30; 40; 50; 60; 70; 80; 90; 100
                total_spirit -= 20
            if day % 11 == 0:  # possible days are 22; 44; 66; 88
                total_price += (23 * items) * 2
                continue
            total_price += 2 * items
            total_spirit += 5

        # check every third day
        if day % 3 == 0:
            if day % 11 == 0:  # possible days are 33; 66; 99
                total_price += (23 * items) * 2
                continue
            total_price += 8 * items
            total_spirit += 13

    # check every fifth day
        if day % 5 == 0:
            total_price += 15 * items
            total_spirit += 17
            if day % 15 == 0:  # possible days 15; 30; 45; 60; 75; 90
                total_spirit += 30
                total_price += 8 * items
            if day % 10 == 0:  # possible days are 10; 20; 30; 40; 50; 60; 70; 80; 90; 100
                total_price += 23 * items

    # check every eleventh day
        if day % 11 == 0:  # possible days are 11; 22; 33; 44; 55; 66; 77; 88; 99
            total_price += (2 * items) * 2

    # check if the last day is tenth day
    if days % 10 == 0:  # possible days are 10; 20; 30; 40; 50; 60; 70; 80; 90; 100
        total_spirit -= 30

    break
print(f'Total cost: {total_price}')
print(f'Total spirit: {total_spirit}')
