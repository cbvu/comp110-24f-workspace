"""tea party exercise"""

__author__: str = "730579512"


def tea_bags(people: int) -> int:
    """number of tea bags needed for party"""
    return people * 2


def treats(people: int) -> int:
    """number of treats needed for party"""
    return int(tea_bags(people=people) * 1.5)


# make sure that return is returning the right type of information
# if a function's parameters have been called in a previous function, it needs to be set equal to something when it's called


def cost(tea_count: int, treat_count: int) -> float:
    """cost of party"""
    return float((tea_count * 0.5) + (treat_count * 0.75))


# spaces should be put between signs and terms in expressions


def main_planner(guests: int) -> None:
    """entrypoint of program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print(
        "Cost: $" + str(cost(tea_count=tea_bags(guests), treat_count=(treats(guests))))
    )


# should make print commands on different lines to print different lines of text
# in order to print a function, the format is print(function(parameters))


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
