__author__: str = "730579512"

from CQs.cq07.find_max import find_and_remove_max


def test_routput() -> None:
    tlist: list[int] = [1, 3, 4, 4, 2]
    assert find_and_remove_max(tlist) == 4


def test_mutlist() -> None:
    tlist: list[int] = [1, 3, 4, 4, 2]
    find_and_remove_max(tlist)
    assert tlist == [1, 3, 2]


def test_allmax() -> None:
    tlist: list[int] = [4, 4, 4, 4]
    find_and_remove_max(tlist)
    assert tlist == []


def test_empty() -> None:
    blist: list[int] = []
    assert find_and_remove_max([]) == -1
    assert blist == []
