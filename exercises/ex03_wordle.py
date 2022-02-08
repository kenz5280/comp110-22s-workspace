"""A complete wordle program using definitons."""

___author___: str = "730489406"


def contains_char(guess: str, single_chr: str) -> bool:
    """Finds match between single character and character in larger string."""
    assert len(single_chr) == 1
    i: int = 0 
    match: bool = False
    while i < len(guess):
        if guess[i] == single_chr:
            match = True
        else:
            not match
        i += 1
    if match:
        return True
    else:
        return False


def emojified(guess: str, secret: str) -> str:
    """Determines colored emoji from contains char function."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji_string: str = ""
    index: int = 0
    while index < len(guess):
        if guess[index] == secret[index]:
            emoji_string += GREEN_BOX
        else:
            if contains_char(secret, guess[index]):
                emoji_string += YELLOW_BOX
            else: 
                emoji_string += WHITE_BOX
        index += 1
    return emoji_string 


def input_guess(expected_length: int) -> str:
    """Asserts that the guess is the correct length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while expected_length != len(guess):
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turn_number: int = 1
    while turn_number <= 6:
        print(f"=== Turn {turn_number}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn_number}/6 turns!")
            turn_number = 7
        else:
            turn_number += 1
    print("X/6 - Sorry, try again tomorrow!")
