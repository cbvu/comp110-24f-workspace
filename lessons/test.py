class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Line:
    start: Point
    end: Point

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def get_length(self) -> float:
        xlen: float = self.end.x - self.start.x
        ylen: float = self.end.y - self.start.y
        return ((xlen**2) + (ylen**2)) ** 0.5

    def get_slope(self) -> float:
        xlen: float = self.end.x - self.start.x
        ylen: float = self.end.y - self.start.y
        return ylen / xlen


p1 = Point(1, 2)
p2 = Point(4, 6)
self = Line(p1, p2)

length = self.get_length()
slope = self.get_slope()

print(length)
print(slope)
