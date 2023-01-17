# 80 points in the Judge system

list_one = input().split(',')
list_two = input().split(',')

zipped = list(zip(list_one, list_two))

combined_list = ''

for index in zipped:
    combined_list += str(index)

numbers_list = list(range(1001))
final_list = ''

for num in numbers_list:
    final_list += str(num) + ','

result = ''

for element in combined_list:
    if element != "'" and element != ',' and element != ' ' and element != '"':
        if element in final_list:
            result += str(element) + ','
   
        
print(result.removesuffix(','))




# Write a program that reads two lists of numbers and combines them by alternatingly taking elements:

# combine 1,2,3 and 7,8,9 -> 1,7,2,8,3,9
# you can assume that the input lists will have the same length.
# Print the resulting combined list to the output, separating elements with a comma.

# Input
# On the first line you will receive the first list.
# On the second line -> 2nd list.


# Output
# On the only line of output, print all the numbers in format n1,n2,n3,..n
#   6,4,1,1,4,3 
#   2,1,4,4,1,2