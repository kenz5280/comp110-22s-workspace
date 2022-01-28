"""EX02 - One-Shot Wordle - Loops."""

__author__ = "730489406"

secret_word: str = "python"

guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index_variable: int = 0

emoji_result: str = ""


while index_variable < len(secret_word) and len(guess) == len(secret_word):
    if guess[index_variable] == secret_word[index_variable]:
        emoji_result = emoji_result + GREEN_BOX

    else:
        elsewhere_character: bool = False 
        secret_index_variable: int = 0
        while secret_index_variable < len(secret_word) and not elsewhere_character:
            if guess[index_variable] == secret_word[secret_index_variable]:
                elsewhere_character = True
            secret_index_variable = secret_index_variable + 1
        if elsewhere_character:
            emoji_result = emoji_result + YELLOW_BOX
        else:
            emoji_result = emoji_result + WHITE_BOX
    index_variable = index_variable + 1

# make variables defined close to where you need them
# edit to make prettier w/ concepts from 1/27 lecture

print(emoji_result)

while len(guess) != len(secret_word):
    guess = input(f"That was not {len(secret_word)} letters! Try again: ")

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")



    
