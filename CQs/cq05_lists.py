"""mutating functions"""

__author__ = "730579512"


def manual_append(a: list[int], num: int) -> None:
    a.append(num)
    return None


def double(b: list[int]) -> None:
    index: int = 0
    while index < len(b):
        b[index] = 2 * b[index]
        index = index + 1
    return None


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)
print(list_1)
print(list_2)
