from math import floor

group_size = int(input())
days = int(input())

coins = 0

for day in range(1, days + 1):
    # every 10th day 2 of the companions leave
    if day % 10 == 0:
        group_size -= 2
    # every 15th day 5 new companions join
    if day % 15 == 0:
        group_size += 5

    #  every day you earn 50 coins
    coins += 50 - (group_size * 2)

    if day % 3 == 0:
        coins -= group_size * 3
    if day % 5 == 0:
        coins += group_size * 20
    if day % 3 == 0 and day % 5 == 0:
        coins -= group_size * 2

print(f'{group_size} companions received {floor(coins / group_size)} coins each.')

# As a young adventurer, you travel with your group worldwide, seeking for gold and glory. But you need to split
# the profit among your companions.
# You will receive a group size. After that, you receive the days of the adventure.
# Every day, you earn 50 coins, but you also spend 2 coins per companion for food.
# Every 3rd (third) day, you organize a motivational party, spending 3 coins per companion for drinking water.
# Every 5th (fifth) day, you slay a boss monster and gain 20 coins per companion. But if you have a motivational
# party the same day, you spend additional 2 coins per companion.
# Every 10th (tenth) day at the start of the day, 2 (two) of your companions leave, but every 15th (fifteenth)
# day 5 (five) new companions are joined at the beginning of the day.
# You should calculate how many coins gets each companion at the end of the adventure.
# Input / Constraints
# The input will consist of exactly 2 lines:
#     • group size – integer in the range [1…100]
#     • days – integer in the range [1…100]
# Output
# Print the following message: "{companions_count} companions received {coins} coins each."
# Note: You cannot split a coin, so you should round down the coins to an integer number.