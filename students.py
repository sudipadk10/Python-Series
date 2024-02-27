import csv
students = [] #Create empty list

with open("students.csv") as file:
    reader = csv.DictReader(file)   #distionary reader 
    for row in reader:
        students.append({"name":row["name"],"home": row["home"]})


    #using key we can choose which variable have to be sorted.
for student in sorted(students , key= lambda student: student["name"]):  #lambda is a annonomous func which has no name .
    print(f"{student['name']} lives in {student['home']}")