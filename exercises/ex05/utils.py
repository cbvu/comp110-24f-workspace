__author__ = "730579512"
"""utils"""


def only_evens(input: list[int]) -> list:
    evlist: list[int] = []
    index: int = 0
    for num in input:
        if num % 2 == 0 or num % -2 == 0:
            evlist.append(num)
            index = index + 1
    return evlist


# returns list of only even terms in list


def sub(input: list[int], sind: int, eind: int) -> list[int]:
    sublist: list[int] = []
    if sind < 0:
        sind = 0
    if eind > len(input):
        eind = len(input)
    if len(input) == 0 or sind > len(input) or eind <= 0:
        return []
    for num in range(sind, eind):
        sublist.append(input[num])
    return sublist


# returns subset of terms between sind and eind in list


def add_at_index(inputl: list[int], numb: int, ind: int) -> None:
    if ind > len(inputl) or ind < 0:
        raise IndexError("Index is out of bounds for the input list")
    inputl.append(0)
    for tm in range(len(inputl) - 1, ind, -1):
        inputl[tm] = inputl[tm - 1]
    inputl[ind] = numb


# must start at last index and step backwards to shift everything right
# must put the index error part first so function ends if the list isn't the right type
# of input
