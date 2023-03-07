"""Example function for unit tests"""

def sum(xs: list[float]) -> float:
    """return sum of all elements"""
    sum_total: float = 0.0
    for idx in range (0,len(xs)):
        sum_total += xs[idx]
    return sum_total