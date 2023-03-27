def value_exists(inp_dict: dict[str,int], val: int) -> bool:
    for elem in inp_dict:
        if inp_dict[elem] == val:
            return True
    return False
    
print(value_exists({"a": 2, "b": 4, "c": 7, "d": 1}, 5))