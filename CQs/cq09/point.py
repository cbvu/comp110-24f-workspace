from __future__ import annotations

# must be on line one of any program that returns its own type
__author__ = "730579512"
"""oop"""


class Point:
    x: float
    y: float

    def __init__(self, x_int: float, y_int: float):
        self.x = x_int
        self.y = y_int

    def scale_by(self: Point, factor: int) -> None:
        self.x = self.x * factor
        self.y = self.y * factor

    # have to modify x and y in terms of self
    def scale(self: Point, factor: int) -> Point:
        return Point(self.x * factor, self.y * factor)


# can do operations within
# a function call
