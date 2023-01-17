
year = int(input())
for i in range(year, 0, -12):
    
    if year % 12 == 8:
        print('Dragon')
    elif year % 12 == 9:
        print('Snake')
    elif year % 12 == 10:
        print('Horse')
    elif year % 12 == 11:
        print('Sheep')
    elif year % 12 == 0:
        print('Monkey')
    elif year % 12 == 1:
        print('Rooster')
    elif year % 12 == 2:
        print('Dog')
    elif year % 12 == 3:
        print('Pig')
    elif year % 12 == 4:
        print('Rat')
    elif year % 12 == 5:
        print('Ox')
    elif year % 12 == 6:
        print('Tiger')
    elif year % 12 == 7:
        print('Hare')
    break


# The Chinese zodiac assigns an animal to year according to the following table:

# Year	Animal		Year	Animal
# 2000	Dragon		2006	Dog
# 2001	Snake		2007	Pig
# 2002	Horse		2008	Rat
# 2003	Sheep		2009	Ox
# 2004	Monkey		2010	Tiger
# 2005	Rooster		2011	Hare
# Write a program that determines the zodiac sign for a particular year. /
# Note that the cycle repeats itself, so 2012 will be the year of the Dragon again.

# Input
# On the first line, you will receive the year

# Output
# On the only line of output, print the corresponding zodiac Sign

# Input
# 2000

# Output
# Dragon

# Input
# 1975

# Output
# Hare