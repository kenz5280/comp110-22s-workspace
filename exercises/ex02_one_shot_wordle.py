"""EX02 - One-Shot Wordle - Loops."""

__author__ = "730489406"

secret_word: str = "python"

guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# fix index_variable. doesn't work as is 
index_variable: int = int(str())

emoji_result: str = str()

while index_variable < len(secret_word):
    if guess[index_variable] == secret_word[index_variable]:
        emoji_result + GREEN_BOX
    else:
        emoji_result + WHITE_BOX
    index_variable = index_variable + 1

print(emoji_result)


    
