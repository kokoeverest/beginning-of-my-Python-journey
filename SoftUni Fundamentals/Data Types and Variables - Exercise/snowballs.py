snowballs = int(input())
highest_value, highest_weight, highest_time_needed, highest_quality = 0, 0, 0, 0
for throw in range(snowballs):
    weight, time_needed, quality = int(input()), int(input()), int(input())

    value = int((weight / time_needed) ** quality)
    if value > highest_value:
        highest_value, highest_weight, highest_time_needed, highest_quality = value, weight, time_needed, quality

print(f'{highest_weight} : {highest_time_needed} = {highest_value} ({highest_quality})')



# Tony and Andi love playing in the snow and having snowball fights, but they always argue about who makes
# the best snowballs. They have decided to involve you in their fray by writing a program that calculates
# snowball data and outputs the best snowball value.
# You will receive N – an integer, the number of snowballs being made by Tony and Andi.
# On the following lines, you will receive 3 inputs for each snowball:
#     • The weight of the snowball (integer).
#     • The time needed for the snowball to get to its target (integer).
#     • The quality of the snowball (integer).
# For each snowball, you must calculate its value by the following formula:
# (snowball_weight / snowball_time) ** snowball_quality
# In the end, you must print the highest calculated value of a snowball.
# Input
#     • On the first input line, you will receive N – the number of snowballs.
#     • On the next N*3 input lines, you will be receiving data about each snowball.
# Output
#     • You need to print the highest calculated snowball's value in the format:
# "{snowball_weight} : {snowball_time} = {snowball_value} ({snowball_quality})"
# Constraints
#     • The number of snowballs (N) will be an integer in range [0, 100].
#     • The weight is an integer in the range [0, 1000].
#     • The time is an integer in the range [1, 500].
#     • The quality is an integer in the range [0, 100].