"""Examples of importing in python."""

from lessons import helpers

# Alias a module / imported name as another name
from lessons import helpers as hp

# import names defined globally in a module
from lessons.helpers import powerful, THE_ANSWER


def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))
    print(f"The answer: {hp.THE_ANSWER}")
    print(powerful(2, 4))
    print(THE_ANSWER)


# Idiom for making a module able to run as a program
# or have its global definitions imported elsewhere.
if __name__ == "__main__":
    main()
else:
    print(f"helpers.py was imported: {__name__}")