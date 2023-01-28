number = input()


def odd_even_sum(num):
    evens_sum = 0
    odds_sum = 0
    for n in num:
        if int(n) % 2 == 0:
            evens_sum += int(n)
        else:
            odds_sum += int(n)

    return f"Odd sum = {odds_sum}, Even sum = {evens_sum}"


print(odd_even_sum(number))

# You will receive a single number. You should write a function that returns the sum of all even and all odd digits
# in a given number. The result should be returned as a single string in the format:
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
# Print the result of the function on the console.
