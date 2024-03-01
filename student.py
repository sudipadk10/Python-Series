def main():
    student=student_data()
    if student["name"] == "Sudip":
        student["house"]= "Ratuwamai"
    
    print(f"{student['name']} is from {student['house']}")

def student_data():
    name = input("Name :")
    house = input("House: ")
    return {"name": name, "house": house}  #Returning a dictionary.

if __name__ == "__main__":
    main()
    