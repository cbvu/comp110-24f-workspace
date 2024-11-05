my_numbers: list[float] = []  # literal
my_numbers.append(1.5)
print(my_numbers)

game_points: list[int] = [102, 96, 94, 94]
print(game_points)


def display(lt: list[int]) -> None:
    index: int = 0
    while index < len(lt):
        print(lt[index])
        index += 1


# function to print list
display(lt=game_points)
