num = int(input())
total_sum = 0
for i in range(num):
    symbol = input()
    total_sum += ord(symbol)
print(f'The sum equals: {total_sum}')

# Write a program, which sums the ASCII codes of N characters and prints the sum on the console.
# On the first line, you will receive N – the number of lines. On the following N lines – you will receive a
# letter per line. Print the total sum in the following format: "The sum equals: {total_sum}".
# Note: n will be in the interval [1…20].