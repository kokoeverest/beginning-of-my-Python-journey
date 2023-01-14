user_input = input()
letters = user_input.lower()
count = 0
string = ''

for letter in letters:
    string += letter
    if 'water' in string:
        count += 1
        string = ''

string = ''

for letter in letters:
    string += letter
    if 'sand' in string:
        count += 1
        string = ''

string = ''

for letter in letters:
    string += letter
    if 'fish' in string:
        count += 1
        string = ''
string = ''
for letter in letters:
    string += letter
    if 'sun' in string:
        count += 1
        string = ''
print(count)

# Beaches are filled with sand, water, fish, and sun. Given a string, calculate how many times the words
# "Sand", "Water", "Fish", and "Sun" appear (case insensitive).