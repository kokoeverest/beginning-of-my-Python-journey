N = int(input())
received_numbers = []
most_occurance = []
most_seen = 0
for i in range(0, N):
    numbers = int(input())
    if N == 1:
        received_numbers.append(numbers)

    if numbers in received_numbers:
        most_occurance.append(numbers)
        
    else:
        received_numbers.append(numbers)
        

if most_occurance == []:
    print(min(received_numbers))
else:
    print(min(most_occurance))


# Repeating Numbers
# Write a program that accepts an array of integers and returns the one that occurs the most times. /
# If there are two numbers that occur the same amount of times, return the smaller of the two.

# Input
# Read from the standard input;
# The number N is on the first line;
# An integer between 1 and 10 is written on each of the next N lines;
# The input data will always be valid and in the format described. There is no need to check it explicitly;
# Output
# Print to the standard output;
# On the only output line you must print the number that occurs the most;
# Constraints
# The number N is a positive integer between 1 and 100 000, inclusive;
# The list of numbers consists of positive integers between 1 and 10, inclusive;
# Sample tests
# Input
# 1
# 6
# Output
# 6
# Input
# 4
# 1
# 3
# 3
# 7
# Output
# 3
# Input
# 5
# 1
# 2
# 3
# 1
# 2
# Output
# 1