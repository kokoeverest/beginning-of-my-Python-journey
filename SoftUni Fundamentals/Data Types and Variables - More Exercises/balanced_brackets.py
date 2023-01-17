lines = int(input())
brackets = []
counter = 0
for line in range(lines):
    symbol = input()

    if (symbol == ')' and brackets == []) or (symbol == '(' and '(' in brackets):
        counter -= 1
        continue
    if symbol == '(' or symbol == ')' and ')' not in brackets:
        brackets.append(symbol)
    if '(' and ')' in brackets:
        counter += 1
        brackets = []
if counter > 0:
    print('BALANCED')
else:
    print('UNBALANCED')


# On the first line, you will receive n – the number of lines, which will follow. On the following n lines,
# you will receive one of the following:
#     • Opening bracket – "(",
#     • Closing bracket – ")" or
#     • Random string
# Your task is to find out if the brackets are balanced. That means after every opening bracket should follow a
# closing one. Nested parentheses are not valid, and if, for example, two consecutive opening brackets exist,
# the expression should be marked as unbalanced. You should print "BALANCED" if the parentheses are balanced
# and "UNBALANCED"