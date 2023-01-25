
cards = input().split(' ')
shuffles = int(input())
list_1 = []
list_2 = []

for shuffle in range(shuffles):
    list_1 = cards[0:int(len(cards)/2)]
    list_2 = cards[int(len(cards)/2):]
    new_list = list(zip(list_1, list_2))
    cards.clear()
    for i, k in new_list:
        cards.append(i)
        cards.append(k)
print(cards)

# A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half.
# Then the cards in the two halves are perfectly interleaved, such that the original bottom card is still on the
# bottom and the original top card is still on top.
# For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once, gives
# ['ace', 'four', 'two', 'five', 'three', 'six']
# Write a program that receives a single string (cards separated by space) and on the second line receives a
# count of faro shuffles that should be made. Print the state of the deck after the shuffle.
# Note: The length of the deck of cards will always be an even number.
