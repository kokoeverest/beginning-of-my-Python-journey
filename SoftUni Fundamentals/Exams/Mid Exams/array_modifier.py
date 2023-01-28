array_values = input().split(' ')
result = []
while True:
    command = input().split(' ')

    result_multiply = 0

    if command == ["end"]:
        break
    elif command == ["decrease"]:
        for i in array_values:
            result.append(int(i) - 1)
    else:
        index_1 = int(command[1])
        index_2 = int(command[2])
        if command[0] == "swap":
            array_values[index_1], array_values[index_2] = array_values[index_2], array_values[index_1]
        elif command[0] == "multiply":
            result_multiply += int(array_values[index_1]) * int(array_values[index_2])
            array_values.pop(index_1)
            array_values.insert(index_1, str(result_multiply))

final_result = ""
for i in result:
    final_result += (str(i) + ", ")

print(final_result[:-2])

'''
You are given an array with integers. Write a program to modify the elements after receiving the following commands:
    • "swap {index1} {index2}" takes two elements and swap their places.
    • "multiply {index1} {index2}" takes element at the 1st index and multiply it with the element at 2nd index.
     Save the product at the 1st index.
    • "decrease" decreases all elements in the array with 1.
Input
On the first input line, you will be given the initial array values separated by a single space.
On the next lines you will receive commands until you receive the command "end". The commands are as follow:
    • "swap {index1} {index2}"
    • "multiply {index1} {index2}"
    • "decrease"
Output
The output should be printed on the console and consist of elements of the modified array – separated by a comma
and a single space ", ".
Constraints
    • Elements of the array will be integer numbers in the range [-231...231]
    • Count of the array elements will be in the range [2...100]
    • Indexes will be always in the range of the array

    '''