sequence = input().split(" ")


def sorted_sequence(seq):
    sorted_seq = []
    for i in seq:
        sorted_seq.append(int(i))

    return sorted(sorted_seq)


print(sorted_sequence(sequence))

# Write a program that receives a sequence of numbers (integers) separated by a single space. It should print a
# sorted list of numbers in ascending order. Use sorted().
