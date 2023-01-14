N = input()

odd_digits = []
even_digits = []
number = 0 
sum_odds = 0
sum_evens = 0
for i in N[0:18]:
    if int(i) % 2 == 1:
        odd_digits.append(i)
        sum_odds += int(i)
    else:
        even_digits.append(i)
        sum_evens += int(i)

if sum_odds > sum_evens:
    print(f'{sum_odds} cups of coffee')
elif sum_evens > sum_odds:
    print(f'{sum_evens} energy drinks')
else:
    print(f'{sum_odds} of both')
# Energy drink calculations are simple - in order to decide how many drinks you should have, you are given a number. Find the sum of the even digits and the sum of the odd digits of that number, then compare these sums and:

# If the sum of the even digits is bigger, drink energy drinks.
# If the sum of the odd digits is bigger, drink cups of coffee.
# If the two sums are equal, drink both.

# Input
# The input data is read from the standard input (the console).

# The only input line contains the number N.

# Output
# The output data is printed on the standard output (the console).

# The output consists of one line. You must print the kind of beverage you should drink, as well as the sum of digits that lead to that decision.
# Note: The beverage is always in plural, no matter the number before it.

# Constraints
# That number can consist of up to 18 digits.
# The digit zero (0) is considered to be even.
# Sample Tests
# Input
# 10
# Output
# 1 cups of coffee
# Explanation
# Odd digits: 1
# Even digits: 0
# Sum of odd digits = 1
# Sum of even digits = 0
# 1 > 0, so output "1 cups of coffee"
# Input
# 3621
# Output
# 8 energy drinks
# Explanation
# Odd digits: 3, 1
# Even digits: 6, 2
# Sum of odd digits = 4
# Sum of even digits = 8
# 8 > 4, so output "8 energy drinks"
# Input
# 363
# Output
# 6 of both
# Explanation
# Odd digits: 3, 3
# Even digits: 6
# Sum of odd digits = 6
# Sum of even digits = 6
# 6 = 6, so output "6 of both"