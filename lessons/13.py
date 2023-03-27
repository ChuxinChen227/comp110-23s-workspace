def create() -> list[int]:
    list_1: list[int] = []
    i: int = 0
    while i < 3:
        list_1.append(i)
        i += 1
    return list_1


def increase(a_list: list[int], x: int) -> None:
    i: int = 0
    while i < len(a_list):
        a_list[i] += x
        i += 1
    return None


def main() -> None:
    list_1: list[int] = create()
    list_2: list[int] = list_1
    list_1 = create()
    increase(list_1, 2)

    print(list_1)
    print(list_2)


if __name__ == "__main__":
    main()

def remove_first(xs: list[int]):
    xs.pop(0)

course: list[str] = ["comp", "110"]
print(remove_first(course))

def dup(xs: list[int]):
    start_len: int = len(xs)
    i: int = 0
    while i <= start_len - 1:
        xs.append(xs[i])
        i += 1

groceries: list[str] = ["apples", "eggs"]
print(dup(groceries))
print(groceries)

def odds_list(min: int, max: int) -> list[int]:
    odds: list[int] = list()
    x: int = min
    while x <= max:
        if x % 2 == 1:
            odds.append(x)
        x += 1
    return odds

global_odds: list[int] = odds_list(2,10)
print(global_odds)