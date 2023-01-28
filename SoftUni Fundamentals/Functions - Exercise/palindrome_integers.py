integers = input().split(", ")


def palindrome(par1):
    result = []
    for i in par1:
        current_number = [list(i)]
        reversed_number = [list(reversed(i))]
        if current_number == reversed_number:
            result.append("True")
        else:
            result.append("False")

    return result


final_result = palindrome(integers)

for elem in final_result:
    print(elem)

# A palindrome is a number that reads the same backward as forward, such as 323 or 1001. Write a function that receives
# a list of positive integers, separated by comma and space ", ". The function should check if each integer is a
# palindrome - True or False. Print the result.
