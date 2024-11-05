"""wordle"""

__author__: str = "730579512"


def input_word(length: int) -> str:
    gword: str = input("Enter a 5 letter word: ")
    while len(gword) != length:
        print(f"That wasn't {length} chars! Try again: {gword}")
    if len(gword) == length:
        print(gword)
    return gword


def contains_char(sword: str, char: str) -> bool:
    """searching word for char to see if it's there or not"""
    assert len(char) == 1
    index: int = 0
    while len(sword) > index:
        if char == sword[index]:
            return True
        index = index + 1
    return False


def emojified(gword: str, sword: str) -> str:
    assert len(gword) == len(sword)
    index: int = 0
    emojis: str = ""

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while index < len(sword):
        char = gword[index]
        if gword[index] == sword[index]:
            emojis += GREEN_BOX
        elif contains_char(sword, char):
            emojis += YELLOW_BOX
        else:
            emojis += WHITE_BOX
        index += 1
    return str(emojis)


def main(secret: str) -> None:
    """the entrypoint of program and main game loop"""
    turn: int = 1
    slen = len(secret)
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        gword = input_word(length=slen)
        emojis = emojified(gword=gword, sword=secret)
        print(emojis)
        if gword == secret:
            print(f"You won in {turn}/6 turns")
            return
        turn = turn + 1
    if turn >= 6:
        print("X/6 - Sorry, try again tomorrow!")
    return None


if __name__ == "__main__":
    main(secret="codes")
