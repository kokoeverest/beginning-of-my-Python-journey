# unresolved: if number is negative the index takes only "-" symbol, and not the whole number "-1" (for example)

numbers = input().split(" ")


def even_numbers(n):

    for _ in n:
        if int(n) % 2 == 0:
            return True
        else:
            return False


evens = list(filter(even_numbers, numbers))
result = [int(i) for i in evens]

print(result)


# Write a program that receives a sequence of numbers (integers) separated by a single space. It should print a list
# of only the even numbers. Use filter().
