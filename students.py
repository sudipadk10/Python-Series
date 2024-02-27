students = [] #Create empty list

with open("students.csv") as file:
    for line in file:
        name,house =line.rstrip().split(",")
        student = { "name": name , "house" : house}                    #Create a dictionary
        students.append(student)

def get_name(student):       #you can get house either, if you wanna sort by house alphabet.
    return student["name"]
    #using keey we can choose which variable have to be sorted.
for student in sorted(students , key=get_name , reverse= True):
    print(f"{student['name']} lives in {student['house']} ")