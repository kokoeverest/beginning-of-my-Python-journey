total_price = 0

special = False
regular = True

while True:
    price = input()
    current_price = 0
    if price == "special":
        special = True
        regular = False
        break
    elif price == "regular":
        break
    else:
        if float(price):
            current_price += float(price)
            if current_price < 0:
                print("Invalid price!")
            else:
                total_price += current_price
        else:
            current_price = int(price)
            total_price += current_price
taxes = total_price * 0.20
special_price = (total_price + taxes) * 0.90

if total_price != 0:
    if special:
        print(f"Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total_price:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print("-----------")
        print(f"Total price: {special_price:.2f}$")
    else:
        print(f"Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total_price:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print("-----------")
        print(f"Total price: {total_price + taxes:.2f}$")
else:
    print("Invalid order!")

# Write a program that prints you a receipt for your new computer. You will receive the parts' prices (without tax)
# until you receive what type of customer this is - special or regular. Once you receive the type of customer you
# should print the receipt.
# The taxes are 20% of each part's price you receive.
# If the customer is special, he has a 10% discount on the total price with taxes.
# If a given price is not a positive number, you should print "Invalid price!" on the console and continue

# Input
#     • You will receive numbers representing prices (without tax) until command "special" or "regular":
# Output
#     • The receipt should be in the following format:
# "Congratulations you've just bought a new computer!
# Price without taxes: {total price without taxes}$
# Taxes: {total amount of taxes}$
# -----------
# Total price: {total price with taxes}$"
# Note: All prices should be displayed to the second digit after the decimal point! The discount is applied only
# on the total price. Discount is only applicable to the final price!