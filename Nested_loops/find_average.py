values = int(input())
result = 0

for _ in range(values):
    n = float(input())
    result += n

print(f'{result / values:.2f}')
# You need to calculate the average of a collection of values. Every value will be valid number. /
# The average must be printed with two digits after the decimal point.
# Input

#     On the first line, you will receive N - the number of the values you must read
#     On the next N lines you will receive numbers.

# Output

#     On the only line of output, print the average with two digits after the decimal point.