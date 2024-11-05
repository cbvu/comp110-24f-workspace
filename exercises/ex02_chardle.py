"""EX02 - Chardle - A cute step toward Wordle."""

__author__: str = "730579512"


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")
    if len(word) == 5:
        return word
    else:
        print("Error: Word must contain 5 characters." + "'" + word + "'")
        exit()


# should delete parts of functions that were once correct if autograder does odd things


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        return letter
        # must make sure there's always a return and the return is the same return type as specified in the function definition
        # exit can exist by itself and can come after return    return letter
    else:
        print("Error: Character must be a single character. " + letter)
        exit()


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    index: int = 0
    # must put count = 0 to start ocunt at beginning if word
    # index can be anything but counting must be specified in some way before it starts
    if word[0] == letter:
        print(letter + " found at index 0")
        index += 1
    if word[1] == letter:
        print(letter + " found at index 1")
        index += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        index += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        index += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        index += 1
    if (
        word[0] == letter
        or word[1] == letter
        or word[2] == letter
        or word[3] == letter
        or word[4] == letter
    ):
        # until you find a better way to do this this is how you ensure that this function is carried out if one of the above conditions is true
        if index < 2:
            print(str(index) + " instance of " + letter + " found in " + word)
        if index >= 2:
            print(str(index) + " instances of " + letter + " found in " + word)
    # you need to read every single letter of the assignment
    else:
        print("No instances of " + letter + " found in " + word)
    return None


# not every function needs an exit
# if you want to print something that combines info from multiple if statements you should put it at the same indentation of if and else below all of the ifs and elses


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())
    return None


if __name__ == "__main__":
    main()
# needed to make the function work
