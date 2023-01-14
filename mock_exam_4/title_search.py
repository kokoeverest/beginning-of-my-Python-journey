title = input()
lines = int(input())

title_list = []
for index in title:
    title_list.append(index)

modified_title = ''

for i in range(lines):
    letters = input()
    if letters not in modified_title:
        print('No such title found!')
        break
    new_title = ''
    
    for j in letters:
        modified_title += str(j)
        
        if j in title_list:
            title_list.remove(j)
            
        if title_list == []:
            print(' ')
            break
    for k in title_list:
        new_title += str(k)    
    print(new_title)
    
    continue

# You will receive a string title which contains only small latin letters [a-z]. After that you will have to read from /
# the input N lines of text. For each of these lines, your task is to find out if there is such a sequence in the string /
# you receive as input on the first line (title). The sequence may not be on consecutive indices. Each time you find a/
#  sequence of these characters you remove it from the initial string and print the modified string. If no such sequence //
# is found you have to print No such title found! and not modify the string.

# Examples:
# telerik is found in telerikacademy and the remaining string is academy
# telerik is also found in tpeplpeprik and the remaining string is pppp
# Input
# Read from the standard input
# On the first line you receive a string containing small latin letters [a-z]
# On the next line you receive an integer N which represents the number of lines which you will have to read
# On each of the next N lines you receive a string
# Output
# Print on the standard output
# On every N line, print the result of the operation
# Examine the sample tests for explanation
# Constraints
# 3 <= N <= 10
# 200 <= title.length() <= 5000