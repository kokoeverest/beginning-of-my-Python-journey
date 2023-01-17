sign = input()

card_faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
card_suits = ['spades,', 'clubs,', 'hearts,', 'diamonds']

while True:
    
    for c in card_faces:
        print()
        for f in card_suits:
            print(f'{c} of {f}', end=(' '))
        if sign == c:
            break
    break
# Description

# Write a program that reads a card sign(as a string) from the console and generates and prints /
# all possible cards from a standard deck of 52 cards up to the card with the given sign(without the jokers)./
#  The cards should be printed using the classical notation (like 5 of spades, A of hearts, 9 of clubs;/
#  and K of diamonds).

#     The card faces should start from 2 to A(10 is 10).
#     Print each card face in its four possible suits: clubs, diamonds, hearts and spades.

# Input

#     On the only line, you will receive the sign of the card to which, including, you should print the /
# cards in the deck.

# Output

#     The output should follow the format bellow(assume our input is 5): 