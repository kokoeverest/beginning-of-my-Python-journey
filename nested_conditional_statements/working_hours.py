time = int(input())
day = input()

if day == "Monday" \
        or day == "Tuesday" \
        or day == "Wednesday"\
        or day == "Thursday" \
        or day == "Friday" \
        or day == "Saturday":
        if time >= 10 and time <= 18:
            print("open")
        else:
            print("closed")
else:
    print("closed")

# Да се напише програма, която чете час от денонощието(цяло число) и ден от седмицата(текст) - въведени от /
# потребителя и проверява дали офисът на фирма е отворен, като работното време на офисът е от 10-18 часа, от /
# понеделник до събота включително