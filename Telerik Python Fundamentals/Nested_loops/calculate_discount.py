items = int(input())
discounted_item = 0

for x in range(items):
    price = float(input())
    discounted_item = price * 0.35

    print(f'{discounted_item:.2f}')



# You need to calculate the discounted price for each item in your shopping cart. /
# The discount is 65%, a real deal for you.
# Input

#     On the first line, you will receive N - the number of the items in your shopping cart
#     On the next N lines you will each item's price

# Output

#     On each line in the output print the discounted price of the item with /
# two digits after the decimal point (Math rules for rounding apply)
