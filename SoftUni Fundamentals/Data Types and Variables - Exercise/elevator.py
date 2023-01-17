people = int(input())
capacity = int(input())

result = people // capacity
remaining_people = people % capacity

if 0 < remaining_people < capacity:
    result += 1

print(result)

# Calculate how many courses will be needed to elevate N persons by using an elevator with a capacity of P persons.
# The input holds two lines: the number of people N and the capacity P of the elevator.
# Examples
# Input # Output# Comments
# 17
# 3         6       5 courses * 3 people + 1 course * 2 persons
# 4
# 5
# 1
# All the persons fit inside the elevator.
# Only one course is needed.
# 10
# 5
# 2
# 2 courses * 5 people
