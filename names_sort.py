#prints name of names.txt in alfabetical order

names = []
with open("names.txt") as file:         #default is "r"
    for line in file:
        names.append(line.rstrip())
for name in sorted(names):              # If you want in reverse order then , (names , reverse=True).
    print(f"Hello , {name}")

