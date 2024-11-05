__author__ = "730579512"


def find_and_remove_max(input: list[int]) -> int:
    index: int = 0
    if len(input) == 0:
        return -1

    cmax: int = input[0]
    if len(input) >= 1:
        for num in input:
            if num > cmax:
                cmax = num

        while index < len(input):
            if input[index] == cmax:
                input.pop(index)
            else:
                index += 1

    return cmax
