"""EX07 - Dictionary Functions."""

__author__ = "730564297"


def invert(inp: dict[str, str]) -> dict[str, str]:
    """Invert the key and value in a dictionary."""
    new: dict[str, str] = {}
    for key in inp:
        if inp[key] in new:
            raise KeyError("Duplicated values found in input dictionary.")
        new[inp[key]] = key
    return new
    

def favorite_color(inp: dict[str, str]) -> str:
    """Return the color that appears most frequently."""
    color: dict[str, int] = {}
    for key in inp:
        if inp[key] in color:
            color[inp[key]] += 1
        else:
            color[inp[key]] = 1
        
    favorite: str = ""
    count: int = 0
    for new_key in color:
        if color[new_key] > count:
            count = color[new_key]
            favorite = new_key
    return favorite


def count(inp: list[str]) -> dict[str, int]:
    """Return a dictionary that counts the number of the items in the list."""
    new: dict[str, int] = {}
    for item in inp:
        if item in new:
            new[item] += 1
        else:
            new[item] = 1
    return new
