# membership operators = used to test weather a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word:  # if we use not in then the statements are switched
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")