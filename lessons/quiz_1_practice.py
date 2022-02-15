"""Working through quiz 01 problem."""


def rerun(word: str, n: int) -> str:
    """A repetition of characters."""
    char_rerun: int = 0
    i: int = 0
    char_string: str = ""
    while i < len(word):
        while char_rerun < n:
            char_string += word[i]
            n += 1
        i += 1
    return char_string