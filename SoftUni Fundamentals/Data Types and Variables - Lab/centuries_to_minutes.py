centuries = int(input())


years = centuries * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60

print(f'{centuries} centuries = {years:.0f} years = {days:.0f} days = {hours:.0f} hours = {minutes:.0f} minutes')
# # Write a program that reads an integer number of centuries and converts it to years, days, hours, and minutes.
#
# Examples
# Input # Output
# 1 # 1 centuries = 100 years = 36524 days = 876576 hours = 52594560 minutes
# 5 # 5 centuries = 500 years = 182621 days = 4382904 hours = 262974240 minutes
# Hints
#     • Assume that one year has 365.2422 days on average (the Tropical year).