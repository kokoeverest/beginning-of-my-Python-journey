number = int(input())

max = 0
min = 0
sum = 0
avg = 0
minimal = 0

for _ in range(number):
    lines = float(input())
    sum += lines
    avg += 1
    if lines > max:
        max = lines
    if lines < max:
        min = lines
    
print(f'min={min:.2f}')
print(f'max={max:.2f}')
print(f'sum={sum:.2f}')
print(f'avg={sum / avg:.2f}')
# Description

# Write a program that reads from the console a sequence of N real numbers and returns the minimal, /
# the maximal number, the sum and the average of all numbers (displayed with 2 digits after the decimal point)./


#     The input starts by the number N (alone in a line) followed by N lines, each holding an real number.
#     The output is like in the examples below.

# Input

#     On the first line, you will receive the number N.
#     On each of the next N lines, you will receive a single real number.

# Output

#     You output must always consist of exactly 4 lines - the minimal element on the first line, the /
# maximal on the second, the sum on the third and the average on the fourth, in the following format:
