"""list utility"""

__author__: str = "730579512"


def all(input: list[int], gint: int) -> bool:
    index: int = 0
    if len(input) == 0:
        return False

    while index < len(input):
        if input[index] == gint:
            index = index + 1
            return True
        else:
            return False
    return False


# loop must contain return true and return false statements


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    index: int = 0
    max: int = input[index]
    while index < len(input) - 1:
        if max < input[index + 1]:
            max = input[index + 1]
        index += 1
    return max


# max needed since a variable is needed to represent the greatest number in the list so far
# max is compared to as the list is indexed


def is_equal(input: list[int], input2: list[int]) -> bool:
    if len(input) == len(input2):
        index: int = 0
        while index < len(input) - 1:
            if input[index] != input2[index]:
                return False
            else:
                index += 1
        return True
    else:
        return False


# most efficient way to compare two things is to write a return false statement first
# then write a set of operations to compare things


def extend(a: list[int], b: list[int]) -> None:
    index: int = 0
    while index < len(b):
        a.append(b[index])
        index += 1
    return None


# cannot add whole lists, must index through list and add indiv items
