gifts = input().split(" ")

while True:
    command = input().split(" ")
    if command == ["No", "Money"]:
        break
    for element in command:

        if command == "OutOfStock":
            continue
        if element in gifts:
            for elem in range(len(gifts)):
                if element in gifts[elem]:
                    gifts.insert(elem, "None")
                    gifts.remove(element)
                else:
                    continue
        if element == "Required":
            current_command = command[1]
            if int(command[2]) <= len(gifts):
                gifts.insert(int(command[2]) + 1, current_command)
                gifts.remove(gifts[int(command[2])])
                break
        if element == "JustInCase":
            gifts.pop()
            gifts.append(command[1])
            break
result = ''
for e in gifts:
    if e == "None":
        pass
    else:
        result += e + ' '
print(result)


# As a good friend, you decide to buy presents for your friends.
# Create a program that helps you plan the gifts for your friends and family. First, you are going to receive
# the gifts you plan on buying on a single line, separated by space, in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
#     • "OutOfStock {gift}"
#         ◦ Find the gifts with this name in your collection, if any, and change their values to "None".
#     • "Required {gift} {index}"
#         ◦ If the index is valid, replace the gift on the given index with the given gift.
#     • "JustInCase {gift}"
#         ◦ Replace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with value "None", separated by a single space
# in the following format:
# "{gift1} {gift2} {gift3} … {giftn}"
# Input / Constraints
#     • On the 1st line,  you will receive the names of the gifts, separated by a single space.
#     • On the following lines, until the "No Money" command is received, you will be receiving commands.
#     • The input will always be valid.
# Output
#     • Print the gifts in the format described above.
