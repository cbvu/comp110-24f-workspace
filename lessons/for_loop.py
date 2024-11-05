pets: list[str] = ["Louie", "Bo", "Bear"]
p2: list[str] = []
for animal in pets:
    p2.append(f"Good boy, {animal}!")
print(p2)

i: int = 0
ys: list[int] = [110, 120]
while i < len(ys):
    y: int = ys[i]
    print(y)
    i += 1

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
n2: list[str] = []
index: int = 0
for index in range(0, len(names)):
    n2.append(f"{index}: {names[index]}")

print(n2)
