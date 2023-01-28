def validator(par):
    invalid_symbols = ""
    invalid_length = ""
    invalid_digits = ""
    digits = 0
    letters = 0
    length_valid_symbols = 0
    for i in par:
        length_valid_symbols += 1
        if ord(i) in range(48, 58):
            digits += 1
        elif ord(i) in range(97, 123):
            letters += 1
        elif ord(i) in range(65, 91):
            letters += 1
        else:
            invalid_symbols = "Password must consist only of letters and digits"

    if not 6 <= length_valid_symbols <= 10:
        invalid_length = "Password must be between 6 and 10 characters"

    if digits < 2:
        invalid_digits = "Password must have at least 2 digits"

    if invalid_length == "" and invalid_symbols == "" and invalid_digits == "":
        return "Password is valid"
    else:
        return f"{invalid_length}\
               \n{invalid_symbols}\
               \n{invalid_digits}"


password = input()
print(validator(password))

# Write a function that checks if a given password is valid. Password validations are:
#     • It should be 6 - 10 (inclusive) characters long
#     • It should consist only of letters and digits
#     • It should have at least 2 digits
# If a password is valid, print "Password is valid".
# Otherwise, for every unfulfilled rule, print a message:
#     • "Password must be between 6 and 10 characters"
#     • "Password must consist only of letters and digits"
#     • "Password must have at least 2 digits"
