"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730489406"

word_guess: str = input("Enter a 5-character word: ")

if len(word_guess) != 5:
    print("Error: Word must contain 5 letters.")
    exit()

single_character: str = input("Enter a single character: ")

if len(single_character) != 1:
    print("Error: Character must be a single character. ")
    exit()

print("Searching for " + single_character + " in " + word_guess)

if single_character == word_guess[0]:
    print(single_character + " found at index 0")
    character_count_0 = 1
else:
    character_count_0 = 0

if single_character == word_guess[1]:
    print(single_character + " found at index 1")
    character_count_1 = 1
else:
    character_count_1 = 0

if single_character == word_guess[2]:
    print(single_character + " found at index 2")
    character_count_2 = 1
else: 
    character_count_2 = 0

if single_character == word_guess[3]:
    print(single_character + " found at index 3")
    character_count_3 = 1
else:
    character_count_3 = 0

if single_character == word_guess[4]:
    print(single_character + " found at index 4")
    character_count_4 = 1
else:
    character_count_4 = 0

character_full_count = character_count_0 + character_count_1 + character_count_2 + character_count_3 + character_count_4

if character_full_count == 0:
    print("No instances of " + single_character + " found in " + word_guess)

if character_full_count == 1:
    print(str(character_full_count) + " instance of " + single_character + " found in " + word_guess)

if character_full_count > 1:
    print(str(character_full_count) + " instances of " + single_character + " found in " + word_guess)

# can make this nested to make it neater. try this at a later time