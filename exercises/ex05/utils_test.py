__author__ = "730579512"
"""util test"""

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


# only evens test
def test_only_evens() -> None:
    inputl: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(inputl) == [2, 4, 6]
    assert inputl == [2, 4, 6]


# in order to check on status of parameter after function is run call funct in test and
# then assert parameter = thing
def test_only_evens2() -> None:
    inputl: list[int] = [1, -2, 3, -4, 5, 6]
    assert only_evens(inputl) == [-2, -4, 6]


def test_only_evens3() -> None:
    input2: list[int] = [1, 5, 7]
    assert only_evens(input2) == []


def test_evonlist() -> None:
    evlist: list[int] = [2, 2, 4]
    assert only_evens(evlist) == [2, 2, 2]


# sub tests
def test_sfunct() -> None:
    input: list[int] = [1, 2, 3]
    assert sub(input, 0, 1) == [1]
    assert input == [1]


def test_sempty() -> None:
    binp: list[int] = []
    assert sub(binp, 0, 1) == []


def test_sneg() -> None:
    input: list[int] = [1, 2, 3]
    assert sub(input, -1, 3) == [1, 2, 3]


def test_semptyo() -> None:
    input: list[int] = [1, 2, 3]
    assert sub(input, 3, 3) == []


# tests for add at index
def test_addreg() -> None:
    input: list[int] = [1, 2, 3, 4]
    add_at_index(input, 5, 3)
    assert add_at_index(input, 5, 3)
    assert input == [1, 2, 3, 5, 4]


def test_addzero() -> None:
    sinp: list[int] = [1]
    add_at_index(sinp, 3, 0)
    assert sinp == [3, 1]


def test_addempty() -> None:
    input: list[int] = []
    add_at_index(input, 5, 0)
    assert input == [5]


def test_add_at_index_raises_indexerror():
    with pytest.raises(IndexError):
        input: list[int] = [1, 2, 3, 4]
        add_at_index(input, 5, 5)


def test_add_at_index_raises_indexerror_again():
    with pytest.raises(IndexError):
        input: list[int] = [1, 2, 3, 4]
        add_at_index(input, 5, -5)


# names of unit tests are kind of arbitrary they just have to start with test
