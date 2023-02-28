"""EX04 - 'list' Utility Functions"""

__author__ = "730564297"

def all (numbers: list[int], number: int) -> bool:
    idx: int = 0
    while len(numbers) > 0 and idx < len(numbers):
        if numbers[idx] == number:
            idx += 1
        else:
            return False
    return True

def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max: int = input[0]
    idx: int = 1
    while idx < len(input):
        if input[idx] > max:
            max = input[idx]
        idx += 1
    return max

def is_equal(list1: list[int], list2: list[int]) -> bool:
    idx: int = 0
    while len(list1) == len(list2) and idx < len(list1):
        if list1[idx] == list2[idx]:
            idx += 1
        else:
            return False
    return True