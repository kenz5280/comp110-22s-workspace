"""Tests for EX06 - Dictionary Functions."""

__author__: str = "730489406"

from dictionary import invert, favorite_color, count
import pytest
# says to import pytest but from where?


def test_invert_normal_single() -> None:
    """Tests invert with single entry in dictionary."""
    assert invert({"key": "lock"}) == {"lock": "key"}


def test_invert_normal_multiple() -> None:
    """Tests invert with multiple entries in dictionary."""
    assert invert({"dog": "cat", "rain": "sun", "dark": "light"}) == {"cat": "dog", "sun": "rain", "light": "dark"}


def test_invert_no_string() -> None:
    """Tests invert with empty string arguments."""
    assert invert({"": "ball"}) == {"ball": ""}


def test_invert_key_error() -> None:
    """Tests invert when there is a key error."""
    with pytest.raises(KeyError):
        a_dict = {"red": "black", "blue": "black"}
        invert(a_dict)


def test_favorite_color_normal() -> None:
    """Tests favorite_color under normal circumstances."""
    a_dict: dict[str, str] = {"Kenzie": "yellow", "Eli": "green", "Kenna": "green"}
    assert favorite_color(a_dict) == "green"  


def test_favorite_color_no_fav() -> None:
    """Tests favorite_color when there is no favored color; gives first color in dictionary."""
    a_dict: dict[str, str] = {"Kenzie": "yellow", "Eli": "green", "Kenna": "purple"}
    assert favorite_color(a_dict) == "yellow"


def test_favorite_color_multiple_ties() -> None:
    """Tests favorite_color when there is multiple ties; gives first color tie listed."""
    a_dict: dict[str, str] = {"Kenzie": "yellow", "Eli": "green", "Kenna": "purple", "Kyle": "yellow", "Kip": "purple"}
    assert favorite_color(a_dict) == "yellow"


def test_favorite_color_empty() -> None:
    """Tests favorite_clor when argument is empty dictionary."""
    a_dict: dict[str, str] = {}
    assert favorite_color(a_dict) == ""


def test_count_normal() -> None:
    """Tests count under normal circumstances."""
    a_list: list[str] = ["red", "red", "blue", "green"]
    count(a_list) == {"red": 2, "blue": 1, "green": 1}


def test_count_all_green() -> None:
    """Tests count when given list of all green."""
    g_list: list[str] = ["green", "green", "green"]
    assert count(g_list) == {"green": 3}


def test_count_empty() -> None:
    """Tests count when given empty list."""
    a_list: list[str] = []
    assert count(a_list) == {}
