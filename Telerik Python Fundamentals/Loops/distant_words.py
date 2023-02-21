target_num = int(input())
words = int(input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'
total = 0
for i in range(1, words + 1):
    word = input()
    result = 0
    
    for letter in word:
        counter = 0
        for l in alphabet:
            counter += 1
            if letter == str(l):
                result += counter
    total += (abs(result - target_num))
    print(f'{word} {abs(result - target_num)}')
print(f'{total / words:.2f}')

# Angel and Bibkata have very weird taste - their last idea of fun is calculating the "distance" that a\
#  word is from a given number. The distance is calculated by summing the position in the alphabet of each \
# letter in the word and than finding the absolute difference between that word and another predefined number.\
#  You are a programmer so you must ruin their fun by automating the process.

# Examples:

# word 'bob', number = 22, distance = 3 ('b' + 'o' + 'b' = 2 + 15 + 2 = 19)
# word 'bob', number = 10, distance = 9
# Write a program that calculates the distance for each string and also outputs the average distance.

# Input
# The input consists of several lines.
# T - the target number
# N - the number of words to follow
# on the next N lines - each word on a new line
# Output
# Output consists of N + 1 lines
# First N lines - word + its distance in format word distance
# Last line - the average distance, rounded to two digits after the decimal point
# Constraints
# Each word consists of only uppercase and lowercase english alphabet letters
# 1 <= N <= 20
# 0 <= T <= 1000
# Sample Tests
# Input
# 28
# 3
# coffee
# tea
# pineapple
# Output
# coffee 12
# tea 2
# pineapple 66
# 26.67
# Input
# 10
# 4
# flower
# window
# curtain
# book
# Output
# flower 69
# window 78
# curtain 76
# book 33
# 64.00