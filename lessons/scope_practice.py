def remove_chars(msg: str, char: str) -> str:
    copy: str = ""
    index: int = 0
    while index < len(msg):
        if msg[index] != char:
            copy = copy + msg[index]
            index = index + 1
        else:
            copy = copy
            index = index + 1
    return copy


word: str = "yoyo"
# this line would show up in globals in memory diagram

print(remove_chars(word, "y"))
# makes msg = word and char = y
