"""Tests for linked list utils."""

# from sre_constants import SUCCESS
import pytest

from exercises.ex10.linked_list import Node, last, value_at, max, linkify, scale, is_equal

__author__ = "730489406"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise an value error."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return a reference to its last Node."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_0_index() -> None:
    """Tests value_at when index is 0."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 0) == 1


def test_value_at_index() -> None:
    """Test value_at when index is 3."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 1) == 2
    

def test_value_outside_index() -> None:
    """Tests value_at when given an index outside of linked node range."""
    linked_list = Node(1, Node(2, Node(3, None)))
    with pytest.raises(IndexError):
        value_at(linked_list, 5)


def test_max_normal() -> None:
    """Tests max when given a Node list."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert max(linked_list) == 30


def test_max_empty() -> None:
    """Tests max when given empty list."""
    with pytest.raises(ValueError):
        max(None)


def test_max_multi() -> None:
    """Tests max when given multiple Nodes w same data value."""
    linked_list = Node(10, Node(10, Node(10, None)))
    assert max(linked_list) == 10


def test_linkify_normal() -> None:
    """Tests linkify with normal items list."""
    assert is_equal(linkify([1, 2, 3]), Node(1, Node(2, Node(3, None))))


def test_linkify_empty() -> None:
    """Tests linkify with empty items list."""
    assert linkify([]) is None


def test_scale_normal() -> None:
    """Tests scale with normal conditions."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert scale(linked_list, 2) 


def test_scale_zero_scale() -> None:
    """Tests scale with scale value of 0."""
    assert is_equal(scale(linkify([1, 2, 3]), 0), Node(0, Node(0, Node(0, None))))


def test_scale_empty() -> None:
    """Tests scale when head is None."""
    assert scale(linkify([]), 2) is None