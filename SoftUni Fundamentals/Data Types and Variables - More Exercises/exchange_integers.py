a, b = int(input()), int(input())

print('Before:')
print(f'a = {a}')
print(f'b = {b}')
print('After: ')

c = b
b = a
a = c
print(f'a = {a}')
print(f'b = {b}')



# Read two integer numbers and, after that, exchange their values. Print the variable values before and
# after the exchange, as shown below: