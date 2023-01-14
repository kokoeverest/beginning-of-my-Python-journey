pens_price = 5.80
pens = int(input()) * pens_price

marker_price = 7.20
markers = int(input()) * marker_price

board_cleaner_price = 1.20
board_cleaner = int(input()) * board_cleaner_price

discount = int(input()) / 100

price_before_discount = pens + markers + board_cleaner
total_price = price_before_discount - price_before_discount * discount

print(total_price)
