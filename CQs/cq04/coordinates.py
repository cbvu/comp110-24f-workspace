"""coordinates function"""

__author__ = "730579512"


def get_coords(xs: str, ys: str) -> None:
    c: int = 0
    while c < len(xs):
        c2: int = 0
        while c2 < len(ys):
            print("(" + xs[c] + "," + ys[c2] + ")")
            c2 += 1
        c += 1
