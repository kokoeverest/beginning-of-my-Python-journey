day = input()
ticket_price = 0

if day == "Monday":
    ticket_price = 12
elif day == "Tuesday":
    ticket_price = 12
elif day == "Wednesday":
    ticket_price = 14
elif day == "Thursday":
    ticket_price = 14
elif day == "Friday":
    ticket_price = 12
elif day == "Saturday" or day == "Sunday":
    ticket_price = 16

print(ticket_price)
# Да се напише програма която чете ден от седмицата (текст) – въведен от потребителя и принтира на /
# конзолата цената на билет за кино според деня от седмицата: