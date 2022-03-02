"""EX06 - Dictionary Functions."""

__author__: str = "730489406"


def invert(xs: dict[str, str]) -> dict[str, str]:
    """A function that invert given keys and values."""
    inversion: dict[str, str] = {}
    check: list[str] = list()
    for key in xs:
        if xs[key] in check:
            raise KeyError("Key Error")
        else:
            check.append(xs[key])
    for key in xs:
        value: str = xs[key]
        inversion[value] = key
    return inversion


def favorite_color(a_dict: dict[str, str]) -> str:
    """A function that returns the most popular color."""
    fav_color_count: dict[str, int] = {}
    for name in a_dict:
        if a_dict[name] in fav_color_count:
            fav_color_count[a_dict[name]] += 1
        else:
            fav_color_count[a_dict[name]] = 1
    max_count: int = 0
    max_color: str = ""
    for color in fav_color_count:
        if fav_color_count[color] > max_count:
            max_color = color
            max_count = fav_color_count[color]
    return max_color 


def count(ys: list[str]) -> dict[str, int]:
    """A function that gives a count of number of times a list value occurs."""
    result: dict[str, int] = {}
    for item in ys:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
