def get_first(input: list[str]) -> str:
    return input[0]


def remove_first(input: list[str]) -> None:
    input.pop(0)
    return None


def get_and_remove_first(input: list[str]) -> list:
    input.pop(0)
    return input
