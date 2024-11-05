"""while loops challenge question"""

__author__ = "730579512"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0

    while index < len(phrase):
        if search_char == phrase[index]:
            count = count + 1

        index = index + 1
    return count
