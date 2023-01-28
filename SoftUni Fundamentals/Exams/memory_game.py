
#  71/100 points in Judge, 2 unknown corner cases not resolved

sequence = input().split(' ')
moves = 0
game_over = False

if sequence[-1] == "":
    sequence.pop()
while True:
    user_input = input().split(' ')
    moves += 1
    if user_input == ["end"]:
        if len(sequence) > 1:
            print("Sorry you lose :(")
            game_over = True
        break
    index_1 = int(user_input[0])
    index_2 = int(user_input[1])
    str_on_current_index_1 = sequence[index_1]
    str_on_current_index_2 = sequence[index_2]
    if index_1 < 0 or index_2 < 0 or index_1 > len(sequence) or index_2 > len(sequence):
        print("Invalid input! Adding additional elements to the board")
        sequence.insert(int(len(sequence)/2), f"-{moves}a")
        sequence.insert(int(len(sequence)/2), f"-{moves}a")
    elif sequence[index_1] == sequence[index_2]:
        print(f"Congrats! You have found matching elements - {sequence[0]}!")
        sequence.remove(str_on_current_index_1)
        sequence.remove(str_on_current_index_2)
    else:
        print("Try again!")
    if sequence == [''] or sequence == []:
        print(f"You have won in {moves} turns!")
        break

lost_result = ""
for i in sequence:
    lost_result += str(i) + " "

if game_over:
    print(lost_result[:-1])

# problem description:

'''

Write a program that recreates the Memory game.
On the first line, you will receive a sequence of elements. Each element in the sequence will have a twin. Until the
player receives "end" from the console, you will receive strings with two integers separated by a space, representing
the indexes of elements in the sequence.
If the player tries to cheat and enters two equal indexes or indexes which are out of bounds of the sequence, you
should add two matching elements at the middle of the sequence in the following format:
"-{number of moves until now}a"
Then print this message on the console:
"Invalid input! Adding additional elements to the board"
Input
    • On the first line, you will receive a sequence of elements
    • On the following lines, you will receive integers until the command "end"
Output
    • Every time the player hit two matching elements, you should remove them from the sequence and print on the
    console the following message:
"Congrats! You have found matching elements - ${element}!"
    • If the player hit two different elements, you should print on the console the following message:
"Try again!"
    • If the player hit all matching elements before he receives "end" from the console, you should print on the
    console the following message:
"You have won in {number of moves until now} turns!"
    • If the player receives "end" before he hits all matching elements, you should print on the console the
    following message:
"Sorry you lose :(
{the current sequence's state}"
Constraints
    • All elements in the sequence will always have a matching element.

'''
