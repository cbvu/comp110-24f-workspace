"""wordle"""

__author__: str = "730579512"


def input_guess(secret_word_len: int) -> str:
    """prompts use for guess and ensure it's correct length"""
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    while len(guess) != secret_word_len:
        print(f"That wasn't {secret_word_len} chars! Try again: {guess}")
        guess = input(f"Enter a {secret_word_len} character word: ")
    return guess


# read every single character of the assignment
# dont restrict number of characters in word


def contains_char(sword: str, char: str) -> bool:
    """searching word for char to see if it's there or not"""
    assert len(char) == 1
    index: int = 0
    while len(sword) > index:
        if char == sword[index]:
            return True
        index = index + 1
    return False


# bool function needs return true and return false statements


def emojified(guess: str, sword: str) -> str:
    assert len(guess) == len(sword)
    index: int = 0
    emojis: str = ""

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while index < len(sword):
        char = guess[index]
        if guess[index] == sword[index]:
            emojis += GREEN_BOX
        elif contains_char(sword, char):
            emojis += YELLOW_BOX
        else:
            emojis += WHITE_BOX
        index += 1
    return str(emojis)


# do not make this too complicated if you cant see the top of the code it's probably wrong
def main(secret: str) -> None:
    """the entrypoint of program and main game loop"""
    turn: int = 1
    slen = len(secret)
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(secret_word_len=slen)
        emojis = emojified(guess=guess, sword=secret)
        print(emojis)
        if guess == secret:
            print(f"You won in {turn}/6 turns")
            return
        turn = turn + 1
    if turn >= 6:
        print("X/6 - Sorry, try again tomorrow!")
    return None


# to call functions you have to set each of the parameters equal to something that is defined within the function
# if there are weird errors with characters that print try to use fstring notation
if __name__ == "__main__":
    main(secret="codes")
