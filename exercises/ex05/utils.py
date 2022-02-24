"""A space to implement functions for ex05."""

__author__: str = "730489406"


def only_evens(xs: list[int]) -> list[int]:
    """A function that returns the even integers of a list."""
    i: int = 0
    evens: list[int] = []
    while i < len(xs):
        if xs[i] % 2 == 0:
            evens.append(xs[i])
        i += 1
    return evens


def sub(ys: list[int], start_index: int, end_index: int) -> list[int]:
    """A function that lists integers in a given range of indeces."""
    i: int = 0
    add_list: list[int] = []
    while i < end_index and i < len(ys):
        if i >= start_index:
            add_list.append(ys[i])
        i += 1
    return add_list


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """A function that returns a list of both given lists."""
    total_list: list[int] = []
    i: int = 0
    x: int = 0
    while i < len(xs):
        total_list.append(xs[i])
        i += 1
    while x < len(ys):
        total_list.append(ys[x])
        x += 1
    return total_list
