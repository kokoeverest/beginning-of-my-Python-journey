number = int(input())
result = ''
for i in range(0, number):
    result += '*'
    print(result)


for r in range(number - 1, 0, - 1):
    reverse = ''
    reverse += r * '*'
    print(reverse)

# Write a program that receives a number and creates the following pattern. The number represents the largest count \
# of stars on one row.