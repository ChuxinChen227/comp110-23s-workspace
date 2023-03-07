"""EX05 - 'list' Utility Functions."""

__author__ = "730564297"

def only_evens(mix: list[int]) -> list:
    """Return a new list that only contains even elements"""
    even: list[int] = list()
    for numbers in mix:
        if numbers % 2 == 0:
            even.append(numbers)
    return even

def concat(list1: list[int], list2: list[int]) -> list:
    """Generate a new list that contains all elements in both lists"""
    all: list[int] = list1
    for elements in list2:
        all.append(elements)
    return all

def sub(input: list[int], start_idx: int, end_idx: int) -> list:
    """Generate a subset of the given list, between the specified start index and the end index - 1."""
    new: list[int] = list()
    if start_idx < 0:
        start_idx = 0
    if end_idx > len(input):
        end_idx = len(input)
    if len(input) == 0 or start_idx >= len(input) or end_idx <= 0:
        return new
    for idx in range (start_idx, end_idx):
        new.append(input[idx])
    return new