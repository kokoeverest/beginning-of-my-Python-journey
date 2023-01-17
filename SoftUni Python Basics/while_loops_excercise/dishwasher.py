detergent = int(input())
counter = 0

total_detergent = detergent * 750
plates_washed = 0
pots_washed = 0
used_detergent = 0
while True:
    if used_detergent > total_detergent:
        break
    dishes = input()

    if dishes == 'End':
        break

    counter += 1

    if counter % 3 == 0:
        plate_detergent = int(dishes) * 15
        pots_washed += int(dishes)
        used_detergent += plate_detergent
        continue
    plate_detergent = int(dishes) * 5
    used_detergent += plate_detergent
    plates_washed += int(dishes)
if used_detergent > total_detergent:
    print(f'Not enough detergent, {used_detergent - total_detergent} ml. more necessary!')
else:
    print('Detergent was enough!')
    print(f'{plates_washed} dishes and {pots_washed} pots were washed.')
    print(f'Leftover detergent {total_detergent - used_detergent} ml.')
