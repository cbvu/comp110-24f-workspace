"""conditionals exercise"""

___author___ = "730579512"


def guess_a_number() -> None:
    x: int = int(input("Guess a number: "))
    print("Your guess was " + str(x))
    if secret == x:
        print("You got it!")
    elif secret > x:
        print(f"Your guess was too low! The secret number is {secret}")
    else:
        print(f"Your guess was too high! The secret number is {secret}")
    return None


secret: int = 7

if __name__ == "__main__":
    guess_a_number()
