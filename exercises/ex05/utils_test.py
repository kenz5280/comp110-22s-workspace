"""A space to test utils function."""

__author__: str = "730489406"

# For each function (only_evens, sub, concat) you are to
# define at least 3x unit test functions: 
# one edge case, two use cases

from utils import only_evens, sub, concat


def test_only_evens_normal() -> None:
    """A test for normal circumstances."""
    assert only_evens([1, 2, 3]) == [2]


def test_only_evens_none() -> None:
    """A test for no evens."""
    assert only_evens([1, 3, 5]) == []


def test_only_evens_all() -> None:
    """A test for all evens."""
    assert only_evens([4, 4, 4]) == [4, 4, 4]


def test_sub_negative_start() -> None:
    """A test for a negative start index."""
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, -2, 3) == [10, 20, 30]


def test_sub_over_end() -> None:
    """A test for a over list length end index."""
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, 1, 5) == [20, 30, 40]


def test_sub_normal() -> None:
    """A test for normal circumstances.""" 
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, 1, 3) == [20, 30]


def test_sub_empty() -> None: 
    """A test for an empty list."""
    a_list: list[int] = []
    assert sub(a_list, 1, 3) == []


def test_sub_over_start() -> None:
    """A test for an over start index."""
    a_list: list[int] = [10, 20, 30]
    assert sub(a_list, 4, 6) == []


def test_sub_negative_end() -> None:
    """A test for a negative end case."""
    a_list: list[int] = [10, 20, 30]
    assert sub(a_list, -3, -1) == []

 
def test_concat_normal() -> None:
    """A test for normal circumstances."""
    a_list: list[int] = [10, 20, 30]
    b_list: list[int] = [2, 3, 4]
    assert concat(a_list, b_list) == [10, 20, 30, 2, 3, 4]


def test_concat_empty() -> None:
    """A test for one empty list."""
    a_list: list[int] = []
    b_list: list[int] = [1, 2]
    assert concat(a_list, b_list) == [1, 2]


def test_concat_total_empty() -> None: 
    """A test for both empty lists."""
    a_list: list[int] = []
    b_list: list[int] = []
    assert concat(a_list, b_list) == []


def test_concat_repeat() -> None:
    """A test for repeated values in both lists."""
    a_list: list[int] = [0, 1, 2]
    b_list: list[int] = [0, 1, 2, 3]
    assert concat(a_list, b_list) == [0, 1, 2, 0, 1, 2, 3]