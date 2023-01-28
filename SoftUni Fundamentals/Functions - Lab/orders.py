product = input()
quantity = int(input())


def order_calculator(a, b):
    if a == "coffee":
        return b * 1.50
    elif a == "water":
        return b * 1.00
    elif a == "coke":
        return b * 1.40
    elif a == "snacks":
        return b * 2.00


print(f"{order_calculator(product, quantity):.2f}")
# Write a function that calculates the total price of an order and returns it. The function should receive one of the
# following products: "coffee", "coke", "water", or "snacks", and a quantity of the product. The prices for a single
# piece of each product are:
#     • coffee - 1.50
#     • water - 1.00
#     • coke - 1.40
#     • snacks - 2.00
#
# Print the result formatted to the second decimal place.
