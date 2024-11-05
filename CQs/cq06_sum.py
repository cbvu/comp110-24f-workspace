"""summing the elements of a list using different loops"""

__author__ = "730579512"


def w_sum(vals: list[float]) -> float:
    index: int = 0
    sum: float = 0.0
    while index < len(vals):
        sum = sum + vals[index]
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for nums in vals:
        sum = sum + nums
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for nums in range(0, len(vals)):
        sum = sum + vals[nums]
    return sum
