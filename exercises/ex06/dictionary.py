__author__ = "730579512"
"""dictionary utility functs"""


def invert(dic1: dict[str, str]) -> dict[str, str]:
    ndic: dict[str, str] = {}
    for idx in dic1:
        if dic1[idx] in ndic:
            raise KeyError("key already in dictionary")
        else:
            ndic[dic1[idx]] = idx

    return ndic


# must raise a key error for duplicate values bc inverted list cant have duplicate keys


def favorite_color(cdic: dict[str, str]) -> str:
    cntdic: dict[str, int] = {}
    for p in cdic:
        if cdic[p] in cntdic:
            cntdic[cdic[p]] += 1
        else:
            cntdic[cdic[p]] = 1
    max: int = 0
    fcolor: str = ""
    for color in cntdic:
        if cntdic[color] > max:
            max = cntdic[color]
            fcolor = color
        if cntdic[color] == max and fcolor != color:
            return fcolor
    return fcolor


# function put colors in dictionary with how many times they appeared in og dic
# second for loop compares the values to find max
# in order to find string that appears most times you need two variables to keep track
# of
# one to represent the max and then one as a placeholder to keep track of the string
# assoc with the current max


def count(clist: list[str]) -> dict[str, int]:
    ctdic: dict[str, int] = {}
    for val in clist:
        if val in ctdic:
            ctdic[val] += 1
        else:
            ctdic[val] = 1
    return ctdic


# same concenptually as the last one


def alphabetizer(alist: list[str]) -> dict[str, list[str]]:
    adic: dict[str, list[str]] = {}
    for wd in alist:
        if wd[0] in adic:
            adic[wd[0]].append(wd)
        else:
            adic[wd[0]] = [wd]
    return adic


# append list in dict with dict[key].append(thingyoureappendingwith)


def update_attendance(datt: dict[str, list[str]], dow: str, stud: str) -> None:
    if dow in datt:
        return
    else:
        datt[dow] = []
        if stud in datt[dow]:
            return
        else:
            datt[dow].append(stud)
    return None


# to stop function from running if stuff is improper just put return under if
# need to initialize list if there's a new key by setting it equal to empty list
# before adding stuff to it
