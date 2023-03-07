"""Unit tests for 'list' Utility Functions."""

__author__ = "730564297"

from exercises.ex05.utils import only_evens, sub, concat

def test_onlyeven_empty() -> None:
    """Test only_evens function with empty list"""
    assert only_evens([]) == []

def test_onlyeven_many() -> None:
    """Test only_evens function with many elements"""
    test_list: list[int] = [1, 2, 3]
    assert only_evens(test_list) == [2]

def test_onlyeven_many_with_negatives() -> None:
    """Test only_evens function with negative elements"""
    test_list: list[int] = [1, -2, -4]
    assert only_evens(test_list) == [-2, -4]

def test_concat_empty() -> None:
    """Test concat function with empty lists"""
    assert concat([], []) == []

def test_concat_one_empty_list() -> None:
    """Test concat function with one empty list"""
    test_list1: list[int] = []
    test_list2: list[int] = [1, 2, 3]
    assert concat(test_list1, test_list2) == [1, 2, 3]

def test_concat_non_empty_lists() -> None:
    """Test concat function with two non_empty lists"""
    test_list1: list[int] = [1, 3, 7]
    test_list2: list[int] = [0, 2, 9]
    assert concat(test_list1, test_list2) == [1, 3, 7, 0, 2, 9]

def test_sub_empty() -> None:
    """Test sub function with empty list"""
    assert sub([], 0, 3) == []

def test_sub_out_of_range() -> None:
    """Test sub function with out-of-range index"""
    test_list: list[int] = [1, 2, 3]
    assert sub(test_list, 3, 5) == []

def test_sub_valid_input() -> None:
    """Test sub function with valid inputs"""
    test_list: list[int] = [1, -3, 6, 11, 5]
    assert sub(test_list, 1, 4) == [-3, 6, 11]