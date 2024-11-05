"""concatenation function"""

__author__ = "730579512"


def concat(word1: str, word2: str) -> str:
    return word1 + word2


word1 = "happy"
word2 = "tuesday"
print(concat(word1, word2))

if __name__ == "__main__":
    concat(word1, word2)
