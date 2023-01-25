text = input().split(' ')

result = []

for number in text:
    if int(number) <= 0:
        result.append(abs(int(number)))
    else:
        result.append(-abs(int(number)))

print(result)


# my first solution, before discovering the -abs() function!!!
#     else:
#         result.append("-" + number)
#
# # final_result = []
# #
# # for element in result:
# #     final_result.append(int(element))
# #
# # print(final_result)
# Write a program that receives a single string containing positive and negative numbers separated by a single space.
# Print a list containing the opposite of each number.