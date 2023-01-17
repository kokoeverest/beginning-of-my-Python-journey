number = int(input())

positives = []
negatives = []
count_positives = 0
sum_negatives = 0

for i in range(number):
    num = int(input())
    if num >= 0:
        count_positives += 1
        positives.append(num)
    else:
        sum_negatives += num
        negatives.append(num)
print(positives)
print(negatives)
print(f'Count of positives: {count_positives}')
print(f'Sum of negatives: {sum_negatives}')

# On the first line, you will receive a number n. On the following n lines, you will receive integers.
# You should create and print two lists:
#     • One with all the positives (including 0) numbers
#     • One with all the negatives numbers
# Finally, print the following message:
# "Count of positives: {count_positives}
# Sum of negatives: {sum_of_negatives}"