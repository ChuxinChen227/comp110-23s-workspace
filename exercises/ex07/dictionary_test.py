"""Unit test for dictionary functions."""

__author__ = "730564297"

from exercises.ex07.dictionary import invert, favorite_color, count
import pytest

def test_invert_duplicated_value() -> None:
    """Test invert function with an input dictionary that has duplicate values."""
    with pytest.raises(KeyError):
        input_dict = {'kris': 'jordan', 'michael': 'jordan'}
        invert(input_dict)


def test_invert_normal() -> None:
    """Test invert function with a normal input dictionary."""
    test_dict = {'a': 'z', 'b' : 'y', 'c': 'x'}
    assert invert(test_dict) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_single_key_value() -> None:
    """Test invert function with an input dictionary that has only one key-value pair."""
    test_dict = {'apple': 'cat'}
    assert invert(test_dict) == {'cat': 'apple'}


def test_favorite_color_single_color() -> None:
    """Test that the function returns the only color in the dictionary."""
    assert favorite_color({"Marc": "yellow"}) == "yellow"


def test_favorite_color_tie() -> None:
    """Test that the function returns the color that appeared first in the dictionary in case of a tie."""
    assert favorite_color({"Marc": "blue", "Ezri": "yellow", "Kate": "yellow", "Kris": "blue"}) == "blue"


def test_favorite_color_first_in_dict() -> None:
    """Test that the function returns the color that appeared most frequently in the dictionary."""
    assert favorite_color({"Marc": "blue", "Ezri": "yellow", "Kris": "yellow"}) == "yellow"


def test_count_empty() -> None:
    """Test count with an empty list."""
    assert count([]) == {}


def test_count_single() -> None:
    """Test count with a list containing a single item."""
    assert count(["apple"]) == {"apple": 1}


def test_count_multiple() -> None:
    """Test count with a list containing multiple items."""
    assert count(["milk", "bread", "apple", "bread", "milk", "milk"]) == {"bread": 2, "milk": 3, "apple": 1}