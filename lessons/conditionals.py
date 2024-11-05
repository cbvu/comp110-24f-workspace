"""practice with conditionals"""


def less_than_10(num: int) -> bool:
    """tell me if number is less than ten"""
    if num < 10:
        print(True)
    else:
        print(False)


print(less_than_10(num=5))


def nom(hungry: bool) -> bool:
    if hungry:
        print("eat")
    else:
        print("go sleep")


nom(hungry=False)


def check_first_letter(word: str, letter: str) -> str:
    if (word[0]) == letter:
        print("match!")
    else:
        print("no match!")


check_first_letter(word="fish", letter="g")
