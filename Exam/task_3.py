blossom_date = input().split(' ')
avg_temp_prediction = int(input())
rainfall = int(input())
winter_length = int(input())

leap_years = []
for year in range(2000, int(blossom_date[2]), 4):
    leap_years.append(year)

additional_days = winter_length / 7
new_blossom_date = int(blossom_date[0]) + additional_days

if int(blossom_date[2]) in leap_years:
    avg_temp_prediction += 5
if avg_temp_prediction > 20:
    for i in range(20, avg_temp_prediction):
        new_blossom_date += 1
elif avg_temp_prediction < 20:
    for i in range(20, avg_temp_prediction):
        new_blossom_date -= 1

if rainfall > 30:
    for j in range(30, rainfall, 3):
        new_blossom_date += 1
elif rainfall < 30:
    for j in range(30, rainfall, -3):
        new_blossom_date -= 1

print(int(new_blossom_date), blossom_date[1], blossom_date[2])

# Cherry Blossom
# Japanese scientists have invented a new type of cherry tree that blossoms in blue. However, due to gene modification the tree is very /
# sensitive to weather conditions - expected blossom date is always in March, but sometimes the trees blossom in February, and sometimes /
# in April. That's why scientists had to develop a set of rules to predict the exact date the cherry tree will blossom. There are several /
# factors to account for: winter length, rain quantity during blossom season, average temperature and the expected blossom day.

# Here are how these factors affect the blossom process - each week of the winter will cause the cherry tree to blossom one day later that /
# the expected blossom date. The optimal average temperature is 20. Each degree over that will cause the tree to blossom one day earlier, /
# and each degree below what will cause the tree to blossom one day later. Optimal rain is 30cm, each 3 cm below or over will cause the tree /
# to blossom one day later. And on leap years average temperature is 5 degrees over the expected temperature.

# Following these instruction and given the expected blossom date your task is to find the exact date the tree will blossom.

# Input
# Exactly 4 lines:

# the expected blossom date (day, full month name, year)
# average temperature prediction
# rain
# winter length (in days)

# Output
# Exactly one line:

# the date the cherry tree will blossom (day, full month name, year)

# Sample tests

# Input
# 11 March 2021
# 22
# 27
# 35

# Output
# 15 March 2021

# Input
# 7 March 2021
# 30
# 30
# 7

# Output
# 26 February 2021