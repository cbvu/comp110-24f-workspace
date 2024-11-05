def input_guess(secret_word_len: int) -> str:
    gword: str = input("Enter a 5 letter word: ")
    while len(gword) != secret_word_len:
        print(f"That wasn't {secret_word_len} chars! Try again: {gword}")
    if len(gword) == secret_word_len:
        print(gword)
    return gword
