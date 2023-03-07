"""EX04 - 'list' Utility Functions."""

__author__ = "730564297"


def all(numbers: list[int], number: int) -> bool:
    """Check if a given number is equal to every integer in a list."""
    if len(numbers) == 0:  # return False if the list is empty
        return False
    idx: int = 0
    while idx < len(numbers):  
        if numbers[idx] == number:
            # If the number matches the first index, check next
            idx += 1
        else:
            return False  # If doesn't match, return False
    return True  # If the number equals to every integer in a given list, return True


def max(input: list[int]) -> int:
    """Find the largest integer in a givenlist."""
    if len(input) == 0:  # return error message if the list is empty
        raise ValueError("max() arg is an empty List")
    max: int = input[0]  # set the first index as max
    idx: int = 1
    while idx < len(input):
        if input[idx] > max:  # if the next index is larger than max, replace max with it
            max = input[idx]
        idx += 1  # check the next index
    return max  # return the largest number


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Check if the objects in two lists match."""
    if len(list1) == 0 and len(list2) == 0:  # if both are empty, return True
        return True
    if len(list1) != len(list2) or len(list1) == 0 or len(list2) == 0:  # check if the lengths of the two lists are equal and one of them is not empty
        return False
    idx: int = 0
    while idx < len(list1):  
        if list1[idx] == list2[idx]:
            # if the object at a certain index matches, compare that of the next index
            idx += 1
        else:
            return False  # if doesn't match, return False
    return True  # if they all match, return True