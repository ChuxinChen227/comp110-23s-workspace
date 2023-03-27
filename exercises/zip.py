"""CQ 04 - Dict Function Writing."""

def zip(keys: list[str], values: list[int]) -> dict:
    new: dict[str,int] = dict()
    if len(keys) != len(values) or len(keys) == 0 or len(values) == 0:
        return new
    for idx in range(0, len(keys)):
        new[keys[idx]] = values[idx]
    return new