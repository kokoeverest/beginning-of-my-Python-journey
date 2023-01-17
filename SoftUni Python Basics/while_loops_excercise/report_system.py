needed_money = int(input())
collected_money = 0
counter = 0
cash_transactions = 0
cash_money = 0
card_transactions = 0
card_money = 0
while True:
    if collected_money >= needed_money:
        print(f'Average CS: {cash_money / cash_transactions:.2f}')
        print(f'Average CC: {card_money / card_transactions:.2f}')
        break
    # elif collected_money < needed_money:
    #     print(f'Failed to collect required money for charity.')
    #     break
    item_price = input()

    if item_price == 'End':
        print(f'Failed to collect required money for charity.')
        break
    counter += 1
    if counter % 2 == 0 and int(item_price) < 10:
        print('Error in transaction!')
    elif counter % 2 == 0 and int(item_price) >= 10:
        collected_money += int(item_price)
        card_money += int(item_price)
        card_transactions += 1
        print('Product sold!')

    if counter % 2 == 1 and int(item_price) > 100:
        print('Error in transaction!')
    elif counter % 2 == 1 and int(item_price) <= 100:
        collected_money += int(item_price)
        cash_money += int(item_price)
        cash_transactions += 1
        print('Product sold!')
