
with open("students.csv") as file:
    for line in file:
        row=line.rstrip().split(",")
        print(f"{row[0]} lives in {row[1]}")git