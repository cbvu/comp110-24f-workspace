from CQs.cq09.point import Point

__author__ = "730579512"
"""checking scale function"""


def test_nomutscale() -> None:
    m: Point = Point(2.0, 3.0)
    m.scale(3)
    assert m.x == 2.0 and m.y == 3.0


# have to use object.funct to test out functions
# that correspond to objects
