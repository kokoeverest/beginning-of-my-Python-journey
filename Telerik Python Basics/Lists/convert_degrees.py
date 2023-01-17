degrees_celsius = input().split(' ')

for value in degrees_celsius:
    result = int(value) * 1.8 + 32 # the formula to convert Celcius to Fahrenheit
    print(round(result))

# You need to provide conversion of the temperature given in Celsius to their Fahrenheit representation.

# Explanation
# Hint
# Search how you could split the list of values and then you can iterate over them.
# JavaScript
# forEach
# Java
# For-each loop
# C#
# For-each loop
# Input
# On the first line, you will receive a list of values separated by a single space.
# Output
# On each line in the output print the converted temperature. Print a whole number rounded to the nearest integer \
# (Math rules apply) and without digits after the decimal point.
# Input
# 0 15 30
# Output
# 32
# 59
# 86