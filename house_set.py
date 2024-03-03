students = [
    {"name" : "Ram" , "house" : "red"},
    {"name" : "rita" , "house" : "green"},
    {"name" : "gita" , "house" : "red"},
    {"name" : "sita" , "house" : "blue"},
    {"name" : "syam" , "house" : "yellow"}
]

houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)