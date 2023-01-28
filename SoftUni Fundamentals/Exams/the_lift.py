# input is the same for both solutions

people = int(input())
cabin_occupation = input().split(' ')

# solution 2: 60/100 in Judge, after 100 lines of code and countless if/else conditional statements...
'''
result = []
last_cabin = 0
the_lift_has_empty_spots = False

for current_cabin in cabin_occupation:
    cabin_capacity = 4
    if int(current_cabin) > 4:
        continue
    if people > 4:
        people -= cabin_capacity - int(current_cabin)
        result.append(cabin_capacity)

    elif people == 4:
        if cabin_capacity - int(current_cabin) == 1:
            people -= 1
            result.append(cabin_capacity)
            last_cabin = cabin_capacity
        elif cabin_capacity - int(current_cabin) == 2:
            people -= 2
            result.append(cabin_capacity)
            last_cabin = cabin_capacity
        elif cabin_capacity - int(current_cabin) == 3:
            people -= 3
            result.append(cabin_capacity)
            last_cabin = cabin_capacity
        elif cabin_capacity - int(current_cabin) == 4:
            people -= 4
            result.append(cabin_capacity)
            last_cabin = cabin_capacity
    elif people == 3:
        if cabin_capacity - int(current_cabin) == 1:
            people -= 1
            result.append(cabin_capacity)
            last_cabin = cabin_capacity
        elif cabin_capacity - int(current_cabin) == 2:
            people -= 2
            result.append(cabin_capacity)
            last_cabin = cabin_capacity
        elif cabin_capacity - int(current_cabin) == 3:
            people -= 3
            result.append(cabin_capacity)
            last_cabin = cabin_capacity
        elif cabin_capacity - int(current_cabin) == 4:
            last_cabin = people
            people -= 3
            result.append(last_cabin)
    elif people == 2:
        if cabin_capacity - int(current_cabin) == 1:
            people -= 1
            result.append(cabin_capacity)
            last_cabin = cabin_capacity
        elif cabin_capacity - int(current_cabin) == 2:
            people -= 2
            result.append(cabin_capacity)
            last_cabin = cabin_capacity
        elif cabin_capacity - int(current_cabin) == 3:
            last_cabin = people + int(current_cabin)
            people -= 2
            result.append(last_cabin)
        elif cabin_capacity - int(current_cabin) == 4:
            last_cabin = people + int(current_cabin)
            people -= 2
            result.append(last_cabin)
    elif people == 1:
        if cabin_capacity - int(current_cabin) == 1:
            people -= 1
            result.append(cabin_capacity)
            last_cabin = cabin_capacity
        elif cabin_capacity - int(current_cabin) == 2:
            last_cabin = people + int(current_cabin)
            people -= 1
            result.append(last_cabin)
        elif cabin_capacity - int(current_cabin) == 3:
            last_cabin = people + int(current_cabin)
            people -= 1
            result.append(last_cabin)
        elif cabin_capacity - int(current_cabin) == 4:
            last_cabin = people + int(current_cabin)
            people -= 1
            result.append(last_cabin)
    if people == 0:
        if last_cabin < 4 or 0 <= int(current_cabin) < 4:
            the_lift_has_empty_spots = True
            break

final_result = ''
for i in result:
    final_result += str(i) + " "

if the_lift_has_empty_spots:
    print("The lift has empty spots!")
    print(final_result)
elif people == 0 and last_cabin == 4:
    print(final_result)
else:
    print(f"There isn't enough space! {people} people in a queue!")
    print(final_result)'''

# solution 1: 70/100 in Judge; problem with people < 4 and semi full cabins left
'''
result = []
last_digit = 0
for cab in cabin_occupation:
    if people <= 0:
        break

    if 4 > people > 0:
        last_digit = people + int(cab)
        result.append(people + int(cab))
        people -= people
        break

    current_cabin = 4
    people -= current_cabin - int(cab)
    result.append(current_cabin)
    last_digit = current_cabin

final_result = ''
for i in result:
    final_result += str(i) + " "

if people == 0 and last_digit == 4:
    print(final_result)
elif people == 0 and 0 < last_digit < 4:
    print("The lift has empty spots!")
    print(final_result)
else:
    print(f"There isn't enough space! {people} people in a queue!")
    print(final_result)
'''

# problem description

'''Write a program that finds a place for the tourist on a lift. 
Every wagon should have a maximum of 4 people on it. If a wagon is full, you should direct the people to the next
one with space available.
Input
    • On the first line, you will receive how many people are waiting to get on the lift
    • On the second line, you will receive the current state of the lift separated by a single space: " ".
Output
When there is no more available space left on the lift, or there are no more people in the queue, you should print
on the console the final state of the lift's wagons separated by " " and one of the following messages:
    • If there are no more people and the lift have empty spots, you should print:
"The lift has empty spots!
{wagons separated by ' '}"
    • If there are still people in the queue and no more available space, you should print:
"There isn't enough space! {people} people in a queue!
{wagons separated by ' '}"
    • If the lift is full and there are no more people in the queue, you should print only the wagons separated by " "
    '''
